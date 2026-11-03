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
