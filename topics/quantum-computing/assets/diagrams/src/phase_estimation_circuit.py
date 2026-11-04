"""Phase estimation -> phase-estimation-circuit.<lang>.svg

m control qubits in |0⟩, H on each, controlled-U^{2^k} from control k on the |ψ⟩ register,
inverse QFT on the controls, measure. Marks the intermediate state 2^{-m/2} Σ_x e^{2πixθ}|x⟩.
Three explicit controls (k = 0, 1, m−1) with a dotted row for the rest.
"""
from __future__ import annotations

from svgkit import ACCENT, ACCENT2, MUTED, control, gate, line, meter, multigate, slash, svg, text, vwire, wire, write

LABELS = {
    "es": {
        "state": "2^(−m/2) Σₓ e^(2πi x θ) |x⟩",
        "psi": "|ψ⟩ (no cambia)",
        "out": "y  →  θ ≈ y / 2ᵐ",
        "eig": "U|ψ⟩ = e^(2πiθ) |ψ⟩",
    },
}

W, H = 980, 470


def build(lang: str) -> str:
    t = LABELS[lang]
    yc = [70, 140, 260]          # controls k = 0, 1, m-1
    powers = ["U", "U²", "U^(2^(m−1))"]
    ypsi = 360
    b: list[str] = []
    for y in yc:
        b.append(text(80, y + 6, "|0⟩", 18, anchor="end"))
        b.append(wire(90, 830, y))
    b.append(text(160, 205, "⋮", 26, MUTED))
    b.append(text(80, ypsi + 6, "|ψ⟩", 18, anchor="end"))
    b.append(wire(90, 600, ypsi)); b.append(slash(115, ypsi, "n"))
    for y in yc:
        b.append(gate(160, y, "H"))
    xs = [260, 360, 480]
    for x, y, p in zip(xs, yc, powers):
        b.append(vwire(x, y, ypsi - 22))
        b.append(control(x, y))
        w = 70 if len(p) < 4 else 110
        b.append(multigate(x, ypsi, ypsi, p, width=w, fill="#fde3d3", stroke=ACCENT2, size=17))
    b.append(text(420, 205, "⋯", 22, MUTED))
    b.append(line(560, 30, 560, 300, MUTED, 1, dash="4 4"))
    b.append(text(560, 22, t["state"], 15, ACCENT))
    b.append(multigate(660, yc[0], yc[-1], "QFT⁻¹", width=90, size=20))
    for y in yc:
        b.append(meter(780, y))
    b.append(text(840, 205, t["out"], 16, ACCENT, anchor="start"))
    b.append(text(620, ypsi + 6, t["psi"], 15, MUTED, anchor="start"))
    b.append(text(W / 2, H - 25, t["eig"], 15, MUTED))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"phase-estimation-circuit.{lang}.svg", build(lang)))
