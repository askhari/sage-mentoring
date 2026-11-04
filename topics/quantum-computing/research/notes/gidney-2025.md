---
source: gidney-2025
concepts: [shor-algorithm, post-quantum-cryptography, surface-code, resource-estimation, fault-tolerant-gates]
---

Accessed: full text of arXiv:2505.15917v1 (21 May 2025), pp. 1-25 incl. references; appendix A (pp. 26+) not read. Page numbers are those of the paper. Preprint, not peer-reviewed at access. Quantum-complexity not covered (only a passing remark on asymptotics).

## Headline estimate and assumptions

- Main result: a 2048-bit RSA integer could be factored in under a week by a quantum computer with under a million noisy physical qubits (abstract, p. 1; §3.2, p. 20). → shor-algorithm
- Hardware assumptions, the same as in 2019: square grid of qubits with nearest-neighbour connections, uniform gate error rate 0.1% (1 error per 1000 gates, uniform depolarizing noise), surface code cycle time 1 microsecond, control-system reaction time 10 microseconds (abstract, p. 1; §3.2, p. 20). → shor-algorithm
- Comparison: Gidney+Ekerå 2019 estimated 8 hours with 20 million noisy qubits; the new paper cuts qubits about 20x (to about 1 million) but takes longer (abstract, p. 1; §4, p. 21). → shor-algorithm
- The longer runtime comes mainly from performing more Toffoli gates and using fewer magic state factories than in 2019. Compared with Chevignard-Fouque-Schrottenloher 2024 (CFS24), the Toffoli count falls by over 100x (abstract, p. 1). → shor-algorithm
- Detailed physical count: 897,864 physical qubits, reported as "one million" to leave slack (about 100K slack for unforeseen cold-storage overhead during streaming) (§3.2, pp. 18-20). → resource-estimation
- Runtime derivation: about 12.07 hours per shot, expected 9.2 shots, about 4.63 days; dividing by the 93.3% chance of no logical error gives 4.96 days, rounded up to "a week" (§3.2, p. 20). → shor-algorithm
- Figure 1 (p. 2) compares historical physical-qubit estimates for RSA-2048 under comparable assumptions (2012 to 2021 works) and shows the downward trend. → shor-algorithm

## Algorithmic ideas (high level)

- Context: before CFS24 it was believed that factoring an n-bit number needed at least about 1.5n logical qubits (n was thought the minimum because modular arithmetic "required" an n-qubit register). GE21 used about 3n logical qubits and 3 billion Toffolis (§1, p. 3). → shor-algorithm
- CFS24 showed approximate modular exponentiation with only small intermediate values. Combined with Ekerå-Håstad period finding it needs only about (0.5+ε)n logical qubits, but at about 2 trillion Toffolis (roughly 1000x more Toffolis for 6x less space) (§1, p. 3). → shor-algorithm
- Approximate residue arithmetic: represent values modulo a product L of many small primes (about 22 bits each) and add modulo each prime separately. L must be at least N^m so no wraparound occurs. Register sizes then scale with log log N, not log N (§2.1, pp. 3-5). → shor-algorithm
- Modular exponentiation g^e mod N is rewritten as a sum, a dot product between bits of the residues and a classically precomputed table. Additions are truncated to f kept bits, which gives a small "modular deviation" that is acceptable for period finding. The needed f grows like log log N (§2.1, pp. 5-7). → shor-algorithm
- Heuristic: a prime set P with L mod N tiny (deviation below 2^-f) is found by random search. The paper states this as unproven Assumption 1 and gives an example set of 25,000 22-bit primes for the RSA-2048 challenge number (§2.1, p. 6). → shor-algorithm
- Approximate period finding: the approximate function is only approximately periodic, so the output is measured with a "superposition mask" (a uniform random offset added in the output register) that hides the low bits. Mask size S = sqrt(ε) gives a shot failure probability of at most 2·sqrt(ε). The masked success rate is estimated numerically and relies on Assumption 2 (§2.2, pp. 7-13). → shor-algorithm
- Ekerå-Håstad period finding is used in place of Shor's original 2n-qubit input register. It needs n/2 + n/s input qubits, works only for RSA integers (two similar-sized primes), and needs s+1 shots. It recovers d = p+q-2 and then p and q from a quadratic (§2.3, pp. 13-14). → shor-algorithm
- Larger s means fewer input qubits, fewer multiplications and fewer primes, so s = 3 is both smaller and faster than s = 1. The chosen parameters for n = 2048 are s = 8, 21-bit primes, f = 33, m = 1280 input qubits (§2.3, p. 14; Table 5, p. 18). → shor-algorithm
- Arithmetic optimizations: replace modular multiplications by additions via precomputed short discrete logarithms; windowing (lookup tables); merging computation of one prime's sum with uncomputation of the previous one; deferring and merging phase corrections; a modular adder costing about 2.5n Toffolis (§2.4, pp. 14-16). → shor-algorithm
- Logical cost: essentially all work is additions, lookups and "phaseups". Table 5 gives for n = 2048: 6.5e9 expected Toffolis and 1399 logical qubits (peak 1409 during loop4), with Pdeviant = 1.25% (§3.1, pp. 16-18). → shor-algorithm
- Table 5 also gives scaling to other sizes: n = 1024 needs 1.1e9 Toffolis and 742 logical qubits; n = 4096 needs 4.0e10 Toffolis and 2692 logical qubits (§3.1, p. 18). → shor-algorithm
- Stated conclusion: the author sees no way to cut qubits by another order of magnitude under the same physical assumptions and cannot plausibly claim 100,000 noisy qubits would suffice (§4, p. 21). → shor-algorithm
- The qubit reduction comes mainly from three sources: approximate residue arithmetic, yoked surface codes for idle logical qubits, and magic state cultivation (abstract, p. 1; §4, p. 21). → shor-algorithm

