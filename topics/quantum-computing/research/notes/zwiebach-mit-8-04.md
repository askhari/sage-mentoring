---
source: zwiebach-mit-8-04
concepts: [quantization-and-wave-particle, superposition-principle, state-vector-postulate, born-rule-measurement, observables, unitary-time-evolution, uncertainty-and-noncommutativity, two-level-systems]
---

Accessed: full text of lecture notes 1-9 (B. Zwiebach, MIT 8.04 Quantum Physics I, Spring 2016, OCW CC BY-NC-SA). Locations are "LN<n> §<section>, p. <page>" (page = page within each lecture note).

## quantization-and-wave-particle
- Photoelectric effect observations: a threshold frequency ν0 below which no current flows; current proportional to light intensity; photoelectron energy independent of intensity (LN3 §1, p. 1) → quantization-and-wave-particle
- Einstein (1905) explained this by light energy coming in discrete quanta hν. An electron leaves with kinetic energy hν minus the work function W, and the threshold satisfies hν0 = W. More intensity means more photons per second, so more current, not faster electrons (LN3 §1, p. 1-2) → quantization-and-wave-particle
- Einstein predicted a linear rise of photoelectron energy with frequency. Millikan (1915) confirmed it and fixed Planck's constant to better than 1%. Skeptics still doubted that light is made of particles (LN3 §1, p. 2) → quantization-and-wave-particle
- A photon's energy depends only on its color (E = hν). To make a beam of the same color more energetic you add photons. A "quantum particle" of light is an indivisible packet of energy and momentum, not a classical point particle with definite position and velocity (LN1 §3, p. 5-6) → quantization-and-wave-particle
- Compton scattering (X-rays on carbon, 1923-24): classical Thomson scattering predicts no change of frequency, but the data show a wavelength shift. A photon colliding with a stationary electron loses energy, and the shift grows with scattering angle (λf = λi + (h/mec)(1-cosθ)), up to 2 Compton wavelengths at 180°. This convinced most skeptics that photons carry momentum (E = pc, p = h/λ) (LN3 §2, p. 3-5; LN1 §3, p. 5) → quantization-and-wave-particle
- de Broglie (1924) proposed that wave-particle duality is universal: a matter particle of momentum p has wavelength λ = h/p. The wave nature disappears as h→0, so it is a purely quantum property (LN3 §3, p. 6) → quantization-and-wave-particle
- Evidence for matter waves: Davisson-Germer electron diffraction (1927), single-electron two-slit interference, and interference of molecules with hundreds of atoms (LN3 §3, p. 6) → quantization-and-wave-particle
- Rule of thumb: wave effects are negligible when the de Broglie wavelength is much smaller than the obstacle, i.e. when x·p is much larger than h. Classical electromagnetic fields correspond to coherent states with a fluctuating photon number, not to a fixed photon number (LN3 §3, p. 6-7) → quantization-and-wave-particle
- The de Broglie relations p = ħk and E = ħω hold for all particles. Zwiebach gives three motivations: the packet's group velocity equals the particle velocity, relativistic four-vector consistency, and agreement with E = hν for photons (LN4 §1, p. 3-4) → quantization-and-wave-particle

## superposition-principle
- Linearity: for a linear equation Lu = 0, any combination αu1 + βu2 of solutions is a solution. Maxwell's theory is linear (many EM waves coexist without disturbing each other). Newtonian mechanics and general relativity are nonlinear (LN1 §1, p. 1-3) → superposition-principle
- The Schrödinger equation is linear, so αΨ1 + βΨ2 is a solution for complex α, β. Zwiebach argues that quantum mechanics is "simpler" than classical mechanics in this sense (LN1 §1, p. 3-4; LN5 §2, p. 7) → superposition-principle
- Interference at the single-photon level: in a Mach-Zehnder interferometer a single photon interferes with itself, because interference between two photons would mean "two photons giving none", which energy conservation forbids. The photon is therefore in a superposition of "upper branch" and "lower branch" (LN1 §4, p. 9) → superposition-principle
- Mach-Zehnder in vector form: the state is a two-component amplitude vector (α, β) for upper/lower beam, with |α|²+|β|²=1. A phase shifter multiplies an amplitude by e^{iδ}. A balanced beam splitter is a 2×2 matrix of the form (1/√2)[[1,1],[1,-1]] (up to sign convention), and linearity fixes its action on any superposition (LN2 §1, p. 1-4) → superposition-principle
- Two beam splitters in sequence send an input photon entirely to detector D0 with probability 1 and D1 with probability 0, because of destructive interference at BS2. Blocking one path lets the photon reach D1 with probability 1/4 (1/2 absorbed by the block, 1/4 at D0), so removing a path increases a detection probability (LN2 §1, p. 4-6) → superposition-principle
- Elitzur-Vaidman bomb: put a bomb with a photon-detector trigger in one arm. A dud lets all photons end at D0. A working bomb explodes with probability 1/2, gives D0 with 1/4, and gives D1 with 1/4. A click at D1 certifies a working bomb without the photon having "touched" it (interaction-free measurement) (LN2 §2, p. 6-7) → superposition-principle
- Interpretation of a superposition of "A" (always gives value a) and "B" (always gives value b): a measurement yields a or b, never an intermediate value. The coefficients set the probabilities. Multiplying a state by a nonzero complex number does not change the physics (LN1 §4, p. 10) → superposition-principle
- A superposition is physically different from a classical 50/50 ensemble: an equal superposition of spin up and spin down along z gives the same z statistics as a mixture, but measuring along x gives all "up" for the superposition and 50/50 for the mixture (LN1 §4, p. 12) → superposition-principle
- Entanglement: a two-particle state is entangled if it cannot be written as a product (state of 1) ⊗ (state of 2). Example: |↑⟩⊗|↓⟩ + |↓⟩⊗|↑⟩ gives perfectly anti-correlated z spins, and factorization is shown impossible by solving for the coefficients. Bell (1964) showed that measurements in several directions give correlations that no classical ensemble reproduces, and entanglement cannot be used to signal faster than light (LN1 §5, p. 12-14) → superposition-principle

