"""Three colour wheels side by side -> color-wheels-comparison.<lang>.svg

(1) Traditional painter's RYB wheel (12 sectors). Its colours are a conventional
    schematic: RYB is not defined colorimetrically, so there are no exact values.
(2) RGB/CMY wheel of light and screens: 12 fully saturated sRGB hues (HSV hue steps
    of 30°), additive primaries R, G, B and their opposites C, M, Y.
(3) Perceptual Munsell-type circle: 10 hues (5R ... 5RP) at L* 60, C*ab 32, hue
    angles from colormath.munsell_hue_angle (approximate).
On each wheel a line marks red and the hue opposite to it.
"""
from __future__ import annotations

import colorsys
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from colormath import MUNSELL_PRINCIPAL, lch_hex, munsell_hue_angle, munsell_hue_number  # noqa: E402

LABELS = {
    "es": {
        "titles": ["Rueda RYB tradicional", "Rueda RGB/CMY", "Círculo perceptual (Munsell)"],
        "subtitles": ["pintores, primarios rojo-amarillo-azul", "luz y pantallas", "diez matices equiespaciados a la vista"],
        "red": "rojo",
        "opposite": ["opuesto: verde", "opuesto: cian", "opuesto: azul-verde (5BG)"],
        "ryb": ["R", "", "", "", "Y", "", "", "", "B", "", "", ""],
        "rgb": ["R", "", "Y", "", "G", "", "C", "", "B", "", "M", ""],
    },
}

# Conventional RYB wheel (schematic, see module docstring): red, red-orange, orange,
# yellow-orange, yellow, yellow-green, green, blue-green, blue, blue-violet, violet, red-violet.
RYB = ["#d7261e", "#e2531c", "#ef861c", "#f5ae1a", "#f7d417", "#a9c62a", "#3a9a3a",
       "#1f8a86", "#2a5fb0", "#4a46a3", "#7a3d97", "#ad2d6f"]

W, H = 960, 420
R_OUT, R_IN = 120, 52
OUT = Path(__file__).resolve().parent.parent


def wedge(cx, cy, a0, a1, col):
    def pt(a, r):
        return cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))
    p = [pt(a0, R_OUT), pt(a1, R_OUT), pt(a1, R_IN), pt(a0, R_IN)]
    large = 1 if a1 - a0 > 180 else 0
    return (f'<path d="M{p[0][0]:.1f},{p[0][1]:.1f} A{R_OUT},{R_OUT} 0 {large} 1 {p[1][0]:.1f},{p[1][1]:.1f} '
            f'L{p[2][0]:.1f},{p[2][1]:.1f} A{R_IN},{R_IN} 0 {large} 0 {p[3][0]:.1f},{p[3][1]:.1f} Z" '
            f'fill="{col}" stroke="#ffffff" stroke-width="1.5"/>')


def ink(hex_col: str) -> str:
    """Dark text on light sectors, white on dark ones (sRGB luma)."""
    r, g, b = (int(hex_col[i:i + 2], 16) for i in (1, 3, 5))
    return "#222" if 0.299 * r + 0.587 * g + 0.114 * b > 165 else "#fff"


def wheel(cx, cy, colours, labels):
    """Draw sectors with the first one centred at the top, clockwise."""
    n = len(colours)
    step = 360 / n
    # Axis red -> opposite, drawn first so the sectors and labels cover it.
    s = [f'<line x1="{cx}" y1="{cy - R_OUT - 8}" x2="{cx}" y2="{cy + R_OUT + 8}" stroke="#222" stroke-width="2" stroke-dasharray="6 4"/>']
    for i, col in enumerate(colours):
        mid = -90 + i * step
        s.append(wedge(cx, cy, mid - step / 2, mid + step / 2, col))
        if labels and labels[i]:
            r = (R_OUT + R_IN) / 2
            x, y = cx + r * math.cos(math.radians(mid)), cy + r * math.sin(math.radians(mid))
            s.append(f'<text x="{x:.1f}" y="{y + 5:.1f}" text-anchor="middle" fill="{ink(col)}" font-weight="bold" font-size="14">{labels[i]}</text>')
    # Red (top) and its opposite (bottom).
    s.append(f'<circle cx="{cx}" cy="{cy - R_OUT - 8}" r="4" fill="#222"/><circle cx="{cx}" cy="{cy + R_OUT + 8}" r="4" fill="#222"/>')
    return s


def render(lang: str) -> str:
    t = LABELS[lang]
    rgb = []
    for i in range(12):
        r, g, b = colorsys.hsv_to_rgb(i / 12, 1, 1)
        rgb.append("#%02x%02x%02x" % (round(r * 255), round(g * 255), round(b * 255)))
    munsell = [lch_hex(60, 32, munsell_hue_angle(munsell_hue_number(5, f))) for f in MUNSELL_PRINCIPAL]
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="14">',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
    cy = 215
    for k, (cols, labs) in enumerate([(RYB, t["ryb"]), (rgb, t["rgb"]), (munsell, [f"5{f}" if f in ("R", "Y", "G", "B", "P") else "" for f in MUNSELL_PRINCIPAL])]):
        cx = 160 + k * 320
        s.append(f'<text x="{cx}" y="30" text-anchor="middle" font-weight="bold" font-size="16" fill="#222">{t["titles"][k]}</text>')
        s.append(f'<text x="{cx}" y="50" text-anchor="middle" fill="#555" font-size="13">{t["subtitles"][k]}</text>')
        s += wheel(cx, cy, cols, labs)
        s.append(f'<text x="{cx + 10}" y="{cy - R_OUT - 2}" fill="#222" font-size="13">{t["red"]}</text>')
        s.append(f'<text x="{cx}" y="{cy + R_OUT + 34}" text-anchor="middle" fill="#222" font-size="14">{t["opposite"][k]}</text>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    for lang in LABELS:
        (OUT / f"color-wheels-comparison.{lang}.svg").write_text(render(lang), encoding="utf-8")
        print(f"wrote color-wheels-comparison.{lang}.svg")
