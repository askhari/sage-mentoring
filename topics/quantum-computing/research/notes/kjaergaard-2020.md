---
source: kjaergaard-2020
concepts: [superconducting-qubits, coherence-and-fidelity, quantum-advantage-experiments, hardware-landscape]
---

Accessed: full text of arXiv:1905.13641v3 (21 Apr 2020), Annual Review of Condensed Matter Physics review by MIT/Lincoln Lab authors (page numbers = arXiv PDF pages). Written in 2019-early 2020; numbers date from then.

## superconducting-qubits
- Circuits are made by lithography, metal deposition, etching and controlled oxidation of thin films (Al or Nb) on silicon or sapphire, compatible with CMOS-type techniques; the chip sits in a Cu/Al package thermally anchored at about 10 mK in a dilution refrigerator (§2, pp. 3-4) → superconducting-qubits
- A Josephson junction (two superconductors separated by a thin insulator, Cooper-pair tunneling) is a lossless nonlinear inductor (p. 4 sidebar) → superconducting-qubits
- An LC oscillator has equally spaced levels so cannot be a qubit; the junction makes the spectrum anharmonic so each transition is individually addressable, and the two lowest levels form the qubit (§2.1, pp. 4-5) → superconducting-qubits
- Charge qubit (Cooper-pair box, regime E_C > E_J): large anharmonicity (>10 GHz) but strongly limited by charge noise and device-to-device variability (§2.1.1, p. 5) → superconducting-qubits
- Transmon: add a large shunt capacitor, E_J/E_C of about 50 or more, which gives exponentially reduced charge-noise sensitivity ("charge-insensitive charge qubit"); coherence 50-100 µs, at the cost of anharmonicity of only about -200 MHz against a ~5 GHz qubit frequency (§2.1.1, pp. 5-6) → superconducting-qubits
- Transmon frequency is fixed by shunt capacitor and junction critical current; replacing the junction with a dc-SQUID makes it flux-tunable but adds sensitivity to flux noise (p. 6) → superconducting-qubits
- Transmons couple capacitively, directly or via a resonator bus, giving an XX+YY-type interaction; a coupler qubit or coupler SQUID makes the coupling tunable (p. 6) → superconducting-qubits
- Flux qubits (persistent-current): large anharmonicity and coherence up to 23 µs but poor reproducibility; capacitively shunted flux qubits reach 50-100 µs with about 500 MHz anharmonicity; flux qubits couple inductively and are the main platform for annealing (e.g. D-Wave) (§2.1.2-2.1.3, pp. 6-7) → superconducting-qubits
- The transmon is the most widely used qubit for gate-based computing; fluxonium has exceeded 100 µs but needs many junctions per qubit and is not yet used in larger circuits (pp. 7, 22) → superconducting-qubits
- Alternatives (§5.2, p. 22): gatemons (semiconductor or graphene junctions, voltage-tuned) with coherence/field-compatibility gains, but nanowire placement hinders scaling; 2DEG/graphene variants are more amenable to top-down fabrication but reintroduce gate charge noise → superconducting-qubits
- Single-qubit gates: resonant microwave pulses (I/Q drive) rotate about x,y axes; z rotations are done "virtually" by shifting the drive phase; DRAG pulses suppress leakage to higher levels caused by low anharmonicity (§2.2, p. 7) → superconducting-qubits
- Two-qubit gates fall in three classes: tunable-qubit gates (flux-tuned, e.g. adiabatic CZ, √iSWAP), fixed-frequency all-microwave gates (cross-resonance, CR), and parametrically driven gates. Tunable qubits are faster but more flux-noise sensitive; fixed-frequency ones usually live longer but need longer gates (§2.2, pp. 7-8) → superconducting-qubits
- Dispersive readout: qubit state shifts a readout resonator frequency by χ (about g²/Δ for a two-level system, modified for transmons); κ is designed close to χ, a few MHz; larger κ speeds readout but increases Purcell decay, mitigated by Purcell filters (§2.3, p. 9) → superconducting-qubits
- Readout needs quantum-limited parametric amplifiers (JPAs, stepped-impedance, JTWPAs); frequency-multiplexed readout puts several resonators on one amplifier chain, limited by amplifier bandwidth/saturation power (§2.3, p. 9) → superconducting-qubits
- Bosonic encoded qubits (cat, binomial codes in a cavity, controlled and read out through a coupled transmon; SNAP gates plus displacements give universal control) exploit long cavity lifetimes (§2.4, pp. 9-10) → superconducting-qubits
- Near-term scaling: control and coherence across large chips, scalable calibration, reproducible fabrication; non-planar connectivity of high-fidelity qubits not yet shown (§5.3, p. 23) → superconducting-qubits
- Authors judge that current techniques can scale to roughly 1000 qubits; beyond that, new techniques such as cryogenic co-located control/readout electronics and on-the-fly QEC decoders are needed (§5.3, p. 23) → superconducting-qubits

