---
source: ibm-quantum-learning
concepts: [qiskit-circuits, simulators-and-statevectors, transpilation, primitives-sampler-estimator, running-on-hardware, error-mitigation, variational-algorithms, nisq-era]
---

Accessed: lesson pages (public web) of three IBM Quantum Learning courses, base https://quantum.cloud.ibm.com/learning/courses/ :
- "Variational algorithm design" (`variational-algorithm-design/`): lessons Variational algorithms, Reference states, Ansaetze and variational forms, Cost functions, Optimization loops, Instances and extensions, Examples and applications (slugs: variational-algorithms, reference-states, ansaetze-and-variational-forms, cost-functions, optimization-loops, instances-and-extensions, examples-and-applications). Qiskit 1.1.0 / qiskit-ibm-runtime 0.23.0 only printed in "Cost functions"; other lessons state no version (code is Qiskit 1.x, V2 primitives; benchmark dated 5-30-24).
- "Utility-scale quantum computing" (`utility-scale-quantum-computing/`): lessons read: Bits, gates, and circuits (`bits-gates-and-circuits`), Classical simulation (`classical-simulation`, intro only), Hardware (`hardware`), Quantum circuit optimization (`quantum-circuit-optimization`), Error mitigation (`error-mitigation`), Utility I (`utility-i`). Qiskit 2.0.2, qiskit_ibm_runtime 0.40.1, qiskit_aer 0.17.1 (stated on these lessons). Not read: Teleportation, Grover, QPE, Variational quantum algorithms, Quantum simulation, Utility II/III.
- "Quantum computing in practice" (`quantum-computing-in-practice/`): lessons read: Running quantum circuits (`running-quantum-circuits`), Utility-scale QAOA (`utility-scale-qaoa`). "Which problems are quantum computers good for?" slug guess returned 404, not read; Mapping, Simulating nature, Exam not read. Running quantum circuits mentions "Qiskit v1.0" only; Utility-scale QAOA states no version.
Page fetches were summarized by a tool, so wording is paraphrased; details are from lesson text, not verified against the original notebooks.

## qiskit-circuits
- Circuits are `QuantumCircuit` objects; a classical register (`QuantumCircuit(2, 2)`) stores measurements; gates are added as methods (`h`, `x`, `cx`), `measure(qubit, bit)` records results; `draw("mpl")` and `depth()` inspect them (Utility-scale QC, "Bits, gates, and circuits") → qiskit-circuits
- Qiskit uses little-endian ordering: qubit 0 is the rightmost bit of a bitstring (Utility-scale QC, "Bits, gates, and circuits") → qiskit-circuits
- Classical basis reference states need only X gates (e.g. |001> via X on qubit 0); entangled/superposed ones need H, CNOT, etc. (Variational algorithm design, "Reference states") → qiskit-circuits
- Composite template circuits (NLocal, TwoLocal, efficient_su2) are expanded with `decompose()` for display; parameterized gates can be bound to angles later (Variational algorithm design, "Ansaetze and variational forms") → qiskit-circuits

## simulators-and-statevectors
- `Statevector(qc)` gives the ideal output state of a circuit, useful for checking results without hardware noise (Utility-scale QC, "Bits, gates, and circuits") → simulators-and-statevectors
- The same Sampler code works on `AerSimulator` and on real hardware, default 1024 shots (Utility-scale QC, "Bits, gates, and circuits") → simulators-and-statevectors
- In the Utility I lesson, an exact AerSimulator run of a 27-qubit, 6-layer circuit is the reference; a noisy fake-device simulation is much slower, so the lesson advises against running larger circuits on fake devices (Utility-scale QC, "Utility I") → simulators-and-statevectors
- Variational lessons use `StatevectorEstimator`/statevector Sampler for noiseless local runs and compare with hardware (Variational algorithm design, "Optimization loops", "Examples and applications") → simulators-and-statevectors
- Worked example in the Primitives section: for |+> and H = 2X - Z the exact value is 2; a Sampler-based estimate gave 1.9958 and Estimator gave 2.0000, showing sampling noise (Variational algorithm design, "Cost functions") → simulators-and-statevectors
- Error mitigation options are not available on simulators (Variational algorithm design, "Cost functions") → simulators-and-statevectors
- The "Classical simulation" lesson page is only an intro (optional but highly recommended, author Y. Kawase, content on GitHub); no memory limits or tensor network claims available from it → simulators-and-statevectors

