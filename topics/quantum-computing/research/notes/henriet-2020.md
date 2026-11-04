---
source: henriet-2020
concepts: [neutral-atom-qubits, coherence-and-fidelity, hardware-landscape]
---

Accessed: full text of arXiv:2006.12326v2 (Quantum, accepted 2020-09-17, CC-BY 4.0), read from the extracted file; page numbers are the arXiv PDF pages. Vendor caveat: the authors are mostly from Pasqal (a neutral-atom company) plus academic groups (Institut d'Optique), and the paper emphasizes the technological choices of Pasqal and the Browaeys/Lahaye group (p. 2). All performance and comparison claims below are the authors' own, as of mid-2020.

## neutral-atom-qubits: trapping, register, readout
- The authors say each qubit is two electronic states of an atom; rubidium is a common choice because its laser technology is mature (p. 4). → neutral-atom-qubits
- Digital-mode qubit: the two hyperfine ground states (F=1, F=2) of rubidium, with lifetimes of tens of years, so there is no radiative coupling to the environment (p. 7). → neutral-atom-qubits
- Loading: a cold cloud of about 10^6 atoms (about 1 mm^3) in a 3D magneto-optical trap inside an ultra-high-vacuum chamber. A strongly focused trapping beam (about 1 µm spots, "optical tweezers") isolates single atoms, at most one per tweezer (p. 5). → neutral-atom-qubits
- Tweezer geometry (1D, 2D or 3D) is set holographically with a spatial light modulator (SLM) that imprints a phase pattern. The authors claim scalability is limited only by trapping laser power and optical-system quality (p. 5). → neutral-atom-qubits
- Loading is random: only about 50% of tweezers are filled. A fluorescence image shows which are filled (p. 5). → neutral-atom-qubits
- Rearrangement: moving tweezers steered by 2D acousto-optic deflectors (AOD) shift atoms to build a defect-free sub-register, with success rate above 99% (p. 6). An algorithm on an external GPU, fed via FPGA, computes the moves within a few tens of ms. A final image confirms the assembly (p. 6). A single-atom move takes under 1 ms (Fig. 5, p. 7). → neutral-atom-qubits
- The register is not permanent, unlike superconducting, silicon or NV qubits: it is rebuilt every cycle (prepare, process, read out) (p. 4). → neutral-atom-qubits
- Timing (authors' device, 2020): processing takes under 100 µs, but the whole cycle with loading and readout takes about 200 ms. The acquisition (measurement) rate is about 5 Hz (pp. 6, 12). → neutral-atom-qubits
- Readout: a fluorescence image on an EMCCD camera, with |0> bright and |1> dark. Detection efficiency above 98.6% has been reported (cited result, ref. 13). The authors call this comparable to superconducting processors (p. 6). Cycles are repeated many times to gather statistics (p. 6). → neutral-atom-qubits
- Single-qubit gates: Raman laser pulses. Rotation angles are set by the Rabi frequency, detuning and phase, and pulse duration, intensity and phase are tuned with AOM/EOM modulators (p. 9). → neutral-atom-qubits
- Individual addressing is possible because atoms sit several micrometers apart and the lasers are tightly focused (pp. 7-8). → neutral-atom-qubits

## neutral-atom-qubits: Rydberg blockade and gates
- Ground-state atoms a few µm apart barely interact. The Jaksch et al. 2000 proposal excites atoms to Rydberg states, whose dipole moment can be about 1000 times larger, so the dipole-dipole interaction shifts the doubly excited state and prevents two atoms being excited together. This is the Rydberg blockade (p. 10). → neutral-atom-qubits
- Blockade as logic: exciting the first atom conditions the excitation of the second (p. 10). → neutral-atom-qubits
- CZ gate by 3 pulses (pi on control, 2pi on target, pi on control). The lasers couple |0> to the Rydberg state |r>. |11> is untouched by all pulses; |01> and |10> pick up −1 from a 2π rotation of one atom; for |00> the blockade stops the target's pulse and the control's two π pulses give −1. The result is diag(−1,−1,−1,1) = e^{iπ}·CZ, i.e. CZ up to a global phase. CNOT = CZ with Hadamards on the target before and after (Box 1, pp. 9-10). → neutral-atom-qubits
- Authors' claims for the gate: it takes about 1 µs (1 MHz QPU clock), and more than 100 gates fit within the typical coherence time (p. 11). The cited experimental two-qubit fidelity is F = 94.1% (ref. 21, Lukin group). The authors expect large improvement from optimal control (shaped pulses; needs AWGs sampling at about 100 ns) (p. 11). Transient Rydberg population is named as an error source (p. 11). → neutral-atom-qubits
- Connectivity: gates can act between distant atoms, within the blockade radius. The authors' routing simulation (Cirq compiler, 48 qubits, average of 64 random circuits) finds 5 to 10 times lower gate overhead than nearest-neighbor connectivity (as in most transmon layouts) (Fig. 8, pp. 11-12). → neutral-atom-qubits
- Native multi-qubit gates: a Toffoli takes 7 pulses (CCZ with 5 pulses plus 2 Hadamards). The alternative is at least six CNOTs plus single-qubit gates, over 30 pulses (Fig. 9, p. 12). → neutral-atom-qubits

## neutral-atom-qubits: digital vs analog mode
- Digital: gate circuits, with laser pulses addressing chosen atoms individually. Authors list universality and cross-device compatibility as advantages (pp. 2, 7). Analog: the lasers (for instance a global beam) realize a Hamiltonian, and the atoms evolve under the Schrödinger equation (pp. 2, 7, Fig. 6). → neutral-atom-qubits
- Analog Ising mode: ground state plus Rydberg state gives a Hamiltonian with a Rabi-frequency term, a detuning term, and a van der Waals interaction falling as 1/r^6 (Eq. 1, p. 13). The XY model comes from two dipole-coupled Rydberg states, with 1/r^3 interaction driven by microwaves (Eq. 2, p. 14). Combining state pairs and geometry gives other spin models, for example XXZ (p. 14). → neutral-atom-qubits
- Combined global and local addressing lets the user add controllable disorder (p. 14). → neutral-atom-qubits
- Analog mode can natively solve Maximum Independent Set on unit-disk graphs, because the blockade enforces the independent-set constraint (Box 5, p. 22). The authors argue that gate fidelity or quantum volume are not always the best criteria for judging a task-specific processor (p. 22). → neutral-atom-qubits
- Analog devices can reach arrays of a few hundred atoms, which the authors say is beyond classical simulation (p. 13). → neutral-atom-qubits

## neutral-atom-qubits: challenges and prospects (authors' view)
- Qubit count is currently limited by trapping laser power. A few thousand qubits would need higher-power lasers and better imaging optics (p. 15). → neutral-atom-qubits
- Atom lifetime in the trap is set by residual vacuum pressure and becomes limiting at a few thousand qubits. Remedies named: compact cryogenic QPUs, or faster loading, assembly and imaging. They expect about 10x better repetition rate (p. 15). → neutral-atom-qubits
- Decoherence from parasitic charges around the atoms must be reduced by designing the electrostatic environment. Better electronics (AWGs) would help fidelity (pp. 15-16). → neutral-atom-qubits
- The authors note that clock rate (1 MHz) and acquisition rate (5 Hz) are low relative to other platforms (p. 12). → neutral-atom-qubits
- Long term: optically interconnected multi-core processors. Surface-code error correction on large sizes is described as a possible path to fault tolerance; this needs atom-photon interfaces, which the authors call a great experimental challenge (p. 24). → neutral-atom-qubits

## coherence-and-fidelity
- The authors define fidelity F as a number between 0 and 1 giving the closeness of the produced state to the expected one. F = 99.5% means a 0.5% chance of an undesired outcome (p. 9). → coherence-and-fidelity
- Single-qubit gates: Rabi oscillations with very high contrast (refs. 17, 18) imply F above 99.5% (p. 9). Two-qubit Rydberg CZ/CNOT: F = 94.1% (ref. 21, 2018), with ~1 µs gate time (p. 11). So in this source the two-qubit gate is clearly the less accurate one (about 5.9% error vs under 0.5%). The text does not state the comparison explicitly, and the values come from different experiments. The two-qubit gate is also much longer than the single-qubit pulses, though no single-qubit duration is given. → coherence-and-fidelity
- Gate time versus coherence: more than 100 gates fit in the system's coherence time (p. 11). The authors discuss "quality factor" Q ~ 10^2, the ratio of coherent evolution rate to decoherence rate, for analog Rydberg operation. Interaction energies are tens of MHz, at least 100x above decoherence energy scales. Q estimates how many operations are possible before the system turns classical (p. 14). → coherence-and-fidelity
- Rydberg errors: transient Rydberg population (p. 11). Doppler dephasing of Rydberg atoms can be reduced by trapping them (p. 14). → coherence-and-fidelity
- Hyperfine ground-state qubit lifetime is of order tens of years, so spontaneous radiative decay is negligible for T1 (p. 7). Coherence time itself is not quantified. → coherence-and-fidelity
- Extra SWAP gates add errors, which motivates connectivity (p. 11). Quantum volume is mentioned only in passing (p. 22). → coherence-and-fidelity
- Readout efficiency above 98.6% (neutral atoms, ref. 13) is described as comparable to superconducting readout (p. 6). → coherence-and-fidelity

## hardware-landscape
- The authors claim neutral atoms have identical qubits by nature, whereas superconducting circuits and silicon spin qubits are "artificial atoms" needing very uniform fabrication (vendor view) (p. 2). → hardware-landscape
- They also claim larger connectivity and native multi-qubit gates compared with other platforms, and that scaling needs more tweezers rather than new chips (pp. 2, 12-13). → hardware-landscape
- Admitted weaknesses: slow clock (1 MHz) and slow acquisition (5 Hz) compared with other platforms (p. 12). Two-qubit fidelity at 94.1% in the cited experiments (p. 11). → hardware-landscape
- The NISQ era is defined as 50-1,000 qubit devices. The authors cite Google's Sycamore as outperforming supercomputers on one task (ref. 2) (p. 2). → hardware-landscape
- Not all hardware is equivalent: native operations depend on the platform (superconducting, neutral atoms, ions, photons), which motivates hardware-efficient algorithms (p. 21). → hardware-landscape
- A claimed target: 100-1,000 qubits; registers up to a few thousand are said to be possible (pp. 2, 24). Fault-tolerance paths named: surface code (via multi-core) or bosonic codes (p. 25). → hardware-landscape

## Not covered / level
- Requested but not in this source: no numbers for T1, T2, or randomized benchmarking. No atom-loss rate figures. No comparison table.
- Level: specialist review (university level), vendor-authored. Hardware numbers are from 2018-2020 and are dated.
