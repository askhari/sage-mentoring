# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6"]
# ///
"""Learner progress: pick questions, record attempts, rebuild the summary.

Usage:
  uv run tools/progress.py pick    <topic> <learner> [--n 10] [--layer N] [--domain D] [--concept C] [--lang es]
  uv run tools/progress.py record  <topic> <learner> --question ID --result correct|partial|incorrect
                                   [--score 0..1] --session ID [--feedback TEXT] [--lang es] [--mode chat]
  uv run tools/progress.py summary <topic> <learner>

Attempts live in learners/<learner>/progress/<topic>/attempts.jsonl (append-only);
summary.json is always rebuilt from them.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from topiclib import LEARNERS_DIR, Topic, load_topic, load_yaml, resolve_topic  # noqa: E402

INTERVALS_DAYS = [1, 3, 7, 14, 30, 60, 120]  # by consecutive-correct streak
GOOD, PASS = 0.8, 0.5
RECENT = 5
RESULTS = {"correct": 1.0, "partial": 0.5, "incorrect": 0.0}


def now() -> datetime:
    return datetime.now().replace(microsecond=0)


def progress_dir(learner: str, topic_id: str) -> Path:
    return LEARNERS_DIR / learner / "progress" / topic_id


def read_attempts(learner: str, topic_id: str) -> list[dict]:
    path = progress_dir(learner, topic_id) / "attempts.jsonl"
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def question_states(attempts: list[dict]) -> dict:
    states: dict[str, dict] = {}
    for a in sorted(attempts, key=lambda x: x["at"]):
        st = states.setdefault(a["question"], {"streak": 0, "attempts": 0})
        at = datetime.fromisoformat(a["at"])
        score = float(a["score"])
        st["attempts"] += 1
        st["last_at"], st["last_score"] = a["at"], score
        if score >= GOOD:
            st["streak"] += 1
            days = INTERVALS_DAYS[min(st["streak"], len(INTERVALS_DAYS)) - 1]
        elif score >= PASS:
            st["streak"] = max(0, st["streak"] - 1)
            days = 1
        else:
            st["streak"] = 0
            days = 0
        st["due"] = (at + timedelta(days=days)).isoformat()
    return states


def status_of(scores: list[float]) -> str:
    if not scores:
        return "new"
    recent = scores[-RECENT:]
    avg = sum(recent) / len(recent)
    if len(scores) >= 3 and avg >= GOOD and recent[-1] >= GOOD:
        return "mastered"
    if avg < PASS:
        return "weak"
    return "learning"


def build_summary(topic: Topic, learner: str) -> dict:
    attempts = sorted(read_attempts(learner, topic.id), key=lambda x: x["at"])
    by_cl: dict[tuple, list] = {}
    last_at: dict[tuple, str] = {}
    for a in attempts:
        key = (a["concept"], int(a["layer"]))
        by_cl.setdefault(key, []).append(float(a["score"]))
        last_at[key] = a["at"]
    concepts = {}
    totals = {"new": 0, "learning": 0, "weak": 0, "mastered": 0}
    for c in topic.concepts:
        layers = {}
        for layer in range(int(c.get("first_layer", 1)), 4):
            scores = by_cl.get((c["id"], layer), [])
            st = status_of(scores)
            totals[st] += 1
            recent = scores[-RECENT:]
            layers[str(layer)] = {
                "status": st,
                "attempts": len(scores),
                "recent_avg": round(sum(recent) / len(recent), 2) if recent else None,
                "last_at": last_at.get((c["id"], layer)),
            }
        concepts[c["id"]] = {"domain": c["domain"], "layers": layers}
    return {
        "topic": topic.id,
        "learner": learner,
        "updated": now().isoformat(),
        "attempts": len(attempts),
        "totals": totals,
        "concepts": concepts,
        "questions": question_states(attempts),
    }


def write_summary(topic: Topic, learner: str) -> dict:
    summary = build_summary(topic, learner)
    path = progress_dir(learner, topic.id) / "summary.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return summary


def learner_lang(learner: str, default: str) -> str:
    profile = load_yaml(LEARNERS_DIR / learner / "profile.yaml", {}) or {}
    return profile.get("language") or default


def cmd_pick(args) -> int:
    topic = load_topic(resolve_topic(args.topic))
    lang = args.lang or learner_lang(args.learner, topic.languages[0])
    texts = topic.lang_questions(lang)
    summary = build_summary(topic, args.learner)
    qstates = summary["questions"]
    cmap = topic.concept_map()
    order = {c["id"]: i for i, c in enumerate(topic.concepts)}
    dorder = {d: i for i, d in enumerate(topic.domains)}

    def concept_started(cid: str) -> bool:
        layers = summary["concepts"].get(cid, {}).get("layers", {})
        return any(v["status"] in ("learning", "mastered") for v in layers.values())

    pool = []
    for q in topic.all_questions():
        c = cmap.get(q.get("concept"))
        if not c or q["id"] not in texts:
            continue
        if args.layer and q["layer"] != args.layer:
            continue
        if args.domain and c["domain"] != args.domain:
            continue
        if args.concept and c["id"] != args.concept:
            continue
        pool.append((q, c))

    t_now = now()
    due, new, practice = [], [], []
    for q, c in pool:
        st = qstates.get(q["id"])
        if st is None:
            unlocked = all(concept_started(p) for p in c.get("prerequisites") or []) or args.concept
            # a concept's lower layers come first
            lower_pending = any(
                v["status"] == "new"
                for k, v in summary["concepts"][c["id"]]["layers"].items()
                if int(k) < q["layer"]
            )
            if unlocked and not lower_pending:
                new.append((dorder[c["domain"]], order[c["id"]], q["layer"], q["id"], q, "new"))
            continue
        if datetime.fromisoformat(st["due"]) <= t_now:
            due.append((st["last_score"], st["due"], q["id"], q, "review"))
        else:
            practice.append((st["last_score"], st["due"], q["id"], q, "practice"))

    due.sort(key=lambda x: x[:3])
    new.sort(key=lambda x: x[:4])
    practice.sort(key=lambda x: x[:3])
    n_due = min(len(due), max(1, round(args.n * 0.6)) if new else args.n)
    picked = [(x[-2], x[-1]) for x in due[:n_due]]
    picked += [(x[-2], x[-1]) for x in new[: args.n - len(picked)]]
    picked += [(x[-2], x[-1]) for x in due[n_due:]][: args.n - len(picked)]
    picked += [(x[-2], x[-1]) for x in practice][: args.n - len(picked)]

    # interleave: avoid consecutive questions on the same concept when possible
    out, rest = [], picked[:]
    while rest:
        idx = next((i for i, (q, _) in enumerate(rest) if not out or q["concept"] != out[-1]["concept"]), 0)
        q, reason = rest.pop(idx)
        out.append({**q, **{k: v for k, v in texts[q["id"]].items() if k != "id"}, "reason": reason, "lang": lang})

    print(json.dumps({"topic": topic.id, "learner": args.learner, "lang": lang,
                      "available": {"review": len(due), "new": len(new), "practice": len(practice)},
                      "questions": out}, ensure_ascii=False, indent=2))
    return 0


def cmd_record(args) -> int:
    topic = load_topic(resolve_topic(args.topic))
    q = next((x for x in topic.all_questions() if x.get("id") == args.question), None)
    if not q:
        print(f"Unknown question '{args.question}' in topic '{topic.id}'")
        return 1
    score = RESULTS[args.result] if args.score is None else args.score
    if not 0.0 <= score <= 1.0:
        print("score must be between 0 and 1")
        return 1
    attempt = {
        "at": now().isoformat(),
        "question": q["id"],
        "concept": q["concept"],
        "layer": q["layer"],
        "mode": args.mode,
        "lang": args.lang or learner_lang(args.learner, topic.languages[0]),
        "result": args.result,
        "score": round(score, 2),
        "session": args.session,
    }
    if args.feedback:
        attempt["feedback"] = args.feedback
    path = progress_dir(args.learner, topic.id) / "attempts.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(attempt, ensure_ascii=False) + "\n")
    summary = write_summary(topic, args.learner)
    st = summary["concepts"][q["concept"]]["layers"][str(q["layer"])]["status"]
    print(f"recorded {q['id']} ({args.result}, {attempt['score']}) → {q['concept']} layer {q['layer']}: {st}")
    return 0


def cmd_summary(args) -> int:
    topic = load_topic(resolve_topic(args.topic))
    summary = write_summary(topic, args.learner)
    print(f"{topic.id} · {args.learner} · {summary['attempts']} attempts · {summary['totals']}")
    for domain in topic.domains:
        print(f"\n[{domain}]")
        for cid, c in summary["concepts"].items():
            if c["domain"] != domain:
                continue
            cells = "  ".join(f"L{k}:{v['status']}" for k, v in c["layers"].items())
            print(f"  {cid:<28} {cells}")
    return 0


def main() -> int:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    for name in ("pick", "record", "summary"):
        s = sub.add_parser(name)
        s.add_argument("topic")
        s.add_argument("learner")
        if name in ("pick", "record"):
            s.add_argument("--lang")
    pick = sub.choices["pick"]
    pick.add_argument("--n", type=int, default=10)
    pick.add_argument("--layer", type=int, choices=[1, 2, 3])
    pick.add_argument("--domain")
    pick.add_argument("--concept")
    rec = sub.choices["record"]
    rec.add_argument("--question", required=True)
    rec.add_argument("--result", required=True, choices=list(RESULTS))
    rec.add_argument("--score", type=float)
    rec.add_argument("--session", required=True)
    rec.add_argument("--feedback")
    rec.add_argument("--mode", default="chat", choices=["chat", "anki"])
    args = p.parse_args()
    return {"pick": cmd_pick, "record": cmd_record, "summary": cmd_summary}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
