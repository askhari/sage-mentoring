---
source: kubelka-munk-1931
concepts: [pigment-mixing-behavior, subtractive-mixing, transparency-opacity, optical-mixing]
---

Accessed: full text of Westin's translation (PDF, 16 pages), "An Article on Optics of Paint Layers" (Kubelka & Munk, Aug 1931). Page numbers are those of the translation. Albedo H = fraction of incident diffuse light reflected (reflectance).

## Scope and model
- The paper aims at a first theoretical treatment of how a paint coat of given composition and thickness changes the colour of its substrate, and what thickness hides the substrate. It treats mainly matte, uncoloured (white/light grey) coats; coloured coats are only touched on; glossy coats are excluded (p. 1, Introduction) → transparency-opacity
- Model: a flat, matte layer of thickness X under diffuse light. Only two light fluxes are considered, i (downward) and j (upward), a simplification the authors admit ignores other directions (p. 1-2, §1 and footnote 3) → pigment-mixing-behavior
- Each thin slice dx removes a fixed fraction of the light passing through it: s dx by absorption and r dx by scattering. s is the absorption constant and r the scattering constant, both specific to the paint (p. 2, §1) → pigment-mixing-behavior
- Light lost by scattering from one flux is added to the opposite flux. Light lost by absorption is not added back. This gives the coupled differential equations (1) for i and j (p. 2, §1, Eq. 1) → pigment-mixing-behavior
- Absorption is what removes light permanently from the layer, while scattering only redirects it. This distinction is what the paper builds the model on, and it is the central difference from the older view that did not separate the two (p. 2, §1; footnote 6, p. 7) → subtractive-mixing
- Integrating over the full thickness gives a relation (Eq. 3) between the layer albedo H, the substrate albedo H', thickness X, r and the ratio a = (r+s)/r = 1 + s/r (p. 3, §1, Eq. 2-3) → pigment-mixing-behavior

## Infinitely thick layer
- Setting X to infinity gives H_inf = a - sqrt(a^2 - 1) = 1 + s/r - sqrt((s/r)^2 + 2 s/r) (p. 3, §2, Eq. 4) → pigment-mixing-behavior
- H_inf depends only on the ratio s/r, not on the absolute values. The look of a thick achromatic coat therefore depends only on absorption relative to scattering (p. 3, §2) → pigment-mixing-behavior
- The authors call H_inf the "intrinsic albedo" of the paint (p. 15, Conclusion 1) → pigment-mixing-behavior
- Adding a strongly absorbing pigment (lampblack) to a white paint raises s in proportion to the amount added, while scattering stays practically unchanged, provided the amounts are small enough not to alter the paint structure. So s/r is directly proportional to the amount of black added (p. 3, §2) → subtractive-mixing
- Fig. 1 plots H_inf against the lampblack amount (s/r). Pure white is extremely sensitive to tiny traces of colouring additive or impurity. The sensitivity falls markedly between technical white (about 0.8) and light grey (0.5), and rises many times over between technical white and ideal white (H_inf = 1) (p. 3-4, §2, Fig. 1) → subtractive-mixing
- The authors say the sensitivity of white to contamination explains why a near-ideal white surface is hard to make (p. 3, §2) → subtractive-mixing

