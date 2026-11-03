---
source: zwiebach-mit-8-05
concepts: [two-level-systems, superposition-principle, state-vector-postulate, born-rule-measurement, observables, uncertainty-and-noncommutativity, unitary-time-evolution]
---

Accessed: full text of MIT 8.05 (Fall 2013) ch.2 (Spin one-half, bras, kets, and operators) and ch.6 (Quantum dynamics, §2 and §3 only; harmonic oscillator, coherent and squeezed states skipped). Page numbers are those of each chapter.

## two-level-systems
- Stern and Gerlach (1922) sent silver atoms through an inhomogeneous magnetic field and saw quantized magnetic moments taking two values; the silver atom's moment is that of its single outer 5s electron (ch.2 §1, pp. 1, 3). → two-level-systems
- A magnetic moment in a field gradient feels a force along z proportional to μ_z. Classically one expects a smooth spread on the screen. Instead two separate peaks appear, so S_z takes only the values ±ħ/2, which defines spin one-half (ch.2 §1, pp. 4-5). → two-level-systems
- The electron's intrinsic spin is not a spinning ball of charge (the electron is treated as pointlike). Its magnetic moment is μ = -g μ_B S/ħ with g = 2 (ch.2 §1, pp. 2-3). → two-level-systems
- The spin state space is a 2-dimensional complex vector space with orthonormal basis |z;+⟩ = (1,0)^T and |z;−⟩ = (0,1)^T, also written |1⟩ and |2⟩ (ch.2 §2, pp. 7-8). → two-level-systems
- The Pauli matrices are σ1 = [[0,1],[1,0]], σ2 = [[0,−i],[i,0]], σ3 = [[1,0],[0,−1]], with S_i = (ħ/2)σ_i. Together with the identity they form a real basis for all 2×2 Hermitian matrices (ch.2 §2, pp. 10-11). → two-level-systems
- Pauli matrix identities: each squares to the identity, each is traceless, and distinct ones anticommute. In compact form {σi,σj} = 2δij·1 and σiσj = δij·1 + iε_ijk σk (ch.2 §3, pp. 13-14). → two-level-systems
- Vector form: (a·σ)(b·σ) = (a·b)1 + i(a×b)·σ, so (n·σ)² = 1 for a unit vector n (ch.2 §3, p. 15). → two-level-systems
- For a direction n = (sinθcosφ, sinθsinφ, cosθ), S_n = n·S = (ħ/2)[[cosθ, sinθe^{-iφ}],[sinθe^{iφ}, −cosθ]]. Its eigenstates are |n;+⟩ = cos(θ/2)|+⟩ + sin(θ/2)e^{iφ}|−⟩ and |n;−⟩ = −sin(θ/2)e^{-iφ}|+⟩ + cos(θ/2)|−⟩, which are orthonormal (ch.2 §4, pp. 16-18). → two-level-systems
- The x and y eigenstates are |x;±⟩ = (|z;+⟩ ± |z;−⟩)/√2 and |y;±⟩ = (|z;+⟩ ± i|z;−⟩)/√2. Without complex numbers there would be no y states (ch.2 §2, pp. 11-12). → two-level-systems

## superposition-principle
- Experiment 1: two z-machines in series with the S_z = −ħ/2 beam blocked after the first. All atoms exit the second machine as S_z = +ħ/2. So |z;+⟩ has zero amplitude along |z;−⟩ and the two states are orthogonal (ch.2 §1, p. 5). → superposition-principle
- Experiment 2: an S_z = +ħ/2 beam entering an x-machine splits about half and half into S_x = ±ħ/2. Classically a z-spin would have no x-component, so quantum mechanically a definite-S_z state carries amplitude along both S_x states (ch.2 §1, p. 6). → superposition-principle
- Experiment 3: block S_x = +ħ/2 after the x-machine and send the S_x = −ħ/2 beam into a second z-machine. Half of the atoms emerge with S_z = +ħ/2 and half with −ħ/2. The earlier S_z filter leaves no memory, so a particle does not hold S_x and S_z values at once (ch.2 §1, pp. 6-7). → superposition-principle
- The mathematical model is that |z;±⟩ are superpositions of |x;±⟩ and vice versa: |z;+⟩ = (|x;+⟩ + |x;−⟩)/√2. This matches the equal splitting seen in experiment 2 (ch.2 §2, p. 12). → superposition-principle
- A single atom can be "in both beams" with different amplitudes. Only the act of measurement (the detector screen) forces it to be in one (ch.2 §1, footnote 1, p. 5). → superposition-principle
- The relative sign matters. |x;−⟩ differs from |x;+⟩ by a minus sign, which makes it orthogonal to |x;+⟩ (ch.2 §2, p. 12). → superposition-principle

