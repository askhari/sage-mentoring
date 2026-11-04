---
source: bravyi-2024
concepts: [surface-code, resource-estimation, stabilizer-formalism, decoding, threshold-theorem, superconducting-qubits, hardware-landscape]
---

Accessed: full text of the arXiv v2 preprint (2308.07915v2, 21 Feb 2024; extracted PDF text; page numbers = PDF pages). Authors are all IBM Quantum employees (company authors: Bravyi, Cross, Gambetta, Maslov, Rall, Yoder). Not the final Nature 627 (2024) typeset version; numbers may differ slightly there. The paper is about a quantum MEMORY (storage); it does not provide a universal set of logical gates.

## Surface code as the baseline

- The paper states the surface code gives a threshold close to 1%, fast decoders and compatibility with 2D square-lattice connectivity, and that small single-logical-qubit surface-code demonstrations exist; but scaling to 100+ logical qubits is judged prohibitively expensive because of its poor encoding efficiency (pp. 1-2) → surface-code
- Surface code is asymptotically zero-rate with only square-root distance (n = d² data qubits for k = 1), versus good qLDPC codes with constant rate and linear distance (p. 2) → surface-code
- A distance-d surface code uses d² data qubits plus d²−1 check qubits for one logical qubit, so net rate r ≈ 1/(2d²); this becomes impractical when d must be large because errors are near threshold (p. 2) → surface-code
- Surface-code pseudo-threshold is about 1% for large enough distance, and the surface-code error threshold is cited as nearly 0.7% in this paper's comparison (pp. 2, 6) → surface-code
- ⚠️ Threshold figures are not fully consistent within the paper: abstract says "0.8%" threshold; Table 1 / p. 6 report pseudo-thresholds of 0.0065 ([[144,12,12]]) and 0.0069 ([[288,12,18]]), "close to 0.007", described as nearly the same as the surface-code threshold. Pseudo-threshold (pL(p) = kp break-even) is a different quantity from an asymptotic threshold → surface-code
- Baseline for comparison: 12 logical qubits stored in 12 separate d×d rotated surface-code patches (n = 12d² data qubits) with the standard syndrome circuit, d in {9, 11, 13, 15}; compared at d = 13 the surface code has net rate 1/338 vs 1/24 for the BB code (pp. 5-6, §8 p. 21) → surface-code
- The text notes that the surface-code Tanner graph is planar and local; BB codes are laid out on a torus like the toric code but with weight-6, non-geometrically-local checks (vs 4-body plaquette/vertex checks) (p. 4) → surface-code

## Resource estimation: [[144,12,12]] "gross" code vs surface code

