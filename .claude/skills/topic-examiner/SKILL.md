---
name: topic-examiner
description: Examine the learner on a Sage Mentoring topic in the chat — pick questions with spaced repetition, ask them one by one, grade (open and case answers with their rubric), record every attempt and report progress. Use this whenever the user wants to be tested, quizzed, reviewed or to practice a topic ("examíname", "hazme un test de la capa 1", "repaso de 10 minutos", "pregúntame sobre percepción", "¿qué tal voy en teoría del color?"), even if they don't name the skill.
---

# Topic examiner

Runs an exam in the chat over a topic in `topics/<topic-id>/`. The learner's data lives in `learners/<learner>/` (default learner: `askhari`). Formats are in `docs/format.md`. Speak to the learner in their content language (Spanish).

All bookkeeping is done by `tools/progress.py` — never write `attempts.jsonl` or `summary.json` by hand. That keeps the history append-only and the summary consistent.

## 1. Set up (one short message)
Work out from the request: topic, scope (layer / domain / concept), length (default 10 questions). If something is unclear, propose a default and go, e.g. "Te propongo 10 preguntas mezcladas de lo que toca repasar. ¿Vamos?". Session id: `<YYYY-MM-DD>-<letter>` (a, b, c… for several that day).

Then:
```bash
uv run tools/progress.py pick <topic> <learner> --n 10 [--layer N] [--domain D] [--concept C]
```
It returns the questions already ordered: due reviews first, then new questions whose prerequisites the learner has started, interleaved by concept. `reason` says why each was picked. If it returns nothing for the scope, say so and suggest another scope (or that the content is not built yet). If it returns fewer than requested, it is because the rest is locked behind prerequisites or lower layers not yet attempted — tell the learner that progress unlocks more, and offer `--concept` if they want to jump ahead on purpose.

## 2. Ask one question at a time
Show the progress (`3/10`), the layer, and the prompt. For single-choice, list the options with their letters. Never reveal `correct`, `accepted`, `model_answer` or `rubric` before the learner answers. Wait for the answer.

## 3. Grade
- **single-choice**: correct or incorrect against `correct`.
- **short-answer**: compare with `accepted`, tolerant of accents, case, typos and plurals; a clearly equivalent term counts. Close but not quite → partial.
- **open / case**: go through each rubric criterion and decide met / partly / not met; `score` = share of criteria met (partly = half), rounded to 0.05. `result`: correct ≥ 0.8, partial ≥ 0.5, else incorrect. Grade only against the rubric, not against style or length, so grades are consistent across sessions.

Then record it right away (one call per answer, so nothing is lost if the session ends):
```bash
uv run tools/progress.py record <topic> <learner> --question <id> --result <r> [--score <s>] --session <session> [--feedback "<one line>"]
```
`--score` is needed for open/case; for the other types the result implies it.

## 4. Feedback to the learner
Short and useful: whether it was right; the `explanation` (single-choice) or what was missing against the rubric (open/case) with a brief model answer; and a link to the concept section to review — `topics/<topic>/i18n/<lang>/domains/<domain>/concepts/<concept>.md#layer-<n>`. If the learner disputes a grade with a good argument, re-record with the corrected result and a feedback note; never edit past lines. If the question itself looks wrong or ambiguous, say so and note it for `topic-builder`.

## 5. Close
Run `uv run tools/progress.py summary <topic> <learner>` and report in a few lines: score of the session, concepts that improved, the weakest ones with their sections to re-read, and what the next session should cover. Mention questions flagged as faulty, if any.

## Learner asks "how am I doing?"
Run the summary command only and explain it in plain language — no exam needed.
