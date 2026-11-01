---
name: topic-builder
description: Research and build a complete Sage Mentoring learning topic (concept map, rated sources, research notes, layered content from basics to professional, own diagrams, question bank, layer indexes) following docs/format.md, in phases that can be resumed across sessions. Use this whenever the user wants to learn, research or build a new topic ("quiero aprender X", "investiga sobre X", "prepara el tema de X", "crea un temario de X"), continue or resume a topic ("sigue con el tema de color", "siguiente ámbito"), extend or fix one (add a domain, concepts, sources, questions, diagrams), even if they don't say "topic" or "skill".
---

# Topic builder

Builds a topic under `topics/<topic-id>/` in phases. **`docs/format.md` is the contract** — read it before writing anything, and read `CLAUDE.md` for the project rules. Conversation with the user is in their language (Spanish); technical names in English; content in the topic's content language.

## Why phases
A full topic means reading dozens of sources and writing hundreds of files — far more than one context window or one usage window. Each phase leaves everything on disk, so any session can resume. Raw sources are read only by `source-researcher` subagents, which return compact notes; the main session works from notes and summaries. Keep it that way: don't read sources or whole concept files in the main session unless you need to spot-check.

## Model split
| Work | Who |
|---|---|
| Concept map, source selection, final review | main session (designed for Opus) |
| Reading sources → notes | `source-researcher` subagent (Sonnet) |
| Writing domain content | `concept-writer` subagent (Sonnet) |
| Writing questions | `question-writer` subagent (Sonnet) |
| Validation, layer indexes, diagram rendering | scripts in `tools/` and `assets/diagrams/src/` |

## Step 0 — Find where we are
If `topics/<id>/` exists, read `research/plan.md` (the build log) and run
`uv run tools/validate_topic.py <id> --stage content`, then tell the user in two or three lines what is done and what comes next. Continue from there. If it doesn't exist, start at phase 1.

## Phase 1 — Map (then stop for review)
1. **Clarify the goal in at most 2 questions**, each with a recommended answer: what for (angle: e.g. digital design vs painting vs printing), and anything already known. Default: from zero to professional level.
2. **Explore candidate sources** with WebSearch (search results only, no fetching full documents here). Prefer reliability A (reference textbooks, university courses such as MIT OCW, standards bodies such as CIE/ISO/ICAO, official docs), then B (peer-reviewed papers, reviews); C only as support. Aim for 2+ independent A/B sources per domain, and try to include at least one **open** A/B source per domain: paid books are only usable through their tables of contents, previews, publisher pages and reviews, so a domain backed only by paid sources ends up with thin notes. Put access caveats (search-only, moved URL, approximate year) in the source's optional `notes` field.
   **Check access before relying on a source.** For each A/B candidate, find out with a search (or one fetch of its landing page, not the full document) how much of the body text is legitimately readable, and record it at the start of `notes`: `full text`, `preview`, `TOC only`, `abstract only` or `blocked` (paywall, CAPTCHA). Only `full text` and `preview` sources count towards the 2+ per domain; the others are further reading. In the pilot, two paid A textbooks gave TOC-only notes and an NCBI book was blocked by a CAPTCHA, which cost a whole extra research round.
3. **Design the map.** Domains in study order; concepts with `first_layer` and `prerequisites` (no cycles; prerequisites point to concepts that are simpler or earlier). Size guide: 4–8 domains, 5–12 concepts each. A concept is something that can be explained and tested on its own.
4. **Write**: `topic.yaml`, `i18n/<lang>/topic.yaml` (title, description, layer names, domain titles), `i18n/<lang>/concepts.yaml` (one title per concept — the map is reviewed in the content language, and writers reuse these titles), `concepts.yaml`, `sources.yaml`, and `research/plan.md`:

```markdown
# Build plan: <topic>
Goal: <learner goal and angle>
Content language: es

## Domains
- [ ] perception — sources: fairchild-2013, … — status: pending
- [ ] …

## Doubts to resolve
- <open questions about sources or scope, removed once decided>

## Decisions
- 2026-11-01 — <what the user decided and why, e.g. a source added or excluded>

## Log
- 2026-11-01 — map created (N domains, M concepts, K sources)
```
5. Run `uv run tools/validate_topic.py <id> --stage map` and fix errors.
6. **Stop and present the map**: domains with a one-line purpose, concepts per domain (titles) with their first layer, sources table (id, type, reliability, access) and the doubts. Ask for changes. Do not start phase 2 until the user approves — fixing the map is cheap now and expensive later. When they answer, move each settled doubt to **Decisions** and log the approval.

## Phase 2 — One domain at a time
Recommend one domain per session. For the chosen domain:

