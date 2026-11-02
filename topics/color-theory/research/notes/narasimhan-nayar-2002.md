---
source: narasimhan-nayar-2002
concepts: [atmospheric-perspective, light-and-shadow-color, colored-light-unity]
---

Accessed: full text of the authors' copy (pp. 233-254, extracted text). Computer-vision paper (reliability B); physics is summarized from McCartney (1975) and Middleton (1952). Page numbers are the journal pages printed in the PDF.

## Particles and weather
- Light interacts with the atmosphere by scattering, absorption and emission; scattering by suspended particles is the one that matters here (pp. 233-234, §1) → atmospheric-perspective
- Weather types differ mainly in particle type, size and concentration. Air molecules: radius about 10^-4 µm; haze aerosols: about 10^-2 to 1 µm; fog droplets: about 1-10 µm (Table 1, p. 234, §2) → atmospheric-perspective
- Air molecules are very small relative to visible wavelengths, so pure-air scattering is minimal; the paper calls this a "clear day" (p. 234, §2) → atmospheric-perspective
- Haze is aerosol (volcanic ash, foliage exudates, combustion products, sea salt), larger than air molecules but smaller than fog droplets; it tends to give a grey or bluish hue and reduces visibility (p. 234, §2) → atmospheric-perspective
- Fog forms when humidity reaches saturation and haze nuclei grow into droplets; more humidity can turn haze into fog, with "mist" as the gradual in-between state. Perceptible haze extends several kilometres up, fog only a few hundred feet; practically, fog differs from haze by greatly reduced visibility (p. 235, §2) → atmospheric-perspective
- A cloud is the same as fog but at altitude (p. 235, §2) → atmospheric-perspective
- Scattering pattern depends on particle size relative to wavelength λ: about λ/10 scatters roughly equally forward and backward; about λ/4 scatters more forward; larger than λ scatters almost entirely forward (p. 235, §3, Fig. 1) → atmospheric-perspective
- Multiple scattering makes scattering smoother and less directional, blurs images, and in heavy fog can break the simple exponential law; the paper does not model it (pp. 235-236, §3, §3.1) → atmospheric-perspective