## state-vector-postulate
- The general spin state is |Ψ⟩ = c1|z;+⟩ + c2|z;−⟩ with complex c1, c2, represented as the column vector (c1,c2)^T (ch.2 §2, pp. 7-8). → state-vector-postulate
- Bras are the conjugate-transpose row vectors. The inner product is ⟨α|β⟩ = α1*β1 + α2*β2, and the basis is orthonormal: ⟨i|j⟩ = δij (ch.2 §2, p. 8). → state-vector-postulate
- Normalization condition for a column vector: |c1|² + |c2|² = 1 (ch.2 §2, p. 11). → state-vector-postulate
- The overall phase of an eigenstate is not observable, so one may choose the simplest form. For example |e1;−⟩ = −|x;−⟩ and |e2;−⟩ = i|y;−⟩ describe the same physical states (ch.2 §4, pp. 17-18). → state-vector-postulate
- A state is a unit vector in the state space H. As time passes its tip moves along a trajectory in H (ch.6 §2, pp. 10-11, Fig. 1). → state-vector-postulate
- ⚠️ Footnote 3 (p. 18) notes that no single formula for |n;±⟩ avoids a phase ambiguity over the whole sphere, so the phase choice is a convention. → state-vector-postulate

## born-rule-measurement
- The probability of finding a state in an eigenstate is the squared norm of the amplitude: ⟨x;±|z;+⟩ = 1/√2 gives probability 1/2 each (ch.2 §2, p. 12, eq. 2.34). → born-rule-measurement
- Source claim: the beam entering experiment 1's second machine had overlap 1 with |z;+⟩, so all atoms exit the top port, and overlap 0 with |z;−⟩ (ch.2 §2, p. 8). → born-rule-measurement
- Filter picture: a Stern-Gerlach box with one output blocked acts as a filter that prepares a definite spin state (ch.2 §1, p. 5). → born-rule-measurement
- After passing through the x-machine and being selected for S_x = −ħ/2, atoms no longer have S_z = +ħ/2. Measuring S_z gives ±ħ/2 with probability 1/2 each (ch.2 §1, pp. 6-7). → born-rule-measurement
- The source treats measurement only through these experiments and the amplitude-squared rule. It does not state the Born rule as a formal postulate or discuss the general projection postulate in these chapters (ch.2 §1-2). → born-rule-measurement

## observables
- S_z = (ħ/2)diag(1,−1) is a Hermitian 2×2 matrix with eigenstates |z;±⟩ and eigenvalues ±ħ/2. Spin operators act on 2-component vectors rather than wavefunctions (ch.2 §2, pp. 8-9). → observables
- Hermitian means unchanged by transpose plus complex conjugation. The general 2×2 Hermitian matrix is built from the identity and the three Pauli matrices with real coefficients (ch.2 §2, pp. 9-10). → observables
- S_x and S_y are fixed by requiring Hermiticity, eigenvalues ±ħ/2 and the angular momentum commutation relations. Their matrices are (ħ/2)σ1 and (ħ/2)σ2, unique up to a physically equivalent relabeling (ch.2 §2, p. 11). → observables
- The eigenvalues of each σ_i are ±1 because σ_i² = 1 and tr σ_i = 0, so there is one +1 and one −1 (ch.2 §3, p. 13). → observables
- S_n = n·S is Hermitian, squares to (ħ/2)²·1 and is traceless, so its eigenvalues are ±ħ/2 for every direction n. This is required physically because all directions are equivalent (ch.2 §4, p. 16). → observables
- Spin eigenstates |n;±⟩ satisfy S_n|n;±⟩ = ±(ħ/2)|n;±⟩. They represent spin up or down along n (ch.2 §4, pp. 16-17). → observables
- Hermitian operators can also be built from energy-like quantities. Any Hermitian operator with units of energy can be called a Hamiltonian (ch.6 §2.2, p. 15). → observables

