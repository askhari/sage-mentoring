"""KEM flow (FIPS 203 roles) -> kem-flow.<lang>.svg

Alice: KeyGen -> (ek public, dk private), sends ek. Bob: Encaps(ek) -> (K, c), sends c.
Alice: Decaps(dk, c) -> K. Both end with the same shared key K for symmetric encryption.
"""
from __future__ import annotations

from svgkit import ACCENT, ACCENT2, ACCENT3, INK, MUTED, block, line, svg, text, write

LABELS = {
    "es": {
        "alice": "Alicia",
        "bob": "Bernardo",
        "keygen": ["KeyGen()", "→ ek (pública), dk (privada)"],
        "encaps": ["Encaps(ek)", "→ clave K, texto cifrado c"],
        "decaps": ["Decaps(dk, c)", "→ clave K"],
        "send_ek": "envía ek (canal público)",
        "send_c": "envía c (canal público)",
        "shared": "Ambos tienen la misma clave K → cifrado simétrico (p. ej. AES)",
    },
}

W, H = 900, 470


def build(lang: str) -> str:
    t = LABELS[lang]
    xa, xb, bw, bh = 60, 560, 280, 80
    b: list[str] = []
    b.append(text(xa + bw / 2, 40, t["alice"], 18, ACCENT, weight="bold"))
    b.append(text(xb + bw / 2, 40, t["bob"], 18, ACCENT2, weight="bold"))
    b.append(line(xa + bw / 2, 50, xa + bw / 2, 400, MUTED, 1, dash="4 5"))
    b.append(line(xb + bw / 2, 50, xb + bw / 2, 400, MUTED, 1, dash="4 5"))
    b.append(block(xa, 70, bw, bh, t["keygen"], fill="#dbe9f6", stroke=ACCENT))
    b.append(line(xa + bw + 4, 130, xb - 4, 170, INK, 1.8, arrow="ink"))
    b.append(text(440, 128, t["send_ek"], 13, MUTED))
    b.append(block(xb, 170, bw, bh, t["encaps"], fill="#fde3d3", stroke=ACCENT2))
    b.append(line(xb - 4, 230, xa + bw + 4, 270, INK, 1.8, arrow="ink"))
    b.append(text(460, 276, t["send_c"], 13, MUTED))
    b.append(block(xa, 270, bw, bh, t["decaps"], fill="#dbe9f6", stroke=ACCENT))
    b.append(text(W / 2, 430, t["shared"], 15, ACCENT3, weight="bold"))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"kem-flow.{lang}.svg", build(lang)))
