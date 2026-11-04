"""Three-qubit bit-flip code with syndrome extraction -> bit-flip-code-circuit.<lang>.svg

Encode α|0⟩+β|1⟩ → α|000⟩+β|111⟩ with two CNOTs; an X error may hit one qubit; two
ancillas measure the parities Z0Z1 and Z1Z2 without measuring the data; the syndrome
(s1, s2) says which qubit to flip back. Syndrome table computed here.
"""
from __future__ import annotations

from svgkit import ACCENT, ACCENT2, ACCENT3, INK, MUTED, block, cnot, gate, line, meter, rect, svg, text, wire, write

LABELS = {
    "es": {
        "enc": "codificar",
        "err": "error (X en un qubit, o nada)",
        "syn": "medir paridades (síndrome)",
        "fix": "corregir",
        "table_t": "Síndrome → corrección",
        "rows": [("0 0", "nada"), ("1 0", "X en q0"), ("1 1", "X en q1"), ("0 1", "X en q2")],
        "s1": "s1 = paridad q0⊕q1",
        "s2": "s2 = paridad q1⊕q2",
        "note": "Las ancillas miden solo paridades: el estado α|000⟩+β|111⟩ no se mide ni se copia.",
    },
}

W, H = 1180, 470


def build(lang: str) -> str:
    t = LABELS[lang]
    ys = [80, 150, 220, 310, 380]
    labels = ["α|0⟩+β|1⟩", "|0⟩", "|0⟩", "|0⟩", "|0⟩"]
    names = ["q0", "q1", "q2", "a1", "a2"]
    b: list[str] = []
    for y, lab, nm in zip(ys, labels, names):
        b.append(text(118, y + 6, lab, 16, anchor="end"))
        b.append(text(140, y - 12, nm, 11, MUTED))
    for y in ys[:3]:
        b.append(wire(130, 860, y))
    for y in ys[3:]:
        b.append(wire(130, 690, y))
    # encoding
    b.append(cnot(190, ys[0], ys[1]))
    b.append(cnot(250, ys[0], ys[2]))
    b.append(text(220, 40, t["enc"], 14, ACCENT, weight="bold"))
    # error region
    b.append(rect(300, 52, 90, 196, ACCENT2, "#fde3d3", 1.6, rx=6))
    b.append(text(345, 155, "E", 26, ACCENT2, weight="bold"))
    b.append(text(345, 40, t["err"], 13, ACCENT2))
    # syndrome extraction
    b.append(cnot(440, ys[0], ys[3]))
    b.append(cnot(500, ys[1], ys[3]))
    b.append(cnot(570, ys[1], ys[4]))
    b.append(cnot(630, ys[2], ys[4]))
    b.append(text(535, 40, t["syn"], 14, ACCENT3, weight="bold"))
    b.append(meter(700, ys[3]))
    b.append(meter(700, ys[4]))
    b.append(text(730, ys[3] + 5, "s1", 14, anchor="start"))
    b.append(text(730, ys[4] + 5, "s2", 14, anchor="start"))
    # correction
    for y in ys[:3]:
        b.append(gate(800, y, "X?", fill="#e3f2e8", stroke=ACCENT3))
    b.append(line(722, ys[3] - 25, 790, ys[2] + 26, MUTED, 1.4, dash="4 3", arrow="muted"))
    b.append(text(800, 40, t["fix"], 14, ACCENT3, weight="bold"))
    # table
    tx, ty = 900, 90
    b.append(text(tx + 120, ty - 10, t["table_t"], 14, INK, weight="bold"))
    b.append(text(tx + 40, ty + 20, "s1 s2", 13, MUTED))
    for i, (s, fix) in enumerate(t["rows"]):
        y = ty + 50 + i * 30
        b.append(text(tx + 40, y, s, 14))
        b.append(text(tx + 100, y, fix, 14, anchor="start"))
    b.append(text(tx + 120, ty + 190, t["s1"], 12, MUTED))
    b.append(text(tx + 120, ty + 210, t["s2"], 12, MUTED))
    b.append(text(W / 2, H - 14, t["note"], 13, MUTED))
    return svg(W, H, b)


def syndrome(err_qubit):
    bits = [0, 0, 0]
    if err_qubit is not None:
        bits[err_qubit] = 1
    return (bits[0] ^ bits[1], bits[1] ^ bits[2])


if __name__ == "__main__":
    # check the table against the parity definitions
    assert [syndrome(q) for q in (None, 0, 1, 2)] == [(0, 0), (1, 0), (1, 1), (0, 1)]
    for lang in LABELS:
        print(write(f"bit-flip-code-circuit.{lang}.svg", build(lang)))