- Headline: 12 logical qubits preserved for roughly 10^6 syndrome cycles with 288 physical qubits in total (144 data + 144 check), assuming physical error rate p = 0.1% (abstract; p. 6) → resource-estimation
- Same suppression with the surface code (12 patches) needs nearly 3000 physical qubits to bring the logical error rate from 10^-3 to about 10^-6; the authors call this more than 10x saving for the d = 12 BB code (p. 6) → resource-estimation
- The conclusion quotes "nearly 15x" reduction in qubit overhead for p ≥ 0.1%; the introduction says "more than 10X" (pp. 2, 30) → resource-estimation
- Assumptions of the estimate: circuit-based depolarizing noise, every operation (CNOT, init, measurement, idle) fails independently with probability p; faulty CNOT = ideal CNOT plus one of 15 non-identity two-qubit Paulis uniformly; faulty measurement = classical bit flip of the outcome; idle = random X/Y/Z (§6, p. 16) → resource-estimation
- Logical error rate defined per syndrome cycle, pL ≈ PL(Nc)/Nc, simulated with Nc = d cycles. pL was simulated numerically for p ≥ 10^-3 and extrapolated to lower p with a fitting formula pL = p^(d_circ/2) · exp(c0 + c1·p + c2·p²) (pp. 5-6, §8 pp. 20-21) → resource-estimation
- ⚠️ The low-p numbers (e.g. pL(10^-4) = 8×10^-13 for [[144,12,12]], 2×10^-7 at p = 10^-3) are in part extrapolations, as the paper states; surface-code estimate of ~3000 is read from simulations in its Figure 2B (Table 1 caption p. 5; p. 6) → resource-estimation
- Table 1 values (circuit-level, pL at p = 10^-3 / 10^-4): [[72,12,6]]: 7×10^-5 / 7×10^-8; [[90,8,10]]: 5×10^-6 / 4×10^-10; [[108,8,10]]: 3×10^-6 / 1×10^-10; [[144,12,12]]: 2×10^-7 / 8×10^-13; [[288,12,18]]: 2×10^-12 / 1×10^-22. A [[n,k,d]] BB code needs 2n physical qubits, net rate k/(2n) (p. 5) → resource-estimation
- The [[288,12,18]] code needs 576 physical qubits and gives pL about 2×10^-12 at p = 10^-3 (roughly 10^11 syndrome cycles) (p. 6) → resource-estimation
- Circuit-level distance of the syndrome circuit for [[144,12,12]] is at most 10 (conjectured 10), below the code distance 12; the effective suppression exponent uses d_circ rather than d (pp. 5-6, 16) → resource-estimation
- Overhead of fault-tolerant load-store ancillas undercuts the compactness: for [[144,12,12]] the X and Z measurement ancilla systems add 2×30×(2d−1) = 1380 qubits on top of the 288 (p. 22, §9.4 p. 29). The authors say this is likely reducible, left to future work → resource-estimation
- Earlier belief cited: beating the surface code under realistic circuit noise might require qLDPC codes with more than 10,000 physical qubits (p. 2) → resource-estimation

## Code definition, CSS, LDPC, [[n,k,d]]

- A code is LDPC if each check acts on only a few qubits and each qubit takes part in only a few checks (p. 2) → stabilizer-formalism
- [[n,k,d]] notation: n data qubits, k logical qubits, d distance (p. 4) → stabilizer-formalism
- Bivariate bicycle (BB) codes are CSS stabilizer codes with check operators made of Pauli X or Z only; each check has weight 6, each qubit is in 6 checks (3 X-type, 3 Z-type), so the Tanner graph has degree 6 (pp. 4, 7) → stabilizer-formalism
- Construction: with cyclic-shift matrices x, y (x^ℓ = y^m = identity), pick A = sum of 3 monomials, B = sum of 3 monomials; HX = [A|B], HZ = [Bᵀ|Aᵀ], n = 2ℓm; X- and Z-checks commute because HX·HZᵀ = AB + BA = 0 mod 2 (p. 7) → stabilizer-formalism
- Parameters: k = 2·dim(ker A ∩ ker B); d = min Hamming weight of a vector in ker(HX) not in rowspace(HZ) (a logical operator is a nontrivial element outside the stabilizer); X and Z distances are equal (Lemma 1, p. 7; proof §7 pp. 19-20) → stabilizer-formalism
- For CSS codes k = n − rank(HX) − rank(HZ), and d = min(dX, dZ) (§7, pp. 19-20) → stabilizer-formalism
- Tanner graph: vertices are data qubits and checks; an edge links a check to each qubit on which it acts non-trivially (p. 3) → stabilizer-formalism
- Syndrome-measurement circuit: n ancilla check qubits, 7 layers of CNOTs (8 rounds counting init/measure), independent of code length. Z-type error info flows to X-check ancillas, X-type to Z-check ancillas, so both are read out (pp. 4-5, 12-13) → stabilizer-formalism
- Correctness of the circuit is proved by tracking a stabilizer tableau of the Clifford circuit, and stabilizer-formalism simulation is used to propagate single faults (pp. 13-15, 16) → stabilizer-formalism
- Examples in Table 3 (selected): [[72,12,6]], [[90,8,10]], [[108,8,10]], [[144,12,12]] (ℓ=12, m=6, A = x³+y+y², B = y³+x+x²), [[288,12,18]], [[360,12,≤24]], [[756,16,≤34]] (p. 8) → stabilizer-formalism
- The [[144,12,12]] code is the one the authors consider most promising for near-term demonstration. The paper does not use the name "gross code" in the text read (p. 5) → stabilizer-formalism

