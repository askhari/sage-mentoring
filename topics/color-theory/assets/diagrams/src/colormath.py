"""Shared colour math for the diagrams (standard library only).

- CIE 1931 2° colour-matching functions: multi-lobe analytic fit by
  Wyman, Sloan & Shirley (2013), "Simple Analytic Approximations to the CIE XYZ
  Color Matching Functions", JCGT 2(2).
- XYZ -> linear sRGB (IEC 61966-2-1 matrix, D65) -> gamma-encoded sRGB.
- CIELAB (CIE 1976 L*a*b*) <-> XYZ: CIE S 017:2020 e-ILV term 17-23-076 / CIE 015:2018,
  with the D65 white of IEC 61966-2-1 (sRGB); LCh: C*ab = sqrt(a*^2 + b*^2), h_ab = atan2(b*, a*).
- Photopigment absorbance template (A1, alpha + beta bands): Govardovskii et al.
  (2000), "In search of the visual pigment template", Visual Neuroscience 17.
"""
from __future__ import annotations

import math


def _g(x: float, mu: float, s1: float, s2: float) -> float:
    s = s1 if x < mu else s2
    return math.exp(-0.5 * ((x - mu) / s) ** 2)


def cmf_xyz(nm: float) -> tuple[float, float, float]:
    x = 1.056 * _g(nm, 599.8, 37.9, 31.0) + 0.362 * _g(nm, 442.0, 16.0, 26.7) - 0.065 * _g(nm, 501.1, 20.4, 26.2)
    y = 0.821 * _g(nm, 568.8, 46.9, 40.5) + 0.286 * _g(nm, 530.9, 16.3, 31.1)
    z = 1.217 * _g(nm, 437.0, 11.8, 36.0) + 0.681 * _g(nm, 459.0, 26.0, 13.8)
    return x, y, z


def xyz_to_linear_srgb(x: float, y: float, z: float) -> tuple[float, float, float]:
    return (3.2406 * x - 1.5372 * y - 0.4986 * z,
            -0.9689 * x + 1.8758 * y + 0.0415 * z,
            0.0557 * x - 0.2040 * y + 1.0570 * z)


def encode_srgb(c: float) -> float:
    c = min(1.0, max(0.0, c))
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def hex_rgb(rgb: tuple[float, float, float]) -> str:
    return "#" + "".join(f"{round(encode_srgb(c) * 255):02x}" for c in rgb)


def spectral_color(nm: float, fade: bool = True) -> str:
    """Approximate display colour of a monochromatic light.

    Spectral colours lie outside the sRGB gamut: negative components are removed by
    adding white (desaturation), then the colour is scaled to full brightness. With
    fade, brightness follows the luminous efficiency (y-bar) near the spectrum ends,
    so the band has no sharp borders.
    """
    r, g, b = xyz_to_linear_srgb(*cmf_xyz(nm))
    lo = min(r, g, b)
    if lo < 0:
        r, g, b = r - lo, g - lo, b - lo
    hi = max(r, g, b) or 1.0
    r, g, b = r / hi, g / hi, b / hi
    if fade:
        k = min(1.0, cmf_xyz(nm)[1] / 0.08)
        r, g, b = r * k, g * k, b * k
    return hex_rgb((r, g, b))


def govardovskii_a1(nm: float, lmax: float) -> float:
    """Normalized absorbance of an A1 visual pigment with peak lmax (nm)."""
    x = lmax / nm
    a = 0.8795 + 0.0459 * math.exp(-((lmax - 300) ** 2) / 11940)
    alpha = 1 / (math.exp(69.7 * (a - x)) + math.exp(28 * (0.922 - x)) + math.exp(-14.9 * (1.104 - x)) + 0.674)
    lmb = 189 + 0.315 * lmax
    bb = -40.5 + 0.195 * lmax
    beta = 0.26 * math.exp(-(((nm - lmb) / bb) ** 2))
    return alpha + beta


def spectrum_gradient(gid: str, lo: float, hi: float, fade: bool = True, steps: int = 120) -> str:
    """SVG linearGradient (horizontal) with spectral colours from lo to hi nm."""
    stops = []
    for i in range(steps + 1):
        nm = lo + (hi - lo) * i / steps
        stops.append(f'<stop offset="{i / steps:.4f}" stop-color="{spectral_color(nm, fade)}"/>')
    return f'<linearGradient id="{gid}" x1="0" x2="1" y1="0" y2="0">{"".join(stops)}</linearGradient>'


# --- CIELAB (CIE 1976 L*a*b*) ---------------------------------------------
# Reference white: D65 as used by sRGB (IEC 61966-2-1), Y normalized to 1.
D65_WHITE = (0.95047, 1.0, 1.08883)
_EPS = (6 / 29) ** 3


def _f(t: float) -> float:
    return t ** (1 / 3) if t > _EPS else t / (3 * (6 / 29) ** 2) + 4 / 29


