---
source: preskill-2018
concepts: [nisq-era, variational-algorithms, error-mitigation, running-on-hardware, coherence-and-fidelity, threshold-theorem, resource-estimation]
---

Accessed: full text of the Quantum 2, 79 (2018) article (arXiv:1801.00862v3), pages 1-16, from the extracted text. Written in July 2018; hardware figures are from that date.

## nisq-era
- NISQ is a term coined by the author for the coming era, "Noisy Intermediate-Scale Quantum"; intermediate scale means roughly 50 to a few hundred qubits, noisy means imperfect control of the qubits (§4.1, p. 4-5) → nisq-era
- 50 qubits is a milestone because it exceeds what the most powerful supercomputers can simulate by brute force; the author calls it fuzzy because classical simulation cost also depends on circuit depth (§4.1, p. 5, footnote 2) → nisq-era
- The abstract says 50-100 qubit machines might perform tasks beyond today's classical computers, but gate noise limits the size of circuits that can be run reliably (abstract, p. 1) → nisq-era
- NISQ means noisy gates not protected by quantum error correction (§4.2, p. 5) → nisq-era
- Naive limit: with two-qubit gate error at about 0.1% or worse, circuits with much more than about 1000 two-qubit gates are not expected to work, since noise overwhelms the signal; this caps NISQ computational power (§4.2, p. 5) → nisq-era
- Rule of thumb: in a generic circuit of G gates one fault anywhere may ruin the result, so it is unreliable if error per gate is much larger than 1/G; the author says this may be too pessimistic for some algorithms (§6.4, p. 9) → nisq-era
- Near-term experiments will explore of order 100 qubits with circuit depth below 100, maybe much less (§6.2, p. 8) → nisq-era
- Qubit count is not the only measure of quality: gate accuracy, gate speed, measurement accuracy, connectivity and fabrication yield also matter (§4.2, p. 5) → nisq-era
- Quantum supremacy is the author's term for tasks a quantum device can do that no existing or easily foreseeable classical device can, regardless of usefulness; commercially usefulness matters, and supremacy is mainly a sign of progress toward valuable applications (§6, p. 7) → nisq-era
- A quantum speedup normally means beating the best classical hardware running the best classical algorithm; classical machines keep improving (exascale expected soon), so quantum chases a moving target (§6, p. 7) → nisq-era
- Because NISQ devices are imperfect, it may be hard to validate that the answer is right, especially for quantum simulation; better verification methods are needed (§6, p. 7) → nisq-era
- NISQ is unlikely to change the world by itself; it is a step toward more powerful technology, useful for exploring many-body physics, with business applications uncertain (§4.1, p. 5; §8, p. 15) → nisq-era
- The author is confident of substantial impact in decades but not about commercial potential in the next 5-10 years (§1, p. 1) → nisq-era
- Probably out of NISQ reach: HHL matrix inversion may be too expensive without error correction (§6.6, p. 11); quantum recommendation systems are too costly to validate (§6.7, p. 12); accurate simulation of large molecules and materials may need error correction (§6.9, p. 13) → nisq-era
- Quantum computers are not expected to efficiently solve hard instances of NP-hard problems; exhaustive-search speedups are modest (§3.1, p. 3) → nisq-era
- Long-term role of error correction: the truly transformative technologies will probably have to be fault tolerant, which may be distant; the community should work to hasten that era (§8, p. 16) → nisq-era
- Error correction is the basis for believing quantum computers scale; it encodes information in a highly entangled state so the environment cannot learn it (§2, p. 2; §3.2, p. 4) → nisq-era
- Why quantum computing is hard: observing a system disturbs it uncontrollably, so qubits must be nearly isolated yet strongly interacting, controllable and readable (§3.2, p. 4) → nisq-era
- Near-term experiments should demonstrate an error-corrected qubit with enhanced control (§7, p. 14) → nisq-era
- D-Wave 2000Q (about 2000 qubits) is a quantum annealer, not a circuit-based computer (§6.3, p. 8-9) → nisq-era
- No convincing theory or experiment yet shows annealers beat the best classical hardware and algorithms (§6.3, p. 9) → nisq-era
- An annealer is the noisy version of adiabatic quantum computing; adiabatic equals circuit-based power only for noiseless qubits and with high qubit overhead, and there is no good argument that noisy annealers scale (§6.3, p. 9) → nisq-era
- Annealers have mostly been stoquastic (possibly easy to simulate classically); non-stoquastic ones are coming and may have more speedup potential (§6.3, p. 9) → nisq-era

