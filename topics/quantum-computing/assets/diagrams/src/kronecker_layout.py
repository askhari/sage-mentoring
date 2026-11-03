"""Block layout of the Kronecker (tensor) product -> kronecker-layout.<lang>.svg

Left: A ⊗ B for 2×2 matrices is the 4×4 matrix of blocks a_ij·B.
Right: α ⊗ β for 2-vectors is the 4-vector of blocks α_i·β, i.e. entries α_i β_j in
lexicographic order (00, 01, 10, 11), which is how |a⟩⊗|b⟩ = |ab⟩ is laid out.
"""
from __future__ import annotations

from svgkit import ACCENT, ACCENT2, ACCENT3, INK, MUTED, rect, svg, text, write

LABELS = {
    "es": {
        "mat_title": "Matrices: A ⊗ B",
        "vec_title": "Vectores: α ⊗ β",
        "mat_note": "cada entrada aᵢⱼ de A multiplica a toda la matriz B",
        "vec_note": "orden de las entradas: 00, 01, 10, 11",
    },
}

W, H = 860, 520
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
COLORS = ["#dbe9f6", "#fde3d3", "#dcefe2", "#efe3f5"]
EDGE = [ACCENT, ACCENT2, ACCENT3, "#7b4fa0"]


def build(lang: str) -> str:
    t = LABELS[lang]
    b: list[str] = []
    # --- matrix part
    b.append(text(220, 40, t["mat_title"], 20, weight="bold"))
    x0, y0, cell = 40, 80, 90
    for i in range(2):
        for j in range(2):
            k = 2 * i + j
            bx, by = x0 + j * 2 * cell, y0 + i * 2 * cell
            b.append(rect(bx + 3, by + 3, 2 * cell - 6, 2 * cell - 6, EDGE[k], COLORS[k], 2.5, rx=6))
            for r in range(2):
                for c in range(2):
                    cx, cy = bx + c * cell + cell / 2, by + r * cell + cell / 2 + 6
                    b.append(text(cx, cy, f"a{i+1}{j+1}·b{r+1}{c+1}".translate(SUB), 15, INK))
    b.append(text(220, y0 + 4 * cell + 34, t["mat_note"], 14, MUTED))
    # block labels a_ij B
    # --- vector part
    vx = 560
    b.append(text(vx + 90, 40, t["vec_title"], 20, weight="bold"))
    vcell_w, vcell_h = 120, 70
    labels = ["00", "01", "10", "11"]
    for i in range(2):
        by = y0 + i * 2 * vcell_h
        b.append(rect(vx + 30, by + 3, vcell_w, 2 * vcell_h - 6, EDGE[i * 3], COLORS[i * 3], 2.5, rx=6))
        for j in range(2):
            cy = by + j * vcell_h + vcell_h / 2 + 6
            b.append(text(vx + 30 + vcell_w / 2, cy, f"α{i+1}·β{j+1}".translate(SUB), 16, INK))
            b.append(text(vx + 30 + vcell_w + 30, cy, f"|{labels[2*i+j]}⟩", 16, MUTED))
        b.append(text(vx + 10, by + vcell_h + 6, f"α{i+1}·β".translate(SUB), 15, EDGE[i * 3], anchor="end", italic=True))
    b.append(text(vx + 90, y0 + 4 * vcell_h + 34, t["vec_note"], 14, MUTED))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"kronecker-layout.{lang}.svg", build(lang)))
