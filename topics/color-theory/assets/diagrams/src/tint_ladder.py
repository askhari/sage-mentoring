"""A blue pigment mixed with white, grey and black -> tint-ladder.<lang>.svg

Illustrative model, not measured paint: a synthetic phthalo-like blue reflectance
spectrum is mixed with spectrally flat white, grey and black using the
single-constant Kubelka-Munk rule (colormath.km_mix). Left: swatch ladders.
Right: path of each ladder in CIELAB lightness L* vs chroma C*ab.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from colormath import WAVELENGTHS, km_mix, reflectance_hex, reflectance_lab  # noqa: E402

OUT = Path(__file__).resolve().parent.parent
LABELS = {
    "es": {
        "title": "Un azul aclarado, agrisado y oscurecido (modelo ilustrativo)",
        "rows": ["+ blanco (tintes)", "+ gris (tonos)", "+ negro (sombras)"],
        "pure": "puro",
        "more": "más mezcla →",
        "xaxis": "croma C*ab",
        "yaxis": "claridad L*",
    },
}

BLUE = [0.03 + 0.42 * math.exp(-0.5 * ((n - 475) / 32) ** 2) for n in WAVELENGTHS]
WHITE = [0.90] * len(WAVELENGTHS)
GREY = [0.20] * len(WAVELENGTHS)
BLACK = [0.03] * len(WAVELENGTHS)
# Fraction of the added paint in each step (0 = pure blue).
STEPS = {
    0: (WHITE, [0, 0.5, 0.75, 0.88, 0.94, 0.97, 0.985]),
    1: (GREY, [0, 0.3, 0.5, 0.7, 0.85, 0.93, 0.97]),
    2: (BLACK, [0, 0.2, 0.4, 0.6, 0.75, 0.88, 0.95]),
}
ROW_COLOURS = ["#c47a00", "#666", "#222"]  # path colours in the plot
SW, GAP, X0, Y0, ROW = 50, 4, 150, 80, 92
PX, PY, PW, PH = 620, 70, 300, 300  # plot box
W, H = PX + PW + 40, PY + PH + 60


def ladders():
    out = []
    for r, (other, fracs) in STEPS.items():
        row = []
        for f in fracs:
            spec = km_mix([BLUE, other], [1 - f, f]) if f else BLUE
            row.append((reflectance_hex(spec), reflectance_lab(spec)))
        out.append(row)
    return out


def render(lang: str) -> str:
    t = LABELS[lang]
    data = ladders()
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="14">',
         f'<rect width="{W}" height="{H}" fill="#fff"/>',
         f'<text x="{W / 2}" y="30" text-anchor="middle" font-size="17" font-weight="bold" fill="#222">{t["title"]}</text>']
    for r, row in enumerate(data):
        y = Y0 + r * ROW
        s.append(f'<text x="{X0 - 12}" y="{y + SW / 2 + 5}" text-anchor="end" fill="#222">{t["rows"][r]}</text>')
        for i, (hx, _) in enumerate(row):
            s.append(f'<rect x="{X0 + i * (SW + GAP)}" y="{y}" width="{SW}" height="{SW}" fill="{hx}"/>')
        s.append(f'<circle cx="{X0 - 4}" cy="{y + SW + 10}" r="0"/>')
    s.append(f'<text x="{X0 + SW / 2}" y="{Y0 - 8}" text-anchor="middle" fill="#555" font-size="12">{t["pure"]}</text>')
    s.append(f'<text x="{X0 + 7 * (SW + GAP) - GAP}" y="{Y0 + 3 * ROW}" text-anchor="end" fill="#555" font-size="12">{t["more"]}</text>')
    # plot: x = C*ab 0..70, y = L* 0..100
    cmax = 70
    sx = lambda c: PX + c / cmax * PW
    sy = lambda l: PY + PH - l / 100 * PH
    s.append(f'<rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" fill="none" stroke="#999"/>')
    for v in range(0, 101, 20):
        s.append(f'<text x="{PX - 6}" y="{sy(v) + 4:.1f}" text-anchor="end" fill="#555" font-size="11">{v}</text>')
    for c in range(0, cmax + 1, 10):
        s.append(f'<text x="{sx(c):.1f}" y="{PY + PH + 16}" text-anchor="middle" fill="#555" font-size="11">{c}</text>')
    s.append(f'<text x="{PX + PW / 2}" y="{PY + PH + 36}" text-anchor="middle" fill="#222">{t["xaxis"]}</text>')
    s.append(f'<text x="{PX - 34}" y="{PY + PH / 2}" text-anchor="middle" fill="#222" transform="rotate(-90 {PX - 34} {PY + PH / 2})">{t["yaxis"]}</text>')
    for r, row in enumerate(data):
        pts = [(sx(math.hypot(a, b)), sy(l)) for _, (l, a, b) in row]
        s.append(f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{ROW_COLOURS[r]}" stroke-width="1.5"/>')
        for (x, y), (hx, _) in zip(pts, row):
            s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{hx}" stroke="{ROW_COLOURS[r]}" stroke-width="1.5"/>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    for row in ladders():
        print([(round(l), round(math.hypot(a, b)), round(math.degrees(math.atan2(b, a)))) for _, (l, a, b) in row])
    for lang in LABELS:
        (OUT / f"tint-ladder.{lang}.svg").write_text(render(lang), encoding="utf-8")
