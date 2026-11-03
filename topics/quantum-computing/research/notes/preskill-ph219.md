---
source: preskill-ph219
concepts: [state-vector-postulate, born-rule-measurement, observables, unitary-time-evolution, two-level-systems, density-matrices, decoherence, uncertainty-and-noncommutativity]
---

Accessed: full extracted text of Ch. 2 "Foundations I: States and Ensembles" (version July 2015, 52 pp.) and Ch. 3 "Foundations II: Measurement and Evolution" (extracted file header says "Updated October 2018", i.e. a later revision than 2015). Locations are "ch.<chapter> §<section>, p. <page of that chapter's PDF>". Units hbar = 1 throughout.

## quantum-mechanics

### State vector postulate
- Closed-system QM rests on five axioms (states, observables, measurement, dynamics, composite systems); the chapter recalls them before studying open systems (ch.2 §2.1, p. 3) → state-vector-postulate
- Axiom 1: a state is a ray in a Hilbert space, i.e. a complex vector space with an inner product that is complete in its norm; completeness only matters in infinite dimensions (ch.2 §2.1, pp. 3-4) → state-vector-postulate
- A ray is a class of vectors differing by a nonzero complex scalar; by convention one picks a unit-norm representative, so the overall phase has no physical meaning (|psi> and e^{i alpha}|psi> are the same state) (ch.2 §2.1, p. 4) → state-vector-postulate
- Any superposition a|phi>+b|psi> is also a state, and the RELATIVE phase between terms is physically significant, unlike the global phase (ch.2 §2.1, p. 4) → state-vector-postulate
- A qubit is a system with a two-dimensional Hilbert space; the general state is a|0>+b|1> with |a|^2+|b|^2=1 and global phase irrelevant (ch.2 §2.2, p. 8) → state-vector-postulate
- Composite systems: the Hilbert space is the tensor product H_A (x) H_B, and independently prepared parts give a product state (Axiom 5) (ch.2 §2.1, pp. 6-7) → state-vector-postulate
- Wigner's theorem: a symmetry preserves |<phi|psi>|, so it can be represented (with phase choices) by a unitary or antiunitary map; symmetry representations need only hold up to a phase because states are rays (ch.2 §2.2.1, p. 9) → state-vector-postulate
- Because states are rays, rotations of spin-1/2 are represented only up to sign (2 pi rotation gives -I), yet this is observable via relative phase: a controlled 2 pi rotation flips a superposed control spin to an orthogonal state (ch.2 §2.2.1, p. 12, eq. 2.34) → state-vector-postulate

### Born rule and measurement
- Axiom 3: measuring an observable A yields an eigenvalue a_n with probability ||E_n|psi>||^2 = <psi|E_n|psi> (E_n = projector onto that eigenspace), and the post-measurement state is the normalized E_n|psi> (ch.2 §2.1, p. 5, eqs. 2.7-2.8) → born-rule-measurement
- A repeated measurement immediately afterwards gives the same outcome with probability one (ch.2 §2.1, p. 6) → born-rule-measurement
- For a qubit measured in {|0>,|1>}, outcomes have probability |a|^2 and |b|^2; except when a or b is zero the measurement irrevocably disturbs the state, and a and b cannot be determined from a single measurement (ch.2 §2.2, p. 8) → born-rule-measurement
- Two ways a state changes: unitary evolution (deterministic) and measurement (probabilistic); the unexplained difference is called the measurement problem (ch.2 §2.1, p. 7) → born-rule-measurement
- Von Neumann model: measure observable M by coupling it to a pointer (H ~ lambda M (x) P); the pointer position becomes correlated with the eigenvalue, and reading it projects the system onto an eigenstate with probability |<a|phi>|^2. Stern-Gerlach is the example for sigma_3 (ch.3 §3.1.1, pp. 5-7) → born-rule-measurement
- Orthogonal measurement with projectors {E_a} can be implemented by a unitary that shifts a pointer by a when the system is in E_a; if the outcome is unrecorded the state becomes sum_a E_a rho E_a (ch.3 §3.1.1, pp. 7-8, eqs. 3.12-3.18) → born-rule-measurement
- Measuring the pointer in a different basis gives a generalized measurement with operators M_a satisfying sum M_a^dagger M_a = I; outcomes have probability ||M_a|psi>||^2, post-measurement states need not be orthogonal and the measurement is not repeatable; the operators E_a = M_a^dagger M_a form a POVM (ch.3 §3.1.2, pp. 8-10) → born-rule-measurement
- Any POVM can be realized as an orthogonal measurement on system plus ancilla; the POVM gives probabilities, p(a) = tr(rho E_a), but not the post-measurement state (ch.3 §3.1.2, pp. 10-11) → born-rule-measurement

