---
source: childs-qa
concepts: [query-model-and-oracles, phase-kickback, deutsch-jozsa, bernstein-vazirani-and-simon, quantum-fourier-transform, phase-estimation, shor-algorithm, grover-search, hamiltonian-simulation, quantum-complexity, post-quantum-cryptography]
---

Accessed: full extracted text of the PDF (local file), A. M. Childs, "Lecture Notes on Quantum Algorithms", University of Maryland, title page dated 17 April 2025 (graduate level; assumes an intro quantum information course). Page numbers "p. N" are the PRINTED page numbers; the PDF page = printed + 8. Everything below was read directly in the text. Ch. 1 is a very short review; the notes do not re-derive Deutsch-Jozsa, Bernstein-Vazirani or the Shor factoring reduction (they are assumed known).

### query-model-and-oracles
- Query complexity: the input is a black-box transformation and the goal is to learn a property of it with as few queries as possible; the advantage is that lower bounds can be proved. An efficient query algorithm plus an explicit circuit for the box gives an efficient algorithm for an explicit problem (ch. 1, §1.6, p. 3) → query-model-and-oracles
- Example of a black-box problem: Simon's problem, f: Z_2^n → S with f(x)=f(y) iff y = x ⊕ t, goal is to learn t (§1.6, p. 3) → query-model-and-oracles
- Any classical efficiently computable x ↦ f(x) gives a quantum map |x,y⟩ ↦ |x, y⊕f(x)⟩ by computing reversibly, XORing the answer into an ancilla and uncomputing; this does not necessarily give |x⟩ ↦ |f(x)⟩ unless f can also be efficiently inverted (§1.4, pp. 2-3) → query-model-and-oracles
- Formal model: a function f: S → T with S ⊆ Σ^n; total if S = Σ^n, partial otherwise. Query complexity depends on the computation model: D(f) deterministic, R_ε(f) randomized (error ε), Q_ε(f) quantum (error ε); for constant ε, R_ε and Q_ε are Θ of the ε=1/3 versions because error can be reduced by repetition (§21.1, p. 97) → query-model-and-oracles
- A query algorithm starts from an x-independent state and alternates unitaries with oracle calls O_x: |ψ_t^x⟩ = U_t O_x … U_1 O_x |ψ⟩ (§21.2, p. 98) → query-model-and-oracles
- Bit-flip oracle: Ô_x|i,b⟩ = |i, b⊕x_i⟩, the linear extension of a reversible map; acts as identity on ancillas (§21.2, p. 98, eq. 21.2) → query-model-and-oracles
- Phase oracle: conjugating the bit-flip oracle with Hadamards on the answer qubit gives O_x|i,b⟩ = (−1)^{b x_i}|i,b⟩ (eq. 21.3). It is essential to include a component (b=0) on which the oracle acts trivially; with only the flip |i⟩ ↦ (−1)^{x_i}|i⟩ one cannot distinguish x from its complement (§21.2, p. 98) → query-model-and-oracles
- For a d-ary alphabet, the bit-flip oracle becomes |i,b⟩ ↦ |i, b+x_i mod d⟩ and a Fourier transform of the second register gives the phase oracle with ω_d^{b x_i} (§21.2, p. 98) → query-model-and-oracles
- Acceptance probability of a t-query algorithm on x ∈ {0,1}^n is a polynomial in x_1..x_n of degree at most 2t (each query raises the amplitude degree by at most 1), so Q_ε(f) ≥ approx-degree(f)/2 (Lemma 21.1, §21.3, pp. 98-99) → query-model-and-oracles
- Classical query complexities of OR: D = n, R = Θ(n); quantum Q(OR) = Θ(√n) (§21.1 p. 97; §21.6 p. 101) → query-model-and-oracles
- Parity of n bits needs ≥ n/2 queries even with bounded error (polynomial method, symmetrization, §21.5, pp. 99-100), so the Deutsch parity trick applied pairwise (Q_0(parity) ≤ n/2) is optimal: a problem with no real quantum speedup (just factor 2) → query-model-and-oracles
- Exactly counting marked items needs Ω(n) queries (it would determine parity) (§21.5, p. 100) → query-model-and-oracles

