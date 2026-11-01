"""One transparent blue as masstone, thin film and tint -> masstone-tint-thin-film.<lang>.svg

Illustrative model, not measured paint: a synthetic phthalo-like blue (strong
absorption outside ~440-500 nm, little scattering) and a white paint (little
absorption, strong scattering). Thickness ladder over white paper from the
two-constant Kubelka-Munk layer formula; tints from concentration-weighted K and S
(colormath.km_layer_spectrum, km_mix_ks).
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from colormath import WAVELENGTHS, km_layer_spectrum, km_mix_ks, reflectance_hex  # noqa: E402

OUT = Path(__file__).resolve().parent.parent
LABELS = {
    "es": {
        "title": "Un mismo azul transparente visto de tres maneras (modelo ilustrativo)",
        "big": [("tono de masa", "capa gruesa"), ("película fina sobre blanco", "subtono, sentido Golden"),
                ("mezcla con blanco", "tinte; subtono, sentido MacEvoy")],
        "row1": "capa cada vez más gruesa sobre papel blanco →",
        "row2": "cada vez más blanco en la mezcla →",
    },
}

N = len(WAVELENGTHS)
BLUE_K = [0.15 + 9.0 * (1 - math.exp(-0.5 * ((n - 470) / 28) ** 2)) for n in WAVELENGTHS]
BLUE_S = [0.25] * N
WHITE_K = [0.02] * N
WHITE_S = [6.0] * N
PAPER = 0.88
THIN, THICK = 0.04, 20.0
TINT_PARTS = 10  # 1 part blue : 10 parts white (by weight of K, S)
LADDER_X = [0.01, 0.03, 0.06, 0.12, 0.25, 0.5, 1.0, 20.0]
LADDER_WHITE = [0.0, 0.5, 0.75, 0.9, 0.95, 0.98, 0.99]

W, H = 820, 470
SW = 200


def film(x: float) -> str:
    return reflectance_hex(km_layer_spectrum(BLUE_K, BLUE_S, x, PAPER))


def tint(fw: float) -> str:
    k, s = km_mix_ks([(BLUE_K, BLUE_S), (WHITE_K, WHITE_S)], [1 - fw, fw])
    return reflectance_hex(km_layer_spectrum(k, s, 50.0, PAPER))


def render(lang: str) -> str:
    t = LABELS[lang]
    big = [film(THICK), film(THIN), tint(TINT_PARTS / (TINT_PARTS + 1))]
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="14">',
         f'<rect width="{W}" height="{H}" fill="#fff"/>',
         f'<text x="{W / 2}" y="30" text-anchor="middle" font-size="17" font-weight="bold" fill="#222">{t["title"]}</text>']
    x0 = (W - 3 * SW - 2 * 40) / 2
    for i, hx in enumerate(big):
        x = x0 + i * (SW + 40)
        s.append(f'<rect x="{x}" y="55" width="{SW}" height="130" fill="{hx}" stroke="#ccc"/>')
        a, b = t["big"][i]
        s.append(f'<text x="{x + SW / 2}" y="207" text-anchor="middle" fill="#222" font-weight="bold">{a}</text>')
        s.append(f'<text x="{x + SW / 2}" y="226" text-anchor="middle" fill="#555" font-size="12">{b}</text>')
    for r, (label, cols) in enumerate([(t["row1"], [film(x) for x in LADDER_X]), (t["row2"], [tint(f) for f in LADDER_WHITE])]):
        y = 275 + r * 95
        s.append(f'<text x="{x0}" y="{y - 8}" fill="#222">{label}</text>')
        sw = (3 * SW + 80 - (len(cols) - 1) * 6) / len(cols)
        for j, hx in enumerate(cols):
            s.append(f'<rect x="{x0 + j * (sw + 6):.1f}" y="{y}" width="{sw:.1f}" height="55" fill="{hx}" stroke="#ccc"/>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    for lang in LABELS:
        (OUT / f"masstone-tint-thin-film.{lang}.svg").write_text(render(lang), encoding="utf-8")
