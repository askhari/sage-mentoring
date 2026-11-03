"""Sequential Stern-Gerlach z -> x -> z -> stern-gerlach-zxz.<lang>.svg

Fractions come from the Born rule with |z+> = (|x+> + |x->)/sqrt2 and
|x-> = (|z+> - |z->)/sqrt2, computed explicitly.
"""
from __future__ import annotations

import math

from svgkit import ACCENT, ACCENT2, INK, MUTED, line, rect, svg, text, write

LABELS = {
    "es": {
        "atoms": "átomos",
        "blocked": "bloqueado",
        "note": "Porcentajes del haz que entra en cada caja. El filtro z del principio no deja memoria:",
        "note2": "tras medir x, vuelve a salir 50 % / 50 % en z.",
    },
}

W, H = 920, 360
S = 1 / math.sqrt(2)


def build(lang: str) -> str:
    t = LABELS[lang]
    # amplitudes
    z_plus = {"x+": S, "x-": S}           # <x±|z+>
    x_minus = {"z+": S, "z-": -S}          # <z±|x->
    p_x = {k: v * v for k, v in z_plus.items()}
    p_z = {k: v * v for k, v in x_minus.items()}
    p_unpol = 0.5                           # unpolarized beam: half S_z=+, half S_z=- (Stern-Gerlach)
    f1 = p_unpol                            # beam after first box, S_z=+ kept
    f2 = f1 * p_x["x-"]                     # fraction entering third box
    f3p, f3m = f2 * p_z["z+"], f2 * p_z["z-"]
    b: list[str] = []
    y = 170
    boxes = [(110, "z"), (420, "x"), (730, "z")]
    for x, lab in boxes:
        b.append(rect(x, y - 45, 90, 90, INK, "#eef3f9", 2, rx=8))
        b.append(text(x + 45, y + 10, lab, 30, ACCENT, weight="bold", italic=True))
    b.append(line(20, y, 110, y, ACCENT, 3, arrow="a1"))
    b.append(text(60, y - 14, t["atoms"], 13, MUTED))
    # box 1 outputs
    b.append(line(200, y - 20, 420, y, ACCENT, 3, arrow="a1"))
    b.append(text(300, y - 34, f"+  {p_unpol*100:.0f} %", 15, ACCENT, weight="bold"))
    b.append(line(200, y + 20, 290, y + 80, ACCENT2, 2.5))
    b.append(line(275, y + 92, 305, y + 68, INK, 5))
    b.append(text(312, y + 100, f"−  {p_unpol*100:.0f} %  ({t['blocked']})", 14, ACCENT2, anchor="start"))
    # box 2 outputs
    b.append(line(510, y - 20, 600, y - 80, ACCENT2, 2.5))
    b.append(line(598, y - 98, 598, y - 62, INK, 5))
    b.append(text(612, y - 92, f"+  {p_x['x+']*100:.0f} %  ({t['blocked']})", 14, ACCENT2, anchor="start"))
    b.append(line(510, y + 20, 730, y, ACCENT, 3, arrow="a1"))
    b.append(text(610, y + 42, f"−  {p_x['x-']*100:.0f} %", 15, ACCENT, weight="bold"))
    # box 3 outputs
    b.append(line(820, y - 20, 900, y - 70, ACCENT, 3, arrow="a1"))
    b.append(text(880, y - 82, f"+  {p_z['z+']*100:.0f} %", 15, ACCENT, weight="bold", anchor="end"))
    b.append(line(820, y + 20, 900, y + 70, ACCENT, 3, arrow="a1"))
    b.append(text(880, y + 96, f"−  {p_z['z-']*100:.0f} %", 15, ACCENT, weight="bold", anchor="end"))
    assert abs(f3p - 0.125) < 1e-9 and abs(f3m - 0.125) < 1e-9
    b.append(text(W / 2, H - 46, t["note"], 15, INK))
    b.append(text(W / 2, H - 24, t["note2"], 15, INK))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"stern-gerlach-zxz.{lang}.svg", build(lang)))