### Observables
- Axiom 2: an observable is a self-adjoint operator (A = A^dagger, i.e. <phi|A|psi> = <psi|A|phi>^*) (ch.2 §2.1, p. 4) → observables
- Sum of self-adjoint operators is self-adjoint, but a product AB is self-adjoint only if A and B commute; AB+BA and i(AB-BA) always are (ch.2 §2.1, pp. 4-5) → observables
- Spectral representation: a self-adjoint operator has an orthonormal eigenbasis, A = sum_n a_n E_n = sum_n |n> a_n <n|, with E_n orthogonal projectors (E_n E_m = delta_nm E_n); the projector onto |psi> is |psi><psi| (ch.2 §2.1, p. 5, eqs. 2.4-2.6) → observables
- Expectation value of A in |psi> is sum_n a_n Prob(a_n) = <psi|A|psi> (ch.2 §2.1, p. 6, eq. 2.9) → observables
- An observable on subsystem A alone is M_A (x) I_B (ch.2 §2.3.1, p. 18) → observables
- For a qubit, <n.sigma> in a pure state gives the spin component along n; measuring only along z gives |a|,|b| but not the relative phase, so three axes are needed to determine the state from many copies (ch.2 §2.2.1, p. 13) → observables
- Measuring along axis n equals rotating n to z and then measuring along z (ch.2 §2.2.1, p. 13) → observables

### Unitary time evolution
- Axiom 4: closed-system evolution is a unitary operator, |psi(t')> = U(t',t)|psi(t)> (Schrodinger picture) (ch.2 §2.1, p. 6) → unitary-time-evolution
- Infinitesimal evolution obeys the Schrodinger equation d/dt|psi> = -iH|psi> with H a self-adjoint Hamiltonian (units of energy; hbar = 1); equivalently |psi(t+dt)> = (I - iH dt)|psi(t)>, which is unitary to first order, and finite evolution is a product of such steps (ch.2 §2.1, p. 6) → unitary-time-evolution
- For a time-independent H, U(t',t) = e^{-i(t'-t)H} (ch.2 §2.1, p. 6) → unitary-time-evolution
- The Schrodinger equation is linear, in contrast to typical classical dynamical equations; the text says this property "seems to beg for an explanation" (ch.2 §2.1, p. 7) → unitary-time-evolution
- A symmetry must commute with time evolution; infinitesimally this gives [Q,H]=0 for its generator Q, so symmetries imply conservation laws and vice versa (ch.2 §2.2.1, p. 10) → unitary-time-evolution
- A device that "turns on" a Hamiltonian whose eigenstates are circular (or linear) polarization states rotates (or phase-shifts) a photon polarization; the two together give any 2x2 unitary of determinant 1 (ch.2 §2.2.2, p. 16) → unitary-time-evolution
- For density operators, closed evolution reads rho(t+dt) = rho(t) - i dt [H, rho(t)] (ch.3 §3.5.2, p. 35) → unitary-time-evolution

