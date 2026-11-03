"""Dephasing of a qubit -> dephasing-bloch-density.<lang>.svg

Start from |+> = (|0> + |1>)/sqrt2, rho = [[1/2, 1/2], [1/2, 1/2]]. Under dephasing the
off-diagonal entries decay as e^{-Gamma t} while the diagonal stays fixed. Bloch vector
r = (2 Re rho01, -2 Im rho01, rho00 - rho11): its x, y components shrink by e^{-Gamma t}
and z is unchanged, so the whole ball flattens onto the z axis. All values computed.
"""
from __future__ import annotations

import math

from svgkit import ACCENT, ACCENT2, INK, MUTED, circle, line, path, rect, svg, text, write

LABELS = {
    "es": {
        "matrix_title": "Matriz densidad de |+⟩ con el tiempo",
        "bloch_title": "Corte x–z de la bola de Bloch",
        "diag": "diagonal: no cambia (poblaciones)",
        "off": "fuera de la diagonal: × e^(−Γt) (coherencias)",
        "ball": "la bola se aplasta hacia el eje z",
    },
}

W, H = 920, 470
TIMES = [0.0, 1.0, 3.0]   # values of Gamma*t


def rho(gt: float):
    c = 0.5 * math.exp(-gt)
    return [[0.5, c], [c, 0.5]]


def build(lang: str) -> str:
    t = LABELS[lang]
    b: list[str] = []
    b.append(text(250, 40, t["matrix_title"], 18, weight="bold"))
    for k, gt in enumerate(TIMES):
        x0, y0 = 40 + k * 150, 90
        m = rho(gt)
        b.append(text(x0 + 60, y0 - 10, f"Γt = {gt:g}", 15, INK))
        for i in range(2):
            for j in range(2):
                v = m[i][j]
                diag = i == j
                f = v / 0.5                       # 0 (white) .. 1 (full colour)
                base = (0x9c, 0xc3, 0xe6) if diag else (0xf4, 0xa2, 0x7a)
                fill = "rgb(" + ",".join(str(round(255 + (c - 255) * f)) for c in base) + ")"
                b.append(rect(x0 + j * 60, y0 + i * 60, 58, 58, ACCENT if diag else ACCENT2, fill, 1.5, rx=4))
                b.append(text(x0 + j * 60 + 29, y0 + i * 60 + 35, f"{v:.2f}", 15, INK))
    b.append(text(40, 260, "■ " + t["diag"], 14, ACCENT, anchor="start"))
    b.append(text(40, 285, "■ " + t["off"], 14, ACCENT2, anchor="start"))
    # Bloch cross-section
    cx, cy, R = 720, 250, 150
    b.append(text(cx, 40, t["bloch_title"], 18, weight="bold"))
    b.append(line(cx - R - 25, cy, cx + R + 25, cy, MUTED, 1, arrow="muted"))
    b.append(line(cx, cy + R + 25, cx, cy - R - 25, MUTED, 1, arrow="muted"))
    b.append(text(cx + R + 30, cy + 5, "x", 15, MUTED, anchor="start", italic=True))
    b.append(text(cx + 8, cy - R - 28, "z", 15, MUTED, anchor="start", italic=True))
    b.append(text(cx + 8, cy - R + 16, "|0⟩", 14, INK, anchor="start"))
    b.append(text(cx + 8, cy + R - 6, "|1⟩", 14, INK, anchor="start"))
    for k, gt in enumerate(TIMES):
        s = math.exp(-gt)
        rx = R * s
        col = ACCENT if k == 0 else ACCENT2
        b.append(path(f"M{cx:.1f},{cy - R:.1f} A{rx:.1f},{R:.1f} 0 1 1 {cx:.1f},{cy + R:.1f} A{rx:.1f},{R:.1f} 0 1 1 {cx:.1f},{cy - R:.1f}",
                      col, width=2 if k == 0 else 1.5))
        # Bloch vector of the state: (2*rho01, 0, 0)
        bx = 2 * rho(gt)[0][1]
        px = cx + bx * R
        b.append(circle(px, cy, 5, stroke=col, fill=col))
        b.append(text(px + 4, cy + 22 + 16 * (k % 2), f"Γt={gt:g}", 12, col, anchor="start" if k else "middle"))
    b.append(line(cx, cy, cx + R - 6, cy, ACCENT, 2.5, arrow="a1"))
    b.append(text(cx, cy + R + 50, t["ball"], 14, MUTED))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"dephasing-bloch-density.{lang}.svg", build(lang)))