def _finv(t: float) -> float:
    return t ** 3 if t > 6 / 29 else 3 * (6 / 29) ** 2 * (t - 4 / 29)


def xyz_to_lab(x: float, y: float, z: float, white=D65_WHITE) -> tuple[float, float, float]:
    """CIE 1976 L*a*b* from XYZ (e-ILV 17-23-076): L* = 116 f(Y/Yn) - 16, a* = 500[f(X/Xn) - f(Y/Yn)],
    b* = 200[f(Y/Yn) - f(Z/Zn)], f = cube root above (6/29)^3 and linear below."""
    fx, fy, fz = _f(x / white[0]), _f(y / white[1]), _f(z / white[2])
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)


def lab_to_xyz(l: float, a: float, b: float, white=D65_WHITE) -> tuple[float, float, float]:
    """Inverse of xyz_to_lab."""
    fy = (l + 16) / 116
    return white[0] * _finv(fy + a / 500), white[1] * _finv(fy), white[2] * _finv(fy - b / 200)


def lch_to_lab(l: float, c: float, h_deg: float) -> tuple[float, float, float]:
    """CIELAB from lightness L*, chroma C*ab and hue angle h_ab (degrees)."""
    h = math.radians(h_deg)
    return l, c * math.cos(h), c * math.sin(h)


def lab_to_linear_srgb(l: float, a: float, b: float) -> tuple[float, float, float]:
    """Linear sRGB (may fall outside [0, 1] when the colour is out of gamut)."""
    return xyz_to_linear_srgb(*lab_to_xyz(l, a, b))


def in_srgb_gamut(rgb: tuple[float, float, float], tol: float = 1e-4) -> bool:
    return all(-tol <= c <= 1 + tol for c in rgb)


def lch_hex(l: float, c: float, h_deg: float) -> str | None:
    """sRGB hex for an LCh colour, or None when it lies outside the sRGB gamut."""
    rgb = lab_to_linear_srgb(*lch_to_lab(l, c, h_deg))
    return hex_rgb(rgb) if in_srgb_gamut(rgb) else None


def max_srgb_chroma(l: float, h_deg: float, hi: float = 200.0) -> float:
    """Largest C*ab at (L*, h_ab) still inside the sRGB gamut (bisection)."""
    lo = 0.0
    for _ in range(40):
        mid = (lo + hi) / 2
        if lch_hex(l, mid, h_deg) is None:
            hi = mid
        else:
            lo = mid
    return lo


# --- Munsell hue -> approximate CIELAB hue angle --------------------------
# Munsell hue as a number on a 0-100 circle: R 0-10, YR 10-20, Y 20-30, GY 30-40,
# G 40-50, BG 50-60, B 60-70, PB 70-80, P 80-90, RP 90-100 (so 5R = 5, 5PB = 75).
# Anchors: measured Munsell hue and h_ab = atan2(b*, a*) of paints with chroma > 5 in
# Golden Artist Colors, "Munsell and Lab Readings for Williamsburg Handmade Oil Colors"
# (source justpaint-munsell-cielab). Paint films, not renotation data: only approximate.
MUNSELL_PRINCIPAL = ["R", "YR", "Y", "GY", "G", "BG", "B", "PB", "P", "RP"]
_HUE_ANCHORS = [  # (Munsell hue number, h_ab in degrees, paint)
    (3.94, 22.65, "Persian Rose"),
    (8.00, 38.41, "Cadmium Red Medium"),
    (10.50, 52.65, "Permanent Orange"),
    (19.62, 70.32, "Yellow Ochre"),
    (22.73, 81.46, "Cadmium Yellow Medium"),
    (29.06, 95.03, "Cadmium Lemon"),
    (45.67, 160.39, "French Terre Verte"),
    (51.51, 178.01, "Viridian"),
    (61.42, 204.83, "Phthalo Green"),
    (71.61, 243.93, "Cerulean Blue French"),
    (76.42, 280.28, "Cobalt Blue"),
    (80.71, 304.24, "Ultramarine Violet"),
    (88.53, 321.84, "Manganese Violet"),
    (93.01, 345.68, "Dianthus Pink"),
]


def munsell_hue_number(step: float, family: str) -> float:
    """'5', 'PB' -> 75.0 on the 0-100 hue circle."""
    return (MUNSELL_PRINCIPAL.index(family) * 10 + step) % 100


def munsell_hue_angle(hue_number: float) -> float:
    """Approximate CIELAB hue angle (degrees) for a Munsell hue number, by circular
    linear interpolation between the paint anchors above."""
    pts = sorted(_HUE_ANCHORS)
    ext = [(n - 100, h - 360) for n, h, _ in pts] + [(n, h) for n, h, _ in pts] + [(n + 100, h + 360) for n, h, _ in pts]
    x = hue_number % 100
    for (n0, h0), (n1, h1) in zip(ext, ext[1:]):
        if n0 <= x <= n1:
            return (h0 + (h1 - h0) * (x - n0) / (n1 - n0)) % 360
    raise ValueError(hue_number)