### Two-level systems
- A qubit is the smallest nontrivial quantum system; unlike a probabilistic classical bit there is "more than one way to look at" it (measurement in different bases) (ch.2 §2.2, p. 8) → two-level-systems
- Spin-1/2 realisation: |0>,|1> are spin up/down along z; the two real parameters of the state (after normalisation and global phase) give the spin direction (polar theta, azimuth phi) (ch.2 §2.2.1, pp. 8-9) → two-level-systems
- The spin-1/2 rotation generators are J_k = sigma_k/2 (Pauli matrices, which anticommute and square to I); a rotation by theta about unit vector n is U = cos(theta/2) I - i sin(theta/2) n.sigma, and every 2x2 unitary of determinant 1 has this form, so any qubit gate is a spin rotation up to global phase (ch.2 §2.2.1, pp. 11-12) → two-level-systems
- The state pointing along (theta, phi) is (e^{-i phi/2} cos(theta/2), e^{i phi/2} sin(theta/2)), an eigenstate of n.sigma with eigenvalue 1 (ch.2 §2.2.1, p. 13, eqs. 2.39-2.40) → two-level-systems
- Interference example: |up_x> = (|up_z>+|down_z>)/sqrt2 and |down_x> are each 50/50 in z, but the superposition (|up_x>+|down_x>)/sqrt2 is |up_z> and always gives up in z, unlike a probabilistic classical bit (ch.2 §2.2.1, p. 14) → two-level-systems
- Formal equivalence with spin-1/2 holds for any two-level system, but not every two-level system transforms as a spinor under spatial rotations (ch.2 §2.2.1, p. 14) → two-level-systems
- Photon polarization is another qubit: massless, spin-1 (not a spinor); linear states |x>,|y> rotate by the real rotation matrix, with circular states |R>,|L> as eigenstates (ch.2 §2.2.2, pp. 14-15) → two-level-systems
- Polarizer demo: x then y analyzer passes nothing, but inserting a 45-degree analyzer between them lets about 1/8 of photons through; this rules out each photon carrying a classical polarization bit (ch.2 §2.2.2, p. 16) → two-level-systems
- ⚠️ Spin precession (a magnetic field driving rotation of the spin) is not discussed explicitly in these chapters; only the general statement that a Hamiltonian generates a rotation (see unitary-time-evolution bullets). → two-level-systems