## transpilation
- Default transpiler pipeline has six stages: init, layout, routing, translation, optimization, scheduling (Utility-scale QC, "Quantum circuit optimization"; also QC in practice, "Running quantum circuits") → transpilation
- Layout maps logical to physical qubits (passes TrivialLayout, VF2Layout, SabreLayout); optimization stage loops until the circuit stops changing (Utility-scale QC, "Quantum circuit optimization") → transpilation
- Circuits must be translated to native gates; IBM 1-qubit basis is rz, sx, x and the 2-qubit gate typically ECR; CX, ECR, CZ are equivalent up to local Clifford gates; translation can lengthen circuits (Utility-scale QC, "Quantum circuit optimization") → transpilation
- Eagle basis: ecr, id, rz, sx, x; Heron basis: cz, id, rz, sx, x (Utility-scale QC, "Hardware") → transpilation
- Routing inserts SWAPs when two-qubit gates act on unconnected qubits; a star-shaped GHZ circuit on heavy-hex needs many SWAPs, while a linear-connectivity rewrite is shallower (Utility-scale QC, "Quantum circuit optimization") → transpilation
- Optimization levels 0-3: 0 does only what is needed to run, 1 is default, 2 and 3 add two-qubit block optimization; in the GHZ experiment level 2 was closer to ideal than level 0 (Utility-scale QC, "Quantum circuit optimization") → transpilation
- Higher levels are heuristic, so more effort does not always give a better circuit; `mapomatic` is mentioned for layout suggestions (QC in practice, "Running quantum circuits") → transpilation
- Cost functions lesson recommends `optimization_level=3` for most cases, uses `generate_preset_pass_manager(backend=..., optimization_level=...)`, and shows level 3 tracking the ideal curve better than level 0 in a simulated test (Variational algorithm design, "Cost functions") → transpilation
- The observable must follow the circuit's layout: `observable.apply_layout(layout=isa_circuit.layout)` (Variational algorithm design, "Cost functions") → transpilation
- Backend must be chosen before transpiling because optimization depends on the processor; transpiler does mapping, unrolling to ISA, routing (QC in practice, "Utility-scale QAOA") → transpilation

## primitives-sampler-estimator
- Primitives are building blocks; two main ones: Sampler (runs shots, estimates bitstring probabilities) and Estimator (expectation values of observables decomposed into terms with known eigenbases); they also handle much suppression/mitigation (QC in practice, "Running quantum circuits") → primitives-sampler-estimator
- Sampler returns computational-basis probabilities; efficient only for sparse distributions, shots grow quickly for dense ones (Variational algorithm design, "Cost functions") → primitives-sampler-estimator
- Estimator decomposes the observable into Paulis; efficient only if nonzero Pauli terms grow at most polynomially with qubits (Variational algorithm design, "Cost functions") → primitives-sampler-estimator
- Sampler workflow: transpile with preset pass manager, run `Sampler` (qiskit_ibm_runtime), read counts via `result[0].data.c.get_counts()`; job retrievable by ID (Utility-scale QC, "Bits, gates, and circuits") → primitives-sampler-estimator
- Estimator is used for cost functions/VQE; Sampler for overlaps in VQD (compute-uncompute) and for sampling bitstrings in QAOA max-cut (Variational algorithm design, "Instances and extensions", "Examples and applications") → primitives-sampler-estimator
- Lessons use V2 primitives (SamplerV2, EstimatorV2, EstimatorOptions) (Variational algorithm design, "Instances and extensions"; Utility-scale QC, "Utility I") → primitives-sampler-estimator

