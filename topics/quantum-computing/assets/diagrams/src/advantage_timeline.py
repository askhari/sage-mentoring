"""Quantum advantage claims vs classical responses -> advantage-timeline.<lang>.svg

Two lanes. Events and figures as cited in quantum-advantage-experiments.md:
arute-2019, zhong-2020, pan-2022 and eisert-2025 (the last ones without exact dates in
our sources, so they are grouped under "recogido por Eisert y Preskill").
Figures marked * are the authors' own extrapolations or estimates.
"""
from __future__ import annotations

from svgkit import ACCENT, ACCENT2, INK, MUTED, block, line, svg, text, write

LABELS = {
    "es": {
        "q": "Reclamaciones cuánticas",
        "c": "Respuestas clásicas",
        "years": ["2019", "2020", "2021", "2022", "más tarde"],
        "e1": ["Sycamore (Google)", "53 qubits, 20 ciclos", "200 s frente a 10 000 años*"],
        "e2": ["Jiuzhang (USTC)", "muestreo de bosones, 76 clics", "200 s frente a 2500 millones de años*"],
        "e3": ["Google: RCS con 103 qubits", "y 40 capas de puertas de 2 qubits"],
        "e4": ["IBM: Ising con patada,", "127 qubits («utilidad»)"],
        "r1": ["IBM: guardar el estado", "en RAM y disco de Summit", "(sin cifra en Pan et al.)"],
        "r2": ["Pan, Chen y Zhang", "~15 h en 512 GPU; fidelidad", "estimada 0,0037 frente a 0,002"],
        "r4": ["reproducido pronto con redes", "tensoriales y dinámica de Pauli"],
        "group": "recogido por Eisert y Preskill (preprint 2025-26), sin fecha exacta",
        "note": "* extrapolación o estimación de los propios autores. La frontera se mueve: cada reclamación invita a mejores algoritmos clásicos.",
    },
}

W, H = 1220, 500


def build(lang: str) -> str:
    t = LABELS[lang]
    b: list[str] = []
    xs = [150, 410, 570, 720, 980]
    ay = 285
    b.append(line(60, ay, 1180, ay, INK, 2, arrow="ink"))
    for x, y in zip(xs, t["years"]):
        b.append(line(x, ay - 6, x, ay + 6, INK, 2))
        b.append(text(x, ay + 26, y, 14, INK, weight="bold"))
    b.append(text(70, 60, t["q"], 15, ACCENT, anchor="start", weight="bold"))
    b.append(text(70, 445, t["c"], 15, ACCENT2, anchor="start", weight="bold"))
    bw, bh = 230, 80
    # quantum lane
    for x, key in ((xs[0], "e1"), (xs[1], "e2")):
        b.append(block(x - bw / 2, 100, bw, bh, t[key], fill="#dbe9f6", stroke=ACCENT, size=13))
        b.append(line(x, 180, x, ay - 8, ACCENT, 1.4, dash="4 3"))
    b.append(block(xs[4] - 250, 80, 230, 64, t["e3"], fill="#dbe9f6", stroke=ACCENT, size=13))
    b.append(block(xs[4] + 10, 80, 200, 64, t["e4"], fill="#dbe9f6", stroke=ACCENT, size=13))
    b.append(line(xs[4], 150, xs[4], ay - 8, ACCENT, 1.4, dash="4 3"))
    # classical lane
    b.append(block(xs[0] - bw / 2, 340, bw, bh, t["r1"], fill="#fde3d3", stroke=ACCENT2, size=13))
    b.append(line(xs[0], ay + 34, xs[0], 340, ACCENT2, 1.4, dash="4 3"))
    b.append(block(xs[3] - bw / 2, 340, bw, bh, t["r2"], fill="#fde3d3", stroke=ACCENT2, size=13))
    b.append(line(xs[3], ay + 34, xs[3], 340, ACCENT2, 1.4, dash="4 3"))
    b.append(line(xs[0] + 100, 180, xs[3] - 20, 338, ACCENT2, 1.6, arrow="a2"))
    b.append(block(xs[4] + 10, 340, 200, 64, t["r4"], fill="#fde3d3", stroke=ACCENT2, size=13))
    b.append(line(xs[4] + 110, 146, xs[4] + 110, 338, ACCENT2, 1.6, arrow="a2"))
    b.append(text(xs[4] + 90, 398, t["group"], 12, MUTED))
    b.append(text(W / 2, H - 10, t["note"], 13, MUTED))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"advantage-timeline.{lang}.svg", build(lang)))
