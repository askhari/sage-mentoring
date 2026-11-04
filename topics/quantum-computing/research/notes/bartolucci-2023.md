---
source: bartolucci-2023
concepts: [photonic-qubits, threshold-theorem, surface-code]
---

Accessed: full text of arXiv:2101.09310v1 (22 Jan 2021 version, pp. 1-17 read of the extracted text; appendices B-E and later pages not read). Cited as "arXiv p. N" / section. The authors are from PsiQuantum (a company building photonic hardware); all claims are "the authors report/propose". The cited year 2023 is the later journal version; numbers below are from v1 and may differ in the published version. All threshold numbers are numerical simulations (Monte Carlo + minimum-weight matching), not experiments.

## Fusion-based quantum computation (FBQC): model
- The authors introduce FBQC, a universal model built on two primitives: generating small, constant-size entangled resource states, and projective entangling measurements ("fusions") between qubits of different resource states (abstract, p. 1; §I) → photonic-qubits
- Resource states have fixed size independent of the computation, typically O(10) qubits; large-scale entanglement arises only from fusions among different resource states (§I.A p. 2; §II p. 3) → photonic-qubits
- A fusion network is the arrangement of resource states plus the fusions; the algorithm is run by changing the basis of some fusions (§I.A, p. 1) → photonic-qubits
- A Bell fusion is a two-qubit projective measurement of the operators X1X2 and Z1Z2 (rank 1, destructive); used as the main example (§II, p. 3) → photonic-qubits
- Claimed hardware advantage: each physical qubit is created and then measured almost immediately, so depth is extremely low, which limits error accumulation, tolerates leakage and cuts classical-processing needs (§I, p. 1; §I.C p. 3) → photonic-qubits
- Classical feed-forward/decoding happens only at the logical timescale, not the fusion clock; physical qubits need not wait in memory for decisions (§I.C p. 3; §VII.B p. 16) → photonic-qubits
- Authors say FBQC can also apply to other platforms where multi-qubit measurements are native (homodyne measurements on GKP qubits, anyonic charge projection, or a multi-qubit gate plus single-qubit measurements in ions/superconducting qubits) (§I p. 1; §I.C pp. 2-3) → photonic-qubits
- Architecture elements: resource state generators (RSGs) that emit states every clock cycle, a fusion-network router with spatial routing and delay lines, reconfigurable fusion devices, and a classical decoder (Fig. 1, p. 2; §VII.C pp. 16-17) → photonic-qubits
- Fixed routing (no switching in the bulk) is attractive because the authors consider reconfigurable components error-prone; fixed integrated photonic circuits have much higher fidelity than reconfigurable ones (§I.C p. 3 and footnote 1) → photonic-qubits

## Linear optics, dual-rail qubits, fusion failure, loss
- Dual-rail qubit: one photon in two modes (e.g. two waveguides = path encoding); photon number is fixed, so loss leaves the computational subspace and is heralded by detectors (§II.A, p. 3 and footnote 3) → photonic-qubits
- Dual-rail makes relative phase shifts between different qubits irrelevant, which allows storing qubits in long delay lines; only the phase between the two rails of one qubit must be kept (§II.A pp. 3-4) → photonic-qubits
- In dual-rail, single-qubit gates are deterministic and accurate with linear optics: Hadamard = 50/50 beamsplitter, phase gate = phase shift on one rail (§II.A, p. 4) → photonic-qubits
- Linear-optical Bell fusion (type-II fusion) is simple but non-deterministic: it fails with probability p_fail, then yields only single-qubit measurements (Z1, Z2), from which Z1Z2 can still be inferred; failure is thus a Bell measurement with one outcome erased and creates no entanglement (§II.A, p. 4; Fig. 2) → photonic-qubits
- Three fusion outcomes: success (both outcomes), failure (one outcome), erasure (none; caused by errors such as photon loss). Failure occurs even with ideal hardware; erasure only from errors (Fig. 2, p. 4) → photonic-qubits
- Basic path-encoded type-II fusion uses two beam splitters and four detectors with p_fail = 50%; boosting with a Bell pair gives 25%; more ancilla photons lower it further, p_fail = 1/2^n with 2^n - 2 extra photons (§II.A p. 4; §VI.C.2 p. 14, citing ref. [29]) → photonic-qubits
- Fusion failure is more benign than erasure: it is heralded and leaves pure states usable without extra noise (§II.A, p. 4) → photonic-qubits
- Key design point: in FBQC the non-determinism of fusion is handled directly by the error-correcting code, together with other errors, rather than by repeat-until-success (abstract; §II.A p. 3) → photonic-qubits
- Resource states in linear optics are made by fusions on smaller seed states (Bell pairs, 3-GHZ states) with probabilistic steps; switching networks (multiplexing) approximate post-selection on success, with constant overhead because the resource state size is fixed (§III.A, p. 5) → photonic-qubits
- Fusion measurement basis can be changed by single-qubit rotations before the fusion (e.g. a Hadamard on one qubit gives <XZ,ZX>); a switch before the fusion allows reconfiguration (§II.A p. 4) → photonic-qubits
- Authors state optical loss is the dominant physical error source in photonic architectures, and the very short qubit lifetime in FBQC is a strength for this (§VII.C, p. 16) → photonic-qubits
- Loss model: with N photons in a fusion, probability none is lost is eta^N, eta = 1 - p_loss; any lost photon erases both outcomes. Tradeoff: boosting lowers p_fail but adds photons that can be lost, so each network has an optimal intermediate p_fail (§VI.C.2 p. 14; Fig. 10 p. 13) → photonic-qubits
- Local encoding: using a (2,2)-Shor code ([[4,1,2]]) in the resource states lowers the erasure probability of encoded fusions (for unencoded erasure p0 < 0.5, the encoded one is smaller) (§II.A p. 4; §VI.C.2 p. 14) → photonic-qubits
- Photonic connectivity need not be local; long-range connectivity is possible, enabling other topologies; time-ordering can even use a single RSG interleaved over a block (§VII.C, p. 17) → photonic-qubits

