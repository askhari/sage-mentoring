---
source: cerezo-2021
concepts: [variational-algorithms, error-mitigation, nisq-era, primitives-sampler-estimator]
---

Accessed: full text of the arXiv version (2012.09265v2, Oct 2021), pages 1-23 read; page numbers are those of the arXiv PDF.

## General structure of a VQA
- A VQA defines a cost function C(theta) that encodes the problem, an ansatz (parametrized circuit/unitary) and possibly training data; a hybrid quantum-classical loop solves theta* = argmin C(theta). The quantum computer estimates the cost (or gradient) and a classical optimizer updates the parameters (§II, p. 2, Fig. 1) → variational-algorithms
- The cost can be written as a sum of functions of expectation values Tr[O_k U(theta) rho_k U(theta)^dagger]; during optimization only finite-statistics estimates are available (§II.A, p. 2) → variational-algorithms
- Desirable cost properties: faithful (minimum = solution), efficiently estimable on a quantum device but not classically, operationally meaningful (lower = better), and trainable (§II.A, pp. 2-3) → variational-algorithms
- For NISQ hardware the cost circuits must keep depth and ancilla count small, because of gate errors, few qubits and short coherence times (§II.A, p. 3) → variational-algorithms, nisq-era
- The ansatz can be problem-inspired (uses problem knowledge) or problem-agnostic; generically it is a product of L layers U_l(theta_l) (Eq. 4-5) (§II.B, p. 3) → variational-algorithms

## Ansatz types
- Hardware-efficient ansatz: gates taken from the device's native gate set and connectivity to avoid compilation depth overhead; versatile (can encode symmetries), suited to Hamiltonians resembling the device interactions; layered brick-like versions are common problem-agnostic choices but can have trainability problems when randomly initialized (§II.B.1, p. 3) → variational-algorithms
- Unitary coupled cluster (UCC) ansatz: problem-inspired, for quantum chemistry ground states; excites a reference state (usually Hartree-Fock) with single and double excitations (UCCSD); fermionic operators are mapped to qubits with Jordan-Wigner or Bravyi-Kitaev (§II.B.2, pp. 3-4) → variational-algorithms
- QAOA ansatz (quantum alternating operator ansatz): p alternating layers of a problem unitary e^{-i gamma H_P} and a mixer unitary e^{-i beta H_M}, inspired by Trotterized adiabatic evolution; parameters theta=(gamma,beta); compiling to native gates can give long circuits because of many-body terms and limited connectivity; a feasible subspace smaller than the Hilbert space can help (§II.B.3, p. 4) → variational-algorithms
- Variational Hamiltonian ansatz: Trotterized adiabatic state preparation for H = sum of Pauli strings, used in chemistry, optimization and simulation (§II.B.4, p. 4) → variational-algorithms
- Variable-structure ansatz: also optimizes the circuit structure (adding/removing elements), e.g. ADAPT-VQE, which greedily adds one term at a time; the exact problem is hard but greedy heuristics help (§II.B.5, p. 4) → variational-algorithms
- Other ansatz families: sub-logical (pulse-level) ansatz linked to optimal control, which can give on-the-fly calibration against coherent noise; hybrid ansatzes with classical parts; ansatzes for mixed states (§II.B.6-8, pp. 4-5) → variational-algorithms
- Expressibility: an ansatz is expressible if it explores the whole state space uniformly; measured by comparing its state distribution to the Haar distribution. Entangling capability is a separate quality measure (§II.B.9, p. 5) → variational-algorithms

