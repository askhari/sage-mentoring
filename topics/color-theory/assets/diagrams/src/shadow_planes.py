"""Colour of shadow planes outdoors -> shadow-planes.<lang>.svg

A white wall with a projecting slab, seen from below eye level, with the sun behind
it, on sandy ground. Every plane in shadow gets only indirect light, and its colour
depends on which light sources it faces:
  * cast shadow on the ground (faces up): blue skylight only;
  * wall face (vertical): half sky, half sunlit ground;
  * slab underside (faces down): light bounced from the sunlit ground.
Colours are computed in linear RGB as albedo x irradiance, with illustrative values
for sunlight (slightly warm), skylight (blue) and sand. A simple model in the spirit
of the up-facing-cool / down-facing-warm rule painters use; not a radiometric render.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from colormath import encode_srgb  # noqa: E402

LABELS = {
    "es": {
        "sun": "sol detrás del muro",
        "lit": "suelo al sol: sol + cielo",
        "cast": "sombra en el suelo (mira arriba): solo cielo → azulada",
        "wall": "muro en sombra (vertical): cielo + suelo",
        "under": "parte inferior del voladizo (mira abajo): rebote del suelo → cálida",
    },
}

SUN = (1.00, 0.90, 0.76)       # direct sunlight on a horizontal plane
SKY = (0.22, 0.33, 0.62)       # whole-sky irradiance on a horizontal plane
SAND = (0.56, 0.47, 0.35)      # ground albedo (linear)
WHITE = (0.80, 0.80, 0.80)     # wall albedo (linear)
EXPOSURE = 1.15
OUT = Path(__file__).resolve().parent.parent
W, H = 960, 560


def mul(a, b):
    return tuple(x * y for x, y in zip(a, b))


def add(*vs):
    return tuple(sum(c) for c in zip(*vs))


def scale(a, k):
    return tuple(x * k for x in a)


def hexc(lin) -> str:
    return "#" + "".join(f"{round(255 * encode_srgb(min(1.0, max(0.0, EXPOSURE * c)))):02x}" for c in lin)


def colours() -> dict[str, str]:
    ground_lit = mul(SAND, add(SUN, SKY))
    cast = mul(SAND, scale(SKY, 0.75))                              # wall hides part of the sky
    wall = mul(WHITE, add(scale(SKY, 0.5), scale(ground_lit, 0.5)))
    under = mul(WHITE, scale(ground_lit, 0.85))                     # most of the ground it sees is sunlit
    return {"lit": hexc(ground_lit), "cast": hexc(cast), "wall": hexc(wall), "under": hexc(under),
            "sky_top": hexc(scale((0.25, 0.42, 0.85), 0.75)), "sky_hor": hexc((0.62, 0.70, 0.82))}


def poly(pts, fill) -> str:
    return '<path d="M' + " L".join(f"{x},{y}" for x, y in pts) + f' Z" fill="{fill}"/>'


def label(x, y, tx, ty, text, anchor="start") -> str:
    return (f'<line x1="{x}" y1="{y}" x2="{tx}" y2="{ty - 4}" stroke="#222" stroke-width="1"/>'
            f'<circle cx="{x}" cy="{y}" r="3" fill="#222"/>'
            f'<text x="{tx}" y="{ty}" text-anchor="{anchor}" fill="#111" font-size="14" stroke="#fff" '
            f'stroke-width="4" stroke-opacity="0.85" paint-order="stroke">{text}</text>')


def render(lang: str) -> str:
    t, c = LABELS[lang], colours()
    horizon = 300
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="14">',
         '<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
         f'<stop offset="0" stop-color="{c["sky_top"]}"/><stop offset="1" stop-color="{c["sky_hor"]}"/></linearGradient></defs>',
         f'<rect width="{W}" height="{horizon}" fill="url(#sky)"/>',
         f'<rect y="{horizon}" width="{W}" height="{H - horizon}" fill="{c["lit"]}"/>',
         poly([(300, 380), (660, 380), (760, 470), (220, 470)], c["cast"]),     # cast shadow on the ground
         poly([(300, 150), (660, 150), (660, 380), (300, 380)], c["wall"]),     # wall face
         poly([(300, 150), (660, 150), (720, 110), (240, 110)], c["under"]),    # slab underside
         poly([(240, 92), (720, 92), (720, 110), (240, 110)], c["wall"]),       # slab front edge
         ]
    s.append(f'<text x="480" y="80" text-anchor="middle" fill="#7a5a00" font-size="13" font-style="italic">☀ {t["sun"]}</text>')
    s.append(label(560, 130, 590, 40, t["under"], "middle"))
    s.append(label(480, 260, 700, 250, t["wall"]))
    s.append(label(560, 430, 600, 512, t["cast"], "middle"))
    s.append(label(850, 420, 940, 520, t["lit"], "end"))
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    for lang in LABELS:
        (OUT / f"shadow-planes.{lang}.svg").write_text(render(lang), encoding="utf-8")
        print(f"wrote shadow-planes.{lang}.svg", colours())
