---
source: slussarenko-2019
concepts: [photonic-qubits, quantum-advantage-experiments, hardware-landscape, divincenzo-criteria]
---

Accessed: full text of arXiv:1907.06331v2 (11 Dec 2019), 11 pages; pages below are arXiv pages. Review by Slussarenko and Pryde (Griffith University, a photonic-QC research group; hardware numbers are as of 2019).

## Encodings and basics
- A qubit is commonly encoded in a dual-rail form: one photon shared between two modes (orthogonal polarizations or two paths). Time-bin, transverse spatial, frequency and temporal-mode encodings are gaining attention (p. 2, §I.B) → photonic-qubits
- Single-qubit operations (moving population between the two modes, applying relative phases) are done with interferometry and are easy and very high fidelity (p. 1-2) → photonic-qubits
- Optics can also encode multi-level qudits, and several degrees of freedom of one photon can be used at once (p. 2, §I.B) → photonic-qubits
- Putting many qubits into one photon across many modes (Reck-type universal unitary) needs exponentially many components, so one qubit per photon with several photons is needed (p. 2) → photonic-qubits
- A two-qubit gate needs a conditional pi phase, a nonlinear optical effect that is extremely weak at the single-photon level. It can be mimicked with linear optics plus measurement, giving a probabilistic gate (postselected or heralded) (p. 2) → photonic-qubits
- The authors say photons satisfy roughly five of the seven DiVincenzo criteria; the hard ones are due to weak photon-photon interaction (deterministic two-qubit gates). Photon loss and sometimes the need for an optical quantum memory add overhead (p. 1) → divincenzo-criteria
- Photons are called clean, decoherence-free flying qubits, needed for networking and distributed computing (p. 1) → photonic-qubits

## KLM
- KLM (Knill, Laflamme, Milburn, 2001) needs only linear optics, single-photon detection and classical feed-forward. It uses nonclassical interference conditioned on heralding detections for a photon-number-nonlinear phase, builds nondeterministic gates, and applies repeat-until-success with teleportation of successful gates (p. 2, §I.B; p. 8) → photonic-qubits
- KLM resource scaling is linear in qubit number (not exponential), but the overhead of ancilla photons and circuitry is large, because gates are nondeterministic (p. 2) → photonic-qubits
- KLM proved scalability of optical processing but a full-scale error-corrected machine was not buildable then (p. 8, §III) → photonic-qubits

## Detectors
- Photon detectors are characterized by efficiency, reset time, timing jitter, dark counts and photon-number resolution; no ideal detector exists (p. 2-3, §II.A) → photonic-qubits
- Si avalanche photodiodes (Geiger mode): reset under about 100 ns, about 100 dark counts/s, efficiency up to about 65%, no number resolution, not for telecom bands. At 65% efficiency, detecting ten photons with ten detectors has probability under 2% (p. 3) → photonic-qubits
- Superconducting nanowire detectors (SNSPD): reset about 40 ns, efficiency about 0.93 and recently 0.95 or more at telecom wavelength, operating at 0.8-3 K, but no number resolution (p. 3) → photonic-qubits
- Transition-edge sensors (TES): resolve up to about 20 photons, efficiency about 0.95 to 0.98, but slow (about microsecond reset, 50 ns or more jitter; best reported reset about 460 ns, jitter 2.3 ns). The authors say practical PQC likely needs clock cycles of 10 ns or less (p. 3) → photonic-qubits

## Sources
- Wanted: very many (N roughly 10 to 10^11) simultaneous on-demand single photons that are efficiently collected, pure, indistinguishable and compatible with low-loss materials. The authors state no source yet satisfies all of these (p. 3, §II.B) → photonic-qubits
- Spontaneous parametric downconversion (SPDC) makes heralded single photons or entangled pairs probabilistically. A pump photon splits into signal and idler under energy and momentum conservation (p. 4) → photonic-qubits
- Simple bulk SPDC has coupling loss, spectral entanglement between twins (lowering heralded purity), and heralding efficiency of about 10-15% (some about 30%). Experiments reached up to 10 photons with low rates (p. 4) → photonic-qubits
- Periodically poled crystals (quasi-phase matching) plus group-velocity matching give pure, spectrally uncorrelated telecom photons. Reported heralding efficiency is above 0.8, state purity 0.997 or more, and entangled-state fidelity above 0.99 (p. 4-5) → photonic-qubits
- SPDC/four-wave-mixing pair probability per pulse is limited to about 1% or less, because higher pump power creates multi-pair noise. Combining n sources succeeds with probability only xi^n, so direct combining does not scale (p. 5) → photonic-qubits
- Multiplexing (spatial across n sources, or temporal with a delay network) approaches deterministic output, efficiency 1-(1-xi)^n in theory, limited by switch/component loss. A demonstration with all features gave about 0.6 single-photon probability at the output fiber and about 0.9 interference visibility (p. 5-6) → photonic-qubits
- Quantum-dot sources are on-demand and bright, but fiber coupling is about 33% or less and different dots emit distinguishable photons (p. 5) → photonic-qubits
- Optical quantum memory, from a simple switchable delay loop up to matter-based memories, can synchronize probabilistic sources (p. 6) → photonic-qubits

