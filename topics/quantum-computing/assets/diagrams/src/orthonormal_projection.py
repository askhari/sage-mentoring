"""Expanding a vector in a rotated orthonormal basis -> orthonormal-projection.<lang>.svg

v in R²; orthonormal basis e1, e2 rotated by θ from the axes; components ⟨e1,v⟩ e1 and
⟨e2,v⟩ e2 computed explicitly; they form a right triangle with v, so ||v||² is the sum of
the squared components (Pythagoras).
"""
from __future__ import annotations

import math

from svgkit import ACCENT, ACCENT2, ACCENT3, INK, MUTED, line, path, svg, text, write

LABELS = {
    "es": {
        "v": "v",
        "e1": "e₁",
        "e2": "e₂",
        "c1": "⟨e₁, v⟩ e₁",
        "c2": "⟨e₂, v⟩ e₂",
        "pyth": "‖v‖² = |⟨e₁, v⟩|² + |⟨e₂, v⟩|²",
        "sum": "v = ⟨e₁, v⟩ e₁ + ⟨e₂, v⟩ e₂",
    },
}

W, H = 640, 520
OX, OY, U = 170, 400, 90
THETA = math.radians(25)
V = (3.0, 2.6)


def px(x: float, y: float) -> tuple[float, float]:
    return OX + x * U, OY - y * U


def build(lang: str) -> str:
    t = LABELS[lang]
    e1 = (math.cos(THETA), math.sin(THETA))
    e2 = (-math.sin(THETA), math.cos(THETA))
    c1 = V[0] * e1[0] + V[1] * e1[1]
    c2 = V[0] * e2[0] + V[1] * e2[1]
    p1 = (c1 * e1[0], c1 * e1[1])
    b: list[str] = []
    # standard axes (faint)
    b.append(line(OX - 60, OY, W - 40, OY, MUTED, 1, arrow="muted"))
    b.append(line(OX, OY + 50, OX, 40, MUTED, 1, arrow="muted"))
    # basis vectors (unit length) — drawn first, thick
    for e, lab, col, ar in ((e1, t["e1"], ACCENT3, "a3"), (e2, t["e2"], ACCENT3, "a3")):
        x, y = px(*e)
        b.append(line(OX, OY, x, y, col, 3.5, arrow=ar))
        b.append(text(x + (14 if e is e1 else -16), y + (18 if e is e1 else -4), lab, 18, col, weight="bold"))
    # component along e1
    x1, y1 = px(*p1)
    b.append(line(OX, OY, x1, y1, ACCENT2, 2, arrow="a2", dash="7,4"))
    mx, my = px(p1[0] / 2, p1[1] / 2)
    b.append(text(mx + 18, my + 28, t["c1"], 15, ACCENT2, anchor="start"))
    # component along e2, drawn from the tip of the first one
    vx, vy = px(*V)
    b.append(line(x1, y1, vx, vy, ACCENT2, 2, arrow="a2", dash="7,4"))
    mx2, my2 = (x1 + vx) / 2, (y1 + vy) / 2
    b.append(text(mx2 + 12, my2 + 6, t["c2"], 15, ACCENT2, anchor="start"))
    # right-angle mark at the foot
    s = 14
    a = (x1 - e1[0] * s, y1 + e1[1] * s)
    c = (a[0] - e2[0] * s, a[1] + e2[1] * s)
    d = (x1 - e2[0] * s, y1 + e2[1] * s)
    b.append(path(f"M{a[0]:.1f},{a[1]:.1f} L{c[0]:.1f},{c[1]:.1f} L{d[0]:.1f},{d[1]:.1f}", INK, width=1.2))
    # v itself
    b.append(line(OX, OY, vx, vy, ACCENT, 3, arrow="a1"))
    b.append(text(vx - 16, vy - 8, t["v"], 20, ACCENT, weight="bold", italic=True))
    # formulas
    b.append(text(W / 2, 50, t["sum"], 17, INK))
    b.append(text(W / 2, 80, t["pyth"], 17, INK))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"orthonormal-projection.{lang}.svg", build(lang)))
