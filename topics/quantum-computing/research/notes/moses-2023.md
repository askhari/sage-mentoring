---
source: moses-2023
concepts: [trapped-ion-qubits, coherence-and-fidelity, quantum-advantage-experiments]
---

Accessed: full text of arXiv:2305.03828v2 (16 May 2023), pages 1-15 plus start of appendix. Company-authored paper (Quantinuum); all numbers are the authors' own report for the H2 device as of early 2023, and they have likely been superseded.

## Trapped-ion architecture (QCCD, H2)
- The authors, from Quantinuum, describe a QCCD trapped-ion machine (System Model H2) on a "race track" linear trap with periodic boundary conditions, initially with 32 qubits (abstract; p. 1) → trapped-ion-qubits
- Motivation for QCCD: a single trapping zone limits qubit count because individual addressing in a large ion crystal is hard and motional modes become crowded; with several zones, operations always involve few ions, giving low crosstalk and high fidelity (§I, p. 2) → trapped-ion-qubits
- Arbitrary pairs are coupled by moving ions into the same zone during the circuit, so connectivity is arbitrary without SWAP-gate overhead (§I, p. 2) → trapped-ion-qubits
- QCCD needs many programmable electrodes, via microfabricated surface traps (§I, p. 2) → trapped-ion-qubits
- Scaling problem in linear traps: the time to rearrange ions for arbitrary connectivity grows poorly with qubit number. The authors expect future QCCD to use 2D traps, whose own challenges are junction transport and signal routing (§I, p. 2) → trapped-ion-qubits
- Other open QCCD scaling items listed: coupling several trap dies, electrode count, laser delivery and detection (§I, p. 2) → trapped-ion-qubits
- Previous H0/H1 generation (same source): qubits went from 4 to 20 and 2Q gate error fell about 5x; more transport speed and gate zones kept the layer time roughly constant (§I, p. 2) → trapped-ion-qubits
- Trap: 2 concentric RF electrodes (about 200 V, 42 MHz) make an RF null 70 µm above the surface. Gate zones are spaced 750 µm. There are 8 gate zones (4 "DG", 4 "UG"), but only the 4 DG zones do quantum operations (gates, state preparation, measurement) (§II A, p. 2) → trapped-ion-qubits
- Scalability features: "RF tunnels", voltage broadcasting (an a,b,c repeating electrode pattern needs only 3 signals for the conveyor-belt storage regions) and MOT loading. Totals: 376 electrodes, 268 independent voltage sources, 1 RF drive (§II A, p. 2-3) → trapped-ion-qubits
- Qubit species: two species per "pair", 171Yb+ (qubit) and 138Ba+ (coolant). The 138Ba+ ions are Doppler-cooled during transport and sideband-cooled before 2Q gates (§II B, E, p. 3-4; Fig. 2) → trapped-ion-qubits
- Qubit encoding: hyperfine "clock" states of 171Yb+ (F=0 and F=1, m=0 in the 2S1/2 level). Preparation is by optical pumping, and in the DG zones only, so 8 qubits at a time and 4 rounds for 32 qubits (§II B, p. 3-4) → trapped-ion-qubits
- Loading: a 2D MOT replaces the oven. Best case about 1.2 ms per 171Yb+ and 40 ms per 138Ba+. The full 32 pairs take about 3-4 min, and a lost pair is replaced in 10-15 s (§II B, p. 3) → trapped-ion-qubits
- Gates are laser-driven via stimulated Raman processes. 1Q gates use co-propagating beams. 2Q gates use a phase-sensitive Mølmer-Sørensen interaction coupling to the axial motional mode, with 1Q "wrapper" pulses forming the parameterized gate U_ZZ(θ)=exp(-iθZZ/2) (§II C, p. 4) → trapped-ion-qubits
- Error of the parameterized 2Q gate falls roughly linearly as θ→0, down to a finite offset of about 5e-4. The offset arises from laser phase noise and spontaneous emission while the laser is partly on. The linear fit is ε(θ)=(2.9(2)θ/π+0.46(6))e-3 (§II C p. 4; Fig. 3 p. 6) → coherence-and-fidelity
- The 2Q laser beams have the strictest requirements and use a large share of the laser power budget; 4 beam pairs operate 4 gate zones (§II C, p. 4) → trapped-ion-qubits
- Measurement is by state-dependent resonance fluorescence, with a PMT array for the gate zones. Mid-circuit measurement and reset (MCMR) causes small crosstalk on neighbors from stray light, mitigated by "micromotion hiding" for gate-zone ions (§II D, p. 4) → trapped-ion-qubits
- Transport primitives: split/combine, linear shifts, physical swaps, and the "batch shift" of 8-ion batches. The batch shift is comparatively slow and dominates circuit time (§II E, p. 4) → trapped-ion-qubits
- Transport takes on average about 60% of total circuit time. Table I gives per-circuit budgets (e.g. QV circuit: 1% quantum ops / 52% transport / 47% cooling, 1.23 s per shot; mirror benchmarking 1/67/32, 1.05 s; random-circuit-sampling circuit 1/67/32, 0.72 s) (§II E p. 4; Table I p. 5) → trapped-ion-qubits
- A compiler groups 2Q gates into layers and sorts qubits with a modified Sugiyama algorithm and parallel bubble sort to minimize transport time. 2Q gates are done on a four-ion YBBY crystal (two Yb-Ba pairs) (§II E, p. 4-5) → trapped-ion-qubits
- Sources of memory error: imperfect spatial phase tracking (magnetic field inhomogeneity and AC Zeeman shifts), transport failures, background-gas collisions that reorder ions, and a finite T1 of several minutes (§II E, p. 5) → coherence-and-fidelity
- Authors' summary: 2Q gates remain the dominant error source. Transport time between arbitrary layers increased relative to H1, which increases memory error. Planned fixes are better lasers, faster transport and magnetic field stability (§VI, p. 15) → trapped-ion-qubits

