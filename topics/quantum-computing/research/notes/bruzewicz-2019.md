---
source: bruzewicz-2019
concepts: [trapped-ion-qubits, coherence-and-fidelity, divincenzo-criteria, hardware-landscape]
---

Accessed: full text of arXiv:1904.04178v1 (8 Apr 2019; later published in Appl. Phys. Rev. 6, 021314), pp. 1-34 read in detail (Sections I-IV.B); Sections IV.B.3 end, V (integrated technology) and VI (outlook) only seen in the table of contents. Page numbers below are arXiv pages. Authors are from MIT Lincoln Laboratory (review, not a company paper). All hardware numbers are as of early 2019 and may be outdated.

## DiVincenzo criteria (§I.C, p. 2-3)
- DiVincenzo (2000) gave five criteria: (1) well-defined two-level qubits isolated from the environment; (2) initialization to a definite state; (3) decoherence times much longer than gate times; (4) a universal gate set; (5) high-accuracy qubit readout (p. 2) → divincenzo-criteria
- Two extra criteria for quantum communication: interconverting stationary and "flying" qubits (photons), and transmitting flying qubits faithfully. They are not needed for a stationary computer but are for quantum networks and for photonic links between ion modules (p. 3) → divincenzo-criteria
- The authors say trapped ions are one of only a few technologies that have satisfied all five original criteria at high fidelity. They say all criteria have essentially been met since 2004, yet the largest fully controlled ion register was only 20 ions (pp. 2-3) → divincenzo-criteria
- Mapping to ions: initialization by optical pumping plus motional cooling; readout by state-dependent fluorescence; universal gates from single-qubit rotations plus one entangling gate; coherence far longer than gate times fulfils the remaining criteria (pp. 2-3) → divincenzo-criteria
- Ion-photon entanglement at high fidelity has been shown (ref. 32). Ions can be shuttled on a chip but are unlikely to be the long-distance flying qubits (p. 3) → divincenzo-criteria
- The five criteria are not enough in practice. Scalability needs more: modularity, monolithic integration, error correction, an architecture with connectivity, ion-loss handling and scalable addressing/readout (§I.E, pp. 5-6) → divincenzo-criteria
- A scalable computer is defined as one whose number of elements can grow on demand without loss of performance or disproportionate cost. The authors state no QC technology achieves this yet (p. 5) → hardware-landscape

## Qubit types and encodings (§I.C, §II.B, pp. 2, 10-13)
- Four qubit types, by level splitting: Zeeman (MHz, magnetic sublevels), hyperfine (GHz, odd isotopes with nuclear spin), fine-structure (THz, D3/2 and D5/2 levels), optical (hundreds of THz, ground state plus metastable D level) (pp. 2, 10-11, 13) → trapped-ion-qubits
- Typical species are Group-II-like ions. Hyperfine ground levels have lifetimes approaching the age of the universe; D levels are metastable with ~seconds lifetimes (p. 10) → trapped-ion-qubits
- Zeeman qubits: simple level structure and essentially infinite lifetime, but high sensitivity to magnetic-field noise. Coherence of 300 ms (2.1 s with dynamical decoupling) was reached using mu-metal shielding (p. 11) → trapped-ion-qubits
- Hyperfine qubits: "clock" states (mF = 0) are first-order insensitive to B at zero field. 171Yb+ clock qubits show seconds of coherence, up to 600 s with dynamical decoupling (p. 12) → trapped-ion-qubits
- First-order-field-insensitive (FOFI) hyperfine qubits at non-zero field reach minutes of coherence in plain Ramsey experiments. The limits are technical: field drift, RF amplitude, local-oscillator stability (p. 12) → trapped-ion-qubits
- Optical qubits: coherence reached ~0.2 s. The laser is the local oscillator, so its phase noise often limits coherence. The ultimate limit is upper-state decay, 1 to tens of seconds (p. 12) → trapped-ion-qubits
- Optical qubits allow near-unit-efficiency readout by electron shelving and use red/near-IR lasers. The authors argue this favors them for scaling with integrated photonics, since waveguides are harder at blue/UV (pp. 12-13) → trapped-ion-qubits
- Fine-structure qubits have ~second lifetimes, limited by leakage rather than relaxation. They use IR Raman lasers, which are friendlier for integrated photonics (p. 13) → trapped-ion-qubits
- Ions of one species and isotope are identical, so they need the same drive frequency and have the same coherence. This reduces calibration compared with superconducting qubits, whose frequencies vary with fabrication and thermal cycling (p. 4) → trapped-ion-qubits
- Extra internal levels mean leakage errors and repump lasers are needed. Ions can be lost from the trap (lifetimes of hours to months), so reloading is needed (p. 4) → trapped-ion-qubits

