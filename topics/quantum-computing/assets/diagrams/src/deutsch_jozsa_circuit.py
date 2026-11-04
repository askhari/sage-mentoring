"""Deutsch-Jozsa circuit -> deutsch-jozsa-circuit.<lang>.svg

n input qubits in |0^n⟩ and one auxiliary qubit in |1⟩; H on all; one query U_f;
H^{⊗n} on the inputs; measure. Output 0^n means constant, anything else means balanced.
"""
from __future__ import annotations

from svgkit import ACCENT2, gate, meter, multigate, slash, svg, text, wire, write

LABELS = {
    "es": {
        "query": "una sola consulta",
        "rule": "Resultado 0ⁿ → constante; otro resultado → equilibrada",
        "inputs": "n qubits",
    },
}

W, H = 820, 300


def build(lang: str) -> str:
    t = LABELS[lang]
    yx, ya = 90, 190
    b: list[str] = []
    b.append(text(95, yx + 6, "|0ⁿ⟩", 18, anchor="end"))
    b.append(text(95, ya + 6, "|1⟩", 18, anchor="end"))
    b.append(wire(105, 650, yx)); b.append(wire(105, 560, ya))
    b.append(slash(130, yx, t["inputs"]))
    b.append(gate(200, yx, "H⊗ⁿ")); b.append(gate(200, ya, "H"))
    b.append(multigate(340, yx, ya, "U_f", width=80, fill="#fde3d3", stroke=ACCENT2, size=22))
    b.append(text(340, ya + 52, t["query"], 14, ACCENT2))
    b.append(gate(480, yx, "H⊗ⁿ"))
    b.append(meter(600, yx))
    b.append(text(410, 275, t["rule"], 15, anchor="middle"))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"deutsch-jozsa-circuit.{lang}.svg", build(lang)))
