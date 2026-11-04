"""Two-qubit gate time vs error across platforms -> platform-gate-time-vs-error.<lang>.svg

Log-log scatter of dated points cited in hardware-landscape.md:
superconducting arute-2019 (Table II, isolated / simultaneous) and kjaergaard-2020 (Table 1);
trapped ions bruzewicz-2019 (pp. 18-20); neutral atoms henriet-2020 (2018 experiment, p. 11);
spins stano-2022 (Si, April 2022). A band shows the 2024-25 neutral-atom state:
best Rydberg CZ error 0.29 % (Sr, saffman-2025 p. 9) with sub-microsecond gates
(eisert-2025 Box 1). Grey band: "<0.5 %, approaching 0.1 %" (eisert-2025 Box 1).
"""
from __future__ import annotations

import math

from svgkit import ACCENT, ACCENT2, ACCENT3, INK, MUTED, circle, line, rect, svg, text, write

PURPLE = "#7b4fa0"
POINTS = [  # (platform, time_s, error_percent, label)
    ("sc", 12e-9, 0.30, "Sycamore 2019, aislada"),
    ("sc", 12e-9, 0.60, "Sycamore 2019, en paralelo"),
    ("sc", 60e-9, 0.30, "CZ 2020"),
    ("ion", 30e-6, 0.09, "⁹Be⁺ 2019"),
    ("ion", 100e-6, 0.10, "⁴³Ca⁺ 2019"),
    ("ion", 1.6e-6, 0.20, "⁴³Ca⁺ rápida 2019"),
    ("atom", 1e-6, 5.9, "2018"),
    ("spin", 40e-9, 0.19, "Si 2022"),
]
COLORS = {"sc": ACCENT, "ion": ACCENT2, "atom": ACCENT3, "spin": PURPLE}
LABELS = {
    "es": {
        "x": "tiempo de la puerta de dos qubits (escala logarítmica)",
        "y": "error de la puerta de dos qubits (%)",
        "leg": {"sc": "superconductores", "ion": "iones atrapados", "atom": "átomos neutros", "spin": "espines en silicio"},
        "band": "átomos 2024-25: CZ con 0,29 % (Sr), puertas < 1 µs",
        "grey": "2025: < 0,5 % y acercándose a 0,1 % en las mejores plataformas (Eisert y Preskill)",
        "note": "Cifras de años y dispositivos distintos: no es un ranking. Cada punto lleva su año.",
    },
}

W, H = 1180, 600
X0, Y0, PW, PH = 110, 500, 760, 420
TMIN, TMAX = 1e-9, 1e-3
EMIN, EMAX = 0.05, 10.0


def px(ts):
    return X0 + (math.log10(ts) - math.log10(TMIN)) / (math.log10(TMAX) - math.log10(TMIN)) * PW


def py(e):
    return Y0 - (math.log10(e) - math.log10(EMIN)) / (math.log10(EMAX) - math.log10(EMIN)) * PH


def build(lang: str) -> str:
    t = LABELS[lang]
    b: list[str] = []
    # grey band 0.1-0.5 %
    b.append(rect(X0, py(0.5), PW, py(0.1) - py(0.5), "none", "#eeeeee", 0))
    b.append(text(X0 + PW - 8, py(0.5) + 16, t["grey"], 12, MUTED, anchor="end"))
    # axes
    b.append(line(X0, Y0, X0 + PW, Y0, INK, 1.3))
    b.append(line(X0, Y0, X0, Y0 - PH, INK, 1.3))
    for ts, lab in ((1e-9, "1 ns"), (1e-8, "10 ns"), (1e-7, "100 ns"), (1e-6, "1 µs"), (1e-5, "10 µs"), (1e-4, "100 µs"), (1e-3, "1 ms")):
        b.append(line(px(ts), Y0, px(ts), Y0 + 6, INK, 1))
        b.append(text(px(ts), Y0 + 22, lab, 12))
    for e in (0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10):
        b.append(line(X0 - 6, py(e), X0, py(e), INK, 1))
        b.append(text(X0 - 10, py(e) + 4, f"{e:g}".replace(".", ","), 12, anchor="end"))
    b.append(text(X0 + PW / 2, Y0 + 48, t["x"], 13, MUTED))
    b.append(text(X0 - 10, Y0 - PH - 16, t["y"], 13, MUTED, anchor="start"))
    # neutral-atom 2024-25 band: 0.29 % at < 1 µs (drawn 0.2-1 µs)
    b.append(line(px(0.2e-6), py(0.29), px(1e-6), py(0.29), ACCENT3, 5))
    b.append(text(px(0.2e-6), py(0.29) - 10, t["band"], 12, ACCENT3, anchor="start"))
    # points
    offsets = {"Sycamore 2019, aislada": (10, -8), "Sycamore 2019, en paralelo": (10, -8), "CZ 2020": (10, 14),
               "⁹Be⁺ 2019": (10, 14), "⁴³Ca⁺ 2019": (10, -8), "⁴³Ca⁺ rápida 2019": (10, 16), "2018": (10, 4), "Si 2022": (-10, -10)}
    for plat, ts, e, lab in POINTS:
        x, y = px(ts), py(e)
        b.append(circle(x, y, 7, COLORS[plat], COLORS[plat]))
        dx, dy = offsets[lab]
        b.append(text(x + dx, y + dy, lab, 12, COLORS[plat], anchor="start" if dx > 0 else "end"))
    # legend
    lx, ly = X0 + PW + 30, 120
    for i, (k, v) in enumerate(t["leg"].items()):
        b.append(circle(lx + 7, ly + i * 30, 7, COLORS[k], COLORS[k]))
        b.append(text(lx + 22, ly + i * 30 + 5, v, 13, INK, anchor="start"))
    b.append(text(W / 2, H - 10, t["note"], 13, MUTED))
    return svg(W, H, b)


if __name__ == "__main__":
    for lang in LABELS:
        print(write(f"platform-gate-time-vs-error.{lang}.svg", build(lang)))
