"""Gamut mask on a hue-chroma disc -> gamut-mask.<lang>.svg

Left: a disc of hues (angle, Munsell-type spacing as in hue_circle.py) and chroma
(radius, C*ab 0 at the centre to 40 at the rim) at constant L* 60. A triangle (the
mask) selects the colours of one painting; outside it the disc is veiled. The three
corners are the "subjective primaries" of the mask (Gurney's gamut-masking method).
Right: the colour strings premixed from the mask: each corner towards the centre
grey, and corner to corner along the edges. Strings are straight lines in CIELAB,
an idealisation: real paint mixtures follow curved paths (Kubelka-Munk), so some
colours inside the mask may not be reachable from three corner paints.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from colormath import lch_hex, lch_to_lab, max_srgb_chroma, munsell_hue_angle  # noqa: E402

LABELS = {
    "es": {
        "left": "Máscara sobre el círculo de matices",
        "right": "Cadenas de color premezcladas",
        "corners": ["A", "B", "C"],
        "strings": ["A → gris", "B → gris", "C → gris", "A → B", "B → C", "C → A"],
        "centre": "gris",
        "note": "Mezclas en línea recta (idealizadas); la pintura real se desvía.",
    },
}

L_STAR, C_MAX = 60.0, 40.0
# Mask corners as (Munsell hue number, C*ab): a yellow-red, a blue-green and a muted purple.
CORNERS = [(15.0, 36.0), (55.0, 26.0), (85.0, 14.0)]
R = 170
CX, CY = 220, 250
W, H = 940, 520
OUT = Path(__file__).resolve().parent.parent


def pos(n: float, c: float) -> tuple[float, float]:
    a = math.radians(-90 + (n - 5) * 3.6)
    r = R * c / C_MAX
    return CX + r * math.cos(a), CY + r * math.sin(a)


def lab_hex(lab) -> str:
    l, a, b = lab
    c, h = math.hypot(a, b), math.degrees(math.atan2(b, a)) % 360
    return lch_hex(l, c, h) or "#808080"


def render(lang: str) -> str:
    t = LABELS[lang]
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="14">',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
         f'<text x="{CX}" y="40" text-anchor="middle" font-weight="bold" font-size="16" fill="#222">{t["left"]}</text>']
    tri = [pos(n, c) for n, c in CORNERS]
    rings, sectors = 16, 90
    cells = []
    for i in range(rings):
        c0, c1 = C_MAX * i / rings, C_MAX * (i + 1) / rings
        for j in range(sectors):
            n0, n1 = 100 * j / sectors, 100 * (j + 1) / sectors
            nm, cm = (n0 + n1) / 2, (c0 + c1) / 2
            h = munsell_hue_angle(nm)
            col = lch_hex(L_STAR, min(cm, max_srgb_chroma(L_STAR, h)), h)
            pts = [pos(n0, c0), pos(n1 + 0.3, c0), pos(n1 + 0.3, c1 + 0.1), pos(n0, c1 + 0.1)]
            d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z"
            cells.append(f'<path d="{d}" fill="{col}" stroke="{col}" stroke-width="0.5"/>')
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in tri) + " Z"
    s.append(f'<defs><clipPath id="mask"><path d="{d}"/></clipPath></defs>')
    s.append('<g opacity="0.35">' + "".join(cells) + '</g>')
    s.append('<g clip-path="url(#mask)">' + "".join(cells) + '</g>')
    s.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="#bbb" stroke-width="1"/>')
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in tri) + " Z"
    s.append(f'<path d="{d}" fill="none" stroke="#222" stroke-width="2.2"/>')
    for (x, y), lab in zip(tri, t["corners"]):
        dx, dy = x - CX, y - CY
        k = 22 / max(1.0, math.hypot(dx, dy))
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="#222"/>')
        s.append(f'<text x="{x + dx * k:.1f}" y="{y + dy * k + 5:.1f}" text-anchor="middle" font-weight="bold" fill="#222">{lab}</text>')
    s.append(f'<circle cx="{CX}" cy="{CY}" r="3" fill="#555"/>')
    s.append(f'<text x="{CX + 8}" y="{CY + 16}" font-size="12" fill="#444">{t["centre"]}</text>')

    # Colour strings, straight lines in CIELAB.
    labs = [lch_to_lab(L_STAR, c, munsell_hue_angle(n)) for n, c in CORNERS]
    grey = (L_STAR, 0.0, 0.0)
    pairs = [(labs[0], grey), (labs[1], grey), (labs[2], grey),
             (labs[0], labs[1]), (labs[1], labs[2]), (labs[2], labs[0])]
    x0, sw, sh, steps = 540, 50, 42, 7
    s.append(f'<text x="{x0 + steps * sw / 2}" y="40" text-anchor="middle" font-weight="bold" font-size="16" fill="#222">{t["right"]}</text>')
    for k, (a, b) in enumerate(pairs):
        y = 70 + k * (sh + 24) + (14 if k >= 3 else 0)
        s.append(f'<text x="{x0 - 12}" y="{y + sh / 2 + 5}" text-anchor="end" fill="#333">{t["strings"][k]}</text>')
        for i in range(steps):
            u = i / (steps - 1)
            col = lab_hex(tuple(a[m] + (b[m] - a[m]) * u for m in range(3)))
            s.append(f'<rect x="{x0 + i * sw}" y="{y}" width="{sw}" height="{sh}" fill="{col}" stroke="#fff" stroke-width="1"/>')
    s.append(f'<text x="{x0 + steps * sw / 2}" y="{H - 18}" text-anchor="middle" font-size="12" fill="#555" font-style="italic">{t["note"]}</text>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    for lang in LABELS:
        (OUT / f"gamut-mask.{lang}.svg").write_text(render(lang), encoding="utf-8")
        print(f"wrote gamut-mask.{lang}.svg")
