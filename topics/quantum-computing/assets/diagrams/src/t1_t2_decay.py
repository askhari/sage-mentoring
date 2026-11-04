"""T1 relaxation and T2 dephasing of one transmon -> t1-t2-decay.<lang>.svg

Values from Krantz et al. 2019, pp. 15-17 (one device): T1 = 85 µs, Ramsey T2* ≈ 95 µs
(98 µs in the text), Hahn-echo T2E = 120 µs. Bound T2 ≤ 2·T1 = 170 µs.
Curves are exponentials computed here; the Ramsey fringes use an illustrative detuning.
"""
from __future__ import annotations

import math

from svgkit import ACCENT, ACCENT2, ACCENT3, INK, MUTED, line, svg, text, write

T1, T2S, T2E = 85.0, 95.0, 120.0
LABELS = {
    "es": {
        "p1": "Relajación: población de |1⟩",
        "p2": "Desfase: Ramsey (T2*) y eco de Hahn (T2E)",
        "t": "tiempo (µs)",
        "t1": "e^(−t/T1), T1 = 85 µs",
        "ramsey": "Ramsey, T2* ≈ 95 µs",
        "echo": "eco, T2E = 120 µs",
        "bound": "2·T1 = 170 µs (cota de T2)",
        "note": "Un mismo transmon (Krantz et al. 2019). T2* es 95 µs en el pie de figura y 98 µs en el texto.",
    },
}

W, H = 1160, 430
PW, PH, Y0 = 470, 280, 350
TMAX = 300


def axes(b, x0, title, t):
    b.append(text(x0 + PW / 2, 46, title, 15, INK, weight="bold"))
    b.append(line(x0, Y0, x0 + PW, Y0, INK, 1.3))
    b.append(line(x0, Y0, x0, Y0 - PH, INK, 1.3))
    for v in range(0, TMAX + 1, 50):
        x = x0 + v / TMAX * PW
        b.append(line(x, Y0, x, Y0 + 5, INK, 1))
        b.append(text(x, Y0 + 21, str(v), 12))
    for k in (0, 0.5, 1):
        y = Y0 - k * PH
        b.append(line(x0 - 5, y, x0, y, INK, 1))
        b.append(text(x0 - 9, y + 4, str(k).replace(".", ","), 12, anchor="end"))
    b.append(text(x0 + PW / 2, Y0 + 44, t["t"], 13, MUTED))


def curve(b, x0, f, color, width=2.2, dash=None, n=600):
    pts = []
    for i in range(n + 1):
        tt = TMAX * i / n
        pts.append(f"{'M' if i == 0 else 'L'}{x0 + tt / TMAX * PW:.1f},{Y0 - f(tt) * PH:.1f}")
    d = f" stroke-dasharray='{dash}'" if dash else ""
    b.append(f"<path d='{' '.join(pts)}' stroke='{color}' fill='none' stroke-width='{width}'{d}/>")


def build(lang: str) -> str:
    t = LABELS[lang]
    b: list[str] = []
    xa, xb = 70, 650
    axes(b, xa, t["p1"], t)
    curve(b, xa, lambda s: math.exp(-s / T1), ACCENT)
    b.append(text(xa + 170, Y0 - 0.62 * PH, t["t1"], 13, ACCENT, anchor="start"))
    axes(b, xb, t["p2"], t)
    det = 2 * math.pi / 40.0   # illustrative Ramsey detuning: one fringe per 40 µs
    curve(b, xb, lambda s: 0.5 + 0.5 * math.exp(-s / T2S) * math.cos(det * s), ACCENT2, 1.2)
    curve(b, xb, lambda s: 0.5 + 0.5 * math.exp(-s / T2S), ACCENT2, 1.6, dash="5 4")
    curve(b, xb, lambda s: 0.5 + 0.5 * math.exp(-s / T2E), ACCENT3, 2.4)
    xbound = xb + 170 / TMAX * PW
    b.append(line(xbound, Y0, xbound, Y0 - PH, MUTED, 1.4, dash="6 4"))
    b.append(text(xbound + 6, Y0 - PH + 14, t["bound"], 12, MUTED, anchor="start"))
    b.append(text(xb + 300, Y0 - 0.80 * PH, t["echo"], 13, ACCENT3, anchor="start"))
    b.append(text(xb + 300, Y0 - 0.70 * PH, t["ramsey"], 13, ACCENT2, anchor="start"))
    b.append(text(W / 2, H - 6, t["note"], 13, MUTED))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"t1-t2-decay.{lang}.svg", build(lang)))
