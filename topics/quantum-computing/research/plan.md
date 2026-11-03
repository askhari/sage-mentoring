# Build plan: quantum-computing
Goal: partir de cero (programa; álgebra lineal oxidada) y llegar a nivel profesional. Enfoque principal: **programación y algoritmos** (qubits, circuitos, algoritmos, práctica con Qiskit, corrección de errores), con la **base matemática y física** que los sostiene y bastante peso en **cómo se construyen los ordenadores cuánticos actuales** con distintas tecnologías (superconductores, iones, átomos neutros, espines, fotones, topológicos).
Content language: es

## Domains
- [x] math-foundations — sources: axler-2024, watrous-2025 (L1–L3 only; no eigenvalue material there), de-wolf-2026 (App. A–B, ch. 1) — status: done
- [x] quantum-mechanics — sources: zwiebach-mit-8-04 (LN1–9), zwiebach-mit-8-05 (ch. 2, 6), openstax-physics-3 (§6–7), preskill-ph219 (ch. 2–3), watrous-2025 (Unit III), zurek-2003 · not researched: nielsen-chuang-2010 (TOC only) — status: done
- [x] qubits-and-circuits — sources: watrous-2025 (Unit I L1–L4, L6.2, L9.3), de-wolf-2026 (ch. 1–2, 13, 17), aaronson-2018 (lec. 3–5, 7, 9–10, 13–14, 16; prose only, PDF extraction lost formulas), preskill-ph219 (ch. 4 [2001], ch. 5 [2015]), hensen-2015 — status: done
- [ ] quantum-algorithms — sources: watrous-2025, de-wolf-2026, childs-qa, shor-mit-2022, aaronson-2018, shor-1997, grover-1996, nist-fips-203, gidney-2025 — status: pending
- [ ] qiskit-programming — sources: qiskit-docs, ibm-quantum-learning, preskill-2018, cerezo-2021, peruzzo-2014, farhi-2014 — status: pending
- [ ] quantum-hardware — sources: divincenzo-2000, krantz-2019, kjaergaard-2020, bruzewicz-2019, henriet-2020, burkard-2023, slussarenko-2019, bartolucci-2023, nayak-2008, arute-2019, eisert-2025 (unconfirmed) — status: pending
- [ ] error-correction — sources: watrous-2025, de-wolf-2026, preskill-ph219, fowler-2012, google-2025, bluvstein-2024, gidney-2025 — status: pending

Concept titles (es): `i18n/es/concepts.yaml`.

## Doubts to resolve
- Hardware sources are mostly 2019–2020 reviews; the current state (2025–2026) rests on a few papers and the unconfirmed `eisert-2025`. Look for one more recent open A/B review per platform during the domain's research (especially trapped ions, neutral atoms, topological after the 2025 Microsoft claims).
- Several hardware papers are written by companies (Pasqal, PsiQuantum, QuEra, Google); keep their claims attributed and cross-check with independent reviews.
- `arute-2019`: the classical-simulation estimate was disputed afterwards; an A/B source for the rebuttals is still missing.
- math-foundations gaps: no source on numerical linear algebra (Gram-Schmidt stability, eigenvalue computation); the rank-1 criterion for product states and the fidelity of pure states are [unverified] — look for support in watrous-2025 (Schmidt decomposition, Unit III) when researching later domains. Two forward links (hamiltonian-simulation, qiskit-programming index) resolve once those domains are written.
- quantum-mechanics gaps: no source derives Larmor precession or the general bound ΔAΔB ≥ ½|⟨[A,B]⟩| (both [unverified]); amplitude damping only from Preskill; three "why it matters" claims (interference amplifies right answers, algorithms make the right answer likely) are [unverified] until the quantum-algorithms domain backs them.
- qubits-and-circuits gaps: "two-qubit gates are the costliest on hardware" is [unverified] (back it in quantum-hardware); no source explains why the T count matters in fault tolerance (error-correction domain); preskill-ph219 ch. 4 is a 2001 draft (outdated on Bell loopholes; hensen-2015 added for the 2015 loophole-free test).
- `qiskit-docs` change with each SDK version: notes must record the version, and code in the content must be checked against it.

## Decisions
- 2026-11-03 — Angle: programming and algorithms, plus physics/math foundations and hardware construction (user answer). Learner programs and has rusty linear algebra → a math refresher domain first.
- 2026-11-03 — Map approved as proposed: hardware before error correction; quantum annealing and quantum machine learning stay out for now; `nielsen-chuang-2010` is further reading only (TOC).
- 2026-11-03 — Large sources shared by several domains (watrous-2025, de-wolf-2026, preskill-ph219) are researched per domain: each domain's researcher appends its concepts to the existing note instead of reading the whole book at once.

## Log
- 2026-11-03 — map created (7 domains, 69 concepts, 34 sources)
- 2026-11-03 — map approved; starting math-foundations
- 2026-11-03 — `de-wolf-2023` renamed `de-wolf-2026` (the arXiv v6 of 27 Aug 2026 was read; nothing cited it yet)
- 2026-11-03 — quantum-mechanics: added zwiebach-mit-8-05 (spin 1/2, unitary dynamics) and zurek-2003 (decoherence); 8.04 covers neither spin nor decoherence
- 2026-11-03 — math-foundations done: 8 concepts (layers 1–3), 56 questions (layer 1: 24, layer 2: 16, layer 3: 16), 3 own diagrams (complex-plane-unit-circle, orthonormal-projection, kronecker-layout), 6 [unverified]
- 2026-11-03 — math-foundations: fidelity claim now backed by watrous-2025 (L12.2); one [unverified] fewer
- 2026-11-03 — quantum-mechanics done: 10 concepts, 77 questions (layer 1: 19, layer 2: 36, layer 3: 22), 3 own diagrams (mach-zehnder-amplitudes, stern-gerlach-zxz, dephasing-bloch-density), 11 [unverified]
- 2026-11-03 — qubits-and-circuits: added hensen-2015 (first loophole-free Bell test)
- 2026-11-03 — qubits-and-circuits done: 12 concepts, 91 questions (layer 1: 23, layer 2: 40, layer 3: 28), 4 own diagrams (bloch-sphere, bell-circuit, teleportation-circuit, chsh-game), 1 [unverified]