## state-vector-postulate
- The wavefunction Ψ is the dynamical variable of quantum mechanics and is itself complex. The Schrödinger equation contains i explicitly, so real solutions are impossible (LN1 §2, p. 5; LN5 §1, p. 4) → state-vector-postulate
- Complex numbers cannot be measured, so Ψ relates only indirectly to observable quantities: probabilities are computed from |Ψ|² (LN1 §2, p. 5) → state-vector-postulate
- Wavefunctions/states are treated as vectors in a complex vector space, because states can be added and multiplied by complex numbers (LN1 §2, p. 5; §4, p. 10) → state-vector-postulate
- Ψ and αΨ (α≠0) describe the same physics. If ∫|Ψ|²dx = N is finite (square-integrable), dividing by √N gives a normalized wavefunction, and probabilities use |Ψ|²/N (LN6 §1, p. 2) → state-vector-postulate
- Counting parameters: a photon polarization state α|x⟩ + β|y⟩ has two complex numbers, but the overall factor is irrelevant, so only the ratio β/α matters, which is one complex or two real parameters. This matches the two real parameters of classical elliptical polarization (LN1 §4, p. 10-11) → state-vector-postulate
- A plane wave e^{i(kx-ωt)} has |Ψ|²=1, so its integral is infinite and it cannot represent a single particle. Superposing such waves produces normalizable wave packets (LN6 §1, p. 2) → state-vector-postulate
- Ψ(x,0) determines Φ(k) by Fourier transform and vice versa, so Φ carries the same information. Parseval/Plancherel gives ∫|Ψ|²dx = ∫|Φ|²dk, and Φ(p) is the wavefunction in momentum space (LN8 §1, p. 1-3) → state-vector-postulate
- For an observable with eigenstates ψi, the state is expanded as Σαiψi with αi = (ψi,Ψ), and normalization means Σ|αi|² = 1. The same state can be expanded in the eigenbasis of different observables (LN9 §1, p. 3-4) → state-vector-postulate

## born-rule-measurement
- Quantum mechanics is not deterministic: a photon hitting a polarizer at angle α passes with probability cos²α, and no one can predict which photon passes, though all photons are identical (LN1 §3, p. 6-7) → born-rule-measurement
- Each photon is either absorbed or transmitted whole, since a fractional photon would have a different frequency. The classical wave fraction cos²α of energy therefore becomes a probability for each single photon (LN1 §3, p. 7) → born-rule-measurement
- Hidden-variable explanations (Einstein and others) are testable. After Bell's work, experiments rule out most versions, and nobody has found how to restore determinism (LN1 §3, p. 7; §5, p. 14) → born-rule-measurement
- Schrödinger first thought |Ψ|² was the fraction of a particle at x. Born observed that particles stay whole in scattering experiments and proposed that |Ψ(x,t)|² d³x is the probability to find the particle in that volume on measurement at time t (LN5 §3, p. 8; LN1 §1, p. 3) → born-rule-measurement
- A normalized wavefunction satisfies ∫|Ψ|² = 1. The probability density is ρ = Ψ*Ψ (LN5 §3, p. 8; LN6 §2, p. 3) → born-rule-measurement
- Measurement of a superposition Σαi|i⟩ yields outcome i with probability |αi|², and afterwards the state becomes |i⟩ ("collapse"). Repeating immediately gives the same result with certainty (LN1 §4, p. 10; LN9 §1, p. 3) → born-rule-measurement
- With degenerate eigenvalues, collapse projects onto the sum of the degenerate components, renormalized (LN9 §1, p. 3-4) → born-rule-measurement
- Measurement postulate "follows the Copenhagen interpretation." Because individual outcomes are unpredictable, probabilities are only determined by repeating over an ensemble (LN9 §1, p. 4; LN1 §4, p. 11-12) → born-rule-measurement
- By analogy |Φ(p)|²dp is the probability of finding momentum in (p, p+dp), which is postulated, motivated by Parseval (LN8 §1, p. 3) → born-rule-measurement
- Worked example: a state on a circle written as a combination of momentum eigenstates ψ_{±1}, ψ_{±3} gives probabilities 1/6, 1/6, 1/3, 1/3 for p = ±2πħ/L, ±6πħ/L (LN9 §1, p. 4-5) → born-rule-measurement

