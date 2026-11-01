---
source: sochorova-2021
concepts: [subtractive-mixing, pigment-mixing-behavior, primary-colors, tints-shades-tones, target-color-mixing, transparency-opacity, limited-palette]
---

Accessed: full text (PDF, 11 pages).

## Subtractive mixing vs RGB
- RGB corresponds to additive mixing of coloured lights: blue and yellow light shone on one spot have spectra that sum linearly, giving grey; painting software built on RGB therefore mixes blue+yellow to grey (p. 1, §1) → subtractive-mixing
- Paints get colour from pigment particles that absorb and scatter light in a complex way, so the outcome of mixing is highly non-linear (p. 1, §1; Fig. 3) → pigment-mixing-behavior
- Subtractive mixing (overlaid colour filters, as in CMYK print) can make green from yellow and blue, but it models only absorption; real pigment mixtures involve absorption and scattering, so the result is darker, less saturated and of a different hue than real paint (p. 3-4, §2; Figs. 5-6) → subtractive-mixing
- A hybrid subtractive-additive model (Simonot and Hébert 2014) gives lighter results than pure subtractive but still mispredicts the hue, because it keeps the subtractive component (p. 4, §2; Fig. 6) → subtractive-mixing
- The RYB approach (Gossett and Chen 2004) interpolates 8 hand-picked colours at the corners of a cube so that blue+yellow gives green; the paper says it gives colours far from real pigment behaviour (p. 3, §2; Fig. 5) → subtractive-mixing

## Kubelka-Munk and pigment mixing behaviour
- Why blue+yellow gives green: both kinds of particles repeatedly absorb and scatter light inside the paint, leaving mostly green wavelengths to emerge; the authors liken this to subsurface scattering (p. 2, §2; Fig. 3) → pigment-mixing-behavior
- The Kubelka-Munk (K-M) model predicts mixtures from each pigment's absorption K(λ) and scattering S(λ) coefficients, which are functions of wavelength and must be measured beforehand (p. 2, §2) → pigment-mixing-behavior
- For a mix with concentrations c (non-negative, summing to 1), the mixture's K and S are the concentration-weighted linear sums of the pigments' K and S (Eq. 1, p. 2, after Duncan 1940) → pigment-mixing-behavior
- The mixture's reflectance is then computed from K_mix/S_mix with the K-M equation for a layer thick enough to hide the substrate (Eq. 2, p. 3); the colour is not the average of the pigments' colours, since the linear averaging happens in K and S, not in reflectance or RGB → pigment-mixing-behavior
- To get a screen colour, the reflectance is corrected for surface reflection (Saunderson, Eq. 6), integrated against the D65 illuminant and CIE observer functions (Eqs. 3-5), and converted to sRGB (Eq. 7) (p. 3, §2) → pigment-mixing-behavior
- K-M predictions agree well with real mixtures of Cobalt Blue and Hansa Yellow, whereas RGB, RYB, subtractive and subtractive-additive models do not (p. 3, Fig. 5; p. 4, Fig. 6) → pigment-mixing-behavior
- Because of the non-linearity, mixed colours bend away from grey and keep saturation, producing secondary hues; RGB mixing follows straight lines in RGB space, while K-M follows curved trajectories (p. 10, Fig. 14; p. 11, §6) → pigment-mixing-behavior
- Practical barrier to K-M in software: it needs per-pixel pigment concentrations or per-wavelength K/S, many more than 3 channels, and costly spectrum integrals per pixel (p. 2, §1) → pigment-mixing-behavior

## Mixing with white (tints)
- In RGB, a colour mixed with white loses saturation. Real paints momentarily gain saturation, and the hue can shift: Phthalo Blue goes from purple to turquoise as white is added (p. 1, §1; p. 3, Fig. 4) → tints-shades-tones
- K-M reproduces the saturation gain and hue shift for Quinacridone Magenta and Phthalo Blue with white; RGB gradients toward white look grey and dim (p. 3, Fig. 4; p. 8, Fig. 11; p. 9, §4) → tints-shades-tones
- The tint effect is shown as a property of the pigment ("revealing the true nature of the pigment"), not of the white alone (p. 1, §1) → tints-shades-tones
- Mixing Phthalo Blue with Titanium White reaches a turquoise so saturated that an ordinary sRGB monitor cannot display it (p. 5, §3.1) → tints-shades-tones

