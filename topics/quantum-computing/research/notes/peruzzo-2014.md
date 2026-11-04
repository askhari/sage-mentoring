---
source: peruzzo-2014
concepts: [variational-algorithms, nisq-era, phase-estimation, primitives-sampler-estimator]
---

Accessed: arXiv v1 (1304.3061v1, April 2013) extracted full text, pp. 1-10 (main text pp. 1-5, Appendix pp. 7-10). Pages below are arXiv pages. The published Nat. Commun. 5, 4213 (2014) version may differ in wording and numbering.

## Variational algorithm (VQE idea)
- Two-part scheme: a quantum processing unit (QPU) evaluates the expectation value of H for a prepared state (Algorithm 1); a classical processor (CPU) minimizes it by updating the state parameters (Algorithm 2). Fig. 1 shows the feedback loop (p. 1-2) → variational-algorithms
- Any Hamiltonian can be written as a sum of Pauli-operator products with real coefficients (Eq. 1); by linearity, ⟨H⟩ is the weighted sum of the expectation values of each Pauli term (Eq. 2) (p. 1) → variational-algorithms
- Requirement: the number of terms must be polynomial in system size. They list electronic-structure Hamiltonians, the Ising and Heisenberg models, sums of n-fold tensor products, and k-sparse Hamiltonians (via a decomposition into 1-sparse parts) as examples (p. 1-2) → variational-algorithms
- Each term is a tensor product of Paulis, measured as a separate quantum calculation. The CPU adds the results with their weights (Fig. 1 caption, p. 2; Appendix step 3(a), p. 7) → variational-algorithms
- Variational basis: the lowest-eigenvalue eigenvector is the state that minimizes the Rayleigh-Ritz quotient ⟨ψ|H|ψ⟩/⟨ψ|ψ⟩ (Eq. 3, p. 2). This is the variational principle in the form the paper uses. ⚠️ The paper never writes "⟨H⟩ ≥ E0" explicitly; it is implied by "lowest eigenvalue minimizes the quotient" → variational-algorithms
- Algorithm 2 procedure (Appendix, p. 7): (1) design a parametrized circuit {θi} and define the objective f(θ)=⟨ψ(θ)|H|ψ(θ)⟩; (2) at each iteration, compute all Pauli-term expectations on the QPU and sum them classically; (3) pass f to a classical minimizer (e.g. gradient descent or Nelder-Mead), which proposes the next θ; repeat until converged → variational-algorithms
- At the end, the final parameter set is a compact recipe for rebuilding the eigenvector, so other properties can be computed later (p. 2, p. 5) → variational-algorithms
- Ansatz: states preparable efficiently have only polynomially many parameters, so the classical search explores only polynomially many dimensions. Example: the unitary coupled cluster ansatz e^(T-T†)|Φ_ref⟩, with the Hartree-Fock state as reference (p. 3; Appendix pp. 7-8). They say no efficient classical algorithm for this ansatz is known → variational-algorithms
- Two ansatz strategies for larger problems: chemistry-motivated ansätze (such as UCC), or a "device ansatz", the set of states the hardware can prepare. The device ansatz has a depth capped by qubit coherence time and gives a variationally optimal solution for the given resources, possibly only approximately right (as Hartree-Fock is in classical chemistry) (p. 5) → variational-algorithms
- Entanglement in the ansatz: separable states are a doubly exponentially small part of state space. The ability to reach entangled states adds paths to convergence and will matter for large-scale versions. The HeH+ ground state has small but non-zero entanglement (tangle) (p. 4) → variational-algorithms
- Classical optimizer choice (Appendix, p. 8): they used Nelder-Mead with restarts. Gradient descent did not converge to the ground state under their experimental noise (Poissonian photon statistics, accidental counts), while Nelder-Mead reached the global minimum in most runs → variational-algorithms
- Excited states: repeat the procedure on (H-λ)², the "folded spectrum" method, which converges to the eigenvector closest to λ. Scanning λ gives other eigenpairs. The cost is a polynomial overhead, since the term count grows quadratically (Appendix, p. 8) → variational-algorithms

## HeH+ demonstration
- Hardware: reconfigurable silicon-waveguide photonic chip. Photon pairs come from spontaneous parametric down-conversion. The chip has single-qubit rotations (8 thermal phase shifters) and one CNOT-type entangling gate, and prepares an arbitrary 2-qubit pure state with mean fidelity above 99%. Measurement is by single-photon detector coincidence counts (Fig. 2, p. 3) → variational-algorithms
- Problem: ground-state energy of HeH+ in a minimal basis (STO-3G, FCI). This gives a 4x4 Hamiltonian written as a sum of one- and two-qubit Pauli terms (Eq. 5, p. 3-4; Eq. 11, p. 7). Coefficients depend on the nuclear separation R and were computed with the PSI3 package → variational-algorithms
- Result at R=90 pm: the energy and the overlap with the true ground state converge within about 100 optimization steps despite noise (Fig. 3, p. 4) → variational-algorithms
- Bond-dissociation curve from the ground states of 79 Hamiltonians (79 values of R). Equilibrium bond length R=92.3±0.1 pm and energy -2.865±0.008 MJ/mol, after correcting a systematic error. More than 96% of the data are within chemical accuracy of the exact FCI curve (Fig. 4, pp. 4-5) → variational-algorithms
- Errors: a constant systematic shift of about 50 kJ/mol, attributed to imperfect down-conversion photon states, circuit imperfections, and unbalanced coupling. The statistical standard deviation of ⟨Hi⟩ was about 37 kJ/mol, from Poissonian photon statistics. Error grows with R because the first and second excited states become degenerate, which hampers the minimizer (Appendix, pp. 9-10) → variational-algorithms
- Cost of the run: each expectation value came from four two-qubit Pauli measurements. About 2000-4000 two-fold events per second, about 100 points per optimization run, about 158 hours in total. The chip needed 17 s of cooling per step (about 5% duty cycle) (Appendix, p. 10) → variational-algorithms