## observables
- An operator Q is Hermitian if (Ψ1, QΨ2) = (QΨ1, Ψ2), with (Ψ1,Ψ2) = ∫Ψ1*Ψ2. Observables are represented by Hermitian operators, and their possible measured values are the eigenvalues (LN6 §2, p. 4; LN9 §1, p. 1) → observables
- Claim: the expectation value of a Hermitian operator is real. Claim: its eigenvalues are real. The expectation value of Q in one of its eigenstates equals that eigenvalue (LN9 §1, p. 1-2) → observables
- Eigenfunctions of different eigenvalues are orthogonal. They can be chosen orthonormal, including in degenerate subspaces (this part is deferred to 8.05) (LN9 §1, p. 2) → observables
- Spectral theorem (stated, proven in 8.05 for finite dimensions): the eigenfunctions form a complete basis, so any reasonable Ψ is a superposition Σαiψi (LN9 §1, p. 3) → observables
- Measurement postulate: measuring Hermitian Q in state Ψ gives eigenvalue qi with probability |αi|², and the state then becomes ψi (LN9 §1, p. 3) → observables
- The expectation value ⟨Q⟩ = ∫Ψ*QΨ dx equals Σ pi qi, the probability-weighted sum of outcomes. It is the average over many identically prepared copies, and the position and momentum versions are derived from the probability densities |Ψ|² and |Φ|² (LN8 §2, p. 4-5; LN9 §1, p. 4) → observables
- Momentum operator p̂ = (ħ/i)∂/∂x, with plane waves as its eigenstates. The position operator x̂ multiplies by x. Operators ↔ matrices, wavefunctions ↔ vectors, eigenstates ↔ eigenvectors (LN5 §1, p. 1-2; §2, p. 5-6) → observables
- Uncertainty ΔQ of an observable in a state: (ΔQ)² = ⟨Q²⟩ - ⟨Q⟩². It is zero exactly when the state is an eigenstate of Q (LN9 §2, p. 6-7) → observables
- ⚠️ A typo in LN9 eq. (1.24): the denominator uses |αj| where the degenerate components are labeled i and k. The intended normalization is |αi|²+|αk|².

## unitary-time-evolution
- Schrödinger equation: iħ ∂Ψ/∂t = ĤΨ. The Hamiltonian Ĥ = p̂²/2m + V(x,t) is the energy operator, and the equation is linear (LN1 §1, p. 3-4; LN5 §2, p. 4) → unitary-time-evolution
- The equation is first order in time, so Ψ at one initial time determines Ψ at all times. This differs from a conventional second-order wave equation, which has real solutions (LN5 §1, p. 4; §2, p. 7) → unitary-time-evolution
- Time evolution of any initial state: Fourier-decompose Ψ(x,0) into plane waves and multiply each by e^{-iω(k)t} (LN5 §1, p. 3; LN7 §3, p. 6) → unitary-time-evolution
- The total probability N(t)=∫|Ψ|²dx must remain 1. Using the Schrödinger equation and its complex conjugate, dN/dt = 0 holds if Ĥ is Hermitian (LN6 §2, p. 3-4) → unitary-time-evolution
- The Hamiltonian is Hermitian, so conservation of normalization is guaranteed (Zwiebach reduces the proof to showing Ĥ Hermitian, and later uses its hermiticity) (LN6 §2, p. 4; LN8 §3, p. 6) → unitary-time-evolution
- Local conservation law ∂ρ/∂t + ∂J/∂x = 0 with probability current J = (ħ/m) Im(Ψ*∂Ψ/∂x). Probability in a region changes only through flow across its boundary, analogous to charge conservation in electromagnetism (LN6 §3-4, p. 5-8) → unitary-time-evolution
- The time dependence of expectation values for an operator without explicit time dependence is iħ d⟨Q⟩/dt = ⟨[Q,H]⟩ (LN8 §3, p. 6) → unitary-time-evolution
- Free wavepackets spread: the shape change is negligible only for t much less than mΔx²/ħ. A Gaussian packet width has timescale 2ma²/ħ. An electron localized to 10⁻¹⁰ m spreads in about 10⁻¹⁶ s (LN7 §2-3, p. 5-7) → unitary-time-evolution
- ⚠️ The word "unitary" does not appear in these notes. The unitarity of evolution is shown only as probability conservation with Hermitian Ĥ.