# --- Reflectance spectra and Kubelka-Munk mixing ----------------------------
# Kubelka & Munk (1931), "An Article on Optics of Paint Layers" (trans. Westin):
# for an opaque (infinitely thick) layer, reflectance R depends only on the ratio
# K/S of absorption to scattering: K/S = (1 - R)^2 / (2R), and its inverse
# R = 1 + K/S - sqrt((K/S)^2 + 2 K/S). Mixtures: single-constant simplification,
# K/S of a mixture = concentration-weighted sum of each colorant's K/S (Duncan 1940,
# as used by Sochorova & Jamriska 2021). Used here only for illustrative diagrams
# with synthetic spectra, not for measured paints.
WAVELENGTHS = list(range(400, 701, 5))


def ks_from_r(r: float) -> float:
    r = min(max(r, 1e-4), 1.0)
    return (1 - r) ** 2 / (2 * r)


def r_from_ks(ks: float) -> float:
    return 1 + ks - math.sqrt(ks * ks + 2 * ks)


def km_mix(spectra: list[list[float]], weights: list[float]) -> list[float]:
    """Single-constant Kubelka-Munk mixture of opaque reflectance spectra."""
    tot = sum(weights)
    out = []
    for i in range(len(WAVELENGTHS)):
        ks = sum(w * ks_from_r(s[i]) for s, w in zip(spectra, weights)) / tot
        out.append(r_from_ks(ks))
    return out


def optical_mix(spectra: list[list[float]], weights: list[float]) -> list[float]:
    """Partitive (optical) mixture: area-weighted average of reflected light."""
    tot = sum(weights)
    return [sum(w * s[i] for s, w in zip(spectra, weights)) / tot for i in range(len(WAVELENGTHS))]


def _xyz_raw(spec: list[float]) -> tuple[float, float, float]:
    x = y = z = 0.0
    for nm, r in zip(WAVELENGTHS, spec):
        cx, cy, cz = cmf_xyz(nm)
        x, y, z = x + r * cx, y + r * cy, z + r * cz
    return x, y, z


_E_WHITE = _xyz_raw([1.0] * len(WAVELENGTHS))


def reflectance_xyz(spec: list[float]) -> tuple[float, float, float]:
    """XYZ of a reflectance spectrum under an equal-energy illuminant, rescaled per
    channel so the perfect white maps to the D65 white (a crude von Kries-type
    adaptation; good enough for illustrative diagrams, not for measurement)."""
    x, y, z = _xyz_raw(spec)
    return (x / _E_WHITE[0] * D65_WHITE[0], y / _E_WHITE[1], z / _E_WHITE[2] * D65_WHITE[2])


def reflectance_lab(spec: list[float]) -> tuple[float, float, float]:
    return xyz_to_lab(*reflectance_xyz(spec))


def reflectance_hex(spec: list[float]) -> str:
    return hex_rgb(xyz_to_linear_srgb(*reflectance_xyz(spec)))


# --- Two-constant Kubelka-Munk: layers of finite thickness ------------------
# Kubelka & Munk (1931): a layer with absorption K and scattering S (per unit
# thickness) and thickness X over a background of reflectance Rg reflects
#   R = (1 - Rg (a - b coth(b S X))) / (a - Rg + b coth(b S X)),
# with a = 1 + K/S and b = sqrt(a^2 - 1). For X -> infinity this tends to
# R_inf = a - b, the opaque-layer value used by r_from_ks. Mixtures of paints
# add their K and S weighted by concentration (two-constant form). Illustrative
# use with synthetic K and S spectra only.

def km_layer(k: float, s: float, x: float, rg: float) -> float:
    """Reflectance of one paint layer (K, S, thickness X) over a background Rg."""
    a = 1 + k / s
    b = math.sqrt(a * a - 1)
    bsx = b * s * x
    coth = 1 / math.tanh(bsx) if bsx < 30 else 1.0
    return (1 - rg * (a - b * coth)) / (a - rg + b * coth)


def km_layer_spectrum(k: list[float], s: list[float], x: float, rg: list[float] | float) -> list[float]:
    """km_layer per wavelength; rg may be a spectrum or a constant."""
    rgs = rg if isinstance(rg, list) else [rg] * len(WAVELENGTHS)
    return [km_layer(ki, si, x, gi) for ki, si, gi in zip(k, s, rgs)]


def km_mix_ks(paints: list[tuple[list[float], list[float]]], weights: list[float]) -> tuple[list[float], list[float]]:
    """Two-constant mixture: concentration-weighted K and S spectra."""
    tot = sum(weights)
    k = [sum(w * p[0][i] for p, w in zip(paints, weights)) / tot for i in range(len(WAVELENGTHS))]
    s = [sum(w * p[1][i] for p, w in zip(paints, weights)) / tot for i in range(len(WAVELENGTHS))]
    return k, s
