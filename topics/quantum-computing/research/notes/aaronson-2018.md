---
source: aaronson-2018
concepts: [qubit, bloch-sphere, single-qubit-gates, multi-qubit-states, entanglement, two-qubit-gates, quantum-circuits, no-cloning, universal-gate-sets, quantum-teleportation, superdense-coding, bell-inequalities]
---

Accessed: full text of Scott Aaronson's CS378 (UT Austin, Spring 2017) lecture notes, lectures 3, 4, 5, 7, 9, 10, 13, 14, 16 (extracted text; student-style scribe notes). Formulas and symbols were mostly lost in extraction, so only claims stated in the prose are recorded; numeric values given only as formulas are omitted. Locations are "Lec<n>, p. <page within lecture>". Lecture 16 is a guest lecture by Tom Wong in Aaronson's course.

## qubits-and-circuits

### qubit
- A pure quantum state is a unit vector in a complex vector space; the course sticks to discrete systems where a measurement has finitely many outcomes (Lec3, p. 1) → qubit
- A qubit is the simplest interesting quantum system: a two-level system with labels 0 and 1 and an amplitude on each. A one-state system would be trivial (Lec3, p. 1) → qubit
- Quantum mechanics gives a hybrid picture: a continuum of possible states, but each measurement has a discrete outcome. The continuum is never observed directly, only used to compute probabilities of discrete outcomes. He notes the same is true of classical probability distributions (Lec3, p. 1) → qubit
- Global phase is unobservable (multiplying the whole state by a scalar changes nothing), but relative phase is observable. His analogy: shifting the entire universe 20 feet left (Lec3, p. 4) → qubit
- Two states differing in relative phase (the |+⟩/|−⟩ pair) can be told apart by rotating by 45 degrees and then measuring in the standard basis (Lec3, p. 4) → qubit
- Hadamard maps the {0,1} basis to the {+,−} basis; the two are complementary: being maximally certain in one means being maximally uncertain in the other (Lec4, p. 1) → qubit
- Measuring in an orthonormal basis gives each outcome with probability equal to the squared projection of the state on that basis vector; the {0,1} basis in the Born rule was a special case chosen by convention (Lec4, p. 1) → qubit
- Measurement is irreversible, probabilistic and discontinuous, unlike unitary evolution, which is invertible, deterministic and continuous. Reconciling the two is the Measurement Problem (Lec4, pp. 2-3) → qubit
- Even one qubit has a richer behaviour than a classical bit. Example: a qubit can be distinguished from another only if their states are orthogonal; for non-orthogonal states the best basis for equal-prior guessing bisects the two vectors (Lec5, pp. 1-2) → qubit
- Aaronson-Drucker coin problem: deciding whether a coin is fair or biased takes about log-many bits of memory classically, but 1 qubit suffices, by rotating the qubit by a small angle per flip and measuring at the end. His remark: there is still low-hanging fruit even in the mechanics of one qubit (Lec5, p. 1) → qubit

### bloch-sphere
- The Bloch sphere is a geometric picture of all single-qubit states. The usual circle wastes half its points, since a state and its negative give the same density matrix. Redrawing so that opposite directions mean orthogonal states gives the sphere (Lec7, p. 1) → bloch-sphere
- Points on the surface are pure states; antipodal points are orthogonal states (Lec7, p. 1) → bloch-sphere
- The maximally mixed state is the origin: it is the sum of any pair of antipodal pure states (Lec7, p. 1) → bloch-sphere
- Any mixed state is a point inside the sphere. A mixture of two pure states is a point on the segment between them (Lec7, p. 1) → bloch-sphere
- Geometric argument that every mixed state of one qubit is a mixture of only two pure states: draw a line from any chosen pure state through the interior point, and the other point where it exits the surface is the second pure state (Lec7, p. 1) → bloch-sphere
- Experimentalists like the Bloch sphere because it mirrors spin-1/2 particles: you can measure spin along any axis, and the true "state" is just a point on the sphere. He calls it remarkable that the sphere's three dimensions match physical space (Lec7, pp. 1-2) → bloch-sphere
- Gates as rotations: the X, Y, Z gates are half-turns about their axes, and the square-root and eighth-root gates (such as the phase/T-type gates) are quarter- and eighth-turns (Lec7, p. 2). ⚠️ The extraction lost the symbols, so which gate names go with which turn fraction is not recoverable from this text → bloch-sphere

