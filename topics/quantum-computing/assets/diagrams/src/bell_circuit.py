"""Bell-state circuit H + CNOT with the state after each step -> bell-circuit.<lang>.svg

The states under the circuit are computed by applying the gate matrices to the 4-vector
(order |q0 q1⟩, q0 written first), then formatted as kets.
"""
from __future__ import annotations

import math

from svgkit import ACCENT, INK, MUTED, cnot, gate, line, svg, text, wire, write

LABELS = {"es": {"step": ["inicio", "tras H", "tras CNOT"]}}

W, H = 760, 330
S = 1 / math.sqrt(2)


def apply_h_q0(v):
    a00, a01, a10, a11 = v
    return [S * (a00 + a10), S * (a01 + a11), S * (a00 - a10), S * (a01 - a11)]


def apply_cnot(v):
    a00, a01, a10, a11 = v
    return [a00, a01, a11, a10]


def ket(v) -> str:
    terms = [(c, lab) for c, lab in zip(v, ["00", "01", "10", "11"]) if abs(c) > 1e-9]
    if len(terms) == 1:
        return f"|{terms[0][1]}⟩"
    assert all(abs(abs(c) - S) < 1e-9 for c, _ in terms)
    body = " ".join(("+ " if c > 0 else "− ") + f"|{lab}⟩" for c, lab in terms).lstrip("+ ")
    return f"({body})/√2"


def build(lang: str) -> str:
    t = LABELS[lang]
    v0 = [1, 0, 0, 0]
    v1 = apply_h_q0(v0)
    v2 = apply_cnot(v1)
    y0, y1 = 80, 170
    b: list[str] = []
    b.append(text(70, y0 + 6, "q₀  |0⟩", 18, anchor="end"))
    b.append(text(70, y1 + 6, "q₁  |0⟩", 18, anchor="end"))
    b.append(wire(80, W - 60, y0))
    b.append(wire(80, W - 60, y1))
    b.append(gate(280, y0, "H"))
    b.append(cnot(470, y0, y1))
    # step markers and states
    for x, lab, v in ((150, t["step"][0], v0), (375, t["step"][1], v1), (620, t["step"][2], v2)):
        b.append(line(x, y0 - 40, x, y1 + 40, MUTED, 1, dash="4,4"))
        b.append(text(x, y1 + 70, lab, 14, MUTED))
        b.append(text(x, y1 + 100, ket(v), 18, ACCENT, weight="bold"))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"bell-circuit.{lang}.svg", build(lang)))
