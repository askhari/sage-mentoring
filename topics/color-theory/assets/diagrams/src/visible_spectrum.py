"""Visible spectrum band inside the electromagnetic spectrum -> visible-spectrum.<lang>.svg"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from colormath import spectrum_gradient  # noqa: E402

LABELS = {
    "es": {
        "bands": ["Rayos gamma", "Rayos X", "Ultravioleta", "", "Infrarrojo", "Microondas", "Ondas de radio"],
        "visible": "Luz visible",
        "axis": "Longitud de onda (nm)",
        "short": "más corta",
        "long": "más larga",
    },
}

W, H = 760, 300
OUT = Path(__file__).resolve().parent.parent


def render(lang: str) -> str:
    t = LABELS[lang]
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="13">',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
    # Top: whole EM spectrum (schematic, not to scale)
    x0, top, bw, bh = 40, 30, 680, 34
    widths = [90, 90, 100, 40, 110, 110, 140]
    greys = ["#d8d8e8", "#dcdcec", "#e0dcf0", None, "#f0dcdc", "#ece4dc", "#e8e8dc"]
    x = x0
    vis_x = None
    for w, g, name in zip(widths, greys, t["bands"]):
        if g is None:
            vis_x = x
            s.append(f'<defs>{spectrum_gradient("vis", 380, 750, fade=False, steps=40)}</defs>')
            s.append(f'<rect x="{x}" y="{top}" width="{w}" height="{bh}" fill="url(#vis)"/>')
        else:
            s.append(f'<rect x="{x}" y="{top}" width="{w}" height="{bh}" fill="{g}"/>')
            s.append(f'<text x="{x + w / 2}" y="{top + bh / 2 + 4}" text-anchor="middle" font-size="11">{name}</text>')
        x += w
    s.append(f'<rect x="{x0}" y="{top}" width="{sum(widths)}" height="{bh}" fill="none" stroke="#666"/>')
    s.append(f'<text x="{x0}" y="{top - 8}" font-size="11" fill="#444">← {t["short"]}</text>')
    s.append(f'<text x="{x0 + sum(widths)}" y="{top - 8}" font-size="11" fill="#444" text-anchor="end">{t["long"]} →</text>')
    # Zoom lines
    zx0, zx1, ztop, zh = 60, 700, 130, 60
    s.append(f'<path d="M{vis_x},{top + bh} L{zx0},{ztop} M{vis_x + 40},{top + bh} L{zx1},{ztop}" stroke="#888" fill="none" stroke-dasharray="4 3"/>')
    s.append(f'<text x="{(zx0 + zx1) / 2}" y="{ztop - 10}" text-anchor="middle" font-weight="bold">{t["visible"]}</text>')
    # Bottom: visible band 360-830 nm with faded ends
    lo, hi = 360, 830
    s.append(f'<defs>{spectrum_gradient("band", lo, hi)}</defs>')
    s.append(f'<rect x="{zx0}" y="{ztop}" width="{zx1 - zx0}" height="{zh}" fill="url(#band)"/>')
    for nm in range(400, 801, 50):
        px = zx0 + (nm - lo) / (hi - lo) * (zx1 - zx0)
        s.append(f'<line x1="{px:.1f}" y1="{ztop + zh}" x2="{px:.1f}" y2="{ztop + zh + 6}" stroke="#333"/>')
        s.append(f'<text x="{px:.1f}" y="{ztop + zh + 20}" text-anchor="middle">{nm}</text>')
    s.append(f'<text x="{(zx0 + zx1) / 2}" y="{ztop + zh + 42}" text-anchor="middle">{t["axis"]}</text>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    for lang in LABELS:
        (OUT / f"visible-spectrum.{lang}.svg").write_text(render(lang), encoding="utf-8")
