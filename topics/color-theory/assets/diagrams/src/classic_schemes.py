"""Classic colour schemes on a Munsell-type hue circle -> classic-schemes-hue-circle.<lang>.svg

Five small hue rings (constant L* 60, C*ab 32, as in hue_circle.py) with the hues of
each scheme marked: monochromatic (one hue, several values), analogous (neighbours),
complementary (opposites), split complementary (a hue and the two neighbours of its
opposite) and triad (three equally spaced hues). Opposites here are Munsell
opposites; on a traditional RYB painter's wheel the pairs differ (see color-wheels-comparison).
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from colormath import lch_hex, max_srgb_chroma, munsell_hue_angle, svg_hue_ring  # noqa: E402

LABELS = {
    "es": {
        "titles": ["Monocromático", "Análogo", "Complementario", "Complementario dividido", "Tríada"],
        "notes": ["un matiz, varios valores", "matices vecinos", "matices opuestos",
                  "un matiz y los vecinos de su opuesto", "tres matices equidistantes"],
    },
}

# Marked hues per scheme, as Munsell hue numbers (5R = 5, 5Y = 25, 5PB = 75 ...).
SCHEMES = [
    [75.0],                       # monochromatic: 5PB
    [15.0, 25.0, 35.0],           # analogous: 5YR, 5Y, 5GY
    [25.0, 75.0],                 # complementary: 5Y - 5PB
    [25.0, 65.0, 85.0],           # split complementary: 5Y + 5B, 5P
    [5.0, 5.0 + 100 / 3, 5.0 + 200 / 3],  # triad
]
L_STAR, C_STAR = 60.0, 32.0
PW, PH = 320, 300
W, H = PW * 3, PH * 2 + 20
R_OUT, R_IN = 100, 74
OUT = Path(__file__).resolve().parent.parent


def render(lang: str) -> str:
    t = LABELS[lang]
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="14">',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
    for k, hues in enumerate(SCHEMES):
        row, col = divmod(k, 3)
        ox = col * PW + (PW / 2 if row == 1 else 0)  # centre the second row of two
        cx, cy = ox + PW / 2, row * PH + 125

        def pos(n: float, r: float, cx=cx, cy=cy) -> tuple[float, float]:
            a = math.radians(-90 + (n - 5) * 3.6)
            return cx + r * math.cos(a), cy + r * math.sin(a)

        s += svg_hue_ring(pos, R_OUT, R_IN, L_STAR, C_STAR)
        pts = [pos(n, (R_OUT + R_IN) / 2) for n in hues]
        if len(pts) > 1 and k != 1:  # analogous hues are neighbours: no connecting lines
            inner = [pos(n, R_IN - 4) for n in hues]
            d = " ".join(f"{'M' if i == 0 else 'L'}{x:.1f},{y:.1f}" for i, (x, y) in enumerate(inner))
            closed = " Z" if len(pts) > 2 else ""
            s.append(f'<path d="{d}{closed}" fill="none" stroke="#444" stroke-width="1.4" stroke-dasharray="5 4"/>')
        elif len(pts) == 1:
            # Monochromatic: the same hue at four values, shown as swatches in the centre.
            h = munsell_hue_angle(hues[0])
            for i, l in enumerate([30, 45, 60, 75]):
                c = min(24.0, max_srgb_chroma(l, h))
                s.append(f'<rect x="{cx - 46 + i * 23:.1f}" y="{cy - 14:.1f}" width="23" height="28" '
                         f'fill="{lch_hex(l, c, h)}" stroke="#fff" stroke-width="1"/>')
        for (x, y), n in zip(pts, hues):
            colr = lch_hex(L_STAR, C_STAR, munsell_hue_angle(n))
            s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="14" fill="{colr}" stroke="#222" stroke-width="2.5"/>')
        s.append(f'<text x="{cx:.1f}" y="{cy + R_OUT + 32:.1f}" text-anchor="middle" fill="#222" '
                 f'font-weight="bold" font-size="16">{t["titles"][k]}</text>')
        s.append(f'<text x="{cx:.1f}" y="{cy + R_OUT + 52:.1f}" text-anchor="middle" fill="#444" '
                 f'font-size="13">{t["notes"][k]}</text>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    for lang in LABELS:
        (OUT / f"classic-schemes-hue-circle.{lang}.svg").write_text(render(lang), encoding="utf-8")
        print(f"wrote classic-schemes-hue-circle.{lang}.svg")
