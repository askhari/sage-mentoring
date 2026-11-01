"""Three thin paint layers over white paper with a black stripe -> opacity-black-stripe.<lang>.svg

Illustrative model, not measured paint: one synthetic red absorption spectrum K,
scaled with three levels of scattering S (opaque, semi-opaque, transparent). Each layer
has the same thickness; its reflectance over white and over black comes from the
two-constant Kubelka-Munk layer formula (colormath.km_layer_spectrum).
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from colormath import WAVELENGTHS, km_layer_spectrum, reflectance_hex  # noqa: E402

OUT = Path(__file__).resolve().parent.parent
LABELS = {
    "es": {
        "title": "La misma capa fina sobre blanco y sobre negro (modelo ilustrativo)",
        "paints": ["opaca", "semiopaca", "transparente"],
        "white": "papel blanco",
        "black": "banda negra",
    },
}

# Red paints: strong absorption below ~580 nm, weak above. Opaque paints scatter
# much more and are loaded more heavily, so absorption is scaled up with them:
# (absorption scale, scattering S) for opaque, semi-opaque, transparent.
K = [0.08 + 3.5 / (1 + math.exp((n - 585) / 12)) for n in WAVELENGTHS]
PAINTS = [(12.0, 12.0), (3.0, 1.5), (1.0, 0.06)]
X = 0.6  # same layer thickness for the three paints
PAPER, BLACK = 0.88, 0.04

W, H = 760, 400
BX, BW, BGAP = 190, 150, 30  # paint bands
TOP, BOT = 80, 360
STRIPE_Y, STRIPE_H = 185, 90


def render(lang: str) -> str:
    t = LABELS[lang]
    paper = reflectance_hex([PAPER] * len(WAVELENGTHS))
    black = reflectance_hex([BLACK] * len(WAVELENGTHS))
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="14">',
         f'<rect width="{W}" height="{H}" fill="#fff"/>',
         f'<text x="{W / 2}" y="30" text-anchor="middle" font-size="17" font-weight="bold" fill="#222">{t["title"]}</text>',
         f'<rect x="{BX - 30}" y="{TOP}" width="{3 * BW + 2 * BGAP + 60}" height="{BOT - TOP}" fill="{paper}" stroke="#bbb"/>',
         f'<rect x="{BX - 30}" y="{STRIPE_Y}" width="{3 * BW + 2 * BGAP + 60}" height="{STRIPE_H}" fill="{black}"/>',
         f'<text x="{BX - 40}" y="{(TOP + STRIPE_Y) / 2 + 5}" text-anchor="end" fill="#222">{t["white"]}</text>',
         f'<text x="{BX - 40}" y="{STRIPE_Y + STRIPE_H / 2 + 5}" text-anchor="end" fill="#222">{t["black"]}</text>']
    for i, (ks, sv) in enumerate(PAINTS):
        kp = [ks * k for k in K]
        sp = [sv] * len(WAVELENGTHS)
        on_white = reflectance_hex(km_layer_spectrum(kp, sp, X, PAPER))
        on_black = reflectance_hex(km_layer_spectrum(kp, sp, X, BLACK))
        x = BX + i * (BW + BGAP)
        s.append(f'<rect x="{x}" y="{TOP + 15}" width="{BW}" height="{STRIPE_Y - TOP - 15}" fill="{on_white}"/>')
        s.append(f'<rect x="{x}" y="{STRIPE_Y}" width="{BW}" height="{STRIPE_H}" fill="{on_black}"/>')
        s.append(f'<rect x="{x}" y="{STRIPE_Y + STRIPE_H}" width="{BW}" height="{BOT - 15 - STRIPE_Y - STRIPE_H}" fill="{on_white}"/>')
        s.append(f'<text x="{x + BW / 2}" y="{TOP - 10}" text-anchor="middle" fill="#222" font-weight="bold">{t["paints"][i]}</text>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    for lang in LABELS:
        (OUT / f"opacity-black-stripe.{lang}.svg").write_text(render(lang), encoding="utf-8")
