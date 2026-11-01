"""Shared helpers to load a topic folder (see docs/format.md)."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TOPICS_DIR = ROOT / "topics"
# Overridable so tests never touch real learner data.
LEARNERS_DIR = Path(os.environ.get("SAGE_LEARNERS_DIR", ROOT / "learners"))

LAYERS = (1, 2, 3)
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CITATION_BLOCK_RE = re.compile(r"\[([^\[\]]*@[^\[\]]*)\]")
CITATION_KEY_RE = re.compile(r"@([a-z0-9][a-z0-9-]*[a-z0-9]|[a-z0-9])")
LAYER_ANCHOR_RE = re.compile(r"^##\s+(.+?)\s*\{#layer-(\d)\}\s*$", re.MULTILINE)
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)


def load_yaml(path: Path, default=None):
    if not path.exists():
        return default
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    return default if data is None else data


def split_frontmatter(text: str) -> tuple[dict, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    meta = yaml.safe_load(match.group(1)) or {}
    return meta, text[match.end():]


@dataclass
class Topic:
    path: Path
    meta: dict = field(default_factory=dict)
    concepts: list = field(default_factory=list)
    sources: list = field(default_factory=list)
    assets: list = field(default_factory=list)
    questions: dict = field(default_factory=dict)  # domain -> list

    @property
    def id(self) -> str:
        return self.meta.get("id", self.path.name)

    @property
    def domains(self) -> list:
        return list(self.meta.get("domains") or [])

    @property
    def languages(self) -> list:
        return list(self.meta.get("languages") or [])

    def lang_dir(self, lang: str) -> Path:
        return self.path / "i18n" / lang

    def concept_file(self, lang: str, concept: dict) -> Path:
        return (self.lang_dir(lang) / "domains" / concept["domain"]
                / "concepts" / f"{concept['id']}.md")

    def concept_map(self) -> dict:
        return {c.get("id"): c for c in self.concepts if isinstance(c, dict)}

    def all_questions(self) -> list:
        return [q for qs in self.questions.values() for q in qs]

    def lang_questions(self, lang: str) -> dict:
        """question id -> per-language text block."""
        out = {}
        qdir = self.lang_dir(lang) / "questions"
        for domain in self.domains:
            for item in load_yaml(qdir / f"{domain}.yaml", []) or []:
                if isinstance(item, dict) and "id" in item:
                    out[item["id"]] = item
        return out


def resolve_topic(name_or_path: str) -> Path:
    path = Path(name_or_path)
    if path.is_dir():
        return path.resolve()
    return (TOPICS_DIR / name_or_path).resolve()


def load_topic(path: Path) -> Topic:
    topic = Topic(path=path)
    topic.meta = load_yaml(path / "topic.yaml", {}) or {}
    topic.concepts = load_yaml(path / "concepts.yaml", []) or []
    topic.sources = load_yaml(path / "sources.yaml", []) or []
    topic.assets = load_yaml(path / "assets.yaml", []) or []
    for domain in topic.domains:
        topic.questions[domain] = load_yaml(path / "questions" / f"{domain}.yaml", []) or []
    return topic


def citation_keys(text: str) -> list[str]:
    keys = []
    for block in CITATION_BLOCK_RE.findall(text):
        keys.extend(CITATION_KEY_RE.findall(block))
    return keys


def layer_sections(body: str) -> dict[int, str]:
    """layer number -> section heading title."""
    return {int(n): title for title, n in LAYER_ANCHOR_RE.findall(body)}
