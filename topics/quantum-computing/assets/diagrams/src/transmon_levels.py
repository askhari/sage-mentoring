"""Harmonic oscillator vs transmon energy levels -> transmon-levels.<lang>.svg

Transmon levels from the standard large-EJ/EC expansion
E_n ≈ −EJ + sqrt(8·EJ·EC)·(n + 1/2) − (EC/12)·(6n² + 6n + 3), which gives
f01 = sqrt(8·EJ·EC) − EC and anharmonicity α = f12 − f01 = −EC.
EC and EJ are chosen so that f01 = 5.0 GHz and α = −200 MHz (Kjaergaard et al. 2020, §2.1.1).
The potentials are drawn to scale only qualitatively.
"""
from __future__ import annotations

import math

from svgkit import ACCENT, ACCENT2, INK, MUTED, line, path, svg, text, write

F01, ALPHA = 5.0, -0.200            # GHz
EC = -ALPHA
W8 = F01 + EC                        # sqrt(8 EJ EC)
LABELS = {
    "es": {
        "ho": "Oscilador armónico (LC)",
        "tr": "Transmon (unión de Josephson)",
        "pot_ho": "potencial parabólico",
        "pot_tr": "potencial coseno",
        "eq": "niveles equiespaciados: todas las transiciones a la misma frecuencia",
        "anh": "anarmonicidad α = f12 − f01 ≈ −200 MHz",
        "qubit": "|0⟩ y |1⟩ forman el qubit; a escala, 200 MHz es solo el 4 % de 5 GHz",
        "ghz": "GHz",
        "note": "Niveles del transmon con la aproximación E_n ≈ √(8EJEC)(n+½) − EC(6n²+6n+3)/12, ajustada a f01 = 5 GHz y α = −200 MHz (Kjaergaard et al. 2020). Sycamore (2019): α mediana −208 MHz.",
    },
}

W, H = 1180, 580


def levels_transmon(n):
    return [W8 * (k + 0.5) - EC / 12 * (6 * k * k + 6 * k + 3) for k in range(n)]


def fmt(v):
    return f"{v:.1f}".replace(".", ",")


def build(lang: str) -> str:
    t = LABELS[lang]
    b: list[str] = []
    base, scale = 480, 22.0            # y of E=0 reference, px per GHz
    # harmonic
    cx = 290
    b.append(text(cx, 28, t["ho"], 16, INK, weight="bold"))
    pts = [f"{'M' if i == 0 else 'L'}{cx + x:.1f},{base - 0.0218 * x * x:.1f}" for i, x in enumerate(range(-130, 131, 2))]
    b.append(path(" ".join(pts), MUTED, width=1.6))
    b.append(text(cx + 130, 80, t["pot_ho"], 12, MUTED, anchor="start"))
    ho = [F01 * (k + 0.5) for k in range(4)]
    for k, e in enumerate(ho):
        y = base - e * scale * 0.0 - (k + 0.5) * 70
        half = 40 + 22 * k
        b.append(line(cx - half, y, cx + half, y, ACCENT, 2.4))
        b.append(text(cx - half - 10, y + 5, f"|{k}⟩", 14, anchor="end"))
        if k:
            b.append(text(cx + half + 12, y + 40, f"{fmt(F01)} {t['ghz']}", 13, ACCENT, anchor="start"))
    # transmon
    cx2 = 830
    b.append(text(cx2, 28, t["tr"], 16, INK, weight="bold"))
    pts = [f"{'M' if i == 0 else 'L'}{cx2 + x:.1f},{base - (1 - math.cos(x / 60)) * 205:.1f}" for i, x in enumerate(range(-185, 186, 2))]
    b.append(path(" ".join(pts), MUTED, width=1.6))
    b.append(text(cx2 + 185, 100, t["pot_tr"], 12, MUTED, anchor="start"))
    tr = levels_transmon(4)
    e0 = tr[0]
    for k, e in enumerate(tr):
        # same vertical mapping as the oscillator: 70 px per 5 GHz step
        y = base - 35 - (e - e0) / F01 * 70
        half = 40 + 22 * k
        b.append(line(cx2 - half, y, cx2 + half, y, ACCENT2, 2.4))
        b.append(text(cx2 - half - 10, y + 5, f"|{k}⟩", 14, anchor="end"))
        if k:
            f = e - tr[k - 1]
            b.append(text(cx2 + half + 12, y + 40, f"f{k-1}{k} ≈ {fmt(f)} {t['ghz']}", 13, ACCENT2, anchor="start"))
    b.append(text(cx, base + 30, t["eq"], 13, ACCENT))
    b.append(text(cx2, base + 30, t["anh"], 13, ACCENT2))
    b.append(text(cx2, base + 50, t["qubit"], 13, MUTED))
    b.append(text(W / 2, H - 8, t["note"], 12, MUTED))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"transmon-levels.{lang}.svg", build(lang)))