## Component numbers (H2, 2023; averages over the 4 DG zones, Table II p. 6; ×1e-4 infidelity)
- 1Q RB infidelity: 0.25(3)e-4, i.e. 2.5e-5 per gate (abstract; Table II) → coherence-and-fidelity
- 2Q RB infidelity per 2Q gate: 18.3(5)e-4, about 1.8e-3 (abstract gives 1.84(5)e-3; Table II). So 2Q gate error is about 70x the 1Q error on this machine (ratio computed from the two numbers above; not stated in the paper) → coherence-and-fidelity
- A 2Q Clifford takes on average 1.5 U_ZZ(π/2) gates; the 2Q RB infidelity is scaled to a per-gate figure by that factor (§III, p. 6) → coherence-and-fidelity
- SPAM error: 1.6(1)e-3 per qubit (abstract; Table II). The measurement is prepared in |0> and |1> in turn and the two flip probabilities are averaged, so preparation and measurement errors cannot be separated. Modeling predicts measurement dominates for 171Yb+ (§III, p. 6) → coherence-and-fidelity
- Leakage: 0.04(2)e-4 per 1Q gate and 3.9(2)e-4 per 2Q gate. It is most likely from unavoidable spontaneous emission in Raman-driven gates, and is detected with an ancilla-based "leakage detection gadget" (Table II; §III p. 7; Figs. 4-5) → coherence-and-fidelity
- Haar-random SU(4) 2Q RB gives 41(1)e-4 per SU(4) operation (built from 3 parameterized U_ZZ gates), larger than the π/2-gate 2Q RB (Table II; §III p. 6) → coherence-and-fidelity
- Transport memory error: interleaved 1Q RB on all 32 qubits with dummy 2Q gates (forcing transport and cooling) gives 2.2(3)e-4, dominated by memory error rather than 1Q gate error (Table II; §III p. 6) → coherence-and-fidelity
- Measurement crosstalk 0.045(6)e-4 and reset crosstalk 0.038(6)e-4 on neighboring qubits (Table II; §III p. 6) → coherence-and-fidelity
- The authors give no gate durations in the main text read. Time costs are given only as circuit-level budgets (Table I) → trapped-ion-qubits

