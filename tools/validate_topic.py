# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6"]
# ///
"""Validate a topic folder against docs/format.md.

Usage: uv run tools/validate_topic.py <topic-id-or-path> [--stage map|content|final] [--domain <id>]

Stages (what is expected to exist so far):
  map      topic.yaml, concepts.yaml, sources.yaml, research/plan.md and, per language,
           i18n/<lang>/topic.yaml (title, layer and domain names) and
           i18n/<lang>/concepts.yaml (concept titles); notes, if any
  content  + everything for the domains that already have a concept file (or --domain)
  final    + every domain, overview, layer indexes up to date (default)

Exit code 1 if there are errors. Warnings never fail.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_layer_index  # noqa: E402
from topiclib import (  # noqa: E402
    CITATION_BLOCK_RE, ID_RE, IMAGE_RE, LAYERS, MD_LINK_RE, REQUIRED_SECTIONS, TEMPLATE_SECTIONS,
    Topic, citation_keys, layer_bodies, layer_sections, load_topic, load_yaml, resolve_topic,
    section_names, split_frontmatter, subsections,
)

SOURCE_TYPES = {"textbook", "course", "standard", "paper", "docs", "article"}
RELIABILITY = {"A", "B", "C"}
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s#]+\.md)(?:#[^)]*)?\)")
ACCESS = {"open", "paid"}
QUESTION_TYPES = {"single-choice", "short-answer", "open", "case"}
ORIGINS = {"own", "third-party"}
SHAREABLE_LICENSE_PREFIXES = ("CC-", "CC0", "public-domain")
# Only the arrow that ends a line (optionally followed by a parenthetical remark) counts,
# so "black+yellow→green" inside a claim is ignored.
NOTE_ARROW_RE = re.compile(r"→\s*([a-z0-9][a-z0-9-]*(?:\s*,\s*[a-z0-9][a-z0-9-]*)*)\s*(?:\([^()]*\))?\s*$", re.MULTILINE)


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, where: str, msg: str) -> None:
        self.errors.append(f"{where}: {msg}")

    def warn(self, where: str, msg: str) -> None:
        self.warnings.append(f"{where}: {msg}")


def check_ids(items, where: str, rep: Report) -> set:
    seen = set()
    if not isinstance(items, list):
        rep.error(where, "must be a list")
        return seen
    for i, item in enumerate(items):
        if not isinstance(item, dict) or "id" not in item:
            rep.error(where, f"item #{i} has no id")
            continue
        iid = item["id"]
        if not isinstance(iid, str) or not ID_RE.match(iid):
            rep.error(where, f"id '{iid}' is not lowercase-kebab-case")
        if iid in seen:
            rep.error(where, f"duplicate id '{iid}'")
        seen.add(iid)
    return seen


def check_topic_meta(t: Topic, rep: Report) -> None:
    where = "topic.yaml"
    if not t.meta:
        rep.error(where, "missing or empty")
        return
    for key in ("id", "version", "languages", "license", "domains"):
        if key not in t.meta:
            rep.error(where, f"missing '{key}'")
    if t.meta.get("id") != t.path.name:
        rep.error(where, f"id '{t.meta.get('id')}' does not match folder '{t.path.name}'")
    for d in t.domains:
        if not ID_RE.match(str(d)):
            rep.error(where, f"domain '{d}' is not lowercase-kebab-case")
    if len(set(t.domains)) != len(t.domains):
        rep.error(where, "duplicate domains")


def check_concepts(t: Topic, rep: Report) -> None:
    where = "concepts.yaml"
    ids = check_ids(t.concepts, where, rep)
    graph = {}
    for c in t.concepts:
        if not isinstance(c, dict) or "id" not in c:
            continue
        cid = c["id"]
        if c.get("domain") not in t.domains:
            rep.error(where, f"'{cid}' has unknown domain '{c.get('domain')}'")
        if c.get("first_layer") not in LAYERS:
            rep.error(where, f"'{cid}' first_layer must be 1, 2 or 3")
        prereqs = c.get("prerequisites") or []
        for p in prereqs:
            if p not in ids:
                rep.error(where, f"'{cid}' prerequisite '{p}' does not exist")
            if p == cid:
                rep.error(where, f"'{cid}' lists itself as prerequisite")
        graph[cid] = [p for p in prereqs if p in ids and p != cid]
    # cycle detection
    state: dict[str, int] = {}

    def visit(node: str, stack: list[str]) -> None:
        state[node] = 1
        for nxt in graph.get(node, []):
            if state.get(nxt) == 1:
                cycle = stack[stack.index(nxt):] + [nxt] if nxt in stack else [node, nxt]
                rep.error(where, "prerequisite cycle: " + " -> ".join(cycle))
            elif state.get(nxt) is None:
                visit(nxt, stack + [nxt])
        state[node] = 2

    for node in graph:
        if state.get(node) is None:
            visit(node, [node])
    for d in t.domains:
        if not any(isinstance(c, dict) and c.get("domain") == d for c in t.concepts):
            rep.warn(where, f"domain '{d}' has no concepts")


def check_sources(t: Topic, rep: Report) -> set:
    where = "sources.yaml"
    ids = check_ids(t.sources, where, rep)
    for s in t.sources:
        if not isinstance(s, dict) or "id" not in s:
            continue
        sid = s["id"]
        for key in ("type", "reliability", "title", "authors", "year", "language", "access", "accessed"):
            if key not in s:
                rep.error(where, f"'{sid}' missing '{key}'")
        if s.get("type") not in SOURCE_TYPES:
            rep.error(where, f"'{sid}' type must be one of {sorted(SOURCE_TYPES)}")
        if s.get("reliability") not in RELIABILITY:
            rep.error(where, f"'{sid}' reliability must be A, B or C")
        if s.get("access") not in ACCESS:
            rep.error(where, f"'{sid}' access must be open or paid")
        if "notes" in s and not isinstance(s["notes"], str):
            rep.error(where, f"'{sid}' notes must be a string")
        if not s.get("identifiers"):
            rep.warn(where, f"'{sid}' has no identifiers (isbn/doi/url)")
    return ids


def check_notes(t: Topic, source_ids: set, concept_ids: set, rep: Report) -> None:
    ndir = t.path / "research" / "notes"
    noted = set()
    if ndir.exists():
        for f in sorted(ndir.glob("*.md")):
            where = f"research/notes/{f.name}"
            meta, body = split_frontmatter(f.read_text(encoding="utf-8"))
            sid = meta.get("source")
            arrows = {c.strip() for m in NOTE_ARROW_RE.findall(body) for c in m.split(",")}
            if not arrows:
                rep.warn(where, "no '→ <concept-id>' bullets (coverage cannot be counted)")
            for c in sorted(arrows - concept_ids):
                rep.error(where, f"bullet points to unknown concept '{c}'")
            for c in meta.get("concepts") or []:
                if arrows and c not in arrows:
                    rep.warn(where, f"concept '{c}' in frontmatter has no '→ {c}' bullet")
            if sid != f.stem:
                rep.error(where, f"frontmatter source '{sid}' must match file name '{f.stem}'")
            if sid not in source_ids:
                rep.error(where, f"source '{sid}' not in sources.yaml")
            for c in meta.get("concepts") or []:
                if c not in concept_ids:
                    rep.error(where, f"concept '{c}' does not exist")
            noted.add(f.stem)
    for sid in sorted(source_ids - noted):
        rep.warn("research/notes", f"source '{sid}' has no notes yet")


def is_shareable(lic: str) -> bool:
    return isinstance(lic, str) and lic.startswith(SHAREABLE_LICENSE_PREFIXES)


def check_assets(t: Topic, concept_ids: set, rep: Report) -> set:
    where = "assets.yaml"
    ids = check_ids(t.assets, where, rep)
    for a in t.assets:
        if not isinstance(a, dict) or "id" not in a:
            continue
        aid = a["id"]
        origin = a.get("origin")
        if origin not in ORIGINS:
            rep.error(where, f"'{aid}' origin must be own or third-party")
        if not is_shareable(a.get("license", "")):
            rep.error(where, f"'{aid}' license '{a.get('license')}' is not shareable (CC-*, CC0, public-domain)")
        if origin == "third-party":
            for key in ("author", "source_url"):
                if not a.get(key):
                    rep.error(where, f"'{aid}' third-party asset missing '{key}'")
        if origin == "own":
            gen = a.get("generator")
            if not gen:
                rep.error(where, f"'{aid}' own asset missing 'generator'")
            elif not (t.path / "assets" / gen).exists():
                rep.error(where, f"'{aid}' generator 'assets/{gen}' not found")
        file = a.get("file", "")
        files = [file.replace("{lang}", lang) for lang in t.languages] if "{lang}" in file else [file]
        for f in files:
            if not f or not (t.path / "assets" / f).exists():
                rep.error(where, f"'{aid}' file 'assets/{f}' not found")
        for c in a.get("concepts") or []:
            if c not in concept_ids:
                rep.error(where, f"'{aid}' concept '{c}' does not exist")
    return ids


def check_markdown_refs(path: Path, body: str, source_ids: set, rep: Report, where: str) -> None:
    for key in citation_keys(body):
        if key not in source_ids:
            rep.error(where, f"citation '@{key}' not in sources.yaml")
    unverified = body.count("[unverified]")
    if unverified:
        rep.warn(where, f"{unverified} [unverified] claim(s)")
    for ref in IMAGE_RE.findall(body):
        if ref.startswith(("http://", "https://")):
            rep.error(where, f"external image '{ref}': images must live in assets/")
            continue
        if not (path.parent / ref).resolve().exists():
            rep.error(where, f"image '{ref}' not found")
    for ref in LINK_RE.findall(body):
        if ref.startswith(("http://", "https://")):
            continue
        if not (path.parent / ref).resolve().exists():
            # Warning, not error: in phase 2 a concept may link ahead to a domain not built yet.
            rep.warn(where, f"link '{ref}' not found")


KEY_IDEA_MAX_WORDS = 60
# A citation ends a sentence or clause when followed by punctuation, another citation,
# a closing bracket or the end of the line.
CITATION_END_OK_RE = re.compile(r"\s*(?:$|[.;:)\]\u2014]|\[)", re.MULTILINE)


def is_format2(meta: dict) -> bool:
    return str(meta.get("format", "")) == "2"


def domain_layers(t: Topic, domain: str) -> list[int]:
    firsts = [int(c.get("first_layer", 1)) for c in t.concepts
              if isinstance(c, dict) and c.get("domain") == domain]
    return [n for n in LAYERS if firsts and n >= min(firsts)]


def mid_sentence_citations(text: str) -> int:
    count = 0
    for m in CITATION_BLOCK_RE.finditer(text):
        if not CITATION_END_OK_RE.match(text, m.end()):
            count += 1
    return count


def check_layer_links(path: Path, layer: int, text: str, concepts: dict, rep: Report, where: str) -> None:
    """Layer N may only rely on layers <= N: no links to later concepts or later layer anchors."""
    for ref, anchor in MD_LINK_RE.findall(text):
        if ref.startswith(("http://", "https://")):
            continue
        if ref and not ref.endswith(".md"):
            continue
        target = (path.parent / ref).resolve() if ref else path.resolve()
        if target.parent.name == "concepts" and target.stem in concepts:
            first = int(concepts[target.stem].get("first_layer", 1))
            if first > layer:
                rep.error(where, f"layer-{layer} links to '{target.stem}', which starts at layer "
                                 f"{first} (only allowed in the 'next' subsection)")
        m = re.fullmatch(r"#layer-(\d)", anchor or "")
        if m and int(m.group(1)) > layer:
            rep.error(where, f"layer-{layer} links to a later section #layer-{m.group(1)} "
                             f"(only allowed in the 'next' subsection)")


def check_template(t: Topic, path: Path, body: str, names: dict, rep: Report, where: str) -> None:
    """Layer template (format: 2): subsections, key idea length, layer rule, citation placement."""
    concepts = t.concept_map()
    mid = 0
    for layer, text in sorted(layer_bodies(body).items()):
        lwhere = f"{where} #layer-{layer}"
        parts = subsections(text, names)
        keys = [k for k, _, _ in parts]
        for k, heading, _ in parts:
            if k is None:
                rep.error(lwhere, f"unknown subsection '### {heading}' (see 'sections' in topic.yaml)")
        for k in REQUIRED_SECTIONS:
            if k not in keys:
                rep.error(lwhere, f"missing subsection '### {names.get(k, k)}'")
        known = [k for k in keys if k is not None]
        if len(set(known)) != len(known):
            rep.error(lwhere, "repeated subsection")
        elif known != sorted(known, key=TEMPLATE_SECTIONS.index):
            rep.error(lwhere, "subsections out of order (" + " → ".join(
                names.get(k, k) for k in TEMPLATE_SECTIONS) + ")")
        for k, _, sub in parts:
            if k == "key-idea":
                words = len(re.sub(r"\[[^\[\]]*@[^\[\]]*\]", "", sub).split())
                if words > KEY_IDEA_MAX_WORDS:
                    rep.warn(lwhere, f"key idea has {words} words (aim for <= {KEY_IDEA_MAX_WORDS})")
            if k != "next":
                check_layer_links(path, layer, sub, concepts, rep, lwhere)
            mid += mid_sentence_citations(sub)
    if mid:
        rep.warn(where, f"{mid} citation(s) in the middle of a sentence (put them at the end)")


def check_domain_bridges(t: Topic, domain: str, body: str, rep: Report, where: str) -> None:
    present = set(layer_sections(body))
    for n in domain_layers(t, domain):
        if n not in present:
            rep.error(where, f"missing bridge section {{#layer-{n}}} (format: 2)")


def check_questions(t: Topic, domains: list, concept_ids: set, source_ids: set, rep: Report) -> None:
    cmap = t.concept_map()
    all_ids: set = set()
    for domain in domains:
        where = f"questions/{domain}.yaml"
        qs = t.questions.get(domain) or []
        if not qs:
            rep.warn(where, "no questions")
            continue
        ids = check_ids(qs, where, rep)
        dup = all_ids & ids
        for d in sorted(dup):
            rep.error(where, f"question id '{d}' also used in another domain")
        all_ids |= ids
        for q in qs:
            if not isinstance(q, dict) or "id" not in q:
                continue
            qid = q["id"]
            concept = cmap.get(q.get("concept"))
            if not concept:
                rep.error(where, f"'{qid}' concept '{q.get('concept')}' does not exist")
            elif concept.get("domain") != domain:
                rep.error(where, f"'{qid}' concept '{concept['id']}' belongs to domain '{concept.get('domain')}'")
            layer = q.get("layer")
            if layer not in LAYERS:
                rep.error(where, f"'{qid}' layer must be 1, 2 or 3")
            elif concept and layer < int(concept.get("first_layer", 1)):
                rep.error(where, f"'{qid}' layer {layer} is below concept first_layer {concept.get('first_layer')}")
            if q.get("type") not in QUESTION_TYPES:
                rep.error(where, f"'{qid}' type must be one of {sorted(QUESTION_TYPES)}")
            srcs = q.get("sources") or []
            if not srcs:
                rep.error(where, f"'{qid}' has no sources")
            for s in srcs:
                if s not in source_ids:
                    rep.error(where, f"'{qid}' source '{s}' not in sources.yaml")
            if q.get("type") == "single-choice" and not q.get("correct"):
                rep.error(where, f"'{qid}' single-choice needs 'correct'")

        for lang in t.languages:
            lwhere = f"i18n/{lang}/questions/{domain}.yaml"
            texts = load_yaml(t.lang_dir(lang) / "questions" / f"{domain}.yaml", []) or []
            tmap = {x["id"]: x for x in texts if isinstance(x, dict) and "id" in x}
            for missing in sorted(ids - set(tmap)):
                rep.error(lwhere, f"missing text for '{missing}'")
            for extra in sorted(set(tmap) - ids):
                rep.error(lwhere, f"'{extra}' not in questions/{domain}.yaml")
            for q in qs:
                if not isinstance(q, dict) or q.get("id") not in tmap:
                    continue
                qid, txt, qtype = q["id"], tmap[q["id"]], q.get("type")
                if not txt.get("prompt"):
                    rep.error(lwhere, f"'{qid}' missing prompt")
                if qtype == "single-choice":
                    opts = txt.get("options") or {}
                    if len(opts) < 2:
                        rep.error(lwhere, f"'{qid}' needs at least 2 options")
                    if q.get("correct") not in opts:
                        rep.error(lwhere, f"'{qid}' correct option '{q.get('correct')}' not in options")
                    if not txt.get("explanation"):
                        rep.warn(lwhere, f"'{qid}' has no explanation")
                elif qtype == "short-answer":
                    if not txt.get("accepted"):
                        rep.error(lwhere, f"'{qid}' short-answer needs 'accepted'")
                elif qtype in ("open", "case"):
                    if not txt.get("model_answer"):
                        rep.error(lwhere, f"'{qid}' needs 'model_answer'")
                    if not txt.get("rubric"):
                        rep.error(lwhere, f"'{qid}' needs 'rubric'")
        # coverage: every concept/layer of the domain should have at least one question
        for c in t.concepts:
            if not isinstance(c, dict) or c.get("domain") != domain:
                continue
            for layer in range(int(c.get("first_layer", 1)), 4):
                if not any(q.get("concept") == c["id"] and q.get("layer") == layer for q in qs if isinstance(q, dict)):
                    rep.warn(where, f"no question for '{c['id']}' at layer {layer}")


def lang_titles(t: Topic, lang: str) -> tuple[dict, dict]:
    """Domain titles (from i18n topic.yaml) and concept titles (from i18n concepts.yaml)."""
    ldir = t.lang_dir(lang)
    lmeta = load_yaml(ldir / "topic.yaml", {}) or {}
    domains = lmeta.get("domains") if isinstance(lmeta.get("domains"), dict) else {}
    items = load_yaml(ldir / "concepts.yaml", []) or []
    concepts = {c["id"]: c.get("title") for c in items if isinstance(c, dict) and "id" in c}
    return domains, concepts


def check_language_meta(t: Topic, lang: str, concept_ids: set, rep: Report) -> None:
    """What every stage needs per language: topic title, layer names, domain and concept titles."""
    ldir = t.lang_dir(lang)
    base = f"i18n/{lang}"
    lmeta = load_yaml(ldir / "topic.yaml", {}) or {}
    if not lmeta.get("title"):
        rep.error(f"{base}/topic.yaml", "missing 'title'")
    layers = lmeta.get("layers") or {}
    for n in LAYERS:
        if not (layers.get(n) or layers.get(str(n))):
            rep.error(f"{base}/topic.yaml", f"missing layers name for {n}")
    dnames = lmeta.get("domains")
    if not isinstance(dnames, dict):
        rep.error(f"{base}/topic.yaml", "missing 'domains' (map of domain id -> title)")
        dnames = {}
    for d in t.domains:
        if not dnames.get(d):
            rep.error(f"{base}/topic.yaml", f"missing title for domain '{d}'")
    for d in sorted(set(dnames) - set(t.domains)):
        rep.error(f"{base}/topic.yaml", f"domain '{d}' not in topic.yaml")
    snames = lmeta.get("sections")
    if snames is not None:
        if not isinstance(snames, dict):
            rep.error(f"{base}/topic.yaml", "'sections' must map template keys to names")
        else:
            for k in TEMPLATE_SECTIONS:
                if not snames.get(k):
                    rep.error(f"{base}/topic.yaml", f"missing sections name for '{k}'")
            for k in sorted(set(snames) - set(TEMPLATE_SECTIONS)):
                rep.error(f"{base}/topic.yaml", f"unknown sections key '{k}'")

    cwhere = f"{base}/concepts.yaml"
    if not (ldir / "concepts.yaml").exists():
        rep.error(cwhere, "missing (concept titles)")
        return
    items = load_yaml(ldir / "concepts.yaml", []) or []
    titled = check_ids(items, cwhere, rep)
    for c in items:
        if isinstance(c, dict) and "id" in c and not c.get("title"):
            rep.error(cwhere, f"'{c['id']}' missing title")
    for cid in sorted(concept_ids - titled):
        rep.error(cwhere, f"missing title for '{cid}'")
    for cid in sorted(titled - concept_ids):
        rep.error(cwhere, f"'{cid}' not in concepts.yaml")


def check_language(t: Topic, lang: str, domains: list, stage: str, source_ids: set,
                   asset_ids: set, rep: Report) -> None:
    ldir = t.lang_dir(lang)
    base = f"i18n/{lang}"
    domain_titles, concept_titles = lang_titles(t, lang)
    names = section_names(t, lang)

    if stage == "final":
        ov = ldir / "overview.md"
        if not ov.exists():
            rep.error(f"{base}/overview.md", "missing (layer 0)")
        else:
            check_markdown_refs(ov, ov.read_text(encoding="utf-8"), source_ids, rep, f"{base}/overview.md")

    for domain in domains:
        idx = ldir / "domains" / domain / "index.md"
        iwhere = f"{base}/domains/{domain}/index.md"
        if not idx.exists():
            rep.error(iwhere, "missing")
        else:
            meta, body = split_frontmatter(idx.read_text(encoding="utf-8"))
            if meta.get("domain") != domain or not meta.get("title"):
                rep.error(iwhere, "frontmatter needs domain and title")
            elif domain in domain_titles and meta["title"] != domain_titles[domain]:
                rep.error(iwhere, f"title differs from {base}/topic.yaml domains.{domain}: "
                                  f"'{meta['title']}' vs '{domain_titles[domain]}'")
            check_markdown_refs(idx, body, source_ids, rep, iwhere)
            if is_format2(meta):
                check_domain_bridges(t, domain, body, rep, iwhere)
        old_format = 0
        for c in t.concepts:
            if not isinstance(c, dict) or c.get("domain") != domain:
                continue
            cf = t.concept_file(lang, c)
            cwhere = str(cf.relative_to(t.path))
            if not cf.exists():
                rep.error(cwhere, "missing")
                continue
            meta, body = split_frontmatter(cf.read_text(encoding="utf-8"))
            if meta.get("concept") != c["id"]:
                rep.error(cwhere, f"frontmatter concept must be '{c['id']}'")
            if not meta.get("title"):
                rep.error(cwhere, "frontmatter missing title")
            elif c["id"] in concept_titles and meta["title"] != concept_titles[c["id"]]:
                rep.error(cwhere, f"title differs from {base}/concepts.yaml: "
                                  f"'{meta['title']}' vs '{concept_titles[c['id']]}'")
            sections = layer_sections(body)
            first = int(c.get("first_layer", 1))
            for n in range(first, 4):
                if n not in sections:
                    rep.error(cwhere, f"missing section {{#layer-{n}}}")
            for n in sections:
                if n < first:
                    rep.error(cwhere, f"section layer-{n} is below first_layer {first}")
            check_markdown_refs(cf, body, source_ids, rep, cwhere)
            if is_format2(meta):
                if not names:
                    rep.error(f"{base}/topic.yaml", "missing 'sections' (needed by format: 2)")
                else:
                    check_template(t, cf, body, names, rep, cwhere)
            else:
                old_format += 1
        if old_format:
            rep.warn(f"{base}/domains/{domain}",
                     f"{old_format} concept file(s) in the old format (no 'format: 2'): migrate to the layer template")

    amap = load_yaml(ldir / "assets.yaml", []) or []
    texts = {a["id"]: a for a in amap if isinstance(a, dict) and "id" in a}
    for aid in sorted(asset_ids - set(texts)):
        rep.error(f"{base}/assets.yaml", f"missing alt text for '{aid}'")
    for aid, a in texts.items():
        if aid not in asset_ids:
            rep.error(f"{base}/assets.yaml", f"'{aid}' not in assets.yaml")
        elif not a.get("alt"):
            rep.error(f"{base}/assets.yaml", f"'{aid}' missing alt")


def domains_with_content(t: Topic) -> list:
    found = []
    for domain in t.domains:
        for lang in t.languages:
            if (t.lang_dir(lang) / "domains" / domain).exists():
                found.append(domain)
                break
    return found


def validate(path: Path, stage: str = "final", domain: str | None = None) -> Report:
    rep = Report()
    t = load_topic(path)
    check_topic_meta(t, rep)
    check_concepts(t, rep)
    concept_ids = {c["id"] for c in t.concepts if isinstance(c, dict) and "id" in c}
    source_ids = check_sources(t, rep)
    check_notes(t, source_ids, concept_ids, rep)
    if not (t.path / "research" / "plan.md").exists():
        rep.error("research/plan.md", "missing (build plan)")
    for lang in t.languages:
        check_language_meta(t, lang, concept_ids, rep)
    if stage == "map":
        return rep

    if stage == "final":
        domains = t.domains
    elif domain:
        if domain not in t.domains:
            rep.error("args", f"domain '{domain}' not in topic.yaml")
            return rep
        domains = [domain]
    else:
        domains = domains_with_content(t)

    asset_ids = check_assets(t, concept_ids, rep)
    check_questions(t, domains, concept_ids, source_ids, rep)
    for lang in t.languages:
        check_language(t, lang, domains, stage, source_ids, asset_ids, rep)

    if stage == "final":
        for lang in t.languages:
            for layer, content in build_layer_index.render(t, lang).items():
                target = t.lang_dir(lang) / "layers" / f"layer-{layer}.md"
                if not target.exists() or target.read_text(encoding="utf-8") != content:
                    rep.error(f"i18n/{lang}/layers/layer-{layer}.md",
                              "missing or out of date: run tools/build_layer_index.py")
    return rep


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("topic")
    parser.add_argument("--stage", choices=["map", "content", "final"], default="final")
    parser.add_argument("--domain")
    args = parser.parse_args()

    path = resolve_topic(args.topic)
    if not path.is_dir():
        print(f"Topic folder not found: {path}")
        return 1
    rep = validate(path, args.stage, args.domain)
    for w in rep.warnings:
        print(f"WARN  {w}")
    for e in rep.errors:
        print(f"ERROR {e}")
    print(f"\n{len(rep.errors)} error(s), {len(rep.warnings)} warning(s)")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