### Density matrices
- When we observe only part of a larger system (open system), states are not rays, measurements are not orthogonal projections, and evolution is not unitary (ch.2 §2.3.1, p. 17) → density-matrices
- For |psi>_AB = a|00>+b|11>, expectation values of observables on A alone equal tr(M_A rho_A) with rho_A = |a|^2|0><0| + |b|^2|1><1|; rho_A is self-adjoint, positive, with unit trace (ch.2 §2.3.1, p. 18) → density-matrices
- General bipartite pure state: rho_A = tr_B(|psi><psi|), the partial trace; it is self-adjoint, positive (nonnegative eigenvalues), unit trace, hence diagonalisable with real eigenvalues summing to 1 (ch.2 §2.3.1, pp. 19-20, eqs. 2.62-2.67) → density-matrices
- Pure state: rho = |psi><psi| with rho^2 = rho. Mixed: rho = sum p_a |a><a| with two or more terms, tr rho^2 = sum p_a^2 < 1; this is an incoherent mixture, meaning relative phases are inaccessible (ch.2 §2.3.1, pp. 20-21) → density-matrices
- Even if the whole system is in a ray, a subsystem generally is not; entangling A with B makes A's phases inaccessible, so "collapse" appears as A being in one of several states with assigned probabilities (ch.2 §2.3.1, p. 21) → density-matrices
- Example: (|up_z>+|down_z>)/sqrt2 gives sigma_1 = +1 with certainty, while the ensemble of up_z/down_z each with 1/2 is rho = I/2 and gives 1/2 along every axis; the half of an equal-weight entangled pair behaves incoherently (ch.2 §2.3.1, pp. 18-19) → density-matrices
- Qubit: rho(P) = (I + P.sigma)/2; rho is valid iff |P| <= 1, so single-qubit density matrices fill a unit ball (the "Bloch sphere" is really a ball); the surface |P|=1 are pure states; <n.sigma> = n.P, and P can be measured from three independent axes (ch.2 §2.3.2, pp. 21-22) → density-matrices
- Density operators form a convex set; pure states are exactly its extremal points; for d>2 the boundary of the set contains non-pure states, unlike the qubit ball (ch.2 §2.5.1, pp. 26-28) → density-matrices
- A mixed state has infinitely many decompositions into pure-state ensembles (e.g. I/2 = equal mix of up_z/down_z = equal mix of up_x/down_x = any antipodal pair), yet they are observationally indistinguishable; a pure state has only one preparation. A classical distribution, in contrast, is a simplex with unique decomposition (ch.2 §2.5.2, pp. 28-30) → density-matrices
- Ambiguity does not allow faster-than-light signalling: Bob's choice of measuring B in different bases prepares different ensembles for Alice but the same rho_A, so she cannot tell them apart without his classical message (ch.2 §2.5.3, pp. 30-31) → density-matrices
- Schmidt decomposition: any bipartite pure state is sum_i sqrt(p_i)|i>_A|i'>_B, with rho_A, rho_B having the same nonzero eigenvalues; Schmidt number > 1 means entangled, in which case the reduced states are mixed (ch.2 §2.4, pp. 23-26) → density-matrices
- HJW theorem: any two ensemble decompositions of rho_A come from purifications related by a unitary on B alone, so measuring B in a suitable basis realises any chosen ensemble; this is the general "quantum eraser" (ch.2 §2.5.4-2.5.5, pp. 31-36) → density-matrices
- Layer 3: in the open-system formulation, a state is a density operator, a measurement a POVM (probability tr(E_a rho)) and dynamics a trace-preserving completely positive map; the closed axioms are recovered via purification and dilations ("church of the larger Hilbert space") (ch.3 §3.3.3, p. 23) → density-matrices