## Traps and motion (§II.A, §II.C, pp. 6-15)
- Paul traps (RF oscillating field) are the main platform for QC. Penning traps (static E plus B field) hold large 2D crystals of hundreds of ions, which rotate and are hard to address individually (p. 7) → trapped-ion-qubits
- Linear Paul traps have an RF null along a line, so ion chains avoid excess micromotion. Ions can also be moved along the axis, which underpins shuttling architectures (p. 7) → trapped-ion-qubits
- Surface-electrode traps put all electrodes in one plane and are suited to microfabrication and CMOS integration. They have lower trap depth and frequency for the same voltage (p. 9) → trapped-ion-qubits
- Photoionization loading is isotope-selective, unlike electron bombardment (p. 9) → trapped-ion-qubits
- For N ions there are 3N motional (phonon) modes that act as a quantum bus coupling the ions' internal states. Sideband Rabi frequencies scale with the Lamb-Dicke parameter η (p. 13) → trapped-ion-qubits
- Anomalous motional heating is electric-field noise much larger than known sources. It scales roughly as d^-4 with ion-electrode distance, so miniaturization is hard (p. 14) → trapped-ion-qubits
- Cooling electrodes from room temperature to ~4 K cuts the heating rate by about two orders of magnitude. Surface treatments (laser, plasma, ion milling) also help. For d = 40-80 µm, heating can be made low enough for fault-tolerant codes (pp. 14-15) → trapped-ion-qubits
- Trap-frequency fluctuations of 10^-6 to 10^-5 (fractional) on 10-100 s timescales have been measured, and keeping this stability across large arrays is an engineering challenge (p. 14) → trapped-ion-qubits

## State preparation and readout (§III.A, §III.C, pp. 15-25)
- Preparation uses optical pumping, with errors ~1e-4 achieved. Doppler cooling gives millikelvin temperatures, and resolved-sideband or EIT cooling reaches the motional ground state (EIT cooling: up to 18 ions, phonon occupation ~0.01-0.02) (pp. 15-16) → trapped-ion-qubits
- Readout uses state-dependent fluorescence: a "bright" state scatters many photons and a "dark" state almost none. A photon-count threshold separates them with Poissonian statistics (worked example λb=20, λd=1, threshold 7 gives ~99.99% and ~99.97%) (p. 22) → trapped-ion-qubits
- Best readout figures reported: >99.99% in <200 µs (ref. 9); 99.93% in 11 µs with superconducting-nanowire detectors, which need cryogenics (p. 4, p. 25). Combined state-preparation-and-measurement (SPAM) fidelity is 99.93% (p. 4) → coherence-and-fidelity
- Multi-ion readout: ~99% per ion in a 53-ion chain on an EMCCD (300 µs); 99.99% in ~400 µs for 4 ions at larger spacing (p. 23) → trapped-ion-qubits
- Collection efficiency is limited: solid angle 1-10% and detector efficiency 0.2-0.4, so total detection efficiency is ~2-4% (pp. 24-25) → trapped-ion-qubits
- Stray detection photons can decohere neighboring data ions. This matters for error correction, where ancillas are measured mid-circuit. Mitigations: a second ion species (quantum logic spectroscopy) or shelving (pp. 24, 32-33) → trapped-ion-qubits

