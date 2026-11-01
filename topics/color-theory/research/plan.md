# Build plan: color-theory
Goal: partir de cero y llegar a nivel profesional (aplicar con criterio). Enfoque: **pintura y arte** (pigmentos reales, mezcla en paleta, color y luz en el cuadro). La ciencia de la luz y la percepción se trata como base común, con la profundidad que necesita un pintor.
Content language: es

## Domains
- [x] light-and-vision — sources: cie-e-ilv, openstax-college-physics-2e, openstax-psychology-2e, openstax-physics-3, webvision, conway-2009 (abstract) · TOC only: fairchild-2013, berns-2019 · blocked: purves-2001 — status: done
- [x] color-attributes — sources: cie-e-ilv, munsell-1905, cleland-1921, newton-1704, konica-minolta-pcc, justpaint-munsell-cielab, briggs-dimensions (C, partial) · TOC/abstract only: fairchild-2013, berns-2019, cie-015-2018, okumura-2005 · blocked/secondary only: newhall-1943 — status: done
- [x] color-mixing — sources: openstax-college-physics-2e, newton-1704, munsell-1905, kubelka-munk-1931, sochorova-2021, koenderink-2018, gomez-sanchez-2014, handprint-macevoy (C), briggs-dimensions (C, partial), justpaint-munsell-cielab · abstract only: zhao-berns-2006 · TOC/secondary only: berns-2016, berns-2019, livingstone-2014 — status: done
- [x] paints-and-pigments — sources: feller-1986, feller-1994, learner-2007 (A, open), berrie-2025, golden-justpaint, mitra-astm (B), kubelka-munk-1931, sochorova-2021, handprint-macevoy (C) · TOC/abstract only: mayer-1991, berns-2016, astm-d4303, colour-index — status: done
- [ ] color-interaction — sources: albers-2013, witzel-2018, shevell-2008, livingstone-2014 — status: pending
- [ ] color-harmony — sources: schloss-palmer-2011, palmer-2013, gage-1993, cleland-1921, albers-2013, gurney-2010 — status: pending
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

## Decisions
- 2026-11-01 — `sochorova-2021` added (B, open) for pigment-mixing-behavior.
- 2026-11-01 — Itten (The Art of Color) stays out.
- 2026-11-01 — `gurney-2010` stays C; its claims are backed by A/B sources where possible.
- 2026-11-01 — Paid sources: use only what is legitimately accessible (tables of contents, previews/excerpts, publisher pages, reviews); the note says what was accessed.
- 2026-11-01 — paints-and-pigments: the four planned A sources (mayer-1991, berns-2016, astm-d4303, colour-index) are paid and only gave TOC/abstract notes, so open A/B substitutes were added: feller-1986 (NGA Artists' Pigments vol. 1), feller-1994 (Getty), learner-2007 (Getty), berrie-2025 (NGA Facture), golden-justpaint, mitra-astm.
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
