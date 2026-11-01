"""Blue + yellow: paint mixture vs optical mixture -> blue-yellow-mixing.<lang>.svg

Illustrative model, not measured paint. Synthetic reflectance spectra of a blue and
a yellow are mixed in steps two ways:
- paint (pigments in one film): single-constant Kubelka-Munk (colormath.km_mix);
- optical (small dots seen from afar): area-weighted average of reflected light
  (colormath.optical_mix).
Top: the two swatch strips. Bottom left: dots of the two colours at decreasing
size. Bottom right: both paths in the CIELAB a*b* plane.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from colormath import WAVELENGTHS, km_mix, optical_mix, reflectance_hex, reflectance_lab  # noqa: E402

OUT = Path(__file__).resolve().parent.parent
LABELS = {
    "es": {
        "title": "Azul + amarillo: mezcla en la paleta frente a mezcla óptica (modelo ilustrativo)",
        "paint": "pintura mezclada",
        "optical": "mezcla óptica",
        "dots": "puntos de azul y amarillo vistos cada vez desde más lejos",
        "plane": "trayectorias en el plano a*b*",
        "a": "a* (verde ← → rojo)",
        "b": "b* (azul ↓ ↑ amarillo)",
    },
}
BLUE = [0.03 + 0.45 * math.exp(-0.5 * ((n - 470) / 35) ** 2) for n in WAVELENGTHS]
YELLOW = [0.05 + 0.80 / (1 + math.exp(-(n - 505) / 12)) for n in WAVELENGTHS]
N = 11
SW, GAP, X0 = 54, 4, 190
W, H = X0 + N * (SW + GAP) + 30, 560


def strips():
    paint, optical = [], []
    for i in range(N):
        f = i / (N - 1)
        w = [1 - f, f]
        ps = km_mix([BLUE, YELLOW], w) if 0 < f < 1 else (BLUE if f == 0 else YELLOW)
        os_ = optical_mix([BLUE, YELLOW], w)
        paint.append((reflectance_hex(ps), reflectance_lab(ps)))
        optical.append((reflectance_hex(os_), reflectance_lab(os_)))
    return paint, optical


def render(lang: str) -> str:
    t = LABELS[lang]
    paint, optical = strips()
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="14">',
         f'<rect width="{W}" height="{H}" fill="#fff"/>',
         f'<text x="{W / 2}" y="30" text-anchor="middle" font-size="17" font-weight="bold" fill="#222">{t["title"]}</text>']
    for r, (name, row) in enumerate([(t["paint"], paint), (t["optical"], optical)]):
        y = 56 + r * (SW + 18)
        s.append(f'<text x="{X0 - 12}" y="{y + SW / 2 + 5}" text-anchor="end" fill="#222" font-weight="bold">{name}</text>')
        for i, (hx, _) in enumerate(row):
            s.append(f'<rect x="{X0 + i * (SW + GAP)}" y="{y}" width="{SW}" height="{SW}" fill="{hx}"/>')
    # dots panel: checkerboards of shrinking cells
    bh, bw = paint[0][0], paint[-1][0]
    dy = 230
    s.append(f'<text x="30" y="{dy - 12}" fill="#222">{t["dots"]}</text>')
    # Cells stay >= 4 px: finer patterns get averaged by the renderer in gamma-encoded
    # sRGB, which shows a false green instead of the true optical average.
    for k, cell in enumerate([24, 10, 4]):
        x0 = 30 + k * 115
        pid = f"chk{k}"
        s.append(f'<defs><pattern id="{pid}" width="{2 * cell}" height="{2 * cell}" patternUnits="userSpaceOnUse">'
                 f'<rect width="{2 * cell}" height="{2 * cell}" fill="{bw}"/>'
                 f'<rect width="{cell}" height="{cell}" fill="{bh}"/><rect x="{cell}" y="{cell}" width="{cell}" height="{cell}" fill="{bh}"/>'
                 f'</pattern></defs>')
        s.append(f'<rect x="{x0}" y="{dy}" width="96" height="96" fill="url(#{pid})" stroke="#999"/>')
    s.append(f'<text x="{30 + 3 * 115 + 6}" y="{dy + 54}" fill="#555" font-size="20">→</text>')
    s.append(f'<rect x="{30 + 3 * 115 + 34}" y="{dy}" width="96" height="96" fill="{optical[N // 2][0]}" stroke="#999"/>')
    s.append(f'<text x="{30 + 3 * 115 + 82}" y="{dy + 114}" text-anchor="middle" fill="#555" font-size="12">media al 50 %</text>')
    # a*b* plane
    cx, cy, sc = W - 170, 400, 1.35
    s.append(f'<text x="{cx}" y="{cy - 140}" text-anchor="middle" fill="#222">{t["plane"]}</text>')
    s.append(f'<line x1="{cx - 120}" y1="{cy}" x2="{cx + 120}" y2="{cy}" stroke="#bbb"/>')
    s.append(f'<line x1="{cx}" y1="{cy - 125}" x2="{cx}" y2="{cy + 125}" stroke="#bbb"/>')
    s.append(f'<text x="{cx}" y="{cy + 145}" text-anchor="middle" fill="#555" font-size="11">{t["a"]}</text>')
    s.append(f'<text x="{cx + 124}" y="{cy - 110}" text-anchor="end" fill="#555" font-size="11">{t["b"]}</text>')
    for row, dash in [(paint, ""), (optical, ' stroke-dasharray="5 4"')]:
        pts = [(cx + a * sc, cy - b * sc) for _, (l, a, b) in row]
        s.append(f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="#444" stroke-width="1.5"{dash}/>')
        for (x, y), (hx, _) in zip(pts, row):
            s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{hx}" stroke="#444"/>')
    lx = 30
    s.append(f'<line x1="{lx}" y1="{H - 170}" x2="{lx + 40}" y2="{H - 170}" stroke="#444" stroke-width="1.5"/>'
             f'<text x="{lx + 48}" y="{H - 165}" fill="#222" font-size="12">{t["paint"]}</text>')
    s.append(f'<line x1="{lx}" y1="{H - 146}" x2="{lx + 40}" y2="{H - 146}" stroke="#444" stroke-width="1.5" stroke-dasharray="5 4"/>'
             f'<text x="{lx + 48}" y="{H - 141}" fill="#222" font-size="12">{t["optical"]}</text>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    p, o = strips()
    print("paint mid", [round(v) for v in p[N // 2][1]], "optical mid", [round(v) for v in o[N // 2][1]])
    for lang in LABELS:
        (OUT / f"blue-yellow-mixing.{lang}.svg").write_text(render(lang), encoding="utf-8")
