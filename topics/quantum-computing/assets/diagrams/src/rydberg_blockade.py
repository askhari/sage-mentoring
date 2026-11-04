"""Rydberg blockade and the three-pulse CZ (lasers couple |0⟩ to |r⟩, as in Henriet et al.) -> rydberg-blockade.<lang>.svg

Schematic (no measured numbers): two atoms in optical tweezers (~1 µm spots, a few µm
apart) with levels |0⟩, |1⟩ (hyperfine) and |r⟩ (Rydberg). Panel A: if the control is in
|r⟩, the neighbour's Rydberg level is shifted and cannot be reached. Panel B: CZ as
π (control), 2π (target), π (control). After Henriet et al. 2020, pp. 5, 9-10.
"""
from __future__ import annotations

from svgkit import ACCENT, ACCENT2, ACCENT3, INK, MUTED, circle, line, rect, svg, text, write

LABELS = {
    "es": {
        "a": "A. Bloqueo de Rydberg",
        "b": "B. Puerta CZ en tres pulsos",
        "ctrl": "control",
        "tgt": "objetivo",
        "tweezer": "pinza óptica (~1 µm)",
        "shift": "nivel desplazado: el láser ya no es resonante",
        "dist": "unos pocos µm",
        "p1": "π",
        "p2": "2π",
        "p3": "π",
        "steps": ["El láser acopla |0⟩ con |r⟩ (convención de Henriet et al.).",
                  "1. π en el control: |0⟩ → |r⟩",
                  "2. 2π en el objetivo: vuelta completa |0⟩ → |r⟩ → |0⟩ (fase −1),",
                  "    salvo si el control está en |r⟩: bloqueado, no hace nada",
                  "3. π en el control: |r⟩ → |0⟩"],
        "result": "|11⟩ no cambia; |00⟩, |01⟩ y |10⟩ toman fase −1: diag(−1, −1, −1, 1) = CZ salvo una fase global",
        "note": "Esquema según Henriet et al. 2020 (Pasqal). El estado de Rydberg tiene un momento dipolar ~1000 veces mayor que el fundamental.",
    },
}

W, H = 1180, 460


def atom_levels(b, x, y, label, rshift=0, excited=False, blocked=False):
    # levels: |0>, |1>, |r>
    ly = {"1": y + 170, "0": y + 140, "r": y + 20}
    for k, yy in ly.items():
        w = 70
        col = INK
        b.append(line(x - w / 2, yy, x + w / 2, yy, col, 2.2))
        b.append(text(x + w / 2 + 8, yy + 5, f"|{k}⟩", 14, anchor="start"))
    if rshift:
        b.append(line(x - 35, ly["r"] - rshift, x + 35, ly["r"] - rshift, ACCENT2, 2.2))
        b.append(f"<path d='M{x-35},{ly['r']} L{x+35},{ly['r']}' stroke='{MUTED}' stroke-dasharray='4 4' stroke-width='1.2'/>")
    if excited:
        b.append(circle(x, ly["r"], 7, ACCENT, ACCENT))
    else:
        b.append(circle(x, ly["0"], 7, ACCENT, ACCENT))
    b.append(text(x, y + 205, label, 14, MUTED))
    return ly


def build(lang: str) -> str:
    t = LABELS[lang]
    b: list[str] = []
    # Panel A
    b.append(text(260, 36, t["a"], 16, INK, weight="bold"))
    for x in (130, 380):
        b.append(f"<ellipse cx='{x}' cy='170' rx='16' ry='60' fill='#fde3d3' fill-opacity='0.6' stroke='none'/>")
    b.append(text(130, 250, t["tweezer"], 11, MUTED))
    ly = atom_levels(b, 130, 120, t["ctrl"], excited=True)
    ly2 = atom_levels(b, 380, 120, t["tgt"], rshift=34)
    # laser on target, not resonant
    b.append(line(380, ly2["0"] - 6, 380, ly2["r"] + 6, ACCENT2, 1.8, dash="5 4", arrow="a2"))
    b.append(text(380, ly2["r"] - 46, t["shift"], 12, ACCENT2))
    # interaction
    b.append(line(150, ly["r"], 340, ly["r"] - 34, ACCENT, 1.4, dash="2 3"))
    b.append(line(130, 360, 380, 360, MUTED, 1.2, arrow="muted"))
    b.append(line(380, 360, 130, 360, MUTED, 1.2, arrow="muted"))
    b.append(text(255, 378, t["dist"], 12, MUTED))
    # Panel B: pulse sequence
    x0 = 620
    b.append(text(x0 + 260, 36, t["b"], 16, INK, weight="bold"))
    rows = [(110, t["ctrl"]), (190, t["tgt"])]
    for y, lab in rows:
        b.append(text(x0 - 10, y + 5, lab, 14, MUTED, anchor="end"))
        b.append(line(x0, y, x0 + 480, y, INK, 1.4))
    pulses = [(x0 + 60, 110, t["p1"], 50), (x0 + 200, 190, t["p2"], 100), (x0 + 380, 110, t["p3"], 50)]
    for x, y, lab, w in pulses:
        b.append(rect(x, y - 26, w, 26, ACCENT, "#dbe9f6", 1.6, rx=3))
        b.append(text(x + w / 2, y - 8, lab, 15, ACCENT, weight="bold"))
    for i, s in enumerate(t["steps"]):
        b.append(text(x0 - 40, 260 + i * 26, s, 13, INK, anchor="start"))
    b.append(text(x0 - 40, 400, t["result"], 13, ACCENT3, anchor="start"))
    b.append(text(W / 2, H - 14, t["note"], 12, MUTED))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"rydberg-blockade.{lang}.svg", build(lang)))
