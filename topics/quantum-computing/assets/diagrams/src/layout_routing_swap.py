"""Routing a CX between non-adjacent physical qubits -> layout-routing-swap.<lang>.svg

Left: a small coupling map (fragment in the style of a heavy-hex lattice: a row of
qubits linked to the next row through bridge qubits). Virtual qubits a and b sit on
physical 0 and 2, which are not coupled. Right: the logical CX(a, b) before routing,
and after routing: SWAP(0, 1) then CX(1, 2). A SWAP costs three CX, so one logical
two-qubit gate becomes four.
"""
from __future__ import annotations

from svgkit import ACCENT, ACCENT2, INK, MUTED, circle, cnot, line, swap, text, wire, svg, write

LABELS = {
    "es": {
        "map": "Mapa de acoplamiento (fragmento)",
        "before": "Antes del routing: CX(a, b) con a en 0 y b en 2 (no acoplados)",
        "after": "Después: SWAP(0, 1) acerca a; luego CX(1, 2)",
        "count_before": "1 puerta de dos qubits",
        "count_after": "SWAP = 3 CX → 4 puertas de dos qubits",
        "phys": "físico",
    },
}

W, H = 1180, 460
# physical qubit positions (index -> x, y)
POS = {0: (60, 120), 1: (140, 120), 2: (220, 120), 3: (300, 120), 4: (380, 120),
       5: (60, 210), 6: (380, 210),
       7: (60, 300), 8: (140, 300), 9: (220, 300), 10: (300, 300), 11: (380, 300)}
EDGES = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 5), (5, 7), (4, 6), (6, 11),
         (7, 8), (8, 9), (9, 10), (10, 11)]


def build(lang: str) -> str:
    t = LABELS[lang]
    b: list[str] = []
    ox, oy = 20, 20
    b.append(text(ox + 220, 50, t["map"], 15, INK, weight="bold"))
    for i, j in EDGES:
        (x1, y1), (x2, y2) = POS[i], POS[j]
        on_path = (i, j) in [(0, 1), (1, 2)]
        b.append(line(ox + x1, oy + y1, ox + x2, oy + y2, ACCENT2 if on_path else MUTED, 3 if on_path else 2))
    for q, (x, y) in POS.items():
        hl = q in (0, 2)
        b.append(circle(ox + x, oy + y, 18, ACCENT if hl else INK, "#dbe9f6" if hl else "white", 2))
        b.append(text(ox + x, oy + y + 5, str(q), 14))
    b.append(text(ox + 60, oy + 85, "a", 16, ACCENT, italic=True, weight="bold"))
    b.append(text(ox + 220, oy + 85, "b", 16, ACCENT, italic=True, weight="bold"))
    # dashed wish-line between 0 and 2
    b.append(f"<path d='M{ox+60},{oy+138} Q{ox+140},{oy+190} {ox+220},{oy+138}' stroke='{ACCENT}' "
             "fill='none' stroke-width='1.6' stroke-dasharray='5 4'/>")
    b.append(text(ox + 140, oy + 182, "CX?", 13, ACCENT))

    # circuits
    cx0, ys = 560, [130, 175, 220]
    b.append(text(cx0 + 280, 70, t["before"], 14, INK))
    for q, y in enumerate(ys):
        b.append(text(cx0 - 20, y + 5, f"{q}", 14, MUTED, anchor="end"))
        b.append(wire(cx0, cx0 + 200, y))
    b.append(cnot(cx0 + 100, ys[0], ys[2]))
    b.append(text(cx0 + 360, ys[1] + 5, t["count_before"], 14, ACCENT2, anchor="start"))

    ys2 = [y + 200 for y in ys]
    b.append(text(cx0 + 280, 285, t["after"], 14, INK))
    for q, y in enumerate(ys2):
        b.append(text(cx0 - 20, y + 5, f"{q}", 14, MUTED, anchor="end"))
        b.append(wire(cx0, cx0 + 300, y))
    b.append(swap(cx0 + 90, ys2[0], ys2[1]))
    b.append(cnot(cx0 + 210, ys2[1], ys2[2]))
    b.append(text(cx0 + 360, ys2[1] + 5, t["count_after"], 14, ACCENT2, anchor="start"))
    b.append(text(cx0 - 40, 100, t["phys"], 12, MUTED, anchor="end"))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"layout-routing-swap.{lang}.svg", build(lang)))
