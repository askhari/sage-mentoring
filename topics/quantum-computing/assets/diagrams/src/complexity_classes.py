"""Complexity classes -> complexity-classes.<lang>.svg

Proven: P ⊆ BPP ⊆ BQP ⊆ PSPACE (and NP ⊆ PSPACE). Believed: NP and BQP incomparable,
NP-complete problems outside BQP. Factoring in BQP (Shor), not known to be in BPP.
"""
from __future__ import annotations

from svgkit import ACCENT, ACCENT2, ACCENT3, INK, MUTED, circle, ellipse, svg, text, write

LABELS = {
    "es": {
        "factoring": "factorización",
        "npc": "NP-completos",
        "npc2": "(SAT, viajante…)",
        "proven": "Demostrado: P ⊆ BPP ⊆ BQP ⊆ PSPACE.",
        "believed": "Creencia, no demostrada: BQP y NP son incomparables y los NP-completos quedan fuera de BQP.",
        "fact_note": "La factorización está en BQP (Shor); no se sabe si está en BPP.",
    },
}

W, H = 900, 620


def build(lang: str) -> str:
    t = LABELS[lang]
    b: list[str] = []
    b.append(ellipse(450, 280, 420, 250, INK, "#f4f4f4", 1.8))
    b.append(text(450, 60, "PSPACE", 20, INK, weight="bold"))
    b.append(ellipse(350, 300, 230, 170, ACCENT, "#dbe9f6", 2, opacity=0.8))
    b.append(text(220, 230, "BQP", 20, ACCENT, weight="bold"))
    b.append(ellipse(560, 300, 230, 170, ACCENT2, "#fde3d3", 2, opacity=0.55))
    b.append(text(700, 230, "NP", 20, ACCENT2, weight="bold"))
    b.append(ellipse(370, 330, 130, 80, ACCENT3, "#e3f2e8", 2, opacity=0.9))
    b.append(text(330, 300, "BPP", 17, ACCENT3, weight="bold"))
    b.append(ellipse(430, 350, 48, 34, INK, "white", 1.6))
    b.append(text(430, 357, "P", 17, INK, weight="bold"))
    b.append(circle(470, 200, 6, ACCENT, ACCENT))
    b.append(text(482, 205, t["factoring"], 14, INK, anchor="start"))
    b.append(text(680, 330, t["npc"], 14, ACCENT2, weight="bold"))
    b.append(text(680, 350, t["npc2"], 13, ACCENT2))
    b.append(text(W / 2, 555, t["proven"], 14, INK))
    b.append(text(W / 2, 577, t["believed"], 14, MUTED))
    b.append(text(W / 2, 599, t["fact_note"], 14, MUTED))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"complexity-classes.{lang}.svg", build(lang)))