## Gates (§III.B, pp. 16-20, Table I p. 18)
- Single-qubit gates use microwaves or Raman laser pairs (hyperfine) or a single resonant laser (optical). Microwaves have cm wavelengths, so individual addressing is hard; options are near-field on-chip microwaves, magnetic-field gradients, or moving ions between zones (pp. 16-17) → trapped-ion-qubits
- Entangling gates use the shared motional modes as a bus. Cirac-Zoller (1995) needs ground-state cooling and individual addressing (early demos 71-77% fidelity) (pp. 17-18) → trapped-ion-qubits
- The Mølmer-Sørensen (MS) gate uses bichromatic light near the sideband transitions to apply a state-dependent force. The motional state traces a closed loop in phase space, giving a geometric phase. It works without ground-state cooling and can use global beams (p. 18) → trapped-ion-qubits
- Leibfried's geometric-phase gate is similar but does not drive transitions between qubit states. It cannot be used with FOFI qubits (p. 19) → trapped-ion-qubits
- Highest-fidelity two-qubit gates all use MS or geometric-phase gates: 99.91% in 30 µs (9Be+, MS, ref. 37); 99.9% in 100 µs (43Ca+ geometric-phase, ref. 27); optical MS 99.6% (ref. 38), 99.3% in 50 µs (pp. 18-19) → trapped-ion-qubits
- Fast two-qubit gates: 99.8% in 1.6 µs (43Ca+, ref. 40, needing hundreds of mW of Raman light); <500 ns gates only ~60% fidelity; ultrafast-pulse gates ≤76%. Faster than the MHz trap frequency, multiple modes get excited and the optical phase matters (p. 20) → trapped-ion-qubits
- Microwave-gradient two-qubit gates reach 99.7% (AC gradient) and 98.5% (static) but take milliseconds (2.7-3.25 ms) (p. 19, Table I) → trapped-ion-qubits
- Dual-species gates: 99.8% in 27.4 µs (40Ca+/43Ca+, with a spin-echo pulse in the gate) and 97.9% in 35 µs (9Be+/25Mg+) (Table I, p. 18) → trapped-ion-qubits
- Typical gate times: single-qubit ~µs; two-qubit 10-100 µs (some faster) (p. 3) → trapped-ion-qubits

