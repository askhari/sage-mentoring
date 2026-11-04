"""QFT on 4 qubits -> qft-circuit.<lang>.svg

Standard ladder: on qubit j, H then controlled-R_s (s = 2, 3, ...) controlled by the
following qubits, with R_s = diag(1, e^{2πi/2^s}); final swaps reverse the order.
Output phases (unnormalised) are listed per wire after the swaps; they are generated from
the binary-fraction product form, so the labels always match the gate ladder.
"""
from __future__ import annotations

from svgkit import ACCENT, ACCENT2, MUTED, control, gate, swap, svg, text, vwire, wire, write

N = 4
LABELS = {
    "es": {
        "note": "Salida sin normalizar (falta 1/√2 por qubit). Coste: n(n+1)/2 = {g} puertas y {s} swaps para n = {n}.",
    },
}

W, H = 1180, 380
SUB = "₀₁₂₃₄₅₆₇₈₉"


def sub(k: int) -> str:
    return "".join(SUB[int(c)] for c in str(k))


def build(lang: str) -> str:
    t = LABELS[lang]
    ys = [70 + 70 * i for i in range(N)]
    b: list[str] = []
    for i, y in enumerate(ys):
        b.append(text(80, y + 6, f"|k{sub(i + 1)}⟩", 18, anchor="end"))
    x = 140
    cols: list[tuple] = []
    for j in range(N):
        cols.append(("H", j))
        for c in range(j + 1, N):
            cols.append(("R", j, c, c - j + 1))
    xend = x + 62 * (len(cols) + 1) + 60
    for y in ys:
        b.append(wire(90, xend, y))
    gates = 0
    for col in cols:
        if col[0] == "H":
            b.append(gate(x, ys[col[1]], "H")); gates += 1
        else:
            _, j, c, s = col
            b.append(vwire(x, ys[j] + 22, ys[c]))
            b.append(gate(x, ys[j], f"R{sub(s)}", fill="#fde3d3", stroke=ACCENT2))
            b.append(control(x, ys[c])); gates += 1
        x += 62
    x += 20
    swaps = 0
    for i in range(N // 2):
        b.append(swap(x + 30 * i, ys[i], ys[N - 1 - i])); swaps += 1
    # output labels: after the swaps, wire i carries 0.k_{N-i} ... k_N
    for i, y in enumerate(ys):
        start = N - i
        frac = "0." + "".join(f"k{sub(m)}" for m in range(start, N + 1))
        b.append(text(xend + 10, y + 6, f"|0⟩ + e^(2πi·{frac}) |1⟩", 16, ACCENT, anchor="start"))
    b.append(text(W / 2, H - 25, t["note"].format(g=gates, s=swaps, n=N), 14, MUTED))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"qft-circuit.{lang}.svg", build(lang)))