## variational-algorithms
- The emerging near-term paradigm for optimization is hybrid quantum-classical: a quantum processor prepares an n-qubit state, all qubits are measured, a classical optimizer uses the outcomes to tweak the state preparation, and the cycle repeats until convergence (§6.1, p. 8) → variational-algorithms
- Applied to classical combinatorial optimization it is called QAOA; applied to quantum problems such as low-energy states of molecules it is called the Variational Quantum Eigensolver (VQE) (§6.1, p. 8) → variational-algorithms
- Prospects: nobody knows whether QAOA/VQE on NISQ hardware will beat well-honed classical approximate methods; early devices may fall short but results could encourage hope and spur improvement (§6.1, p. 8) → variational-algorithms
- A quantum advantage for approximate optimization is an open question, plausible because of the gap between best classical approximation and the NP-hardness barrier; NISQ may be inadequate to show it (§6.1, p. 7-8) → variational-algorithms
- Heuristics found experimentally can work before being explained (simplex method, deep learning), so quantum heuristics may be validated experimentally (§6.2, p. 8) → variational-algorithms
- Some noise-resilient tensor-network constructions are used for quantum optimization with VQE (§6.4, p. 9) → variational-algorithms
- The summary names hybrid quantum-classical algorithms for classical and quantum optimization as the specific near-term thing to try (§8, p. 15) → variational-algorithms

## error-mitigation
- NISQ devices will not use error correction in the near term, but methods for mitigating noise may matter a lot in the NISQ era (§6.4, p. 9) → error-mitigation
- For some problems only a few circuit locations can cause bad failure (low depth with tolerable constant final error per qubit, or early errors that decay away), so noisy circuits may beat the 1/G rule (§6.4, p. 9) → error-mitigation
- Researchers should find ways to make circuits noise resilient to extend NISQ reach; tradeoff: more noise resilience may make circuits easier to simulate classically (§6.4, p. 9-10) → error-mitigation
- Near-term algorithms should be designed with noise resilience in mind (§8, p. 15) → error-mitigation
- Near-term error-correction experiments should suggest more effective noise mitigation techniques (§7, p. 14) → error-mitigation
- ⚠️ The paper names no concrete mitigation technique, only pointers and general principles (§6.4, §7) → error-mitigation

## running-on-hardware
- Near-term quantum computers will likely be special-purpose devices that most users reach via the cloud (§6, p. 7) → running-on-hardware
- Google (72-qubit) and IBM (50-qubit) superconducting devices had been announced (§4.1, footnote 1, p. 5) → running-on-hardware
- Best-controlled platforms are trapped ions and superconducting circuits; superconducting gates are about 1000 times faster than ion-trap gates (§4.2, p. 5) → running-on-hardware
- Connectivity (which pairs allow accurate two-qubit gates) and how many fabricated qubits perform well enough matter when comparing devices (§4.2, p. 5) → running-on-hardware
- It is unknown whether low error rates can be kept as devices grow to many qubits (§4.2, p. 5) → running-on-hardware

## coherence-and-fidelity
- 2018 two-qubit gate error with the best trapped-ion and superconducting hardware: above the 0.1% level, often much worse (§4.2, p. 5) → coherence-and-fidelity
- Measurement error about 1% for superconducting qubits, much better for trapped ions (§4.2, p. 5) → coherence-and-fidelity
- Lower gate error lets larger circuits run without error correction and lowers later error-correction overhead; Microsoft's topological program bets on much lower error rates (§7, p. 14-15; §8, p. 15) → coherence-and-fidelity

## resource-estimation
- Error correction has a large overhead: many extra physical qubits per protected qubit, and extra gates, so reliable error-corrected machines are not near (§3.2, p. 4; §4.2, p. 5) → resource-estimation
- Algorithms with thousands of protected qubits (e.g. factoring numbers thousands of bits long) need millions of physical qubits or more (§7, p. 14, citing ref. 56) → resource-estimation
- Going from hundreds to millions of physical qubits is the "quantum chasm" and will take time; full scalability needs advances in science and engineering (§7, p. 14-15) → resource-estimation

## threshold-theorem
- Better physical gate accuracy lowers the overhead of error correction (§7, p. 14; §8, p. 15) → threshold-theorem
- ⚠️ The paper does not state the threshold theorem or any numeric threshold; this is only the qualitative link between gate error and overhead → threshold-theorem

## Not covered / level
- Not covered: Qiskit or software, concrete mitigation techniques (e.g. extrapolation), T1/T2 coherence times, threshold value. Shor's algorithm is mentioned only as the factoring example (§3.1, p. 3); the paper says factoring thousands-of-bit numbers needs fault tolerance (§7, p. 14).
- Level: intro / general-audience technical overview; 2018 snapshot, hardware numbers outdated.
