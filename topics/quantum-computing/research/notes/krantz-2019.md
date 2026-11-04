---
source: krantz-2019
concepts: [superconducting-qubits, coherence-and-fidelity]
---

Accessed: full extracted text of arXiv:1904.06560v5 (9 Jul 2021 version, 67 pp.; page numbers below are arXiv pages). Review by Krantz, Kjaergaard, Yan, Orlando, Gustavsson, Oliver (MIT). Gate and coherence numbers come from experiments up to about 2018; hardware numbers age fast.

## Superconducting qubits: design and transmon

- Superconducting qubits are nanofabricated, lithographically defined, macroscopic anharmonic oscillators. Their level spectrum follows from circuit parameters, so they are called "artificial atoms". Natural-system platforms (spins, ions, atoms, photons) differ in this (p. 2) → superconducting-qubits
- A linear LC circuit is a harmonic oscillator with equally spaced levels, so a two-level subspace cannot be addressed selectively. Anharmonicity is needed so that the 0→1 and 1→2 transitions can be told apart (pp. 4-5) → superconducting-qubits
- The Josephson junction (a nonlinear, dissipationless inductor) supplies the anharmonicity. It replaces the quadratic potential with a cosine potential, H = 4E_C n² − E_J cos φ (p. 5, Eqs. 15-16) → superconducting-qubits
- The community converged on E_J ≫ E_C. When E_J ≤ E_C (the Cooper-pair-box charge qubit), the qubit is very sensitive to charge noise, which is hard to mitigate (p. 5) → superconducting-qubits
- Transmon: the junction is shunted by a large capacitor (C_s ≫ C_J), which makes E_C small. Charge sensitivity is suppressed exponentially in E_J/E_C, while anharmonicity falls only as a weak power law (pp. 5-6) → superconducting-qubits
- Typical transmon design: anharmonicity α ≈ −E_C of about 100-300 MHz, qubit frequency 3-6 GHz, E_J/E_C ≥ 50. The anharmonicity is negative and limited in size. The transmon is a weakly anharmonic Duffing oscillator, and higher levels still exist physically (p. 6; p. 30 gives 200-300 MHz) → superconducting-qubits
- A large shunt capacitor also spreads the electric field and reduces participation of lossy interfaces. The 3D transmon (2D transmon in a 3D cavity) gained coherence this way (p. 6) → superconducting-qubits
- Split transmon: a dc-SQUID loop of two junctions makes E_J tunable with external flux (E_J' = 2E_J|cos φ_e|). The cost is sensitivity to flux noise, which is zero only at the sweet spots Φ = kΦ0 (p. 6) → superconducting-qubits
- Asymmetric junctions reduce flux-noise sensitivity over the whole tuning range but shrink the tunability. This is a good trade, since only about 1 GHz of tuning is usually needed (pp. 7, 22) → superconducting-qubits
- Flux qubit (3-4 junctions) and fluxonium (about 100 array junctions, a "superinductance") reach larger anharmonicity. They have smaller transition matrix elements, and fluxonium has reached millisecond T1. The capacitively shunted flux qubit has positive anharmonicity. Flux qubits are best at the flux degeneracy (half-flux) point (pp. 7-9) → superconducting-qubits
- Coupling: qubits couple capacitively (H_int ∝ n1 n2) or inductively (mutual inductance). It can be direct, through a resonator bus (which can span about 1 cm), or through a tunable coupler. A tunable coupler gives a wide coupling range and a high on/off ratio, at the price of an extra control line (pp. 9-11) → superconducting-qubits
- Transverse coupling (σyσy / σxσx) is the form used in most gates. Longitudinal coupling (σzσz) is used for annealing (pp. 10-11) → superconducting-qubits
- Typical qubits sit at about 5 GHz and are operated at about 20 mK in a dilution refrigerator, so thermal excitation is exponentially suppressed (p. 14). Dilution refrigerators are "off-the-shelf" products, but signal routing and wiring at scale are still in development. 3D integration and superconducting interconnects address some of the scaling concerns (p. 54) → superconducting-qubits
- Planar superconducting qubits are described as a promising platform for medium-scale processors. D-Wave flux-qubit annealers are cited as beyond 2000 qubits (the authors' 2019-21 survey, p. 54) → superconducting-qubits
- Cat-state cavity qubits (3D cavities) are a parallel approach with high Q (p. 54) → superconducting-qubits

## Control: single-qubit gates

- Single-qubit X and Y rotations come from capacitively coupled microwave pulses at the qubit frequency, shaped by an AWG and IQ mixer. The I quadrature gives x-rotations, the Q quadrature gives y-rotations, and the pulse area sets the angle (pp. 28-29) → superconducting-qubits
- Virtual Z gate: a Z rotation is done in software by shifting the phase of all following microwave pulses. It takes no time and is nominally perfect. With one physical X_{π/2} plus virtual Z, any single-qubit gate is available (p. 30) → superconducting-qubits
- DRAG: the weak anharmonicity means short pulses leak into |2⟩ (leakage) and cause phase errors. An extra derivative-shaped pulse on the quadrature channel reduces both. The optimal scaling is λ=0.5 for phase error and λ=1 for leakage (p. 30) → superconducting-qubits
- Anharmonicity limits how short a pulse can be (p. 5) → superconducting-qubits
- Universality: arbitrary single-qubit rotations plus any entangling two-qubit gate suffice. Common sets are {X_θ, Y_θ, Z_θ, Ph, CNOT} and Clifford+T. Native gates depend on the hardware (pp. 26-27) → superconducting-qubits

## Control: two-qubit gate families

- Two families: flux-tunable gates (iSWAP, CPHASE) and all-microwave gates on fixed-frequency qubits (cross-resonance and others). Hybrid and tunable-coupler schemes are increasingly important (p. 31) → superconducting-qubits
- iSWAP: bring two tunable transmons into resonance for time π/2g (coupling g/2π typically 5-40 MHz). It cannot give a CNOT alone, and two iSWAPs are needed per CNOT (pp. 31-33) → superconducting-qubits
- CPHASE (CZ): move |11⟩ adiabatically near the |11⟩↔|20⟩ avoided crossing to pick up a π phase. It uses the transmon's higher level. Heuristic minimum gate time is about 2π/g ≈ 50 ns for g/2π ≈ 20 MHz (pp. 33-35) → superconducting-qubits
- Frequency crowding is a risk when qubits are tuned in frequency. One remedy is on/off tunable coupling, e.g. the "gmon" (on/off ratio about 1000, CPHASE F = 0.9907) (p. 36) → superconducting-qubits
- Cross-resonance (CR): drive qubit 1 at qubit 2's frequency to get a ZX interaction. It needs only microwaves and fixed-frequency qubits, which have longer lifetimes and no flux-noise sensitivity (p. 37) → superconducting-qubits
- CR drawbacks: the gate time depends on detuning, anharmonicity and coupling, so fabrication frequency errors lengthen the gate. The coupling is always on, which creates a tension between isolation (good single-qubit gates) and coupling (good two-qubit gates) (p. 38) → superconducting-qubits
- CR is the native two-qubit gate on the IBM Quantum Experience (p. 38) → superconducting-qubits
- Other microwave gates: bSWAP (drives |00⟩↔|11⟩, the analogue of Mølmer-Sørensen), MAP (microwave-activated CPHASE), RIP (resonator-induced phase, tolerates large frequency differences). Each has strict spectral requirements (pp. 39-40) → superconducting-qubits
- Tunable-coupler or parametric gates are generally faster than fixed-frequency-only schemes (p. 40) → superconducting-qubits

## Readout

- Dispersive readout: the qubit is detuned from a readout resonator (Δ ≫ g, κ). The qubit state shifts the resonator frequency by χ = g²/Δ, and the state is inferred from the phase/amplitude of a microwave tone reflected or transmitted. It is approximately quantum non-demolition, valid below the critical photon number n_c = Δ²/4g² (pp. 41-42) → superconducting-qubits
- Best state discrimination is obtained by probing between the two resonator frequencies, with χ ≈ κ/2 as the criterion for maximal visibility (p. 43) → superconducting-qubits
- Signal chain: IQ mixing, heterodyne demodulation and digitisation give a point in the IQ plane. Noise makes the two states Gaussian blobs. SNR > 1 means a strong (single-shot) measurement (pp. 43-47) → superconducting-qubits
- Residual photons in the resonator cause ac-Stark dephasing, so thermalisation, filtering and attenuation matter (p. 43) → superconducting-qubits
- Purcell effect: the readout resonator enhances qubit decay by γ ≈ (g/Δ)²κ. A Purcell filter allows fast readout (wide κ) while protecting the qubit. It can also serve as a frequency-multiplexed bus (pp. 48-49) → superconducting-qubits
- A HEMT amplifier alone gives a system noise temperature of about 7-10 K (about 10-20 added photons), which is too noisy for single-shot readout. Quantum-limited parametric amplifiers (JPA, TWPA) add about half a photon of noise. Resonator-based JPAs have limited bandwidth (about 10-50 MHz) and low saturation power; the TWPA addresses both (pp. 50-53) → superconducting-qubits

## Coherence and noise

- Bloch-Redfield model: T1 is the energy-relaxation (longitudinal) time, Γ1 = 1/T1. T2 is the transverse decoherence time, Γ2 = Γ1/2 + Γφ, with Γφ the pure-dephasing rate (pp. 13-14) → coherence-and-fidelity
- T1 is caused by transverse noise at the qubit frequency. Because k_BT ≪ ħω_q, the up-rate is exponentially suppressed and the qubit decays to |0⟩ (p. 14) → coherence-and-fidelity
- Pure dephasing comes from longitudinal noise (frequency fluctuations), is broadband and elastic, and is in principle reversible. Energy relaxation is irreversible (p. 16) → coherence-and-fidelity
- Hard bound: T2 ≤ 2T1, with equality when there is no pure dephasing (p. 17) → coherence-and-fidelity
- Measurement of T1: prepare |1⟩ with a π pulse, wait τ, then measure. The example device has T1 = 85 µs (p. 15) → coherence-and-fidelity
- Measurement of T2*: Ramsey interferometry, two π/2 pulses with a free evolution between them. It is sensitive to low-frequency quasi-static noise ("inhomogeneous broadening"). The example device has T2* of about 95 µs. ⚠️ The Fig. 5 caption says 95 µs and the text on p. 16 says 98 µs, and the text on p. 17 quotes both (T2 = 95 µs, Tφ,G = 98 µs) → coherence-and-fidelity
- T2 echo (Hahn echo): a π pulse in the middle of the free evolution refocuses quasi-static noise. The example gives T2E = 120 µs, still below the 2T1 = 170 µs limit (pp. 15-16). The T1/T2*/T2E triple is from one transmon, citing Ref. 117 (device not named) → coherence-and-fidelity
- 1/f noise: charge, flux and critical-current noise have a 1/f-like spectrum. It is singular at zero frequency and long-correlated, so decay is non-exponential (Gaussian, exp[−(t/Tφ,G)²]) and Γ2 = Γ1/2 + Γφ is not strictly valid (pp. 16-17) → coherence-and-fidelity
- Quasi-universal flux-noise amplitude is about (1 µΦ0)²/Hz at 1 Hz with exponent about 0.8-1.0. Charge-noise amplitude is about (10⁻³ e)²/Hz at 1 Hz with exponent about 1 (p. 18) → coherence-and-fidelity
- Dynamical decoupling (CPMG sequences with N π pulses) shifts the noise filter to higher frequencies and pushes T2 toward 2T1. Noise spectroscopy is built on this (pp. 20-22) → coherence-and-fidelity
- Charge noise (dielectric defects) couples transversely and causes T1 loss. It causes dephasing only if E_J/E_C is too small (below about 60) (p. 18) → coherence-and-fidelity
- Photon shot noise in the readout resonator gives white dephasing at rate Γφ ∝ n̄ (p. 19) → coherence-and-fidelity
- Quasiparticles (observed density about 10⁻⁷-10⁻⁶ per Cooper pair, higher than BCS theory predicts) cause T1 loss and dephasing (p. 19) → coherence-and-fidelity
- Mitigation covers materials and fabrication, design (a low-sensitivity qubit), dynamical decoupling and cryogenic engineering, all of which trade off against each other (pp. 21-22) → coherence-and-fidelity
- Intrinsic coherence times of superconducting qubits have been above 100 µs in recent years (the authors, p. 49) → coherence-and-fidelity

## Gate fidelity, gate time and benchmarking

- Gate fidelity is bounded above by coherence, so short gates are desirable. This sets up a tension with adiabaticity for CPHASE (p. 35) → coherence-and-fidelity
- Interleaved randomized benchmarking is the technique used for the reported gate fidelities (p. 35). It is also used to tune the DRAG parameters (p. 30) → coherence-and-fidelity
- Single-qubit gates: modern DRAG gates routinely reach F ≳ 0.99, from a 2017-2018 era literature survey, as the text says (p. 31) → coherence-and-fidelity
- Two-qubit CPHASE: F = 0.9944 by interleaved RB, gate time 43 ns, xmon device (Barends et al., p. 35). Kelly et al. improved F from 0.984 to 0.993 by optimising with RB (p. 35). CPHASE is cited as "F ≳ 0.99" in general (p. 34) → coherence-and-fidelity
- Two-qubit CR: initial experiments F_QPT ≈ 0.81-0.88 and echo-CR 0.9347 (IRB). Active-cancellation echo-CR (Sheldon et al.) reached F = 0.991 with τ = 160 ns, against 0.948 without cancellation. Early CR gate times were 300-400 ns versus 30-60 ns for CPHASE, which the authors say largely accounts for the lower CR fidelities (p. 38) → coherence-and-fidelity
- Other two-qubit gates were lower: bSWAP F = 0.9 (QPT, long high-power pulse, extra dephasing), MAP F = 0.87 in 514 ns, RIP F = 0.96-0.98 in 285-760 ns, parametric iSWAP F = 0.9823 in 183 ns, hybrid iSWAP 0.94 in 150 ns and CPHASE 0.88-0.93 in 210-290 ns (pp. 39-40) → coherence-and-fidelity
- Two-qubit gates are slower than single-qubit gates, but the text gives no explicit single-qubit gate time: ⚠️ not stated, so no ratio can be taken from this source. What it does show: single-qubit F ≳ 0.99 (p. 31) vs two-qubit best 0.99-0.994 (p. 35) with much longer, noisier fixed-frequency implementations (0.87-0.98 for other gates). The text also notes always-on coupling (CR) trades off single-qubit isolation against two-qubit speed (p. 38) → coherence-and-fidelity
- Surface-code threshold of about 1% means two-qubit F > 0.99 is a milestone. It lets error rates fall as qubits are added and lets arbitrarily long computations be run in principle (p. 35) → coherence-and-fidelity
- Leakage (excitation to |2⟩) and phase errors from weak anharmonicity are the main single-qubit error mechanisms addressed by DRAG (p. 30) → coherence-and-fidelity
- Crosstalk: spurious cross-talk to spectator qubits studied in CR experiments, which led to a four-pulse echo-CR scheme (p. 38). A cross-talk term η = 0.03 is included in the CR simulation (p. 37) → coherence-and-fidelity
- Readout fidelity is limited by (1) separation error ε = ½ erfc(SNR/2) and (2) T1 decay during readout, F(τ_ro) ≈ 1 − e^{−τ_ro/T1}. Readout must be much shorter than T1 and have high SNR (pp. 47-48) → coherence-and-fidelity
- Examples of lower-fidelity multi-qubit state quality: 5-qubit GHZ state fidelity 0.817 (Barends et al., p. 35); 4-qubit GHZ state fidelity 0.79 by state tomography (p. 41) → coherence-and-fidelity
- Despite improvements in lifetimes and fidelity, error correction is still needed for large-scale devices. A logical qubit outliving its physical qubits was an open challenge at the time of writing (p. 55) → coherence-and-fidelity

## Not found

- DiVincenzo criteria are not discussed. The paper mentions universality and readout as cornerstones, and the intro opens with quantum parallelism and interference, but there is no list of criteria.
- Cross-entropy benchmarking and quantum volume are not discussed. Randomized benchmarking is used but not explained in detail. Dilution-refrigerator wiring and fabrication are only touched on.

Concepts requested but not covered: divincenzo-criteria.
Level: university / specialist review (assumes QM and EE background; rigorous derivations).