### single-qubit-gates
- Quantum states change by linear transformations; a transformation is unitary if it preserves the 2-norm (equivalently it preserves inner products). The rows (or columns) of a unitary form an orthonormal basis (Lec3, pp. 2-3) → single-qubit-gates
- Identity and permutation matrices are the only matrices that are both unitary and stochastic (Lec3, p. 2) → single-qubit-gates
- A real unitary is an orthogonal matrix, a product of rotations and reflections. A rotation by an angle is a basic one-qubit unitary; a phase gate maps |0⟩ to |0⟩ and |1⟩ to i|1⟩ (Lec3, pp. 2-3) → single-qubit-gates
- The NOT gate has a square root (√NOT), which needs complex numbers (or an extra dimension) to exist. That is one reason complex amplitudes matter: unitaries can then be applied continuously in time (Lec4, pp. 1-2) → single-qubit-gates
- Hadamard is ubiquitous because it converts between the {0,1} and {+,−} bases; the Hadamard on a basis can be used to measure in another basis (Lec4, p. 1) → single-qubit-gates
- Unitaries are invertible, so unitary evolution never destroys information (his example: burning a book, in principle, preserves its information in the smoke and ash) (Lec4, p. 2) → single-qubit-gates
- Interference example: applying Hadamard twice returns |0⟩ with certainty, because the two paths to |1⟩ cancel (one positive, one negative amplitude). He says anything interesting in quantum mechanics can be explained by interference (Lec3, p. 4; Lec4, p. 3) → single-qubit-gates
- He calls quantum mechanics an "island in theory space": norm-preserving theories other than the 2-norm give nothing interesting, and complex amplitudes work better than reals or quaternions (Lec4, p. 3) → single-qubit-gates