## uncertainty-and-noncommutativity
- Orbital angular momentum obeys [L_i,L_j] = iħε_ijk L_k, so [L_x,L_y] = iħL_z and cyclic permutations (ch.2 §2, p. 9). → uncertainty-and-noncommutativity
- Spin as an angular momentum must satisfy the same algebra: [S_x,S_y] = iħS_z, [S_y,S_z] = iħS_x, [S_z,S_x] = iħS_y (ch.2 §2, p. 9). → uncertainty-and-noncommutativity
- Explicit check with the matrices (ħ/2)σ_i gives [S_x,S_y] = iħS_z (ch.2 §2, p. 11, eq. 2.27). → uncertainty-and-noncommutativity
- For Pauli matrices: [σi,σj] = 2iε_ijk σk, and the anticommutator vanishes for i≠j (ch.2 §3, pp. 12-14). → uncertainty-and-noncommutativity
- The decomposition XY = ½{X,Y} + ½[X,Y] splits a product into symmetric and antisymmetric parts, and yields σiσj = δij + iε_ijk σk (ch.2 §3, p. 14). → uncertainty-and-noncommutativity
- Physical incompatibility is shown by experiment 3: S_x and S_z cannot both be definite, since filtering S_x erases the prior S_z value (ch.2 §1, pp. 6-7). → uncertainty-and-noncommutativity
- For triplets of non-commuting operators the order matters in dot and cross products. Their dot product is not necessarily commutative (ch.2 §3, p. 15). → uncertainty-and-noncommutativity
- Source claim: commutators correspond to iħ times classical Poisson brackets, [A,B] ⇔ iħ{A,B}_pb, with [x,p] = iħ while {x,p}_pb = 1 (ch.6 §2.2, pp. 14-15). → uncertainty-and-noncommutativity

## unitary-time-evolution
- Postulate: for any system there is a unitary operator U(t,t0) with |Ψ,t⟩ = U(t,t0)|Ψ,t0⟩. It is the same for all initial states and is unique (ch.6 §2.1, p. 10). → unitary-time-evolution
- Unitarity, U†U = 1, conserves the norm of the state (ch.6 §2.1, pp. 10-11). → unitary-time-evolution
- Properties of U: U(t0,t0) = 1, composition U(t2,t0) = U(t2,t1)U(t1,t0), and inverse U(t0,t) = U†(t,t0) (ch.6 §2.1, pp. 11-12). → unitary-time-evolution
- Derivation of the Schrödinger equation: differentiate |Ψ,t⟩ = U|Ψ,t0⟩ to get ∂t|Ψ,t⟩ = Λ|Ψ,t⟩, with Λ = (∂t U) U†. Differentiating UU† = 1 shows Λ is antihermitian, and an insertion of identity shows Λ is independent of t0 (ch.6 §2.2, pp. 12-13). → unitary-time-evolution
- Defining H = iħΛ gives a Hermitian operator with units of energy, and the equation iħ ∂t|Ψ,t⟩ = H(t)|Ψ,t⟩. Unitary evolution therefore implies the Schrödinger equation (ch.6 §2.2, p. 14). → unitary-time-evolution
- H is identified with the Hamiltonian because energy is conjugate to time, and because d⟨Q⟩/dt = ⟨[Q,H]⟩/(iħ) mirrors the classical Poisson bracket equation dQ/dt = {Q,H}_pb (ch.6 §2.2, p. 14). → unitary-time-evolution
- For H of form p²/2m + V(x), the Schrödinger equation for the wavefunction Ψ(x,t) = ⟨x|Ψ,t⟩ takes the familiar position-space form (ch.6 §2.2, p. 15). → unitary-time-evolution
- The operator satisfies iħ dU/dt = H U. For time-independent H, U(t,t0) = exp[−iH(t−t0)/ħ], with the matrix exponential defined by its Taylor series. The ordering matters: U(0)e^{tK} would not solve the equation (ch.6 §2.3, Case 1, pp. 15-16). → unitary-time-evolution
- If H(t) at different times commute (the source's example is a spin in a field of varying magnitude but fixed direction), U = exp[−(i/ħ)∫H dt']. In general one needs the time-ordered exponential series (ch.6 §2.3, Cases 2-3, pp. 16-17). → unitary-time-evolution
- Heisenberg picture: A_H(t) = U†(t,0) A_S U(t,0), which equals A_S at t = 0. It preserves products and commutators, and ⟨Ψ,t|A_S|Ψ,t⟩ = ⟨Ψ,0|A_H(t)|Ψ,0⟩ (ch.6 §3.1, pp. 18-20). → unitary-time-evolution
- Heisenberg equation of motion: iħ dA_H/dt = [A_H, H_H] + iħ(∂A_S/∂t)_H. An operator commuting with H is conserved, so A_H = A_S and its expectation value is constant (ch.6 §3.2, pp. 20-22). → unitary-time-evolution
- ⚠️ Spin precession in a magnetic field (Larmor) is not worked out in the sections read. Only a passing mention of a spin in a field appears (ch.6 §2.3, p. 16). → unitary-time-evolution

## Not covered / level
- Not covered: Larmor precession (explicit derivation) and a formal Born-rule or projection postulate.
- Level: university (second course in quantum mechanics, MIT 8.05).
