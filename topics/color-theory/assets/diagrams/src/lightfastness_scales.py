"""Blue wool, Feller classes and ASTM categories on one axis -> lightfastness-scales.<lang>.svg

No colour science: a layout of three rating scales. Blue wool references 1-8
(each step drawn as one unit of the axis); Feller's classes C/B/A placed at blue
wool 3 and 6 (Feller 1994, pp. 6-7, Table 1.1); ASTM categories placed with
MacEvoy's approximate correspondence to the blue wool scale (handprint, pigmt9).
ASTM colour-difference bands from the MITRA fact sheet (pp. 1-2).
"""
from __future__ import annotations

from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent
LABELS = {
    "es": {
        "title": "Tres escalas de resistencia a la luz, alineadas de forma aproximada",
        "rows": ["lana azul", "clases de Feller", "categorías ASTM"],
        "less": "← más fugitiva",
        "more": "más permanente →",
        "feller": {"C": "C: < 20 años", "B": "B: 20–100 años", "A": "A: ≥ 100 años"},
        "de_title": "Categorías ASTM según el cambio de color medio ΔE*ab tras la exposición:",
        "de": "I < 4 · II 4–8 · III 8–16 · IV 16–24 · V > 24",
        "note": "Correspondencias aproximadas: clases según Feller (1994); ASTM–lana azul según MacEvoy (fuente C).",
    },
}

X0, U = 200, 70  # axis origin and pixels per blue-wool step
W, H = X0 + 8 * U + 40, 400
FELLER = [("C", 0, 3, "#d9d9d9"), ("B", 3, 6, "#b3b3b3"), ("A", 6, 8, "#8c8c8c")]
ASTM = [("V", 0, 2.1, "#d7301f"), ("IV", 2.1, 5.45, "#fc8d59"), ("III", 5.45, 6.05, "#fee08b"),
        ("II", 6.05, 7.05, "#91cf60"), ("I", 7.05, 8, "#1a9850")]


def render(lang: str) -> str:
    t = LABELS[lang]
    px = lambda v: X0 + v * U
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="14">',
         f'<rect width="{W}" height="{H}" fill="#fff"/>',
         f'<text x="{W / 2}" y="30" text-anchor="middle" font-size="17" font-weight="bold" fill="#222">{t["title"]}</text>',
         f'<text x="{px(0)}" y="62" fill="#555" font-size="12">{t["less"]}</text>',
         f'<text x="{px(8)}" y="62" text-anchor="end" fill="#555" font-size="12">{t["more"]}</text>']
    ys = [75, 145, 215]
    for r, y in enumerate(ys):
        s.append(f'<text x="{X0 - 12}" y="{y + 30}" text-anchor="end" fill="#222" font-weight="bold">{t["rows"][r]}</text>')
    for n in range(1, 9):
        s.append(f'<rect x="{px(n - 1) + 2}" y="{ys[0]}" width="{U - 4}" height="48" fill="#2c4f9e"/>')
        s.append(f'<text x="{px(n - 0.5)}" y="{ys[0] + 30}" text-anchor="middle" fill="#fff" font-weight="bold">{n}</text>')
    for key, a, b, c in FELLER:
        s.append(f'<rect x="{px(a) + 2}" y="{ys[1]}" width="{(b - a) * U - 4}" height="48" fill="{c}"/>')
        s.append(f'<text x="{px((a + b) / 2)}" y="{ys[1] + 29}" text-anchor="middle" fill="#111" font-size="13">{escape(t["feller"][key])}</text>')
    for key, a, b, c in ASTM:
        s.append(f'<rect x="{px(a) + 1}" y="{ys[2]}" width="{(b - a) * U - 2}" height="48" fill="{c}"/>')
        s.append(f'<text x="{px((a + b) / 2)}" y="{ys[2] + 30}" text-anchor="middle" fill="#111" font-weight="bold">{key}</text>')
    s.append(f'<text x="{X0 - 150}" y="312" fill="#222">{t["de_title"]}</text>')
    s.append(f'<text x="{X0 - 150}" y="336" fill="#222" font-weight="bold">{escape(t["de"])}</text>')
    s.append(f'<text x="{X0 - 150}" y="372" fill="#555" font-size="12">{escape(t["note"])}</text>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    for lang in LABELS:
        (OUT / f"lightfastness-scales.{lang}.svg").write_text(render(lang), encoding="utf-8")