## coherence-and-fidelity
- Coherence history (Fig. 2c, p. 4): the first flux qubit exceeded 10 µs, reaching 23 µs; transmons and capacitively shunted flux qubits are at 50-100 µs; fluxonium exceeds 100 µs; the figure plots T1 and T2 rising across 2000-2016 by several orders of magnitude (read only from caption/text, no numeric table) → coherence-and-fidelity
- Cavity-based (bosonic) encodings use long-lived resonators; a cat-code logical qubit (Ofek 2016) passed "break-even", with an error-corrected lifetime longer than that of the best constituent (Fock-state) element; a binomial-code result came close (§4.3, p. 21) → coherence-and-fidelity
- Fidelity benchmarking: single-qubit gates are routinely at fidelity of about 0.99 or higher, typically measured by interleaved Clifford randomized benchmarking (RB), which estimates average gate fidelity by interleaving the gate in random Clifford sequences (§2.2, p. 7) → coherence-and-fidelity
- Two-qubit gate fidelities above 0.99 in multi-qubit transmon systems were first shown in 2014 (CZ, 99.4%, 40 ns, Barends et al.); Table 1 (p. 8) lists best values: adiabatic CZ 99.7% in 60 ns (Kjaergaard et al., 2020), cross-resonance 99.1% in 160 ns (Sheldon 2016), parametric CZ 99.2% in 176 ns (Hong et al. 2019), √iSWAP ~98.2%-98.5% in 183-413 ns (Sheldon 2016); tomography-based entries are lower (e.g. 79-90%). Most are RB-determined → coherence-and-fidelity
- Google Sycamore (Arute et al. 2019; as reported in review): calibrated single- and two-qubit gate fidelities of 99-99.9% with all qubits operating simultaneously (§3.1, p. 11) → coherence-and-fidelity
- ⚠️ No explicit statement that two-qubit gates are more error-prone or slower than single-qubit gates, and no single-qubit gate time. The text only says single-qubit fidelities are ≳0.99 routinely while two-qubit gates "several" reached >0.99 (p. 7), and Table 1 gives two-qubit gate times of 30-800 ns (best-fidelity gates 40-190 ns), with fidelities as low as 79-90% for some. Tying this to "two-qubit is worse" would be an inference, not stated → coherence-and-fidelity
- Gate-time versus coherence trade-off is described qualitatively: fixed-frequency qubits have longer lifetimes but slower gates; tunable qubits are faster but flux-noise-sensitive (p. 8) → coherence-and-fidelity
- Low transmon anharmonicity causes leakage and dephasing under fast drive, countered by DRAG (p. 7); Purcell decay into the readout resonator limits T1, countered by Purcell filters (p. 9); cross-resonance crosstalk was cancelled by optimized pulses in a weight-4 parity experiment (Takita et al., p. 19) → coherence-and-fidelity
- Verification at scale: Clifford RB across a whole chip becomes infeasible as qubit count grows, so cross-entropy benchmarking and direct benchmarking were proposed and used (§5.3, p. 23); SPAM errors are separated from gate errors by RB in the [[4,2,2]] code experiment (p. 20) → coherence-and-fidelity
- Surface-code error threshold: the 2014 CZ (99.4%) was described as the first superconducting two-qubit gate (RB-measured) beating the surface-code error threshold (§4.1, p. 18) → coherence-and-fidelity
- Higher gate fidelity reduces the physical-per-logical qubit overhead and is needed for NISQ algorithms (§5.3, p. 23) → coherence-and-fidelity