## Layer of finite thickness over a substrate
- General formula (Eq. 5, p. 4, §3): the albedo H of a non-covering layer over a substrate of albedo H' depends on H_inf, on the product rX, and on H'. The layer is therefore characterised by two parameters, H_inf and rX (p. 4, §3, Eq. 5) → transparency-opacity
- r and X appear only as the product rX. This matches the practical fact that a paint can be thinned with a clear, non-scattering binder without changing the albedo of the coat, if it is applied to the same surface as before. Thinning lowers s and r in the same proportion, so s/r and H_inf stay constant. It also raises X in the same proportion that r drops, so rX stays constant (p. 5, §3) → transparency-opacity
- Special case of a black substrate (H' = 0): Eq. 6 (p. 5, §3). Fig. 2 plots H against rX for various H_inf. Albedo rises very steeply with thickness at first, then the curves bend and approach H_inf asymptotically. Darker paints approach it very fast, and paints with H_inf above 0.9 approach it increasingly slowly (p. 5-6, §3, Fig. 2) → transparency-opacity
- Because of this steep rise, Eq. 6 (black substrate) is also a good approximation for light substrates. In the worked example the error is about 3%: a coat of albedo 0.75 with H_inf = 0.8 needs only 1.03 times the thickness on a black substrate compared with a grey one of H' = 0.1 (p. 6, §3) → transparency-opacity
- Ideal white case (s = 0, H_inf = 1), Eq. 8: H = ((1-H')rX + H') / ((1-H')rX + 1). On a black substrate this reduces to H = rX/(rX+1) (Eq. 9) (p. 6, §4) → transparency-opacity
- Without scattering (r = 0, a pure glaze), the equations reduce to H = H' exp(-2sX) (Eq. 11): the light that passes through the layer is attenuated exponentially. This happens on the way down and again on the way up, which accounts for the factor 2 in the exponent (p. 6-7, §5, Eq. 10-11) → optical-mixing
- Glaze: the albedo of an infinitely thick non-scattering coat tends to 0. The paper says such a coat is the only way to get an absolutely black painted surface (p. 7, §5) → optical-mixing
- Ostwald also used an exponential law for covering, but without separating absorption from scattering (footnote 6, p. 7) → transparency-opacity
- Because the glaze's albedo is the substrate's albedo times a factor, a glaze only darkens the ground. The ground shows through scaled by exp(-2sX). The paper does not describe this as an optical mixture or discuss coloured glazes over a coloured ground (p. 7, Eq. 11) → optical-mixing
- Absolute black is harder to reach than absolute white. Scattering must be eliminated entirely, and a little brighter dust ruins the black. This follows from the steep start of the curves in Fig. 2 (p. 7, §5) → transparency-opacity

## Covering power (hiding)
- The covering power is defined as the area of black substrate covered by a unit quantity of paint. It is the reciprocal of the thickness X_D needed to cover: 1/X_D (p. 7-8, §6, Eq. 12) → transparency-opacity
- Two definitions of "covering" (p. 7, §6) → transparency-opacity
  - a) The coat on black is not distinguishable by eye from an infinitely thick coat (the Pfund Kryptometer principle).
  - b) The coat on a white substrate and on a black one cannot be told apart (the contrast-substrate or checkerboard principle).
- Under definition a), the covering condition is (H_inf - H_D)/H_D = S, where S is the visual threshold. This gives Eq. 14 for 1/X_D (p. 8, §7, Eq. 13-14) → transparency-opacity
- For ideal white (H_inf = 1) the covering power is rS (Eq. 15). For a pure glaze, definition a) gives an infinite covering power (Eq. 16). The authors call this a fundamental deficiency of the definition, so it is only usable for white and light opaque paints (p. 9, §7) → transparency-opacity
- The covering power depends very strongly on H_inf, especially close to 1. With S = 0.01 and r = 1, the quantity 1000/(rX_D) is 10 for H_inf = 1.00, 32 for 0.97, 74 for 0.90 and 124 for 0.80 (p. 9, §7, Fig. 3). A paint with H_inf = 0.8 still looks white to the eye, and ordinary zinc white has H_inf of about 0.75 (p. 9, footnotes 12-13). So a slightly less bright white hides far better (p. 9, §7) → transparency-opacity
- Covering power is also very sensitive to the eye's threshold S, which explains the large scatter of visual covering-power measurements. At H_inf = 1 it is proportional to S (p. 10, §7, Fig. 4) → transparency-opacity
- Definition b) (Eq. 17): (H_w - H_s)/H_w = S, comparing the albedo over white (H_w) and over black (H_s). This gives Eq. 18, and Eq. 19 for ideal white (p. 12, §8) → transparency-opacity
- For H'_w = H_inf, the contrast-substrate formula reduces to the Kryptometer one (p. 12, §8) → transparency-opacity
- A transparent (non-scattering) coat has no covering power under definition b). The ratio H_s/H_w equals H'_s/H'_w for any thickness (Eq. 20), so it can never reach 1 - S (p. 13, §8, Eq. 20) → transparency-opacity
- Definition b) works for all coats, including s = 0 and r = 0, without nonsensical values (p. 13, §8) → transparency-opacity
- Apparent hiding by a very dark glaze comes from the failure of Fechner's law at low light levels. It depends on the absolute light intensity, so it is not real covering (footnote 15, p. 13) → transparency-opacity
- The contrast-substrate covering power depends strongly on the albedo of the white substrate, especially for bright paints. The dependence fades for darker paints (p. 13-14, §8, Fig. 5 and table) → transparency-opacity

## Coloured coatings
- The achromatic relations carry over to coloured paint by applying them wavelength by wavelength. Each wavelength has its own H, H_inf and H'. The scattering constant r is taken as roughly independent of wavelength (p. 14, §9) → pigment-mixing-behavior
- r depends mainly on the relative refractive index of pigment and binder (for normal pigment particle size) (footnote 16, p. 14) → pigment-mixing-behavior
- It generally suffices to compute at 5 to 7 wavelengths because spectra are smooth (p. 14, §9) → pigment-mixing-behavior
- For a coloured paint over an achromatic ground, a simplification is possible using only two wavelength groups. The authors say quantitative covering power for coloured paint is still open (p. 15, §9) → transparency-opacity

## What the paper does NOT contain
- ⚠️ No treatment of mixtures of different pigments. There is no statement that the coefficients s and r of a mixture are the concentration-weighted sums of the components' coefficients. The only mixing remark is the qualitative one for lampblack in white (s/r proportional to the amount of black, p. 3, §2). The additivity of coefficients, often attributed to Kubelka-Munk theory, must come from a later source → pigment-mixing-behavior
- No discussion of subtractive mixing of coloured pigments (for example yellow plus blue), and no discussion of optical mixing (dots or juxtaposition) → subtractive-mixing
- The text does not use the later K/S (absorption/scattering) notation or the form (1-R)^2/2R. It uses H_inf, s and r. The "reflection constant" r and the "scattering constant" r are the same quantity (p. 4 and p. 15) → pigment-mixing-behavior
- ⚠️ Translation points: the Conclusion (p. 15) labels the main formula "(6)", but it is the same general formula as Eq. 5. The translator corrected two algebra slips of the original (p. 16) → pigment-mixing-behavior

Not covered: additivity of coefficients for pigment mixtures (explicitly absent); optical mixing as a perceptual effect; coloured glazes (only the achromatic non-scattering case, Eq. 11).
Level: specialist / university (original physics-of-paint research paper, in translation; the equations need calculus).