### multi-qubit-states
- Tensor products build bigger vectors from smaller ones; a gate acting on one qubit among many (e.g. "Hadamard the third qubit") means the tensor product of that gate with the identity on all other qubits (Lec3, p. 1; Lec5, p. 3) → multi-qubit-states
- A general 2-qubit state has four amplitudes (on 00, 01, 10, 11); probabilities of outcomes are the squared magnitudes (Lec5, p. 2) → multi-qubit-states
- Partial measurement rule: if you measure only the first qubit, discard the amplitudes incompatible with the outcome and renormalize the rest; the state collapses just as needed to fit the measurement and outcome. He calls it the last basic rule of quantum mechanics in the course (Lec5, p. 2) → multi-qubit-states
- There is no distance limit between qubits: one on Earth and one on the moon form a joint state; only the local qubit can be measured by each party (Lec5, p. 2) → multi-qubit-states
- An n-qubit state needs a vector of 2^n amplitudes. Simulating this classically is hard because the number of amplitudes grows exponentially (Feynman's 1982 motivation). With 300 qubits there are more amplitudes than atoms in the observable universe (Lec16, pp. 1, 3) → multi-qubit-states
- An unentangled pure n-qubit state is a tensor product of n single-qubit states, so it needs only about 2n numbers. A quantum computer whose state never had entanglement would be easy to simulate classically and give no speedup (Lec16, p. 3) → multi-qubit-states
- A classical computer can simulate an n-qubit quantum computer by storing the 2^n amplitudes and updating them for each unitary, so quantum computers do not solve anything uncomputable; they could at most falsify the Extended (not the original) Church-Turing Thesis (Lec16, p. 2) → multi-qubit-states

### entanglement
- A Bell pair (also called singlet or EPR pair) is made by Hadamard on qubit 1 then CNOT from 1 to 2, starting from |00⟩ (Lec5, p. 4) → entanglement
- For pure states, "entangled" simply means not decomposable as a tensor product; "unentangled", "separable" and "product state" are synonyms at that level. Most states are entangled (Lec5, p. 4) → entanglement
- Entanglement is forced by the basic rules and was noticed early. It worried Einstein ("spooky action at a distance"): particles must be close to become entangled, but stay entangled over any distance. It has been demonstrated experimentally over about 150 miles and, via Chinese satellite experiments, a couple of thousand miles (Lec5, p. 4) → entanglement
- Measuring the Bell pair in the standard basis only gives a correlation of two random bits, which is also classical. EPR's sharper point: Alice could measure in another basis (Hadamard first), which leaves Bob's qubit in a different pair of states, and this looks like faster-than-light signalling (Lec5, pp. 4-5) → entanglement
- Resolution hint: Bob's measurement statistics are the same whichever basis Alice measures in (equal probabilities); this leads to the density matrix description and the No-Communication Theorem, so Alice cannot send a signal (Lec5, p. 5; Lec7, p. 3; Lec14, p. 2) → entanglement
- The GHZ state is a 3-qubit analogue of the Bell pair. Unlike three classically correlated bits, whose correlation is visible to any two parties, in GHZ the entanglement is visible only with all three qubits: Alice and Bob alone see only classical correlation (Charlie could have measured unnoticed, by no-communication). Analogy: Borromean rings (Lec10, pp. 4-5) → entanglement
- Monogamy of entanglement: if Alice's qubit is maximally entangled with Bob's, it cannot also be maximally entangled with Charlie's. In the W state, neither pair is maximally entangled, though there is some entanglement between Alice-Bob and Alice-Charlie (Lec10, p. 5) → entanglement
- Two qubits need not interact directly to become entangled (an intermediary qubit, or teleportation, can do it). In practice, experiments usually create the entangled pair between Alice and Bob and send one qubit to each (Lec10, p. 4) → entanglement
- Role of entanglement in computing: one can develop the theory without mentioning it, but any interesting quantum computation has it "along for the ride" (Lec16, p. 3) → entanglement

### two-qubit-gates
- Controlled-NOT (CNOT) flips the second (target) bit if and only if the first (control) bit is 1 (Lec5, p. 3) → two-qubit-gates
- Gates built from tensor products (e.g. NOT on one bit, identity on the other) cannot make one qubit affect another; the CNOT is the example where the first qubit affects the second, and such operations are required for interaction (Lec5, p. 3) → two-qubit-gates
- Hadamard on qubit 1 followed by CNOT (control 1, target 2) starting from |00⟩ gives the Bell pair, so CNOT turns a product state into an entangled one (Lec5, p. 4) → two-qubit-gates
- CNOT is not a counterexample to no-cloning: it copies only when the control is a basis state |0⟩ or |1⟩. On a superposition it creates a Bell pair, an entangled "copy", which differs from two independent copies (Lec7, p. 4) → two-qubit-gates
- CNOT alone is classically reversible but only expresses functions that are affine mod 2 (no AND or OR); no 2-bit reversible gate is universal classically (Lec16, p. 6) → two-qubit-gates
- The set {CNOT} cannot create superposition, since it maps basis states to basis states (Lec16, p. 6) → two-qubit-gates
- {CNOT, Hadamard} can create entangled superpositions but has only real entries, so it is not universal (Lec16, pp. 6-7) → two-qubit-gates
- Every unitary on any number of qubits decomposes into 1- and 2-qubit gates (a theorem not proved in the lecture) (Lec16, p. 3) → two-qubit-gates

### quantum-circuits
- Circuit notation tracks which qubits there are and what operations act on them; example: start in |0⟩, Hadamard, Hadamard, then measure (implicitly in the {0,1} basis) (Lec4, p. 3) → quantum-circuits
- Wires are never branched into several wires, since that is not a unitary operation; to enlarge the system, add a new qubit, called an ancilla (Lec4, p. 3) → quantum-circuits
- Example circuit with control and target: start with two |0⟩, Hadamard on qubit 1, CNOT with qubit 1 as control and qubit 2 as target, giving the Bell pair (Lec5, p. 4) → quantum-circuits
- A quantum computer is, in picture, a quantum circuit on n qubits (maybe a million or more) with gates acting on 1 or 2 qubits each, followed by measurement of some or all qubits (Lec16, p. 2) → quantum-circuits
- Why gates act on few qubits: physics gives local interactions, as classical circuits use small gates (AND, OR, NOT). A giant unitary that solves 3SAT exists formally, but it has to be built from small components (Lec16, p. 2) → quantum-circuits
- Any unitary can be built with exponentially many simple gates; the real question is which can be implemented with polynomially many, taken as the "feasible" ones (Lec16, pp. 2-3) → quantum-circuits
- Quantum Zeno effect: repeated measurements in slightly rotated bases can drag a qubit from |0⟩ to |1⟩ with the failure probability (by union bound) made arbitrarily small by using more steps. Attributed to one discoverer being Alan Turing (Lec4, pp. 3-4) → quantum-circuits
- Watched pot effect: a qubit that would drift from |0⟩ to |1⟩ is kept at |0⟩ with high probability if it is measured often enough in the {0,1} basis (Lec4, p. 4) → quantum-circuits
- Elitzur-Vaidman bomb (early 1990s): with a qubit probe and repeated small rotations, you can learn whether a bomb (which measures the probe in the {0,1} basis) is present while setting it off with only tiny probability; the catch is that the object must be "quantumly interrogable" (Lec4, pp. 4-5) → quantum-circuits
- Interference is the central quantum resource: the aim is to arrange amplitudes so wrong answers cancel and the right answer reinforces; without interference one could use a classical randomized computer (Lec16, p. 3) → quantum-circuits

### no-cloning
- No-cloning theorem: a procedure that reliably copies an unknown quantum state cannot exist. He calls it easy to prove but fundamental (Lec7, p. 3) → no-cloning
- Clarification: a known procedure that prepares a state can simply be rerun; the theorem concerns a state that is given and otherwise unknown (Lec7, p. 3) → no-cloning
- Proof 1 (linearity): a cloner would map a state with a blank ancilla to two copies, which is quadratic in the amplitudes, so it is not linear and cannot be unitary (Lec7, p. 3) → no-cloning
- Proof 2 (inner products): unitaries preserve inner products, but cloning squares the inner product; this works only if the inner product is 0 or 1. So a cloner can only copy states from one orthonormal basis; for any known orthonormal basis, its vectors can be cloned (Lec7, p. 4) → no-cloning
- Motivation: if Bob could make unlimited copies, he could do state tomography to find which basis Alice measured, giving faster-than-light signalling, contradicting no-communication. So this is also an indirect proof (Lec7, p. 3) → no-cloning
- Classical analog: you cannot simulate a second independent flip of a coin of unknown bias given only the outcome of the first, since that map would not be stochastic (it is non-linear) (Lec7, p. 4) → no-cloning
- Consequences: classical information can be copied; no arbitrary copying of a physical system (science-fiction teleporting oneself) if relevant information is encoded in states outside a known orthogonal basis (Lec7, pp. 4-5). In teleportation, a consequence is that only one copy of the qubit exists (Lec10, p. 1) → no-cloning
- Quantum money (Wiesner, proposed 1969, published in the 1980s) is an application: each bill has a classical serial number and n unentangled qubits, each in one of four states (two bases); the bank keeps a database of the intended states. Verification means measuring each qubit in its proper basis. A counterfeiter guessing bases fails with exponentially small chance. Security against any counterfeiter was only proved much later, by Molina, Vidick and Watrous, after Aaronson asked on Stack Exchange (Lec7, pp. 5-6) → no-cloning
- Practical problem for Wiesner money: qubits decohere quickly (an hour at best in labs), far faster in a wallet. Money needs both unclonability and verifiability (Lec7, p. 5) → no-cloning

### universal-gate-sets
- A classical gate set is universal if it can express every Boolean function; NAND alone is. {AND, OR} is not (only monotone functions) and {NOT, XOR} is not (only affine mod 2 functions) (Lec16, p. 5) → universal-gate-sets
- A reversible gate set is universal if it can express any reversible transformation, using ancilla bits that are returned to their initial state. Toffoli (controlled-controlled-NOT) is universal and can simulate NAND. Fredkin (controlled-SWAP) can also simulate NAND but preserves Hamming weight, so it is not universal in the stronger sense. No 2-bit reversible gate is universal; at least 3 bits are needed (Lec16, pp. 5-6) → universal-gate-sets
- Any classical reversible gate is also a quantum gate, so a quantum circuit can compute anything a similarly sized classical circuit can, by using Toffoli gates (Lec16, p. 6) → universal-gate-sets
- A quantum gate set is universal if composing its gates can approximate any unitary on any number of qubits to any precision. With a finite gate set only approximation is possible, since unitaries are uncountable and circuits countable (Lec16, p. 6) → universal-gate-sets
- Four ways to fail universality: no superposition (e.g. {CNOT}); no entanglement (e.g. {Hadamard}, or any one-qubit gates); only real gates (e.g. {CNOT, Hadamard}); contained in the stabilizer set {CNOT, Hadamard, Phase}. The last is non-obvious: by the Gottesman-Knill theorem, stabilizer circuits on |0...0⟩ can be simulated classically in polynomial time (Lec16, pp. 6-7) → universal-gate-sets
- Whether there are other ways to fail is an open question, one of his favourites, though few care since many universal sets exist (Lec16, p. 7) → universal-gate-sets
- Universal examples: replacing Hadamard in the stabilizer set by almost anything else gives universality; {Toffoli, Hadamard, Phase} is universal (Yaoyun Shi, 2002); a random 2-qubit gate is universal with probability 1 (Lec16, p. 7) → universal-gate-sets
- Counting argument (Shannon, 1949, classical): there are too many n-bit Boolean functions and too few small circuits, so almost every function needs exponentially large circuits, without giving an example. The quantum version compares dimensions: even diagonal n-qubit unitaries need about 2^n parameters, while a circuit with few gates has few continuous parameters. So almost all unitaries need exponentially many gates, even approximately (Lec16, pp. 3-4) → universal-gate-sets
- Solovay-Kitaev theorem: for a universal gate set closed under inverses, any unitary can be approximated to precision epsilon with a number of gates only polylogarithmic in 1/epsilon (so a power of log(1/epsilon)), found by a reasonably fast algorithm. Whether closure under inverses is needed is open; special number-theoretic gate sets achieve the information-theoretic optimum (Lec16, p. 8) → universal-gate-sets

### quantum-teleportation
- Teleportation (1991): Alice and Bob use a pre-shared entangled pair plus classical communication to send a qubit perfectly. It does not move qubits instantaneously; that would violate causality. Cost: one ebit plus two classical bits per qubit (Lec10, p. 1) → quantum-teleportation
- Protocol: Alice has the unknown qubit and shares a Bell pair with Bob. She applies CNOT (unknown qubit as control, her half of the pair as target), Hadamards the unknown qubit, and measures both her qubits. She tells Bob the two result bits, and he applies X or Z corrections depending on them (Lec10, p. 2) → quantum-teleportation
- Before hearing from Alice, Bob's qubit is maximally mixed, in line with the No-Communication Theorem, so classical communication is necessary (Lec10, pp. 1-2) → quantum-teleportation
- Alice does not need to know the state, and her measurement is destructive, so she is left without it, in agreement with no-cloning. The Bell pair is used up (Lec10, pp. 1, 3) → quantum-teleportation
- Aaronson on "infinite information": the amplitudes could be arbitrary complex numbers, but Bob obtains only what he could measure; amplitudes act more like probabilities than like lengths. The same holds for classical coin biases that encode Shakespeare (Lec10, p. 3) → quantum-teleportation
- The teleported qubit can be half of another Bell pair, so an arbitrary n-qubit entangled state can be teleported qubit by qubit using n ebits (Lec10, pp. 3-4) → quantum-teleportation
- Entanglement swapping: Alice with two entangled qubits and two Bell pairs shared with Bob can teleport both qubits; they become entangled at Bob's end though never in causal contact. It has been used in loophole-free Bell tests, and teleportation itself has been shown in many experiments (Lec10, p. 4) → quantum-teleportation
- He notes protocols like this are hard to discover: quantum mechanics dates to 1926, teleportation to the 1990s. Sometimes trying to prove impossibility leads to a protocol (Lec10, p. 3) → quantum-teleportation

### superdense-coding
- Superdense coding is the first protocol that needs entanglement: Alice sends two classical bits to Bob by sending one qubit, provided they share entanglement beforehand (Lec9, p. 1) → superdense-coding
- Without prior entanglement, Holevo's theorem limits Alice to one classical bit per qubit (intuition: Bob can measure only once in one basis, losing the rest of the state). Not proved in the lecture (Lec9, p. 1) → superdense-coding
- Key idea: by acting on her half of a shared Bell pair, Alice can reach four mutually orthogonal states (using identity, NOT, phase flip, or both), which form a basis, so Bob can distinguish them (Lec9, p. 1) → superdense-coding
- Encoding: for two bits, she applies NOT depending on one bit and the phase gate depending on the other, then sends her qubit to Bob (Lec9, p. 1) → superdense-coding
- Decoding: Bob applies the inverse of the Bell-state preparation, CNOT (second qubit controlling the first) then Hadamard on the second qubit, and reads out the two bits in the standard basis (Lec9, p. 2) → superdense-coding
- Optimality: with any amount of shared ebits, one qubit still carries only two classical bits, no more. A factor 2 is a modest speedup, but it breaks the information-theory bound Shannon seemed to give (Lec9, p. 2) → superdense-coding
- Teleportation's resource inequality is nearly the converse of superdense coding's: one ebit + two classical bits gives one qubit (shown optimal) (Lec10, p. 1) → superdense-coding

### bell-inequalities
- Hidden variable theories try to add extra ingredients to the state so that it "merely" predicts what the universe has already fixed for the measurement result (Lec13, p. 1) → bell-inequalities
- Bohmian mechanics (Bohm, 1950s; earlier de Broglie, 1920s) keeps the wavefunction and adds real particle positions guided by a deterministic rule; there are infinitely many such rules reproducing quantum predictions, so experiments can't choose among them. With entangled particles, acting on Alice's particle changes Bob's particle's position instantaneously: non-local, though with no usable signal. Einstein disliked this (Lec13, pp. 1-3) → bell-inequalities
- Einstein wanted local hidden variables: values for all possible measurements fixed at creation, carried locally (like entangled qubits secretly agreeing in advance). Around 1963 Bell drew attention to the non-locality of Bohmian mechanics, and proved all hidden variable theories must be non-local (Lec13, p. 3) → bell-inequalities
- CHSH game (Clauser, Horne, Shimony, Holt, 1969): the referee gives uniformly random bits x and y to Alice and Bob, who are separated and return bits a and b; they win iff a + b = xy mod 2. They may agree on a strategy and share randomness beforehand (Lec13, pp. 3-4) → bell-inequalities
- Classical optimum: 75% (e.g. always output 0, losing only when x=y=1). Proof: randomized strategies are mixtures of deterministic ones (convexity), and no deterministic a(x), b(y) satisfy all four cases. Bell's inequality, in this framework, is exactly this 75% bound (Lec13, p. 4) → bell-inequalities
- With a pre-shared Bell pair and measuring in different bases chosen by x and y, they win with probability about 85% in all four input cases. Because the argument for the 75% bound holds for any local hidden variable story, winning more than 75% rules out local realism, without assuming quantum mechanics (Lec14, pp. 1-2) → bell-inequalities
- Alice can be assumed to measure first by the No-Communication Theorem. Bob's density matrix is unchanged by Alice's measurement, so there is no signalling, though conditioning on her result gives Bob a pure state, which is also true classically for conditioned predictions (Lec14, p. 2) → bell-inequalities
- Aaronson's hierarchy: classical local realism at the bottom, a faster-than-light "science-fiction utopia" at the top; quantum mechanics sits in between (no local realism, no FTL communication). A classical simulation of our universe would need FTL communication, which he calls key evidence that the world is quantum (Lec14, pp. 2-3) → bell-inequalities
- Tsirelson's inequality (1980s): about 85% is optimal even with unlimited entanglement. The full proof is not given; he shows it for strategies of the same type by bounding with unit vectors and a parallelogram inequality. Some theories beyond quantum mechanics (violating Tsirelson but with no FTL) have been studied, with e.g. one-bit communication solving scheduling (Lec14, pp. 3-4) → bell-inequalities
- Experiments: Aspect and others in the 1980s ran CHSH-type tests consistent with quantum mechanics; they did not reach 85%, but showed over 80% with high confidence. Two loopholes: detector inefficiency, and locality (communication at light speed before results are recorded). Each was closed separately by the 2000s; in 2016 several teams closed both at once (Lec14, p. 5) → bell-inequalities
- Superdeterminism is the leftover way to keep classical local realism: a cosmic conspiracy rigs measurement choices. 't Hooft supports it; Aaronson is "on board with entanglement" (Lec14, pp. 5-6) → bell-inequalities
- Other nonlocal games where entanglement wins: odd cycle game (the quantum strategy beats the classical best) and Mermin's magic square game (a quantum strategy with 2 ebits wins with probability 1, classically impossible by a parity argument) (Lec14, pp. 6-7) → bell-inequalities

## Not covered / level
- Requested concepts not covered: none. Exact Bell-test numbers (cos^2(pi/8) form) and gate matrices were lost in extraction; the Bloch-sphere gate-rotation names are uncertain (see ⚠️ above).
- Level: university intro (undergraduate/early-graduate lecture notes, informal with commentary).