## Implications for RSA and migration

- Motivation: planning the transition to quantum-safe cryptosystems requires knowing the cost of quantum attacks. Shor 1994 means RSA is not secure against quantum computers (abstract and §1, pp. 1, 3). → post-quantum-cryptography
- The author hopes the estimate acts as a "sign post" for the state of the art and informs how fast quantum-safe cryptosystems should be deployed (§4, p. 21). → post-quantum-cryptography
- Author's view: "attacks always get better", which has held for quantum factoring over the past decade (§4, p. 21). → post-quantum-cryptography
- The author agrees with the initial public draft of NIST IR 8547: vulnerable systems should be deprecated after 2030 and disallowed after 2035. He adds that this is not because he expects sufficiently large quantum computers by 2030, but because security should not depend on progress being slow (§4, p. 21). → post-quantum-cryptography
- Caveats: the estimate depends on the stated hardware assumptions (0.1% error, 1 microsecond cycle, nearest-neighbour grid). It uses unproven heuristics (Assumptions 1 and 2) and a randomized-analysis approximation. The author notes that cold-storage performance under the streaming workload was not simulated in detail (§2.1-2.2, pp. 6, 12; §3.2, p. 20). → post-quantum-cryptography
- The Ekerå-Håstad variant applies to RSA integers specifically. The author hopes a future version, with Ekerå as co-author, will extend the results to other cryptographic cases (§2.3, p. 13; §5, p. 21). → post-quantum-cryptography

## Error-correction concepts (for the later domain)

- Layout: three regions, namely compute, hot storage and cold storage. Hot storage holds qubits as ordinary distance-d surface code patches using 2(d+1)^2 physical qubits per logical qubit. The compute region does lattice surgery and produces magic states for Toffoli gates (§3.2, p. 18). → surface-code
- Surface code distance d = 25 gives a per-patch per-round logical error rate of 10^-15, so 2·26^2 = 1352 physical qubits per hot logical qubit (§3.2, p. 18; Figure 6, p. 19). → resource-estimation
- Target logical error rate 10^-15 per logical qubit per round: a shot has about 6.9e13 logical-qubit-rounds (about 1600 logical qubits, 12 hours, 1 microsecond rounds), giving a 93.3% chance of no logical error (§3.2, p. 18). → resource-estimation
- Cold storage uses yoked surface codes (surface codes concatenated with a 2D parity-check code) and reaches 10^-15 with 430 physical qubits per logical qubit, about 3x denser than hot storage. The 1280 input qubits sit in cold storage (550,400 physical qubits), 131 logical qubits in hot storage (177,112), and the compute region of 7x18 hot patches uses 170,352 (§3.2, p. 18; Figure 6, p. 19). → resource-estimation
- Logical versus physical for RSA-2048: about 1409 logical qubits at peak (1537 including the compute region and idle hot patches) map to 897,864 physical qubits, so overhead is several hundred physical qubits per logical qubit (§3.2, pp. 18-20). → resource-estimation
- Figure 6 projections use fits with suppression-gain parameters deliberately made more pessimistic than the original yoked-surface-code paper (3.5 instead of 4 and 150 instead of 200) (Figure 6 caption, p. 19). → resource-estimation
- The surface code is used for all error correction, with lattice surgery for logical operations, and temporally encoded lattice surgery lets each layer run in about 2/3 d rounds instead of d (§3.2, pp. 18-20). → surface-code
- Magic states: magic state cultivation produces T states (target logical error 10^-7), followed by 8T-to-CCZ distillation (Jones 2013) to produce the CCZ states that power Toffoli gates (§3.2, p. 18). → fault-tolerant-gates
- Cultivation replaces the first distillation stage, so factories are smaller than the 15x8 factories of GE21. Each factory is a 3x4 patch area, and six factories are used (§3.2, pp. 18-20). → fault-tolerant-gates
- Cultivating one 10^-7 T state costs about 30,000 physical qubit-rounds, and one 8T-to-CCZ factory takes about 114.7 rounds per CCZ state, rounded to 150. With six factories the CCZ period is 25 microseconds, equal to the lattice-surgery period at d = 25 (§3.2, p. 20). → fault-tolerant-gates
- 8T-to-CCZ distillation suppresses error as 28p^2, so input error 10^-7 gives CCZ error below 10^-12, which is negligible against 6.5 billion Toffolis (§3.2, p. 20). → fault-tolerant-gates
- Toffoli gates are implemented with CCZ states, and measurement-based uncomputation produces phase corrections (CZ) that can be deferred and merged. An n-qubit addition costs about n-1 Toffolis (or CCZ states), a lookup with an a-qubit address costs 2^a - a - 1, and a phaseup costs about sqrt(2^n) (§2.4, p. 16; §3.1, p. 16). → fault-tolerant-gates
- Operation times: the largest additions take at most 2 ms, a 6-qubit-address lookup takes at least 63 lattice-surgery layers (about 1.6 ms, rounded to 2 ms), and phaseups take at most 1 ms. Time is limited by CCZ-state production and lattice-surgery rounds (§3.2, p. 20). → fault-tolerant-gates

## Not covered

- quantum-complexity: only a brief asymptotic remark (log log N register sizes, Θ(n^3) Toffolis for loop1 in Table 3). The note does not treat complexity classes, and the lesson writer should not cite this source for them.
- Appendix A (mock-ups, Python reference code) was not read.

## Level

Specialist (research preprint, university-graduate level in quantum computing and cryptography); the introduction and conclusion are accessible.
