"""Equiluminant vs non-equiluminant figure, in colour and as lightness only -> equiluminance.<lang>.svg

An orange disc on a blue-grey ground. Left: disc and ground share CIELAB L*
(equiluminant in this approximation). Right: the disc is much lighter. The bottom
row keeps only L* (C* = 0), a stand-in for what a lightness-only view (a
black-and-white photo, or squinting) keeps: the equiluminant disc disappears.
L* is computed for the CIE standard observer and an sRGB display; on a real
screen and for a given person the equiluminant point shifts, so the effect varies.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from colormath import lch_hex  # noqa: E402

OUT = Path(__file__).resolve().parent.parent
LABELS = {
    "es": {
        "title": "Equiluminancia: color distinto, misma luminosidad",
        "eq": "misma luminosidad (L* 60)",
        "neq": "disco más claro (L* 85)",
        "colour": "en color",
        "grey": "solo luminosidad",
    },
}

GROUND = (60, 18, 250)
DISC_EQ = (60, 50, 55)
DISC_NEQ = (85, 32, 70)
W, H = 820, 560
PW, PH = 290, 200
X1, X2 = 170, 490
Y1, Y2 = 80, 320
R = 55


def hx(l: float, c: float, h: float) -> str:
    v = lch_hex(l, c, h)
    if v is None:
        raise ValueError(f"out of sRGB gamut: L*{l} C*{c} h{h}")
    return v


def render(lang: str) -> str:
    t = LABELS[lang]
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="14">',
         f'<rect width="{W}" height="{H}" fill="#fff"/>',
         f'<text x="{W / 2}" y="32" text-anchor="middle" font-size="17" font-weight="bold" fill="#222">{t["title"]}</text>',
         f'<text x="{X1 + PW / 2}" y="{Y1 - 12}" text-anchor="middle" fill="#222" font-weight="bold">{t["eq"]}</text>',
         f'<text x="{X2 + PW / 2}" y="{Y1 - 12}" text-anchor="middle" fill="#222" font-weight="bold">{t["neq"]}</text>',
         f'<text x="{X1 - 15}" y="{Y1 + PH / 2 + 5}" text-anchor="end" fill="#222">{t["colour"]}</text>',
         f'<text x="{X1 - 15}" y="{Y2 + PH / 2 + 5}" text-anchor="end" fill="#222">{t["grey"]}</text>']
    for x, disc in ((X1, DISC_EQ), (X2, DISC_NEQ)):
        for y, grey in ((Y1, False), (Y2, True)):
            g = hx(GROUND[0], 0, 0) if grey else hx(*GROUND)
            d = hx(disc[0], 0, 0) if grey else hx(*disc)
            s.append(f'<rect x="{x}" y="{y}" width="{PW}" height="{PH}" fill="{g}"/>')
            s.append(f'<circle cx="{x + PW / 2}" cy="{y + PH / 2}" r="{R}" fill="{d}"/>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    for lang in LABELS:
        (OUT / f"equiluminance.{lang}.svg").write_text(render(lang), encoding="utf-8")
