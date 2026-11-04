"""Zero-noise extrapolation of the worked case -> zne-extrapolation.<lang>.svg

Data: ⟨ZZZZ⟩ of a 4-qubit GHZ with every CX folded 1, 3, 5 times, 2 % depolarising noise
per CX, simulated with Qiskit Aer (one run, values printed in error-mitigation.md).
Two fits are extrapolated to λ = 0, computed here: a least-squares line and an
exponential (a line fitted to log E).
"""
from __future__ import annotations

import math

from svgkit import ACCENT, ACCENT2, ACCENT3, INK, MUTED, circle, line, svg, text, write

E0 = 1.0
LAMBDAS = [1, 3, 5]
MEASURED = [0.940, 0.834, 0.739]
LABELS = {
    "es": {
        "x": "factor de ruido λ (cada CX repetido λ veces)",
        "y": "⟨ZZZZ⟩",
        "ideal": "valor ideal {v}",
        "meas": "medidas con ruido amplificado",
        "lin": "ajuste lineal → {v}",
        "exp": "ajuste exponencial → {v}",
        "note": "GHZ de 4 qubits, ruido despolarizante del 2 % por CX (Aer, una ejecución). El valor extrapolado depende del modelo de ajuste.",
    },
}

W, H = 1060, 520
X0, Y0, PW, PH = 110, 440, 620, 360   # plot origin (bottom-left) and size
XMAX, YMIN, YMAX = 5.5, 0.6, 1.05


def px(lam: float) -> float:
    return X0 + lam / XMAX * PW


def py(v: float) -> float:
    return Y0 - (v - YMIN) / (YMAX - YMIN) * PH


def fit_line(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return my - slope * mx, slope


def dec(v: float) -> str:
    return f"{v:.3f}".replace(".", ",")


def build(lang: str) -> str:
    t = LABELS[lang]
    ys = MEASURED
    a_lin, b_lin = fit_line(LAMBDAS, ys)
    a_log, b_log = fit_line(LAMBDAS, [math.log(y) for y in ys])
    e_exp = math.exp(a_log)
    b: list[str] = []
    # axes, ticks
    b.append(line(X0, Y0, X0 + PW, Y0, INK, 1.4))
    b.append(line(X0, Y0, X0, Y0 - PH, INK, 1.4))
    for lam in range(0, 6):
        b.append(line(px(lam), Y0, px(lam), Y0 + 6, INK, 1.2))
        b.append(text(px(lam), Y0 + 24, str(lam), 14))
    for k in range(6, 11):
        v = k / 10
        b.append(line(X0 - 6, py(v), X0, py(v), INK, 1.2))
        b.append(text(X0 - 10, py(v) + 5, dec(v)[:-1] if k < 10 else "1", 13, anchor="end"))
    b.append(text(X0 + PW / 2, Y0 + 52, t["x"], 14, MUTED))
    b.append(text(X0 - 10, Y0 - PH - 14, t["y"], 14, MUTED, anchor="start"))
    # ideal value
    b.append(line(X0, py(E0), X0 + PW, py(E0), ACCENT3, 1.4, dash="6 4"))
    b.append(text(X0 + PW - 4, py(E0) - 8, t["ideal"].format(v=dec(E0)), 13, ACCENT3, anchor="end"))
    # exponential fit curve, sampled
    pts = [(lam / 10, math.exp(a_log + b_log * lam / 10)) for lam in range(0, 56)]
    d = " ".join(f"{'M' if i == 0 else 'L'}{px(x):.1f},{py(y):.1f}" for i, (x, y) in enumerate(pts))
    b.append(f"<path d='{d}' stroke='{ACCENT}' fill='none' stroke-width='2'/>")
    # linear fit
    b.append(line(px(0), py(a_lin), px(5.5), py(a_lin + b_lin * 5.5), ACCENT2, 2, dash="8 5"))
    # measured points and extrapolated values
    for lam, y in zip(LAMBDAS, ys):
        b.append(circle(px(lam), py(y), 6, INK, INK))
    b.append(circle(px(0), py(e_exp), 6, ACCENT, "white", 2.2))
    b.append(circle(px(0), py(a_lin), 6, ACCENT2, "white", 2.2))
    # legend
    lx, ly = X0 + PW + 20, 120
    b.append(circle(lx + 8, ly, 6, INK, INK))
    b.append(text(lx + 22, ly + 5, t["meas"], 13, INK, anchor="start"))
    b.append(line(lx, ly + 34, lx + 16, ly + 34, ACCENT, 2.2))
    b.append(text(lx + 22, ly + 39, t["exp"].format(v=dec(e_exp)), 13, ACCENT, anchor="start"))
    b.append(line(lx, ly + 68, lx + 16, ly + 68, ACCENT2, 2.2, dash="6 4"))
    b.append(text(lx + 22, ly + 73, t["lin"].format(v=dec(a_lin)), 13, ACCENT2, anchor="start"))
    b.append(text(X0 + PW / 2, H - 6, t["note"], 13, MUTED))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"zne-extrapolation.{lang}.svg", build(lang)))
