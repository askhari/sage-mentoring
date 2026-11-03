---
source: openstax-physics-3
concepts: [quantization-and-wave-particle, superposition-principle, state-vector-postulate, born-rule-measurement, uncertainty-and-noncommutativity, unitary-time-evolution]
---

Accessed: full online text of OpenStax University Physics Vol. 3 (CC BY 4.0), sections 6.1, 6.2, 6.3, 6.5, 6.6, 7.1, 7.2, 7.3, read via fetch/summarization. Note: in this edition de Broglie waves are §6.5 and wave-particle duality is §6.6 (not 6.6/6.7). §7.6 (tunneling) not read.

## quantization-and-wave-particle
- Classical (Rayleigh-Jeans) treatment of cavity radiation predicts intensity growing without bound at short wavelengths (the "ultraviolet catastrophe"), contradicting measurements (§6.1) → quantization-and-wave-particle
- Planck (1900) assumed the oscillators in the walls only have energies E_n = nhf, so energy is exchanged in packets of hf; h = 6.626×10⁻³⁴ J·s = 4.136×10⁻¹⁵ eV·s (§6.1) → quantization-and-wave-particle
- Planck's law reproduces the measured spectrum and yields Wien's law (λ_max·T = 2.898×10⁻³ m·K) and Stefan's law (P = σAT⁴); Planck first saw quantization as a mathematical device, Einstein later gave it physical meaning as light particles (§6.1) → quantization-and-wave-particle
- Photoelectric effect: emission is nearly instantaneous; intensity changes the current but not the electrons' maximum kinetic energy; there is a cut-off frequency per metal; K_max grows linearly with frequency. Classical wave theory predicts the opposite on each point (§6.2) → quantization-and-wave-particle
- Einstein (1905): light comes as photons of energy E = hf, each giving all its energy to one electron: K_max = hf − φ (φ = work function); cut-off f_c = φ/h; handy value hc ≈ 1240 eV·nm; intensity = photons per second (§6.2) → quantization-and-wave-particle
- Compton effect: X-rays scattered by electrons come out with longer wavelength, Δλ = (h/m₀c)(1 − cos θ), Compton wavelength h/m₀c ≈ 2.43 pm; explained by photon–electron collision conserving relativistic energy and momentum; photon momentum p = h/λ (§6.3) → quantization-and-wave-particle
- de Broglie (1924): any particle with energy and momentum is also a wave, λ = h/p, E = ħω, p = ħk. Basketball (0.65 kg, 10 m/s): λ ≈ 10⁻³⁴ m (undetectable); electron with K = 1 eV: λ ≈ 1.23 nm (§6.5) → quantization-and-wave-particle
- Evidence: Davisson-Germer (1927) electrons at 54 V off nickel gave measured λ = 1.64 Å vs predicted 1.67 Å; wave behavior also seen for neutrons, protons and C₆₀ molecules. Standing-wave condition 2πr = nλ reproduces Bohr's L = nħ (§6.5) → quantization-and-wave-particle
- Double slit with electrons: fringes build up gradually even when electrons pass one at a time (Pozzi 1974, Tonomura 1989); Jönsson 1961 for beams. Light and matter show wave or particle behavior depending on the experiment (§6.6) → quantization-and-wave-particle

## superposition-principle
- Any linear combination of separable solutions of the Schrödinger equation is also a solution; such combinations can describe a localized particle (§7.3) → superposition-principle
- A two-state system can be in a state with no definite value before observation; a qubit is likened to a combination of 0 and 1 with probabilities p and q = 1 − p (§7.1) → superposition-principle
- Electron fringes in the double slit come from the wave nature (interference of the matter wave), even for single electrons (§6.6) → superposition-principle
- A localized particle is modelled as a wave packet built from many plane waves (§7.2) → superposition-principle
- ⚠️ The text is brief and informal on superposition (no Dirac notation, no amplitudes of discrete states); the qubit remark is loose.

