"""Complex plane with the unit circle and Euler's formula -> complex-plane-unit-circle.<lang>.svg

Point z = a + bi with modulus r and argument φ; the unit circle with e^{iφ} = cos φ + i sin φ
on it (same angle, length 1); the four points 1, i, -1, -i. Geometry is computed, not drawn by hand.
"""
from __future__ import annotations

import math

from svgkit import ACCENT, ACCENT2, INK, MUTED, circle, line, path, svg, text, write

LABELS = {
    "es": {
        "re": "Re (parte real)",
        "im": "Im (parte imaginaria)",
        "z": "z = a + bi",
        "r": "r = |z|",
        "phi": "φ",
        "euler": "e^(iφ) = cos φ + i sen φ",
        "unit": "circunferencia unidad (|z| = 1)",
        "a": "a",
        "b": "b",
    },
}

W, H = 640, 500
CX, CY, U = 300, 290, 150      # origin and pixels per unit
PHI = math.radians(35)
R = 1.6                         # modulus of z


def to_px(x: float, y: float) -> tuple[float, float]:
    return CX + x * U, CY - y * U


def build(lang: str) -> str:
    t = LABELS[lang]
    b: list[str] = []
    # axes
    b.append(line(40, CY, W - 30, CY, arrow="ink"))
    b.append(line(CX, H - 20, CX, 30, arrow="ink"))
    b.append(text(W - 30, CY + 26, t["re"], 14, anchor="end"))
    b.append(text(CX + 10, 40, t["im"], 14, anchor="start"))
    # unit circle
    b.append(circle(CX, CY, U, stroke=MUTED, dash="5,4"))
    ux, uy = to_px(math.cos(math.radians(240)), math.sin(math.radians(240)))
    b.append(text(ux - 20, uy + 30, t["unit"], 13, MUTED, anchor="end"))
    # 1, i, -1, -i
    for (x, y, lab, dx, dy) in ((1, 0, "1", 12, 20), (0, 1, "i", 12, -8), (-1, 0, "−1", -14, 20), (0, -1, "−i", 14, 18)):
        px, py = to_px(x, y)
        b.append(circle(px, py, 4, stroke=INK, fill=INK))
        b.append(text(px + dx, py + dy, lab, 16, anchor="middle", italic=True))
    # z = a + bi and its projections
    a, bb = R * math.cos(PHI), R * math.sin(PHI)
    zx, zy = to_px(a, bb)
    b.append(line(zx, zy, zx, CY, MUTED, 1.2, dash="4,4"))
    b.append(line(zx, zy, CX, zy, MUTED, 1.2, dash="4,4"))
    b.append(text(zx, CY + 22, t["a"], 16, MUTED, italic=True))
    b.append(text(CX - 14, zy + 5, t["b"], 16, MUTED, italic=True))
    b.append(line(CX, CY, zx, zy, ACCENT, 2.5, arrow="a1"))
    b.append(circle(zx, zy, 4.5, stroke=ACCENT, fill=ACCENT))
    b.append(text(zx + 10, zy - 10, t["z"], 17, ACCENT, anchor="start", weight="bold"))
    mx, my = to_px(0.62 * R * math.cos(PHI), 0.62 * R * math.sin(PHI))
    b.append(text(mx - 8, my - 12, t["r"], 15, ACCENT, anchor="end"))
    # e^{iφ} on the unit circle
    ex, ey = to_px(math.cos(PHI), math.sin(PHI))
    b.append(circle(ex, ey, 5, stroke=ACCENT2, fill=ACCENT2))
    b.append(text(ex + 14, ey + 22, t["euler"], 15, ACCENT2, anchor="start"))
    # angle arc
    ar = 0.32 * U
    x1, y1 = CX + ar, CY
    x2, y2 = CX + ar * math.cos(PHI), CY - ar * math.sin(PHI)
    b.append(path(f"M{x1:.1f},{y1:.1f} A{ar:.1f},{ar:.1f} 0 0 0 {x2:.1f},{y2:.1f}", INK, width=1.3))
    hx, hy = CX + (ar + 14) * math.cos(PHI / 2), CY - (ar + 14) * math.sin(PHI / 2)
    b.append(text(hx, hy + 5, t["phi"], 17, italic=True))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"complex-plane-unit-circle.{lang}.svg", build(lang)))
