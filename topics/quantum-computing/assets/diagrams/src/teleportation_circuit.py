"""Teleportation circuit -> teleportation-circuit.<lang>.svg

Wires Q (|ψ⟩), A and B (sharing |φ+⟩). Alice: CNOT Q→A, H on Q, measure A -> a and Q -> b.
Bob: X^a then Z^b on B. The table of Bob's state per outcome is computed from
|ψ⟩ = α|0⟩ + β|1⟩ by applying X^a Z^b symbolically (as coefficient pairs).
"""
from __future__ import annotations

from svgkit import ACCENT, ACCENT2, INK, MUTED, cnot, gate, line, meter, rect, svg, text, vwire, wire, write

LABELS = {
    "es": {
        "alice": "Alice",
        "bob": "Bob",
        "bell": "|φ⁺⟩",
        "table_title": "Estado de B antes de corregir",
        "out": "|ψ⟩",
    },
}

W, H = 900, 520


def bob_state(a: int, b: int) -> str:
    """X^a Z^b (α|0⟩ + β|1⟩) as a ket expression, coefficients ordered by basis state."""
    coeffs = [(1, "α"), (-1 if b else 1, "β")]   # Z^b flips the sign of the |1⟩ amplitude
    if a:                                         # X swaps the |0⟩ and |1⟩ amplitudes
        coeffs = [coeffs[1], coeffs[0]]
    out = ""
    for k, (sign, name) in enumerate(coeffs):
        if k == 0:
            out += ("−" if sign < 0 else "") + f"{name}|{k}⟩"
        else:
            out += (" − " if sign < 0 else " + ") + f"{name}|{k}⟩"
    return out


def build(lang: str) -> str:
    t = LABELS[lang]
    yq, ya, yb = 90, 180, 290
    b: list[str] = []
    for y, lab in ((yq, "Q  |ψ⟩"), (ya, "A"), (yb, "B")):
        b.append(text(70, y + 6, lab, 18, anchor="end"))
    # Bell pair bracket
    b.append(line(80, ya, 80, yb, ACCENT2, 3))
    b.append(text(92, (ya + yb) / 2 + 6, t["bell"], 16, ACCENT2, anchor="start", weight="bold"))
    b.append(wire(150, 420, yq)); b.append(wire(150, 420, ya)); b.append(wire(80, 760, yb))
    b.append(wire(80, 150, yq)); b.append(wire(80, 150, ya))
    b.append(cnot(220, yq, ya))
    b.append(gate(310, yq, "H"))
    b.append(meter(420, yq)); b.append(meter(420, ya))
    # classical wires down to Bob's gates
    xa, xb = 560, 660
    b.append(wire(442, xb, yq, classical=True)); b.append(text(470, yq - 12, "b", 16, INK, italic=True))
    b.append(wire(442, xa, ya, classical=True)); b.append(text(470, ya - 12, "a", 16, INK, italic=True))
    b.append(vwire(xa, ya, yb - 22, classical=True))
    b.append(vwire(xb, yq, yb - 22, classical=True))
    b.append(gate(xa, yb, "X", fill="#fde3d3", stroke=ACCENT2))
    b.append(gate(xb, yb, "Z", fill="#fde3d3", stroke=ACCENT2))
    b.append(text(780, yb + 6, t["out"], 18, ACCENT, anchor="start", weight="bold"))
    # Alice / Bob regions
    b.append(rect(160, 40, 300, 175, MUTED, "none", 1, rx=10))
    b.append(text(310, 32, t["alice"], 15, MUTED))
    b.append(rect(520, 250, 190, 80, MUTED, "none", 1, rx=10))
    b.append(text(615, 350, t["bob"], 15, MUTED))
    # outcome table
    b.append(text(450, 395, t["table_title"], 15, INK, weight="bold"))
    for i, (a, bb) in enumerate(((0, 0), (0, 1), (1, 0), (1, 1))):
        x = 120 + i * 190
        b.append(text(x + 40, 430, f"a={a}, b={bb}", 14, MUTED))
        b.append(text(x + 40, 458, bob_state(a, bb), 16, ACCENT))
        corr = {(0, 0): "—", (0, 1): "Z", (1, 0): "X", (1, 1): "X, Z"}[(a, bb)]
        b.append(text(x + 40, 486, corr, 14, ACCENT2))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"teleportation-circuit.{lang}.svg", build(lang)))
