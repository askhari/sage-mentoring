---
source: divincenzo-2000
concepts: [divincenzo-criteria, coherence-and-fidelity]
---

Accessed: full text of arXiv:quant-ph/0002077v3 (13 Apr 2000), 9 pp., from the extracted text file. Page numbers are arXiv pages. Author is at IBM T.J. Watson; the paper is a 2000 overview (Fortschritte der Physik special issue). All hardware remarks are dated 2000.

## Framing

- The paper lists five requirements for quantum computation, plus two more for quantum communication; the five suffice for computation alone (p. 1 abstract; p. 2 §III; p. 6 §IV) → divincenzo-criteria
- The criteria come from the author's discussions with coworkers over several years, and are used to compare the many proposed physical implementations (p. 2 §III) → divincenzo-criteria

## Criterion 1: scalable physical system with well characterized qubits

- A qubit is any quantum two-level system (spin-1/2, atom ground/excited state, photon polarization); its state space is 2-dimensional complex, and n qubits need a 2^n-dimensional vector (p. 2 §III.1) → divincenzo-criteria
- "Well characterized" means: accurately known internal Hamiltonian, known couplings to other levels, to other qubits and to external control fields (p. 2) → divincenzo-criteria
- If the qubit has extra levels, the control must keep the probability of entering them small; how small is set by what error correction tolerates (p. 2) → divincenzo-criteria
- Pitfall: one electron shared between two quantum dots is not a two-qubit system, because superselection forbids superpositions of different particle number. It is one qubit (electron left vs right) (p. 2) → divincenzo-criteria
- 2000 survey of qubit candidates: ion-trap energy levels (Cirac-Zoller), neutral atoms, NMR spin states, quantum-dot and donor spins, quantum-dot charge states, superconducting charge and flux devices (p. 3 §III.1) → divincenzo-criteria (dated; platform list as of 2000)

## Criterion 2: initialization to a fiducial state such as |000...>

- Needed first because registers must start in a known state (p. 3 §III.2) → divincenzo-criteria
- Needed also because error correction consumes a continuous supply of fresh low-entropy qubits such as |0> (p. 3) → divincenzo-criteria
- If initialization is slow relative to gate time, a "conveyor belt" arrangement would be needed: qubits are carried away, reset, and brought back (p. 3) → divincenzo-criteria
- Two ways to initialize: natural cooling to the Hamiltonian's ground state, or projective measurement (a form of cooling), as in laser cooling and fluorescence of ions (p. 3) → divincenzo-criteria
- Natural thermalization is never faster than the decoherence time, so it is too slow for error correction; measurement-based cooling can be much faster (p. 3) → divincenzo-criteria
- 2000 remark: NMR demonstrations skipped cooling, and the author says NMR cannot scale until cooling schemes are implemented (p. 3) → divincenzo-criteria (dated)

## Criterion 3: decoherence times much longer than gate time

- Simplified definition: the time for a|0>+b|1> to become the mixture |a|^2|0><0| + |b|^2|1><1|; a fuller description lets decay depend on the initial state and includes "leakage" to other levels (p. 3) → coherence-and-fidelity
- Decoherence of neighbouring qubits may be partly correlated; error-correction thinking assumes neither fully correlated nor fully uncorrelated (p. 3) → coherence-and-fidelity
- Only the "relevant" decoherence time counts: e.g., fast orbital dephasing of an electron does not matter if the qubit is encoded in spin states (p. 4) → coherence-and-fidelity
- Quantum error correction (1995-6) means the required coherence does not grow with computation length (p. 4) → divincenzo-criteria
- Key number: if the decoherence time is about 10^4 to 10^5 times the gate ("clock") time, error correction can succeed. The author calls this stringent (p. 4) → divincenzo-criteria
- Same number for coherence vs gate time: threshold stated as a ratio of decoherence time to gate time, not an absolute time (p. 4) → coherence-and-fidelity
- Once this threshold is reachable, decoherence is not an obstacle to scalable computation (p. 4) → divincenzo-criteria
- Error-correction overhead in 2000 estimate: about 10 ancilla qubits per computational qubit, growing only logarithmically with computation size (p. 4) → divincenzo-criteria (dated estimate)
- Decoherence is system-specific: a spin near a device surface may differ from one in the bulk, so test experiments should use realistic device structures (p. 4) → coherence-and-fidelity

## Criterion 4: universal set of quantum gates

