"""Trotter product formula -> trotter-steps.<lang>.svg

e^{-i(A+B)t} split into r slices, each e^{-iAt/r} followed by e^{-iBt/r}; error per slice is
of order (t/r)^2 from the commutator [A, B], so larger r means a better approximation.
"""
from __future__ import annotations

from svgkit import ACCENT, ACCENT2, INK, MUTED, line, rect, svg, text, write

R = 4
LABELS = {
    "es": {
        "exact": "Evolución exacta: e^(−i(A+B)t)",
        "approx": "Aproximación con r = {r} pasos: (e^(−iAt/r) e^(−iBt/r))^r",
        "slice": "un paso: t/r",
        "err": "Si A y B no conmutan, cada paso comete un error de orden (t/r)² debido a [A, B];",
        "err2": "al aumentar r el error total disminuye (si [A, B] = 0, la fórmula es exacta).",
        "time": "tiempo",
    },
}

W, H = 1000, 380


def build(lang: str) -> str:
    t = LABELS[lang]
    x0, x1 = 80, 920
    b: list[str] = []
    b.append(text(x0, 50, t["exact"], 16, anchor="start", weight="bold"))
    b.append(rect(x0, 65, x1 - x0, 46, INK, "#ececec", 1.6, rx=6))
    b.append(text((x0 + x1) / 2, 95, "A + B", 18, INK, weight="bold"))
    b.append(text(x0, 160, t["approx"].format(r=R), 16, anchor="start", weight="bold"))
    sw = (x1 - x0) / R
    for k in range(R):
        xa = x0 + k * sw
        b.append(rect(xa, 175, sw / 2, 46, ACCENT, "#dbe9f6", 1.6, rx=6))
        b.append(text(xa + sw / 4, 205, "A", 18, ACCENT, weight="bold"))
        b.append(rect(xa + sw / 2, 175, sw / 2, 46, ACCENT2, "#fde3d3", 1.6, rx=6))
        b.append(text(xa + 3 * sw / 4, 205, "B", 18, ACCENT2, weight="bold"))
    b.append(line(x0, 240, x0 + sw, 240, MUTED, 1.2, arrow="muted"))
    b.append(line(x0 + sw, 240, x0, 240, MUTED, 1.2, arrow="muted"))
    b.append(text(x0 + sw / 2, 258, t["slice"], 13, MUTED))
    b.append(line(x0, 280, x1 + 30, 280, INK, 1.2, arrow="ink"))
    b.append(text(x1 + 30, 300, t["time"], 13, MUTED, anchor="end"))
    b.append(text(W / 2, 330, t["err"], 14, MUTED))
    b.append(text(W / 2, 352, t["err2"], 14, MUTED))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"trotter-steps.{lang}.svg", build(lang)))
