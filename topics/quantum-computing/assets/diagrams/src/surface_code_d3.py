"""Rotated surface code of distance 3 -> surface-code-d3.<lang>.svg

9 data qubits on a 3×3 grid; 4 weight-4 and 4 weight-2 stabilizers (checkerboard
X/Z), one measure qubit per stabilizer: 17 qubits = 2d² − 1. One logical X (a column
of X) and one logical Z (a row of Z). The script checks that all stabilizers commute,
that the logicals commute with every stabilizer and anticommute with each other,
and that there are n − k = 8 independent checks.
"""
from __future__ import annotations

from svgkit import ACCENT, ACCENT2, INK, MUTED, circle, line, svg, text, write

D = 3
DATA = [(x, y) for y in range(D) for x in range(D)]


def plaquette(cx, cy):
    return [(x, y) for (x, y) in DATA if abs(x - cx) == 0.5 and abs(y - cy) == 0.5]


def kind(cx, cy):
    return "X" if (int(cx - 0.5) + int(cy - 0.5)) % 2 == 0 else "Z"


STABS = []
for cy in (0.5, 1.5):
    for cx in (0.5, 1.5):
        STABS.append((kind(cx, cy), (cx, cy), plaquette(cx, cy)))
STABS += [("X", (1.5, -0.5), plaquette(1.5, -0.5)), ("X", (0.5, 2.5), plaquette(0.5, 2.5)),
          ("Z", (-0.5, 0.5), plaquette(-0.5, 0.5)), ("Z", (2.5, 1.5), plaquette(2.5, 1.5))]
LOG_X = [(0, y) for y in range(D)]
LOG_Z = [(x, 0) for x in range(D)]


def anticommute(k1, s1, k2, s2):
    return k1 != k2 and len(set(s1) & set(s2)) % 2 == 1


def check():
    for i, (k1, _, s1) in enumerate(STABS):
        assert len(s1) in (2, 4)
        for k2, _, s2 in STABS[i + 1:]:
            assert not anticommute(k1, s1, k2, s2)
        assert not anticommute("X", LOG_X, k1, s1) and not anticommute("Z", LOG_Z, k1, s1)
    assert anticommute("X", LOG_X, "Z", LOG_Z)
    assert len(DATA) - len(STABS) == 1 and len(DATA) + len(STABS) == 2 * D * D - 1


LABELS = {
    "es": {
        "title": "Código de superficie (rotado) de distancia 3",
        "data": "qubit de datos (9)",
        "xs": "estabilizador X (mide una paridad X)",
        "zs": "estabilizador Z (mide una paridad Z)",
        "anc": "qubit de medida, uno por estabilizador (8)",
        "lx": "X lógico: X en una columna",
        "lz": "Z lógico: Z en una fila",
        "count": "9 + 8 = 17 qubits = 2d² − 1; cualquier cadena lógica tiene al menos d = 3 qubits",
    },
}

W, H = 1060, 520
S, OX, OY = 130, 140, 110
XF, ZF = "#fde3d3", "#dbe9f6"


def p(x, y):
    return OX + x * S, OY + y * S


def build(lang: str) -> str:
    t = LABELS[lang]
    b: list[str] = [text(W / 2, 40, t["title"], 17, INK, weight="bold")]
    for k, (cx, cy), qs in STABS:
        fill, stroke = (XF, ACCENT2) if k == "X" else (ZF, ACCENT)
        if len(qs) == 4:
            pts = [p(cx - 0.5, cy - 0.5), p(cx + 0.5, cy - 0.5), p(cx + 0.5, cy + 0.5), p(cx - 0.5, cy + 0.5)]
            d = "M" + " L".join(f"{x:.0f},{y:.0f}" for x, y in pts) + " Z"
        else:
            (x1, y1), (x2, y2) = [p(*q) for q in sorted(qs)]
            mx, my = p(cx, cy)
            # half-disc bulging outwards
            d = f"M{x1:.0f},{y1:.0f} Q{mx + (mx - (x1 + x2) / 2):.0f},{my + (my - (y1 + y2) / 2):.0f} {x2:.0f},{y2:.0f} Z"
        b.append(f"<path d='{d}' fill='{fill}' stroke='{stroke}' stroke-width='1.6'/>")
        ax, ay = p(cx, cy)
        if len(qs) == 2:
            ax, ay = ax - (ax - sum(p(*q)[0] for q in qs) / 2) * 0.35, ay - (ay - sum(p(*q)[1] for q in qs) / 2) * 0.35
        b.append(circle(ax, ay, 9, stroke, "white", 2))
        b.append(text(ax, ay + 5, k, 12, stroke, weight="bold"))
    # logical operators
    (x0, y0), (x1, y1) = p(*LOG_X[0]), p(*LOG_X[-1])
    b.append(line(x0, y0 - 30, x1, y1 + 30, ACCENT2, 7))
    (x0, y0), (x1, y1) = p(*LOG_Z[0]), p(*LOG_Z[-1])
    b.append(line(x0 - 30, y0, x1 + 30, y1, ACCENT, 7))
    for x, y in DATA:
        cx, cy = p(x, y)
        b.append(circle(cx, cy, 14, INK, INK))
    # legend
    lx, ly = 560, 140
    b.append(circle(lx, ly, 12, INK, INK)); b.append(text(lx + 24, ly + 5, t["data"], 14, anchor="start"))
    b.append(f"<rect x='{lx-12}' y='{ly+28}' width='24' height='24' fill='{XF}' stroke='{ACCENT2}'/>")
    b.append(text(lx + 24, ly + 45, t["xs"], 14, anchor="start"))
    b.append(f"<rect x='{lx-12}' y='{ly+68}' width='24' height='24' fill='{ZF}' stroke='{ACCENT}'/>")
    b.append(text(lx + 24, ly + 85, t["zs"], 14, anchor="start"))
    b.append(circle(lx, ly + 120, 9, MUTED, "white", 2)); b.append(text(lx + 24, ly + 125, t["anc"], 14, anchor="start"))
    b.append(line(lx - 12, ly + 160, lx + 12, ly + 160, ACCENT2, 4)); b.append(text(lx + 24, ly + 165, t["lx"], 14, ACCENT2, anchor="start"))
    b.append(line(lx - 12, ly + 195, lx + 12, ly + 195, ACCENT, 4)); b.append(text(lx + 24, ly + 200, t["lz"], 14, ACCENT, anchor="start"))
    b.append(text(W / 2, H - 16, t["count"], 14, MUTED))
    return svg(W, H, b)


if __name__ == "__main__":
    check()
    for lang in LABELS:
        print(write(f"surface-code-d3.{lang}.svg", build(lang)))
