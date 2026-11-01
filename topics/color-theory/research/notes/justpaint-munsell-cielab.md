---
source: justpaint-munsell-cielab
concepts: [munsell-system, cielab-basics, value, chroma, masstone-undertone]
---

Accessed: PARTIAL. justpaint.org/?p=5235 returned only a "down for maintenance" page (2026-11-01) and www.justpaint.org PDFs did not resolve (DNS error). The Williamsburg munsell-ordering PDF (mirror on assets.goldenartistcolors.com) downloaded but could not be decoded (no PDF tool). Method statements below come from a search-engine summary of the justpaint page (secondhand, unverified against the page). The numeric table comes from Golden's own page "Munsell Notation listing - Heavy Body Acrylics" (goldenartistcolors.com/resources/munsell-notation-listing-heavy-body-acrylics, no date shown), which is a related Golden listing with H V/C only (no L*a*b*) and is NOT the requested document. Article title and date could NOT be confirmed. A justpaint post of 2021 ("...golden hb and fluid acrylics w light and new colors 032921", URL slug suggests 29 Mar 2021) exists but returned 404 on fetch.

## Method (secondhand, from search summary of the justpaint page)
- The Munsell notations for GOLDEN acrylics are based on Heavy Body Acrylics applied at two thicknesses: 10 mil drawdowns (about 3 sheets of paper) and 1/4 inch discs. (justpaint page via search summary) → cielab-basics
- Few acrylics are fully opaque at 10 mil, so 10 mil readings tend to be lighter and higher in chroma; the fully opaque 1/4 inch disc is included as the comparison reference. (same) → value, chroma
- Golden says the Munsell list was made with a spectrophotometer plus visual interpretation. (Golden Munsell listing page, intro) → munsell-system
- A Williamsburg Oils dataset was measured at 6 mil (about 2 sheets of paper); oils also shift in value or colour while drying, which the user should consider. (search summary of justpaint page) → cielab-basics
- Acrylics shift slightly on drying, becoming deeper and more saturated, so the readings are best used as a guide to the dried colour. (search summary) → cielab-basics
- Illuminant and observer: not found in any accessible material. Unverified. → cielab-basics
- Tables give both Munsell and CIE L*a*b* per paint. Example (search summary, column-to-thickness mapping unclear): Alizarin Crimson Hue 3.1R 2.7/2.1 with L* 27.94, a* 9.37, b* 2.19, and 8.3R 1.1/3.9 with L* 11.83, a* 19.06, b* 5.45. ⚠️ the two readings differ strongly, possibly because of thickness; not verified. → cielab-basics, value

## Munsell notation in Golden's listing (Golden Munsell listing page, table)
- The listing reports each paint as Hue, Value, Chroma (e.g. 3.0 YR, 3.25, 4 for Burnt Sienna), and refers readers to The Munsell Book of Color (1976) or munsell.com for the system itself. → munsell-system
- Achromatic paints are listed as "Black" or "White" instead of a hue, since hue is meaningless at near-zero chroma. → munsell-system, chroma
- Sorting the table by value gives a ready ordering of a palette from dark to light, and by chroma from dull to vivid. Painter use (my inference from the table layout, not a source claim). → value, chroma
- ⚠️ The table has apparent typos ("73.92" as hue of Cadmium Red Dark; "19.0 YR" for Raw Sienna; hue ".75 G" for Sap Green Hue). Treat as errors. → munsell-system

## Examples of H V/C (Golden Heavy Body listing, table; V = value, C = chroma)
- Dark, high chroma: Phthalo Blue (Red Shade) 7.5 PB 1.25/6; Quinacridone Magenta 10 RP 2.5/10. → value, chroma
- Light, high chroma: Cadmium Yellow Primrose 10.0 Y 9/16; Hansa Yellow Opaque 5.0 Y 8/16. → value, chroma
- Mid-value, highest chroma: Pyrrole Orange 9.0 R 5/18; Naphthol Red Light 7.0 R 4.25/17. → chroma
- Earth: Burnt Umber 9.0 YR 2.5/1; Yellow Ochre 9.5 YR 5/8.8; Raw Umber 3.0 Y 2.5/1.3. Earths are low in chroma relative to cadmiums and dark to mid in value. → value, chroma
- Neutral greys: Neutral Gray N2 value 2.8, N3 3.5, N4 4.2, N5 5.1, N6 6.1, N7 7.0, N8 7.9, all chroma 0 to 0.1 (hue listed but meaningless). The N-number approximates the Munsell value. → value, chroma
- Whites and blacks: Titanium White 10/1.1, Zinc White 10/1.5, Carbon Black 1/0.3, Mars Black 1/0.7 (so black paint is about value 1, not 0). → value
- Hue-wise, similar-hue paints differ widely in value: Cerulean Blue Deep 1.2 PB 3/7.9 vs Light Ultramarine Blue 3.0 PB 6.3/7.9 (same chroma, different value). → value, chroma
- Hue name versus mixing: Cadmium Yellow Medium Hue 1.5 Y 8/13.7 (a "Hue" imitation) vs C.P. Cadmium Yellow Medium 3.0 Y 8/16.1 shows the genuine pigment has higher chroma. → chroma

