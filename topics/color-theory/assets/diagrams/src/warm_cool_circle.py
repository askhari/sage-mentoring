"""Warm and cool halves of a Munsell-type hue circle -> warm-cool-hue-circle.<lang>.svg

Same ring as hue_circle.py (constant L* 60, C*ab 32). Outer arcs mark the usual
grouping of warm hues (red, orange/yellow-red, yellow) and cool hues (green,
blue-green, blue, purple-blue), as in palmer-2013 (p. 84); the yellow-green and
purple/red-purple sectors are drawn as uncertain zones, because the sources give no
sharp boundary and the association was only tested for red vs blue (ho-2014).
The exact sector limits are a drawing choice, not measured data.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from colormath import MUNSELL_PRINCIPAL, lch_hex, munsell_hue_angle, munsell_hue_number, svg_hue_ring  # noqa: E402

LABELS = {
    "es": {
        "warm": "cálidos",
        "cool": "fríos",
        "unsure": "límite dudoso",
        "names": {"R": "rojo", "YR": "naranja", "Y": "amarillo", "GY": "verde-amarillo", "G": "verde",
                  "BG": "azul-verde", "B": "azul", "PB": "morado-azul", "P": "morado", "RP": "rojo-morado"},
    },
}

# Sectors on the 0-100 Munsell hue circle (R 0-10, YR 10-20, Y 20-30, ... RP 90-100).
SECTORS = [  # (start, end, kind)
    (0.0, 30.0, "warm"),
    (30.0, 40.0, "unsure"),
    (40.0, 80.0, "cool"),
    (80.0, 100.0, "unsure"),
]
STYLE = {"warm": ("#c4501b", ""), "cool": ("#2a5c9a", ""), "unsure": ("#8a8a8a", ' stroke-dasharray="6 5"')}
L_STAR, C_STAR = 60.0, 32.0
W, H = 700, 680
CX, CY = W / 2, H / 2
R_OUT, R_IN, R_ARC = 190, 130, 214
OUT = Path(__file__).resolve().parent.parent


def pos(n: float, r: float) -> tuple[float, float]:
    a = math.radians(-90 + (n - 5) * 3.6)
    return CX + r * math.cos(a), CY + r * math.sin(a)


def arc(n0: float, n1: float, r: float) -> str:
    (x0, y0), (x1, y1) = pos(n0, r), pos(n1, r)
    large = 1 if (n1 - n0) > 50 else 0
    return f"M{x0:.1f},{y0:.1f} A{r},{r} 0 {large} 1 {x1:.1f},{y1:.1f}"


def render(lang: str) -> str:
    t = LABELS[lang]
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="14">',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
    s += svg_hue_ring(pos, R_OUT, R_IN, L_STAR, C_STAR)
    for n0, n1, kind in SECTORS:
        colr, dash = STYLE[kind]
        s.append(f'<path d="{arc(n0 + 0.6, n1 - 0.6, R_ARC)}" fill="none" stroke="{colr}" stroke-width="10"{dash}/>')
    # Dividers between sectors, from the ring to the arc.
    for n in (0.0, 30.0, 40.0, 80.0):
        (x0, y0), (x1, y1) = pos(n, R_IN), pos(n, R_ARC + 8)
        s.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="#555" stroke-width="1"/>')
    # Hue names inside the ring.
    for fam in MUNSELL_PRINCIPAL:
        n = munsell_hue_number(5, fam)
        x, y = pos(n, R_IN - 26)
        s.append(f'<text x="{x:.1f}" y="{y + 4:.1f}" text-anchor="middle" fill="#333" font-size="12">{t["names"][fam]}</text>')
        mx, my = pos(n, (R_OUT + R_IN) / 2)
        s.append(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="6" fill="{lch_hex(L_STAR, C_STAR, munsell_hue_angle(n))}" '
                 f'stroke="#fff" stroke-width="1.5"/>')
    # Sector labels outside the arcs.
    for n, key, colr in [(15.0, "warm", STYLE["warm"][0]), (60.0, "cool", STYLE["cool"][0]),
                         (35.0, "unsure", "#666"), (90.0, "unsure", "#666")]:
        x, y = pos(n, R_ARC + 34)
        anchor = "middle" if abs(x - CX) < 60 else ("start" if x > CX else "end")
        big = key != "unsure"
        weight = ' font-weight="bold"' if big else ""
        s.append(f'<text x="{x:.1f}" y="{y + 5:.1f}" text-anchor="{anchor}" fill="{colr}" '
                 f'font-size="{20 if big else 13}"{weight}>{t[key]}</text>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    for lang in LABELS:
        (OUT / f"warm-cool-hue-circle.{lang}.svg").write_text(render(lang), encoding="utf-8")
        print(f"wrote warm-cool-hue-circle.{lang}.svg")
