# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6"]
# ///
"""Reader builder tests on the toy topic (assembly always; HTML only if pandoc is installed).

Usage: uv run tools/tests/test_build_reader.py
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))
import build_reader  # noqa: E402
from topiclib import load_topic  # noqa: E402

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "toy-topic"
LABELS = build_reader.LABELS["es"]


class CitationTest(unittest.TestCase):
    def test_locator_is_literal(self):
        self.assertEqual(build_reader.normalize_citation("@a, L2.2, PDF p. 52"), "@a{}, L2.2, PDF p. 52")

    def test_second_locator_merges_into_previous_item(self):
        self.assertEqual(build_reader.normalize_citation("@a, L2.2, p. 53; L3.1, p. 76; @b, ¶4"),
                         "@a{}, L2.2, p. 53\\; L3.1, p. 76; @b{}, ¶4")

    def test_key_without_locator(self):
        self.assertEqual(build_reader.normalize_citation("@a; @b"), "@a; @b")

    def test_block_with_inner_brackets(self):
        out = build_reader.convert_citations("Texto [@a, p. 197 [185]; ej. 1, p. 201 [189]].", LABELS)
        self.assertEqual(out, "Texto [@a{}, p. 197 [185]\\; ej. 1, p. 201 [189]].")

    def test_unverified_becomes_label(self):
        out = build_reader.convert_citations("Algo [unverified].", LABELS)
        self.assertIn("[sin verificar]{.unverified}", out)


class AssemblyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.t = load_topic(FIXTURE)
        self.linker = build_reader.Linker(self.t, "es")

    def md(self, layer: int) -> str:
        return build_reader.layer_markdown(self.t, "es", layer, self.linker, LABELS)

    def test_layer_1_has_only_concepts_from_layer_1(self):
        md = self.md(1)
        self.assertIn("{#c-light}", md)
        self.assertNotIn("{#c-hue}", md)  # hue starts at layer 2

    def test_bridge_text_opens_the_domain(self):
        md = self.md(2)
        self.assertLess(md.index("Qué se ve en la capa 2"), md.index("{#c-light}"))

    def test_prerequisites_are_added(self):
        self.assertIn("Antes conviene: [Luz (light)](#c-light).", self.md(2))

    def test_check_goes_before_next(self):
        md = self.md(1)
        self.assertLess(md.index("### Compruébalo"), md.index("### Para seguir"))
        self.assertIn("**b)** Radiación electromagnética visible", md)

    def test_links_point_to_layer_documents(self):
        md1, md2 = self.md(1), self.md(2)
        self.assertIn("[matiz](layer-2.html#c-hue)", md1)      # concept not in layer 1
        self.assertIn("[matiz](#c-hue)", md2)                  # same document
        self.assertIn("[capa profesional](layer-3.html#c-light)", md2)  # own later layer

    def test_images_resolve_to_files(self):
        md = self.md(2)
        self.assertIn(str((FIXTURE / "assets" / "diagrams" / "wheel.es.svg").resolve()), md)

    @unittest.skipUnless(shutil.which("pandoc"), "pandoc not installed")
    def test_html_build(self):
        out = Path(tempfile.mkdtemp())
        try:
            res = subprocess.run([sys.executable, str(TOOLS / "build_reader.py"), str(FIXTURE), "--out", str(out)],
                                 capture_output=True, text=True)
            self.assertEqual(res.returncode, 0, res.stderr + res.stdout)
            html = (out / "layer-1.html").read_text(encoding="utf-8").replace("\xa0", " ")
            self.assertIn('class="footnote-ref"', html)
            self.assertIn("Jane Doe, 2020, p. 1.", html)
            self.assertNotIn("p. p. 1", html)
            layer3 = (out / "layer-3.html").read_text(encoding="utf-8").replace("\xa0", " ")
            self.assertIn("Jane Doe, 2020, pp. 4-5.", layer3)
            self.assertTrue((out / "index.html").exists())
            md = (out / "layer-1.md").read_text(encoding="utf-8").replace("\xa0", " ")
            self.assertTrue(md.startswith("# "))                  # title first
            self.assertIn("[^2]: Jane Doe, 2020, p. 1.", md)    # numbered note
            self.assertIn("## Fuentes", md)
            self.assertNotIn("@", md.split("## Fuentes")[0])     # no raw citation keys
            self.assertNotIn("<div", md)
            self.assertIn('<a id="c-light"></a>', md)            # link target kept
            self.assertIn("(layer-2.md#c-hue)", md)
        finally:
            shutil.rmtree(out)


if __name__ == "__main__":
    unittest.main(verbosity=1)