## Decoding

- A decoder is a classical algorithm that takes the measured syndromes and outputs a guess of the final error; it succeeds if the guess equals the actual error up to a product of check operators (same action on all logical states), and fails if they differ by a nontrivial logical operator (p. 5, §6 p. 16) → decoding
- The decoder used is Belief Propagation with Ordered Statistics postprocessing (BP-OSD, Panteleev and Kalachev; software of Roffe et al.), extended here from memory-error noise to circuit-level noise (pp. 5, 16) → decoding
- Offline stage: build a "linearized" noise model by enumerating all single-fault circuit realizations (M = 98·n·Nc of them), recording their syndrome and logical effect; this ignores cancellations of two or more faults (probability O(p²)); analogous to a decoding graph for the surface code (§6, pp. 16-17) → decoding
- Detection-event style compression: the sequence of syndromes per check is replaced by its change between consecutive cycles to make the decoding matrix sparse (p. 17) → decoding
- Online stage: solve the minimum-weight decoding problem for a classical linear code (check matrix D, per-fault probabilities); exact solution is NP-hard, hence BP (message-passing estimate of marginals) followed by OSD, which picks the most reliable information set via a greedy algorithm (pp. 17-18) → decoding
- Because BB codes are CSS, X- and Z-errors are decoded separately with matrices DX and DZ, which are (6,35)-sparse; for [[144,12,12]] with 12 cycles they have about 8800 columns (p. 18) → decoding
- Weight-4 stabilizers harm belief propagation, and the chosen codes have none empirically (p. 11) → decoding
- Simulation details: min-sum BP with up to 10,000 iterations and OSD combination-sweep, at least 100 logical errors per data point for most points (§8, p. 20) → decoding
- BP-OSD is also used to bound code distance by solving a related minimum-weight problem with random logical operators (pp. 18-19) → decoding
- The authors say the general-purpose BP-OSD may not be fast enough for real-time error correction and ask for a faster decoder exploiting the structure of BB codes (open question 6, p. 31) → decoding
- Related work noted: spacetime codes (Delfosse and Paetznick), detector-based noise model (McEwen, Bacon, Gidney), BP as a pre-processor for matching decoders (Higgott et al.) (p. 16) → decoding

## Threshold

- Definition used: error correction helps only if the physical error rate is below a threshold depending on the code, syndrome circuit and decoder (abstract, p. 1) → threshold-theorem
- Early fault-tolerance proposals based on concatenated codes aimed at showing the theoretical possibility of error suppression (p. 1) → threshold-theorem
- Result: threshold of 0.8% (abstract) under the circuit-based noise model, said to be on par with the surface code; observed pseudo-thresholds ~0.0065-0.0069 for the 144 and 288-qubit codes (Table 1, p. 5; p. 6) → threshold-theorem
- High-distance codes show a very sharp drop in logical error once p is below threshold, which suits near-threshold early demonstrations (p. 2) → threshold-theorem
- Below threshold the expected scaling is pL ≈ exp[−d·f(p)] with f(p) ≈ −(1/2)·log p for small p, i.e. error suppression of order p^(d/2) for distance d (§8, pp. 20-21) → threshold-theorem
- Noise assumption: independent faults on every circuit operation with equal probability p (p. 3) → threshold-theorem
- Open question: how the threshold changes under noise biased toward measurement errors, which the authors say dominate in superconducting qubits (p. 31) → threshold-theorem
- Alternative they contrast with: Pattison, Krishna and Preskill concatenate a high-rate LDPC code with the surface code (each data qubit encoded in a surface code), which uses surface-code threshold and locality but pays a large qubit overhead (p. 29) → threshold-theorem

