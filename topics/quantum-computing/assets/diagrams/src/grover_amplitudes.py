"""Amplitudes in one Grover iteration, N = 8, one marked item -> grover-amplitudes.<lang>.svg

Computed exactly: uniform 1/sqrt(N); oracle flips the marked sign; diffusion maps each
amplitude v to 2·mean − v ("inversion about the mean").
"""
from __future__ import annotations

import math

from svgkit import ACCENT, ACCENT2, INK, MUTED, line, rect, svg, text, write

N, MARK = 8, 5
LABELS = {
    "es": {
        "p1": "1. Tras H⊗ⁿ: todas iguales",
        "p2": "2. Tras el oráculo Z_f: la marcada cambia de signo",
        "p3": "3. Tras la difusión (inversión respecto a la media)",
        "mean": "media",
        "note": "N = 8, elemento marcado x = {m}. Tras una iteración, la probabilidad de la marcada pasa de 1/8 = 0,125 a {p}.",
    },
}

W, H = 1120, 380
SCALE = 150   # px per unit amplitude


def panel(b, x0, title, amps, mean=None):
    y0 = 200
    b.append(text(x0 + 150, 50, title, 14, INK, weight="bold"))
    b.append(line(x0, y0, x0 + 300, y0, INK, 1.2))
    bw = 26
    for i, a in enumerate(amps):
        x = x0 + 12 + i * 36
        h = a * SCALE
        col = ACCENT2 if i == MARK else ACCENT
        b.append(rect(x, y0 - max(h, 0), bw, abs(h), col, col, 1))
        b.append(text(x + bw / 2, y0 + (20 if h >= 0 else -h + 18), str(i), 12, MUTED))
        b.append(text(x + bw / 2, y0 - h - 6 if h >= 0 else y0 - h + 34, f"{a:+.2f}".replace(".", ","), 10, col))
    if mean is not None:
        ym = y0 - mean * SCALE
        b.append(line(x0, ym, x0 + 300, ym, MUTED, 1.2, dash="5 4"))
        b.append(text(x0 + 302, ym + 4, t_mean, 11, MUTED, anchor="start"))


def build(lang: str) -> str:
    global t_mean
    t = LABELS[lang]
    t_mean = t["mean"]
    a1 = [1 / math.sqrt(N)] * N
    a2 = [(-v if i == MARK else v) for i, v in enumerate(a1)]
    m = sum(a2) / N
    a3 = [2 * m - v for v in a2]
    b: list[str] = []
    panel(b, 20, t["p1"], a1)
    panel(b, 395, t["p2"], a2, mean=m)
    panel(b, 770, t["p3"], a3)
    p = f"{a3[MARK] ** 2:.3f}".replace(".", ",")
    b.append(text(W / 2, H - 20, t["note"].format(m=MARK, p=p), 14, MUTED))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"grover-amplitudes.{lang}.svg", build(lang)))