## Gradients and optimizers
- Parameter-shift rule: for gates e^{i theta sigma} with Pauli sigma, the exact partial derivative of the cost is a difference of two cost evaluations at theta +/- alpha e_l, scaled by 1/(2 sin alpha); estimation accuracy is best at alpha = pi/4; despite resembling finite differences it gives the analytic gradient (§II.C.1, pp. 5-6) → variational-algorithms
- Higher-order derivatives follow by applying the parameter-shift rule repeatedly; the cost is a trigonometric series, so a classical model of it can be built around a point (§II.C.2, p. 6) → variational-algorithms
- Classical optimization in VQAs is expected to be NP-hard in general (many local minima) and is additionally hampered by finite-shot stochasticity, hardware noise and barren plateaus (§II.D, p. 6) → variational-algorithms
- Gradient-based optimizers fall under stochastic gradient descent (e.g. Adam); adaptive-shot methods save measurements, and an unbiased gradient estimate is possible even with a single shot. Quantum natural gradient uses a metric tensor of the state and usually converges in fewer iterations (§II.D.1, p. 6) → variational-algorithms
- Gradient-free options include SPSA (random-direction finite difference, avoids computing all gradient components), and sequential local fitting of the trigonometric dependence on one parameter at a time, which has no hyperparameters. Meta-learning optimizers also exist (§II.D.2, p. 7) → variational-algorithms
- Landscapes are non-convex, so general convergence guarantees are hard; for simplified landscapes SGD guarantees exist, and in a convex region parameter-shift gradients give smaller complexity bounds than value-only methods (§II.D.3, p. 7) → variational-algorithms

## VQE and QAOA as applications
- VQE: first VQA, designed as a near-term alternative to adiabatic preparation and phase estimation, whose depth is beyond NISQ. Cost C(theta) = <psi(theta)|H|psi(theta)>; by the Rayleigh-Ritz variational principle C >= E_G with equality at the ground state, so the cost is faithful. H is written as a linear combination of Pauli strings, so C is a sum of Pauli expectation values (§III.A, p. 7; §III.A.1, p. 8) → variational-algorithms
- VQE needs O(1/epsilon^2) measurements for precision epsilon, versus O(log(1/epsilon)) for quantum phase estimation; "accelerated VQE" interpolates between the two with alpha-QPE (§III.A.7, p. 9) → variational-algorithms, primitives-sampler-estimator
- Excited states can be found with orthogonality-constrained VQE (penalty term on overlap with the found ground state), subspace expansion, subspace VQE and multistate contracted VQE (§III.A.2-5, pp. 8-9) → variational-algorithms
- QAOA targets combinatorial problems (Max-Cut, SAT): objective encoded in a problem Hamiltonian H_P via Pauli-Z operators; cost C(gamma,beta) = <psi_p|H_P|psi_p> with p alternating rounds; the landscape is non-convex with many local optima, so work focuses on optimizers needing few quantum calls (gradient-based, derivative-free, reinforcement learning) (§III.B, pp. 10-11, Eq. 8, Fig. 5) → variational-algorithms
- Further application areas: dynamical simulation, linear systems, factoring, PCA, compilation, error correction, QML (classifiers, autoencoders, generative models, QNNs), foundations and metrology (§III.A-G, pp. 9-15) → variational-algorithms
- VQAs for dynamics use shallow circuits to avoid the depth growth of Trotter-Suzuki product formulas (§III.A, "Dynamical quantum simulation", p. 9) → variational-algorithms, nisq-era

## Barren plateaus and trainability
- Barren plateau (BP): partial derivatives of the cost vanish exponentially with system size on average, so the landscape is flat and exponentially many shots/precision are needed to resolve a descent direction, for gradient-based and gradient-free methods alike; this can erase a potential quantum advantage (§IV.A.1, p. 15) → variational-algorithms
- Cause 1, expressibility/randomness: deep unstructured randomly initialized circuits become 2-designs at polynomial depth and show BPs; the ansatz is problem-agnostic and must search an exponentially large space (§IV.A.1, p. 16) → variational-algorithms
- Cause 2, cost locality: for shallow layered ansatzes, global costs (comparing objects in exponentially large spaces) give BPs, while local costs (single-qubit level) give gradients vanishing only polynomially if depth is at most logarithmic in n (§IV.A.1, p. 16) → variational-algorithms
- Other BP sources: learning a scrambling unitary (any ansatz gives BPs), and perceptron-based QNNs with much entanglement (§IV.A.1, p. 16) → variational-algorithms
- Cause 3, noise: noise can induce BPs regardless of the ansatz; noise through the circuit drives the state toward the maximally mixed state, which occurs when depth grows linearly or more with system size (§IV.A.1, p. 16) → variational-algorithms, error-mitigation
- Mitigation by parameter initialization: use patterns of good QAOA parameters; choose some parameters at random and set the rest so the circuit reduces to identity; correlate parameters; layer-by-layer training (which may cause abrupt trainability transitions); pretraining with classical neural networks (§IV.A.2, pp. 16-17) → variational-algorithms
- Mitigation by ansatz choice: structured, problem-inspired ansatzes (UCC, QAOA ansatz) are usually trainable even when randomly initialized; other remedies are local cost functions, tailored optimizers and QCNN/tree-tensor-network architectures, which do not show BPs (§IV.A.2, p. 17; §III.F.5, p. 14) → variational-algorithms
- Linear-systems VQA example: the global Hamiltonian cost has exponentially vanishing gradients; fixed by a local Hamiltonian with the same ground state or a hybrid ansatz (§III.C.1, p. 11) → variational-algorithms

