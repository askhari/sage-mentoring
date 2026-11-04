---
source: grover-1996
concepts: [grover-search, query-model-and-oracles, quantum-complexity]
---

Accessed: full text of the updated arXiv version (quant-ph/9605043) of the STOC 1996 paper, 8 pages, via local extraction. Formulas were partly garbled in the extraction, so the claims below rely on the surrounding prose. Page numbers are those of the arXiv version.

## Problem and classical baseline
- The problem is an unsorted database of N items, exactly one of which satisfies a given condition. That item must be found, and no sorting exists that could help. (§1.0, p. 1; formal version §2, p. 3) → grover-search
- Once an item is examined, one step tells whether it satisfies the condition. (§1.0, p. 1) → grover-search
- The best classical method is to examine items one by one without repeating. On average this takes about N/2 looks (the "N/2" is read from the context of the garbled formula). (§1.0, p. 1) → grover-search
- The Summary says any classical algorithm, deterministic or probabilistic, needs about N/2 looks to find the item with probability 1/2 (reading garbled symbols from context). (Summary, p. 1) → grover-search
- The quantum algorithm finds the item in O(√N) steps. It is within a small constant factor of the fastest possible quantum algorithm. (Summary, p. 1; §1.1, p. 2) → grover-search
- Before this result, the limit for structure-free search was generally assumed to be O(N), since a classical algorithm clearly takes N steps. (§1.1, p. 2) → grover-search

## Building blocks
- Quantum algorithms work with an amplitude vector (complex numbers) over the states. The probability of a state is the squared magnitude of its amplitude. The transition matrix must be unitary so that probability is conserved. (§1.2, p. 2) → grover-search
- The "fair coin flip" matrix M = (1/√2)[[1,1],[1,−1]] sends 0 to an equal superposition and 1 to a superposition with the phase of the state-1 amplitude inverted. Phase has no classical probabilistic analog. (§1.2, p. 2) → grover-search
- Applying M to each of n bits starting from all zeros gives equal amplitude 1/√(2^n) in all 2^n states. (§1.2, p. 2) → grover-search
- Applying M to every bit of an arbitrary starting string gives equal-magnitude amplitudes whose sign is set by the parity of the bitwise dot product x·y. This is the Walsh-Hadamard transformation. (§1.2, pp. 2–3) → grover-search
- Grover says this operation, or the closely related Fourier transform, is part of what makes quantum algorithms more powerful than classical ones. (§1.2, p. 3) → grover-search
- The third needed operation is a selective rotation of the phase of certain states. It is a diagonal matrix of phases e^{jφ}. It leaves each state's probability unchanged. (§1.2, p. 3) → grover-search

## Algorithm
- Step (i): initialize to the uniform amplitude 1/√N in all N states. This takes O(log N) steps (Walsh-Hadamard). (§3, p. 3) → grover-search
- Step (ii): repeat O(√N) times the following two unitary operations. The precise number of repetitions matters, with a pointer to [BBHT96]. (§3, p. 3) → grover-search
- Step (ii)(a), selective phase inversion: if C(S)=1, rotate the phase of that state by π radians. If C(S)=0, leave the state unchanged. (§3, p. 3) → grover-search
- Step (ii)(b), the diffusion transform D: D_ij = 2/N for i≠j and D_ii = −1+2/N. It is implemented as D = W R W. Here W is the Walsh-Hadamard matrix and R is a phase matrix. R leaves state 0 alone (R_00=1) and flips the sign of every other state. (§3, p. 3; Theorem 1, p. 5) → grover-search
- Step (iii): sample the final state. If a unique state S_ν satisfies C(S_ν)=1, the final state is S_ν with probability at least 1/2. (§3, p. 3) → grover-search
- D can be written as −I + 2P, where P is the projection matrix with every entry 1/N. P²=P, and P applied to a vector gives a vector whose components all equal the mean. Hence D²=I and D is unitary. (§4, p. 4) → grover-search
- Applied to a vector v, D gives component i equal to A + (A − v_i), where A is the average of the components. This is the "inversion about average" operation. (§4, p. 4) → grover-search
- Intuition: if all amplitudes are about 1/√N and one is negative, inversion about average leaves the others almost unchanged. The negative one becomes positive and grows by about 2/√N. (§4, p. 4, Figs. 1–2) → grover-search
- In the loop, the amplitude of the selected state is first inverted by a phase rotation and then inversion about average is applied. Each iteration increases the amplitude of the target by O(1/√N). (§4, pp. 4–5) → grover-search
- Theorem 3: if the target amplitude is k with 0<k<1/√2 and every other amplitude is l>0 with l>1/√(2N), then one round (a)+(b) increases k by more than 1/(2√N). The remaining amplitudes stay positive. (§4 p. 5; proof §5, pp. 6–7) → grover-search
- Consequence: some M<√N exists such that after M iterations k exceeds 1/√2. The probability is then above 1/2, since it is the square of the amplitude. (§4, p. 5) → grover-search
- D can be implemented as a product of three "local" transitions (W, R, W), each acting on one bit or as a phase. This is why the non-local-looking D is physically valid. (§5, p. 5, Theorem 1) → grover-search
- The proofs in §5 (Theorems 2–3 and Corollaries 2.1–2.2) cover the amplitude formulas after D and the conservation of probability. Theorem 3 requires N≥9 for part of the argument. (§5, pp. 6–7) → grover-search

