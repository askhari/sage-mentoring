"""Hybrid loop of a variational quantum algorithm -> variational-loop.<lang>.svg

Once: build the parameterised ansatz U(θ) and the observable H, transpile once to an ISA
circuit. Every iteration: the classical optimizer proposes θ, the Estimator returns
C(θ) = ⟨ψ(θ)|H|ψ(θ)⟩, the optimizer updates θ, until convergence.
"""
from __future__ import annotations

from svgkit import ACCENT, ACCENT2, ACCENT3, MUTED, block, line, path, svg, text, write

LABELS = {
    "es": {
        "once": "una vez",
        "each": "en cada iteración",
        "b0": ["Ansatz U(θ) + observable H", "(SparsePauliOp)", "→ transpilar a ISA"],
        "opt": ["Optimizador clásico", "(COBYLA, SPSA, …)", "propone θ nuevo"],
        "qpu": ["Estimator (QPU o simulador)", "prepara |ψ(θ)⟩ = U(θ)|0⟩", "y estima ⟨ψ(θ)|H|ψ(θ)⟩"],
        "theta": "θ",
        "cost": "C(θ)",
        "out": ["θ* y C(θ*) ≈ energía", "mínima (cota superior)"],
        "conv": "¿converge?",
    },
}

W, H = 1100, 560


def arc(d: str, color: str, marker: str) -> str:
    return path(d, color, width=2.2).replace("/>", f" marker-end='url(#arrow-{marker})'/>")


def build(lang: str) -> str:
    t = LABELS[lang]
    b: list[str] = []
    x, w = 330, 280
    # once block on top
    b.append(text(x + w + 20, 85, t["once"], 14, ACCENT3, anchor="start", weight="bold"))
    b.append(block(x, 30, w, 100, t["b0"], fill="#e3f2e8", stroke=ACCENT3, size=14))
    b.append(line(x + w / 2, 132, x + w / 2, 208, ACCENT3, 2, arrow="a3"))
    # loop
    b.append(text(x + w / 2, 545, t["each"], 14, ACCENT2, weight="bold"))
    b.append(block(x, 210, w, 100, t["qpu"], fill="#fde3d3", stroke=ACCENT2, size=14))
    b.append(block(x, 400, w, 100, t["opt"], fill="#dbe9f6", stroke=ACCENT, size=14))
    b.append(arc(f"M{x + w},260 C{x + w + 110},260 {x + w + 110},450 {x + w + 2},450", ACCENT, "a1"))
    b.append(text(x + w + 100, 360, t["cost"], 16, ACCENT, anchor="start", italic=True))
    b.append(arc(f"M{x},450 C{x - 110},450 {x - 110},260 {x - 2},260", ACCENT2, "a2"))
    b.append(text(x - 100, 360, t["theta"], 18, ACCENT2, anchor="end", italic=True))
    # output
    b.append(line(x + w / 2 + 60, 502, x + w + 190, 530, MUTED, 1.6, dash="5 4", arrow="muted"))
    b.append(text(x + w + 70, 500, t["conv"], 13, MUTED, anchor="start"))
    b.append(block(x + w + 195, 490, 230, 64, t["out"], fill="#f2f2f2", size=13))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"variational-loop.{lang}.svg", build(lang)))
