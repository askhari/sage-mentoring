"""Shor's algorithm as a pipeline -> shor-pipeline.<lang>.svg

Classical: pick a, check gcd -> Quantum: phase estimation of M_a on |1⟩ -> Classical:
continued fractions + lcm -> r -> Classical: if r even, gcd(a^{r/2} − 1, N). Failure loops back.
"""
from __future__ import annotations

from svgkit import ACCENT, ACCENT2, ACCENT3, MUTED, block, line, path, svg, text, write

LABELS = {
    "es": {
        "classical": "clásico",
        "quantum": "cuántico",
        "b1": ["Elegir a al azar", "en {2, …, N − 1}", "¿mcd(a, N) > 1?"],
        "b2": ["Estimación de fase", "de M_a: |x⟩ → |ax mod N⟩", "sobre |1⟩ → y/2ᵐ ≈ k/r"],
        "b3": ["Fracciones continuas", "→ k/r irreducible;", "mcm de varias → r"],
        "b4": ["Si r es par:", "d = mcd(a^(r/2) − 1, N)", "¿1 < d < N?"],
        "found": "factor de N",
        "retry": "si falla (r impar o d trivial): otro a; éxito ≥ 1/2 por intento",
        "yes": "sí",
    },
}

W, H = 1180, 360


def build(lang: str) -> str:
    t = LABELS[lang]
    bw, bh, y = 230, 120, 90
    xs = [30, 320, 610, 900]
    kinds = [("classical", "#e3f2e8", ACCENT3), ("quantum", "#fde3d3", ACCENT2),
             ("classical", "#e3f2e8", ACCENT3), ("classical", "#e3f2e8", ACCENT3)]
    b: list[str] = []
    for x, key, (kind, fill, stroke) in zip(xs, ["b1", "b2", "b3", "b4"], kinds):
        b.append(block(x, y, bw, bh, t[key], fill=fill, stroke=stroke, size=15, title=t[kind], title_color=stroke))
    for x in xs[:-1]:
        b.append(line(x + bw + 4, y + bh / 2, x + 290 - 4, y + bh / 2, ACCENT, 2.2, arrow="a1"))
    # found factor (from b1 and b4)
    b.append(line(xs[0] + bw / 2, y - 4, xs[0] + bw / 2, 40, ACCENT, 1.8, arrow="a1"))
    b.append(text(xs[0] + bw / 2 + 8, 62, t["yes"], 13, MUTED, anchor="start"))
    b.append(text(xs[0] + bw / 2, 30, t["found"], 15, ACCENT, weight="bold"))
    b.append(line(xs[3] + bw / 2, y - 4, xs[3] + bw / 2, 40, ACCENT, 1.8, arrow="a1"))
    b.append(text(xs[3] + bw / 2 + 8, 62, t["yes"], 13, MUTED, anchor="start"))
    b.append(text(xs[3] + bw / 2, 30, t["found"], 15, ACCENT, weight="bold"))
    # retry loop from b4 back to b1
    yb = y + bh + 60
    b.append(path(f"M{xs[3] + bw / 2},{y + bh + 4} L{xs[3] + bw / 2},{yb} L{xs[0] + bw / 2},{yb} "
                  f"L{xs[0] + bw / 2},{y + bh + 10}", MUTED, width=1.6))
    b.append(line(xs[0] + bw / 2, y + bh + 20, xs[0] + bw / 2, y + bh + 6, MUTED, 1.6, arrow="muted"))
    b.append(text(W / 2, yb + 26, t["retry"], 14, MUTED))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"shor-pipeline.{lang}.svg", build(lang)))