## Optimality
- A matching lower bound is due to [BBBV96]: without information about the structure, a quantum system needs at least Ω(√N) steps. The algorithm's O(√N) is therefore within a constant factor of the optimum. (§1.1, p. 2; §6, p. 7) → grover-search
- The BBBV argument: an algorithm running T steps is sensitive to only O(T²) queries, because if more queries are possible, the answer to at least one can be flipped without changing the behavior. To decide correctly when all C(S)=0, T must be Ω(√N). If T<Ω(√N), flipping one query answer would give a wrong result. (§6, p. 7) → grover-search
- Grover credits Ethan Bernstein with providing the lower-bound argument. [BBHT96] gives a direct proof and tight bounds, showing the algorithm is within a few percent of the fastest possible quantum algorithm. (§6, p. 7; §9, p. 8) → grover-search

## Multiple solutions and extensions
- The algorithm assumes a unique solution. For multiple solutions, one option is to check a range of solution counts (k, k+1, ..., 2k) for various k. Within about log N repetitions one can determine whether at least one solution exists. [BBHT96] discusses this in detail. (§8, obs. 3(i), p. 8) → grover-search
- The other option is to perturb the problem randomly [MVV87] so that a unique solution holds with high probability. [VV86] gives a scheme that turns any algorithm for unique-solution NP-search into one for general NP-search. (§8, obs. 3(ii), p. 8) → grover-search
- The search algorithm does not use knowledge of the problem's structure. Grover suggests it might be combined with structure-exploiting algorithms such as Shor's. (§8, obs. 2, p. 7) → grover-search

## Oracle and condition model
- The abstracted problem has N=2^n states, labelled by n-bit strings. A unique state S_ν has C(S_ν)=1 and all others have C(S)=0. C(S) can be evaluated in unit time for any S. (§2, p. 3) → query-model-and-oracles
- The paper never uses the word "oracle". The condition C(S) plays that role. Step (ii)(a) is a conditional phase rotation: part of the system senses the state and decides whether to rotate the phase. (§3, p. 3) → query-model-and-oracles
- The implementation must leave no trace of the state, so that paths to the same final state are indistinguishable and can interfere. It involves no classical measurement. (§3, p. 3) → query-model-and-oracles
- The lower bound is stated in terms of queries. An algorithm of T steps is sensitive to only O(T²) queries C(S). (§6, p. 7) → query-model-and-oracles
- The conditional phase shift is easier if the function is computed at each point than if it is retrieved from memory, because computing avoids quantum memory. If table lookup is needed, in principle the data could stay in classical memory and only the sampling system be quantum, provided the system can "feel" the values without leaving a trace. (§7 (iii)–(iv), p. 7) → query-model-and-oracles
- Obs. 1 relates this to interaction-free measurements: a small probability of examining the target may be enough to find it without examining all items. (§8, obs. 1, p. 7) → query-model-and-oracles

## Complexity
- SAT asks whether some combination of n binary variables satisfies a set of clauses. There are N=2^n candidates, and the key issue in NP-completeness is whether it can be solved in time polynomial in n, i.e. polynomial in log N. (§1.1, p. 1) → quantum-complexity
- If search could be reduced to a finite power of log N rather than O(√N), that would give a polynomial-time algorithm for NP-complete problems. The paper does not claim this. Its O(√N) bound is far from it. (§1.1, p. 1) → quantum-complexity
- Quantum computers were shown to be at least as powerful as classical ones. They were shown to be more powerful on specialized problems. Shor (1994) showed efficient factoring, a problem with no known efficient classical algorithm. (§1.0, p. 1) → quantum-complexity
- The algorithm needs only Walsh-Hadamard transforms and conditional phase shifts. Grover judges these simpler to build than the large-scale Fourier transform needed for Shor-type factoring. (§7 (i)–(ii), p. 7) → quantum-complexity

## Not covered
- post-quantum-cryptography: this version of the paper says nothing about cryptography, DES or key search. No claim is available.

Concepts requested but not covered: post-quantum-cryptography.
Level: specialist (original research paper, short and readable).