### phase-kickback
- The "well-known phase kickback trick" is invoked to justify that Hadamards around a bit-flip oracle give the phase oracle (−1)^{b x_i}; the text does not derive it (§21.2, p. 98, eq. 21.3) → phase-kickback
- In phase estimation the controlled operation Σ_x |x⟩⟨x| ⊗ U^x applied to |x⟩ ⊗ |φ⟩ with U|φ⟩ = e^{iφ}|φ⟩ yields phases e^{iφx} on the control register, leaving the eigenvector unchanged (§4.3, p. 19, eqs. 4.15-4.16) → phase-kickback
- Phase estimation is also described as von Neumann's measurement: the transformation |ψ⟩|z⟩ ↦ U^z|ψ⟩|z⟩ is exactly the evolution under H⊗p for a pointer in the momentum basis (§27.5, p. 137) → phase-kickback

### deutsch-jozsa
- Not covered as a topic. Only Deutsch's problem (parity of 2 bits) is mentioned as solvable exactly with one quantum query (§21.5, pp. 99-100) → deutsch-jozsa

### bernstein-vazirani-and-simon
- QFT over Z_2^n is H^{⊗n}, with characters χ_y(x) = (−1)^{x·y}; the text says the reader has already seen how it solves Simon's problem (§4.1, p. 17, eq. 4.2). Bernstein-Vazirani is not mentioned → bernstein-vazirani-and-simon
- Simon's problem is the HSP with G = Z_2^n, H = {0,s}: a very simple quantum algorithm, but any classical algorithm needs exponentially many queries in n (§5.3, p. 22) → bernstein-vazirani-and-simon
- Classical lower-bound idea: with unstructured range, nothing beats random queries until a collision is seen; by the birthday problem that takes Ω(√(|G|/|H|)) queries (§5.3, p. 22) → bernstein-vazirani-and-simon
- Theorem 5.1: if G has N subgroups whose only common element is the identity, any deterministic classical HSP algorithm needs Ω(√N) queries (adversary argument; adaptable to randomized) (§5.3, pp. 22-23) → bernstein-vazirani-and-simon
- Classical algorithms are fine when G has only polynomially many subgroups (e.g. Z_p, Z_{2^n} with n+1 subgroups) (§5.3, p. 23) → bernstein-vazirani-and-simon
- General abelian HSP algorithm (generalizes Simon): superposition over G, compute f, discard the output to get a random coset state, apply QFT_G, measure to get a character trivial on H; intersect the kernels of O(log|G|) samples to recover H (§6.1, pp. 25-27) → bernstein-vazirani-and-simon
- Why Fourier works: the coset-state mixture ρ_H is invariant under the regular representation of G, so after the QFT it is diagonal and measuring loses no information (§6.1, p. 26) → bernstein-vazirani-and-simon
- The probability a sampled character fails to cut the current candidate subgroup K ≠ H is ≥ 1/2, giving the O(log|G|) sample count (§6.1, p. 27) → bernstein-vazirani-and-simon

### quantum-fourier-transform
- Abelian QFT: F_G = (1/√|G|) Σ_{x,y} χ_y(x)|y⟩⟨x| over a complete set of characters; unitary by orthogonality of characters (§4.1, p. 17, eq. 4.1) → quantum-fourier-transform
- QFT over Z_{2^n}: F|x⟩ = (1/√2^n)Σ_y ω_{2^n}^{xy}|y⟩ factors as a tensor product of single-qubit states |z_k⟩ = (|0⟩ + ω^{x 2^k}_{2^n}|1⟩)/√2, where qubit k depends only on the n−k least significant bits of x (§4.2, pp. 17-18) → quantum-fourier-transform
- Circuit: Hadamards plus controlled phase rotations R_k = diag(1, ω_{2^k}); uses O(n²) gates (§4.2, p. 18) → quantum-fourier-transform
- Approximate QFT: dropping rotations R_k with k = Ω(log n) leaves O(n log n) gates and gives precision 1/poly(n) (§4.2, p. 18) → quantum-fourier-transform
- QFT over Z_N for general N (not a power of 2): implemented approximately with phase estimation on the add-1-mod-N operator, whose eigenvectors are the Fourier basis states; use n = O(log N) bits of precision, map |x̃,0⟩ ↦ |x̃,x⟩ and run it backwards to erase |x⟩ (§4.4, pp. 19-20) → quantum-fourier-transform
- QFT over any finite abelian group = tensor product of QFTs over its cyclic factors (§4.4, p. 20) → quantum-fourier-transform