## Primaries and gamut
- The authors choose four primary pigments: Phthalo Blue, Quinacridone Magenta, Hansa Yellow, Titanium White, taking the suggestion from Briggs (2007) (p. 4, §3) → primary-colors
- In the implementation, these are four Golden acrylic paints (PB15:4, PY73, PR122, PW6) with K/S coefficients from the Artist Paint Spectral Database (Berns 2016), sampled at 36 wavelengths from 380 to 750 nm in 10 nm steps (p. 7, §3.2) → primary-colors
- Primaries are usually picked from yellow, red and blue categories, each in warm and cool versions with its own colour bias. With one slot reserved for white, only one warm or cool version per category fits (p. 8, §3.3) → limited-palette
- The choice of primaries bakes in mixing behaviour: with a warm blue such as Ultramarine, most blue-hued colours would inherit its warm character in mixing (p. 8, §3.3) → primary-colors
- The paper says the pigment choice is "an intimate part" of an artist's approach and that software should let users choose their own set (p. 8, §3.3) → limited-palette
- The mixtures of the four pigments do not cover the whole RGB gamut, and the paper says some RGB colours cannot be mixed from any currently known pigments (Pointer 1980); such colours can only be made by shining light (p. 2, §1; p. 5, §3) → primary-colors
- Conversely some pigment mixes lie outside sRGB (e.g. very saturated blue-white turquoise). The authors replace the primaries with optimized "surrogate pigments" so that mixtures stay in the sRGB cube; the resulting colour difference is typically near 1 ΔE00, about the just noticeable difference (p. 5-6, §3.1, Eq. 15; p. 10, §4.3, Fig. 15) → primary-colors
- A fifth pigment (e.g. Viridian Green) would make the colour-to-concentration mapping ambiguous, since green could be mixed from blue+yellow or used straight; this is why they limit to four (p. 10, §5) → limited-palette
- A four-colour landscape (dark blue, magenta, yellow, white) was painted as a performance test (p. 9, Fig. 12); orange, violet and green all appear as secondaries in the sample painting (p. 7, Fig. 9) → limited-palette
- Differences in medium: coefficients came from glossy acrylic paints; gloss makes colours richer, so the method may overestimate saturation for a duller medium such as dried watercolour (p. 8, §3.3) → pigment-mixing-behavior

## Target colour and unmixing
- Given an RGB colour, the method finds pigment concentrations c (4 values, non-negative, sum 1) by least squares, minimizing the distance between mix(c) and the target RGB (Eq. 9, p. 4, §3) → target-color-mixing
- The problem is non-linear but smooth and differentiable, so a Newton-type solver (L-BFGS-B with automatic differentiation, starting from c = 0.25 each) is used; one unmix can take up to 100 ms, so results are precomputed in a 256^3 lookup table (p. 4, §3; p. 7, §3.2) → target-color-mixing
- Different pigment combinations can give the same RGB colour, so a fixed primary set must be chosen a priori to make the decomposition unique (p. 4, §3) → target-color-mixing
- Residual: for colours that cannot be mixed from the primaries, unmix gives the closest mixable colour; the residual r = RGB − mix(unmix(RGB)) is the light that would have to be added (p. 5, §3; Eqs. 12-13) → target-color-mixing
- Accuracy: the paper says colours inside the pigment gamut are reproduced exactly ("perfect results"), and only out-of-gamut colours need non-zero residuals (p. 9, §4.2) → target-color-mixing
- Mixing two colours: unmix both, interpolate concentrations and residuals linearly, then decode (kmerp, Eqs. 10-14); a weighted average of n colours works the same way (p. 4-5, §3) → target-color-mixing
- Test with painted samples: in oil, pastel and watercolour simulations, mixed blue+yellow looks green with K-M and grey with RGB; magenta+yellow gives a strong orange with K-M, a weak one with RGB (p. 8-9, §4, Fig. 10) → target-color-mixing

## Transparency and opacity
- The method treats only homogeneous mixing of opaque paint; alpha-blended layers are treated as thick wet paint. K-M layer compositing for translucent layers, e.g. watercolour glazing, is left to future work (p. 10, §5) → transparency-opacity
- Eq. 2 assumes a paint layer so thick that it completely hides the underlying substrate (p. 3, §2) → transparency-opacity

## Not covered
- Complementary colours: not discussed.
- Shades (mixing with black) and tinting strength: not discussed.

Concepts requested but not covered: complementary-colors, tinting-strength (only indirectly via concentrations).
Level: university / specialist (computer graphics paper; useful for the physics of paint mixing, with equations needing graphics background).