## Thresholds (simulation results, v1, Jan 2021)
- Hardware-agnostic error model: each fusion measurement is erased with probability p_erasure and flipped with p_error. Authors find a threshold of 11.98% against erasure and 1.07% against Pauli (flip) error for the 6-ring network (§I p. 1; §VI.C.1 p. 13) → threshold-theorem
- The 4-star network (4-GHZ resource states) has marginal thresholds 6.90% (erasure) and 0.75% (error); the 6-ring network (6-qubit ring graph states) is better and its correctable region contains that of the 4-star (§VI.C.1, p. 13; Fig. 9) → threshold-theorem
- Below the threshold surface, the logical error probability is suppressed exponentially in network size (§VI.C.1, p. 13) → threshold-theorem
- Linear optical model: the authors report that a scheme can tolerate a 10.4% probability of photon loss per fusion (i.e. at least one photon lost) using Bell-pair-boosted fusion (p_fail = 25%) with encoded 6-ring, corresponding to about 2.7% loss per photon (abstract p. 1; §VI.C.2 p. 14) → photonic-qubits
- Fusion-failure threshold (no loss) of the (2,2)-Shor encoded 6-ring is 43.2% with a ballistic scheme, against 14.9% previously reported (ref. [4]); unencoded 4-star and 6-ring have failure thresholds below 25%, so plain Bell-boosted fusion is not enough for them (§I p. 1; §VI.C.2 p. 14) → photonic-qubits
- Threshold methodology: Monte Carlo sampling on L x L x L networks with periodic boundaries, minimum-weight perfect matching decoder, primal and dual graphs decoded separately, thresholds from varying L (§VI.C.1, p. 13) → threshold-theorem
- The authors argue that LDPC-type fault-tolerant fusion networks allow the usual combinatorial arguments for the existence of error thresholds (§V.C, p. 9) → threshold-theorem
- Authors stress the example schemes are pedagogical, not optimized, yet already beat earlier schemes; the higher threshold is attributed to tailoring the fault-tolerance framework to the physical error structure (abstract; §VI p. 9) → threshold-theorem
- A slow decoder does not affect the threshold, since fusions proceed without decoding outcomes (§VII.B, p. 16) → threshold-theorem

## Surface code connection
- The fault-tolerant fusion networks implement surface-code error correction in a 3D topological form (2D code evolving in time = 3D network); repeated identical fusions play the role of repeated stabilizer measurements (§I.B p. 2; §V.C p. 9; §VI p. 9) → surface-code
- Check operators (products of fusion outcomes) are parity checks; the set of outcomes forms a classical LDPC code; syndrome = pattern of check values; a decoder predicts the logical Pauli frame; error correction acts only on classical outcomes since qubits are destroyed (§V.A, p. 7) → surface-code
- Syndrome graph: vertices are checks, edges are fusion outcomes; error chains leave syndromes only at endpoints, which allows minimum-weight matching and union-find decoders; primal and dual graphs as in the surface code (§V.D, p. 9) → surface-code
- Comparison with circuit surface code: there, space-like edges are qubit errors and time-like edges are measurement errors; in FBQC both are fusion outcomes, with no distinction. The two outcomes of a Bell fusion behave like the X and Z parts of an error on a circuit qubit (§VI.A, p. 10) → surface-code
- The 6-ring network has a syndrome graph with extra diagonal edges, akin to "hook" errors of circuit surface codes; each check uses 12 fusion outcomes vs 24 for the 4-star (§VI.B, pp. 10-12) → surface-code
- Logic: boundaries (primal/dual, i.e. rough/smooth) made by replacing some fusions with Z measurements; compatible with punctures/braiding, lattice surgery and defects/twists; universality via magic state injection and distillation (T gates); Pauli frame tracked classically (§VII.A, pp. 15-16) → surface-code

## Not covered / level
- Requested but not covered: nothing missing for photonic-qubits; threshold-theorem is covered only as numerical thresholds for this scheme (the paper does not state or prove the threshold theorem itself, and gives no circuit-level surface-code threshold of ~1% for comparison in the pages read); sources/detectors hardware specifics (no detector efficiency or source figures) and the KLM scheme by name are not detailed in the pages read.
- Level: specialist (research paper, assumes stabilizer formalism); company-authored, simulation-only.
