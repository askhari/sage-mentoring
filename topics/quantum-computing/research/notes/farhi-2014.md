---
source: farhi-2014
concepts: [variational-algorithms, hamiltonian-simulation]
---

Accessed: full extracted text of arXiv:1411.4028v1 (16 pp.), read completely.

## Problem setup
- Combinatorial optimization is given by n bits and m clauses; the objective C(z) counts satisfied clauses, C = sum of clauses C_α, each acting on only a few bits (§I, p. 2, eq. 1) → variational-algorithms
- Approximate optimization asks for a string z with C(z) close to the maximum of C (§I, p. 2) → variational-algorithms
- C is viewed as an operator diagonal in the computational basis of the 2^n-dimensional space (§I, p. 2) → variational-algorithms

## The QAOA state
- Phase-separation unitary U(C,γ)=e^{-iγC}, a product of commuting clause terms; since C has integer eigenvalues, γ can be restricted to [0, 2π] (§I, p. 2, eq. 2) → variational-algorithms
- Mixer B is the sum of single-bit σx operators; U(B,β)=e^{-iβB} is a product of commuting one-qubit rotations, β in [0, π] (§I, p. 2, eqs. 3-4) → variational-algorithms
- Initial state |s⟩ is the uniform superposition over all strings (the product of |+⟩ states, the top eigenstate of B) (§I eq. 5, p. 2; §VI, p. 10) → variational-algorithms
- For integer depth p ≥ 1, the state |γ,β⟩ applies U(C,γ1), U(B,β1), ..., U(C,γp), U(B,βp) in alternation to |s⟩, so there are 2p angles (§I, p. 3, eq. 6) → variational-algorithms
- The circuit has depth at most mp+p even without exploiting problem structure (§I, p. 3) → variational-algorithms
- Gates act at most as locally as the objective's clauses (abstract, p. 1); the circuit depth grows linearly in p times (at worst) the number of constraints (abstract, p. 1) → variational-algorithms
- Objective to optimize: F_p(γ,β)=⟨γ,β|C|γ,β⟩, and M_p is its maximum over angles (§I, p. 3, eqs. 7-8) → variational-algorithms

## Monotonicity and p → ∞
- M_p ≥ M_{p-1}, because a depth p-1 optimization is a constrained case of depth p (§I, p. 3, eq. 9) → variational-algorithms
- M_p tends to the true maximum of C(z) as p → ∞ (stated §I eq. 10, p. 3; proved §VI, pp. 10-11) → variational-algorithms
- Proof idea: the quantum adiabatic algorithm with H(t)=(1-t/T)B+(t/T)C, starting from |s⟩ (the top state of B), reaches the top state of C for large T. The Perron-Frobenius theorem guarantees a nonzero gap at the top of the spectrum (B has non-negative off-diagonal elements) (§VI, p. 10) → variational-algorithms
- A Trotterized approximation of that evolution is exactly an alternation of U(C,γ) and U(B,β), with the sum of the angles equal to the total run time. Small angles (good Trotter accuracy) plus long run time force large p (§VI, pp. 10-11) → hamiltonian-simulation
- The same Trotter link is what gives the p → ∞ result: angles can always be chosen so that F_p is as close to M_p as wanted (§VI, p. 11) → variational-algorithms
- The p → ∞ guarantee may mislead: p may need to be exponentially large in n, and adiabatic evolution aims at overlap with the optimal string. On the ring of disagrees the p=1 state has ratio 3/4 but exponentially small overlap with the optimal strings (§VI, p. 11) → variational-algorithms
- Contrast with the adiabatic algorithm: its success probability is generally not monotonic in run time T (extreme 20-qubit Max2Sat example cited from ref. [4]), whereas the QAOA approximation improves with p. The paper also cites an example, with symmetric Hamming-weight objective, where QAA gets trapped for subexponential time but QAOA with p=1 succeeds (§VI, p. 11) → variational-algorithms

