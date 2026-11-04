"""Logical error per cycle vs surface-code distance, Google 2024 -> google-lambda.<lang>.svg

Data as cited in logical-qubit-experiments.md (google-2025, arXiv v1): measured
ε_7 = 1.43e-3 per cycle and Λ = 2.14. Points for d = 3 and 5 are derived here from
ε_d = ε_7 · Λ^((7 − d)/2); d = 27 → ~7.1e-7 with 1457 qubits is the authors' extrapolation.
"""
from __future__ import annotations

import math

from svgkit import ACCENT, ACCENT2, INK, MUTED, circle, line, rect, svg, text, write

E7, LAM = 1.43e-3, 2.14
LABELS = {
    "es": {
        "x": "distancia del código d",
        "y": "error lógico por ciclo ε_d (escala logarítmica)",
        "meas": "medido (d = 7)",
        "der": "derivado con Λ = 2,14 (d = 3, 5)",
        "ext": "extrapolación de los autores (d = 27, 1457 qubits)",
        "lam": "cada +2 de distancia divide el error por Λ ≈ 2,14",
        "note": "Procesador de 105 qubits de Google (2024, preprint arXiv v1). Solo el punto d = 7 es una medida directa en este gráfico.",
    },
}

W, H = 1080, 520
X0, Y0, PW, PH = 120, 440, 640, 360
DMIN, DMAX = 1, 29
EMIN, EMAX = 1e-7, 1e-1


def px(d):
    return X0 + (d - DMIN) / (DMAX - DMIN) * PW


def py(e):
    return Y0 - (math.log10(e) - math.log10(EMIN)) / (math.log10(EMAX) - math.log10(EMIN)) * PH


def eps(d):
    return E7 * LAM ** ((7 - d) / 2)


def sci(v):
    m, e = f"{v:.1e}".split("e")
    sup = str(int(e)).replace("-", "⁻").translate(str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹"))
    return f"{m.replace('.', ',')}·10{sup}"


def build(lang: str) -> str:
    t = LABELS[lang]
    b: list[str] = []
    b.append(line(X0, Y0, X0 + PW, Y0, INK, 1.3))
    b.append(line(X0, Y0, X0, Y0 - PH, INK, 1.3))
    for d in (3, 5, 7, 9, 11, 15, 19, 23, 27):
        b.append(line(px(d), Y0, px(d), Y0 + 6, INK, 1))
        b.append(text(px(d), Y0 + 22, str(d), 12))
    for e in range(-7, 0):
        b.append(line(X0 - 6, py(10 ** e), X0, py(10 ** e), INK, 1))
        b.append(text(X0 - 10, py(10 ** e) + 4, sci(10 ** e).replace("1,0·", ""), 12, anchor="end"))
    b.append(text(X0 + PW / 2, Y0 + 46, t["x"], 13, MUTED))
    b.append(text(X0 - 10, Y0 - PH - 14, t["y"], 13, MUTED, anchor="start"))
    # trend line
    b.append(line(px(3), py(eps(3)), px(27), py(eps(27)), MUTED, 1.4, dash="6 4"))
    b.append(text(px(17), py(eps(17)) - 14, t["lam"], 12, MUTED, anchor="start"))
    # derived
    for d in (3, 5):
        b.append(circle(px(d), py(eps(d)), 7, ACCENT, "white", 2.2))
        b.append(text(px(d) + 12, py(eps(d)) + 4, sci(eps(d)), 12, ACCENT, anchor="start"))
    # measured
    b.append(circle(px(7), py(E7), 8, ACCENT2, ACCENT2))
    b.append(text(px(7) + 12, py(E7) + 4, "1,43·10⁻³", 12, ACCENT2, anchor="start"))
    # extrapolated
    x, y = px(27), py(eps(27))
    b.append(rect(x - 7, y - 7, 14, 14, MUTED, "#eeeeee", 2))
    b.append(text(x - 12, y + 24, sci(eps(27)), 12, MUTED, anchor="end"))
    # legend
    lx, ly = X0 + PW + 30, 120
    b.append(circle(lx, ly, 8, ACCENT2, ACCENT2)); b.append(text(lx + 16, ly + 4, t["meas"], 12, INK, anchor="start"))
    b.append(circle(lx, ly + 30, 7, ACCENT, "white", 2.2)); b.append(text(lx + 16, ly + 34, t["der"], 12, INK, anchor="start"))
    b.append(rect(lx - 7, ly + 53, 14, 14, MUTED, "#eeeeee", 2)); b.append(text(lx + 16, ly + 64, t["ext"].split(" (")[0], 12, INK, anchor="start"))
    b.append(text(lx + 16, ly + 80, "(" + t["ext"].split(" (")[1], 12, INK, anchor="start"))
    b.append(text(W / 2, H - 10, t["note"], 12, MUTED))
    return svg(W, H, b)


if __name__ == "__main__":
    assert abs(eps(27) - 7.1e-7) / 7.1e-7 < 0.02 and 2 * 27 * 27 - 1 == 1457
    for lang in LABELS:
        print(write(f"google-lambda.{lang}.svg", build(lang)))
