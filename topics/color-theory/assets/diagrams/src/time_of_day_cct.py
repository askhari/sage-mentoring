"""Mean colour temperature of morning vs evening paintings -> time-of-day-cct.<lang>.svg

A strip of blackbody colours from 3500 K to 7000 K (as seen on a D65 display, no
chromatic adaptation) with the mean luminance-weighted correlated colour temperatures
that Yu et al. (2024) measured in landscape paintings: by title label (morning 5233 K,
evening 4692 K) and by observers' majority classification (morning 5686 K, evening
3945 K), plus D65 (about 6500 K) as reference.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from colormath import blackbody_hex  # noqa: E402

LABELS = {
    "es": {
        "title": "Temperatura de color media de cuadros de paisaje",
        "top": "por título",
        "bottom": "por clasificación de los observadores",
        "morning": "mañana",
        "evening": "tarde",
        "d65": "D65 (luz del día de referencia)",
        "warm": "← más cálido",
        "cool": "más frío →",
    },
}

K_LO, K_HI = 3500.0, 7000.0
TOP = [(5233, "morning"), (4692, "evening")]
BOTTOM = [(5686, "morning"), (3945, "evening")]
OUT = Path(__file__).resolve().parent.parent
W, H = 900, 330
X0, X1, Y0, SH = 60, 840, 130, 60


def xk(k: float) -> float:
    return X0 + (k - K_LO) / (K_HI - K_LO) * (X1 - X0)


def render(lang: str) -> str:
    t = LABELS[lang]
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="14">',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
         f'<text x="{W / 2}" y="30" text-anchor="middle" font-weight="bold" font-size="16" fill="#222">{t["title"]}</text>']
    n = 140
    for i in range(n):
        k0 = K_LO + (K_HI - K_LO) * i / n
        x = xk(k0)
        s.append(f'<rect x="{x:.1f}" y="{Y0}" width="{(X1 - X0) / n + 0.6:.1f}" height="{SH}" '
                 f'fill="{blackbody_hex(k0 + (K_HI - K_LO) / n / 2)}"/>')
    s.append(f'<rect x="{X0}" y="{Y0}" width="{X1 - X0}" height="{SH}" fill="none" stroke="#999"/>')
    for k in range(4000, 7001, 500):
        s.append(f'<line x1="{xk(k):.1f}" y1="{Y0 + SH}" x2="{xk(k):.1f}" y2="{Y0 + SH + 6}" stroke="#666"/>')
        s.append(f'<text x="{xk(k):.1f}" y="{Y0 + SH + 20}" text-anchor="middle" font-size="12" fill="#555">{k} K</text>')
    s.append(f'<text x="{X0}" y="{Y0 + SH + 40}" font-size="12" fill="#555">{t["warm"]}</text>')
    s.append(f'<text x="{X1}" y="{Y0 + SH + 40}" text-anchor="end" font-size="12" fill="#555">{t["cool"]}</text>')
    # markers above (title labels) and below (observers' classification)
    s.append(f'<text x="{X0}" y="62" font-size="13" fill="#333" font-style="italic">{t["top"]}</text>')
    for k, key in TOP:
        x = xk(k)
        s.append(f'<path d="M{x:.1f},{Y0 - 2} l-7,-12 l14,0 Z" fill="#222"/>')
        s.append(f'<text x="{x:.1f}" y="{Y0 - 20}" text-anchor="middle" font-size="13" fill="#111">{t[key]} {k} K</text>')
    yb = Y0 + SH + 62
    s.append(f'<text x="{X0}" y="{yb + 40}" font-size="13" fill="#333" font-style="italic">{t["bottom"]}</text>')
    for k, key in BOTTOM:
        x = xk(k)
        s.append(f'<path d="M{x:.1f},{yb - 12} l-7,12 l14,0 Z" fill="#222"/>')
        s.append(f'<text x="{x:.1f}" y="{yb + 16}" text-anchor="middle" font-size="13" fill="#111">{t[key]} {k} K</text>')
    xd = xk(6504)
    s.append(f'<line x1="{xd:.1f}" y1="{Y0 - 30}" x2="{xd:.1f}" y2="{Y0 + SH}" stroke="#222" stroke-dasharray="4 3"/>')
    s.append(f'<text x="{xd:.1f}" y="{Y0 - 36}" text-anchor="middle" font-size="12" fill="#333">{t["d65"]}</text>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    for lang in LABELS:
        (OUT / f"time-of-day-cct.{lang}.svg").write_text(render(lang), encoding="utf-8")
        print(f"wrote time-of-day-cct.{lang}.svg")
