"""15-to-1 magic-state distillation -> distillation-15-to-1.<lang>.svg

15 noisy T states with error ε → Clifford-only circuit of the 15-qubit code + stabilizer
measurements → keep on trivial syndrome → 1 state with error ≈ 35ε³ (success ≈ 1 − 15ε).
Two rounds from ε = 1 %: 3.5e-5, then ≈ 1.5e-12. After Bravyi & Kitaev 2005 and Fowler 2012.
"""
from __future__ import annotations

from svgkit import ACCENT, ACCENT2, ACCENT3, INK, MUTED, block, circle, line, svg, text, write

LABELS = {
    "es": {
        "in": "15 estados T ruidosos, error ε",
        "box": ["código de 15 qubits:", "solo puertas Clifford", "y medidas de estabilizadores"],
        "keep": "síndrome trivial → se conserva",
        "drop": "otro síndrome → se descarta",
        "out": "1 estado T, error ≈ 35ε³",
        "succ": "éxito ≈ 1 − 15ε",
        "r1": "ronda 1",
        "r2": "ronda 2 (15 salidas de la ronda 1)",
        "chain": "ε = 1 %  →  3,5·10⁻⁵  →  ≈ 1,5·10⁻¹²",
        "note": "Según Bravyi y Kitaev (2005; su «tipo H» es el estado T actual) y Fowler et al. (2012). Cada ronda consume 15 estados por cada uno que sale.",
    },
}

W, H = 1120, 430


def sci(v):
    m, e = f"{v:.1e}".split("e")
    sup = str(int(e)).replace("-", "⁻").translate(str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹"))
    return f"{m.replace('.', ',')}·10{sup}"


def build(lang: str) -> str:
    t = LABELS[lang]
    b: list[str] = []
    # 15 inputs
    for i in range(15):
        y = 60 + i * 18
        b.append(circle(70, y, 6, ACCENT2, "#fde3d3", 1.6))
        b.append(line(78, y, 300, 180, ACCENT2, 0.8))
    b.append(text(20, 350, t["in"], 13, ACCENT2, anchor="start"))
    b.append(text(70, 40, t["r1"], 14, INK, weight="bold"))
    b.append(block(300, 120, 260, 120, t["box"], fill="#dbe9f6", stroke=ACCENT, size=14))
    b.append(line(562, 160, 700, 120, ACCENT3, 2, arrow="a3"))
    b.append(text(640, 110, t["keep"], 12, ACCENT3))
    b.append(line(562, 210, 700, 260, MUTED, 1.6, dash="4 3", arrow="muted"))
    b.append(text(640, 285, t["drop"], 12, MUTED))
    b.append(circle(720, 120, 9, ACCENT3, "#e3f2e8", 2))
    b.append(text(740, 116, t["out"], 14, ACCENT3, anchor="start", weight="bold"))
    b.append(text(740, 136, t["succ"], 12, MUTED, anchor="start"))
    b.append(text(740, 190, t["r2"], 13, INK, anchor="start"))
    b.append(text(740, 214, t["chain"], 14, ACCENT, anchor="start", weight="bold"))
    b.append(text(W / 2, H - 14, t["note"], 12, MUTED))
    return svg(W, H, b)


if __name__ == "__main__":
    e1 = 35 * 0.01 ** 3
    e2 = 35 * e1 ** 3
    assert sci(e1) == "3,5·10⁻⁵" and sci(e2) == "1,5·10⁻¹²", (sci(e1), sci(e2))
    for lang in LABELS:
        print(write(f"distillation-15-to-1.{lang}.svg", build(lang)))
