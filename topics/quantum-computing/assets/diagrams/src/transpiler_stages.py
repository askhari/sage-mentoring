"""The six stages of Qiskit's preset pass managers -> transpiler-stages.<lang>.svg

Stage names and roles as in the Qiskit docs (guides/transpile): init, layout, routing,
translation, optimization, scheduling. Input: abstract circuit; output: ISA circuit.
"""
from __future__ import annotations

from svgkit import ACCENT, ACCENT2, ACCENT3, MUTED, block, line, svg, text, write

LABELS = {
    "es": {
        "in": ["Circuito", "abstracto"],
        "out": ["Circuito ISA", "(ejecutable)"],
        "stages": [
            ("init", ["puertas de 3+ qubits", "→ de 1 y 2 qubits"]),
            ("layout", ["qubits virtuales", "→ físicos"]),
            ("routing", ["inserta SWAP donde", "no hay acoplamiento"]),
            ("translation", ["a las puertas", "nativas (base)"]),
            ("optimization", ["simplifica; repite", "hasta una condición"]),
            ("scheduling", ["temporiza; opcional", "(p. ej. desacoplo)"]),
        ],
        "target": "Target del backend: puertas nativas, conectividad (CouplingMap), duraciones",
    },
}

W, H = 1280, 290


def build(lang: str) -> str:
    t = LABELS[lang]
    b: list[str] = []
    y, bh = 80, 110
    b.append(block(10, y + 15, 110, 80, t["in"], fill="#f2f2f2", size=14))
    x, bw, gap = 150, 150, 12
    xs = []
    for name, lines in t["stages"]:
        b.append(block(x, y, bw, bh, lines, fill="#dbe9f6", stroke=ACCENT, size=13, title=name, title_color=ACCENT))
        xs.append(x)
        x += bw + gap
    b.append(block(x + 16, y + 15, 120, 80, t["out"], fill="#e3f2e8", stroke=ACCENT3, size=14))
    b.append(line(122, y + bh / 2, 148, y + bh / 2, ACCENT, 2, arrow="a1"))
    for xi in xs[:-1]:
        b.append(line(xi + bw + 1, y + bh / 2, xi + bw + gap - 1, y + bh / 2, ACCENT, 2, arrow="a1"))
    b.append(line(xs[-1] + bw + 1, y + bh / 2, x + 14, y + bh / 2, ACCENT, 2, arrow="a1"))
    # target feeding layout..scheduling
    ty = 250
    b.append(line(xs[1] + 20, ty - 14, xs[-1] + bw - 20, ty - 14, ACCENT2, 1.6))
    for xi in xs[1:]:
        b.append(line(xi + bw / 2, ty - 14, xi + bw / 2, y + bh + 4, ACCENT2, 1.4, dash="4 3", arrow="a2"))
    b.append(text((xs[1] + xs[-1] + bw) / 2, ty + 10, t["target"], 14, ACCENT2))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"transpiler-stages.{lang}.svg", build(lang)))