## Scaling, limitations
- Per-evaluation cost O(|h_max|²·M/p²) for M Pauli terms at precision p. A classical simulation needs 2^n amplitudes and O(2^n) operations per expectation value. The authors therefore claim an exponential advantage per iteration, provided the Hamiltonian and ansatz assumptions hold. Total cost per iteration is O(n^r |h_max|² M/p²) (Appendix "Computational Scaling", pp. 8-9) → variational-algorithms
- Limitation: convergence to the final ground state still respects the QMA-complete difficulty of the ground-state problem. The scaling argument concerns a single iteration, not the number of iterations (Appendix, p. 9) → variational-algorithms
- Limitation: because the many separate Pauli-term runs are independent, the method is sensitive to variation in state preparation between them. They say this needs further investigation (p. 5) → variational-algorithms
- Unresolved questions they leave to future work: which ansatz to choose, and how to classify device ansätze by overlap with chemical ground states (p. 5) → variational-algorithms
- They argue that classically optimizing the reduced states of each Hamiltonian term separately would hit the N-representability problem (QMA-hard). Keeping a global quantum state avoids this (p. 2) → variational-algorithms
- Qubit count and ancillas: the approach needs no control or auxiliary qubits, only standard measurement techniques. In the 2-qubit case the measurements are the same as in Bell-inequality experiments (p. 5) → variational-algorithms

## NISQ-era motivation
- Main motivation: QPE needs fully coherent evolution, which the authors say is far beyond the tens to hundreds of gates achievable in the short term. Practical applications may need millions or billions of gates (p. 1) → nisq-era
- Their alternative replaces one long coherent evolution with many short ones and so "enhances the potential of the quantum resources available today and in the near future" (abstract, p. 1; p. 5) → nisq-era
- The quantum part is small and fixed-depth (state preparation plus measurement), and the classical computer handles the search. Circuit depth can be capped by the coherence time of the physical qubits (device ansatz, p. 5) → nisq-era
- The classical optimizer must be robust to noisy objective evaluations. Nelder-Mead was chosen for this reason (Appendix, p. 8) → nisq-era
- Expected benefit: devices with a few tens of qubits could be implemented with dramatically fewer resources than the best known alternative (p. 5) → nisq-era
- The term "NISQ" itself does not appear in this paper (it is from 2013, before the term existed). The argument is made in terms of coherence time and gate counts → nisq-era

## Comparison with phase estimation
- QPE gives an exponential speedup and costs O(1/p) quantum operations for precision p. It takes a given eigenvector and finds its eigenvalue, and needs O(1/p) successive applications of e^(-iHt) (p. 1) → phase-estimation
- VQE-style Algorithm 1 trades this for a coherence time of O(1) per measurement after state preparation, plus O(1/p²) repetitions per term. This is a polynomial increase in repetitions relative to QPE, and in exchange the coherence requirement is greatly reduced (p. 2) → phase-estimation
- QPE needs many controlled n-qubit operations in series, so it demands many components and long coherence. In their scheme a small number of n-qubit gates is reused many times in parallel runs. Adding control to arbitrary unitaries is hard or impossible on current architectures (p. 5) → phase-estimation
- Numerical example: QPE for a 4x4 Hamiltonian like HeH+ needs at least 12 CNOT gates, versus 1 in their method (p. 5) → phase-estimation
- Both QPE and Algorithm 1 need a good approximation of the ground state as input. Earlier state-preparation proposals (adiabatic evolution, quantum Metropolis) also need long coherent evolution, whereas the variational Algorithm 2 provides the state with short evolution (p. 2) → phase-estimation
- The effect of errors within each individual short run is the same as in QPE (p. 5) → phase-estimation

## Measurement of Pauli expectation values
- A quantum device can efficiently estimate the expectation of a tensor product of any number of Pauli operators. This takes constant time per measurement, and the operators' spectra are bounded (p. 2; Appendix p. 9) → primitives-sampler-estimator
- To reach precision p for a term with coefficient h, about O(|h|²/p²) repetitions of preparation and measurement are needed. Over M terms the total is O(|h_max|² M/p²) (p. 2; Appendix p. 9) → primitives-sampler-estimator
- Statistical error comes from the shot-noise nature of counting (Poissonian), is intrinsic to estimating quantum expectation values, and scales with the square root of the count rate. It can be reduced at only sublinear cost in measurement time. Measured example: 37 kJ/mol standard deviation over 50 trials at about 1500 coincidences/s (Appendix, p. 9) → primitives-sampler-estimator
- The weighted sum of the term expectations is computed classically on the CPU ("classical adder" in Fig. 1), and the total is passed to the optimizer (p. 2, Fig. 1) → primitives-sampler-estimator
- In the demo, each ⟨H⟩ was reconstructed from four two-qubit Pauli measurements (Appendix, p. 10). The chip phases implement both state preparation and the choice of measurement basis σα⊗σβ, so the CPU computes the chip settings at each iteration (Appendix, p. 9) → primitives-sampler-estimator

## Not covered / level
- Not covered: Qiskit-specific primitives (Sampler/Estimator API), the name "VQE", and any gate-based circuit implementation. The paper uses photonic hardware and does not use the terms "Estimator" or "Sampler".
- Level: specialist (research article, Nature Communications), readable by university students with quantum-computing background.
