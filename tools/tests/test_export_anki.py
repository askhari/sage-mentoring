# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6", "genanki==0.13.1"]
# ///
"""Anki exporter tests on the toy topic.

Usage: uv run tools/tests/test_export_anki.py
"""

from __future__ import annotations

import json
import sqlite3
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))
import export_anki  # noqa: E402
from topiclib import load_topic  # noqa: E402

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "toy-topic"


def notes_by_id(package) -> dict:
    return {n.fields[0]: n for d in package.decks for n in d.notes}


class ExportAnkiTest(unittest.TestCase):
    def setUp(self) -> None:
        self.topic = load_topic(FIXTURE)
        self.package = export_anki.build_package(self.topic, "es")
        self.notes = notes_by_id(self.package)

    def field(self, qid: str, name: str) -> str:
        return self.notes[qid].fields[export_anki.FIELDS.index(name)]

    def test_all_questions_exported(self) -> None:
        self.assertEqual(set(self.notes), {q["id"] for q in self.topic.all_questions()})

    def test_single_choice(self) -> None:
        self.assertIn("<b>a)</b> Un sonido", self.field("q-light-001", "Options"))
        self.assertIn("b) Radiación electromagnética visible", self.field("q-light-001", "Answer"))
        self.assertEqual(self.field("q-light-001", "Explanation"), "Explicación.")

    def test_short_answer(self) -> None:
        self.assertIn("espectro", self.field("q-light-002", "Answer"))
        self.assertEqual(self.field("q-light-002", "Options"), "")

    def test_open_and_case_have_model_answer_and_rubric(self) -> None:
        for qid, item in (("q-hue-001", "Menciona Y"), ("q-hue-002", "Menciona Z")):
            self.assertEqual(self.field(qid, "Answer"), "Respuesta modelo.")
            self.assertIn(f"<li>{item}</li>", self.field(qid, "Rubric"))

    def test_context_names_concept_and_sources_without_paths(self) -> None:
        ctx = self.field("q-hue-001", "Context")
        self.assertIn("Matiz (hue)", ctx)
        self.assertIn("Capa 2 (Comprensión)", ctx)
        self.assertNotIn("http", ctx)
        self.assertNotIn(".md", ctx)
        src = self.field("q-hue-001", "Sources")
        self.assertIn("Jane Doe (2020)", src)
        self.assertIn("ISBN: 000-0-000-00000-0", src)

    def test_tags(self) -> None:
        self.assertEqual(sorted(self.notes["q-light-003"].tags), sorted([
            "sage::toy-topic::domain::basics", "sage::toy-topic::layer::3",
            "sage::toy-topic::concept::light", "sage::toy-topic::type::case",
            "sage::toy-topic::source::src-a"]))

    def test_deck_names(self) -> None:
        self.assertEqual([d.name for d in self.package.decks], ["Tema de juguete::1 Lo básico"])

    def test_ids_are_stable(self) -> None:
        again = notes_by_id(export_anki.build_package(load_topic(FIXTURE), "es"))
        self.assertEqual({k: n.guid for k, n in self.notes.items()},
                         {k: n.guid for k, n in again.items()})
        self.assertEqual(len({n.guid for n in self.notes.values()}), len(self.notes))
        self.assertEqual(export_anki.stable_id("toy-topic", "es", "model"),
                         self.package.decks[0].notes[0].model.model_id)

    def test_types_filter(self) -> None:
        package = export_anki.build_package(self.topic, "es", types=("single-choice",))
        self.assertEqual(set(notes_by_id(package)), {"q-light-001"})

    def test_text_is_escaped(self) -> None:
        self.assertEqual(export_anki.text("a < b\nc"), "a &lt; b<br>c")

    def test_written_package_has_no_learner_data(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "toy.apkg"
            export_anki.main([str(FIXTURE), "--out", str(out)])
            with zipfile.ZipFile(out) as zf:
                self.assertEqual(json.loads(zf.read("media")), {})
                zf.extract("collection.anki2", tmp)
            db = sqlite3.connect(Path(tmp) / "collection.anki2")
            rows = db.execute("select flds from notes").fetchall()
            db.close()
            self.assertEqual(len(rows), 5)
            self.assertFalse(any("learners" in r[0] or "attempts" in r[0] for r in rows))


if __name__ == "__main__":
    unittest.main()
