---
source: saffman-2025
concepts: [neutral-atom-qubits, coherence-and-fidelity, hardware-landscape, logical-qubit-experiments, quantum-advantage-experiments]
---

Accessed: full text of arXiv:2505.11218v3 (9 Nov 2025), lecture notes from Varenna school July 2024, updated to summer 2025. Page numbers = arXiv page. Author M. Saffman is at UW-Madison and Infleqtion (a neutral-atom company); the author reports the numbers, many from his own group's experiments (refs 39, 40, 44). Hardware numbers date from 2022-2025.

## State of the art (Sec. 2, p. 5-7)
- Per the author, mid-2025 state of the art: 2D arrays with hundreds of qubits, coherence times of several seconds, one- and two-qubit gate times from a few microseconds to under 1 microsecond, and single-shot measurement/SPAM fidelity above 99% (p. 5). → neutral-atom-qubits
- Qubit-count records: several arrays with more than 1000 trap sites; latest is a 2D array with 6100 atoms loaded on average into 12000 sites, and 2000 atoms deterministically rearranged into defect-free patterns (p. 5-6). → neutral-atom-qubits
- Arrays can be assembled in 3D, and about 1 mW of trap light per site is needed, so 10^6 sites would need about 1 kW (5 um pitch gives roughly 5 mm per side); the challenges are thermal management and scattered light in high-resolution optics (p. 6). → neutral-atom-qubits
- Defect-free rearrangement of N atoms needs occupancy imaging with error and atom loss both below 1/N. A reported occupancy measurement reached fidelity 0.99991 with loss probability about 7e-4 (ref 67) (p. 6). → neutral-atom-qubits
- State-resolved fluorescence imaging trades speed for quality: the best fidelity-plus-retention results needed the longest integration times, because faster imaging means more scattering, heating and loss. Cavity readout is fast (a few us) but integrating cavities with big arrays is unsolved (p. 7, 21). → neutral-atom-qubits
- Free-space imaging measurement times remain orders of magnitude longer than gate times; high-fidelity measurements well below the surface-code threshold need at least a few ms (p. 17, 21). → neutral-atom-qubits
- Reported gate fidelities (author's review, p. 5): F>0.9999 for global microwave-driven rotations, F>0.999 for site-selective single-qubit gates, F>0.99 for two-qubit gates. This is the source's statement that two-qubit gates are less accurate than single-qubit gates (infidelity roughly 10x or more higher), with no claim that they are slower in time terms (both are us to sub-us). → coherence-and-fidelity
- Best Rydberg CZ fidelity cited: F=0.9971(5) in Sr (ref 107); the author expects F>0.999 soon, perhaps first in Sr and Yb, which use one-photon Rydberg excitation from the metastable clock state (p. 9). → coherence-and-fidelity
- Rydberg CZ fidelity above 99% has been shown with four elements (87Rb, 133Cs, 88Sr, 171Yb); the first Rydberg-gate demonstrations (2010-ish) had low fidelity and improved over years (p. 7, Fig. 4 p. 8). → neutral-atom-qubits
- The platform ranking given: trapped ions, superconducting circuits, photonics, semiconductor electrons, and neutral atoms are the few platforms that have combined isolation and control well; the connectivity problem exists on all of them (p. 2). → hardware-landscape
- The author says neutral atoms' clock rate is slow compared with other platforms (p. 12). → hardware-landscape
- The author contrasts neutral atoms with superconducting circuits and quantum dots: atoms add error channels from motional heating, leakage (frequent because atoms have many accessible levels) and atom loss; leakage also occurs in superconductors but less prominently (p. 21). → hardware-landscape

## Why Rydberg gates are limited (Sec. 3, p. 7-11)
- Rydberg blockade (proposed 25 years before, Lukin 2001) gives CZ gates; atoms must be in a ground/Rydberg superposition during the gate (p. 7-8). → neutral-atom-qubits
- Reasons for better fidelity: colder atoms (early gates above 50 uK, recent high-fidelity ones below 10 uK), because motion causes stochastic gate phases and fluctuating interaction strength; shaped flat-top Rydberg beams; and laser noise reduction, where phase noise near the Rabi frequency is especially harmful and cavity filtering of the laser helped (p. 8-9). → neutral-atom-qubits
- Time-optimal gate pulses that minimize time in the Rydberg state lower scattering errors and have given the highest fidelities (p. 7, 10-11). → neutral-atom-qubits
- Fundamental bound: infidelity is at least about 2/(V * tau_R), with V the Rydberg-Rydberg interaction energy and tau_R the Rydberg lifetime. For Cs 68p at 2.5 um (V = 2pi x 215 MHz, room-temperature lifetime 198 us) this gives about 7.5e-6. Best known protocols are within a factor 2 to 19 of the bound (p. 10-11). → neutral-atom-qubits
- A two-qubit gate fidelity may not map directly to error-correction performance; optimizing gate protocols for syndrome-extraction performance can do better (p. 7). → coherence-and-fidelity
- Crosstalk: with array pitch r at least 4.6 times the in-pair spacing, gate infidelity from neighbor-pair interactions is bounded by 1e-4 (p. 16-17). → coherence-and-fidelity
- Leakage out of the qubit basis arises mainly from polarization errors on gate beams and decay from excited/Rydberg states; even 171Yb can be trapped in metastable triplet or Rydberg states. Leakage detected at a known site becomes an erasure error, which helps codes (threshold can rise by close to an order of magnitude when erasures dominate and are biased) (p. 21-22). → coherence-and-fidelity

## Connectivity and timescales (Sec. 4, p. 11-18)
- Two connectivity tools in neutral atoms: long-range Rydberg interactions and physical transport of atoms; they act at different space and time scales (abstract, p. 2). → neutral-atom-qubits
- Interaction strength scales as 1/R^3 at short range (resonant dipolar) and 1/R^6 at long range (van der Waals); at d=10 with 1.4 um in-code spacing the needed distance 14 um is beyond demonstrated gates. A proposed interaction near 2pi x 6 MHz at 14 um gives CZ with F=0.9992 in 0.46 us (calculation, ref 128) (p. 13-14). → neutral-atom-qubits
- Author's analysis (rotated surface code with distance d, 100 logical qubits, physical error 0.0008): d=10 gives logical error near 1e-6 and needs 19900 physical qubits plus magic-state overhead; this is his "Megaquop" target (p. 12). → logical-qubit-experiments
- Transversal logical CZ via sequentially scanned long-range Rydberg gates: with 0.5 us beam-pointing and 0.46 us CZ, about 90 us; it is the fastest option but the author concludes it does not scale beyond d of about 10 without a longer interaction range (p. 12-15, 18). → neutral-atom-qubits
- Atom transport: tweezers moved with acousto-optic deflectors, or interference patterns. The speed is limited by motional heating; minimal-jerk profiles are better than constant-jerk ones; move time scales as distance^(1/3) (p. 15-16). → neutral-atom-qubits
- Transport-based logical CZ for d=10: move 64 um with 0.1 motional quanta of heating takes about 270 us (about 2 to 5 times slower than the Rydberg approach with sub-us beam pointing); averaged over a 10x10 logical array about 490 us; with a common entangling zone about 530 us. The author concludes cycle time for 100 logical qubits is about 1 kHz at best (p. 17-18). → neutral-atom-qubits
- Per the author, lattice surgery is not competitive on speed because time is dominated by measurement (ms scale); one move of a lattice period takes about 71 us (p. 17-18). → neutral-atom-qubits
- Per the author, transport is the fastest option based on current experimental capabilities, since lattice surgery is measurement-limited and long-range Rydberg gates are range-limited (p. 18). → neutral-atom-qubits
- Qubit transport in atoms needs only a few control signals, unlike ion shuttling with many electrodes, which also heats the ions and requires recooling (p. 15). → neutral-atom-qubits
- Logical-qubit experiments using atom transport (refs 19, 45, 46, 47) and first magic state distillation (ref 50) are listed as demonstrated by 2025 (p. 5). Details not given in this source. → logical-qubit-experiments

## Mid-circuit measurement, two species (Sec. 5, p. 18-21)
- Problem: measuring an ancilla by fluorescence disturbs nearby data atoms, because they act as resonant absorbers separated by only a few wavelengths. Workarounds are transport to a measurement zone, hiding or shelving data qubits (adds errors), cavities, or two species (p. 18-19). → neutral-atom-qubits
- A two-species array (e.g. Rb with Cs; Rb-K also has resonances) needs the same gate operations as single-species syndrome extraction, with strong inter-species Forster resonances. The author says interspecies Rydberg entanglement fidelity has not yet matched single-species gates (p. 19). → neutral-atom-qubits
- Ancillae of one species can be recooled without disturbing the data species, and roles can be swapped to recool data atoms. This gives mid-circuit cooling that appears uniquely straightforward in two species (p. 19-20, 21-22). → neutral-atom-qubits
- A second species used as a repetition code (N atoms) multiplies photon flux by about N and shortens measurement time about N times without cavities; calculated preparation under 5 us for N around 5 (a proposal, not a measurement) (p. 20). → neutral-atom-qubits
- Mid-circuit measurements have only recently been shown for neutral atoms; it is too early to say which method or element is best (p. 21). → neutral-atom-qubits

## Atom loss, heating, leakage (Sec. 6, p. 21-22)
- Three new error channels, the "HLL" set: heating, leakage, loss (p. 21). → neutral-atom-qubits
- Loss sources: background gas collisions, photoionization from Rydberg states, and atoms drifting away when in untrapped states during gates. Cryogenic vacuum has reached single-atom lifetimes of about 6000 s (p. 22). → neutral-atom-qubits
- Mitigation: codes tolerating missing qubits; continuous replacement of lost atoms has been demonstrated to keep 1000-qubit arrays filled, but integrating detection and replacement into the error-correction cycle is still open (p. 22). → neutral-atom-qubits
- The author gives two paths beyond NISQ: high-performance NISQ (needs mainly higher gate fidelity) and fault-tolerant computing (needs orders of magnitude more qubits and only moderate fidelity gains); HLL problems must be solved for deep FTQC circuits (p. 2, 22). → hardware-landscape

## Fidelity versus qubit count (Sec. 1, p. 3-5)
- Effective circuit fidelity is estimated as exp(-epsilon * V_eff), with epsilon the two-qubit infidelity and V_eff roughly the number of two-qubit gates; classical simulation cost grows as 2^A with A the entanglement-cut area. The author concludes that fidelity, not qubit count, is the key to raising classical cost; utility experiments use n around 100 and epsilon around 0.001 (p. 3-4). → coherence-and-fidelity
- NISQ processors are typically limited by the two-qubit gate fidelity (p. 3). → coherence-and-fidelity
- Random circuit sampling "supremacy" experiments (refs 21-25) show tasks beyond classical reach but without broader utility, and classical algorithms have competed back (refs 30, 31) (p. 3). → quantum-advantage-experiments
- Even at very high fidelity, code rate is at best 1/5 and universality needs magic state distillation (p. 5). → logical-qubit-experiments

## Not covered / level
- Requested but not covered: T1/T2 definitions (only "seconds" coherence), randomized benchmarking, quantum volume details (mentioned in passing p. 4), cross-platform numbers (no table).
- Level: specialist/university lecture notes; heavy Rydberg physics. Author is affiliated with Infleqtion; also some numbers are theoretical estimates, flagged above.