## Efficiency of measurement and expectation values
- Even without BPs, estimating expectation values is not guaranteed to be efficient; early resource estimates for chemistry VQE gave astronomically many measurements (§IV.B, p. 17) → variational-algorithms, primitives-sampler-estimator
- Standard approach: write the operator as H = sum_i c_i sigma_i with Pauli strings sigma_i, each diagonalizable with one layer of single-qubit rotations; drawback is the large number of terms (about n^4 distinct strings for chemical Hamiltonians with n orbitals) (§IV.B, p. 17) → primitives-sampler-estimator
- Grouping commuting Pauli strings into simultaneously measurable sets cuts measurements; the partition maps to graph coloring, minimum clique cover or network flow (§IV.B.1, p. 17) → primitives-sampler-estimator
- Qubit-wise commuting (QWC) grouping was the first method and is the simplest, but does not change asymptotic scaling for chemistry; general commuting grouping (with quadratically more gates) reduces measurement scaling to n^3; factorizing the two-electron tensors reaches quadratic or even linear scaling (§IV.B.1, p. 17) → primitives-sampler-estimator
- Optimized shot allocation: the optimal number of shots per Pauli term is proportional to |c_i| times the standard deviation of that term, not uniform; random allocation with those probabilities gives unbiased estimates even with one shot (§IV.B.2, p. 18) → primitives-sampler-estimator, variational-algorithms
- Classical shadows (randomized measurements) let every shot contribute to all Pauli expectations, with the number of measurements scaling logarithmically in the number of terms; neural-network (RBM) tomography lowers sampling variance at the cost of small bias (§IV.B.3-4, p. 18) → primitives-sampler-estimator
- The precision cost O(1/epsilon^2) for VQE reflects statistical shot noise in estimating the energy (§III.A.7, p. 9) → primitives-sampler-estimator

