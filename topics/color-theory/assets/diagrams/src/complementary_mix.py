"""Mixing opposite hues towards grey -> complementary-mix-to-grey.<lang>.svg

Each row starts at a colour of L* 60, C*ab 30 and goes in straight steps through
CIELAB to the colour with the same L* and C*ab and the opposite hue angle (+180°):
the midpoint is the neutral grey. The last row uses a hue only 130° away, so the
midpoint stays a coloured grey. Starting hue angles come from
colormath.munsell_hue_angle (5R, 5Y, 5GY, 5PB) and the end names are approximate.
Schematic: real paints do not mix along straight lines in CIELAB.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from colormath import hex_rgb, lab_to_linear_srgb, lch_to_lab, munsell_hue_angle, munsell_hue_number  # noqa: E402

OUT = Path(__file__).resolve().parent.parent
LABELS = {
    "es": {
        "title": "Mezclar dos colores opuestos pasa por el gris",
        "rows": [("rojo", "azul verdoso"), ("amarillo", "morado azulado"), ("verde amarillento", "morado"),
                 ("azul morado", "amarillo anaranjado")],
        "near": ("rojo", "verde", "casi opuestos: el centro queda gris verdoso, no neutro"),
        "grey": "gris neutro",
        "steps": "proporción de la mezcla →",
    },
}
L_STAR, C_STAR, N = 60.0, 30.0, 11
STARTS = [(5, "R"), (5, "Y"), (5, "GY"), (5, "PB")]
SW, GAP, X0, Y0, ROW = 52, 4, 175, 70, 74
W, H = X0 + N * (SW + GAP) + 190, Y0 + 5 * ROW + 40


def strip(h1: float, h2_offset: float) -> list[str]:
    a1 = lch_to_lab(L_STAR, C_STAR, h1)
    a2 = lch_to_lab(L_STAR, C_STAR, h1 + h2_offset)
    cols = []
    for i in range(N):
        f = i / (N - 1)
        lab = tuple(p + (q - p) * f for p, q in zip(a1, a2))
        cols.append(hex_rgb(lab_to_linear_srgb(*lab)))
    return cols


def render(lang: str) -> str:
    t = LABELS[lang]
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="14">',
         f'<rect width="{W}" height="{H}" fill="#fff"/>',
         f'<text x="{W / 2}" y="30" text-anchor="middle" font-size="17" font-weight="bold" fill="#222">{t["title"]}</text>']
    rows = [(munsell_hue_angle(munsell_hue_number(st, fam)), 180.0, a, b) for (st, fam), (a, b) in zip(STARTS, t["rows"])]
    rows.append((munsell_hue_angle(munsell_hue_number(5, "R")), 130.0, t["near"][0], t["near"][1]))
    for r, (h, off, left, right) in enumerate(rows):
        y = Y0 + r * ROW + (16 if r == len(rows) - 1 else 0)
        for i, c in enumerate(strip(h, off)):
            x = X0 + i * (SW + GAP)
            s.append(f'<rect x="{x}" y="{y}" width="{SW}" height="{SW}" fill="{c}"/>')
        s.append(f'<text x="{X0 - 12}" y="{y + SW / 2 + 5}" text-anchor="end" fill="#222">{left}</text>')
        s.append(f'<text x="{X0 + N * (SW + GAP) + 8}" y="{y + SW / 2 + 5}" fill="#222">{right}</text>')
    mid_x = X0 + (N // 2) * (SW + GAP) + SW / 2
    last_y = Y0 + (len(rows) - 1) * ROW + 16
    s.append(f'<line x1="{X0 - 150}" y1="{last_y - 10}" x2="{W - 20}" y2="{last_y - 10}" stroke="#bbb" stroke-dasharray="4 4"/>')
    s.append(f'<text x="{mid_x}" y="{Y0 - 10}" text-anchor="middle" fill="#555" font-size="12">{t["grey"]} ↓</text>')
    s.append(f'<text x="{mid_x}" y="{last_y + SW + 20}" text-anchor="middle" fill="#555" font-size="12">{t["near"][2]}</text>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    for lang in LABELS:
        (OUT / f"complementary-mix-to-grey.{lang}.svg").write_text(render(lang), encoding="utf-8")
