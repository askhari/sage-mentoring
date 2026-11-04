"""Grover as a rotation -> grover-rotation.<lang>.svg

Plane spanned by |A0⟩ (non-solutions) and |A1⟩ (solutions). |u⟩ = cos θ|A0⟩ + sin θ|A1⟩ with
sin θ = sqrt(s/N). One iteration = reflection about |A0⟩ (Z_f) then about |u⟩ (2|u⟩⟨u| − I),
i.e. a rotation by 2θ. States after t iterations sit at angle (2t+1)θ. Example N = 40, s = 1.
"""
from __future__ import annotations

import math

from svgkit import ACCENT, ACCENT2, ACCENT3, INK, MUTED, circle, line, path, svg, text, write

N, S = 40, 1
LABELS = {
    "es": {
        "a0": "|A₀⟩ (no soluciones)",
        "a1": "|A₁⟩ (soluciones)",
        "u": "|u⟩",
        "zf": "Z_f|u⟩",
        "rot": "2θ",
        "theta": "θ",
        "legend1": "N = {N}, s = {S}: θ = arcsin √(s/N) ≈ {deg}°",
        "legend2": "Una iteración = reflexión respecto a |A₀⟩ (Z_f) y luego respecto a |u⟩ → giro de 2θ",
        "legend3": "Tras t iteraciones: ángulo (2t+1)θ; con t = {topt} la probabilidad de éxito es sin²((2t+1)θ) ≈ {p}",
        "t": "t = {t}",
    },
}

W, H = 1000, 800
CX, CY, R = 300, 600, 470


def pt(angle, r=R):
    return CX + r * math.cos(angle), CY - r * math.sin(angle)


def arc(a1, a2, r, color, width=1.8, arrow=None):
    x1, y1 = pt(a1, r); x2, y2 = pt(a2, r)
    large = 1 if abs(a2 - a1) > math.pi else 0
    sweep = 0 if a2 > a1 else 1
    a = f" marker-end='url(#arrow-{arrow})'" if arrow else ""
    return f"<path d='M{x1:.1f},{y1:.1f} A{r},{r} 0 {large} {sweep} {x2:.1f},{y2:.1f}' stroke='{color}' fill='none' stroke-width='{width}'{a}/>"


def build(lang: str) -> str:
    t = LABELS[lang]
    th = math.asin(math.sqrt(S / N))
    topt = math.floor(math.pi / (4 * th))
    p = math.sin((2 * topt + 1) * th) ** 2
    b: list[str] = []
    b.append(line(CX - 20, CY, CX + R + 40, CY, INK, 1.5, arrow="ink"))
    b.append(line(CX, CY + 40, CX, CY - R - 40, INK, 1.5, arrow="ink"))
    b.append(text(CX + R + 30, CY + 28, t["a0"], 16, anchor="end"))
    b.append(text(CX - 14, CY - R - 30, t["a1"], 16, anchor="end"))
    b.append(arc(-0.2, math.pi / 2 + 0.05, R, MUTED, 1, None).replace("stroke-width='1'", "stroke-width='1' stroke-dasharray='3 5'"))
    # |u> and its reflection about |A0>
    ux, uy = pt(th); zx, zy = pt(-th)
    b.append(line(CX, CY, ux, uy, ACCENT, 3, arrow="a1"))
    b.append(text(ux + 14, uy + 6, t["u"], 17, ACCENT, anchor="start", weight="bold"))
    b.append(line(CX, CY, zx, zy, ACCENT2, 2, dash="6 4", arrow="a2"))
    b.append(text(zx + 14, zy + 10, t["zf"], 15, ACCENT2, anchor="start"))
    b.append(arc(0, th, 110, INK, 1.4)); b.append(text(*pt(th / 2, 128), t["theta"], 15))
    # states after t = 1..topt
    for k in range(1, topt + 1):
        a = (2 * k + 1) * th
        x, y = pt(a)
        col = ACCENT3 if k == topt else ACCENT
        b.append(line(CX, CY, x, y, col, 2.4 if k == topt else 1.8, arrow="a3" if k == topt else "a1"))
        b.append(text(*pt(a, R + 34), t["t"].format(t=k), 15, col, weight="bold" if k == topt else "normal"))
    # first rotation arc 2θ
    b.append(arc(th, 3 * th, 300, ACCENT2, 2, arrow="a2"))
    b.append(text(*pt(2 * th, 330), t["rot"], 16, ACCENT2, weight="bold"))
    b.append(text(W / 2, 40, t["legend1"].format(N=N, S=S, deg=f"{math.degrees(th):.1f}".replace(".", ",")), 15, anchor="middle"))
    b.append(text(W / 2, H - 50, t["legend2"], 14, MUTED))
    b.append(text(W / 2, H - 25, t["legend3"].format(topt=topt, p=f"{p:.3f}".replace(".", ",")), 14, MUTED))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"grover-rotation.{lang}.svg", build(lang)))
