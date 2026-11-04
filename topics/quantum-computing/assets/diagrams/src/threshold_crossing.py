"""Logical vs physical error for several surface-code distances -> threshold-crossing.<lang>.svg

Fowler et al. 2012 fit (Eqs. 10-11): P_L ≈ 0.03 · (p / p_th)^floor((d+1)/2), p_th = 0.0057.
All curves meet at p = p_th (P_L = 0.03). The fit is meant for p below threshold; the
part above p_th is drawn dashed. Computed here; a 2012 model fit, not a measurement.
"""
from __future__ import annotations

import math

from svgkit import ACCENT, ACCENT2, ACCENT3, INK, MUTED, circle, line, svg, text, write

PTH, A = 0.0057, 0.03
DS = [3, 5, 7, 9, 11]
COLS = [MUTED, ACCENT3, ACCENT, "#7b4fa0", ACCENT2]
LABELS = {
    "es": {
        "x": "error físico por operación p (escala logarítmica)",
        "y": "error lógico por ciclo P_L",
        "th": "umbral p_th ≈ 0,57 %",
        "below": "por debajo del umbral, más distancia = menos error",
        "above": "por encima, más distancia = peor",
        "note": "Ajuste de Fowler et al. (2012): P_L ≈ 0,03·(p/p_th)^⌊(d+1)/2⌋. Modelo de 2012, no una medida; válido por debajo del umbral.",
    },
}

W, H = 1100, 560
X0, Y0, PW, PH = 120, 470, 720, 400
PMIN, PMAX = 1e-4, 1e-2
LMIN, LMAX = 1e-12, 1.0


def px(p):
    return X0 + (math.log10(p) - math.log10(PMIN)) / (math.log10(PMAX) - math.log10(PMIN)) * PW


def py(v):
    v = min(max(v, LMIN), LMAX)
    return Y0 - (math.log10(v) - math.log10(LMIN)) / (math.log10(LMAX) - math.log10(LMIN)) * PH


def sci(v):
    m, e = f"{v:.1e}".split("e")
    sup = str(int(e)).replace("-", "⁻").translate(str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹"))
    return f"{m.replace('.', ',')}·10{sup}"


def pl(p, d):
    return A * (p / PTH) ** ((d + 1) // 2)


def build(lang: str) -> str:
    t = LABELS[lang]
    b: list[str] = []
    b.append(line(X0, Y0, X0 + PW, Y0, INK, 1.3))
    b.append(line(X0, Y0, X0, Y0 - PH, INK, 1.3))
    for e in range(-4, -1):
        for m in (1,):
            p = m * 10 ** e
            b.append(line(px(p), Y0, px(p), Y0 + 6, INK, 1))
        lab = {-4: "0,01 %", -3: "0,1 %", -2: "1 %"}[e]
        b.append(text(px(10 ** e), Y0 + 22, lab, 12))
    b.append(text(px(1e-2), Y0 + 22, "1 %", 12))
    for e in range(-12, 1, 2):
        b.append(line(X0 - 6, py(10 ** e), X0, py(10 ** e), INK, 1))
        b.append(text(X0 - 10, py(10 ** e) + 4, sci(10 ** e).replace("1,0·", "") if e else "1", 12, anchor="end"))
    b.append(text(X0 + PW / 2, Y0 + 48, t["x"], 13, MUTED))
    b.append(text(X0 - 10, Y0 - PH - 14, t["y"], 13, MUTED, anchor="start"))
    # threshold line
    b.append(line(px(PTH), Y0, px(PTH), Y0 - PH, MUTED, 1.2, dash="5 4"))
    b.append(text(px(PTH) - 6, Y0 - PH + 14, t["th"], 12, MUTED, anchor="end"))
    for d, col in zip(DS, COLS):
        for lo, hi, dash in ((PMIN, PTH, None), (PTH, PMAX, "6 4")):
            pts = []
            n = 80
            for i in range(n + 1):
                p = 10 ** (math.log10(lo) + (math.log10(hi) - math.log10(lo)) * i / n)
                pts.append(f"{'M' if i == 0 else 'L'}{px(p):.1f},{py(pl(p, d)):.1f}")
            ds = f" stroke-dasharray='{dash}'" if dash else ""
            b.append(f"<path d='{' '.join(pts)}' stroke='{col}' fill='none' stroke-width='2.2'{ds}/>")
        # label at p = 1e-3
        b.append(circle(px(1e-3), py(pl(1e-3, d)), 4, col, col))
        v = sci(pl(1e-3, d))
        b.append(text(px(1e-3) - 8, py(pl(1e-3, d)) + 4, f"d = {d}: {v}", 12, col, anchor="end"))
    b.append(circle(px(PTH), py(A), 5, INK, "white", 2))
    b.append(text(X0 + PW - 4, Y0 - 40, t["below"], 13, INK, anchor="end"))
    b.append(text(X0 + PW - 4, Y0 - 20, t["above"], 13, INK, anchor="end"))
    b.append(text(W / 2, H - 10, t["note"], 12, MUTED))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"threshold-crossing.{lang}.svg", build(lang)))