## Integrated photonics
- Integrated waveguide chips are the path to scale. Key properties: component density, low propagation and coupling loss, fast reconfiguration, ideally on-chip sources and detectors (p. 6, §II.E) → photonic-qubits
- Materials named: femtosecond-laser-written glass (3D circuits, polarization qubits), lithium niobate (sources and GHz electro-optic switching), silicon (dense, low loss, foundry compatible) (p. 6-7) → photonic-qubits
- Example chip (Wang et al., Science 2018): 16 pair sources, 93 phase shifters, 122 beamsplitters, 256 crossers, 64 grating couplers, 2 SNSPD detectors, producing 16-dimensional entangled photon pairs (Fig. 2, p. 7) → photonic-qubits
- SNSPDs have been integrated on chip since 2011. The authors report component counts on integrated quantum photonic chips grew exponentially (Moore's-law-like) (p. 7-8) → photonic-qubits
- Integrated platforms suffer loss from absorption, waveguide roughness and chip coupling. Mitigations: purer materials, high-index-contrast waveguides, on-chip sources and detectors, modular architectures (p. 8) → photonic-qubits

## Measurement-based (cluster-state) computing
- In one-way computing a hard-to-make entangled multi-photon cluster state is made offline with nondeterministic operations. Then computation uses only single-qubit operations, measurements and classical feed-forward, which suit optics (p. 10, §III.B) → photonic-qubits
- Cluster schemes use fewer resources (Bell pairs per effective two-qubit gate) than many other optical schemes, and are more loss-tolerant than KLM (p. 10) → photonic-qubits
- Clusters are built by nondeterministic fusion. A failed fusion shrinks the pieces but does not destroy them. Below a threshold of missing nodes or links, percolation theory still gives a universal resource (p. 10) → photonic-qubits
- Ballistic cluster computing: sources emit entangled photons each time step, forming a 3D cluster layer by layer that is measured on the fly, with no photon storage. Only a few tens of photons need exist at once (p. 10) → photonic-qubits
- The authors say loss is the primary noise source in optics, and that cluster schemes are widely seen as a realistic path to scalable photonic QC and may be more realistic than gate-based models (p. 8, 10) → photonic-qubits

## Intermediate demonstrations and boson sampling
- Photonic CNOTs, Toffoli and Fredkin (controlled-SWAP) gates have been shown by probabilistic/heralded schemes. A method (2009) adds control to any unitary using extra degrees of freedom of the photon. Small algorithms demonstrated include factoring 21 (p. 8-9) → photonic-qubits
- Early chips did not immediately beat bulk optics, for example the compiled Shor factoring of 15 (p. 8) → photonic-qubits
- Boson sampling (non-universal): n single photons enter m≫n modes, pass a random unitary, and the output distribution is classically hard to sample. There is strong theoretical evidence of quantum advantage (p. 9-10) → quantum-advantage-experiments
- The authors say advantage may need roughly 50-100 photons, and strict photon-loss and noise limits must still be met. As of 2019 they report photon numbers in experiments grew from 2-4 up to 12, and that no advantage had yet been demonstrated (p. 10-11) → quantum-advantage-experiments
- Intermediate-scale photonic devices will lack full error correction, so loss and noise need other handling, for example machine learning (p. 10) → photonic-qubits

## Networking and landscape
- Photons are the natural carriers for linking quantum processors. Photonic processors skip stationary-to-flying conversion; other platforms need interconversion and possibly wavelength adjustment (p. 11, §IV) → hardware-landscape
- Loophole-free Bell tests were done with photons and matter qubits (p. 11) → hardware-landscape
- Per the authors, a universal quantum computer remains a challenging quest in any system, photonic or not (p. 8) → hardware-landscape
- The authors report that controlling an arbitrary unitary is generally impossible for matter-based qubits, an advantage of fields (p. 9) → hardware-landscape
- ⚠️ The abstract says photonic QC is a "leading contender"; this is the authors' own field's view, not a neutral comparison across platforms → hardware-landscape

## Not covered / level
- Requested but not covered: coherence-and-fidelity (no T1/T2 or gate-fidelity comparisons, and no numbers on two-qubit versus single-qubit gate error; only qualitative: photonic single-qubit gates are very high fidelity, two-qubit gates are hard, p. 1-2), superconducting, trapped-ion, neutral-atom, spin, topological qubits, random circuit sampling. DiVincenzo criteria only briefly (p. 1).
- Level: university / specialist review, pre-2020 numbers (no Jiuzhang).
