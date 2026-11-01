"""Two constant-hue pages (≈5Y and ≈5PB) -> munsell-hue-page.<lang>.svg

Approximation of Munsell hue pages built in CIELAB: lightness L* on the vertical
axis (Munsell value ≈ L*/10 in the paint data of justpaint-munsell-cielab) and
chroma C*ab on the horizontal axis. Cells are drawn only where the colour fits in
the sRGB gamut, so the right-hand edge shows how far a screen can go at each
lightness. Dots are oil paints of that hue family measured by Golden Artist Colors
(Williamsburg table, 6 mil films), placed by their own L* and C*ab = sqrt(a*^2 + b*^2),
and labelled with their Munsell notation H V/C from the same table.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from colormath import max_srgb_chroma, lch_hex, munsell_hue_angle, munsell_hue_number  # noqa: E402

LABELS = {
    "es": {
        "pages": ["Página de matiz ≈ 5Y (amarillo)", "Página de matiz ≈ 5PB (morado-azul)"],
        "x": "croma C*ab (CIELAB)",
        "y": "claridad L*  (valor Munsell ≈ L*/10)",
        "legend_cells": "colores que caben en una pantalla sRGB",
        "legend_dots": "pinturas al óleo medidas (notación Munsell H V/C)",
        "paints": {
            "Cadmium Lemon": "Amarillo limón de cadmio",
            "Cadmium Yellow Medium": "Amarillo de cadmio medio",
            "Yellow Ochre": "Ocre amarillo",
            "Raw Umber": "Sombra natural",
            "Ultramarine Blue": "Azul ultramar",
            "Cobalt Blue": "Azul cobalto",
            "Cerulean Blue French": "Azul cerúleo",
            "Cobalt Blue Deep": "Azul cobalto oscuro",
        },
    },
}

# (paint, Munsell notation, L*, a*, b*, label dx, label dy) — Golden Artist Colors,
# "Munsell and Lab Readings for Williamsburg Handmade Oil Colors" (justpaint-munsell-cielab).
PAINTS = [
    [("Cadmium Lemon", "9.06Y 9.05/12.69", 89.99, -8.36, 94.94, -10, -12),
     ("Cadmium Yellow Medium", "2.73Y 8.45/16.78", 83.08, 16.80, 111.85, -10, 22),
     ("Yellow Ochre", "9.62YR 5.55/8.69", 55.50, 18.84, 52.68, 10, 4),
     ("Raw Umber", "6.41Y 1.83/1.18", 18.68, 0.42, 7.03, 10, 4)],
    [("Cobalt Blue Deep", "6.82PB 2.20/15.36", 26.17, 17.72, -55.12, 10, -10),
     ("Cobalt Blue", "6.42PB 2.25/13.27", 26.58, 8.91, -49.14, 10, 14),
     ("Cerulean Blue French", "1.61PB 2.61/8.65", 29.58, -15.71, -32.11, 0, -14),
     ("Ultramarine Blue", "9.01PB 0.32/18.16", 4.78, 24.88, -37.90, 10, 4)],
]
HUES = [munsell_hue_angle(munsell_hue_number(5, "Y")), munsell_hue_angle(munsell_hue_number(5, "PB"))]

W, H = 1000, 560
PW, PH = 380, 380          # plot size
C_MAX = 120
OUT = Path(__file__).resolve().parent.parent


def render(lang: str) -> str:
    t = LABELS[lang]
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="13">',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
    for k, h in enumerate(HUES):
        x0, y0 = 90 + k * 480, 60
        sx, sy = PW / C_MAX, PH / 100

        def X(c):
            return x0 + c * sx

        def Y(l):
            return y0 + (100 - l) * sy

        s.append(f'<text x="{x0 + PW / 2}" y="{y0 - 22}" text-anchor="middle" font-weight="bold" font-size="15" fill="#222">{t["pages"][k]}</text>')
        # Cells: L* 5..95 in steps of 10 (centres 10..90), C*ab in steps of 10.
        for l in range(10, 100, 10):
            cmax = max_srgb_chroma(l, h)
            c = 5
            while c <= cmax and c < C_MAX:
                col = lch_hex(l, c, h)
                s.append(f'<rect x="{X(c - 5) + 0.5:.1f}" y="{Y(l + 5) + 0.5:.1f}" width="{10 * sx - 1:.1f}" height="{10 * sy - 1:.1f}" fill="{col}"/>')
                c += 10
        # Axes and ticks.
        s.append(f'<line x1="{x0}" y1="{Y(0)}" x2="{X(C_MAX)}" y2="{Y(0)}" stroke="#333"/>')
        s.append(f'<line x1="{x0}" y1="{Y(0)}" x2="{x0}" y2="{Y(100)}" stroke="#333"/>')
        for l in range(0, 101, 20):
            s.append(f'<text x="{x0 - 8}" y="{Y(l) + 4:.1f}" text-anchor="end" fill="#444" font-size="12">{l}</text>')
        for c in range(0, C_MAX + 1, 20):
            s.append(f'<text x="{X(c):.1f}" y="{Y(0) + 18:.1f}" text-anchor="middle" fill="#444" font-size="12">{c}</text>')
        s.append(f'<text x="{x0 + PW / 2}" y="{Y(0) + 40:.1f}" text-anchor="middle" fill="#222">{t["x"]}</text>')
        s.append(f'<text transform="translate({x0 - 44},{y0 + PH / 2}) rotate(-90)" text-anchor="middle" fill="#222">{t["y"]}</text>')
        # Paint dots.
        for name, notation, l, a, b, dx, dy in PAINTS[k]:
            c = math.hypot(a, b)
            px, py = X(c), Y(l)
            s.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="5.5" fill="#fff" stroke="#111" stroke-width="2"/>')
            anchor = "start" if dx > 0 else ("end" if dx < 0 else "middle")
            s.append(f'<text x="{px + dx:.1f}" y="{py + dy:.1f}" text-anchor="{anchor}" fill="#111" font-size="12" paint-order="stroke" stroke="#fff" stroke-width="3.5" stroke-linejoin="round">'
                     f'{t["paints"][name]} <tspan font-weight="bold">{notation}</tspan></text>')
    # Legend.
    ly = H - 34
    s.append(f'<rect x="90" y="{ly - 11}" width="14" height="14" fill="{lch_hex(70, 30, HUES[0])}"/>')
    s.append(f'<text x="112" y="{ly}" fill="#333">{t["legend_cells"]}</text>')
    s.append(f'<circle cx="527" cy="{ly - 4}" r="5.5" fill="#fff" stroke="#111" stroke-width="2"/>')
    s.append(f'<text x="540" y="{ly}" fill="#333">{t["legend_dots"]}</text>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    for lang in LABELS:
        (OUT / f"munsell-hue-page.{lang}.svg").write_text(render(lang), encoding="utf-8")
        print(f"wrote munsell-hue-page.{lang}.svg")