## Fidelity, coherence and benchmarking (pp. 3-4, 17-21)
- Single-qubit fidelities: 99.9999% with an on-chip microwave in 12 µs (43Ca+); 99.995% optical (40Ca+, 5 µs); 99.993% Raman in 7.5 µs. There is a speed-fidelity tradeoff: <2 µs gates have ~2e-4 error. The authors say these exceed any other modality (pp. 4, 17-18, Table I) → coherence-and-fidelity
- Two-qubit fidelities up to 99.9% (hyperfine), 99.6% (optical). The authors say only superconducting qubits are comparable (p. 4) → coherence-and-fidelity
- Statement that two-qubit gates are worse than single-qubit gates: "errors in two-qubit gates are at least an order of magnitude higher than in single-qubit gates" (p. 20). Example numbers from Table I (p. 18): single-qubit best 1e-6 to 1e-4 error versus two-qubit best ~1e-3 error. Gate times: single-qubit ~µs versus two-qubit typically 10-100 µs (p. 3) → coherence-and-fidelity
- Two-qubit gate error sources: laser frequency and amplitude drift, magnetic-field drift, off-resonant scattering, motional decoherence and heating during the gate (p. 20) → coherence-and-fidelity
- Coherence times (effectively T2) range from 0.2 s (optical) to 50 s (hyperfine, no echo) and up to 600 s with dynamical decoupling. These are limited by technical dephasing, not by fundamental state lifetime (pp. 3-4) → coherence-and-fidelity
- Coherence-to-gate-time ratio is ~10^6 for ions. The authors compare ~1000 for superconducting qubits (ref. 35) and ~200 for Rydberg atoms (ref. 36) (p. 4) → coherence-and-fidelity
- Optical-qubit single-gate fidelity is ultimately limited by the excited-state T1, ~1 s (p. 17) → coherence-and-fidelity
- Motional heating is a T1-type process on the motional mode; motional dephasing is T2-type (p. 13) → coherence-and-fidelity
- Fidelity F = |<ψg|ψe>|² (pure states) is one number. It hides the error type and can be over-optimistic about coherent errors, which add up faster than stochastic ones when a gate is repeated (p. 20) → coherence-and-fidelity
- Process tomography needs 4^N input states and extracts 12 parameters (1 qubit), 240 (2 qubits), 4032 (3 qubits). It also assumes perfect SPAM (p. 20) → coherence-and-fidelity
- Randomized benchmarking (RB) uses long random gate sequences that return to identity. It is insensitive to SPAM errors and is a standard tool. It extracts stochastic errors but reveals little about correlated errors. First ion use: <0.5% error on π/2 pulses (pp. 20-21) → coherence-and-fidelity
- Gate set tomography (GST) amplifies errors with specially chosen sequences and can bound the diamond norm. It is costly and assumes Markovian errors. Robust phase estimation calibrates systematic errors efficiently (10^-4 accuracy with 176 measurements) but gives no stochastic-error information (p. 21) → coherence-and-fidelity
- Slow ion gates make full characterization (GST, tomography) very time-consuming (p. 21) → coherence-and-fidelity
- Crosstalk: addressing one ion in a growing chain without affecting neighbors needs tightly focused beams (full control shown for 20 ions), composite pulses, shelving, or gradient-based frequency separation. Moving ions apart also reduces crosstalk but heats them (pp. 21-22) → coherence-and-fidelity
- Leakage: ions can end up in levels outside the qubit subspace. Optical-qubit decay is treated as a leakage channel, and repump lasers are needed (pp. 4, 16) → coherence-and-fidelity
- Gate time versus decoherence: speeding up gates to outrun decoherence is a stated route to higher fidelity (p. 20) → coherence-and-fidelity
- Dynamical decoupling and spin echo extend memory. A decoherence-free subspace (two ions encoding one qubit) extended coherence up to 20 s (Zeeman, 40Ca+) at a cost of qubit overhead. Composite pulses (BB1, CORPSE) cut single-qubit error by 3-4x (pp. 31) → coherence-and-fidelity
- Fault-tolerance threshold: the surface code is ~1% (depolarizing model, likely an overestimate). Overhead grows sharply near threshold, so errors must be well below it. Ions' high fidelities are named as a chief advantage (pp. 5, 32) → coherence-and-fidelity

