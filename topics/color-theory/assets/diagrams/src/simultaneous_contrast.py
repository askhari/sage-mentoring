"""Same patch on two grounds -> simultaneous-contrast.<lang>.svg

Top row: one mid grey on a dark and on a light ground (lightness contrast).
Bottom row: one muted colour on a blue and on an orange ground (hue contrast).
A thin bridge of the patch colour joins each pair, to show the two patches are
the same paint. Colours are set in CIELAB LCh (colormath.lch_hex), so the
lightness and chroma of each ground are explicit.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from colormath import lch_hex  # noqa: E402

OUT = Path(__file__).resolve().parent.parent
LABELS = {
    "es": {
        "title": "El mismo color sobre dos fondos distintos",
        "row1": "mismo gris (L* 55)",
        "row2": "mismo color apagado",
        "bridge": "la franja que une los dos cuadrados es del mismo color",
    },
}


def lch(l: float, c: float, h: float) -> str:
    hx = lch_hex(l, c, h)
    if hx is None:
        raise ValueError(f"out of sRGB gamut: L*{l} C*{c} h{h}")
    return hx


GREY = lch(55, 0, 0)
MUTED = lch(62, 14, 75)  # greyish yellow-orange
ROWS = [
    ("row1", GREY, lch(18, 0, 0), lch(92, 0, 0)),
    ("row2", MUTED, lch(45, 45, 285), lch(68, 60, 60)),
]
W, H = 760, 590
GW, GH = 300, 200  # ground size
PS = 90  # patch size
X1, X2 = 70, 390
Y0 = 70


def render(lang: str) -> str:
    t = LABELS[lang]
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="14">',
         f'<rect width="{W}" height="{H}" fill="#fff"/>',
         f'<text x="{W / 2}" y="32" text-anchor="middle" font-size="17" font-weight="bold" fill="#222">{t["title"]}</text>']
    for i, (key, patch, g1, g2) in enumerate(ROWS):
        y = Y0 + i * (GH + 50)
        s.append(f'<rect x="{X1}" y="{y}" width="{GW}" height="{GH}" fill="{g1}"/>')
        s.append(f'<rect x="{X2}" y="{y}" width="{GW}" height="{GH}" fill="{g2}"/>')
        py = y + (GH - PS) / 2
        p1x, p2x = X1 + (GW - PS) / 2, X2 + (GW - PS) / 2
        s.append(f'<rect x="{p1x}" y="{py}" width="{PS}" height="{PS}" fill="{patch}"/>')
        s.append(f'<rect x="{p2x}" y="{py}" width="{PS}" height="{PS}" fill="{patch}"/>')
        # bridge below the grounds, joining the two patches
        by = y + GH + 8
        s.append(f'<rect x="{p1x + PS / 2 - 4}" y="{py + PS}" width="8" height="{by - py - PS + 8}" fill="{patch}"/>')
        s.append(f'<rect x="{p2x + PS / 2 - 4}" y="{py + PS}" width="8" height="{by - py - PS + 8}" fill="{patch}"/>')
        s.append(f'<rect x="{p1x + PS / 2 - 4}" y="{by}" width="{p2x - p1x + 8}" height="8" fill="{patch}"/>')
        s.append(f'<text x="{W / 2}" y="{y - 8}" text-anchor="middle" fill="#222" font-weight="bold">{t[key]}</text>')
    s.append(f'<text x="{W / 2}" y="{H - 18}" text-anchor="middle" fill="#555" font-size="13">{t["bridge"]}</text>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    for lang in LABELS:
        (OUT / f"simultaneous-contrast.{lang}.svg").write_text(render(lang), encoding="utf-8")