### Decoherence
- The motivation for open systems: all realistic systems are imperfectly isolated and exchange energy and information with an environment; treat S+E as closed and look only at S (ch.2 §2.1, p. 3) → decoherence
- Entanglement with an inaccessible system destroys interference because the which-state information is in principle available in B; it is "decoherence", but it can be undone partly if B's information is erased by measuring suitably and relaying results (quantum eraser) (ch.2 §2.5.4, pp. 31-33) → decoherence
- Unitary on A+B then tracing out B gives a quantum channel E(rho) = sum_a M_a rho M_a^dagger with sum M_a^dagger M_a = I (Kraus/operator-sum representation); equivalently the trace-preserving completely positive (TPCP) map; any channel arises this way from a joint unitary, and Kraus operators are unique up to a unitary mixing (ch.3 §3.2.1, pp. 11-13) → decoherence
- Unitary evolution is the one-Kraus-operator case; two or more Kraus operators can turn pure states into mixed ones, which is decoherence (ch.3 §3.2.1, p. 13) → decoherence
- Depolarizing channel: with prob 1-p nothing, with prob p one of sigma_1,sigma_2,sigma_3 applied (each p/3). The Bloch ball shrinks uniformly, P' = (1-4p/3)P; at p=3/4 every state maps to I/2. It cannot be inverted since expanding the ball is not positive (ch.3 §3.4.1, pp. 24-27) → decoherence
- Dephasing channel: rho -> (1-p/2) rho + (p/2) sigma_3 rho sigma_3; diagonals unchanged, off-diagonals multiplied by (1-p); with scattering rate Gamma, coherences decay as e^{-Gamma t} and the state decoheres in a preferred basis (pointer basis) while populations stay fixed; the Bloch ball squashes towards the z axis (ch.3 §3.4.2, pp. 27-29) → decoherence
- No-pancake theorem: no channel can shrink only one Bloch component (it would amount to a transpose, which is not completely positive) (ch.3 §3.4.2, p. 29) → decoherence
- Why macroscopic objects look classical: for a heavy object (dust grain), superpositions of distinguishable positions lose coherence at the scattering rate, far faster than its damping time; locality of interactions picks position as the preferred basis; the same applies to Schrodinger's cat. For microscopic systems decoherence need not be fast (ch.3 §3.4.2, pp. 29-30) → decoherence
- If the environment states scattered by the two branches overlap by 1-epsilon, the decoherence rate is epsilon times the scattering rate (ch.3 §3.4.2, p. 30) → decoherence
- Dephasing shows up as decaying visibility of oscillations: for an atom in (|0>+e^{-i omega t}|1>)/sqrt2 with dephasing rate Gamma, Prob(+,t) = (1+e^{-Gamma t} cos omega t)/2, so Gamma can be measured from the decay of visibility (ch.3 §3.4.2, pp. 30-31) → decoherence
- Amplitude damping (spontaneous emission): Kraus operators M_0 = diag(1, sqrt(1-p)), M_1 = sqrt(p)|0><1|; excited population decays as e^{-Gamma t} (T1) while off-diagonals decay as e^{-Gamma t/2} (T2), so T2 = 2 T1 for pure amplitude damping; at long times the atom ends in the ground state (ch.3 §3.4.3, pp. 31-32) → decoherence
- Watching the environment (photon detectors) turns the channel into a POVM; detecting no photon still updates the state (M_0 reduces the excited amplitude by e^{-Gamma t/2}), so one can project onto |0> "by not detecting anything" (ch.3 §3.4.3, pp. 33-34) → decoherence
- Master equation: if evolution is Markovian (environment forgets quickly relative to coarse-graining and damping times, (dt)_damp >> (dt)_coarse >> (dt)_env), then rho_dot = L(rho) = -i[H,rho] + sum_a (L_a rho L_a^dagger - 1/2 L_a^dagger L_a rho - 1/2 rho L_a^dagger L_a) (Lindblad equation); the L_a are jump operators; an exactly Markovian description is impossible because information can flow back from the environment (ch.3 §3.5.1-3.5.2, pp. 34-37) → decoherence
- If the environment is monitored, each jump is detected and a pure state stays pure (stochastic Schrodinger equation / quantum trajectories); the average over trajectories reproduces the master equation (ch.3 §3.5.2, p. 38) → decoherence
- Measurement as decoherence: an unrecorded orthogonal measurement turns rho into sum E_a rho E_a, and the system is described by this mixture once entangled with the pointer, whether or not the pointer is observed (ch.3 §3.1.1, p. 8) → decoherence

### Uncertainty and noncommutativity (marginal coverage only)
- Observables A and B give a self-adjoint product only if they commute (ch.2 §2.1, pp. 4-5) → uncertainty-and-noncommutativity
- Rotations about different axes do not commute, giving [J_k, J_l] = i eps_klm J_m, and the Pauli matrices anticommute (ch.2 §2.2.1, p. 11) → uncertainty-and-noncommutativity
- A narrow pointer wavepacket (width Delta x) has velocity spread ~ hbar/(m Delta x), giving a "standard quantum limit" on resolution ~ sqrt(hbar t / m); a heavy pointer makes it negligible (ch.3 §3.1.1, p. 5) → uncertainty-and-noncommutativity
- ⚠️ The Heisenberg uncertainty relation itself is not stated or derived in these two chapters.

## Not covered / notes
- Requested but only marginally covered: uncertainty-and-noncommutativity (3 weak claims; no uncertainty relation); two-level-systems lacks explicit spin precession in a magnetic field.
- The chapter 3 extracted text is the October 2018 revision, not 2015.
- Level: university / specialist (graduate lecture notes; assumes linear algebra and basic QM).