1. **Research.** Launch `source-researcher` subagents **in parallel**, one per source relevant to the domain that has no note yet (skip sources already noted — notes are reusable; when a source also serves later domains, ask for those concepts too). Give each: topic path, source id and entry, concept ids with a one-line meaning, where to find it, and for paid sources which legitimate routes to try (table of contents, preview, publisher page, reviews). If notes reveal missing or wrong concepts, adjust `concepts.yaml` and tell the user.
   **PDF sources: extract the text first.** Researchers only have WebFetch, which cannot extract text from most PDFs and rejects some certificates (in color-mixing, two open A/B papers came back empty this way). Before launching the researcher for a PDF, run `uv run tools/pdf_to_text.py <url> <scratchpad>/sources --name <source-id>` and give it the `.txt` path (pages are marked) instead of the URL. If the download fails, give it the URL and let it fall back to abstracts.
   **Pages the fetcher can't reach.** A 403, CAPTCHA or bot block is the site's decision: never disguise requests (fake user agents, CAPTCHA solving, rotating hosts) to get around it. If the site's terms allow normal reading, you may open it in the built-in browser as a regular visitor to find an open PDF link, then extract it as above; otherwise use another source. For pages that are down, try the Wayback Machine (`https://archive.org/wayback/available?url=<url>`, then fetch the snapshot with `id_` after the timestamp, using `curl --compressed`) and save it as text for the researcher, since WebFetch can't open web.archive.org. Open institutional collections are worth searching first: the Getty Virtual Library and the NGA backlist have free full-text A sources on artists' materials. Respect each site's terms: the ASTM store forbids AI use of its content, so only a short summary of the public page is kept.
   **Check coverage before writing**: every concept of the domain needs content-level claims (not just TOC locations) from 2+ sources. Count `→ <concept>` bullets per note (the validator warns about notes that lack them). If a concept falls short, find an open A/B source, add it to `sources.yaml` and research it before step 2.
2. **Write content.** Launch one `concept-writer` for the domain (topic, domain, language, learner goal) and tell it which notes are TOC-only or abstract-only (further reading, not claims) and which are unusable. Titles come from `i18n/<lang>/concepts.yaml` and the domain title from `i18n/<lang>/topic.yaml`; if the writer improves one, it changes it in both places.
3. **Diagrams.** For each `diagram-request` comment the writer left (and any you think essential), write a generator in `assets/diagrams/src/<name>.py` that outputs SVG using the standard library only, reusing the shared helpers in `assets/diagrams/src/colormath.py` (colour-matching functions, XYZ ↔ sRGB, spectral colours and gradients, photopigment template; add new helpers there rather than copying code), with color math implemented explicitly (e.g. sRGB ↔ linear ↔ XYZ ↔ Lab/OKLab) so diagrams are accurate and reproducible. Text labels come from a per-language dict so `<id>.<lang>.svg` can be regenerated per language; diagrams without text are `<id>.svg`. Run it with `uv run`, look at the result (e.g. `qlmanage -t -s 900 -o <scratchpad> <file>.svg` on macOS, then read the PNG) to catch overlapping labels or banding, register the asset in `assets.yaml` (origin own, generator, license = topic license, concepts) and alt text + caption in `i18n/<lang>/assets.yaml`, then replace the comment with the image link. Third-party images only with CC/public-domain license and full attribution.
4. **Spot-check the content** before any question is written on it: 2–3 concept sections against the notes (citations support the claims, layers build up), plus every claim the writer reported as a loose fit. Fix what you find — questions built on a weak claim are expensive to fix later.
5. **Questions.** Launch one `question-writer` for the domain. Tell it which sources the content actually cites and where sources disagree on numbers.
6. **Validate** with `--stage content --domain <domain>`; fix errors (delegate back to the relevant subagent if the fix is large).
7. **Spot-check ~10% of the questions** against the content: answer backed by a citation, distractors plausible, rubrics checkable. Fix what you find.
8. Update `research/plan.md` (tick the domain, log line with counts and `[unverified]` count) and report to the user: concepts, questions per layer, diagrams, open issues, next domain.

## Phase 3 — Close the topic
When every domain is done:
1. Write `i18n/<lang>/overview.md` (layer 0): what the topic is, why it matters, a map of the domains in study order with one paragraph each linking to their index, how layers work, and suggested paths. Cited like everything else.
2. `uv run tools/build_layer_index.py <id>`.
3. `uv run tools/validate_topic.py <id>` (final stage) until 0 errors; review warnings with the user (`[unverified]` claims, uncovered concept/layers).
4. Log it in `research/plan.md` and tell the user the topic is ready for `topic-examiner` and the Anki export.

## Changing an existing topic
Same rules, smallest scope: new sources → researcher; new/changed concepts → add the title to `i18n/<lang>/concepts.yaml`, then writer for that domain; questions → question-writer. Never rename ids that already have attempts in `learners/*/progress/<topic>/attempts.jsonl` — progress is linked to them. Re-run the layer index and validation afterwards.

## Non-negotiables (from CLAUDE.md)
Every claim cited or `[unverified]`; summarize, never copy protected text; only shareable images; every question has concept, layer and sources; no personal data inside `topics/`.