- Algorithms are sequences of unitaries on a few (usually at most three) qubits; physical devices only offer limited Hamiltonians (p. 4-5 §III.4) → divincenzo-criteria
- Three-qubit gates reduce to one- and two-qubit gates, and two-qubit interactions can be of a single type, cNOT (p. 5) → divincenzo-criteria
- Fixed interactions that cannot be switched off (NMR) can be cancelled by refocusing sequences (p. 5) → divincenzo-criteria
- Where cNOT is not directly available (exchange interaction in quantum dots, XY interaction), cNOT can be synthesized from the available interaction plus one-qubit operations; each proposal must exhibit such a sequence (p. 5) → divincenzo-criteria
- Pulse shape matters: if higher levels exist, the interaction must be switched smoothly and slowly (adiabatically). Gate clock time is set by pulse duration and the maximum attainable coupling strength (p. 5) → divincenzo-criteria
- A "bus qubit" (ion-chain vibration, cavity photon) mediates interactions when qubits do not couple directly, but adds decoherence channels during gates; a single bus may also hinder parallel gates (p. 5) → divincenzo-criteria
- Error correction requires fully parallel gate operation on a finite fraction of qubits; nearest-neighbour lattice interactions allow enough parallelism (p. 5) → divincenzo-criteria
- Gate errors count as another source of decoherence; tolerable random error is about 10^-4 to 10^-5 per gate operation, in the same range as the decoherence threshold (p. 5) → coherence-and-fidelity
- Same error figure stated for gates: random gate error per operation of about 10^-4 to 10^-5 is acceptable (p. 5) → divincenzo-criteria
- Systematic errors: conservative estimates demand roughly the square of the random-error figure, but some computations (quantum Fourier transform) may tolerate large over/under-rotation; large detectable errors (charge switching) may be tolerable (pp. 5-6) → coherence-and-fidelity
- Stabilizer codes use the same base toolkit (one-qubit gates plus cNOT); decoherence-free subspace codes of 3 to 4 qubits allow universal computation from exchange interactions alone (p. 6) → divincenzo-criteria
- ⚠️ The source gives no statement that two-qubit gates are slower or more error-prone than single-qubit gates; it only says single-qubit operations are "assumed to be more easily doable" than two-body ones (p. 5) → coherence-and-fidelity

## Criterion 5: qubit-specific measurement

- Ideal measurement returns 0 with probability p regardless of coherences or neighbouring qubits, without disturbing the rest of the computer (p. 6 §III.5) → divincenzo-criteria
- A non-demolition measurement also serves as initialization (criterion 2) (p. 6) → divincenzo-criteria
- Measurement quality is summarized by a "quantum efficiency" (100% ideal); it is incomplete as a fidelity measure, like the decoherence time for state damage (p. 6) → coherence-and-fidelity
- Low efficiency can be traded for resources: copy the output qubit's basis value with cNOTs onto about 1/q qubits and measure all; 1% efficiency is usable at the cost of hundreds of copies (p. 6) → divincenzo-criteria
- NMR works with very low efficiency by averaging over a macroscopic ensemble of molecules (p. 6) → divincenzo-criteria (dated)
- A fast measurement, on a timescale of about 10^-4 of the decoherence time, simplifies error correction; otherwise correction needs more gates (p. 6) → divincenzo-criteria
- General theme: trade-offs, e.g., with Bell-basis measurements and entangled-pair initialization, one-qubit gates alone suffice (p. 6) → divincenzo-criteria

## Criteria 6 and 7: communication

- 6: interconvert stationary and flying qubits. 7: faithfully transmit flying qubits between locations. Quantum cryptography needs only 7 (p. 7 §IV) → divincenzo-criteria
- Flying qubits are almost always photons (polarization or spatial mode), using optical fibre; the author also suggests electrons moving in solids (p. 7) → divincenzo-criteria
- In 2000, criterion 6 was "the really hard one"; only Kimble's cavity-photon unloading/loading scheme was concrete enough to plan experiments (p. 7) → divincenzo-criteria (dated)

## Platform and outlook remarks (2000)

- No one can say which technology will win; the author thinks asking may be counterproductive (p. 7 §V) → divincenzo-criteria (dated)
- Two further approaches mentioned: quantum cellular automata (a polymer of qubits addressed globally) and Kitaev's topological quantum computing with non-abelian anyons. No known physical system was agreed to host the needed excitations in 2000 (p. 7) → divincenzo-criteria (dated)

## Not covered / level
- Requested but not in this source: numerical T1/T2 values, randomized benchmarking, SPAM terms, crosstalk, quantum volume, and any specific platform numbers. T1 vs T2 are not distinguished (only a generic "decoherence time" is used).
- Level: specialist overview, readable at university level; 2000 vintage.