## Scaling architectures (§IV.A, pp. 26-30)
- Gates in a long linear chain get slower as the chain grows: smaller Lamb-Dicke parameters, weaker ion-ion coupling and more spectral crowding of modes. Pulse-shaped gates for a 50-ion chain were only proposed (p. 27). Entangling gates with amplitude/frequency/phase modulation have not been shown for chains of more than 5 ions (p. 6) → trapped-ion-qubits
- Ion-chain all-to-all connectivity: 3- and 5-qubit fully connected ion computers ran algorithms with 85-95% success. On Bernstein-Vazirani and Hidden Shift the ion machine beat IBM's 5-qubit superconducting device on success rate but was slower (sub-µs gates for superconducting). The authors say state of the art is about the same for both: ~10 qubits and two-qubit gates ~99% (pp. 25-26) → hardware-landscape
- The QCCD (quantum charge-coupled device) architecture is a 2D array of segmented traps with junctions. Ions are shuttled between memory, interaction, measurement and loading zones. Split/join counts are independent of distance (pp. 27-28) → trapped-ion-qubits
- Shuttling speed: adiabatic transport is limited by roughly the inverse trap frequency. A diabatic scheme moved ions at ~50 m/s with 0.1 quanta of excitation (~5 mm in 100 µs). Transport heats ions and needs recooling, which adds latency (p. 28) → trapped-ion-qubits
- Junctions are demonstrated (Y and X junctions in surface traps), and 2D lattices exist, but a 2D lattice with junctions and streets enabling general transport is still an open goal (p. 28) → trapped-ion-qubits
- Photonic interconnects (remote entanglement): communication ions emit photons entangled with their internal state. Photons interfere on a 50/50 beam splitter, and coincidence detection heralds ion-ion entanglement. The rate is Γ = γrep (ηc ηd)²/2 (pp. 28-30) → trapped-ion-qubits
- Highest reported remote-entanglement rate was ~5 Hz (2019), because the single-mode collection efficiency is only ~0.005. Remedies are multiplexing and high-finesse cavities (cavities are hard at UV and degrade in vacuum) (p. 30) → trapped-ion-qubits
- Photonic links are in practice independent of distance and can link separate vacuum chambers. Many modules would need an optical switch (p. 30) → trapped-ion-qubits
- Dual-species chains (e.g. data ions plus ancilla/cooling ions of a different element) avoid stray-photon decoherence for mid-circuit measurement, remote entanglement and sympathetic cooling. Similar masses are preferred (pp. 33-34) → trapped-ion-qubits
- Ion loss: even with >24 h lifetime, an array of tens of thousands of ions would lose one every few seconds, so fast reloading is needed (p. 6) → trapped-ion-qubits

## Slow gates and scale: pros and cons (§I.D, pp. 3-5)
- Weakness: absolute gate speed is slow. Two-qubit ion gates are µs to 100 µs versus tens of ns for superconducting. The authors cite an estimate of ~10 days (1024-bit) or ~100 days (2048-bit) to factor with a trapped-ion computer. They also note classical clock rates (~10 GHz) versus ions (~1 MHz) make "quantum supremacy" harder for ions (p. 4) → hardware-landscape
- Scale demonstrated (2019): ~100-ion linear chains and 300-ion Penning crystals have meaningful control but no arbitrary entanglement. The largest fully controlled register is 20 ions. D-Wave 2000Q has thousands of annealing qubits with limited connectivity, short coherence and no demonstrated entanglement (pp. 3-5) → hardware-landscape
- The authors say scaling is held back by the optical and electronic control burden (bulk optics, external voltage supplies), whereas other platforms co-fabricate controls on the chip. They add: "the winning technological modality... is still far from certain" (p. 5) → hardware-landscape
- Rydberg-atom qubits have much shorter lifetimes than ions. Ions' advantages are the best coherence-to-gate-time ratio, the best single-qubit, SPAM and readout fidelity, and identical qubits (pp. 4-5) → hardware-landscape
- Demonstrated algorithms (2019): Deutsch-Jozsa (2003), teleportation (2004, 73-78%), semiclassical QFT (2005), Grover on 2 ions (60% vs 50% classical), Shor factoring 15 on 5 ions (2016, 99% success), VQE for H2/LiH and H2O up to 11 ions, 53-qubit analog Ising simulation (pp. 25-26) → hardware-landscape
- Error correction in ions: only small demonstrations so far (3-qubit repetition codes, 7-ion and 4-ion detection codes). A logical qubit better than its physical qubits had not been shown (pp. 32-33) → hardware-landscape
- Near-term targets named: 50-100 ion simulators without error correction (pp. 1, 26) → hardware-landscape

## Gaps
- Requested concepts not covered: none of the other hardware domains. The authors only compare platforms in passing.
- Coherence-and-fidelity: no mention of quantum volume or cross-entropy benchmarking. T1/T2 are discussed only briefly. The two-qubit vs single-qubit error comparison is covered above.
- Not read: §IV.B.3 end, §V (integrated photonics, chip-scale traps) and §VI (NISQ outlook, species/temperature choice) were seen only in the table of contents.
- Level: university/specialist review. The paper is a 2019 snapshot, and numbers have since been surpassed.
