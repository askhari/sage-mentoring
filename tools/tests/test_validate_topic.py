# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6"]
# ///
"""Validator tests: break a copy of the toy topic on purpose and check the error is caught.

Usage: uv run tools/tests/test_validate_topic.py
"""

from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))
import validate_topic  # noqa: E402

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "toy-topic"


class ValidatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())
        self.topic = self.tmp / "toy-topic"
        shutil.copytree(FIXTURE, self.topic)

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp)

    def edit(self, rel: str, old: str, new: str) -> None:
        path = self.topic / rel
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text, f"fixture text not found in {rel}")
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def errors(self, stage: str = "final") -> str:
        return "\n".join(validate_topic.validate(self.topic, stage).errors)

    def assertCaught(self, fragment: str, stage: str = "final") -> None:
        errs = self.errors(stage)
        self.assertIn(fragment, errs, f"expected error containing '{fragment}', got:\n{errs}")

    def test_fixture_is_valid(self):
        self.assertEqual(self.errors(), "")

    def test_citation_to_unknown_source(self):
        self.edit("i18n/es/domains/basics/concepts/light.md", "[@src-a, p. 1]", "[@ghost-2020, p. 1]")
        self.assertCaught("citation '@ghost-2020' not in sources.yaml")

    def test_missing_question_text(self):
        self.edit("i18n/es/questions/basics.yaml", "- id: q-hue-002", "- id: q-hue-999")
        errs = self.errors()
        self.assertIn("missing text for 'q-hue-002'", errs)
        self.assertIn("'q-hue-999' not in questions/basics.yaml", errs)

    def test_unknown_prerequisite(self):
        self.edit("concepts.yaml", "prerequisites: [light]", "prerequisites: [darkness]")
        self.assertCaught("prerequisite 'darkness' does not exist", stage="map")

    def test_prerequisite_cycle(self):
        self.edit("concepts.yaml", "  prerequisites: []", "  prerequisites: [hue]")
        self.assertCaught("prerequisite cycle", stage="map")

    def test_missing_layer_section(self):
        self.edit("i18n/es/domains/basics/concepts/light.md", "## Profesional {#layer-3}", "## Profesional")
        self.assertCaught("missing section {#layer-3}")

    def test_section_below_first_layer(self):
        self.edit("i18n/es/domains/basics/concepts/hue.md", "## Comprensión {#layer-2}",
                  "## Fundamentos {#layer-1}\nx\n\n## Comprensión {#layer-2}")
        self.assertCaught("section layer-1 is below first_layer 2")

    def test_question_below_first_layer(self):
        self.edit("questions/basics.yaml", "concept: hue\n  layer: 2", "concept: hue\n  layer: 1")
        self.assertCaught("layer 1 is below concept first_layer 2")

    def test_correct_option_missing(self):
        self.edit("questions/basics.yaml", "correct: b", "correct: z")
        self.assertCaught("correct option 'z' not in options")

    def test_open_question_without_rubric(self):
        self.edit("i18n/es/questions/basics.yaml", '  rubric: ["Menciona Y"]\n', "")
        self.assertCaught("'q-hue-001' needs 'rubric'")

    def test_third_party_image_without_license(self):
        self.edit("assets.yaml", "origin: own", "origin: third-party")
        self.edit("assets.yaml", "license: CC-BY-4.0", "license: all-rights-reserved")
        errs = self.errors()
        self.assertIn("is not shareable", errs)
        self.assertIn("third-party asset missing 'author'", errs)

    def test_missing_image_file(self):
        (self.topic / "assets/diagrams/wheel.es.svg").unlink()
        errs = self.errors()
        self.assertIn("file 'assets/diagrams/wheel.es.svg' not found", errs)
        self.assertIn("image '../../../../../assets/diagrams/wheel.es.svg' not found", errs)

    def test_external_image(self):
        self.edit("i18n/es/domains/basics/concepts/hue.md",
                  "../../../../../assets/diagrams/wheel.es.svg", "https://example.com/x.png")
        self.assertCaught("external image")

    def test_missing_alt_text(self):
        self.edit("i18n/es/assets.yaml", "- id: wheel", "- id: other")
        self.assertCaught("missing alt text for 'wheel'")

    def test_note_for_unknown_source(self):
        (self.topic / "research/notes/src-b.md").write_text("---\nsource: src-b\n---\n", encoding="utf-8")
        self.assertCaught("source 'src-b' not in sources.yaml", stage="map")

    def test_stale_layer_index(self):
        self.edit("i18n/es/domains/basics/concepts/hue.md", 'title: "Matiz (hue)"', 'title: "Tono"')
        self.assertCaught("out of date")

    def test_bad_source_reliability(self):
        self.edit("sources.yaml", "reliability: A", "reliability: D")
        self.assertCaught("reliability must be A, B or C", stage="map")

    def test_topic_id_mismatch(self):
        self.edit("topic.yaml", "id: toy-topic", "id: other-topic")
        self.assertCaught("does not match folder", stage="map")


    def test_missing_build_plan(self):
        (self.topic / "research/plan.md").unlink()
        self.assertCaught("research/plan.md: missing", stage="map")

    def test_missing_layer_name_at_map_stage(self):
        self.edit("i18n/es/topic.yaml", '  3: "Profesional"\n', "")
        self.assertCaught("missing layers name for 3", stage="map")

    def test_missing_domain_title(self):
        self.edit("i18n/es/topic.yaml", '  basics: "Lo básico"', '  other: "Otro"')
        errs = self.errors("map")
        self.assertIn("missing title for domain 'basics'", errs)
        self.assertIn("domain 'other' not in topic.yaml", errs)

    def test_missing_concept_title(self):
        self.edit("i18n/es/concepts.yaml", "- id: hue", "- id: ghost")
        errs = self.errors("map")
        self.assertIn("missing title for 'hue'", errs)
        self.assertIn("'ghost' not in concepts.yaml", errs)

    def test_missing_concept_titles_file(self):
        (self.topic / "i18n/es/concepts.yaml").unlink()
        self.assertCaught("i18n/es/concepts.yaml: missing", stage="map")

    def test_concept_file_title_mismatch(self):
        self.edit("i18n/es/concepts.yaml", 'title: "Matiz (hue)"', 'title: "Tono"')
        self.assertCaught("title differs from i18n/es/concepts.yaml")

    def test_domain_index_title_mismatch(self):
        self.edit("i18n/es/topic.yaml", '  basics: "Lo básico"', '  basics: "Básico"')
        self.assertCaught("title differs from i18n/es/topic.yaml domains.basics")

    def test_source_notes_must_be_text(self):
        self.edit("sources.yaml", "reliability: A", "reliability: A\n  notes: [x]")
        self.assertCaught("notes must be a string", stage="map")

    def warnings(self, stage: str = "final") -> str:
        return "\n".join(validate_topic.validate(self.topic, stage).warnings)

    def test_note_without_arrows(self):
        self.edit("research/notes/src-a.md", "(p. 1) → light", "(p. 1)")
        self.edit("research/notes/src-a.md", "(p. 2) → hue", "(p. 2)")
        self.assertIn("no '→ <concept-id>' bullets", self.warnings("map"))

    def test_note_frontmatter_concept_without_bullet(self):
        self.edit("research/notes/src-a.md", "(p. 2) → hue", "(p. 2)")
        self.assertIn("concept 'hue' in frontmatter has no '→ hue' bullet", self.warnings("map"))

    def test_note_bullet_to_unknown_concept(self):
        self.edit("research/notes/src-a.md", "(p. 2) → hue", "(p. 2) → ghost")
        self.assertCaught("bullet points to unknown concept 'ghost'", stage="map")

    def test_note_arrow_list(self):
        self.edit("research/notes/src-a.md", "(p. 1) → light", "(p. 1) → light, hue")
        self.edit("research/notes/src-a.md", "(p. 2) → hue", "(p. 2)")
        self.assertNotIn("has no '→ hue' bullet", self.warnings("map"))

    def test_note_arrow_inside_claim_ignored(self):
        self.edit("research/notes/src-a.md", "(p. 2) → hue", "blue+yellow→ghost mix (p. 2) → hue")
        self.assertNotIn("unknown concept 'ghost'", self.errors("map"))
        self.assertNotIn("has no '→ hue' bullet", self.warnings("map"))

    def test_note_arrow_with_trailing_remark(self):
        self.edit("research/notes/src-a.md", "(p. 2) → hue", "(p. 2) → hue (TOC only)")
        self.assertNotIn("has no '→ hue' bullet", self.warnings("map"))

    def test_broken_concept_link_is_a_warning(self):
        self.edit("i18n/es/domains/basics/concepts/hue.md",
                  "Aplicación [@src-a, pp. 4-5].",
                  "Aplicación [@src-a, pp. 4-5]. Ver [luz](light.md) y [nada](../../other/concepts/missing.md#layer-2).")
        warns = self.warnings()
        self.assertIn("link '../../other/concepts/missing.md' not found", warns)
        self.assertNotIn("link 'light.md'", warns)
        self.assertNotIn("missing.md", self.errors())

    # Layer template (format: 2)
    LIGHT = "i18n/es/domains/basics/concepts/light.md"

    def test_template_missing_required_subsection(self):
        self.edit(self.LIGHT, "### Ejemplo\nUn caso [@src-a, p. 2].\n\n", "")
        self.assertCaught("#layer-2: missing subsection '### Ejemplo'")

    def test_template_unknown_subsection(self):
        self.edit(self.LIGHT, "### Errores frecuentes", "### Curiosidades")
        self.assertCaught("unknown subsection '### Curiosidades'")

    def test_template_out_of_order(self):
        self.edit(self.LIGHT, "### Idea clave\nLa luz es radiación electromagnética visible [@src-a, p. 1].\n\n"
                              "### Explicación\nLa luz… [@src-a, p. 1].",
                  "### Explicación\nLa luz… [@src-a, p. 1].\n\n"
                  "### Idea clave\nLa luz es radiación electromagnética visible [@src-a, p. 1].")
        self.assertCaught("#layer-1: subsections out of order")

    def test_template_forward_concept_link(self):
        self.edit(self.LIGHT, "La luz… [@src-a, p. 1].", "La luz y el [matiz](hue.md) [@src-a, p. 1].")
        self.assertCaught("layer-1 links to 'hue', which starts at layer 2")

    def test_template_forward_layer_anchor(self):
        self.edit(self.LIGHT, "Más detalle [@src-a, p. 2]. Se", "Más detalle [@src-a, p. 2]. Ver [aquí](#layer-3). Se")
        self.assertCaught("layer-2 links to a later section #layer-3")

    def test_template_forward_link_allowed_in_next(self):
        errs = self.errors()
        self.assertNotIn("links to", errs)  # 'next' of layers 1 and 2 points ahead on purpose

    def test_template_mid_sentence_citation_warns(self):
        self.edit(self.LIGHT, "La luz… [@src-a, p. 1].", "La luz [@src-a, p. 1] es visible.")
        self.assertIn("1 citation(s) in the middle of a sentence", self.warnings())
        self.assertEqual(self.errors(), "")

    def test_template_citation_in_table_cell_is_fine(self):
        self.edit(self.LIGHT, "La luz… [@src-a, p. 1].", "| a | b |\n|---|---|\n| luz [@src-a, p. 1] | x |")
        self.assertNotIn("middle of a sentence", self.warnings())

    def test_template_long_key_idea_warns(self):
        self.edit(self.LIGHT, "Aplicación [unverified].\n\n### Explicación",
                  " ".join(["palabra"] * 70) + " [unverified].\n\n### Explicación")
        self.assertIn("key idea has 71 words", self.warnings())

    def test_template_missing_domain_bridge(self):
        self.edit("i18n/es/domains/basics/index.md", "## Comprensión {#layer-2}\nQué se ve en la capa 2 [@src-a].\n", "")
        self.assertCaught("missing bridge section {#layer-2}")

    def test_template_old_format_warns(self):
        self.assertIn("1 concept file(s) in the old format", self.warnings())

if __name__ == "__main__":
    unittest.main(verbosity=1)
