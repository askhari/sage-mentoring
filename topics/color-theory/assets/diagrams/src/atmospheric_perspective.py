"""Atmospheric perspective as attenuation + airlight -> atmospheric-perspective.<lang>.svg

The colour reaching the eye from an object at distance d is
    L(d) = L0 * exp(-beta * d) + L_inf * (1 - exp(-beta * d))
(attenuation of the object's light plus airlight; Koschmieder's model as presented by
Narasimhan & Nayar 2002). It is computed per sRGB channel in linear light, with the
scattering coefficient depending on wavelength as beta ~ lambda^-gamma: gamma = 0 for
fog and dense haze (all wavelengths alike, grey-white airlight) and gamma > 0 for
light haze (blue scattered more, bluish airlight). The channel wavelengths, gamma and
horizon colours are illustrative choices, not measurements.

Two rows per panel: a dark object (tree) and a light object (sunlit wall), at optical
distances beta*d = 0 ... 3, then the horizon colour (d = infinity).
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from colormath import decode_srgb, encode_srgb, hex_lab  # noqa: E402

LABELS = {
    "es": {
        "panels": ["Bruma ligera: el aire dispersa más el azul", "Niebla: el aire dispersa todos los colores por igual"],
        "rows": ["objeto oscuro", "objeto claro"],
        "dist": ["cerca", "", "", "", "lejos", "horizonte"],
        "axis": "distancia →",
        "lstar": "L*",
    },
}

DARK, LIGHT = "#2f4a26", "#f7ecd6"           # dark green tree, sunlit white wall
OPTICAL = [0.0, 0.25, 0.6, 1.2, 2.5]            # beta*d for the reference (green) channel
LAMBDA = (610.0, 550.0, 465.0)                 # nominal wavelengths of the R, G, B channels
CASES = [  # (gamma, horizon colour)
    (1.3, "#c9d6e6"),
    (0.0, "#d9d9d6"),
]
OUT = Path(__file__).resolve().parent.parent
SW, SH, GAP = 92, 70, 10
X0, W = 150, 150 + 6 * (SW + GAP) + 30


def _lin(hexcol: str) -> list[float]:
    return [decode_srgb(int(hexcol[i:i + 2], 16) / 255) for i in (1, 3, 5)]


def _hex(lin: list[float]) -> str:
    return "#" + "".join(f"{round(255 * encode_srgb(min(1.0, max(0.0, c)))):02x}" for c in lin)


def seen(obj: str, horizon: str, tau: float, gamma: float) -> str:
    """Colour of `obj` seen through optical depth `tau` (green channel) of air."""
    o, h = _lin(obj), _lin(horizon)
    out = []
    for c in range(3):
        t = math.exp(-tau * (LAMBDA[c] / 550.0) ** -gamma)
        out.append(o[c] * t + h[c] * (1 - t))
    return _hex(out)


def render(lang: str) -> str:
    t = LABELS[lang]
    ph = 2 * (SH + 26) + 56
    H = len(CASES) * ph + 50
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="14">',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
    for p, (gamma, horizon) in enumerate(CASES):
        y0 = 20 + p * ph
        s.append(f'<text x="20" y="{y0 + 16}" font-weight="bold" font-size="16" fill="#222">{t["panels"][p]}</text>')
        for r, obj in enumerate([DARK, LIGHT]):
            y = y0 + 32 + r * (SH + 26)
            s.append(f'<text x="20" y="{y + SH / 2 + 5}" fill="#333">{t["rows"][r]}</text>')
            cols = [seen(obj, horizon, tau, gamma) for tau in OPTICAL] + [horizon]
            for i, col in enumerate(cols):
                x = X0 + i * (SW + GAP) + (14 if i == len(cols) - 1 else 0)
                s.append(f'<rect x="{x}" y="{y}" width="{SW}" height="{SH}" fill="{col}" stroke="#999" stroke-width="0.6"/>')
                l = hex_lab(col)[0]
                s.append(f'<text x="{x + SW / 2}" y="{y + SH + 16}" text-anchor="middle" font-size="12" fill="#555">'
                         f'{t["lstar"]} {l:.0f}</text>')
        ya = y0 + 32 + 2 * (SH + 26) + 4
        for i, lab in enumerate(t["dist"]):
            if lab:
                x = X0 + i * (SW + GAP) + SW / 2 + (14 if i == 5 else 0)
                s.append(f'<text x="{x}" y="{ya + 8}" text-anchor="middle" font-size="12" fill="#333" font-style="italic">{lab}</text>')
    s.append(f'<text x="{X0 + 2.5 * (SW + GAP)}" y="{H - 12}" text-anchor="middle" fill="#333">{t["axis"]}</text>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    for lang in LABELS:
        (OUT / f"atmospheric-perspective.{lang}.svg").write_text(render(lang), encoding="utf-8")
        print(f"wrote atmospheric-perspective.{lang}.svg")