## Hardware requirements (superconducting qubits)

- Required connectivity is a degree-6 graph; each qubit couples to 6 others (4 short-range plus 2 long-range edges in the torus embedding). The graph is not locally embeddable in a 2D grid but has thickness 2, i.e. it splits into two edge-disjoint planar subgraphs (pp. 2, 4, 7) → superconducting-qubits
- Thickness: partition of edges into θ planar subgraphs. θ=1 is planar (no crossing couplers); θ=2 may be realizable by putting two layers of couplers on top and bottom sides of the chip and mating them; θ≥3 is much harder. A general degree-6 graph can have θ=3, so θ=2 here is notable (p. 3-4) → superconducting-qubits
- The authors argue this connectivity is a valid architecture solution for superconducting platforms, and expect near-term processors to offer a few hundred qubits, gate errors near 10^-3 and long-range connectivity (pp. 2, 6, 30) → superconducting-qubits
- Hardware challenges listed: (1) a low-loss second layer, e.g. extra buses on the opposite side of the chip using high-Q through-substrate vias, based on packaging developed for IBM Eagle; (2) qubits coupled to 7 connections (6 buses and 1 control line), compared to 4 in heavy-hex; (3) long-range couplers, with filtering resonators/frequency engineering for the longest buses (p. 30) → superconducting-qubits
- Challenge (2) implies cross-resonance gates would not scale because of frequency collisions with fixed-frequency qubits; tunable couplers (IBM Egret/Heron, similar to Google's) are suggested instead (p. 30) → superconducting-qubits
- Authors estimate transmon capacitance ~60 fF with ~5 fF per coupler, so extra couplers are said to be feasible without changing transmon properties (p. 30) → superconducting-qubits
- ⚠️ These hardware feasibility statements are the IBM authors' own projections (company authors); no hardware demonstration is reported in this paper → superconducting-qubits
- Architecture comparison within the hardware-landscape: the paper positions BB codes as suited to superconducting qubits with long-range couplers, versus the planar nearest-neighbor layouts of surface-code devices (pp. 2, 30) → hardware-landscape

## Memory only, limited logical operations

- The scope is a fault-tolerant quantum memory: initialization, readout, and load-store of logical qubits via teleportation to/from another code (e.g., surface code); no universal logical gate set is given (pp. 3, 21-22, 31) → surface-code
- Logical gates available: depth-4 fault-tolerant automorphism circuits implementing an abelian family of logical CNOT circuits (translations of a logical-qubit grid), and a costly ZX-duality swap with Hadamard that swaps two logical blocks; for [[144,12,12]] the latter has CNOT depth 132 and cannot interleave error correction (§9.2-9.3, pp. 24-27) → surface-code
- Authors admit these gates offer very limited computational power, mainly useful for memory; how to apply general logical gates is left open (open question 7, p. 31) → surface-code
- Logical X and Z of individual qubits are measured by attaching ancilla systems (adapting a construction of Cohen et al., ref. [46]) that can connect to a surface code, giving joint Pauli-product measurement used for teleportation (pp. 21-22, 28-29) → surface-code

## Not covered / level
- Requested but not covered: fault-tolerant gates in depth (Eastin-Knill, lattice surgery, magic states), logical-qubit experiments, quantum-noise-channels beyond the depolarizing circuit model, repetition/Shor codes, Steane code; "gross code" name is not used in this version of the text; Gottesman-Knill is not named (only tableau simulation is used).
- Level: specialist (research paper in quantum error correction; assumes coding theory and CSS/Tanner-graph background). The intro (pp. 1-3) and conclusion (pp. 29-31) are readable at university level.