## Williamsburg oils: Munsell + CIELAB table (verified by the main session, 2026-11-01)
Read directly: Golden PDF "Munsell and Lab Readings for Williamsburg Handmade Oil Colors — Munsell Ordering", 4 pp., https://assets.goldenartistcolors.com/v4/linked-files/2343-munsell-and-cie-lab-data-for-williamsburg-oils-munsell-ordering.pdf (text extracted locally). Columns: Name, Hue, Value, Chroma, L*, a*, b*. Film: 6 mil (header). Illuminant/observer not stated in the PDF.
- The table is sorted by Munsell hue (R → YR → Y → GY → G → BG → B → PB → P → RP) and gives decimal hue, value and chroma for each paint next to its L*, a*, b*. (PDF, header and ordering) → munsell-system, cielab-basics
- Very dark, high-chroma masstones: Ultramarine Blue 9.01PB 0.32/18.16, L* 4.78, a* 24.88, b* −37.90; Phthalo Blue 9.61PB 0.60/12.00, L* 7.75; Alizarin Crimson 1.42YR 1.12/6.15, L* 11.18. (PDF pp. 1–4) → value, chroma, cielab-basics
- Light, high-chroma yellows: Cadmium Lemon 9.06Y 9.05/12.69, L* 89.99, a* −8.36, b* 94.94; Cadmium Yellow Medium 2.73Y 8.45/16.78, L* 83.08, b* 111.85. (PDF) → value, chroma, cielab-basics
- Mid-value, highest-chroma reds: Cadmium Red Light 9.29R 5.13/17.97, L* 51.19, a* 64.23, b* 70.20; Cadmium Red Medium 8R 3.92/16.05. (PDF) → chroma, value
- Earths, low chroma: Yellow Ochre 9.62YR 5.55/8.69, L* 55.50, a* 18.84, b* 52.68; Burnt Sienna 2.23YR 2.61/6.10; Raw Umber 6.41Y 1.83/1.18, L* 18.68, a* 0.42, b* 7.03. (PDF) → chroma, value
- Whites and blacks: Titanium White 2.7GY 9.73/0.24, L* 98.24, a* −0.99, b* 2.58; Ivory Black 5.16PB 1.03/0.08, L* 10.83; Mars Black 8.34YR 0.82/0.19, L* 8.73. Near-neutral paints still receive a hue in the table even though their chroma is near 0. (PDF) → value, chroma, munsell-system
- Same hue family, very different value: Cobalt Blue 6.42PB 2.25/13.27 (L* 26.58) vs Ultramarine Blue 9.01PB 0.32/18.16 (L* 4.78). (PDF) → value, hue
- Munsell value and L* run together in the table (e.g. value 0.32 ↔ L* 4.78, 5.13 ↔ 51.19, 9.73 ↔ 98.24): roughly L* ≈ 10 × value. (PDF, computed from rows) → value, cielab-basics
- Munsell chroma and C*ab = √(a*²+b*²) are not proportional across hues: Cadmium Yellow Medium chroma 16.78 has C*ab ≈ 113, while Ultramarine Blue chroma 18.16 has C*ab ≈ 45. (PDF, computed from rows) → chroma, cielab-basics
- Several high-chroma blues and violets reach their highest chroma at very low value in masstone (Ultramarine 0.32/18, Cobalt Blue Deep 2.20/15.36), while yellows do so near value 8–9. (PDF) → chroma, munsell-system

## Not covered
- Concepts requested but not covered: value-structure (Williamsburg grey match to Munsell values only inferred from the Golden Neutral Gray listing, not from the Williamsburg PDF), paints-and-pigments drying shift beyond the secondhand line above; any L*a*b* meaning or Williamsburg numbers (PDF unreadable).
- Level: intro-to-practical (manufacturer technical data, reliability B). Re-run with a local PDF-to-text tool or when justpaint.org is back to confirm title, date, illuminant/observer and L*a*b* examples.