## Benchmarks
- Authors' rationale: component benchmarks can mischaracterize device performance if crosstalk or non-Markovian errors are present, so system-level benchmarks are also run (§IV, p. 7) → coherence-and-fidelity
- Effective error per 2Q gate ε_2Qeff lumps the 2Q gate error, 1Q errors and memory errors between 2Q gates into one depolarizing error per 2Q gate. It is predicted as 2Q gate error at the mean angle plus twice the transport-RB error: ε=1e-3(2.9θ̄/π+0.9) (§IV, p. 7, Eq. 1) → coherence-and-fidelity
- Predicted vs inferred ε_2Qeff (×1e-3): mirror benchmarking 2.4(1) vs 2.6(2); QV 1.9(1) vs 1.7(1); RCS 2.1(1) vs 1.9(2). The agreement is reasonable but not perfect, since memory error depends on the circuit (Table III, p. 8) → coherence-and-fidelity
- Mirror benchmarking: random layers of Clifford 1Q gates and U_ZZ(π/2) on random pairings, followed by the inverse circuit and a random final Pauli. The success probability decays exponentially with depth, and the decay rate gives an effective 2Q infidelity (§IV A, p. 8) → coherence-and-fidelity
- Mirror benchmarking was run at N=20, 26, 32. For N=32 the effective 2Q error is 2.6(2)e-3, and the authors find it does not grow with qubit number (§IV A, p. 8; Fig. 6) → coherence-and-fidelity
- Quantum volume: random circuits on N qubits, with random SU(4) on random pairs for N rounds. A heavy-output test is passed if the heavy-output probability exceeds 2/3 with 2-sigma confidence, and the result is QV=2^N. A fully decohered circuit gives 1/2 (§IV B, p. 8) → coherence-and-fidelity
- The previous largest QV was 2^15 on H1, per the authors (§IV B, p. 8) → coherence-and-fidelity
- Result (H2, 2023): QV = 2^16 with 200 circuits, 100 shots each, average 296 2Q gates, and heavy-output probability 68.2% (§IV B, p. 8; Fig. 7) → coherence-and-fidelity
- Authors' claim: QV=2^N implies good performance on many circuits with more than N qubits and/or depth beyond N (§IV B, p. 8) → coherence-and-fidelity
- GHZ states: fidelity 0.86(1) for N=20, 0.83(1) for N=26, 0.82(1) for N=32 (log-depth unitary), and 0.74(1) for N=32 with a constant-depth adaptive circuit using mid-circuit measurement. These are not SPAM-corrected. A fidelity above 0.5 witnesses genuine multipartite entanglement (§IV D, p. 10; Table IV) → coherence-and-fidelity
- GHZ states are described as a demanding coherence test because they are maximally sensitive to global dephasing (§IV D, p. 10) → coherence-and-fidelity
- Repetition-code (QEC) benchmark with 32 qubits: distance 31 using 31 data qubits and 1 reused ancilla. Larger distance gives higher logical fidelity, and the bit-flip code beats the phase-flip code, which the authors read as biased noise (§V C, p. 13-14; Fig. 14) → trapped-ion-qubits

## Random circuit sampling / XEB and advantage
- Authors: RCS is not a scalable benchmark, since it needs classical computation exponential in N. A cited result [60] shows that at fixed gate error it is not a scalable route to quantum supremacy at large N (§IV C, p. 9) → quantum-advantage-experiments
- It is still useful because it tests faithful execution of circuits that are hard to simulate classically, and because it has been run on several platforms in advantage demonstrations, which allows cross-platform comparison (§IV C, p. 9) → quantum-advantage-experiments
- Circuits mimic the Sycamore setup. They use a 2D grid pattern (not a hardware constraint of H2), random 1Q gates from {√X, √Y, √W}, and fSim(π/2, π/6) 2Q gates, implemented with a single U_ZZ(5π/12) gate plus software SWAP (§IV C, p. 9; Eqs. 2-3) → quantum-advantage-experiments
- The linear cross-entropy benchmarking fidelity F_XEB quantifies how well the machine samples the true output distribution of each random circuit. H2 data: depth 14, 10 circuits per N, N from 12 to 32, using the "classically verifiable" EFGH tiling (§IV C, p. 9; Fig. 8) → coherence-and-fidelity
- The authors do not claim quantum advantage. 32 qubits is well within the classically feasible regime. They only expect that with more qubits and comparable ε_2Qeff, XEB results would pose serious challenges to classical simulation (§IV C, p. 9) → quantum-advantage-experiments
- Table III gives the inferred effective error for RCS at average angle 0.42π as 1.9(2)e-3 (p. 8) → quantum-advantage-experiments

## Not covered / level
- Not covered: T2/T2*/echo (only "T1 of several minutes" is mentioned), gate durations in µs, advantage claims or rebuttals (none made).
- Level: specialist (experimental device paper by the manufacturer). Self-reported numbers, so treat as vendor claims.
