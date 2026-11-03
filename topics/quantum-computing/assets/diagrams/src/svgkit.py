"""Small shared SVG helpers for the quantum-computing diagrams (standard library only)."""
from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent

INK = "#222222"
MUTED = "#888888"
ACCENT = "#1f6fb2"     # main vector / highlight
ACCENT2 = "#c2571a"    # second highlight
ACCENT3 = "#2e8b57"    # third highlight
FONT = "font-family='Helvetica, Arial, sans-serif'"


def svg(width: int, height: int, body: list[str]) -> str:
    return (
        f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {width} {height}' "
        f"width='{width}' height='{height}' {FONT}>\n"
        f"<rect width='100%' height='100%' fill='white'/>\n"
        "<defs>"
        + "".join(
            f"<marker id='arrow-{n}' viewBox='0 0 10 10' refX='9' refY='5' markerWidth='7' markerHeight='7' "
            f"orient='auto-start-reverse'><path d='M0,0 L10,5 L0,10 z' fill='{c}'/></marker>"
            for n, c in (("ink", INK), ("a1", ACCENT), ("a2", ACCENT2), ("a3", ACCENT3), ("muted", MUTED))
        )
        + "</defs>\n"
        + "\n".join(body)
        + "\n</svg>\n"
    )


def line(x1, y1, x2, y2, color=INK, width=1.5, dash=None, arrow=None) -> str:
    d = f" stroke-dasharray='{dash}'" if dash else ""
    a = f" marker-end='url(#arrow-{arrow})'" if arrow else ""
    return (f"<line x1='{x1:.1f}' y1='{y1:.1f}' x2='{x2:.1f}' y2='{y2:.1f}' "
            f"stroke='{color}' stroke-width='{width}'{d}{a}/>")


def text(x, y, s: str, size=16, color=INK, anchor="middle", italic=False, weight="normal") -> str:
    st = " font-style='italic'" if italic else ""
    return (f"<text x='{x:.1f}' y='{y:.1f}' font-size='{size}' fill='{color}' text-anchor='{anchor}' "
            f"font-weight='{weight}'{st}>{escape(s)}</text>")


def circle(cx, cy, r, stroke=INK, fill="none", width=1.5, dash=None) -> str:
    d = f" stroke-dasharray='{dash}'" if dash else ""
    return f"<circle cx='{cx:.1f}' cy='{cy:.1f}' r='{r:.1f}' stroke='{stroke}' fill='{fill}' stroke-width='{width}'{d}/>"


def rect(x, y, w, h, stroke=INK, fill="none", width=1.5, rx=0) -> str:
    return (f"<rect x='{x:.1f}' y='{y:.1f}' width='{w:.1f}' height='{h:.1f}' rx='{rx}' "
            f"stroke='{stroke}' fill='{fill}' stroke-width='{width}'/>")


def path(d: str, stroke=INK, fill="none", width=1.5) -> str:
    return f"<path d='{d}' stroke='{stroke}' fill='{fill}' stroke-width='{width}'/>"


def write(name: str, content: str) -> Path:
    p = OUT / name
    p.write_text(content, encoding="utf-8")
    return p


# --- quantum-circuit helpers -------------------------------------------------

GATE = 44   # gate box size


def wire(x1, x2, y, classical=False) -> str:
    """Quantum wire (single line) or classical wire (double line)."""
    if classical:
        return line(x1, y - 2.5, x2, y - 2.5, INK, 1.2) + line(x1, y + 2.5, x2, y + 2.5, INK, 1.2)
    return line(x1, y, x2, y, INK, 1.5)


def vwire(x, y1, y2, classical=False) -> str:
    if classical:
        return line(x - 2.5, y1, x - 2.5, y2, INK, 1.2) + line(x + 2.5, y1, x + 2.5, y2, INK, 1.2)
    return line(x, y1, x, y2, INK, 1.5)


def gate(x, y, label: str, fill="#dbe9f6", stroke=ACCENT) -> str:
    """Gate box centred at (x, y)."""
    h = GATE / 2
    return rect(x - h, y - h, GATE, GATE, stroke, fill, 2, rx=5) + text(x, y + 7, label, 20, INK, weight="bold")


def control(x, y) -> str:
    return circle(x, y, 6, stroke=INK, fill=INK)


def target(x, y) -> str:
    r = 13
    return circle(x, y, r, stroke=INK, fill="white", width=1.8) + line(x - r, y, x + r, y, INK, 1.8) + line(x, y - r, x, y + r, INK, 1.8)


def cnot(x, yc, yt) -> str:
    return vwire(x, yc, yt + (13 if yt > yc else -13)) + control(x, yc) + target(x, yt)


def meter(x, y) -> str:
    """Measurement box with a dial."""
    h = GATE / 2
    return (rect(x - h, y - h, GATE, GATE, INK, "#f2f2f2", 2, rx=5)
            + path(f"M{x - 14:.1f},{y + 8:.1f} A16,16 0 0 1 {x + 14:.1f},{y + 8:.1f}", INK, width=1.6)
            + line(x, y + 8, x + 10, y - 10, INK, 1.6))