## quantum-advantage-experiments
- Review's definition: quantum computational supremacy means solving a problem with a quantum computer significantly faster than the best-known classical algorithm (§3.1, p. 11) → quantum-advantage-experiments
- Google Sycamore: 53 transmon qubits and 86 tunable couplers (nearest-neighbor). The task was sampling the output of a pseudorandom circuit; cycles = random single-qubit gates plus prescribed two-qubit gates; with 53 qubits and 20 cycles sampling took 200 s (§3.1, p. 11) → quantum-advantage-experiments
- The reported classical advantage ratio depends on classical assumptions: from about three (citing the IBM-style counter-estimate, ref. 111) to nine orders of magnitude (Google's estimate), so the review itself presents a range rather than a settled number (p. 11) → quantum-advantage-experiments
- The task was chosen because it suits NISQ devices yet is hard to simulate classically; the review calls it a watershed, and notes it is the one notable NISQ demo outperforming a large classical computer in time/accuracy; other NISQ demos remain proof-of-principle (§3, p. 10) → quantum-advantage-experiments
- Authors expect 50-70 qubits of sufficiently high fidelity to reach beyond-classical regime for many NISQ experiments, citing the cross-entropy benchmarking paper (p. 10) → quantum-advantage-experiments
- Quantum simulation (analog or hybrid) is argued likely to reach problem-specific advantage before universal computing (§3.2, p. 12); digital simulations so far were limited to about 5 Trotter steps by gate errors (p. 13) → quantum-advantage-experiments
- Does not cover boson sampling/Jiuzhang or detailed classical rebuttals beyond the 3-9 orders range → quantum-advantage-experiments

## hardware-landscape
- Two parallel tracks (Fig. 1, p. 2): fault-tolerant QEC computers (arbitrary length, arbitrary precision) versus NISQ computers with tailored algorithms and no generalized QEC; many labs pursue both → hardware-landscape
- State of play: 10-20-qubit transmon systems demonstrated, 50-100-qubit processors in development (IBM, Rigetti 128, Intel 49, Google Bristlecone cited), cloud access via IBM (since 2016, 5 qubits), Rigetti, D-Wave (§1, p. 3; §3.1, p. 11) → hardware-landscape
- Pure-transmon architectures had not yet shown logical lifetime beyond physical qubits; bosonic-code qubits were the first to do so and are called leaders in prototype fault-tolerant demonstrations (pp. 3, 20) → hardware-landscape
- Largest error-correction experiments: 9-qubit repetition code (Kelly 2015), Bell state stabilization (~0.74-0.8 fidelity), weight-4 parity fidelity ~0.77-0.80; the 17-qubit surface-code logical qubit "surface-17" was still under development (§4.1, pp. 18-19) → hardware-landscape
- Beyond the surface code: its qubit overhead is "daunting" and its fault-tolerant gate set limited; other codes need better thresholds/connectivity; bosonic codes lack fault-tolerant multi-qubit protocols (§5.1, pp. 21-22) → hardware-landscape
- List of near-term challenges (§5.3, p. 23): medium-scale coherence/control, scalable calibration, verification, connectivity, gate fidelity, reproducible fabrication; ~1000-qubit limit for current techniques → hardware-landscape
- Source covers only superconducting platforms; no comparison with ions, atoms, spins, photons → hardware-landscape

## Not covered / level
- Requested but not covered: divincenzo-criteria, trapped-ion-qubits, neutral-atom-qubits, spin-qubits, photonic-qubits, topological-qubits; also no T1/T2*/echo definitions, quantum volume, wiring/cryo-wiring detail, or tunable-coupler gate detail beyond classes above.
- Level: university/specialist review (assumes quantum mechanics and circuit QED background); academic authors (MIT), 2019-2020 data, stale for current numbers.
