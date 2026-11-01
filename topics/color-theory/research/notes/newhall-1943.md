---
source: newhall-1943
concepts: [munsell-system]
---

Accessed: NOT the report itself. The Optica page (opg.optica.org, via the DOI) timed out or reset on three tries, and the RIT Munsell renotation page failed with a certificate error. The only things read were secondary descriptions: Wikipedia "Munsell color system", the R package munsellinterpol docs (Munsell2xy page, rdrr.io), and search-engine snippets of the CRAN, BabelColor and RIT dataset pages. Each claim below says what those pages say about the report, not what the report says. The report's own text (reasons, smoothing, value function, chroma) could not be checked.

- Bibliographic data: JOSA 33(7), July 1943, pp. 385-418, by Newhall, Nickerson and Judd for the OSA Subcommittee on the Spacing of the Munsell Colors (BabelColor listing, via search snippet) → munsell-system
- The OSA ran an extensive series of experiments in the 1940s, and their results gave the notations of the modern Munsell Book of Color; the earlier 1905 Atlas and the 1929 book were imperfect physical representations of Munsell's theory (Wikipedia, Munsell color system, history section) → munsell-system
- The renotation made small adjustments to the aim points of the Munsell samples to improve spacing uniformity (munsellinterpol docs and BabelColor, via search snippets) → munsell-system
- The 1943 article tabulates colors as CIE xyY, with x and y for Illuminant C (munsellinterpol, Munsell2xy page) → munsell-system
- RIT's file real.dat holds the colors printed in the 1943 article, which lie within the MacAdam limits. The file all.dat (4995 colors) adds 1906 extrapolated colors to the 3089 "real" ones (munsellinterpol docs; search summary of the RIT data page) → munsell-system
- The munsellinterpol author credits the extrapolated colors to a later (1958 NBS) effort and says it is not in the 1943 report. ⚠️ Treat the 1958 attribution as the package author's belief, not verified → munsell-system
- The RIT xyY data are scaled by a factor 1/0.975 (search summary of the RIT data page; ⚠️ not confirmed on the page itself) → munsell-system
- In the munsellinterpol package, luminance factor Y is a function of Value alone, but the formula is not given on the page read (Munsell2xy docs) → munsell-system
- The renotation covers only some points of Munsell space, so a given color needs interpolation (Wikipedia, Munsell color system) → munsell-system

Not covered (needs the report or the RIT page): reasons for respacing in the report's own words, details of the visual scaling experiments, the smoothing procedure, the value-to-luminous-reflectance function, and chroma.
Level: specialist, primary paper (classic colorimetry). Paid, so only secondary descriptions were reachable.
