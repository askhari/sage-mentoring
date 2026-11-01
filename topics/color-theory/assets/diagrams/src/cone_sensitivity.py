"""Normalized spectral sensitivity of S, M, L cones and rods -> cone-sensitivity.<lang>.svg

Curves: Govardovskii et al. (2000) A1 photopigment template. Peaks: Webvision,
chapter "Photoreceptors" (S ~420, M ~530, L ~560, rods ~500 nm). Peaks differ by
measurement method, so the figure is schematic.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from colormath import govardovskii_a1, spectral_color, spectrum_gradient  # noqa: E402

PEAKS = {"S": 420, "M": 530, "L": 560}
ROD = 500
LABELS = {
    "es": {
        "axis": "Longitud de onda (nm)",
        "y": "Sensibilidad relativa",
        "rod": "bastones",
        "note": "Esquema: los picos varían según el método de medida",
    },
}
W, H = 720, 400
L0, L1 = 380, 720
PX0, PX1, PY0, PY1 = 70, 690, 60, 320
OUT = Path(__file__).resolve().parent.parent


def px(nm: float) -> float:
    return PX0 + (nm - L0) / (L1 - L0) * (PX1 - PX0)


def py(v: float) -> float:
    return PY1 - v * (PY1 - PY0)


def curve(lmax: float) -> str:
    pts = [(nm, govardovskii_a1(nm, lmax)) for nm in range(L0, L1 + 1, 2)]
    peak = max(v for _, v in pts)
    return " ".join(f"{px(nm):.1f},{py(v / peak):.1f}" for nm, v in pts)


def render(lang: str) -> str:
    t = LABELS[lang]
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="13">',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
    s.append(f'<defs>{spectrum_gradient("axis", L0, L1)}</defs>')
    s.append(f'<rect x="{PX0}" y="{PY1 + 2}" width="{PX1 - PX0}" height="10" fill="url(#axis)"/>')
    s.append(f'<path d="M{PX0},{PY0} V{PY1} H{PX1}" stroke="#333" fill="none"/>')
    for nm in range(400, 701, 50):
        s.append(f'<text x="{px(nm):.1f}" y="{PY1 + 30}" text-anchor="middle">{nm}</text>')
    for v in (0, 0.5, 1):
        s.append(f'<text x="{PX0 - 8}" y="{py(v) + 4:.1f}" text-anchor="end">{v:g}</text>')
    s.append(f'<text x="{(PX0 + PX1) / 2}" y="{PY1 + 52}" text-anchor="middle">{t["axis"]}</text>')
    s.append(f'<text transform="translate(22,{(PY0 + PY1) / 2}) rotate(-90)" text-anchor="middle">{t["y"]}</text>')
    s.append(f'<polyline points="{curve(ROD)}" fill="none" stroke="#777" stroke-width="2" stroke-dasharray="6 4"/>')
    s.append(f'<text x="{px(ROD)}" y="{py(1) - 28:.1f}" text-anchor="middle" fill="#555">{t["rod"]} ~{ROD}</text>')
    for name, lmax in PEAKS.items():
        col = spectral_color(lmax, fade=False)
        s.append(f'<polyline points="{curve(lmax)}" fill="none" stroke="{col}" stroke-width="3"/>')
        dy = {"S": -8, "M": -8, "L": -8}[name]
        dx = {"S": 0, "M": -6, "L": 24}[name]
        s.append(f'<text x="{px(lmax) + dx:.1f}" y="{py(1) + dy:.1f}" text-anchor="middle" font-weight="bold">{name} ~{lmax}</text>')
    s.append(f'<text x="{PX1}" y="{H - 8}" text-anchor="end" font-size="11" fill="#555">{t["note"]}</text>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    for lang in LABELS:
        (OUT / f"cone-sensitivity.{lang}.svg").write_text(render(lang), encoding="utf-8")