## Running it: sampling and angle choice
- Procedure: choose p and angles, prepare |γ,β⟩, measure in the computational basis, evaluate C(z), repeat. Enough repetitions give a string with C(z) near or above F_p. The difficulty is choosing good angles (§I, p. 3) → variational-algorithms
- Repeated measurement samples C(z) in [0, m] with mean F_p(γ,β), so the expectation is estimated by averaging samples. About m log m repetitions give an outcome of at least F_p-1 with probability 1-1/m (§II, p. 6) → variational-algorithms
- Concentration: for fixed degree v and fixed p, the variance of C(z) is at most of order m (std ~ √m), so a sample mean of order m^2 shots is within 1 of F_p with probability 1-1/m (§III, p. 7, eq. 30) → variational-algorithms
- Angle strategy 1 (fixed p): search a fine grid over [0,2π]^p × [0,π]^p. This is efficient because the partial derivatives of F_p are bounded by O(m²+mn) (§I, p. 3; §VIII, p. 15) → variational-algorithms
- Angle strategy 2: use the quantum computer as a subroutine that evaluates F_p, called by a classical optimizer that maximizes the smooth function F_p. This also applies when p grows with n (§VIII, p. 15) → variational-algorithms
- Angle strategy 3: for fixed p and bounded clause participation per bit, classical preprocessing finds the optimal angles, and the quantum computer is then run only at those angles (§II, p. 4; §VIII, p. 15) → variational-algorithms

## Classical computability of F_p for bounded degree
- Shown for MaxCut with C_{jk}=(1-σz_jσz_k)/2. Each edge term (Heisenberg-conjugated by the p layers) involves only qubits within graph distance p of the edge, because gates away from the edge commute through and cancel (§II, pp. 4-5, eqs. 11-16) → variational-algorithms
- Because |s⟩ is a product state, each edge contribution depends only on a subgraph of size independent of n when the degree is bounded. F_p is therefore a weighted sum over subgraph types, with weights read off the graph (§II, pp. 4-6, eqs. 17, 24-25) → variational-algorithms
- The largest subgraph is a tree with q_tree = 2[(v-1)^{p+1}-1]/[(v-2)] qubits for max degree v (2p+2 if v=2), independent of n and m. Computing F_p needs a Hilbert space of dimension at most 2^q_tree, which does not grow with n (§II, p. 6, eq. 26) → variational-algorithms
- Caveat: for large p this classical computation may be beyond current technology, and it may need space doubly exponential in p (§II, p. 6; §VIII, p. 15) → variational-algorithms

## MaxCut results
- Ring (2-regular): with numerical maximization for p=1..6, M_p = n(2p+1)/(2p+2) (conjectured for all p), so the ratio approaches 1 for large p independent of n. The circuit depth can be made 3p by splitting the edge sum into even and odd edges (§IV, pp. 7-8) → variational-algorithms
- 3-regular graphs, approximation ratio defined as C(z) from the algorithm divided by the maximum of C (§V, p. 8) → variational-algorithms
- For p=1 on any connected 3-regular graph, the worst-case ratio is at least 0.6924. The analysis uses the three subgraph types (g4, g5, g6), counts of isolated triangles T and crossed squares S, and the bound of at most 3n/2-S-T satisfiable edges. The minimum of the bound is numerical, attained at s=t=0 (§V, pp. 8-10, eqs. 32-35) → variational-algorithms
- This p=1 guarantee is weaker than known classical algorithms (§V, p. 10) → variational-algorithms
- p=2 on 3-regular graphs (partial): the largest subgraph is a 14-vertex tree, giving 0.7559 numerically. For bipartite graphs with few short loops the ratio tends to 0.7559. The algorithm at p=2 cannot tell bipartite graphs from those with many long odd loops (§V, p. 10) → variational-algorithms

## Variant and outlook
- A variant for constrained search spaces (e.g. independent set): the Hilbert space is spanned by legal strings only, B is the hypercube adjacency matrix restricted to legal strings, the start state is the empty set |z=0⟩, and U(B,b)=e^{-ibB} uses a real b. Monotonicity and the p → ∞ limit are argued again via a two-stage adiabatic path (§VII, pp. 12-14, eqs. 37-47) → variational-algorithms
- For p=1 the variant is a continuous-time quantum walk on the graph of legal strings. With no edges (hypercube), b=π/2 gives the all-ones string (§VII, p. 14) → variational-algorithms
- The authors hope fixed or slowly growing p can solve combinatorial search problems beyond what classical algorithms achieve (§VIII, p. 15) → variational-algorithms

## Not covered
- nisq-era: the paper says nothing about near-term or noisy devices, which is expected for a 2014 paper. Its only hardware remark is that classical simulation of F_p for large p may exceed "current classical technology" (§II, p. 6). It also thanks the Google Quantum AI Lab in the acknowledgements (p. 15), which has no technical content.
- Qiskit or software specifics: none.

Level: university/specialist (research paper; physics-notation heavy, intro section I and the §VIII conclusion are readable).