### phase-estimation
- Problem: given U (circuit or black box for controlled-U^j) and an eigenvector |φ⟩ with U|φ⟩ = e^{iφ}|φ⟩, output φ to desired precision (§4.3, p. 19) → phase-estimation
- Procedure for n-bit estimate: prepare (1/√2^n)Σ_x |x⟩|φ⟩, apply Σ|x⟩⟨x| ⊗ U^x, apply inverse QFT on the first register, measure. If φ = 2πy/2^n exactly, the output is exact with certainty (§4.3, p. 19, eqs. 4.14-4.16) → phase-estimation
- In general Pr(y) = (1/2^{2n}) · sin²(2^{n−1}φ)/sin²(φ/2 − πy/2^n) (eq. 4.17), strongly peaked at the best n-bit approximation, which is returned with probability at least 4/π² (§4.3, p. 19) → phase-estimation
- Cost: precision μ costs O(1/μ) applications of U (unless high powers of U can be applied cheaper) (§19.3, p. 89) → phase-estimation
- Used as a subroutine: QFT over Z_N (§4.4), quantum counting (§19.3), Hamiltonian simulation via quantum walk (§28.2), and measuring an efficiently simulable operator (von Neumann = phase estimation, §27.5) → phase-estimation

### shor-algorithm
- Discrete log: log_g x is the smallest non-negative α with g^α = x; g^α is computed efficiently by repeated squaring, but no known polynomial algorithm inverts it classically (§5.1, p. 21) → shor-algorithm
- Diffie-Hellman security relies on discrete log being hard; if Eve can take discrete logs she recovers the key (it is open whether breaking DH implies computing discrete log) (§5.2, pp. 21-22) → shor-algorithm
- Shor's discrete log as an abelian HSP in Z_N × Z_N with f(α,β) = x^α g^β, hiding the subgroup H = {(α, −α log_g x)}; after QFT the measurement gives (ν log_g x, ν) with ν uniform in Z_N; if ν is invertible mod N divide to get the log; success probability φ(N)/N = Ω(1/log log N) per try (§5.4, pp. 23-24) → shor-algorithm
- Works for any cyclic group with unique element representation and efficient multiplication; N (the order) is assumed known, otherwise learn it with period finding (§5.4, p. 24) → shor-algorithm
- Factoring N reduces to discrete log in Z_N^×, so discrete log is at least as hard; but discrete-log Shor needs |Z_N^×| = φ(N), which is as hard as factoring, so this does not by itself give a factoring algorithm (§5.4, p. 23) → shor-algorithm
- Factoring reduces to order finding (observed by Miller): order of g is the smallest r with g^r = 1; factor L via order finding in Z_L with a random g ∈ Z_L^× (details not given: assumed from a first course) (§9.1, p. 37) → shor-algorithm
- Period finding over Z: since r need not divide a known N, one works with inputs {0..N−1} and Fourier-samples over Z_N; if no bound on r is known, start from M=2 and keep doubling, with only poly(log r) overhead (§9.1, p. 37) → shor-algorithm
- Steps: uniform superposition, compute f, measure second register to get (1/√n)Σ_j|x_0+jr⟩, QFT over Z_N, measure k. If r | N, the outcome is a uniformly random multiple of N/r (§9.1, pp. 37-38) → shor-algorithm
- General case: Pr(k) = sin²(πkrn/N)/(nN sin²(πkr/N)), peaked near multiples of N/r; the integer nearest to jN/r is observed with probability ≥ about c/r with a constant c (≈ 4/π² for large n) (§9.1, pp. 38-39, eqs. 9.9-9.14) → shor-algorithm
- Classical post-processing by continued fractions: ⌊jN/r⌉/N is within 1/2N of j/r; any fraction p/q with |p/q − x| < 1/(2q²) appears as a convergent (Hardy-Wright Thm 184), so j/r is a convergent if r² < N; N large enough recovers r efficiently (§9.1, p. 39) → shor-algorithm
- Period finding over the reals (irrational period, e.g. Hallgren's Pell's equation algorithm): needs a pseudoperiodic discretization, Ω(1/poly log r) success per sample, two samples with coprime j, j' and N ≥ 3r² (Lemma 9.1, §9.2, pp. 39-41) → shor-algorithm
- Complexity statements: discrete log over an elliptic curve over F_p runs in time poly(log p); Shor takes a comparable number of steps for factoring and discrete log regardless of the group, though elliptic-curve group operations are costlier than integer multiplication (§7.3, p. 32) → shor-algorithm
- Pell's equation, the unit group of Z[√d] (Hallgren), and the abelian group decomposition algorithm (uses order finding + Smith normal form) are further applications of the same period-finding/HSP template (chs. 6, 8, 9) → shor-algorithm
- Shor's algorithm is the base of Part II: "quantum algorithms for algebraic problems", which use the QFT and typically get an exponential (or at least superpolynomial) speedup (Preface, p. vii) → shor-algorithm