## Attenuation (the object's own light fades with distance)
- Attenuation makes the radiance of a scene point fall as its distance from the observer increases (p. 236, §3.1) → atmospheric-perspective
- Eq. 3-4 (Bouguer's law) in words: in each thin slice of air a fixed fraction of the light is scattered out, so the light left after distance d equals the initial light times e^(-βd): exponential decay with distance. β is the total scattering coefficient (depends on wavelength and particle concentration); βd is the "optical thickness" (p. 236, §3.1) → atmospheric-perspective
- Allard's law (Eq. 5) adds the inverse-square fall-off of a point source: irradiance = I0 · e^(-βd) / d² (p. 236, §3.1) → atmospheric-perspective
- Assumptions of the attenuation model: β constant along horizontal paths (homogeneous atmosphere); observer near ground level looking at objects near ground level, not at the sky; light scattered out of the line of sight does not re-enter it; forward-scattered light toward the observer is ignored as small (pp. 236, §3, §3.1) → atmospheric-perspective
- For visible light, β follows a power law of wavelength, β ∝ λ^(-γ) with γ between 0 and 4, analogous to Rayleigh's law for small air particles (Eq. 15, p. 238, §4) → atmospheric-perspective
- For fog and dense haze γ is about 0, so β barely changes with wavelength; only certain metropolitan haze types are excepted. MODTRAN simulations (d = 0.2 km, view 5° above ground) show transmittance nearly flat across 0.4-0.7 µm (p. 238, §4; pp. 242-243, §6, Fig. 9) → atmospheric-perspective
- Hence for fog and dense haze the hue of the directly transmitted light is assumed independent of the object's depth; only its brightness drops (p. 241, §6) → atmospheric-perspective
- ⚠️ The paper does not state that clean-air distance looks blue because of Rayleigh scattering. It gives only the Rayleigh analogy (γ up to 4) and says fog/dense haze are wavelength-neutral. Blue of distant mountains must be sourced elsewhere → atmospheric-perspective

## Airlight (the air adds light, so distant things move toward the horizon colour)
- The atmosphere also acts as a light source, airlight (Koschmieder, 1924): environmental light (direct sunlight, diffuse skylight, ground-reflected light) scattered toward the observer by the particles (pp. 236-237, §3.2) → atmospheric-perspective
- Attenuation makes brightness decrease with path length while airlight makes it increase, so the apparent brightness of a distant point rises with depth (p. 237, §3.2) → atmospheric-perspective
- Eq. 10-11 in words: airlight radiance along a path of length d = horizon radiance × (1 − e^(-βd)). It is zero at d = 0 and tends to the horizon radiance as d goes to infinity; the horizon radiance is observable (p. 237, §3.2) → atmospheric-perspective
- Assumptions of the airlight model: constant illumination along the line of sight, uniformly lit atmosphere (p. 237, §3.2; p. 243, §7) → atmospheric-perspective
- Airlight hue depends on the particle-size distribution and tends to be grey or light blue for haze and fog (p. 241, §6) → atmospheric-perspective
- Full "dichromatic atmospheric scattering" model (Eq. 25): colour reaching the eye = direct transmission (object colour × e^(-βd), faded) + airlight (horizon colour × (1 − e^(-βd))). The observed colour is a linear mix of the object-colour direction and the fog/haze-colour direction; as d grows the first weight shrinks and the second approaches full (pp. 241-242, §6, Fig. 8) → atmospheric-perspective
- The linear mix assumes the illumination hue is the same in clear and bad weather (intensity may differ). It fitted real fog and haze photos well (small mean angular error over about half a million pixels), all under overcast sky (pp. 242-243, §6, Figs. 10, 17) → atmospheric-perspective
- In dense fog with near objects, or mild fog with distant objects, the object's own brightness is heavily attenuated and airlight is the main contribution; airlight also dominates in dense haze around noon (p. 239, §5) → atmospheric-perspective
- Windows of dark interiors have almost no colour of their own, so they show nearly pure airlight (p. 249, §11); sky and black points take on the airlight colour on a bad-weather day (note 2, p. 253) → atmospheric-perspective

## Contrast and visibility
- Fog reduces visibility far more than haze (p. 235, §2); on a clear day sources are seen in their brightest, clearest form (p. 238, §4) → atmospheric-perspective
- Weather degradation depends on each point's depth, so simple global contrast enhancement (histogram equalization, contrast stretching) does not restore it (p. 234, §1) → atmospheric-perspective
- ⚠️ No explicit formula for contrast loss versus distance or for visual range appears; the paper only gives the airlight equation attributed to Koschmieder → atmospheric-perspective

## Sky light, overcast, sun
- Environmental illumination along a path can include direct sunlight, diffuse skylight and ground-reflected light (p. 237, §3.2) → light-and-shadow-color
- Fog is usually accompanied by overcast sky, so the paper uses the overcast-sky model (Moon and Spencer; Gordon and Church): sky radiance at elevation angle θ is proportional to (1 + 2cosθ), measured from the zenith (p. 237, §3.3; p. 252, Appendix A) → light-and-shadow-color
- That model also assumes each scene point's irradiance is dominated by the sky and light from other scene points is negligible (p. 237, §3.3) → light-and-shadow-color
- With strong directional sunlight, scattering is greater in some directions, so airlight depends on viewing direction; the paper's workaround is to use the horizon brightness nearest the scene point (p. 239, §5) → colored-light-unity
- Spectral composition of daylight on different overcast days is taken as "more or less identical"; differences between recovered and actual clear-day colours are attributed to different spectral distributions of illumination on different days (Fig. 12 caption, p. 244; Fig. 19 caption, p. 250) → colored-light-unity
- The airlight colour is obtained by averaging a patch of sky in the bad-weather image; the model requires object colour and airlight to share the same illumination hue (p. 243, §6-§7) → colored-light-unity
- A white patch in the scene can be used to colour-correct when the illumination spectrum differs between two images (p. 243, §7) → colored-light-unity
- Parts of the atmosphere receive less skylight because the scene occludes part of the sky (smaller "sky aperture", more so near the base of buildings and with distance), so the uniform-lighting assumption causes errors (p. 243, §7; Appendix B, pp. 252-253) → light-and-shadow-color
- Atmospheric optics is named as the source of sunrise/sunset colours and the blue of the clear sky, but not explained (p. 233, §1) → light-and-shadow-color

## Limits and other uses
- Models assume homogeneous atmosphere, horizontal near-ground paths, overcast sky, no darkening of wet materials (note 1, p. 253), no blur from multiple scattering, and exclude rain and snow (pp. 235-236, §2-§3.1) → atmospheric-perspective
- The rest of the paper (pp. 238-251) develops computer-vision algorithms to recover depth and "clear day" colours from one or two foggy/hazy photos; not relevant to painting → atmospheric-perspective

## Not covered
- Requested but not covered: Rayleigh blue of distant clear-air scenes, an explicit contrast-loss law and visual range, sun colour, clear vs overcast shadow colour (only the (1+2cosθ) sky model).
- Level: specialist (computer vision / atmospheric optics); equations explained in words above.
