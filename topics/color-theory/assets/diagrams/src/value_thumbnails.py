"""Value structure of one simple landscape -> value-structure-thumbnails.<lang>.svg

Top row: the scene in colour and the same scene in greys of equal CIELAB lightness
(grey_hex(L*) of each colour), to show that a colour picture carries a value pattern.
Bottom row: three-value thumbnails (light L* 85, middle L* 55, dark L* 25) of the
same composition with different value plans, in which light, middle or dark covers
most of the area. Illustrates the few-value planning described by Gurney (gurney-2010,
'Value Planning', 'Loomis's Scheme for Tonal Organization'); the scene is invented.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from colormath import grey_hex, hex_lab, lch_hex  # noqa: E402

LABELS = {
    "es": {
        "colour": "En color",
        "grey": "El mismo cuadro en grises",
        "plans": ["Domina el claro", "Domina el medio", "Domina el oscuro"],
        "legend": ["claro", "medio", "oscuro"],
    },
}

TW, TH = 240, 170  # thumbnail size


def zones(x: float, y: float) -> dict[str, str]:
    """SVG shapes of the scene, keyed by zone: sky, hills, field, ground, tree."""
    def p(pts):
        return " ".join(f"{x + a * TW:.1f},{y + b * TH:.1f}" for a, b in pts)
    return {
        "sky": f'<rect x="{x}" y="{y}" width="{TW}" height="{TH}"',
        "hills": f'<polygon points="{p([(0, .52), (.18, .36), (.38, .46), (.6, .30), (.82, .44), (1, .38), (1, .62), (0, .62)])}"',
        "field": f'<polygon points="{p([(0, .60), (1, .58), (1, .80), (0, .84)])}"',
        "ground": f'<polygon points="{p([(0, .82), (1, .78), (1, 1), (0, 1)])}"',
        "tree": f'<path d="M{x + .70 * TW:.1f},{y + .86 * TH:.1f} l6,0 l0,-38 l-6,0 Z '
                f'M{x + .71 * TW:.1f},{y + .22 * TH:.1f} a30,34 0 1 0 0.1,0 Z"',
    }


ORDER = ["sky", "hills", "field", "ground", "tree"]
COLOURS = {  # LCh of each zone in the colour version
    "sky": (82, 18, 245), "hills": (62, 16, 285), "field": (70, 42, 110),
    "ground": (46, 30, 80), "tree": (32, 26, 145),
}
LEVELS = {"L": 85, "M": 55, "D": 25}
PLANS = [  # value class per zone
    {"sky": "L", "hills": "L", "field": "L", "ground": "M", "tree": "D"},
    {"sky": "L", "hills": "M", "field": "M", "ground": "M", "tree": "D"},
    {"sky": "M", "hills": "D", "field": "D", "ground": "D", "tree": "L"},
]
W, H = 3 * TW + 4 * 30, 2 * TH + 170
OUT = Path(__file__).resolve().parent.parent


def draw(x: float, y: float, fills: dict[str, str]) -> list[str]:
    z = zones(x, y)
    out = [f'{z[k]} fill="{fills[k]}"/>' for k in ORDER]
    out.append(f'<rect x="{x}" y="{y}" width="{TW}" height="{TH}" fill="none" stroke="#333" stroke-width="1"/>')
    return out


def render(lang: str) -> str:
    t = LABELS[lang]
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="14">',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
    colour = {k: lch_hex(*v) for k, v in COLOURS.items()}
    grey = {k: grey_hex(hex_lab(c)[0]) for k, c in colour.items()}
    y1, y2 = 20, TH + 90
    x_c = (W - 2 * TW - 30) / 2
    for i, (fills, title) in enumerate([(colour, t["colour"]), (grey, t["grey"])]):
        x = x_c + i * (TW + 30)
        s += draw(x, y1, fills)
        s.append(f'<text x="{x + TW / 2}" y="{y1 + TH + 22}" text-anchor="middle" fill="#222" font-weight="bold">{title}</text>')
    for i, plan in enumerate(PLANS):
        x = 30 + i * (TW + 30)
        s += draw(x, y2, {k: grey_hex(LEVELS[v]) for k, v in plan.items()})
        s.append(f'<text x="{x + TW / 2}" y="{y2 + TH + 22}" text-anchor="middle" fill="#222" font-weight="bold">{t["plans"][i]}</text>')
    # Legend of the three values.
    ly = y2 + TH + 48
    lx = W / 2 - 150
    for i, key in enumerate("LMD"):
        s.append(f'<rect x="{lx + i * 105}" y="{ly}" width="22" height="16" fill="{grey_hex(LEVELS[key])}" stroke="#333" stroke-width="0.8"/>')
        s.append(f'<text x="{lx + i * 105 + 28}" y="{ly + 13}" fill="#333" font-size="13">{t["legend"][i]}</text>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    for lang in LABELS:
        (OUT / f"value-structure-thumbnails.{lang}.svg").write_text(render(lang), encoding="utf-8")
        print(f"wrote value-structure-thumbnails.{lang}.svg")
