"""Bezold-type assimilation with thin stripes -> assimilation-stripes.<lang>.svg

The same red is crossed by thin white lines (left) and thin black lines (right).
With fine lines the red tends to look lighter among white and darker among black,
the opposite direction to simultaneous contrast. A plain swatch of the same red
sits under each panel for comparison. Colours set in CIELAB LCh (colormath.lch_hex).
The effect depends on viewing distance and line width; the diagram only sets up
the stimulus, it does not measure the effect.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from colormath import lch_hex  # noqa: E402

OUT = Path(__file__).resolve().parent.parent
LABELS = {
    "es": {
        "title": "El mismo rojo entre líneas finas blancas o negras",
        "white": "líneas blancas",
        "black": "líneas negras",
        "ref": "el mismo rojo, sin líneas",
    },
}

RED = lch_hex(48, 55, 30)
WHITE = lch_hex(97, 0, 0)
BLACK = lch_hex(8, 0, 0)
assert RED and WHITE and BLACK
W, H = 760, 470
PW, PH = 300, 260
X1, X2, Y = 60, 400, 80
PERIOD, LINE = 12, 3  # stripe period and line width (px)


def panel(x: float, line_colour: str) -> list[str]:
    s = [f'<rect x="{x}" y="{Y}" width="{PW}" height="{PH}" fill="{RED}"/>']
    yy = Y + PERIOD - LINE
    while yy + LINE <= Y + PH:
        s.append(f'<rect x="{x}" y="{yy}" width="{PW}" height="{LINE}" fill="{line_colour}"/>')
        yy += PERIOD
    s.append(f'<rect x="{x + PW / 2 - 50}" y="{Y + PH + 30}" width="100" height="50" fill="{RED}"/>')
    return s


def render(lang: str) -> str:
    t = LABELS[lang]
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="14">',
         f'<rect width="{W}" height="{H}" fill="#fff"/>',
         f'<text x="{W / 2}" y="32" text-anchor="middle" font-size="17" font-weight="bold" fill="#222">{t["title"]}</text>',
         f'<text x="{X1 + PW / 2}" y="{Y - 12}" text-anchor="middle" fill="#222" font-weight="bold">{t["white"]}</text>',
         f'<text x="{X2 + PW / 2}" y="{Y - 12}" text-anchor="middle" fill="#222" font-weight="bold">{t["black"]}</text>']
    s += panel(X1, WHITE)
    s += panel(X2, BLACK)
    s.append(f'<text x="{W / 2}" y="{Y + PH + 60}" text-anchor="middle" fill="#555" font-size="13">{t["ref"]}</text>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    for lang in LABELS:
        (OUT / f"assimilation-stripes.{lang}.svg").write_text(render(lang), encoding="utf-8")
