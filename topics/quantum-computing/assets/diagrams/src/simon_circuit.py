"""Simon's algorithm -> simon-circuit.<lang>.svg

Top register (n qubits): H^{⊗n}, U_f, H^{⊗n}, measure -> y with y·s = 0 (mod 2).
Bottom register (m qubits) in |0^m⟩ only enters U_f. Then the classical step:
repeat ~n times and solve the linear system mod 2 for s.
"""
from __future__ import annotations

from svgkit import ACCENT, ACCENT2, ACCENT3, block, gate, line, meter, multigate, slash, svg, text, wire, write

LABELS = {
    "es": {
        "top": "n qubits",
        "bottom": "m qubits",
        "y": "y con y · s = 0 (mod 2)",
        "classical_title": "Paso clásico",
        "classical": ["Repetir unas n veces", "(n + 10 en Watrous)", "Resolver el sistema", "lineal módulo 2 → s"],
        "quantum": "Parte cuántica (una consulta por ejecución)",
    },
}

W, H = 1000, 320


def build(lang: str) -> str:
    t = LABELS[lang]
    yx, yb = 100, 210
    b: list[str] = []
    b.append(text(95, yx + 6, "|0ⁿ⟩", 18, anchor="end"))
    b.append(text(95, yb + 6, "|0ᵐ⟩", 18, anchor="end"))
    b.append(wire(105, 600, yx)); b.append(wire(105, 400, yb))
    b.append(slash(130, yx, t["top"])); b.append(slash(130, yb, t["bottom"]))
    b.append(gate(200, yx, "H⊗ⁿ"))
    b.append(multigate(310, yx, yb, "U_f", width=80, fill="#fde3d3", stroke=ACCENT2, size=22))
    b.append(gate(430, yx, "H⊗ⁿ"))
    b.append(meter(540, yx))
    b.append(wire(562, 690, yx, classical=True))
    b.append(text(560, yx - 34, t["y"], 14, ACCENT, anchor="middle"))
    b.append(text(330, 290, t["quantum"], 14, ACCENT2))
    b.append(line(690, yx, 712, yx, ACCENT3, 2, arrow="a3"))
    b.append(block(715, 40, 250, 160, t["classical"], fill="#e3f2e8", stroke=ACCENT3, size=15, title=t["classical_title"], title_color=ACCENT3))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"simon-circuit.{lang}.svg", build(lang)))
