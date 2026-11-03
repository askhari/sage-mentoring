"""CHSH game setup -> chsh-game.<lang>.svg

Referee sends uniform bits x to Alice and y to Bob; they answer a and b without
communicating; they win iff a XOR b = x AND y. The classical optimum (3/4) and the quantum
value cos²(π/8) are computed here, the classical one by brute force over deterministic strategies.
"""
from __future__ import annotations

import itertools
import math

from svgkit import ACCENT, ACCENT2, ACCENT3, INK, MUTED, line, rect, svg, text, write

LABELS = {
    "es": {
        "referee": "Árbitro",
        "alice": "Alice",
        "bob": "Bob",
        "no_comm": "sin comunicación",
        "shared": "pueden compartir un par entrelazado",
        "rule": "Ganan si  a ⊕ b = x ∧ y",
        "classical": "mejor estrategia clásica: {c:.0%}",
        "quantum": "estrategia cuántica: cos²(π/8) ≈ {q:.1%}",
    },
}

W, H = 820, 460


def classical_best() -> float:
    best = 0.0
    for fa in itertools.product((0, 1), repeat=2):        # a = fa[x]
        for fb in itertools.product((0, 1), repeat=2):    # b = fb[y]
            wins = sum((fa[x] ^ fb[y]) == (x & y) for x in (0, 1) for y in (0, 1))
            best = max(best, wins / 4)
    return best


def build(lang: str) -> str:
    t = LABELS[lang]
    c, q = classical_best(), math.cos(math.pi / 8) ** 2
    b: list[str] = []
    # referee
    b.append(rect(330, 30, 160, 60, INK, "#eeeeee", 2, rx=8))
    b.append(text(410, 67, t["referee"], 18, weight="bold"))
    # players
    for x, lab in ((90, t["alice"]), (570, t["bob"])):
        b.append(rect(x, 200, 160, 70, ACCENT, "#dbe9f6", 2, rx=8))
        b.append(text(x + 80, 242, lab, 18, weight="bold"))
    # questions and answers (parallel pairs, labels outside the arrows)
    b.append(line(350, 90, 230, 198, ACCENT, 2, arrow="a1")); b.append(text(308, 162, "x", 18, ACCENT, italic=True, weight="bold"))
    b.append(line(190, 198, 312, 92, ACCENT2, 2, arrow="a2")); b.append(text(228, 128, "a", 18, ACCENT2, italic=True, weight="bold"))
    b.append(line(470, 90, 590, 198, ACCENT, 2, arrow="a1")); b.append(text(512, 162, "y", 18, ACCENT, italic=True, weight="bold"))
    b.append(line(630, 198, 508, 92, ACCENT2, 2, arrow="a2")); b.append(text(592, 128, "b", 18, ACCENT2, italic=True, weight="bold"))
    # wall and shared pair
    b.append(line(410, 120, 410, 255, INK, 4, dash="10,6"))
    b.append(text(410, 275, t["no_comm"], 14, MUTED))
    b.append(line(250, 300, 570, 300, ACCENT3, 2, dash="3,4"))
    b.append(text(410, 324, t["shared"], 13, ACCENT3))
    # rule and values
    b.append(text(410, 385, t["rule"], 20, INK, weight="bold"))
    b.append(text(410, 418, t["classical"].format(c=c), 15, MUTED))
    b.append(text(410, 442, t["quantum"].format(q=q), 15, ACCENT3, weight="bold"))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"chsh-game.{lang}.svg", build(lang)))