## running-on-hardware
- Qiskit patterns: Map, Optimize, Execute, Post-process (QC in practice, "Running quantum circuits"; Utility-scale QC, "Bits, gates, and circuits", "Utility I"; Variational algorithm design, "Examples and applications") → running-on-hardware
- Patterns framework is described as a conceptual framework with modular tooling for each step (QC in practice, "Running quantum circuits") → running-on-hardware
- Backend = interface to a device; its Target models the ISA, properties and constraints; `service.least_busy(...)` or `service.backend(...)` pick devices (Utility-scale QC, "Hardware") → running-on-hardware
- IBM processors are superconducting transmon qubits in a heavy-hex lattice; fleet processors are above 100 qubits; metrics include QuOps, circuits per second, EPLG, CLOPS (QC in practice, "Running quantum circuits") → running-on-hardware
- Eagle example device: median T1 ~285 us, T2 ~173 us, median SX error ~2.3e-4, ECR error ~6.9e-3; readout errors generally exceed two-qubit errors, which exceed one-qubit errors (Utility-scale QC, "Hardware") → running-on-hardware
- Circuit depth matters because gates take time and decoherence limits feasible depth (QC in practice, "Running quantum circuits") → running-on-hardware
- Sessions let a variational loop iterate without requeueing at each parameter update; Open Plan users cannot use sessions; too many submissions can raise error 1217 (Variational algorithm design, "Cost functions") → running-on-hardware
- Hardware VQE example: least-busy backend, Session, 10,000 shots; result several percent off the simulator (Variational algorithm design, "Instances and extensions") → running-on-hardware
- Batches are not discussed in the pages read (sessions also absent from QC in practice, "Running quantum circuits") → running-on-hardware
- Sources of error in a 5-node QAOA example: approximate algorithm with few layers, finite sampling, readout error; more shots reduce sampling error (QC in practice, "Utility-scale QAOA") → running-on-hardware
- Noisy hardware gives nondeterministic cost evaluations that can stop optimizer convergence (Variational algorithm design, "Cost functions") → running-on-hardware

## error-mitigation
- Distinction: error suppression changes circuits at compile time (dynamical decoupling, Pauli twirling); mitigation models noise and corrects results, costing extra quantum and classical overhead (QC in practice, "Running quantum circuits") → error-mitigation
- Resilience levels: 0 none, 1 T-REx (twirled readout error extinction), 2 ZNE (noise amplification then extrapolation) (QC in practice, "Running quantum circuits"; Utility-scale QC, "Error mitigation") → error-mitigation
- PEC must be enabled manually and its cost grows exponentially with gate count, so may not suit large circuits; PEA described as not yet available (QC in practice, "Running quantum circuits") → error-mitigation
- The Utility-scale "Error mitigation" lesson does not mention PEC and makes no efficacy/trade-off claims; it shows option settings: `dynamical_decoupling.enable` (sequence "XX"), `twirling.enable_gates`, `twirling.enable_measure`, `zne.noise_factors=[1,3,5]`, extrapolators exponential/linear, via `estimator.options.resilience_level` (Utility-scale QC, "Error mitigation") → error-mitigation
- T-REx: Pauli twirling with randomized X flips before measurement against readout noise, sampling overhead 2; ZNE overhead equals number of noise factors (Variational algorithm design, "Cost functions") → error-mitigation
- Mitigation lowers bias but raises variance; compensate with more shots (`options.executions.shots`); adds time overhead (Variational algorithm design, "Cost functions") → error-mitigation
- Dynamical decoupling is applied to idle qubits as part of suppression (Variational algorithm design, "Cost functions") → error-mitigation

