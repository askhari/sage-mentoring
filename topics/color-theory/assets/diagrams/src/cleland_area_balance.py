"""Cleland's area-balance rule -> cleland-area-balance.<lang>.svg

Cleland (cleland-1921, pp. ~21-22) multiplies Munsell value by chroma for each
colour and makes areas inversely proportional to these products: Y 7/9 (63) against
P-B 3/4 (12) gives about 12 parts yellow to 63 parts purple-blue. Left: equal areas;
right: areas in the ratio 12:63 (yellow as a small patch in a purple-blue field,
both panels the same total size). Colours are approximations of the Munsell
notations (colormath.munsell_approx_hex), not renotation data.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from colormath import munsell_approx_hex, munsell_hue_number  # noqa: E402

LABELS = {
    "es": {
        "equal": "Áreas iguales",
        "balanced": "Áreas según Cleland (12 : 63)",
        "rule": "valor × croma: Y 7/9 → 63 · P-B 3/4 → 12",
    },
}

YELLOW = munsell_approx_hex(munsell_hue_number(5, "Y"), 7, 9)
PURPLE_BLUE = munsell_approx_hex(munsell_hue_number(5, "PB"), 3, 4)
PW, PH = 300, 220          # panel size
GAP = 60
W, H = 2 * PW + GAP + 80, PH + 120
OUT = Path(__file__).resolve().parent.parent


def render(lang: str) -> str:
    t = LABELS[lang]
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="14">',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
    x0, y0 = 40, 20
    # Equal areas: two halves.
    s.append(f'<rect x="{x0}" y="{y0}" width="{PW / 2}" height="{PH}" fill="{YELLOW}"/>')
    s.append(f'<rect x="{x0 + PW / 2}" y="{y0}" width="{PW / 2}" height="{PH}" fill="{PURPLE_BLUE}"/>')
    s.append(f'<rect x="{x0}" y="{y0}" width="{PW}" height="{PH}" fill="none" stroke="#333"/>')
    # Cleland ratio: the yellow patch takes 12/75 of the panel area.
    x1 = x0 + PW + GAP
    side = math.sqrt(PW * PH * 12 / 75)
    s.append(f'<rect x="{x1}" y="{y0}" width="{PW}" height="{PH}" fill="{PURPLE_BLUE}" stroke="#333"/>')
    s.append(f'<rect x="{x1 + (PW - side) / 2:.1f}" y="{y0 + (PH - side) / 2:.1f}" width="{side:.1f}" height="{side:.1f}" fill="{YELLOW}"/>')
    for x, key in [(x0, "equal"), (x1, "balanced")]:
        s.append(f'<text x="{x + PW / 2}" y="{y0 + PH + 26}" text-anchor="middle" fill="#222" font-weight="bold">{t[key]}</text>')
    s.append(f'<text x="{W / 2}" y="{y0 + PH + 62}" text-anchor="middle" fill="#444" font-size="13">{t["rule"]}</text>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    for lang in LABELS:
        (OUT / f"cleland-area-balance.{lang}.svg").write_text(render(lang), encoding="utf-8")
        print(f"wrote cleland-area-balance.{lang}.svg")
