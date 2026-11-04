---
source: bluvstein-2024
concepts: [neutral-atom-qubits, coherence-and-fidelity, hardware-landscape, logical-qubit-experiments, fault-tolerant-gates, decoding, stabilizer-formalism]
---

Accessed: arXiv:2312.03982v1 (7 Dec 2023), main text pp. 1-8 only (the extracted text has no Methods or Extended Data). Page numbers are arXiv v1 pages. Published as Nature 626, 58-65 (2024). The DOI is NOT in the extracted text. The arXiv abstract page lists the journal DOI 10.1038/s41586-023-06927-3 (with year "2023" for the online publication); the volume and pages come from the brief, not the text. Authors are from Harvard, MIT, NIST/UMD and QuEra Computing (affiliation 2, p. 1). The claims below are the authors' own reports; several are written from the point of view of a company-linked group. Hardware: 87Rb atom arrays, device of this 2023 experiment.

## neutral-atom-qubits
- The authors report a processor with up to 280 atomic qubits (87Rb in optical tweezers); this is the largest size they use, for 40 color codes (p. 1, p. 2, p. 5). → neutral-atom-qubits
- Physical qubits are clock states in the ground-state hyperfine manifold. Tweezer arrays are made with a spatial light modulator (SLM). Coherence T2 is above 1 s, citing earlier work (p. 2). → neutral-atom-qubits
- Zoned architecture with three zones: a storage zone (dense storage, no entangling-gate errors, long coherence), an entangling zone (parallel encoding, stabilizer measurements, logical gates) and a readout zone for mid-circuit measurement (pp. 1-2, Fig. 1a). → neutral-atom-qubits
- Two-qubit gates use fast excitation to Rydberg states and the Rydberg blockade. Gate fidelity 99.5% is cited from the group's earlier work (p. 2; value on p. 4). → neutral-atom-qubits
- Arbitrary connectivity comes from atom transport with 2D acousto-optic deflectors (AODs). AODs use frequency multiplexing, so one voltage waveform per axis makes a large programmable grid of light (p. 2). → neutral-atom-qubits
- Parallel control: a single global Rydberg laser pulse acts on all atoms in the entangling zone. Two logical blocks are interlaced (picked up by the moving AOD grid), so one pulse gives a CNOT on every twin pair (pp. 2-3, Fig. 2a). → neutral-atom-qubits
- Single-qubit rotations are fully programmable through Raman excitation via a second 2D AOD. Parallel grid illumination delivers the same instruction to many atoms (p. 2, Fig. 1b). → neutral-atom-qubits
- Mid-circuit readout: selected atoms are moved about 100 µm to the readout zone and imaged with a focused beam on a CMOS camera. An FPGA decodes in real time and feeds forward (p. 2, Fig. 1c). Imaging takes 500 µs with readout fidelity about 99.8% (Fig. 1c caption). Measuring other qubits disturbs coherence with probability about 1e-3 (Fig. 1c). → neutral-atom-qubits
- Scaling storage: encode ten color codes, move them to storage, then repeat. This gives 40 color codes (280 atoms) with no extra controls. The cost is slow idling error of about 1% logical decoherence per extra encoding step (p. 5, Fig. 4). The authors attribute it mainly to global Raman pi pulses (dynamical decoupling) in the entangling zone and say zone-specific Raman control could reduce it (p. 5). → neutral-atom-qubits
- Outlook (authors' claim, not demonstrated): scaling to over 10000 physical qubits with more laser power and better control. Deep computation needs continuous atom reloading from a reservoir. Modular links via photons or transport, optical lattices and erasure conversion are listed as options (p. 8). → neutral-atom-qubits
- The authors expect clock speed not to limit medium-scale logical systems (p. 8). They give no gate-time numbers in the main text. → neutral-atom-qubits

## coherence-and-fidelity
- Physical numbers cited from earlier work (p. 4): |0> initialization fidelity 99.32(4)% and two-qubit gate fidelity 99.5%. Readout fidelity is about 99.8% (Fig. 1c). → coherence-and-fidelity
- Useful large algorithms need gate error rates generally below about 1e-10. The authors say this is far below what any physical device is likely to reach, which motivates error correction (p. 1). → coherence-and-fidelity
- The authors say two-qubit gate errors should be reduced to 0.1% to improve QEC efficiency (p. 8). This implies the current 0.5% two-qubit error is a limiting factor. They give no explicit single-qubit gate error number in the main text. → coherence-and-fidelity
- Cross-entropy benchmark (XEB): a weighted comparison of the measured and ideal distributions. XEB=1 means the ideal distribution is reproduced exactly; XEB=0 means the uniform distribution that noise-dominated circuits produce. The authors say it is a good fidelity benchmark for IQP circuits (p. 6-7). → coherence-and-fidelity
- Logical XEB for the 12-logical circuit rises from 0.156(2) raw to 0.616(7) with full error detection (p. 7). XEB is about 0.1 for 48 logical qubits (p. 7). → coherence-and-fidelity
- The final-state purity from two-copy measurements, 0.74(3), is consistent with XEB 0.616(7), so XEB is a good proxy for state fidelity (pp. 7-8). → coherence-and-fidelity
- Logical |0_L> initialization is 99.91 (+0.04/-0.09)%, above the physical initialization fidelity and the physical two-qubit gate fidelity (p. 4). → coherence-and-fidelity
- Coherent errors: the authors say the logical circuit is more tolerant to coherent errors and behaves "inherently digital", consistent with theory (p. 7). → coherence-and-fidelity

## hardware-landscape
- The authors claim their XEB (about 0.1 at 48 logicals) is up to about an order of magnitude higher than earlier physical-qubit implementations of similar complexity (p. 7). → hardware-landscape
- Trade-off the authors point out: conventional quantum devices need several classical control lines per physical qubit, which is an obstacle for logical qubits. Atom arrays avoid this with multiplexed optical control (p. 1, p. 2). → hardware-landscape
- Prior milestones cited (p. 2): two logical qubits and one entangling gate [5, 6]. The repeated-QEC memory result comes from ref. [6], which the authors cite as a distance-increase idling-error demonstration (p. 3). They do not name the platform in the main text. → hardware-landscape
- The atom-array advantages the authors list: high two-qubit fidelity, arbitrary connectivity, programmable single-qubit rotations and mid-circuit readout (abstract, p. 1). The limitations they state: repeated error correction is not yet demonstrated, atom reloading is needed, and storage idling errors exist (p. 5, p. 8). → hardware-landscape

## logical-qubit-experiments
- Headline results (abstract, p. 1): surface-code two-qubit gate improves from d=3 to d=7. Color-code qubits are prepared at break-even fidelity. Fault-tolerant logical GHZ states and feedforward entanglement teleportation are made. 40 color codes are operated. Sampling circuits use [[8,3,2]] blocks with up to 48 logical qubits, 228 logical two-qubit gates and 48 logical CCZ gates. → logical-qubit-experiments
- Surface code (p. 3, Fig. 2): transversal CNOT between two surface codes of d=3, 5, 7 (26, 74, 146 physical qubits per Bell pair). Logical Bell-pair error falls with distance under correlated decoding; populations of about 0.95 in XX and ZZ are measured at d=7. Code distance is reduced by removing atoms, so conditions stay the same (d=3 runs four Bell pairs in parallel). → logical-qubit-experiments
- Limitation: the state preparation is non-fault-tolerant beyond d=3, and the result uses only one round of stabilizer measurement and a final projective readout. The authors say the true threshold with repeated noisy syndrome extraction is expected to be somewhat lower, and repeated rounds are a future goal (p. 3-4, p. 8). → logical-qubit-experiments
- Color code (p. 4): 2D d=3 color codes. Ten are encoded non-fault-tolerantly. Five are used as ancillas for flagged fault-tolerant initialization via transversal CNOTs. A 4-logical-qubit GHZ state is built. → logical-qubit-experiments
- Logical GHZ fidelity 72(2)% fault-tolerant with correlated decoding. It rises to 99.85 (+0.1/-1.0)% when postselecting on all computation-logical stabilizers (error detection), at a cost in discarded data. Discarding about 50% of the data gives about 90% (p. 4, Fig. 3). Full tomography uses all 256 logical Pauli strings (p. 5). → logical-qubit-experiments
- Entanglement teleportation (p. 5, Fig. 4d,e): a 3-logical GHZ state, then an X-basis mid-circuit measurement of the middle logical, then a real-time conditioned logical S gate on the other two. Bell fidelity is 77(2)%, or 92(2)% with error detection in the final readout. Without mid-circuit readout it is 75(2)% with postselection. → logical-qubit-experiments
- Scaling: 40 color codes on 280 atoms, 20 of them prepared fault-tolerantly by 20 transversal CNOTs (p. 5, Fig. 4). → logical-qubit-experiments
- [[8,3,2]] sampling (pp. 5-7, Fig. 5): each block encodes 3 logicals. Circuits are layers of {CCZ, CZ, Z} within blocks alternated with CNOTs between blocks; the blocks are prepared in |+_L> and measured in the X basis. They map onto IQP circuits, for which sampling is classically hard in certain instances. → logical-qubit-experiments
- Sampling sizes: 3, 6, 12, 24 and 48 logical qubits, with logical triplets entangled on up to 4D hypercubes. The 48-logical circuit has physical connectivity of a 7D hypercube. XEB is finite at every size and improves with more error detection (p. 7). → logical-qubit-experiments
- The authors say the logical results beat an estimated upper bound for physical-qubit implementations on the same system. Small physical instances land well below that bound (p. 7). The 48-logical-qubit circuit uses 128 physical qubits and 384 T gates in total (p. 7). → logical-qubit-experiments
- The logical circuits are near the limit of exact classical simulation, where one bitstring probability takes about 2 s. The authors say this makes them suitable for exploring error-corrected quantum advantage (pp. 7-8). → logical-qubit-experiments
- Two-copy Bell-basis measurements on 12-logical states show a Page-curve entanglement entropy, an additive Bell magic measure that grows with logical CCZ count, and zero-noise extrapolation of Pauli expectation values to about 10% relative precision (p. 7-8, Fig. 6). → logical-qubit-experiments
- Error detection (postselection) is used heavily for the sampling and GHZ results, so the improvements are not full error correction. The authors present error detection as a way to purify samples at the cost of rate (pp. 4, 6-7). ⚠️ Compare with "error-corrected" in the abstract wording; the caller should present this carefully. → logical-qubit-experiments

## fault-tolerant-gates
- Transversal gate: operations act independently on the physical qubits of a code block. The authors say this makes it inherently fault-tolerant, since errors cannot spread within a block (p. 2). → fault-tolerant-gates
- A logical single-qubit gate is the same Raman pulse on every physical qubit of the block, via an AOD grid. A transversal CNOT interlaces two blocks and applies one global Rydberg pulse (p. 2-3). → fault-tolerant-gates
- Color codes allow transversal H, S and CNOT, hence any Clifford circuit fault-tolerantly. The surface code (2D) cannot easily do non-Clifford gates (pp. 4-5). → fault-tolerant-gates
- No code can implement a universal gate set transversally. 3D codes give transversal non-Clifford gates but lose transversal H (p. 5). → fault-tolerant-gates
- [[8,3,2]] gives transversal CCZ, CZ, Z via physical T and S rotations. Intrablock CNOTs come from physical permutations. Transversal CNOTs are available between blocks (p. 5-6). Transversal H is not available, but X/Z-basis initialization and readout stand in for H at the start and end (p. 6). → fault-tolerant-gates
- The authors say the surface code and other 2D codes need expensive techniques for non-Clifford operations (p. 5). → fault-tolerant-gates
- Fault-tolerant state preparation uses an ancilla-block flag with a transversal CNOT, postselecting on no detected error (p. 4). → fault-tolerant-gates
- The authors note that Clifford circuits are easily classically simulable (p. 5). → fault-tolerant-gates

## decoding
- Decoding means inferring from stabilizer outcomes which error occurred, then correcting it in software by applying a Z_L or X_L correction (p. 3). → decoding
- Conventional decoding is independent minimum-weight perfect matching within each code (p. 3). → decoding
- Correlated decoding: a transversal CNOT spreads physical errors deterministically between the paired blocks, correlating their stabilizers. The authors decode the two logicals jointly with a decoding graph with extra edges and hyperedges joining both blocks' stabilizers (p. 3, Fig. 2b). → decoding
- With conventional decoding the Bell error grows with distance; with correlated decoding it falls (p. 3, Fig. 2d). Correlated decoding also partly mitigates the non-fault-tolerant state preparation (p. 3). → decoding
- The main text gives no decoder details; it cites an in-preparation paper (Cain et al., ref. 80) and the Methods (not read). The GHZ result also uses correlated decoding (p. 4). For [[8,3,2]], Z-basis measurements are corrected with an [[8,3,2]] decoder when full error detection is not applied (Fig. 6a caption, p. 7). → decoding
- Fault-tolerant GHZ is also decoded using the correlated matching weight to rank syndrome events for a sliding postselection threshold (p. 4). → decoding

## stabilizer-formalism
- Surface-code stabilizers are 2D lattice 4-body plaquettes of X and Z operators that commute with the logical operators. Measuring them detects errors without disturbing the logical state (p. 3). → stabilizer-formalism
- The [[8,3,2]] stabilizers (Fig. 5a, p. 6) include four Z-type generators, e.g. Z1Z2Z3Z4, and one all-X stabilizer on eight qubits. The distance is d=2 for Z errors (detection) and d=4 for X errors (correction) (p. 5). → stabilizer-formalism
- Logical Bell-state stabilizers X1L X2L and Z1L Z2L are measured to evaluate entanglement (p. 3). → stabilizer-formalism

## Not covered
- Concepts requested but absent: Rydberg gate time, atom-loss rates, T1 and quantum volume, and the DOI in the text (page 1 has none). The Methods and Extended Data were not in the extracted text. The "99.5%" fidelity is cited from ref. [8], not measured here.
- Level: specialist (research paper, assumes QEC background).
