---
source: konica-minolta-pcc
concepts: [hue, value, chroma, saturation-and-colorfulness, color-wheel, munsell-system, cielab-basics, metamerism]
---

Accessed: official online pages at konicaminolta.com/instruments/knowledge/color/ : part1/03-13, part2/01, part3/01, part4/01, part5/01-02 (index only for page titles). No edition stated; footer reads "©2011- Konica Minolta, Inc.". Page references are "Part I-NN" (NN of 13). Figures are images and were not readable; only text was used. Pages were read through an automatic summarizer, so wording is paraphrase, not verified verbatim.

## Attributes and colour solid (Part I-3 to I-5)
- Two red balls that look alike can differ: one is brighter, one more vivid. Colours are therefore classified by hue, lightness and saturation (Part I-3) → hue, value, saturation-and-colorfulness
- Hue is the classification into colour names such as red, yellow, blue. Mixing hues gives intermediate ones (yellow + red = orange, yellow + green = yellow-green, blue + green = blue-green) (Part I-4) → hue
- Lightness is how bright or dark a colour is, and it can be assessed independently of hue. Examples: lemon yellow is lighter than grapefruit yellow and than cherry red (Part I-4) → value
- Saturation is how vivid or dull a colour is, separate from hue and lightness. Examples: lemon yellow is vivid, pear yellow is dull (Part I-4) → saturation-and-colorfulness
- In the cross-section (Fig. 2), lightness grows upward, and saturation grows horizontally from the centre: dull near the centre, vivid farther out (Part I-4) → value, saturation-and-colorfulness
- The colour wheel (Fig. 1) arranges the continuum of hues in a circle. The guide uses "color wheel" and does not use "hue circle" (Part I-4) → color-wheel, hue
- Figure 3 gives common adjectives for lightness and saturation levels (content is in the image, not the text) (Part I-4) → value, saturation-and-colorfulness
- Combining the three attributes gives a 3D colour solid: hue is the outer rim, lightness the central vertical axis, saturation the spokes outward from the centre (Part I-5) → hue, value, saturation-and-colorfulness
- The solid of real colours is irregular: saturation steps differ in size according to hue and lightness. The simple model still shows how the three relate (Part I-5) → saturation-and-colorfulness, chroma
- The guide does not distinguish saturation from chroma or from colorfulness; the terms "colorfulness" and CIE definitions do not appear. ⚠️ Treat as a popular, simplified treatment, not a CIE-precise one (Part I-4, I-6) → saturation-and-colorfulness

## Munsell (Part I-6)
- In the Munsell system, colours are graded visually against paper colour chips (Munsell Color Charts) on three scales: Munsell Hue (H), Munsell Value (V), Munsell Chroma (C) (Part I-6) → munsell-system, hue, value, chroma
- Each colour is written as H V/C, from visual evaluation against the charts (Part I-6) → munsell-system
- The page treats "saturation" and "chroma" as names for the same third attribute (Part I-6) → chroma, saturation-and-colorfulness
- The page presents Munsell as a colour space, i.e. a way to express an object's or light's colour with notation such as numbers (footnote). It mentions CIE Yxy (1931, from XYZ) and CIE L*a*b* (1976, for more uniform differences) as the other systems (Part I-6) → munsell-system, cielab-basics
- No sample Munsell notation or hue-letter scheme is given in the text (Part I-6) → munsell-system

## CIE Yxy and why CIELAB (Part I-7, I-9)
- XYZ tristimulus values and the Yxy space are the foundation of present CIE colour spaces. XYZ derives from three-component colour vision (receptors for red, green, blue) and is computed with the Standard Observer colour matching functions (Part I-9) → cielab-basics
- Worked Yxy example (apple): x = 0.4832, y = 0.3045, Y = 13.37, read as 13.37 % reflectance (Part I-9) → cielab-basics
- CIELAB was defined by the CIE in 1976 as a uniform colour space, to fix the problem that equal distances on the Yxy x,y diagram did not match equal perceived differences (Part I-7) → cielab-basics
- L*a*b* is described as one of the most popular spaces for measuring object colour, used in many fields (Part I-7) → cielab-basics

