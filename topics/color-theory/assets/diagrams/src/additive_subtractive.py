"""Additive vs subtractive mixing with ideal primaries -> additive-vs-subtractive-overlaps.<lang>.svg

Left: three overlapping lights (sRGB primaries) on black; overlaps add light.
Right: three overlapping ideal filters/inks (cyan, magenta, yellow) on white; each
removes one third of the spectrum, so overlaps get darker. Region colours are the
ideal (block) results, computed explicitly, not blend modes: schematic, not
measurements of real lights or inks.
"""
from __future__ import annotations

from pathlib import Path

OUT = Path(__file__).resolve().parent.parent

LABELS = {
    "es": {
        "add": "Mezcla aditiva: luces",
        "sub": "Mezcla sustractiva: filtros y tintas",
        "add_note": "cada luz añade energía → más claro",
        "sub_note": "cada filtro quita una parte → más oscuro",
        "names": {"R": "rojo", "G": "verde", "B": "azul", "C": "cian", "M": "magenta", "Y": "amarillo"},
        "white": "blanco",
        "dark": "negro",
    },
}

W, H, R = 900, 470, 95
# Channel sets: which thirds of the spectrum (r, g, b) each primary passes/emits.
ADD = {"R": (1, 0, 0), "G": (0, 1, 0), "B": (0, 0, 1)}
SUB = {"C": (0, 1, 1), "M": (1, 0, 1), "Y": (1, 1, 0)}


def hexc(rgb: tuple[int, int, int]) -> str:
    return "#" + "".join("ff" if c else "00" for c in rgb)


def combine(sets: list[tuple[int, int, int]], additive: bool) -> tuple[int, int, int]:
    if additive:
        return tuple(int(any(s[i] for s in sets)) for i in range(3))
    return tuple(int(all(s[i] for s in sets)) for i in range(3))


def panel(cx: float, cy: float, prims: dict, additive: bool, uid: str, t: dict) -> list[str]:
    keys = list(prims)
    off = 0.62 * R
    centres = {keys[0]: (cx, cy - off), keys[1]: (cx - off * 0.87, cy + off * 0.5), keys[2]: (cx + off * 0.87, cy + off * 0.5)}
    s = ["<defs>"]
    for k, (x, y) in centres.items():
        s.append(f'<clipPath id="{uid}{k}"><circle cx="{x:.1f}" cy="{y:.1f}" r="{R}"/></clipPath>')
    s.append("</defs>")
    circ = lambda k: f'<circle cx="{centres[k][0]:.1f}" cy="{centres[k][1]:.1f}" r="{R}"'
    for k in keys:  # single regions
        s.append(f'{circ(k)} fill="{hexc(prims[k])}"/>')
    for i in range(3):  # pairwise overlaps
        a, b = keys[i], keys[(i + 1) % 3]
        s.append(f'<g clip-path="url(#{uid}{b})">{circ(a)} fill="{hexc(combine([prims[a], prims[b]], additive))}"/></g>')
    a, b, c = keys
    s.append(f'<g clip-path="url(#{uid}{c})"><g clip-path="url(#{uid}{b})">{circ(a)} '
             f'fill="{hexc(combine(list(prims.values()), additive))}"/></g></g>')
    # labels outside the circles
    lab_col = "#fff" if additive else "#222"
    for k, (x, y) in centres.items():
        dx, dy = x - cx, y - cy
        n = (dx * dx + dy * dy) ** 0.5
        lx, ly = cx + dx / n * (off + R + (22 if dy < 0 else 34)), cy + dy / n * (off + R + (22 if dy < 0 else 34))
        s.append(f'<text x="{lx:.1f}" y="{ly + 5:.1f}" text-anchor="middle" fill="{lab_col}" font-weight="bold">{t["names"][k]}</text>')
    centre_label = t["white"] if additive else t["dark"]
    s.append(f'<text x="{cx}" y="{cy + 5}" text-anchor="middle" fill="{"#000" if additive else "#fff"}" font-size="12">{centre_label}</text>')
    return s


def render(lang: str) -> str:
    t = LABELS[lang]
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="14">',
         f'<rect x="0" y="0" width="{W / 2}" height="{H}" fill="#000"/>',
         f'<rect x="{W / 2}" y="0" width="{W / 2}" height="{H}" fill="#fff"/>',
         f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" fill="none" stroke="#999"/>']
    s.append(f'<text x="{W / 4}" y="32" text-anchor="middle" fill="#fff" font-size="17" font-weight="bold">{t["add"]}</text>')
    s.append(f'<text x="{3 * W / 4}" y="32" text-anchor="middle" fill="#222" font-size="17" font-weight="bold">{t["sub"]}</text>')
    s += panel(W / 4, 240, ADD, True, "a", t)
    s += panel(3 * W / 4, 240, SUB, False, "s", t)
    s.append(f'<text x="{W / 4}" y="{H - 16}" text-anchor="middle" fill="#ddd">{t["add_note"]}</text>')
    s.append(f'<text x="{3 * W / 4}" y="{H - 16}" text-anchor="middle" fill="#444">{t["sub_note"]}</text>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    for lang in LABELS:
        (OUT / f"additive-vs-subtractive-overlaps.{lang}.svg").write_text(render(lang), encoding="utf-8")