### grover-search
- Unstructured search: black box f: S → {0,1}, |S|=N, marked set M; classical query complexity is Θ(N) even for the decision version (§19.1, p. 87) → grover-search
- Grover: start from the uniform state |S⟩ and alternate the reflection about marked items (Σ_{x∈M} 2|x⟩⟨x| − 1, two queries to f) and the reflection 2|S⟩⟨S| − 1 (no queries); t = O(√(N/|M|)) iterations give constant overlap on the marked state (§19.1, p. 87) → grover-search
- Lower bound: Ω(√(N/|M|)) queries are needed (§19.1, p. 87) → grover-search
- Optimality proofs: polynomial method gives Q(OR) = Ω(√n) via Markov's inequality on the symmetrized polynomial (Lemma 21.3, §21.6, pp. 100-101); adversary method gives Q_ε(OR) ≥ ((1−2√(ε(1−ε)))/2)·√n (§23.3, p. 113) → grover-search
- Grover finds a unique marked item with probability 1−o(1) in (π/4)√n + o(1) queries (§23.3, p. 113) → grover-search
- Quantum-walk view: search on the complete graph; classical hitting time O(1/(δε)) = O(N/|M|), quantum O(1/√(δε)) = O(√(N/|M|)); each walk step costs O(1) queries; Grover's diffusion 2|S⟩⟨S|−1 is a kind of coin-free walk on the complete graph (§§18.4, 19.2, pp. 84-88) → grover-search
- Amplitude amplification: boosts a subroutine with success probability p to constant probability using O(1/√p) rounds; modeled as a two-state Markov chain (§19.3, pp. 88-89) → grover-search
- Quantum counting: phase estimation on the quantized chain, whose eigenphases are ±arccos(1−p) ≈ ±√(2p); estimate p with precision ν in O(√p/ν) steps, and |M| to multiplicative precision ρ in O(√(N/|M|)/ρ); exact counting needs Ω(N) queries (§19.3, p. 89) → grover-search
- Search with locality constraints (graph): expanders searchable in O(√N); d-dimensional lattice: O(√N) for d ≥ 3, O(√N log N) for d = 2, no speedup for d = 1 (§19.4, pp. 89-90) → grover-search
- Collision problem (one-to-one vs two-to-one): Θ(n^{1/3}) quantum queries (algorithm: query m=Θ(n^{1/3}) items, then Grover-search for a repeat; lower bound by polynomial method, Aaronson Ω(n^{1/5}) → Shi Ω(n^{1/3}), Kutin's proof presented) versus Θ(√n) classical (ch. 22, pp. 103-105). The point: modest structure yields only a polynomial speedup → grover-search
- Oblivious amplitude amplification (applied to a block-encoded operator with unknown input state, via W R W† R) is used inside LCU simulation, with cost O(1/s) (§28.3, p. 142) → grover-search

### hamiltonian-simulation
- Setting: for time-independent H, |ψ(t)⟩ = e^{−iHt}|ψ(0)⟩ (ħ=1). H on n qubits is "efficiently simulable" if for any t, ε a circuit of poly(n,t,1/ε) gates approximates e^{−iHt} within ε in operator norm (§§27.1-27.2, p. 133) → hamiltonian-simulation
- Simulating general Hamiltonians is BQP-hard (promise-BQP-complete even under natural restrictions) (§27.2, p. 133) → hamiltonian-simulation
- Time dependence poly(t) is the best possible in general (no "fast-forwarding"): o(t) queries impossible for sparse H, proved by reduction from parity (Ω(n) queries) with a 2-sparse path-graph Hamiltonian whose weights entries √(i(n−i+1)/n) (eq. 28.1) make |0,0⟩ reach |n, parity⟩ in time O(n) (§28.1, p. 139; also §27.2, p. 133) → hamiltonian-simulation
- Easy cases: constant number of qubits (cost poly(log 1/ε) by Solovay-Kitaev); rescaling by poly factors; basis change U H U†; Hamiltonians diagonal in the computational basis with efficiently computable entries, using |a,0⟩ ↦ |a,d(a)⟩ ↦ phase ↦ uncompute (§27.2, p. 134) → hamiltonian-simulation
- Product formulas: e^{−i(H1+H2)t} = lim (e^{−iH1t/m}e^{−iH2t/m})^m (Lie-Trotter); first order needs m = O((νt)²/ε), ν = max‖H_j‖, i.e. cost ∝ t² (§27.3, pp. 134-135) → hamiltonian-simulation
- Symmetric (second-order) formula e^{−iH1t/2m}e^{−iH2t/m}e^{−iH1t/2m} needs fewer steps; with higher-order formulas, cost O(t^{1+δ}) for any fixed δ > 0 (§27.3, p. 135) → hamiltonian-simulation
- Sums of polynomially many terms (e.g. k-local Hamiltonians, particle in a potential discretized, spin models) are handled by splitting into easy terms and composing; commutators i[H1,H2] can also be simulated (§27.3, pp. 134-135) → hamiltonian-simulation
- Sparse Hamiltonians: sparse means poly(log N) nonzeros per row, with efficient row computation. Method: make graph bipartite by simulating σx⊗H, edge-color the graph (Lemma 27.1: d² colors computable locally), simulate each color class (direct sum of 2×2 blocks) and combine with the product formula (§27.4, pp. 135-136) → hamiltonian-simulation
- Quantum-walk simulation (Szegedy-type, Berry-Childs): build a walk whose eigenvalues are e^{±i arccos(λ/X)}, X ≥ max_j Σ_k|H_jk|, run phase estimation, apply phase e^{−iλt}, uncompute. Needs 1/δ = Θ(Xt/ε) precision so complexity is linear in t and poly in 1/ε; refined version: O(‖H‖t/√ε + d‖H‖_max t) = O(d‖H‖_max t/√ε) queries for d-sparse H; matches the Ω(t) bound in t (§28.2, p. 140) → hamiltonian-simulation
- LCU (Taylor series): truncated series Ũ(t) = Σ_{k≤K}(−iHt)^k/k!; error ≤ e^{‖H‖t}(‖H‖t)^{K+1}/(K+1)!, so K = O(log(‖H‖t/ε)/loglog(‖H‖t/ε)). Write H = Σα_ℓ H_ℓ (unitary, Hermitian terms, e.g. Pauli strings), implement Σβ_j V_j with PREPARE/SELECT: W = B† select(V) B, success amplitude 1/s (§28.3, pp. 140-142) → hamiltonian-simulation
- LCU cost: query complexity O(τ log(τ/ε)/loglog(τ/ε)) with τ = d²‖H‖_max t, i.e. poly-logarithmic in 1/ε (better than product formulas in ε); needs oblivious amplitude amplification (W R W† R) because the input is unknown; with s=2 the amplitude 1/2 becomes 1, analogous to Grover with one marked item of 4 (§28.3, pp. 140-142) → hamiltonian-simulation
- Block encoding: U block-encodes A if A = (⟨0|⊗I)U(|0⟩⊗I); needs ‖A‖ ≤ 1, can rescale A/α; d-sparse efficiently computable matrices are block-encoded (R†C encodes A/d); closure under products and sums (§29.1, pp. 143-144) → hamiltonian-simulation
- Quantum signal processing (Low-Yoder-Chuang): interleaving the rotation W(x)=e^{i arccos(x)σ_x} with z rotations realizes matrices with polynomial entries P(x),Q(x) iff deg P ≤ k, deg Q ≤ k−1, parities k and k−1 mod 2, and |P|²+(1−x²)|Q|² = 1 on [−1,1] (Lemma 29.1, §29.2, p. 144) → hamiltonian-simulation
- Qubitization: a block encoding splits into 2D invariant subspaces on which U acts as the reflection R(λ); alternating U, U† with phases e^{iθ(2Π−1)} applies QSP in each subspace, giving a block encoding of P(A). Theorem 29.2: for a degree-d polynomial f with |f| ≤ 1/2 on [−1,1] there is a circuit block-encoding f(A) using d uses of U, U† and one controlled-U (§29.3, pp. 146-147) → hamiltonian-simulation
- QSP simulation: use the Jacobi-Anger expansion e^{it cosθ} = J_0(t)+2Σ i^k J_k(t) cos(kθ) truncated at K = O(t + ln(1/ε)/ln(e + ln(1/ε)/t)) (stated as tight), then robust oblivious amplitude amplification with constant overhead. Result: sparse-Hamiltonian simulation with optimal query complexity in both t and ε (§29.4, pp. 147-148) → hamiltonian-simulation
- Simulation is also the engine for continuous-time quantum walks and adiabatic algorithms; the notes motivate it by Feynman's original proposal (ch. 27 intro, p. 133) → hamiltonian-simulation
- Glued-trees problem: a continuous-time quantum walk traverses it in poly time, while no classical algorithm can; a black-box (query) exponential separation (§17.4-17.5, pp. 75-77) → hamiltonian-simulation
- ⚠️ Adiabatic quantum computing (Part VI, chs. 30-33) treated separately in the text; not requested here → hamiltonian-simulation

### quantum-complexity
- "Efficient" = poly(size of input in bits) gates with uniform circuits (a fixed Turing machine outputs the n-th circuit in poly(n) time) (§§1.5-1.6, p. 3) → quantum-complexity
- Bounded error convention: decision problems with success probability bounded above 1/2; otherwise Ω(1) when answers are checkable; repetition reduces error (§1.6, p. 3) → quantum-complexity
- Any efficient classical computation can be run efficiently on a quantum computer via reversible computation (§1.4, p. 3) → quantum-complexity
- Solovay-Kitaev: gate set choice only changes cost by polylog factors, so even polynomial quantum speedups are robust to the gate set (Thm 2.1, ch. 2, p. 7); circuit error accumulates at most linearly in the number of gates (Lemma 2.2, p. 7) → quantum-complexity
- Counting argument: most n-qubit unitaries need exponentially large circuits of 1- and 2-qubit gates (§1.3, p. 2) → quantum-complexity
- Fault tolerance assumed: the threshold theorem (noise below roughly 10^-3 to 10^-4 depending on the model) allows arbitrarily long computation with arbitrarily small error; the notes assume it throughout (§1.7, p. 4) → quantum-complexity
- Hamiltonian simulation is BQP-hard / promise-BQP-complete in general (§27.2, p. 133) → quantum-complexity
- Quantum computers get no exponential speedup for completely unstructured problems: search needs Ω(√n) queries "exponentially many in the number of bits needed to specify an index" (§22.1, p. 103) → quantum-complexity
- The collision problem shows that mild structure gives only a polynomial gain (Θ(n^{1/3}) vs Θ(√n)), unlike the HSP whose group structure gives much smaller query complexity (§22.1, p. 103) → quantum-complexity
- Query vs computational: the (nonabelian) HSP has polynomial quantum query complexity, poly(log|G|) queries (Ettinger-Høyer-Knill), but this does not imply an efficient quantum algorithm since the post-processing may be inefficient. Number of subgroups of G is 2^{O(log²|G|)} (§10.3, pp. 45-46) → quantum-complexity
- Efficient quantum algorithms for the HSP are known for all abelian groups and only a few nonabelian groups (§5.3, p. 22; §10.1, p. 44) → quantum-complexity
- Nonabelian HSP in S_n would give graph automorphism / isomorphism, where no efficient classical algorithm is known; an efficient dihedral-group HSP (standard method) would solve poly(n)-unique shortest vector (Regev) (§10.1, pp. 43-44) → quantum-complexity
- Query lower bounds are the main route to limits on quantum algorithms (polynomial method, adversary method; Part IV, Preface p. vii; §21.1 notes that lower bounds on explicit-input complexity are notoriously hard) → quantum-complexity
- The text does not discuss relations such as BQP vs P/NP/PSPACE; apart from "BQP-hard" in §27.2 no class inclusions are stated → quantum-complexity
- Quantum walk hitting time gives a generic square-root speedup over classical random-walk hitting time via phase estimation (§18.4, pp. 84-86) → quantum-complexity

### post-quantum-cryptography
- Diffie-Hellman (first public-key protocol) is insecure against a quantum computer because discrete log can be solved efficiently by Shor's algorithm (§5.3, p. 22; §5.2, pp. 21-22) → post-quantum-cryptography
- Shor's algorithm also breaks elliptic curve cryptography, the "main competitor to RSA"; only implementation details differ from the integer case, no new quantum ideas needed (ch. 7 intro, p. 29; §7.3, p. 32) → post-quantum-cryptography
- ECC is viewed as more secure than RSA per key size because best classical attacks on EC discrete log are generic (e.g. Pollard rho, O(√p)), so smaller keys are used; but Shor needs comparable steps for both (§7.2-7.3, pp. 32) → post-quantum-cryptography
- Elliptic curve group: points of y² = x³+ax+b over F_p plus the point at infinity, with chord-and-tangent addition formulas; secure curves avoid supersingular/anomalous cases (§§7.1-7.2, pp. 29-32) → post-quantum-cryptography
- Lattice cryptosystems (based on a unique shortest vector assumption) are among the few proposals "not compromised by Shor's algorithm"; an efficient quantum algorithm for the dihedral HSP via the standard method would break them (Regev) (§10.1, p. 44) → post-quantum-cryptography
- Studying limits of quantum HSP algorithms may suggest cryptosystems robust to quantum attacks (§10.1, p. 44) → post-quantum-cryptography
- The text does not mention standardized post-quantum schemes (NIST, hash-based, code-based) by name; no resource estimates for breaking RSA/ECC are given → post-quantum-cryptography

Not covered / weak: deutsch-jozsa (only a remark on Deutsch's 2-bit parity), bernstein-vazirani (not mentioned), phase-kickback (only named, not derived), BQP and its relations to P/NP/PSPACE (only "BQP-hard"), post-quantum standards (none).
Level: university/graduate to specialist (lecture notes, rough, may contain mistakes per the preface).