## CIELAB and L*C*h (Part I-7, I-8)
- L* is lightness. a* and b* are chromaticity coordinates: +a* red, -a* green, +b* yellow, -b* blue. The centre is achromatic and saturation increases as a*, b* move away from it (Part I-7) → cielab-basics, value, saturation-and-colorfulness
- The a*b* diagram (Fig. 6) is a horizontal cut through the solid at constant L*. A vertical cut gives chromaticity vs lightness (Fig. 7) (Part I-7) → cielab-basics
- Apple example: a* = +47.63, b* = +14.12 plotted gives the apple's chromaticity (Part I-7) → cielab-basics
- L*C*h uses the same diagram with cylindrical rather than rectangular coordinates. L* is the same lightness (Part I-8) → cielab-basics
- C* is chroma: 0 at the centre and increasing with distance from the centre (Part I-8) → cielab-basics, chroma
- h is the hue angle in degrees from the +a* axis: 0° = +a* (red), 90° = +b* (yellow), 180° = -a* (green), 270° = -b* (blue) (Part I-8) → cielab-basics, hue
- The text of Part I-8 gives no explicit formulas for C* and h (⚠️ the standard C* = sqrt(a*²+b*²) and h = atan2(b*, a*) are not on these pages) → cielab-basics
- Hunter Lab is mentioned as an earlier, more visually uniform alternative to Yxy, still used e.g. in the US paint industry (Part I-8) → cielab-basics

## Colour difference (Part I-11, I-12)
- Standard (apple A): L* 43.31, a* +47.63, b* +14.12. Sample (apple B): L* 47.34, a* +44.58, b* +15.16 (Part I-11) → cielab-basics
- Differences: ΔL* = +4.03, Δa* = -3.05, Δb* = +1.04. "Δ" means difference (Part I-11) → cielab-basics
- ΔE*ab = sqrt(ΔL*² + Δa*² + Δb*²); here 5.16. It gives the size of the total difference, not its direction (Part I-11) → cielab-basics
- In L*C*h the same pair gives ΔL* = +4.03, ΔC* = -2.59 (B less saturated) and ΔH* = +1.92 (B shifted toward +b*, more yellow) (Part I-11) → cielab-basics, chroma, hue
- ΔH* = sqrt(ΔE*ab² - ΔL*² - ΔC*²) (Part I-11) → cielab-basics
- Words give the direction of a lightness or chroma difference but not its degree without a modifier. B is "paler" than A, more exactly "slightly paler" because ΔC* is small (Part I-11) → cielab-basics, value, chroma
- Two colours that look the same to the eye can still show small numeric differences. Examples: ΔE*ab 0.77 (ΔL* -0.32, Δa* -0.01, Δb* -0.70), 0.18, 0.15. The text gives no tolerance thresholds (Part I-12) → cielab-basics
- A parts-supplier case study (plastic parts, inspectors vs handheld colorimeters) argues for numeric colour control (Part I-12) → cielab-basics
- Part I-10: the eye cannot measure colour accurately and perception shifts with background or light source. A colorimeter measures always with the same source and geometry, giving numbers per international standards (Part I-10) → illuminant-color, cielab-basics

## Limits of CIELAB, observers, illuminants (later parts)
- ΔE*ab treats the tolerance as a perfect circle for all saturations and hues, but human discrimination is elliptical, so colorimeter values can disagree with visual judgement (Part V-2) → cielab-basics
- Cited facts on discrimination: sensitivity to differences is low at high saturation, varies with hue, and lightness sensitivity peaks near L* 50 (Part V-2) → cielab-basics
- Colour needs three conditions: light, an object and vision. In darkness there is no colour (Part II-1) → illuminant-color
- Instruments can calculate data under CIE Standard Illuminant C or D65. The instrument "observer" approximates the CIE 1931 Standard Observer (Part I-13) → illuminant-color
- Object colour depends on viewing conditions and on observation and illumination angle; optical geometries 45/0, 0/45, d/0 and 0/d are described (Part III-1) → illuminant-color
- Two observers: 2° Standard Observer (1931) for fields of 1° to 4°, 10° Supplementary Standard Observer (1964) for larger than 4° (Part IV-1) → illuminant-color
- Metamerism appears only in passing: colorimeters are said to be unsuited to analyses such as metamerism, while spectrophotometers (spectral reflectance per wavelength) are the instrument for it. It is not explained (Part III-1) → metamerism

## Not covered / level
- Not covered: hue circle as a distinct concept, colour solid detail beyond the above, Munsell notation examples, formulas for C* and h, ΔE thresholds, illuminant definition, metamerism explanation.
- Level: intro to lower university, instrument-maker's technical guide (reliability B); much of the content lives in figures that were not readable.