## variational-algorithms
- Variational algorithms are hybrid quantum-classical, built from cost function, ansatz and optimizer; workflow: reference state, ansatz U_A = U_V(theta) U_R, evaluate cost on QPU, classical optimizer updates parameters, iterate (Variational algorithm design, "Variational algorithms") → variational-algorithms
- Variational theorem: any normalized state has expected energy at least the ground-state energy, so minimizing over parametrized states approximates the ground state (Variational algorithm design, "Variational algorithms") → variational-algorithms
- Reference state: fixed starting state, default |0...0>, can be a good guess to speed convergence (Variational algorithm design, "Reference states") → variational-algorithms
- Heuristic ansatz trade-offs: speed (smaller search space), accuracy (may exclude solution), noise (deeper circuits suffer more) (Variational algorithm design, "Ansaetze and variational forms") → variational-algorithms
- Hardware-efficient/heuristic ansaetze: NLocal/TwoLocal (rotation + entanglement layers), `efficient_su2` (SU(2) layers + CX) (Variational algorithm design, "Ansaetze and variational forms") → variational-algorithms
- Problem-specific ansaetze restrict the search space using problem knowledge (e.g. `QAOAAnsatz` for max-cut; zz_feature_map + TwoLocal for QML) (Variational algorithm design, "Ansaetze and variational forms") → variational-algorithms
- ⚠️ the lesson's stated parameter bound (fewer than 2^(2n)) looks inconsistent with Hilbert space dimension 2^n; flagged by the fetch summary, check original (Variational algorithm design, "Ansaetze and variational forms") → variational-algorithms
- Cost function is problem-specific; QPU acts as a black-box oracle; max-cut maps to an Ising-type Z observable plus offset (Variational algorithm design, "Cost functions") → variational-algorithms
- Local optimizers converge fast but depend on the start and get trapped in local minima; global optimizers explore more but are slower; bootstrapping (global then local, or prior solution as start) helps (Variational algorithm design, "Optimization loops") → variational-algorithms
- Gradient-based methods (e.g. BFGS) follow the negative gradient and reach local minima; gradient-free (e.g. COBYLA) suit hard/noisy gradients, more robust, need more evaluations in high dimensions; toy example evaluations: SLSQP 112, BFGS 144, COBYLA 137 (Variational algorithm design, "Optimization loops") → variational-algorithms
- Barren plateaus: gradients shrink exponentially with qubit count; suggested mitigations: bootstrapping, hardware-efficient ansatz, error suppression/mitigation, gradient-free optimizers; active research area (Variational algorithm design, "Optimization loops") → variational-algorithms
- SPSA is not mentioned in "Optimization loops" (Variational algorithm design) → variational-algorithms
- VQE: reference + ansatz + Hamiltonian expectation, COBYLA updates; observable 2II-2XX+3YY-3ZZ gives about -6.00 on simulator (Variational algorithm design, "Instances and extensions") → variational-algorithms
- SSVQE finds k lowest eigenvalues with k orthogonal reference states and decreasing weights; VQD finds excited states by overlap penalties with beta greater than eigenvalue gaps; QSR fits a Fourier-series cost classically to cut QPU calls (Variational algorithm design, "Instances and extensions") → variational-algorithms
- Examples: custom VQE reached about -6.0 (error 2.7e-8); H2 ground state about -1.857 Ha on simulator and about -1.83 on hardware; variational result cannot go below the true ground state (Variational algorithm design, "Examples and applications") → variational-algorithms
- QAOA max-cut: 4-node, 5-edge graph, `QAOAAnsatz` with 2 reps, COBYLA; most frequent sampled bitstring gives the partition (Variational algorithm design, "Examples and applications") → variational-algorithms
- Utility-scale QAOA: 125-node max-cut challenge, one qubit per node; QAOA is approximate, more layers improve quality at greater cost (QC in practice, "Utility-scale QAOA") → variational-algorithms
- "Instances and extensions" page does not cover QAOA itself; QAOA appears in "Examples and applications" and QC in practice (Variational algorithm design) → variational-algorithms

## nisq-era
- Variational algorithms are framed as able to use the utility of today's non-fault-tolerant computers (term "NISQ" not used on that page) (Variational algorithm design, "Variational algorithms") → nisq-era
- In this course "utility" is used informally: experiments beyond exact statevector simulation that still give usable results on noisy hardware; such circuits are "utility-scale"; quantum advantage is framed as a longer-term goal (Utility-scale QC, "Utility I") → nisq-era
- The utility experiment: time dynamics of the 2D transverse-field Ising model, first-order Trotter, 127 qubits, 60 layers (20 steps), observable <Z62>; ZNE with probabilistic error amplification (PEA) reduces errors; RZZ(-pi/2) needs one CX; heavy-hex ZZ layers use 3 edge colors (Utility-scale QC, "Utility I") → nisq-era
- Limits: noise strongly distorts results (27-qubit demo); the lesson does not attempt the full 127-qubit mitigated run since PEA is experimental and slow; results depend on device state (Utility-scale QC, "Utility I") → nisq-era
- Circuit depth limited by decoherence; mitigation costs grow (PEC exponential in gates) (QC in practice, "Running quantum circuits") → nisq-era

## Not covered / level
- Not found: SPSA, batches, PEC details beyond one sentence, statevector memory limits, expressibility by name, "NISQ" as a term, a lesson on "Which problems are quantum computers good for?" (404 on guessed slug). Qiskit version varies by lesson (1.1.0 / 2.0.2 / unstated); Variational algorithm design lessons are older (2024).
- Level: intro to university-level practical course material.