## Noise, resilience and error mitigation
- Noise effects on VQAs: slower training, biased landscape (noisy optimum may differ from noise-free one), and corrupted final cost; observed training is typically slowed because incoherent noise flattens the landscape and gradients decay exponentially with depth (§IV.C.1, p. 18) → variational-algorithms, error-mitigation
- Under local Pauli noise the cost concentrates exponentially in depth around the maximally-mixed-state value; this does not matter for QAOA (cost computed classically after sampling) but matters for VQE energy accuracy, motivating error mitigation. The noise-induced BP results do not account for error mitigation, whose scope is an open question (§IV.C.1, pp. 18-19) → error-mitigation, variational-algorithms
- Inherent resilience to coherent noise: since the optimizer only sees sampled observables, a coherent parameter error U(theta+delta) can be compensated on the fly; seen experimentally in superconducting qubits with errors reduced by over an order of magnitude; requires optimizing faster than calibration drift and enough ansatz flexibility (§IV.C.2, p. 19) → error-mitigation, variational-algorithms
- Resilience to incoherent noise: optimal parameter resilience (OPR) means global minima of the noisy cost coincide with noise-free ones; shown for variational compilation, open for other VQAs (§IV.C.2, p. 19; §III.D, p. 12) → error-mitigation
- Quantum error mitigation (QEM) suppresses errors in expectation values through classical post-processing of measurement results, not by encoding qubits (§IV.C.3, p. 19) → error-mitigation
- Zero-noise extrapolation (ZNE): deliberately boost noise (extra noisy pulses, longer gates), measure at several noise levels and extrapolate to zero noise; variants are Richardson, exponential and multi-parameter least-squares fits; cannot fully remove errors, and variance grows so more shots are needed (§IV.C.3, p. 19, Fig. 7) → error-mitigation
- Probabilistic error cancellation (PEC): given a full noise characterization (e.g. gate set tomography), invert the noise with extra random gate operations and post-process outcomes (the inverse is unphysical) to obtain unbiased expectation values, at a sampling overhead (§IV.C.3, pp. 19-20) → error-mitigation
- Clifford-data approaches: compare exactly simulable near-Clifford circuits to their noisy hardware results, then calibrate/regress to correct observables or tune the extrapolation (§IV.C.3, p. 20) → error-mitigation
- Symmetry verification: for ansatzes preserving symmetries (particle or spin number) errors break the symmetry, so measure the symmetry and discard violating outcomes (like error detection); unlike other methods it can recover the state itself (§IV.C.3, p. 20) → error-mitigation
- Further QEM: subspace expansion (works better for coherent than stochastic noise); multi-copy purification-like methods suppressing errors exponentially in the number of copies M but needing more qubits; measurement-error mitigation for correlated readout errors (§IV.C.3, p. 20) → error-mitigation
- Quantum error correction is beyond NISQ qubit budgets but could complement mitigation; variational circuits (QVECTOR etc.) can find hardware-tailored codes (§III.E, pp. 12-13) → error-mitigation
- Outlook: new mitigation strategies are expected to improve accuracy by orders of magnitude and be built into cloud platforms (§VI, pp. 22-23) → error-mitigation

## NISQ positioning and quantum advantage
- NISQ devices have limited qubits, limited connectivity and errors limiting depth; devices of 50-100 qubits reach "quantum supremacy" only for contrived tasks, while practical quantum advantage is not yet achieved and fault tolerance may be years or decades away (§I, p. 1) → nisq-era
- The paper claims VQAs are the leading strategy for quantum advantage on NISQ devices because an optimization/learning approach can account for all NISQ constraints at once, keeping circuits shallow and so limiting noise, in contrast to fault-tolerant-era algorithms (§I, p. 1) → nisq-era, variational-algorithms
- Implicit requirement: the cost must not be efficiently classically computable, else no advantage (§II.A, p. 3) → nisq-era
- Advantage candidates: chemistry/materials (e.g. FeMo cofactor, strongly correlated systems), nuclear and particle physics (lattice gauge theory), QAOA for optimization, and QML (§V.A-C, pp. 20-22) → nisq-era
- QAOA arguments for advantage: provable guarantees at p=1, p=1 cannot be efficiently simulated classically, performance cannot get worse with larger p; but some problems need p to grow with size (§V.C.1, p. 22) → nisq-era
- Conditions for advantage: avoid BPs, keep measurement cost efficient, control noise; requires larger and better devices; the authors expect VQAs to move from proposal to implementation and to benchmark new hardware (§IV intro p. 15; §V p. 20; §VI p. 23) → nisq-era, variational-algorithms
- Outlook: better scaling analyses, quantum-aware optimizers, adaptive and application-specific ansatzes, hybrid classical-quantum models, hardware improvements (§VI, pp. 22-23) → variational-algorithms
- ⚠️ The paper states that VQAs "appear to be the best hope" for quantum advantage (abstract, p. 1); this is the authors' view, not an established result, and the paper itself lists unresolved trainability, accuracy and efficiency issues (§IV) → nisq-era

## Not covered / level
- Not covered: Qiskit-specific API (Sampler/Estimator primitives as software objects) is not mentioned; only the underlying idea (Pauli-term measurement estimation) is.
- Level: university / specialist review (graduate-level physics and computer science).
