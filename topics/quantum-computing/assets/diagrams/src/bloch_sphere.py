"""Bloch sphere with the six cardinal states and a general state -> bloch-sphere.<lang>.svg

Orthographic projection of the unit sphere (view azimuth/elevation below). Each point is
r = (sin θ cos φ, sin θ sin φ, cos θ) for the state cos(θ/2)|0⟩ + e^{iφ} sin(θ/2)|1⟩, so the
labels and the general state are placed by computation, not by hand.
"""
from __future__ import annotations

import math

from svgkit import ACCENT, ACCENT2, INK, MUTED, circle, line, path, svg, text, write

LABELS = {
    "es": {
        "general": "|ψ⟩ = cos(θ/2)|0⟩ + e^(iφ) sen(θ/2)|1⟩",
        "theta": "θ",
        "phi": "φ",
    },
}

W, H = 640, 600
CX, CY, R = 300, 300, 200
AZ, EL = math.radians(30), math.radians(18)     # view: rotate about z, then tilt
THETA, PHI = math.radians(55), math.radians(60)  # example general state


def proj(x: float, y: float, z: float) -> tuple[float, float, float]:
    """3D unit-sphere point -> (screen x, screen y, depth). Depth > 0 is towards the viewer."""
    # rotate about z by -AZ so the x axis points left-down towards the viewer
    xr = x * math.cos(AZ) - y * math.sin(AZ)
    yr = x * math.sin(AZ) + y * math.cos(AZ)
    # tilt about the screen-horizontal axis by EL
    depth = xr * math.cos(EL) - z * math.sin(EL) * 0 + 0
    sx = yr
    sy = z * math.cos(EL) - xr * math.sin(EL)
    depth = xr * math.cos(EL) + z * math.sin(EL)
    return CX + R * sx, CY - R * sy, depth


def bloch(theta: float, phi: float) -> tuple[float, float, float]:
    return math.sin(theta) * math.cos(phi), math.sin(theta) * math.sin(phi), math.cos(theta)


def curve(points, color, width=1.4, dash_back=True) -> list[str]:
    """Polyline split into front (solid) and back (dashed) parts."""
    out = []
    for (a, b) in zip(points, points[1:]):
        x1, y1, d1 = a
        x2, y2, d2 = b
        back = (d1 + d2) / 2 < 0
        out.append(line(x1, y1, x2, y2, MUTED if back else color, width, dash="4,4" if back and dash_back else None))
    return out


def build(lang: str) -> str:
    t = LABELS[lang]
    b: list[str] = [circle(CX, CY, R, stroke=INK, width=1.8)]
    n = 120
    equator = [proj(math.cos(2 * math.pi * k / n), math.sin(2 * math.pi * k / n), 0) for k in range(n + 1)]
    b += curve(equator, INK)
    # axes
    for (v, lab, dx, dy) in (((1, 0, 0), "x", -18, 14), ((0, 1, 0), "y", 14, 6), ((0, 0, 1), "z", 10, -6)):
        x2, y2, _ = proj(*[1.25 * c for c in v])
        b.append(line(CX, CY, x2, y2, MUTED, 1.2, arrow="muted"))
        b.append(text(x2 + dx, y2 + dy, lab, 16, MUTED, italic=True))
    # cardinal states
    states = [
        ("|0⟩", (0, 0), 14, -12), ("|1⟩", (math.pi, 0), 14, 24),
        ("|+⟩", (math.pi / 2, 0), -40, 6), ("|−⟩", (math.pi / 2, math.pi), 20, -10),
        ("|+i⟩", (math.pi / 2, math.pi / 2), 12, 22), ("|−i⟩", (math.pi / 2, 3 * math.pi / 2), -42, -8),
    ]
    for lab, (th, ph), dx, dy in states:
        x, y, d = proj(*bloch(th, ph))
        col = INK if d >= -1e-9 else MUTED
        b.append(circle(x, y, 5, stroke=col, fill=col if d >= -1e-9 else "white"))
        b.append(text(x + dx, y + dy, lab, 16, col, weight="bold"))
    # general state
    gx, gy, _ = proj(*bloch(THETA, PHI))
    fx, fy, _ = proj(*bloch(math.pi / 2, PHI))   # foot on the equator
    b.append(line(CX, CY, fx, fy, ACCENT2, 1.2, dash="5,4"))
    b.append(line(gx, gy, fx, fy, ACCENT2, 1.2, dash="5,4"))
    b.append(line(CX, CY, gx, gy, ACCENT, 3, arrow="a1"))
    b.append(text(gx + 12, gy - 8, "|ψ⟩", 18, ACCENT, anchor="start", weight="bold"))
    # θ arc (from z axis to the state) and φ arc (on the equator, from x to the foot)
    th_arc = [proj(*[0.35 * c for c in bloch(THETA * k / 30, PHI)]) for k in range(31)]
    b += curve(th_arc, ACCENT2, 1.6, dash_back=False)
    mx, my, _ = proj(*[0.45 * c for c in bloch(THETA / 2, PHI)])
    b.append(text(mx + 4, my, t["theta"], 17, ACCENT2, italic=True))
    ph_arc = [proj(*[0.35 * c for c in bloch(math.pi / 2, PHI * k / 30)]) for k in range(31)]
    b += curve(ph_arc, ACCENT2, 1.6, dash_back=False)
    px, py, _ = proj(*[0.5 * c for c in bloch(math.pi / 2, PHI / 2)])
    b.append(text(px, py + 16, t["phi"], 17, ACCENT2, italic=True))
    b.append(text(W / 2, H - 22, t["general"], 16, INK))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"bloch-sphere.{lang}.svg", build(lang)))