## state-vector-postulate
- The wave function Ψ(x,t) is generally complex-valued, so one uses the complex conjugate Ψ* to get real probabilities (§7.1) → state-vector-postulate
- Normalization: ∫|Ψ|²dx over all space = 1, because the particle must be found somewhere; this fixes amplitude constants (§7.1) → state-vector-postulate
- Free particle solution is the complex plane wave Ψ = A e^{i(kx−ωt)}; real sine/cosine do not solve the equation; the text stresses Ψ is "merely a tool" for calculation, not directly observable (§7.3) → state-vector-postulate
- Acceptable solutions must be continuous, have continuous derivative (unless the potential is infinite) and not diverge at ±∞, which makes them normalizable (§7.3) → state-vector-postulate
- Matter waves carry information on the probable position and other properties of the particle; quantum theory treats them as fundamental (§6.6) → state-vector-postulate

## born-rule-measurement
- Born interpretation: |Ψ|² is a probability density (probability per unit length) for finding the particle at x at time t (§7.1) → born-rule-measurement
- Probability in a small interval: P = |Ψ|²dx; over a finite interval, integrate |Ψ|² (§7.1) → born-rule-measurement
- Expectation values: ⟨x⟩ = ∫Ψ* x Ψ dx; ⟨p⟩ = ∫Ψ*(−iħ d/dx)Ψ dx; ⟨K⟩ uses K̂ = −(ħ²/2m) d²/dx² (§7.1) → born-rule-measurement
- Odd integrands over symmetric intervals vanish, so ⟨x⟩ and ⟨p⟩ can be zero for symmetric states (§7.1) → born-rule-measurement
- Measurement: before detection position has no single value; on detection the particle takes a definite position with probability |Ψ|²dx, called state reduction/wave function collapse (Copenhagen interpretation, still most commonly taught); Schrödinger's cat was a critique (§7.1) → born-rule-measurement
- Quantum predictions depend only on |Ψ|² (§7.3) → born-rule-measurement
- Single-electron double-slit hits are individually random but build up the interference pattern statistically (§6.6) → born-rule-measurement

## uncertainty-and-noncommutativity
- Position–momentum: ΔxΔp ≥ ħ/2; precise position implies poor momentum knowledge and vice versa (§7.2) → uncertainty-and-noncommutativity
- It stems from the wave nature of matter, not from apparatus imprecision; a definite-momentum plane wave has totally undetermined position (§7.2) → uncertainty-and-noncommutativity
- A Gaussian wave packet attains the minimum product ΔxΔp = ħ/2 (§7.2) → uncertainty-and-noncommutativity
- Energy–time: ΔEΔt ≥ ħ/2; short-lived states have ill-defined energy, so short-lived excited states give broad spectral lines (§7.2) → uncertainty-and-noncommutativity
- Scale examples: for a speed uncertainty of 1.0×10⁻³ m/s, minimum Δx ≈ 5.8 cm for an electron but ≈ 8.8×10⁻³³ m for a 6 kg bowling ball (§7.2) → uncertainty-and-noncommutativity
- Confining an electron to 0.1 nm gives zero-point-like energy ≈ ħ²/(8mL²) ≈ 0.95 eV, about 1 eV, consistent in order of magnitude with the ~10 eV ionization energy (§7.2) → uncertainty-and-noncommutativity
- Momentum operator in position space is −iħ d/dx (§7.1); ⚠️ the text does not discuss commutators or noncommutativity explicitly → uncertainty-and-noncommutativity

## unitary-time-evolution
- Time-dependent Schrödinger equation: −(ħ²/2m)∂²Ψ/∂x² + UΨ = iħ ∂Ψ/∂t; compared in role to Newton's second law; often needs numerical solution (§7.3) → unitary-time-evolution
- Obtained from the energy relation E = p²/2m + U with wave relations (§7.3) → unitary-time-evolution
- If U is time-independent, separate variables: Ψ(x,t) = ψ(x)e^{−iEt/ħ}; E is the real total energy (§7.3) → unitary-time-evolution
- Time-independent equation: −(ħ²/2m)d²ψ/dx² + Uψ = Eψ (§7.3) → unitary-time-evolution
- Free particle: Ψ = A e^{i(kx−ωt)} (§7.3) → unitary-time-evolution
- The equation is linear, so combinations of separable solutions are solutions (§7.3) → unitary-time-evolution
- ⚠️ The text does not use the term "stationary state" or "unitary", nor show norm preservation; the separable form is the nearest idea (§7.3).

## Not covered / level
- Not covered: explicit unitarity, Hilbert space/state vector, commutators; §7.6 tunneling not read.
- Level: intro / first-year university (calculus-based physics).
