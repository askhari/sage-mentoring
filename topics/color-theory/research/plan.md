# Build plan: color-theory
Goal: partir de cero y llegar a nivel profesional (aplicar con criterio). Enfoque: **pintura y arte** (pigmentos reales, mezcla en paleta, color y luz en el cuadro). La ciencia de la luz y la percepción se trata como base común, con la profundidad que necesita un pintor.
Content language: es

## Domains
- [x] light-and-vision — sources: cie-e-ilv, openstax-college-physics-2e, openstax-psychology-2e, openstax-physics-3, webvision, conway-2009 (abstract) · TOC only: fairchild-2013, berns-2019 · blocked: purves-2001 — status: done
- [x] color-attributes — sources: cie-e-ilv, munsell-1905, cleland-1921, newton-1704, konica-minolta-pcc, justpaint-munsell-cielab, briggs-dimensions (C, partial) · TOC/abstract only: fairchild-2013, berns-2019, cie-015-2018, okumura-2005 · blocked/secondary only: newhall-1943 — status: done
- [x] color-mixing — sources: openstax-college-physics-2e, newton-1704, munsell-1905, kubelka-munk-1931, sochorova-2021, koenderink-2018, gomez-sanchez-2014, handprint-macevoy (C), briggs-dimensions (C, partial), justpaint-munsell-cielab · abstract only: zhao-berns-2006 · TOC/secondary only: berns-2016, berns-2019, livingstone-2014 — status: done
- [x] paints-and-pigments — sources: feller-1986, feller-1994, learner-2007 (A, open), berrie-2025, golden-justpaint, mitra-astm (B), kubelka-munk-1931, sochorova-2021, handprint-macevoy (C) · TOC/abstract only: mayer-1991, berns-2016, astm-d4303, colour-index — status: done
- [x] color-interaction — sources: witzel-2018, chevreul-1890 (A, public domain), otazu-2022, regier-kay-cook-2005, zeki-2017, webvision, koenderink-2018, cie-e-ilv, gomez-sanchez-2014, openstax-psychology-2e, openstax-college-physics-2e, livingstone-2014 (secondary only), conway-livingstone-2007 · TOC/abstract only: albers-2013, shevell-2008, conway-2009 — status: done
- [x] color-harmony — sources: schloss-palmer-2011, palmer-2013 (authors' copy), palmer-schloss-2010, ho-2014, jonauskaite-2020 (B, open), cleland-1921, munsell-1905, chevreul-1890, gurney-2010 (C, blog), witzel-2018, livingstone-2014 (secondary only) · TOC only: gage-1993, albers-2013 — status: done
- [ ] color-in-painting — sources: livingstone-2014, conway-livingstone-2007, berns-2016, openstax-physics-3, gurney-2010 — status: pending

Concept titles (es): `i18n/es/concepts.yaml`.

## Doubts to resolve
- Years of `handprint-macevoy` and `briggs-dimensions` (websites) are approximate; the researcher must confirm them.
- `purves-2001`: NCBI Bookshelf returns a CAPTCHA to the fetcher — unusable unless read manually. Candidate for removal.

- `briggs-dimensions`: www.huevaluechroma.com fails TLS for the fetcher; the note rests on search excerpts (year still unconfirmed). Re-read in a browser before relying on it in color-mixing.
- `justpaint-munsell-cielab`: the explanatory justpaint.org article was down; method details (film thickness, drying shift, illuminant/observer) are unverified. The Williamsburg data PDF was read directly.
- No open source found for ΔE tolerance thresholds or for the 1943 Munsell renotation (newhall-1943 unreachable).
- `berns-2016` (TOC only) and `livingstone-2014` (author's article, a review and a lecture abstract only): both are planned for later domains (paints-and-pigments, color-interaction, color-in-painting). Find open A/B substitutes or read them from a library copy before relying on them.
- color-mixing gaps: no A/B source defines tint/shade/tone; no measured data on coloured glazes; oil/acrylic mixing advice rests on MacEvoy (watercolour, C). `zhao-berns-2006` PDF host (art-si.org) does not resolve.

- paints-and-pigments gaps: no A/B source defines tinting strength numerically (Golden describes its tint test two ways: equal parts white vs 1:10); "undertone" has two meanings (thin film, Golden; tint, MacEvoy) and no A/B source settles it; the effect of white pigments on fading (Just Paint "ASTM lightfastness testing for oil paints") could not be read (justpaint.org 404, Wayback copy failed); ASTM category II is "Good" (Golden) vs "Very Good" (MITRA); the ASTM–blue wool correspondence in the lightfastness-scales diagram is MacEvoy's (C).
- `colour-index`: explanatory pages returned HTTP 500/404; retry colour-index.com/ci-explained to replace the search-summary claims in colour-index-names.
- `astm-d4303`: the ASTM store forbids AI use of its content; categories and ΔE bands come from mitra-astm and golden-justpaint instead.
- color-interaction gaps: no open source on the modern mechanism of simultaneous contrast (only a remark in Webvision/Gouras, read through a summarizer); no source gives painters a rule for stripe width or viewing distance in assimilation; Albers' Interaction of Color is only known through TOC and descriptions; Zeki-2017's Discussion contradicts its Results on colour labels (content uses Results); the Webvision "Color Vision" (Gouras) bullets come from summarizer output, re-check wording if quoted.
- `conway-livingstone-2007` and `chevreul-1890` notes already include claims for color-in-painting (shadows, local vs perceived colour) and color-harmony (harmonies of analogy/contrast); reuse them.
- color-harmony gaps: no source defines "tonal key" or gives numeric accent proportions (e.g. 60-30-10); "warm advances / cool recedes" has no source; warm/cool association measured only for red vs blue (ho-2014, small samples); harmony data are two-colour squares on a monitor from Berkeley students (no triads, paint, unequal areas or non-Western samples); Cleland's value × chroma area rule is untested. gage-1993 gave TOC only. Several gurney-2010 claims (gamut-mask accents, unmixable colours inside the triangle, Speed's view) rest on search summaries of blog posts.
- Forward links: color-schemes → color-in-painting/gamut-planning and color-temperature → color-in-painting/light-and-shadow-color will resolve when color-in-painting is written (validator warns until then). The gurney-2010 note already covers the color-in-painting concepts; reuse it.

## Decisions
- 2026-11-01 — `sochorova-2021` added (B, open) for pigment-mixing-behavior.
- 2026-11-01 — Itten (The Art of Color) stays out.
- 2026-11-01 — `gurney-2010` stays C; its claims are backed by A/B sources where possible.
- 2026-11-01 — Paid sources: use only what is legitimately accessible (tables of contents, previews/excerpts, publisher pages, reviews); the note says what was accessed.
- 2026-11-01 — color-interaction: albers-2013 and shevell-2008 gave only TOC/abstract notes, so open substitutes were added: chevreul-1890 (A, public domain; cite by §), otazu-2022, regier-kay-cook-2005, zeki-2017 (B). `livingstone-hubel-1987` was dropped (PMC has only the abstract; jneurosci.org blocks scripts); `foster-2011` was not added (PhilArchive behind a Cloudflare check, author page down).
- 2026-11-01 — paints-and-pigments: the four planned A sources (mayer-1991, berns-2016, astm-d4303, colour-index) are paid and only gave TOC/abstract notes, so open A/B substitutes were added: feller-1986 (NGA Artists' Pigments vol. 1), feller-1994 (Getty), learner-2007 (Getty), berrie-2025 (NGA Facture), golden-justpaint, mitra-astm.
- 2026-11-01 — color-harmony: open B sources added for the thin concepts: palmer-schloss-2010 (colour preference, ecological valence), ho-2014 (warm/cool), jonauskaite-2020 (colour–emotion, 30 nations). palmer-2013 read from the authors' copy on the Palmer lab page; schloss-palmer-2011 and ho-2014 through the Europe PMC open-access XML (no PMC access).
- 2026-11-01 — `konica-minolta-pcc` B → C (instrument maker's technical guide, not peer-reviewed); `justpaint-munsell-cielab` B → A (manufacturer's official data on its own paints; cite only for those data).

## Log
- 2026-11-01 — map created (7 domains, 49 concepts, 24 sources)
- 2026-11-01 — map approved by the user (+ sochorova-2021 → 25 sources)
- 2026-11-01 — light-and-vision research: 9 notes. Paid books (fairchild-2013, berns-2019) only give TOC-level notes; added open A sources cie-e-ilv, openstax-college-physics-2e, openstax-psychology-2e (→ 28 sources).
- 2026-11-01 — light-and-vision done: 8 concepts, 56 questions (L1 12, L2 27, L3 17), 2 diagrams (visible-spectrum, cone-sensitivity), 27 [unverified] (mostly painter-practice inferences, to revisit with the painting sources)
- 2026-11-01 — color-attributes research: 8 new notes; added open sources munsell-1905, newton-1704 (A, public domain), konica-minolta-pcc, justpaint-munsell-cielab (B), okumura-2005 (abstract only) (→ 33 sources). cleland-1921 URL moved to archive.org (munsell.com redirects to pantone.com). cie-015-2018 abstract only; newhall-1943 blocked.
- 2026-11-01 — color-attributes done: 8 concepts, 52 questions (L1 12, L2 19, L3 21), 3 diagrams (hue-circle, color-wheels-comparison, munsell-hue-page; new CIELAB and Munsell-hue helpers in colormath.py), 13 [unverified]
- 2026-11-01 — color-mixing research: 8 new notes + openstax-college-physics-2e extended; added open sources kubelka-munk-1931 (A, Westin translation), koenderink-2018, gomez-sanchez-2014 (B), zhao-berns-2006 (B, abstract only) (→ 37 sources). PDFs read via new tools/pdf_to_text.py (WebFetch could not extract them).
- 2026-11-01 — color-mixing done: 8 concepts, 47 questions (L1 9, L2 19, L3 19), 4 diagrams (additive-vs-subtractive-overlaps, complementary-mix-to-grey, tint-ladder, blue-yellow-mixing; Kubelka-Munk helpers in colormath.py), 7 [unverified]
- 2026-11-01 — paints-and-pigments research: 9 new notes (feller-1986, feller-1994, learner-2007, berrie-2025, golden-justpaint, mitra-astm, mayer-1991 TOC, astm-d4303 store page, colour-index home page) + handprint-macevoy extended (→ 43 sources). NGA PDF found through the built-in browser (WebFetch 403); Just Paint articles through the Wayback Machine.
- 2026-11-01 — paints-and-pigments done: 7 concepts, 53 questions (L1 10, L2 27, L3 16), 3 diagrams (opacity-black-stripe, masstone-tint-thin-film, lightfastness-scales; two-constant Kubelka-Munk layer helpers in colormath.py), 6 [unverified]
- 2026-11-01 — color-interaction research: 7 new notes (witzel-2018, chevreul-1890, otazu-2022, regier-kay-cook-2005, zeki-2017, conway-livingstone-2007, albers-2013 TOC, shevell-2008 abstract) + webvision extended (→ 47 sources). PMC pages gave a CAPTCHA to the fetcher; two short PMC papers were read in the built-in browser, Zeki through the Europe PMC open-access XML.
- 2026-11-01 — color-interaction done: 6 concepts, 47 questions (L1 4, L2 25, L3 18), 3 diagrams (simultaneous-contrast, assimilation-stripes, equiluminance), 12 [unverified] (11 in content, 1 in a caption)
- 2026-11-01 — color-harmony research: 7 new notes (schloss-palmer-2011, palmer-2013, palmer-schloss-2010, ho-2014, jonauskaite-2020, gurney-2010 from the author's blog, gage-1993 TOC) (→ 50 sources). Reused cleland-1921, munsell-1905, chevreul-1890, albers-2013.
- 2026-11-01 — color-harmony done: 6 concepts, 60 questions (L1 9, L2 28, L3 23), 4 diagrams (classic-schemes-hue-circle, warm-cool-hue-circle, value-structure-thumbnails, cleland-area-balance; new hex→Lab, greyscale, approximate-Munsell and hue-ring helpers in colormath.py), 5 [unverified]