## uncertainty-and-noncommutativity
- The commutator [A,B] = AB - BA. Operator ordering matters, as with matrices. Operators commute when [A,B]=0 (LN5 §2, p. 5) → uncertainty-and-noncommutativity
- Direct computation on an arbitrary test function gives [x̂, p̂] = iħ, called the most fundamental commutation relation of quantum mechanics. In 3D, [x̂i, p̂j] = iħ δij (LN5 §2, p. 5-8) → uncertainty-and-noncommutativity
- No finite-dimensional matrices can satisfy [x̂,p̂] = iħ times identity, so x̂ and p̂ need infinite-dimensional matrices (LN5 §2, p. 6) → uncertainty-and-noncommutativity
- The Pauli matrices σ1, σ2, σ3 don't commute, e.g. [σ1,σ2] = 2iσ3, with cyclic permutations. They describe spin 1/2, with S_i = (ħ/2)σ_i (LN5 §2, p. 6) → uncertainty-and-noncommutativity
- Heisenberg's uncertainty principle (stated) follows from the commutator: ΔxΔp ≥ ħ/2 (LN5 §2, p. 6; LN7 §1, p. 3) → uncertainty-and-noncommutativity
- Wavepackets are superpositions of plane waves with weights Φ(k) (Fourier transform of Ψ). A narrow spread Δk requires a wide spread Δx, with ΔxΔk ≈ 1 (a Fourier-transform property, not specifically quantum) (LN7 §1, p. 1-3) → uncertainty-and-noncommutativity
- The quantum input is p = ħk, which converts this into ΔxΔp ≈ ħ (rough form). Precise definitions of Δx and Δp give ΔxΔp ≥ ħ/2 (LN7 §1, p. 3) → uncertainty-and-noncommutativity
- Example: a step-shaped Φ(k) of width Δk gives Ψ(x) ∝ sin(Δk x/2)/x, with ΔxΔk ≈ 2π (LN7 §1, p. 4) → uncertainty-and-noncommutativity
- For the observable-level uncertainty, ΔQ=0 iff Ψ is an eigenstate of Q (LN9 §2, p. 6-7) → uncertainty-and-noncommutativity
- ⚠️ The Heisenberg bound is stated but its general proof from the commutator is not given in these notes (LN5 mentions it can be proven, LN7 only says "one can then show").

## two-level-systems
- Photon polarization: |photon;x⟩ and |photon;y⟩ are two basis states. A photon polarized at angle α is cosα|x⟩ + sinα|y⟩, and a polarizer along x outputs |x⟩ with probability cos²α (LN1 §3, p. 7-8) → two-level-systems
- A general polarization state is α|x⟩ + β|y⟩ with complex α, β. Only the ratio β/α is physical (LN1 §4, p. 10-11) → two-level-systems
- Spin of the electron: along any chosen axis only two outcomes, up or down. States |↑;z⟩, |↓;z⟩ and their superposition give 50/50 outcomes along z, but a definite result along x (LN1 §4, p. 11-12) → two-level-systems
- Mach-Zehnder path states (1,0) and (0,1) form a two-component vector. Beam splitters and phase shifters act as 2×2 matrices (LN2 §1, p. 1-4) → two-level-systems
- Spin 1/2 is described by the Pauli matrices (2×2) with S_i = ħσ_i/2, which don't commute (LN5 §2, p. 6) → two-level-systems
- Two spin-1/2 particles: product states |↑⟩⊗|↓⟩ combine by superposition into entangled states (LN1 §5, p. 13-14) → two-level-systems

## Entanglement and determinism (extra)
- Entanglement and Bell tests are covered in the superposition-principle section above (LN1 §5, p. 12-14). Determinism loss and the hidden-variable debate are in the born-rule-measurement section (LN1 §3, p. 7-8). Zwiebach mentions the 1927 Solvay conference "God does not play dice" exchange with Bohr (LN1 §3, p. 8) → born-rule-measurement

## Not covered / level
- Not covered: Dirac bra-ket formalism and inner products of states as an abstract vector space, density matrices, qubit/Bloch-sphere formalism, unitary operators by name, tensor-product formalism beyond a short introduction.
- Level: university (first-course undergraduate quantum mechanics, wavefunction-based, with calculus/Fourier prerequisites).
