"""Munsell-type hue circle with opposite hues -> hue-circle.<lang>.svg

Ten principal and intermediate hues (5R ... 5RP) on a ring of constant CIELAB
lightness and chroma (L* 60, C*ab 32, inside sRGB for every hue). Hue angles come
from colormath.munsell_hue_angle (interpolated from measured paints), so colours
are approximate. Dashed lines join each hue with the one opposite on the circle
(five steps away), passing through the neutral grey at the centre.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from colormath import MUNSELL_PRINCIPAL, lch_hex, munsell_hue_angle, munsell_hue_number  # noqa: E402

LABELS = {
    "es": {
        "names": {"R": "rojo", "YR": "amarillo-rojo", "Y": "amarillo", "GY": "verde-amarillo", "G": "verde",
                  "BG": "azul-verde", "B": "azul", "PB": "morado-azul", "P": "morado", "RP": "rojo-morado"},
        "centre": "gris neutro",
    },
}

L_STAR, C_STAR = 60.0, 32.0
W = H = 640
CX, CY = W / 2, H / 2 + 6
R_OUT, R_IN = 205, 140
OUT = Path(__file__).resolve().parent.parent


def pos(hue_number: float, r: float) -> tuple[float, float]:
    # 5R at the top, hues advancing clockwise (R -> YR -> Y ...), as in Munsell's circle.
    a = math.radians(-90 + (hue_number - 5) * 3.6)
    return CX + r * math.cos(a), CY + r * math.sin(a)


def render(lang: str) -> str:
    t = LABELS[lang]
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="14">',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
    # Continuous ring: 100 wedges, one per Munsell hue step.
    for i in range(100):
        n0, n1 = i - 0.5, i + 0.52
        col = lch_hex(L_STAR, C_STAR, munsell_hue_angle(i))
        p = [pos(n0, R_OUT), pos(n1, R_OUT), pos(n1, R_IN), pos(n0, R_IN)]
        s.append(f'<path d="M{p[0][0]:.1f},{p[0][1]:.1f} A{R_OUT},{R_OUT} 0 0 1 {p[1][0]:.1f},{p[1][1]:.1f} '
                 f'L{p[2][0]:.1f},{p[2][1]:.1f} A{R_IN},{R_IN} 0 0 0 {p[3][0]:.1f},{p[3][1]:.1f} Z" fill="{col}" stroke="{col}" stroke-width="0.8"/>')
    # Neutral centre (same lightness, chroma 0).
    grey = lch_hex(L_STAR, 0, 0)
    # Opposite pairs: dashed lines between the five-step hues (5R-5BG, 5YR-5B, ...).
    for k, fam in enumerate(MUNSELL_PRINCIPAL[:5]):
        a = pos(munsell_hue_number(5, fam), R_IN - 6)
        b = pos(munsell_hue_number(5, MUNSELL_PRINCIPAL[k + 5]), R_IN - 6)
        s.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" '
                 f'stroke="#444" stroke-width="1.2" stroke-dasharray="5 4"/>')
    s.append(f'<circle cx="{CX}" cy="{CY}" r="46" fill="{grey}" stroke="#555" stroke-width="1"/>')
    s.append(f'<text x="{CX}" y="{CY - 4}" text-anchor="middle" fill="#fff" font-weight="bold">N</text>')
    s.append(f'<text x="{CX}" y="{CY + 14}" text-anchor="middle" fill="#fff" font-size="12">{t["centre"]}</text>')
    # Markers and labels for the ten hues.
    for fam in MUNSELL_PRINCIPAL:
        n = munsell_hue_number(5, fam)
        col = lch_hex(L_STAR, C_STAR, munsell_hue_angle(n))
        mx, my = pos(n, (R_OUT + R_IN) / 2)
        s.append(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="15" fill="{col}" stroke="#fff" stroke-width="2"/>')
        lx, ly = pos(n, R_OUT + 34)
        anchor = "middle" if abs(lx - CX) < 40 else ("start" if lx > CX else "end")
        if anchor != "middle":
            lx += -18 if anchor == "start" else 18
        s.append(f'<text x="{lx:.1f}" y="{ly - 2:.1f}" text-anchor="{anchor}" fill="#222" font-weight="bold">5{fam}</text>')
        s.append(f'<text x="{lx:.1f}" y="{ly + 15:.1f}" text-anchor="{anchor}" fill="#444" font-size="13">{t["names"][fam]}</text>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    for lang in LABELS:
        (OUT / f"hue-circle.{lang}.svg").write_text(render(lang), encoding="utf-8")
        print(f"wrote hue-circle.{lang}.svg")
