# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6"]
# ///
"""Build the reading version of a topic: one HTML document and one clean Markdown file per layer.

Usage: uv run tools/build_reader.py <topic-id-or-path> [--lang es] [--layer N] [--out DIR] [--keep-source]

Output (default): exports/reader/<topic>/<lang>/{index,layer-1,layer-2,layer-3}.{html,md}
The .md files are GitHub-flavoured Markdown with numbered notes and a sources section.

The script writes no content of its own: it assembles the pieces already written
(domain bridge texts, the layer section of each concept), adds "Antes conviene"
from concepts.yaml and "Compruébalo" from the question bank, turns citations into
footnotes with a bibliography, and renders with pandoc (>= 3). See docs/format.md.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from topiclib import (  # noqa: E402
    IMAGE_RE, LAYERS, MD_LINK_RE, ROOT, Topic, layer_bodies, load_topic,
    load_yaml, resolve_topic, section_names, split_frontmatter, subsections,
)

READER_DIR = Path(__file__).resolve().parent / "reader"

# Texts the script adds itself; a new language needs its entry.
LABELS = {
    "es": {
        "prereq": "Antes conviene",
        "check": "Compruébalo",
        "answer": "Ver respuesta",
        "accepted": "Respuestas aceptadas",
        "model": "Respuesta modelo",
        "rubric": "Comprueba que tu respuesta:",
        "unverified": "sin verificar",
        "references": "Fuentes",
        "contents": "Contenido",
        "overview": "Orientación",
        "layer_of": "capa",
    },
}

SOURCE_TYPES = {"textbook": "book", "course": "webpage", "standard": "standard",
                "paper": "article-journal", "docs": "webpage", "article": "article"}
CHECK_TYPE_ORDER = {"single-choice": 0, "short-answer": 1, "open": 2, "case": 3}
MAX_CHECK_QUESTIONS = 2


# ---------- sources and citations ----------

def csl_items(t: Topic) -> list[dict]:
    items = []
    for s in t.sources:
        if not isinstance(s, dict) or "id" not in s:
            continue
        item = {"id": s["id"], "type": SOURCE_TYPES.get(s.get("type"), "book"),
                "title": s.get("title", s["id"]),
                "author": [{"literal": a} for a in (s.get("authors") or [])]}
        year = re.search(r"\d{4}", str(s.get("year", "")))
        if year:
            item["issued"] = {"date-parts": [[int(year.group())]]}
        ids = s.get("identifiers") or {}
        for key, csl in (("url", "URL"), ("doi", "DOI"), ("isbn", "ISBN")):
            if ids.get(key):
                item[csl] = str(ids[key])
        items.append(item)
    return items


# A citation block; allows one level of brackets inside, as in "p. 197 [185]" (printed page).
CITATION_BLOCK_RE = re.compile(r"\[((?:[^\[\]]|\[[^\[\]]*\])*@(?:[^\[\]]|\[[^\[\]]*\])*)\]")
CITE_ITEM_RE = re.compile(r"^(?P<prefix>.*?)(?P<key>-?@[a-z0-9][a-z0-9-]*)(?P<rest>.*)$", re.DOTALL)


def normalize_citation(block: str) -> str:
    """'@a, L2.2, PDF p. 53; L3.1, p. 76; @b, ¶4' -> '@a{}, L2.2, PDF p. 53\\; L3.1, p. 76; @b{}, ¶4'.

    Locators become literal suffixes, and parts without a key (a second locator of the
    same source) are merged into the previous item.
    """
    items: list[list[str]] = []  # [prefix, key, locator]
    for part in block.split(";"):
        m = CITE_ITEM_RE.match(part)
        if m:
            loc = m.group("rest").strip()
            loc = loc[1:].strip() if loc.startswith(",") else loc
            items.append([m.group("prefix").strip(), m.group("key"), loc])
        elif items:
            # escaped, or pandoc would read the part without a key as a broken citation item
            items[-1][2] = f"{items[-1][2]}\\; {part.strip()}" if items[-1][2] else part.strip()
    out = []
    for prefix, key, loc in items:
        loc = loc.replace("{", "(").replace("}", ")")
        piece = f"{prefix} {key}".strip()
        # '@key{}, text': empty locator, so pandoc keeps the text as a literal suffix
        # (otherwise it parses labels: "vol. 3" -> "vols. 3", "§5.2" -> "párr. 5.2").
        out.append(f"{piece}{{}}, {loc}" if loc else piece)
    return "; ".join(out)


def convert_citations(text: str, labels: dict) -> str:
    text = CITATION_BLOCK_RE.sub(lambda m: f"[{normalize_citation(m.group(1))}]", text)
    return text.replace("[unverified]", f"[{labels['unverified']}]{{.unverified}}")


# ---------- links and images ----------

class Linker:
    """Rewrites links between topic files so they point into the layer documents."""

    def __init__(self, t: Topic, lang: str) -> None:
        self.t = t
        self.concepts = t.concept_map()
        self.ldir = t.lang_dir(lang).resolve()
        self.domain_first = {}
        for c in t.concepts:
            d, f = c.get("domain"), int(c.get("first_layer", 1))
            self.domain_first[d] = min(self.domain_first.get(d, 3), f)

    def concept_target(self, cid: str, layer: int, current: int) -> str:
        first = int(self.concepts[cid].get("first_layer", 1))
        target = max(layer, first)
        return f"#c-{cid}" if target == current else f"layer-{target}.html#c-{cid}"

    def domain_target(self, domain: str, current: int) -> str:
        first = self.domain_first.get(domain, 1)
        target = current if current >= first else first
        return f"#d-{domain}" if target == current else f"layer-{target}.html#d-{domain}"

    def rewrite(self, text: str, source: Path, current: int, self_concept: str | None = None) -> str:
        def link(m: re.Match) -> str:
            whole, ref, anchor = m.group(0), m.group(1), m.group(2) or ""
            if ref.startswith(("http://", "https://", "mailto:")):
                return whole
            if ref and not ref.endswith(".md"):
                return whole
            target = (source.parent / ref).resolve() if ref else source.resolve()
            new = self.resolve(target, anchor, current, self_concept)
            if new is None:
                return whole
            return whole[: whole.rindex("(")] + f"({new})"

        def image(m: re.Match) -> str:
            ref = m.group(1)
            if ref.startswith(("http://", "https://")):
                return m.group(0)
            return m.group(0).replace(ref, str((source.parent / ref).resolve()))

        text = MD_LINK_RE.sub(link, text)
        return IMAGE_RE.sub(image, text)

    def resolve(self, target: Path, anchor: str, current: int, self_concept: str | None) -> str | None:
        m = re.fullmatch(r"#layer-(\d)", anchor)
        layer = int(m.group(1)) if m else current
        try:
            rel = target.relative_to(self.ldir)
        except ValueError:
            return None
        parts = rel.parts
        if len(parts) == 4 and parts[0] == "domains" and parts[2] == "concepts":
            cid = target.stem
            if cid in self.concepts:
                return self.concept_target(cid, layer, current)
        if len(parts) == 3 and parts[0] == "domains" and parts[2] == "index.md":
            return self.domain_target(parts[1], current)
        if len(parts) == 2 and parts[0] == "layers":
            return target.stem + ".html"
        if parts == ("overview.md",):
            return "index.html"
        return None


# ---------- question bank ----------

def check_block(t: Topic, qtext: dict, cid: str, layer: int, labels: dict) -> str:
    qs = [q for q in t.all_questions()
          if q.get("concept") == cid and int(q.get("layer", 0)) == layer and q.get("id") in qtext]
    qs.sort(key=lambda q: (CHECK_TYPE_ORDER.get(q.get("type"), 9), q["id"]))
    qs = qs[:MAX_CHECK_QUESTIONS]
    if not qs:
        return ""
    out = ['::: check', f"### {labels['check']}", ""]
    for i, q in enumerate(qs, 1):
        txt = qtext[q["id"]]
        out += [f"{i}. {' '.join(str(txt.get('prompt', '')).split())}", ""]
        opts = txt.get("options") or {}
        for k, v in opts.items():
            out.append(f"    - **{k})** {v}")
        if opts:
            out.append("")
        out.append(f"    <details><summary>{labels['answer']}</summary>")
        out.append("")
        if q.get("type") == "single-choice" and q.get("correct") in opts:
            out.append(f"    **{q['correct']})** {opts[q['correct']]}")
            if txt.get("explanation"):
                out += ["", f"    {txt['explanation'].strip()}"]
        elif txt.get("accepted"):
            out.append(f"    {labels['accepted']}: " + ", ".join(f"*{a}*" for a in txt["accepted"]))
            if txt.get("explanation"):
                out += ["", f"    {txt['explanation'].strip()}"]
        else:
            if txt.get("model_answer"):
                out.append("    " + " ".join(str(txt["model_answer"]).split()))
            if txt.get("rubric"):
                out += ["", f"    {labels['rubric']}", ""]
                out += [f"    - {r}" for r in txt["rubric"]]
        out += ["", "    </details>", ""]
    out.append(":::")
    return "\n".join(out) + "\n"


# ---------- assembly ----------

def layer_markdown(t: Topic, lang: str, layer: int, linker: Linker, labels: dict) -> str:
    ldir = t.lang_dir(lang)
    lmeta = load_yaml(ldir / "topic.yaml", {}) or {}
    layer_names = {int(k): v for k, v in (lmeta.get("layers") or {}).items()}
    names = section_names(t, lang)
    qtext = t.lang_questions(lang)
    titles = {c["id"]: c.get("title", c["id"])
              for c in load_yaml(ldir / "concepts.yaml", []) or [] if isinstance(c, dict) and "id" in c}
    title = lmeta.get("title", t.id)

    nav = [f"[{labels['overview']}](index.html)"]
    for n in LAYERS:
        nav.append(f"[{n} · {layer_names.get(n, n)}](layer-{n}.html)"
                   + ('{aria-current="page"}' if n == layer else ""))
    out = [
        "---",
        f"title: {json.dumps(f'{title} · {layer_names.get(layer, layer)}', ensure_ascii=False)}",
        f"lang: {lang}",
        f"reference-section-title: {json.dumps(labels['references'], ensure_ascii=False)}",
        f"toc-title: {json.dumps(labels['contents'], ensure_ascii=False)}",
        "---", "",
        "::: reader-nav", " · ".join(nav), ":::", "",
    ]

    for domain in t.domains:
        concepts = [c for c in t.concepts
                    if c.get("domain") == domain and int(c.get("first_layer", 1)) <= layer]
        if not concepts:
            continue
        idx = ldir / "domains" / domain / "index.md"
        dmeta, dbody = split_frontmatter(idx.read_text(encoding="utf-8")) if idx.exists() else ({}, "")
        out += [f"# {dmeta.get('title', domain)} {{#d-{domain}}}", ""]
        bridge = layer_bodies(dbody).get(layer)
        if bridge:
            out += [linker.rewrite(bridge.strip(), idx, layer), ""]

        for c in concepts:
            cid = c["id"]
            cf = t.concept_file(lang, c)
            if not cf.exists():
                continue
            _, body = split_frontmatter(cf.read_text(encoding="utf-8"))
            section = layer_bodies(body).get(layer)
            if section is None:
                continue
            out += [f"## {titles.get(cid, cid)} {{#c-{cid}}}", ""]
            prereqs = [p for p in c.get("prerequisites") or [] if p in linker.concepts]
            if prereqs:
                links = ", ".join(f"[{titles.get(p, p)}]({linker.concept_target(p, layer, layer)})"
                                  for p in prereqs)
                out += [f"::: prereq", f"{labels['prereq']}: {links}.", ":::", ""]
            check = check_block(t, qtext, cid, layer, labels)
            parts = subsections(section, names) if names else []
            if parts:
                intro = section[: section.index("###")].strip() if "###" in section else ""
                if intro:
                    out += [linker.rewrite(intro, cf, layer, cid), ""]
                for key, heading, text in parts:
                    if key == "next" and check:
                        out += [check, ""]
                        check = ""
                    text = linker.rewrite(text.strip(), cf, layer, cid)
                    if key == "key-idea":
                        # A class on the heading, not a div: pandoc would put the div's footnotes right after it.
                        out += [f"### {heading} {{.key-idea}}", "", text, ""]
                    else:
                        out += [f"### {heading}", "", text, ""]
            else:
                out += [linker.rewrite(section.strip(), cf, layer, cid), ""]
            if check:
                out += [check, ""]
    return convert_citations("\n".join(out), labels)


def overview_markdown(t: Topic, lang: str, linker: Linker, labels: dict) -> str:
    ldir = t.lang_dir(lang)
    lmeta = load_yaml(ldir / "topic.yaml", {}) or {}
    ov = ldir / "overview.md"
    meta, body = split_frontmatter(ov.read_text(encoding="utf-8")) if ov.exists() else ({}, "")
    title = meta.get("title") or lmeta.get("title", t.id)
    body = re.sub(r"\A\s*#\s+.*\n", "", body)  # the title goes in the header
    head = ["---", f"title: {json.dumps(title, ensure_ascii=False)}", f"lang: {lang}",
            f"reference-section-title: {json.dumps(labels['references'], ensure_ascii=False)}",
            "---", ""]
    return convert_citations("\n".join(head) + linker.rewrite(body, ov, 0), labels)


def pandoc(md: str, out: Path, bib: Path, toc: bool) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as fh:
        fh.write(md)
        src = fh.name
    cmd = ["pandoc", src, "-f", "markdown", "-t", "html5", "--standalone", "--embed-resources",
           "--citeproc", "--bibliography", str(bib), "--csl", str(READER_DIR / "sage-notes.csl"),
           "--css", str(READER_DIR / "style.css"),
           "--include-after-body", str(READER_DIR / "notes.html"),
           "--reference-location=document", "--resource-path", str(ROOT), "-o", str(out)]
    if toc:
        cmd += ["--toc", "--toc-depth=2"]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True)
    finally:
        Path(src).unlink(missing_ok=True)
    if res.returncode != 0:
        raise SystemExit(f"pandoc failed for {out.name}:\n{res.stderr}")
    for line in res.stderr.splitlines():
        print(f"  pandoc: {line}")


def pandoc_md(md: str, out: Path, bib: Path) -> None:
    """Clean Markdown (GFM) for reading in any editor: numbered notes and a sources section."""
    md = re.sub(r"\((index|layer-\d)\.html", r"(\1.md", md)
    md = re.sub(r"(!\[[^\]]*\]\()(/[^)\s]+)",
                lambda m: m.group(1) + os.path.relpath(m.group(2), out.parent), md)
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as fh:
        fh.write(md)
        src = fh.name
    cmd = ["pandoc", src, "-f", "markdown-implicit_figures", "-t", "gfm", "--wrap=none",
           "--citeproc", "--bibliography", str(bib), "--csl", str(READER_DIR / "sage-notes.csl"),
           "--lua-filter", str(READER_DIR / "gfm.lua"), "--reference-location=document", "-o", str(out)]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True)
    finally:
        Path(src).unlink(missing_ok=True)
    if res.returncode != 0:
        raise SystemExit(f"pandoc failed for {out.name}:\n{res.stderr}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("topic")
    parser.add_argument("--lang")
    parser.add_argument("--layer", type=int, choices=LAYERS)
    parser.add_argument("--out", help="output folder (default exports/reader/<topic>/<lang>)")
    parser.add_argument("--keep-source", action="store_true",
                        help="also write the assembled pandoc markdown (<name>.source.md), for debugging")
    args = parser.parse_args()

    if not shutil.which("pandoc"):
        print("pandoc not found: install it (e.g. 'brew install pandoc').")
        return 1
    t = load_topic(resolve_topic(args.topic))
    langs = [args.lang] if args.lang else t.languages
    for lang in langs:
        labels = LABELS.get(lang)
        if not labels:
            print(f"No LABELS entry for language '{lang}' in tools/build_reader.py.")
            return 1
        out_dir = Path(args.out) if args.out else ROOT / "exports" / "reader" / t.id / lang
        out_dir.mkdir(parents=True, exist_ok=True)
        bib = out_dir / ".sources.json"
        bib.write_text(json.dumps(csl_items(t), ensure_ascii=False), encoding="utf-8")
        linker = Linker(t, lang)
        docs = {}
        if args.layer is None:
            docs["index"] = (overview_markdown(t, lang, linker, labels), False)
        for layer in ([args.layer] if args.layer else LAYERS):
            docs[f"layer-{layer}"] = (layer_markdown(t, lang, layer, linker, labels), True)
        for name, (md, toc) in docs.items():
            if args.keep_source:
                (out_dir / f"{name}.source.md").write_text(md, encoding="utf-8")
            pandoc(md, out_dir / f"{name}.html", bib, toc)
            pandoc_md(md, out_dir / f"{name}.md", bib)
            shown = out_dir.relative_to(ROOT) if out_dir.is_relative_to(ROOT) else out_dir
            print(f"wrote {shown / name}.html and .md")
        bib.unlink(missing_ok=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
