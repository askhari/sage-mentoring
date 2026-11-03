"""Mach-Zehnder interferometer with path amplitudes -> mach-zehnder-amplitudes.<lang>.svg

Beam splitters are modelled as H = (1/sqrt2)[[1,1],[1,-1]] acting on (upper, lower)
amplitudes and the phase shifter as diag(1, e^{i delta}) on the lower arm. Amplitudes and
detector probabilities are computed with complex arithmetic, not typed in.
"""
from __future__ import annotations

import cmath
import math

from svgkit import ACCENT, ACCENT2, ACCENT3, INK, MUTED, line, rect, svg, text, write

LABELS = {
    "es": {
        "source": "fotón",
        "bs1": "divisor 1",
        "bs2": "divisor 2",
        "mirror": "espejo",
        "phase": "desfase δ",
        "upper": "rama superior",
        "lower": "rama inferior",
        "amp": "amplitudes (sup., inf.)",
        "case0": "Sin desfase (δ = 0):",
        "general": "Con desfase δ:  P(D0) = cos²(δ/2),  P(D1) = sen²(δ/2)",
    },
}

W, H = 900, 600
S = 1 / math.sqrt(2)


def bs(v):
    a, b = v
    return (S * (a + b), S * (a - b))


def fmt(z: complex) -> str:
    if abs(z) < 1e-9:
        return "0"
    if abs(z.imag) < 1e-9:
        r = z.real
        if abs(abs(r) - S) < 1e-9:
            return ("−" if r < 0 else "") + "1/√2"
        return f"{r:g}"
    return f"{z:.2f}"


def build(lang: str) -> str:
    t = LABELS[lang]
    v0 = (1 + 0j, 0j)                  # photon enters the upper port
    v1 = bs(v0)                        # after BS1
    v2 = (v1[0], v1[1] * cmath.exp(0j))  # delta = 0
    v3 = bs(v2)                        # after BS2
    p0, p1 = abs(v3[0]) ** 2, abs(v3[1]) ** 2
    b: list[str] = []
    # geometry: BS1 at (220,150), upper mirror (620,150), lower mirror (220,370), BS2 (620,370)
    x1, x2, yu, yl = 220, 620, 150, 370
    # beams
    b.append(line(60, yu, x1, yu, ACCENT, 3, arrow="a1"))
    b.append(line(x1, yu, x2, yu, ACCENT, 3, arrow="a1"))           # upper arm (transmitted)
    b.append(line(x1, yu, x1, yl, ACCENT, 3, arrow="a1"))           # down to lower mirror
    b.append(line(x1, yl, x2, yl, ACCENT, 3, arrow="a1"))           # lower arm
    b.append(line(x2, yu, x2, yl, ACCENT, 3, arrow="a1"))           # upper mirror down to BS2
    b.append(line(x2, yl, x2 + 170, yl, ACCENT, 3 if p0 > 0.01 else 1, arrow="a1", dash=None if p0 > 0.01 else "4,4"))
    b.append(line(x2, yl, x2, yl + 110, ACCENT, 3 if p1 > 0.01 else 1, arrow="a1", dash=None if p1 > 0.01 else "4,4"))
    # optics
    for (x, y, lab, dy) in ((x1, yu, t["bs1"], -26), (x2, yl, t["bs2"], 40)):
        b.append(line(x - 22, y + 22, x + 22, y - 22, INK, 5))
        b.append(text(x - 30, y + dy, lab, 14, anchor="end"))
    for (x, y) in ((x2, yu), (x1, yl)):
        b.append(line(x - 22, y + 22, x + 22, y - 22, MUTED, 7))
        b.append(text(x + 34, y - 14 if y == yu else y + 30, t["mirror"], 13, MUTED, anchor="start" if y == yu else "end"))
    # phase shifter on lower arm
    b.append(rect(400, yl - 20, 46, 40, ACCENT2, "#fde3d3", 2, rx=4))
    b.append(text(423, yl + 46, t["phase"], 14, ACCENT2))
    b.append(text(70, yu - 16, t["source"], 14, anchor="start"))
    b.append(text(420, yu - 16, t["upper"], 13, MUTED))
    b.append(text(330, yl - 30, t["lower"], 13, MUTED))
    # detectors
    b.append(rect(x2 + 170, yl - 25, 60, 50, INK, "#eeeeee", 2, rx=6))
    b.append(text(x2 + 200, yl + 6, "D0", 16, weight="bold"))
    b.append(rect(x2 - 30, yl + 110, 60, 50, INK, "#eeeeee", 2, rx=6))
    b.append(text(x2, yl + 141, "D1", 16, weight="bold"))
    b.append(text(x2 + 200, yl - 36, f"P = {p0:g}", 15, ACCENT3, weight="bold"))
    b.append(text(x2 + 48, yl + 141, f"P = {p1:g}", 15, ACCENT3, anchor="start", weight="bold"))
    # amplitude vectors
    b.append(text(60, 40, t["case0"] + "  " + t["amp"], 15, anchor="start", weight="bold"))
    b.append(text(110, yu + 30, f"({fmt(v0[0])}, {fmt(v0[1])})", 14, ACCENT, anchor="middle"))
    b.append(text(420, 250, f"({fmt(v2[0])}, {fmt(v2[1])})", 14, ACCENT, anchor="middle"))
    b.append(text(x2 + 95, yl + 30, f"({fmt(v3[0])}, {fmt(v3[1])})", 14, ACCENT, anchor="middle"))
    b.append(text(60, H - 22, t["general"], 15, INK, anchor="start"))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"mach-zehnder-amplitudes.{lang}.svg", build(lang)))
