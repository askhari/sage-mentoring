# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6", "genanki==0.13.1"]
# ///
"""Export a topic's question bank to an Anki deck (.apkg).

Usage:
  uv run tools/export_anki.py <topic> [--lang es] [--types single-choice,short-answer,open,case]
                              [--out exports/anki/<topic>.<lang>.apkg]

Only reads topics/ (never learners/): the deck carries no personal progress.
Note GUIDs are derived from (topic, lang, question id), so re-importing an updated
deck updates the existing notes instead of duplicating them. The first note field,
QuestionId, links Anki reviews back to the question bank.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import sys
from pathlib import Path

import genanki

sys.path.insert(0, str(Path(__file__).resolve().parent))
from topiclib import ROOT, Topic, load_topic, load_yaml, resolve_topic  # noqa: E402

TYPES = ("single-choice", "short-answer", "open", "case")
FIELDS = ["QuestionId", "Prompt", "Options", "Answer", "Explanation", "Rubric",
          "Context", "Sources", "Type"]

# Card UI strings, per content language.
LABELS = {
    "es": {
        "also": "También vale",
        "rubric": "Comprueba que tu respuesta:",
        "concept": "Concepto",
        "layer": "Capa",
        "sources": "Fuentes",
    },
}

FRONT = """<div class="prompt">{{Prompt}}</div>
{{#Options}}<div class="options">{{Options}}</div>{{/Options}}"""

BACK = """{{FrontSide}}
<hr id="answer">
<div class="answer">{{Answer}}</div>
{{#Explanation}}<div class="explanation">{{Explanation}}</div>{{/Explanation}}
{{#Rubric}}<div class="rubric">{{Rubric}}</div>{{/Rubric}}
<div class="meta">{{Context}}<br>{{Sources}}</div>"""

CSS = """.card { font-family: -apple-system, "Helvetica Neue", Arial, sans-serif; font-size: 19px;
  text-align: left; line-height: 1.45; color: #1d1d1f; background: #fff; max-width: 42em; margin: 0 auto; }
.nightMode.card, .night_mode .card { color: #eee; background: #1e1e1e; }
.prompt { font-weight: 600; }
.options ol { list-style: none; padding-left: 0; }
.options li { margin: .35em 0; }
.answer { margin: .6em 0; }
.answer .correct { color: #1a7f37; font-weight: 600; }
.nightMode .answer .correct, .night_mode .answer .correct { color: #4ac26b; }
.explanation { margin: .6em 0; }
.rubric ul { margin: .3em 0; }
.meta { margin-top: 1.2em; font-size: 14px; opacity: .7; }
"""


def stable_id(*parts: str) -> int:
    """Deterministic id in the range Anki/genanki expect for models and decks."""
    digest = hashlib.sha256("/".join(("sage-mentoring",) + parts).encode()).digest()
    return (1 << 30) + int.from_bytes(digest[:4], "big") % (1 << 30)


def text(value) -> str:
    """Escape plain text for a card field, keeping line breaks."""
    return html.escape(str(value).strip()).replace("\n", "<br>")


def source_ref(src: dict) -> str:
    authors = ", ".join(src.get("authors") or [])
    head = f"{text(authors)} ({src.get('year', 's. f.')}). " if authors else ""
    ref = f"{head}<i>{text(src.get('title', src.get('id')))}</i>"
    ids = src.get("identifiers") or {}
    if ids.get("url"):
        url = html.escape(ids["url"], quote=True)
        ref += f'. <a href="{url}">{url}</a>'
    elif ids.get("doi"):
        ref += f". DOI: {text(ids['doi'])}"
    elif ids.get("isbn"):
        ref += f". ISBN: {text(ids['isbn'])}"
    return ref


def build_model(topic: Topic, lang: str) -> genanki.Model:
    return genanki.Model(
        stable_id(topic.id, lang, "model"),
        f"Sage Mentoring ({topic.id}, {lang})",
        fields=[{"name": f} for f in FIELDS],
        templates=[{"name": "Card", "qfmt": FRONT, "afmt": BACK}],
        css=CSS,
        sort_field_index=0,
    )


def note_fields(q: dict, t: dict, lab: dict, concept_title: str, layer_name: str,
                domain_title: str, sources: dict) -> list[str]:
    options = answer = explanation = rubric = ""
    qtype = q["type"]
    if qtype == "single-choice":
        opts = t.get("options") or {}
        options = "<ol>" + "".join(
            f"<li><b>{text(k)})</b> {text(v)}</li>" for k, v in opts.items()) + "</ol>"
        correct = q.get("correct")
        answer = f'<span class="correct">{text(correct)}) {text(opts.get(correct, ""))}</span>'
        explanation = text(t.get("explanation", "")) if t.get("explanation") else ""
    elif qtype == "short-answer":
        accepted = [str(a) for a in t.get("accepted") or []]
        answer = f'<span class="correct">{text(accepted[0])}</span>' if accepted else ""
        if len(accepted) > 1:
            answer += f"<br>{lab['also']}: " + ", ".join(text(a) for a in accepted[1:])
        explanation = text(t["explanation"]) if t.get("explanation") else ""
    else:  # open, case
        answer = text(t.get("model_answer", ""))
        items = t.get("rubric") or []
        if items:
            rubric = (f"{lab['rubric']}<ul>"
                      + "".join(f"<li>{text(i)}</li>" for i in items) + "</ul>")
    context = (f"{lab['concept']}: <b>{text(concept_title)}</b> · {text(domain_title)} · "
               f"{lab['layer']} {q['layer']} ({text(layer_name)}) · {text(q['id'])}")
    refs = [source_ref(sources[s]) if s in sources else text(s) for s in q.get("sources") or []]
    src_html = f"{lab['sources']}: " + "; ".join(refs) if refs else ""
    return [q["id"], text(t.get("prompt", "")), options, answer, explanation, rubric,
            context, src_html, qtype]


def tags_for(topic: Topic, q: dict, domain: str) -> list[str]:
    base = f"sage::{topic.id}"
    tags = [f"{base}::domain::{domain}", f"{base}::layer::{q['layer']}",
            f"{base}::concept::{q['concept']}", f"{base}::type::{q['type']}"]
    tags += [f"{base}::source::{s}" for s in q.get("sources") or []]
    return tags


def build_package(topic: Topic, lang: str, types=TYPES) -> genanki.Package:
    lab = LABELS.get(lang)
    if lab is None:
        raise SystemExit(f"no card labels for language '{lang}' (add them to LABELS)")
    meta = load_yaml(topic.lang_dir(lang) / "topic.yaml", {}) or {}
    titles = {c["id"]: c.get("title", c["id"])
              for c in load_yaml(topic.lang_dir(lang) / "concepts.yaml", []) or []}
    layer_names = {int(k): v for k, v in (meta.get("layers") or {}).items()}
    domain_titles = meta.get("domains") or {}
    sources = {s["id"]: s for s in topic.sources if isinstance(s, dict) and "id" in s}
    texts = topic.lang_questions(lang)
    model = build_model(topic, lang)
    root = meta.get("title", topic.id)

    missing = [q["id"] for q in topic.all_questions() if q["id"] not in texts]
    if missing:
        raise SystemExit(f"missing '{lang}' text for: {', '.join(missing)}")

    decks = []
    for i, domain in enumerate(topic.domains, 1):
        deck = genanki.Deck(stable_id(topic.id, lang, "deck", domain),
                            f"{root}::{i} {domain_titles.get(domain, domain)}")
        for q in topic.questions.get(domain, []):
            if q["type"] not in types:
                continue
            fields = note_fields(q, texts[q["id"]], lab, titles.get(q["concept"], q["concept"]),
                                 layer_names.get(int(q["layer"]), ""),
                                 domain_titles.get(domain, domain), sources)
            deck.add_note(genanki.Note(
                model=model, fields=fields, tags=tags_for(topic, q, domain),
                guid=genanki.guid_for("sage-mentoring", topic.id, lang, q["id"])))
        if deck.notes:
            decks.append(deck)
    return genanki.Package(decks)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("topic")
    ap.add_argument("--lang", default=None, help="content language (default: first of topic.yaml)")
    ap.add_argument("--types", default=",".join(TYPES),
                    help="comma-separated question types to include")
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args(argv)

    topic = load_topic(resolve_topic(args.topic))
    lang = args.lang or (topic.languages or ["es"])[0]
    types = tuple(t.strip() for t in args.types.split(",") if t.strip())
    unknown = set(types) - set(TYPES)
    if unknown:
        ap.error(f"unknown types: {', '.join(sorted(unknown))}")
    out = args.out or ROOT / "exports" / "anki" / f"{topic.id}.{lang}.apkg"
    out.parent.mkdir(parents=True, exist_ok=True)

    package = build_package(topic, lang, types)
    package.write_to_file(str(out))
    n = sum(len(d.notes) for d in package.decks)
    print(f"{out}: {n} notes in {len(package.decks)} decks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
