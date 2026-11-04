---
source: watrous-2025
concepts: [complex-numbers, vectors-and-dirac-notation, inner-products-and-norms, matrices-and-linear-maps, unitary-and-hermitian-matrices, tensor-products, probability-basics, born-rule-measurement, density-matrices, decoherence, unitary-time-evolution, qubit, bloch-sphere, single-qubit-gates, multi-qubit-states, entanglement, two-qubit-gates, quantum-circuits, no-cloning, universal-gate-sets, quantum-teleportation, superdense-coding, bell-inequalities, query-model-and-oracles, phase-kickback, deutsch-jozsa, bernstein-vazirani-and-simon, quantum-fourier-transform, phase-estimation, shor-algorithm, grover-search, quantum-complexity, post-quantum-cryptography]
---

Accessed: full text of arXiv:2507.11536v1 (extracted text), read Lessons 1, 2 and 3.2-3.3 (Unit I). Locations are given as "L<lesson>.<section>, PDF p. N". PDF page = book page + 6. Unit I does not contain a stand-alone linear-algebra review or appendix.

## math-foundations

### complex-numbers
- A quantum state vector is defined by two properties: its entries are complex numbers (not necessarily nonnegative reals), and the sum of the squared absolute values of the entries is 1. The source says all differences between quantum and classical information come from this change (L1.2, PDF p. 18) → complex-numbers
- Complex entries can have imaginary parts, as in (1+2i)/3 |0> - (2/3)|1>. The source checks it is a valid state with |1+2i|^2/9 + 4/9 = 5/9 + 4/9 = 1 (L1.2, PDF pp. 19-20) → complex-numbers
- Measurement probability is the absolute value squared of the amplitude (Born rule), so a negative or complex entry changes no standard-basis probabilities. |+> and |-> give identical 1/2, 1/2 outcomes (L1.2, PDF pp. 23-24) → complex-numbers
- The sign changes and, more generally, the phases (also called arguments) of the complex entries can significantly change a state. Applying H and measuring distinguishes |+> from |-> with certainty (L1.2, PDF p. 27) → complex-numbers
- The bra of a vector uses the complex conjugate of each entry in addition to the transpose, e.g. the bra of (1+2i)/3 |0> - (2/3)|1> is (1-2i)/3 <0| - (2/3) <1| (L1.2, PDF pp. 20-21) → complex-numbers, vectors-and-dirac-notation
- Global phase: if |phi> = alpha|psi> with |alpha| = 1 (alpha = e^{i theta}), the two states give the same measurement probabilities and stay equal up to the same factor under any unitary, so they are treated as the same state. Example: |-> and -|-> (L3.3, PDF pp. 91-92) → complex-numbers
- Relative phase (a sign or phase on only some entries) is not a global phase and does matter: |+> and |-> are not equivalent (L3.3, PDF p. 92) → complex-numbers
- The phase operation P_theta = diag(1, e^{i theta}) is unitary. S = P_{pi/2} = diag(1, i), T = P_{pi/4}, Z = P_pi (L1.2, PDF p. 26) → complex-numbers, unitary-and-hermitian-matrices
- ⚠️ Limited coverage: the source does not review complex-number arithmetic (polar form, conjugate rules). It uses conjugate, modulus and phase as known tools. Anything more would need another source.

### vectors-and-dirac-notation
- A system's classical states form a finite nonempty set Sigma (bit {0,1}, die, DNA bases...). Vector indices are labelled by Sigma, so the vector order is a choice, usually a default one (L1.1, PDF pp. 10-11) → vectors-and-dirac-notation
- A probabilistic or quantum state is a column vector. The ket |a> is the standard basis vector with a 1 at position a and 0 elsewhere. Every column vector is a linear combination of standard basis vectors, e.g. (3/4, 1/4) = 3/4|0> + 1/4|1> (L1.1, PDF p. 12) → vectors-and-dirac-notation
- The bra <a| is the row vector with a 1 at position a. The product <a|b> is 1 if a = b and 0 otherwise. A bra next to a ket gives a "bracket" (notation due to Dirac) (L1.1, PDF pp. 15-16) → vectors-and-dirac-notation
- For any ket |psi>, <a|psi> is the entry of |psi> at index a, and <psi| is the conjugate transpose of |psi> (L1.2, PDF p. 20) → vectors-and-dirac-notation
- Any label can be put inside a ket (|psi>, |+>, |-> ...). |+> = (|0>+|1>)/sqrt2 and |-> = (|0>-|1>)/sqrt2. "Superposition" and "linear combination" are essentially synonyms for quantum states (L1.2, PDF p. 20) → vectors-and-dirac-notation
- Dirac notation lets you write large or partly unspecified vectors compactly (e.g. the uniform superposition 1/sqrt|Sigma| times the sum of |a>), and removes the need to fix an ordering of the classical states. The source says it will mostly stop using column vectors except for small examples (L1.2, PDF pp. 21-22) → vectors-and-dirac-notation
- Dirac notation is not always the best choice: a 6x6 unitary with 20 nonzero entries is clearer as a matrix than as 20 terms (L2.2, PDF p. 63) → vectors-and-dirac-notation
- A qubit is a system with classical state set {0,1}. A qutrit has {0,1,2}. A qudit has {0,...,d-1} (L1.2 PDF p. 19; L2.2 PDF p. 54) → vectors-and-dirac-notation
- A basis is not only the standard one. The Bell basis of 4 states is a basis, so any complex 4-vector is a linear combination of the four Bell states. Example: |00> = (|phi+> + |phi->)/sqrt2 (L2.2, PDF p. 53) → vectors-and-dirac-notation

### inner-products-and-norms
- The Euclidean norm of a column vector is the square root of the sum of |alpha_k|^2. Quantum state vectors are exactly the unit vectors under this norm (L1.2, PDF pp. 18-19) → inner-products-and-norms
- The inner product <psi|phi> is the bra times the ket, i.e. the sum over a of conj(alpha_a)*beta_a (conjugation on the first vector). It is "critically important" in quantum information (L3.2, PDF p. 80) → inner-products-and-norms
- Norm and inner product: <psi|psi> = ||psi||^2, so ||psi|| = sqrt(<psi|psi>). The inner product is positive definite: <psi|psi> >= 0 and equals 0 only for the zero vector (L3.2, PDF p. 81) → inner-products-and-norms
- Inner product properties: conjugate symmetry <psi|phi> = conj(<phi|psi>), linear in the second argument and conjugate-linear in the first, and the Cauchy-Schwarz inequality |<psi|phi>| <= ||psi|| ||phi|| (L3.2, PDF pp. 81-82) → inner-products-and-norms
- Two vectors are orthogonal if <psi|phi> = 0 (geometrically, at right angles). An orthogonal set has every pair orthogonal. An orthonormal set is also made of unit vectors, i.e. <psi_j|psi_k> = 1 if j = k and 0 otherwise (L3.2, PDF p. 82) → inner-products-and-norms
- An orthonormal basis is an orthonormal set that is also a basis, equivalently an orthonormal set whose size equals the dimension of the space. Examples: standard basis vectors, {|+>,|->} for one qubit, the Bell basis for two qubits (L3.2, PDF p. 83) → inner-products-and-norms
- Orthonormal sets are always linearly independent, so m <= n. Any orthonormal set can be extended to an orthonormal basis, for instance with the Gram-Schmidt process (L3.2, PDF p. 83) → inner-products-and-norms
- The norm is multiplicative under tensor products: ||phi (x) psi|| = ||phi|| ||psi||. So a tensor product of unit vectors is a unit vector (L2.2, PDF p. 51) → inner-products-and-norms, tensor-products
- Inner products give the following limit: two non-orthogonal states (<phi|psi> != 0) cannot be perfectly discriminated. Perfectly discriminable states must be orthogonal (L3.3, PDF p. 95; the proof continues beyond the part read) → inner-products-and-norms

### matrices-and-linear-maps
- Operations on states are linear maps. Operations on probability vectors are matrices (matrix-vector multiplication), and composition is a matrix product: apply M1 first, then M2, gives M2 M1 (a later one multiplies on the left) (L1.1, PDF p. 17) → matrices-and-linear-maps
- Matrix multiplication is associative but not commutative. The source's example is M2 M1 != M1 M2 for the reset and NOT matrices, so the order of operations matters (L1.1, PDF pp. 17-18) → matrices-and-linear-maps
- The outer product |b><a| is a column times a row. It is a matrix with a single 1 at (row b, column a). Example: |0><1| = [[0,1],[0,0]] (L1.1, PDF p. 15) → matrices-and-linear-maps
- Any deterministic function f is the matrix sum over a of |f(a)><a|. It satisfies M|a> = |f(a)> and has exactly one 1 in each column. This works because <a|b> is 1 or 0, so in general a matrix is a sum of terms |c><d| (L1.1, PDF pp. 14-16) → matrices-and-linear-maps
- The entry of a matrix is <a|M|b>. For tensor products, the source defines M (x) N through <ac|M (x) N|bd> = <a|M|b><c|N|d> (L2.1, PDF p. 47) → matrices-and-linear-maps, tensor-products
- A linear map can be applied through linearity on the standard basis (e.g. T|+> computed from T|0> and T|1>) without writing the matrix. The source says the two ways are equivalent (L1.2, PDF pp. 27-28) → matrices-and-linear-maps
- The conjugate transpose satisfies (A B)† = B† A†. This is used to show that |psi><psi| is Hermitian (L3.2, PDF p. 86) → matrices-and-linear-maps
- Dirac notation also gives other matrices easily, e.g. the "increment mod 8" operation is the sum over k of |(k+1) mod 8><k|. Its conjugate transpose is the sum over k of |k><(k+1) mod 8|, the inverse operation (L2.1, PDF pp. 45-46; L2.2, PDF pp. 63-64) → matrices-and-linear-maps
- The source shows block matrices. An example is M = sum_k |k><0| (x) Pi_k, a block matrix with the Pi_k stacked in the first block column (L3.2, PDF p. 89) → matrices-and-linear-maps

### unitary-and-hermitian-matrices
- Quantum operations on state vectors are unitary matrices, not stochastic ones. A square complex matrix U is unitary if U U† = I and U† U = I, which for square matrices are equivalent, and U† = U^{-1}. For non-square M, M†M = I does not imply M M† = I (L1.2, PDF pp. 24-25) → unitary-and-hermitian-matrices
- U is unitary iff it preserves the Euclidean norm of every vector, ||U|psi>|| = ||psi||. So unitaries are exactly the linear maps that take quantum state vectors to quantum state vectors, analogous to stochastic matrices for probability vectors (L1.2, PDF p. 25) → unitary-and-hermitian-matrices
- Examples of qubit unitaries: the Paulis I, X (bit flip, NOT), Y, Z (phase flip, Z|1> = -|1>), the Hadamard H = [[1,1],[1,-1]]/sqrt2, and the phase operations P_theta, including S and T. The source verifies H† H = I by hand (L1.2, PDF pp. 25-26) → unitary-and-hermitian-matrices
- Action of H: H|0> = |+>, H|1> = |->, H|+> = |0>, H|-> = |1>. Phase differences between |+> and |-> become distinguishable by H (L1.2, PDF p. 27) → unitary-and-hermitian-matrices
- Compositions are matrix products. R = H S H has R^2 = X (NOT), so R is a "square root of NOT". The source notes that this is not possible with a classical single-bit operation (L1.2, PDF pp. 28-29) → unitary-and-hermitian-matrices
- A permutation matrix (one 1 in every row and column) is always unitary. A matrix that is both stochastic and unitary is exactly a permutation matrix. Examples: the 3-state addition mod 3, the NOT operation. Unitary and deterministic operations are called reversible (L1.2, PDF p. 29; L2.2, PDF pp. 63-64) → unitary-and-hermitian-matrices
- The 4x4 quantum Fourier transform matrix (1/2)[[1,1,1,1],[1,i,-1,-i],[1,-1,1,-1],[1,-i,-1,i]] is given as a unitary example. The source says it plays a key role in quantum algorithms (L1.2, PDF p. 29) → unitary-and-hermitian-matrices
- Three equivalent statements for a square U: U is unitary, its columns form an orthonormal basis, its rows form an orthonormal basis. The proof looks at U†U as the matrix of inner products of the columns (L3.2, PDF pp. 83-85) → unitary-and-hermitian-matrices, inner-products-and-norms
- Consequence: any orthonormal set of m vectors in dimension n can be made the first m columns of some unitary matrix (L3.2, PDF p. 85) → unitary-and-hermitian-matrices
- A Hermitian matrix equals its own conjugate transpose. A projection is a matrix that is Hermitian and idempotent (Pi^2 = Pi). |psi><psi| with ||psi|| = 1 is a projection, and so is any sum of |psi_k><psi_k| over an orthonormal set (L3.2, PDF pp. 85-86) → unitary-and-hermitian-matrices
- A projective measurement is a set of projections summing to I. Outcome a has probability ||Pi_a|psi>||^2, and the new state is Pi_a|psi> / ||Pi_a|psi>||. Standard-basis measurement is the case Pi_a = |a><a| (L3.2, PDF p. 87) → unitary-and-hermitian-matrices
- A unitary acting on a joint system with an ancilla can implement any projective measurement. Idea: build M = sum_k |k><0| (x) Pi_k, whose first n columns are orthonormal, and complete it to a unitary U (L3.2, PDF pp. 88-91) → unitary-and-hermitian-matrices
- No-cloning: no unitary U and fixed state |phi> satisfy U(|psi>|phi>) = |psi>|psi> for all |psi>. The proof is that the map is not linear in |psi> (L3.3, PDF pp. 93-94) → unitary-and-hermitian-matrices
- ⚠️ Eigenvalues/eigenvectors and spectral decomposition are not treated in the parts read. The source only touches the idea of Hermitian projections as sums of |psi_k><psi_k|. Not used for the eigenvalue concept.

### tensor-products
- The classical states of a joint system (X, Y) are the Cartesian product Sigma x Gamma, and for n systems the n-tuples. A joint probabilistic or quantum state is then a vector indexed by that product (L2.1, PDF pp. 32-34) → tensor-products
- Ordering convention: Cartesian products are ordered alphabetically (lexicographically), with the leftmost symbol most significant. For example {0,1}x{0,1} is 00, 01, 10, 11, and the vector entries follow this order (L2.1, PDF p. 35) → tensor-products
- Qiskit labels qubits (X_{n-1},...,X_0), with the highest index on the left. In circuit diagrams the top qubit is q_0 and sits in the rightmost position of the tuple. The source calls this a reversal of a more common convention and a frequent source of confusion (L2.1, PDF p. 33; L3.1, PDF p. 74) → tensor-products
- Tensor product of vectors: |phi> (x) |psi> = sum over (a,b) of alpha_a beta_b |ab>, i.e. <ab|pi> = <a|phi><b|psi>. As columns, (alpha_1..alpha_m) (x) (beta_1..beta_k) lists alpha_1 times the whole beta, then alpha_2 times beta, and so on (L2.1, PDF pp. 37-38) → tensor-products
- Notation: |phi>|psi> and |phi (x) psi> mean |phi> (x) |psi>. For basis kets |a> (x) |b> = |ab>. The tensor product is bilinear and scalars can move freely, alpha|phi> (x) |psi> = |phi> (x) alpha|psi> (L2.1, PDF pp. 38-39) → tensor-products
- The tensor product is not commutative: |phi> (x) |pi> is in general a different vector from |pi> (x) |phi>. Subscripting kets with system names (|a>_4 |b>_2 ...) lets you reorder them for calculation without changing the state (L2.2, PDF p. 60) → tensor-products
- A product state of several systems is an (n-fold) tensor product of the individual state vectors. The n-fold product is multilinear and can be defined recursively (L2.1, PDF pp. 39-40) → tensor-products
- A tensor product of quantum state vectors is a quantum state vector, since norms multiply. The product state means "the states have nothing to do with one another" (L2.2, PDF p. 51) → tensor-products
- Entangled states: a state vector that is not a product state is entangled. For two qubits, (|00>+|11>)/sqrt2 is not a product, shown by a contradiction in the entries <0|phi><1|psi> = 0 vs <0|phi><0|psi> != 0. The value 1/sqrt2 does not matter, only that it is nonzero, so (3/5)|00> + (4/5)|11> is also entangled (L2.2, PDF p. 52) → tensor-products
- For quantum state vectors, entanglement is equivalent to being not a product state. The source says this is not so simple for noisy states described by density matrices (L2.2, PDF p. 52) → tensor-products
- A product state example: (|00> + i|01> - |10> - i|11>)/2 = ((|0>-|1>)/sqrt2) (x) ((|0>+i|1>)/sqrt2). All four Bell states, the GHZ state (|000>+|111>)/sqrt2 and the W state are not product states (L2.2, PDF pp. 53-54) → tensor-products
- Tensor product of matrices: M (x) N = sum alpha_ab beta_cd |ac><bd|. It is the unique matrix with (M (x) N)(|phi> (x) |psi>) = (M|phi>) (x) (N|psi>). In block form, each entry alpha_ij of M is replaced by alpha_ij N (L2.1, PDF p. 47) → tensor-products
- The matrix tensor product is multiplicative: (M1 (x) ... (x) Mn)(N1 (x) ... (x) Nn) = (M1 N1) (x) ... (x) (Mn Nn). Also (M (x) N)† = M† (x) N† (L2.1, PDF p. 48; L2.2, PDF p. 64) → tensor-products
- Independent operations on separate systems are the tensor product of the matrices, for stochastic matrices and for unitaries. A tensor product of unitaries is unitary, proved from (A (x) B)† = A† (x) B† and the multiplicativity above (L2.1, PDF p. 48; L2.2, PDF pp. 64-65) → tensor-products, unitary-and-hermitian-matrices
- "Do nothing" on a subsystem is the identity on it. A gate on one qubit of two is U (x) I or I (x) U. For example H (x) I is a 4x4 matrix with H's entries placed in the block pattern given in the source (L2.2, PDF pp. 65-66) → tensor-products
- Not all operations are tensor products. SWAP and controlled-NOT cannot be written as a tensor product of unitaries (L2.2, PDF p. 66) → tensor-products
- Useful joint operations in Dirac form: SWAP = sum over c,d of |c><d| (x) |d><c|. Controlled-U = |0><0| (x) I + |1><1| (x) U (CNOT is U = X). Toffoli = (|00><00| + |01><01| + |10><10|) (x) I + |11><11| (x) X (L2.2, PDF pp. 66-68) → tensor-products
- With control X and target Y the CNOT matrix is [[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]]. With the roles exchanged (control = second system), the matrix changes, so the order of the systems matters (L2.1, PDF pp. 44-45) → tensor-products
- Measuring part of a joint state: write |psi> = sum_a |a> (x) |phi_a>, the outcome a has probability ||phi_a||^2, and the state becomes |a> (x) |phi_a>/||phi_a||. This divides by the norm, like the probabilistic case divides by the sum of the entries (L2.2, PDF pp. 55-57) → tensor-products, inner-products-and-norms
- A quantum state vector has no analogue of the reduced (marginal) state of a single subsystem in this formulation. The source says the density matrices of Lesson 9 fix this (L2.2, PDF pp. 58-59) → tensor-products

### probability-basics
- A probabilistic state of a system represents knowledge or belief about its classical state. It is a probability vector: entries are nonnegative reals that sum to 1. For a bit, Pr(0) = 3/4 and Pr(1) = 1/4 is (3/4, 1/4) (L1.1, PDF pp. 11-12) → probability-basics
- Measuring a probabilistic state shows one classical state a, and the description updates to |a>. The source says this changes our knowledge, not the system. Different observers can legitimately have different vectors (L1.1, PDF pp. 12-13) → probability-basics
- A deterministic operation is a function f: Sigma -> Sigma, represented by a matrix with exactly one 1 in each column. Examples are the constant functions, the identity and NOT (L1.1, PDF p. 14) → probability-basics
- A probabilistic operation is a stochastic matrix: nonnegative entries and every column sums to 1 (each column is a probability vector). These are exactly the matrices that always map probability vectors to probability vectors (L1.1, PDF pp. 16-17) → probability-basics
- A probabilistic operation can be seen as a random choice among deterministic ones. Example: [[1,1/2],[0,1/2]] = 1/2 identity + 1/2 constant-0 (L1.1, PDF p. 17) → probability-basics
- Composition of probabilistic operations M1 then M2 is M2 M1, which is again stochastic. The order matters (L1.1, PDF pp. 17-18) → probability-basics
- Joint states: a probabilistic state of (X, Y) assigns a probability to each pair (a, b). Example: 1/2|00> + 1/2|11> has correlated (always equal) random bits (L2.1, PDF pp. 34-35) → probability-basics
- Independence: Pr((X,Y)=(a,b)) = Pr(X=a) Pr(Y=b) for all a, b. Equivalently the joint vector is a tensor product of probability vectors (a product state). Example: (1/6, 1/12, 1/2, 1/4) = (1/4, 3/4) (x) (2/3, 1/3) (L2.1, PDF pp. 35-37) → probability-basics, tensor-products
- Correlation is defined as lack of independence. 1/2|00> + 1/2|11> is not a product, by an argument on zero entries (L2.1, PDF pp. 36-37) → probability-basics
- Marginal (reduced) state: Pr(X=a) = the sum over b of Pr((X,Y)=(a,b)). The source argues this is required, because otherwise measuring Y would change X's statistics, allowing faster-than-light signalling (L2.1, PDF p. 41) → probability-basics
- Conditional probability and update after measuring X = a: Pr(Y=b | X=a) = Pr((a,b))/Pr(X=a). In vector terms, take the part of the joint vector for a and normalize it by the sum of its entries. The worked example gives Pr(X=0) = 7/12 and Y|X=0 = 6/7|1> + 1/7|3> (L2.1, PDF pp. 41-43) → probability-basics
- Joint operations: any operation on (X, Y) is a stochastic matrix indexed by Sigma x Gamma. Independent operations M on X and N on Y combine as M (x) N, and a tensor product of stochastic matrices is stochastic (L2.1, PDF pp. 44-49) → probability-basics, tensor-products
- The "no-cloning" argument works for probabilistic states too: cloning an unknown probabilistic state is non-linear, so no stochastic matrix does it (L3.3, PDF pp. 94-95) → probability-basics
- Quantum measurement in the standard basis gives outcome a with probability |<a|psi>|^2 (Born rule). It is consistent because these probabilities sum to 1 for a unit vector. The quantum analogue of the marginal is the sum over b of |alpha_ab|^2 (L1.2, PDF p. 23; L2.2, PDF pp. 55-56) → probability-basics

## Not covered
- eigenvalues-and-eigenvectors: no eigenvalue or spectral decomposition material in the parts read (L1, L2, L3.2, L3.3); it is probably in a later unit (e.g. density matrices, Lesson 9). Not checked.
- Complex-number arithmetic basics (polar form, conjugate properties): not reviewed, only used.

## Level
University (advanced undergraduate / intro graduate). Linear algebra is introduced as needed from a classical-probability analogy, so it is accessible to a programmer with some rusty linear algebra.

## quantum-mechanics

Accessed (this section): full text of Unit III, Lessons 9-12 (density matrices, channels, general measurements, purifications and fidelity), read in the extracted text (not all proofs; Lesson 10.3 and parts of 11.1/11.3 skimmed). Locations: "L<lesson>.<section>, PDF p. N" (PDF page = book page + 6). Measurement facts from Unit I reuse the locations already given above.

### born-rule-measurement
- Standard-basis measurement of a state vector gives outcome a with probability |<a|psi>|^2, which sums to 1 for a unit vector (L1.2, PDF pp. 23-24, as already noted above) → born-rule-measurement
- Projective measurement: a family of projection matrices Pi_a with sum equal to the identity. Outcome a has probability ||Pi_a|psi>||^2. The post-measurement state is Pi_a|psi> renormalized. Standard-basis measurement is the case Pi_a = |a><a| (L3.2, PDF p. 87; restated in L11.1, PDF pp. 328-329) → born-rule-measurement
- For a state given as a density matrix rho, the probability of outcome a of a projective measurement is Tr(Pi_a rho). For a pure state this equals ||Pi_a|psi>||^2, and by linearity it equals the average of the probabilities over any convex mixture of pure states (L11.1, PDF p. 329) → born-rule-measurement
- General measurement (POVM in the usual name; the source does not use that name in the parts read): replace the projections by arbitrary positive semidefinite matrices P_0..P_{m-1} that sum to the identity. Outcome a has probability Tr(P_a rho). These probabilities are nonnegative and sum to 1 (L11.1, PDF p. 330) → born-rule-measurement
- Every projective measurement is a general measurement. The standard-basis measurement of a qubit is P_0 = |0><0|, P_1 = |1><1|, and its probabilities are the diagonal entries <0|rho|0> and <1|rho|1> (L11.1, PDF p. 330) → born-rule-measurement
- Non-projective examples: a two-outcome qubit measurement with non-projection matrices (outcome probabilities 5/6 and 1/6 on |+>), and the four-outcome "tetrahedral" measurement P_a = |phi_a><phi_a|/2 built from four states at the vertices of a regular tetrahedron on the Bloch sphere (L11.1, PDF pp. 331-333) → born-rule-measurement
- Naimark's theorem: any general measurement can be implemented by adding an ancilla Y in |0>, applying a unitary U to (Y, X), and then measuring Y in the standard basis. The proof builds U with the square roots of the P_a as its first block column (L11.2, PDF pp. 341-343) → born-rule-measurement
- Destructive measurement outputs only the outcome. Non-destructive measurement also gives the post-measurement state, which is sqrt(P_a) rho sqrt(P_a) / Tr(P_a rho) when taken from the Naimark construction. This state is not unique, because a unitary V_a after outcome a gives other valid choices with the same outcome probabilities. Equivalently, Kraus matrices A_a with sum A_a† A_a = I give outcome probability Tr(A_a rho A_a†) and post-state A_a rho A_a† / that probability (L11.2, PDF pp. 344-346) → born-rule-measurement
- Measurements can be described as channels whose output is always diagonal (classical). Such a channel is the completely dephasing channel on the outcome register composed with the measurement, and the two descriptions (matrices, classical-output channels) are equivalent (L11.1, PDF pp. 327-329) → born-rule-measurement, decoherence

### observables
- ⚠️ Not covered: The parts of the book read describe measurements only through projections and positive semidefinite matrices summing to I, with no stand-alone Hermitian "observable" or expectation-value formalism. The nearest link is that projections are Hermitian (L3.2, PDF pp. 85-86, see above). The one eigen-based measurement in the parts read is state discrimination, where the optimal projective measurement uses the spectral decomposition of the weighted difference p rho_0 - (1-p) rho_1 (L11.3, PDF p. 348).

### density-matrices
- A quantum state of a system is a density matrix rho: a square matrix indexed by the classical states with two conditions, trace 1 and positive semidefinite (rho >= 0). The source calls this the "general formulation", which can describe noise and the state of an isolated part of a system (L9 intro, PDF pp. 261-262; L9.1, PDF p. 263) → density-matrices
- Positive semidefinite means P = M†M for some M. It is equivalent to P being Hermitian with nonnegative eigenvalues, and to <psi|P|psi> >= 0 for all |psi>. It does not mean that the entries are nonnegative (L9.1, PDF pp. 263-264) → density-matrices
- Informal reading of entries: the diagonal entries are the standard-basis measurement probabilities. The off-diagonal entries tell how much the two classical states are in superposition, with their relative phase (L9.1, PDF p. 265) → density-matrices
- A state vector |psi> corresponds to the density matrix |psi><psi|, called a pure state. It is a rank-1 projection, with one eigenvalue 1 and the rest 0, so it carries no uncertainty. Not every density matrix is pure (L9.1, PDF pp. 265-267) → density-matrices
- Density matrices remove the global-phase ambiguity: |psi> and e^{i theta}|psi> give the same matrix. In general two states give the same statistics for every measurement iff their density matrices are equal (a "faithful" representation) (L9.1, PDF pp. 267-268) → density-matrices
- A random choice of states is the convex combination sum p_k rho_k. Averaging state vectors does not work (the result may not be a unit vector, and (|psi> + (-|psi>))/2 is zero). Example: (|0><0| + |+><+|)/2 = [[3/4,1/4],[1/4,1/4]] (L9.2, PDF pp. 268-269) → density-matrices
- The same density matrix arises from different ensembles. The completely mixed state I/2 comes from {|0>,|1>}, from {|+>,|->}, or from any two orthogonal states. The two preparations cannot be told apart by any measurement, as shown with Parseval's identity (L9.2, PDF pp. 269-271) → density-matrices
- Spectral theorem: every density matrix is a convex combination of orthonormal pure states, weighted by its eigenvalues (which are nonnegative and sum to 1 because the trace is 1). Other, non-orthogonal decompositions also exist. Example: [[3/4,1/4],[1/4,1/4]] has eigenvalues cos^2(pi/8) and sin^2(pi/8) (L9.2, PDF pp. 272-274) → density-matrices
- Classical probabilistic states are exactly the diagonal density matrices, sum p_a |a><a|. With no off-diagonal terms there is only classical randomness and no superposition (L9.2, PDF pp. 271-272) → density-matrices
- Bloch sphere (qubits only): up to global phase a pure qubit state is cos(theta/2)|0> + e^{i phi} sin(theta/2)|1>, and its density matrix is (I + x sigma_x + y sigma_y + z sigma_z)/2 with (x, y, z) a unit vector. |0>, |1> are the poles, |+>, |-> the x axis, |+i>, |-i> the y axis (L9.3, PDF pp. 275-279) → density-matrices
- Bloch ball: convex combinations of points give points inside the sphere, which are the mixed states. The completely mixed state I/2 is the center, (0,0,0). Orthogonal states are antipodal points (L9.3, PDF pp. 280-281) → density-matrices
- Multiple systems: tensor products of density matrices are product states (independence). Correlated classical states, classical-quantum states, and separable states sum p_k rho_k (x) sigma_k are the non-entangled cases. A state that is not separable is entangled. The Bell states as density matrices keep off-diagonal terms linking |00> and |11> (L9.4, PDF pp. 282-284) → density-matrices
- Reduced state and partial trace: discarding system B leaves rho_A = Tr_B(rho). It is characterized by Tr_B(M (x) N) = Tr(N) M. For the e-bit |phi+> the reduced state of each qubit is the completely mixed state I/2, which is the only description consistent with no faster-than-light signalling (L9.4, PDF pp. 285-289) → density-matrices
- For a pure entangled pair the local state is mixed. A pure state of the whole can have a mixed reduced state, as all four Bell states give I/2 on each qubit (L9.4, PDF p. 286; L12.1, PDF p. 364) → density-matrices
- Purification: for any density matrix rho of X there is a pure state of (X, Y) with Tr_Y = rho, if Y has at least as many classical states as X (rank(rho) states suffice). One example is sum sqrt(p_a)|phi_a>|a>. Two purifications of the same rho differ by a unitary on Y alone (L12.1, PDF pp. 356-363) → density-matrices

### decoherence
- A channel is a linear map from density matrices to density matrices that must stay valid when applied to part of a larger system (trace-preserving and completely positive). The source says any physically realizable discrete-time change of state is described by a channel, including unitary gates and noise. Matrix transposition is a linear map that is not a channel (L10 intro, PDF p. 293; L10.1, PDF pp. 295-296) → decoherence
- Completely dephasing channel Delta: it zeros the off-diagonal entries and keeps the diagonal. The source calls it an extreme form of decoherence, which essentially ruins superpositions and turns them into classical probabilistic states. It is also equivalent to a standard-basis measurement whose result is discarded or kept (L10.1, PDF pp. 300-301) → decoherence
- Partial dephasing: Delta_eps = (1-eps) Id + eps Delta multiplies the off-diagonal entries by (1-eps) and leaves the diagonal alone (L10.1, PDF pp. 301-302) → decoherence
- Dephasing applied to one half of an e-bit turns |phi+><phi+| into (|00><00| + |11><11|)/2, a classically correlated state with the entanglement removed (L10.1, PDF p. 301) → decoherence
- Completely depolarizing channel Omega(rho) = Tr(rho) I/2 outputs the completely mixed state. The variant (1-eps) rho + eps Omega(rho) is the less extreme version. The qubit reset channel Tr(rho)|0><0| is another non-unitary example (L10.1, PDF pp. 299-302) → decoherence
- Stinespring representation: any channel can be implemented as adding an initialized workspace, applying a unitary to the combined system, and tracing out (discarding) part of it. Phrased physically, noise comes from the system interacting with an environment that is then ignored (L10.2, PDF pp. 303-305) → decoherence, unitary-time-evolution
- Dephasing by an environment: a CNOT from the input qubit to a |0> workspace copies the classical state, and discarding the copy collapses the input to a classical mixture, which is complete dephasing. The source gives an explicit matrix calculation (L10.2, PDF pp. 305-307) → decoherence
- Dephasing is also a mixed-unitary (Pauli) channel: apply the identity or sigma_z with probability 1/2 each, i.e. rho/2 + sigma_z rho sigma_z/2. The same holds for the depolarizing channel, which is the Pauli average of I, X, Y, Z (L10.2, PDF pp. 309, 312-313) → decoherence
- Kraus representation: Phi(rho) = sum A_k rho A_k† with the condition sum A_k† A_k = I (equivalent to trace preservation, while complete positivity is automatic). At most n*m Kraus matrices are needed for an n-input, m-output channel (L10.2, PDF p. 310) → decoherence
- Kraus matrices for common channels: dephasing has A_0 = |0><0|, A_1 = |1><1| (or I/sqrt2 and sigma_z/sqrt2). Reset has |0><0| and |0><1|. Depolarizing needs at least four Kraus matrices, e.g. I, X, Y, Z each divided by 2 (L10.2, PDF pp. 311-313) → decoherence
- Kraus and Stinespring forms are not unique. The Choi matrix J(Phi) = sum |a><b| (x) Phi(|a><b|) identifies a channel uniquely, and it is Phi applied to half of a maximally entangled state (times n) (L10.2, PDF pp. 313-315) → decoherence
- ⚠️ Not covered: amplitude damping is not in the parts read (only reset, dephasing and depolarizing examples were found). No decay-time T1/T2 language was seen.

### unitary-time-evolution
- In the simplified formulation, operations on state vectors are unitary matrices, which are exactly the norm-preserving linear maps (L1.2, PDF p. 25, as noted above) → unitary-time-evolution
- A unitary operation acts on density matrices as conjugation, Phi(rho) = U rho U†. This agrees with U|psi> being mapped to U|psi><psi|U†, and by linearity it extends to all rho (L10.1, PDF pp. 297-298) → unitary-time-evolution
- Conjugation by a unitary is a valid channel, also when applied to one part of a joint system. Positive semidefiniteness is preserved because U rho U† = K†K, and the trace is preserved by the cyclic property (L10.1, PDF p. 298) → unitary-time-evolution
- The identity channel (U = I) is the perfect noiseless channel or ideal memory (L10.1, PDF p. 298) → unitary-time-evolution
- A unitary channel is a Kraus representation with a single Kraus matrix A_0 = U, and the Kraus condition reduces to U†U = I (L10.2, PDF p. 313) → unitary-time-evolution
- Unitary operations are the building block of every channel: channels = add ancilla, unitary, trace out. Noisy evolution is therefore a unitary on system plus environment, seen from the system alone (L10.2, PDF pp. 303-305, 326) → unitary-time-evolution
- Mixed unitary channels sum p_k U_k rho U_k† are random choices among unitaries, and Pauli channels use only Pauli matrices. They are generally not unitary channels (L10.1, PDF p. 299) → unitary-time-evolution
- ⚠️ The source treats unitary evolution as discrete gates (time steps), not as a Schrodinger-equation or Hamiltonian evolution in the parts read. The word "time evolution" and the Hamiltonian were not found there.

### extra for math-foundations
- Schmidt decomposition of a pure state of (X, Y): |psi> = sum over a of sqrt(p_a) |x_a>|y_a>, with positive p_a summing to 1 and both sets orthonormal. The Schmidt coefficients are unique. It is built from an eigenbasis of the reduced state (L12.1, PDF pp. 358-362) → tensor-products
- The number r of terms equals the rank of the reduced state. The nonzero eigenvalues of both reduced states equal the squared Schmidt coefficients, so both subsystems have the same randomness for a pure global state (L12.1, PDF pp. 361-362) → tensor-products
- ⚠️ The source does not state the rank criterion (Schmidt rank 1 iff product state) in the parts read. It follows from the above (a product state has a pure reduced state), but that conclusion is not written in the source.
- Entanglement for mixed states: states that are not separable (sum p_k rho_k (x) sigma_k) are entangled. For pure states this agrees with "not a product state", but the source says entanglement is more complicated for non-pure states (L9.4, PDF p. 284) → tensor-products
- Fidelity between two pure states is |<phi|psi>|, between 0 (orthogonal) and 1 (equal up to global phase). The general definition for density matrices is F(rho, sigma) = Tr sqrt( sqrt(rho) sigma sqrt(rho) ), and the source warns that some authors define fidelity as the square of this (L12.2, PDF pp. 368-369) → inner-products-and-norms
- Fidelity is symmetric. With one pure argument F = sqrt(<phi|sigma|phi>), and with both pure F = |<phi|psi>|. F = the trace norm of sqrt(sigma) sqrt(rho) (L12.2, PDF pp. 369-370) → inner-products-and-norms
- Properties listed without proof: 0 <= F <= 1, F = 1 iff rho = sigma, F = 0 iff the images are orthogonal, F is multiplicative on product states, and F never decreases under a channel (L12.2, PDF p. 371) → inner-products-and-norms
- Uhlmann's theorem: F(rho, sigma) is the maximum of |<phi|psi>| over purifications of rho and of sigma (Y at least as large as X). It uses the unitary equivalence of purifications (L12.2, PDF pp. 374-376) → inner-products-and-norms

## Not covered (quantum-mechanics section)
- observables: the book has no Hermitian-observable formalism in the parts read (see the placeholder above).
- amplitude damping: not found. T1/T2 time language: not found.
- Hamiltonians and continuous time evolution: not found (gate-based time steps only).
- Trace distance, state discrimination, tomography and the gentle-measurement lemma exist in L11.3 and L12.2 (PDF pp. 347-348, 371-374) but were only skimmed and are not turned into claims.

## Level (quantum-mechanics section)
University (advanced undergraduate / intro graduate), written for quantum computing. Proofs are included, and this part assumes comfort with the spectral theorem, partial trace and block matrices.

## qubits-and-circuits

Accessed (this section): full text of Unit I Lessons 3.1 and 4 (circuits, no-cloning, teleportation, superdense coding, CHSH game), Lesson 1.2 and 2.2 passages on qubits, gates and Bell states, Bloch sphere in L9.3, and the universal-gate-set passage in L6.2/L6.3. Locations as "L<lesson>.<section>, PDF p. N". Claims already in math-foundations are only referenced.

### qubit
- A qubit state is a unit vector alpha|0> + beta|1> with |alpha|^2 + |beta|^2 = 1. Examples: |0>, |1>, and the plus state (|0>+|1>)/sqrt2, whose standard-basis outcomes are 0 and 1 with probability 1/2 each (L1.2, PDF pp. 19-23) → qubit
- The minus state (|0>-|1>)/sqrt2 gives the same standard-basis measurement statistics as plus, yet is a different state. The two behave differently under operations: H then measurement separates them with certainty (L1.2, PDF pp. 23-24, 27) → qubit
- The states |+i> = (|0>+i|1>)/sqrt2 and |-i> = (|0>-i|1>)/sqrt2 form another basis. They sit on the +y and -y axes of the Bloch sphere (L9.3, PDF p. 279) → qubit
- Measuring |0> gives 0 with certainty and |1> gives 1 with certainty, which links these states to the classical states of a bit (L1.2, PDF p. 24) → qubit
- Every qubit state is equivalent up to global phase to one with a nonnegative real coefficient on |0> (L9.3, PDF p. 275) → qubit
- Orthonormal bases of a qubit: {|0>,|1>} (standard) and {|+>,|->}. See math-foundations bullets on orthonormal bases (L3.2, PDF p. 83) → qubit
- The real-amplitude qubit states |psi_theta> = cos(theta)|0> + sin(theta)|1> give |0>, |1>, |+>, |-> for theta = 0, pi/2, pi/4, -pi/4. The inner product of two of them is cos(difference of angles) (L4.3, PDF pp. 111, 118) → qubit
- A qubit is a system with classical states {0,1}. See math-foundations bullet on qubit/qutrit/qudit (L1.2, PDF p. 19) → qubit

### bloch-sphere
- The Bloch sphere represents qubit states only. The analogous picture is no longer a sphere for three or more classical states (L9.3, PDF p. 275) → bloch-sphere
- Up to global phase a pure qubit state is cos(theta/2)|0> + e^{i phi}sin(theta/2)|1>, with theta in [0, pi] and phi in [0, 2pi). Theta and phi are unique unless the state is |0> or |1>, where phi is irrelevant (L9.3, PDF pp. 275-276) → bloch-sphere
- The density matrix of that state equals (I + sin(theta)cos(phi) X + sin(theta)sin(phi) Y + cos(theta) Z)/2. The coefficients form a unit vector, i.e. a point on the unit 2-sphere with polar angle theta and azimuth phi (L9.3, PDF pp. 276-277) → bloch-sphere
- Six states: |0> at the north pole (0,0,1), |1> at the south pole, |+> and |-> at +x and -x, |+i> and |-i> at +y and -y. Orthogonal states are antipodal (L9.3, PDF pp. 278-279, 281) → bloch-sphere
- Real-amplitude states |psi_alpha> = cos(alpha)|0> + sin(alpha)|1> lie in the x-z plane at Bloch vector (sin 2alpha, 0, cos 2alpha), so the Bloch angle is twice the Hilbert-space angle (L9.3, PDF p. 280) → bloch-sphere
- The Bloch ball includes the interior. Points inside are mixed states from convex combinations, and the center is the completely mixed state I/2 (L9.3, PDF pp. 280-281) → bloch-sphere
- The CHSH measurement matrix U_theta (a real rotation) is written as R_y(-2 theta), where R_y(t) has entries cos(t/2), sin(t/2). This is the only link to gates as rotations in the parts read (L4.3, PDF p. 119) → bloch-sphere
- ⚠️ The source does not describe single-qubit gates (X, H, S, T) as Bloch-sphere rotations in the parts read. Only the R_y remark above was found. Another source is needed for "gates as rotations".

### single-qubit-gates
- Pauli matrices I, X = sigma_x, Y = sigma_y, Z = sigma_z. X is the bit flip or NOT (X|0> = |1>), Z the phase flip (Z|0> = |0>, Z|1> = -|1>) (L1.2, PDF pp. 25-26) → single-qubit-gates
- Hadamard H = [[1,1],[1,-1]]/sqrt2 with H|0> = |+>, H|1> = |->, H|+> = |0>, H|-> = |1> (L1.2, PDF pp. 26-27) → single-qubit-gates
- Phase operation P_theta = diag(1, e^{i theta}), with S = P_{pi/2}, T = P_{pi/4}, Z = P_pi, I = P_0. All are unitary (L1.2, PDF p. 26) → single-qubit-gates
- Example computation: T|+> = (|0> + (1+i)/sqrt2 |1>)/sqrt2, obtained by linearity from T|0> = |0> and T|1> = (1+i)/sqrt2 |1> (L1.2, PDF pp. 27-28) → single-qubit-gates
- The circuit T H S H applied to |0> gives ((1+i)/2)|0> + (1/sqrt2)|1> (L3.1, PDF p. 73) → single-qubit-gates
- H S H squared equals X, so H S H is a square root of NOT, which has no classical single-bit analogue (L1.2, PDF pp. 28-29) → single-qubit-gates
- In circuit diagrams, X, Y, Z, H, S, T are drawn as labelled boxes and X is sometimes drawn as a circle with a plus (L3.1, PDF p. 78) → single-qubit-gates
- Rotation-type gates U_theta = cos/sin matrix are used in the CHSH strategy (L4.3, PDF p. 119) → single-qubit-gates

### multi-qubit-states
- The classical states of n systems are n-tuples, so n bits give 2^n classical states. 10 bits give 1024 states written as strings 0000000000 to 1111111111 (L2.1, PDF pp. 32-33) → multi-qubit-states
- Qiskit orders qubits (q_{n-1}, ..., q_0), q_0 at the top of a circuit and rightmost in the tuple. See math-foundations bullet on the Qiskit ordering (L3.1, PDF p. 74) → multi-qubit-states
- A state of n systems is a unit vector indexed by the Cartesian product of the classical states, and measuring all of them gives string a_{n-1}...a_0 with probability |<a_{n-1}...a_0|psi>|^2 (L2.2, PDF p. 55) → multi-qubit-states
- Product states are tensor products of the individual state vectors. See math-foundations bullets on product states and the non-product example (L2.2, PDF pp. 51-53) → multi-qubit-states
- Examples of three-qubit states: GHZ = (|000>+|111>)/sqrt2 and W = (|001>+|010>+|100>)/sqrt3. Neither is a product of three qubit states (L2.2, PDF p. 54) → multi-qubit-states
- A one-qubit gate acting inside a larger circuit is the identity on the other qubits, e.g. I (x) H when the gate acts on the top qubit (L3.1, PDF p. 75) → multi-qubit-states
- Measuring only one qubit of a joint state: outcome a has probability equal to the squared norm of the part of the vector attached to |a>, and the rest collapses to the normalized part. See math-foundations bullet on partial measurement (L2.2, PDF pp. 55-57) → multi-qubit-states

### entanglement
- The four Bell states are |phi+> = (|00>+|11>)/sqrt2, |phi-> = (|00>-|11>)/sqrt2, |psi+> = (|01>+|10>)/sqrt2, |psi-> = (|01>-|10>)/sqrt2. All are entangled and they form the orthonormal Bell basis (L2.2, PDF p. 53; L3.1, PDF p. 76) → entanglement
- Entanglement is defined as non-classical quantum correlation, essentially a definition by what it is not. The source admits this is unsatisfying and that entanglement is hard to explain intuitively (L4, PDF p. 100) → entanglement
- The classical state (1/2)|00> + (1/2)|11> (two perfectly correlated random bits) is not entangled. Remarks like "measuring one qubit affects the other" or "each has a memory of the other" are also true of this classical state, so they do not capture entanglement (L4, PDF pp. 100-101) → entanglement
- What distinguishes entanglement is what can be done with it that no classical correlation allows. The three examples of Lesson 4 (teleportation, superdense coding, CHSH game) are of this kind (L4, PDF p. 101) → entanglement
- Entanglement is treated as a resource. The state |phi+> counts as one e-bit even though it uses two qubits. "Sharing an e-bit" means Alice has qubit A, Bob has qubit B and (A,B) is in |phi+> (L4, PDF p. 101) → entanglement
- The classical analogue of the e-bit resource is one bit of shared randomness, the state (1/2)|00> + (1/2)|11>, which is useful for cryptography but is not entangled (L4, PDF p. 101) → entanglement
- Circuit H on the upper qubit followed by CNOT creates |phi+> from |00>. The full unitary maps |00>, |01>, |10>, |11> to |phi+>, |phi->, |psi+>, -|psi->, i.e. converts the standard basis into the Bell basis (L3.1, PDF pp. 74-76) → entanglement
- For quantum state vectors, not a product state is equivalent to entangled. See math-foundations bullets on entangled states (L2.2, PDF p. 52) → entanglement
- Reduced state of each qubit of a Bell pair is the completely mixed state. See density-matrices bullets (L9.4, PDF p. 286) → entanglement

### two-qubit-gates
- Controlled-NOT: acts on standard basis states as |a>|b> -> |a>|a XOR b>, with the first qubit the control and the second the target. Drawn as a filled circle joined to a circle with a plus (L3.1, PDF pp. 70, 72) → two-qubit-gates
- The CNOT matrix is [[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]] when the control is the second (top) qubit under Qiskit ordering, so which qubit is control changes the matrix (L3.1, PDF p. 75) → two-qubit-gates
- Controlled gates have a filled-circle control joined to the controlled operation: controlled-NOT, Toffoli (controlled-controlled-NOT), controlled-swap (Fredkin), and controlled versions of any unitary U (L3.1, PDF pp. 72-73) → two-qubit-gates
- Controlled-Z is like CNOT but applies Z to the target. A controlled-Z at the start of the Bell-state circuit, or a swap at the end, removes the -1 phase on the last output state (L3.1, PDF p. 76) → two-qubit-gates
- Toffoli maps |a>|b>|c> to |a>|b>|c XOR (a AND b)> and is a query gate for AND. It can be built from H, T, T-dagger and CNOT gates (L6.3, PDF pp. 177-178) → two-qubit-gates
- A SWAP can be built from three CNOT gates (L6.3, PDF pp. 180-181) → two-qubit-gates
- CNOT copies standard basis states: with a target in |0>, |a>|0> becomes |a>|a>. It does not copy |+> (L3.3, PDF pp. 94-95) → two-qubit-gates
- Matrix and Dirac forms of SWAP, controlled-U and Toffoli, and the fact that CNOT and SWAP are not tensor products of single-qubit gates, are in math-foundations (see the tensor-products bullets, L2.2, PDF pp. 66-68) → two-qubit-gates
- A CNOT from the input qubit to a |0> workspace and discarding the copy gives complete dephasing (see decoherence bullets, L10.2, PDF pp. 305-307) → two-qubit-gates

### quantum-circuits
- A circuit is an acyclic network of wires and gates, with no feedback loops. Information flows left to right and gates are evaluated in that order (L3.1, PDF pp. 69-70) → quantum-circuits
- In a quantum circuit the wires are qubits and the gates are unitary operations or standard-basis measurements. In the one-qubit example H, S, H, T from left to right, the whole circuit is the composition T H S H (L3.1, PDF p. 73) → quantum-circuits
- Inputs and outputs can be written on the wires (e.g. |0> in and ((1+i)/2)|0> + (1/sqrt2)|1> out). Circuits often begin with all qubits in |0> but may start in other states (L3.1, PDF p. 73) → quantum-circuits
- Reading order of qubits: the top wire is q_0 and the rightmost entry of the tuple (Qiskit convention). The source says this is a reversal of a more common convention and applies it throughout (L3.1, PDF p. 74) → quantum-circuits
- A gate on a single qubit acts as the identity on all other qubits, so its two-qubit matrix is a tensor product with I (L3.1, PDF p. 75) → quantum-circuits
- The unitary of a whole circuit is the product of the gate matrices in order (a later gate multiplies on the left). The Bell-state circuit is the product of the CNOT matrix and I (x) H (L3.1, PDF pp. 75-76) → quantum-circuits
- Classical bit wires are drawn as double lines. A measurement gate writes the standard-basis outcome onto a classical bit and leaves the qubit in |0> or |1>. A compact form shows measurement as taking a qubit to a classical bit, with the measured qubit discarded (L3.1, PDF pp. 76-77) → quantum-circuits
- Gates with classical controls are applied or not depending on the classical bit. This is used by Bob in teleportation (L4.1, PDF p. 98) → quantum-circuits
- Circuits can be reversed: replace each gate by its inverse and reverse the order, giving the circuit for U-dagger. Toffoli, CNOT and NOT are their own inverses (L6.3, PDF p. 181) → quantum-circuits
- Deferred measurement: a mid-circuit measurement can be postponed to the end by adding a workspace qubit and a CNOT, so a computation is a unitary part followed by a read-out (L6.2, PDF pp. 171-172) → quantum-circuits
- Circuit size is the number of gates. Circuit depth is the minimum number of layers where gates in a layer act on different wires (L6.2, PDF pp. 172-173) → quantum-circuits
- Workspace qubits initialized to |0> are common in circuits (L3.3, PDF p. 96) → quantum-circuits
- Quantum circuits can simulate any Boolean circuit using NOT, CNOT and Toffoli gates plus workspace. Garbage qubits are removed by running the circuit in reverse, because garbage would ruin the interference that quantum algorithms need (L6.3, PDF pp. 177-181) → quantum-circuits

### no-cloning
- Theorem: no unitary U and fixed state |phi> satisfy U(|psi>|phi>) = |psi>|psi> for all quantum states |psi>. See math-foundations bullet on no-cloning for the linearity argument (L3.3, PDF pp. 93-94) → no-cloning
- The sketch of the proof: if U cloned |a>, |b> and hence (|a>+|b>)/sqrt2, linearity would give (|aa>+|bb>)/sqrt2, but a true clone is (|aa>+|ab>+|ba>+|bb>)/2, a different vector (L3.3, PDF p. 94) → no-cloning
- The theorem is absolute, about perfect cloning. It says nothing against approximate cloning with limited accuracy, which exists and has its own bounds (L3.3, PDF p. 94) → no-cloning
- It concerns an arbitrary unknown state. A standard basis state is easy to copy with a CNOT onto |0>, but that circuit fails on |+> (L3.3, PDF pp. 94-95) → no-cloning
- It is not specific to quantum information. An unknown probabilistic state cannot be cloned either, because cloning is non-linear and so no stochastic matrix does it. The example is a random number between 1 and 10 (L3.3, PDF pp. 94-95) → no-cloning
- Consequence: quantum information cannot be sent by classical communication alone. If it could, a second receiver copying the classical message would get a copy of the qubit (L4.1, PDF p. 97) → no-cloning
- Teleportation does not clone: the original qubit Q ends in |b> after Alice's measurement and the e-bit is used up (L4.1, PDF p. 98) → no-cloning
- Related limit: non-orthogonal states cannot be perfectly discriminated (see inner-products-and-norms bullet, L3.3, PDF pp. 95-98) → no-cloning

### universal-gate-sets
- The default gate set adopted for quantum circuits: single-qubit gates X, Y, Z, H, S, S-dagger, T, T-dagger; controlled-NOT; single-qubit standard-basis measurements (L6.2, PDF p. 170) → universal-gate-sets
- Alternative common choice: Toffoli, Hadamard and S as elementary gates, plus measurement. Allowing all single-qubit gates is often done but gives an unrealistically powerful model if accuracy is ignored (L6.2, PDF p. 170) → universal-gate-sets
- The unitary gates of the default set form a universal gate set: any unitary on any number of qubits can be approximated to any accuracy by circuits from these gates alone (L6.2, PDF p. 170) → universal-gate-sets
- The definition of universality puts no limit on the number of gates needed. A measure-based argument shows that most unitaries must have extremely high cost (L6.2, PDF p. 170) → universal-gate-sets
- The proof of universality of quantum gate sets is not simple and is not given in the course (L6.2, PDF p. 170) → universal-gate-sets
- Arbitrary multi-qubit unitaries are treated as non-elementary because assigning unit cost to a gate on millions of qubits gives no realistic cost measure (L6.2, PDF p. 170) → universal-gate-sets
- AND, OR, NOT and FANOUT form a universal set for deterministic Boolean computation, so any function of fixed input and output length can be built from them (L6.2, PDF p. 171) → universal-gate-sets
- Toffoli can be built from H, T, T-dagger and CNOT, and with NOT it implements AND, OR, with CNOT FANOUT, so these gates can simulate any Boolean circuit (L6.3, PDF pp. 177-179) → universal-gate-sets
- ⚠️ The Solovay-Kitaev theorem and the explicit universality proof are not in the parts read. Approximation cost is only mentioned qualitatively.

### quantum-teleportation
- Goal: Alice sends the state of a qubit Q to Bob using a shared e-bit and two classical bits. Matter is not moved, only quantum information (L4.1, PDF p. 102) → quantum-teleportation
- Set-up: Alice holds A and Bob holds B with (A,B) in |phi+>. The state of Q is unknown to both and may be entangled with other systems. Alice cannot send qubits directly, only classical bits (L4.1, PDF p. 102) → quantum-teleportation
- Protocol: Alice applies CNOT (Q control, A target) then H on Q, measures A (outcome a) and Q (outcome b) in the standard basis and sends a and b to Bob. Bob applies X if a = 1 and Z if b = 1, so the possible corrections are I, Z, X, ZX (L4.1, PDF p. 104) → quantum-teleportation
- Analysis for Q = alpha|0> + beta|1>: after CNOT and H the joint state can be regrouped so that each of the four outcomes ab (each probability 1/4) leaves B in alpha|0> + beta|1> up to the X or Z fix. The apparent dependence on alpha and beta before communication is only algebra (L4.1, PDF pp. 105-107) → quantum-teleportation
- Alice's measurement result is uniformly random whatever alpha, beta are, so it reveals nothing about the state. This is essential, because extracting information from an unknown state generally disturbs it (L4.1, PDF p. 107) → quantum-teleportation
- Why no faster-than-light signalling: Bob's qubit is only correct after he receives the classical bits a and b. Before that his qubit does not depend on alpha and beta, and the outcomes are random (L4.1, PDF pp. 106-107, derived from the source's remark that nothing magical has happened) → quantum-teleportation
- General case: if Q is entangled with another system R, the protocol leaves (B,R) in the state that (Q,R) had. The source argues this follows because the protocol acts as the identity channel on one qubit (L4.1, PDF pp. 108-110) → quantum-teleportation
- Costs: the e-bit is used up (A ends in |a>, unentangled), Q ends in |b>, so there is no cloning. Classical communication alone cannot send qubits, so the e-bit is needed (L4.1, PDF pp. 97-98) → quantum-teleportation
- Teleportation is a protocol for quantum communication and not an application in itself. Related ideas: entanglement distillation and gate teleportation (L4.1, PDF p. 110) → quantum-teleportation

### superdense-coding
- Goal: Alice sends two classical bits c, d to Bob by sending one qubit, using a shared e-bit (L4.2, PDF pp. 110-111) → superdense-coding
- It is described as the complement of teleportation: teleportation sends one qubit with two classical bits plus one e-bit, superdense coding sends two classical bits with one qubit plus one e-bit (L4.2, PDF p. 110) → superdense-coding
- Alice's encoding: apply Z if d = 1, then X if c = 1, to her qubit A, and send A to Bob (L4.2, PDF p. 111) → superdense-coding
- Bob's decoding: CNOT with A as control and B as target, then H on A, then standard-basis measurement of B (gives c) and of A (gives d) (L4.2, PDF p. 111) → superdense-coding
- Analysis: Alice's gates map |phi+> to |phi+>, |phi->, |psi+>, |psi-> for cd = 00, 01, 10, 11 (I, Z, X, XZ). Bob's operations map these four Bell states to |00>, |01>, |10>, -|11>, so measurement reveals cd (the global -1 is irrelevant) (L4.2, PDF pp. 112-113) → superdense-coding
- Interpretation: Alice picks one of four Bell states and Bob measures to find which one (L4.2, PDF p. 112) → superdense-coding
- Holevo's theorem implies that without shared entanglement one qubit cannot carry more than one classical bit. Entanglement thus doubles the classical capacity of a qubit (L4.2, PDF p. 111) → superdense-coding
- The source says trading one qubit for two bits at the cost of an e-bit seems hardly worth it in practice, but the protocol is a clear use of entanglement (L4.2, PDF p. 111) → superdense-coding

### bell-inequalities
- Nonlocal game: a referee asks Alice and Bob classical questions x, y chosen with known probabilities, they answer a, b without communicating, and win or lose by a fixed rule. They can prepare a strategy beforehand. No communication may be modelled by distance and the speed of light (L4.3, PDF pp. 113-114) → bell-inequalities
- CHSH game: x, y, a, b are bits, questions chosen uniformly (probability 1/4 each), and they win iff a XOR b = x AND y. So answers must agree except for (x,y) = (1,1), where they must differ (L4.3, PDF pp. 115-116) → bell-inequalities
- Classical deterministic strategies cannot win every time: winning on (0,0), (0,1), (1,0) forces a(0)=b(0)=a(1)=b(1)... and so a loss on (1,1). There are 16 deterministic strategies and the best wins 3 of 4 cases, e.g. always answer 0 (L4.3, PDF p. 116) → bell-inequalities
- Classical bound is 3/4. Shared randomness and probabilistic strategies do not help because they are random choices among deterministic strategies and an average is never above the maximum (L4.3, PDF p. 117) → bell-inequalities
- Quantum strategy: Alice and Bob share |phi+>. Alice applies U_0 if x = 0 and U_{pi/4} if x = 1, Bob applies U_{pi/8} if y = 0 and U_{-pi/8} if y = 1, each then measures in the standard basis and answers with the outcome. U_theta is a rotation by angle -theta mapping |psi_theta> to |0> (L4.3, PDF pp. 113-114, 119-120) → bell-inequalities
- Key formula: for angles alpha (Alice) and beta (Bob), the answers agree with probability cos^2(alpha - beta) and differ with probability sin^2(alpha - beta). For (0,0), (0,1), (1,0) the angle difference is pi/8, so winning has probability cos^2(pi/8). For (1,1) the difference is 3pi/8 and winning needs a differing answer, sin^2(3pi/8) = cos^2(pi/8) (L4.3, PDF pp. 120-122, 126-128) → bell-inequalities
- Winning probability is (2 + sqrt2)/4 = cos^2(pi/8), about 0.85, in every question case. This is clearly above the classical 3/4 (L4.3, PDF pp. 121-124) → bell-inequalities
- Tsirelson's inequality: this is the best any quantum strategy can do, whatever entangled state or measurements (L4.3, PDF p. 124) → bell-inequalities
- Meaning: it is an example of Bell test and of nonlocality. The essence of Bell's theorem is that quantum mechanics is incompatible with local hidden variable theories. The CHSH game is a clean demonstration (L4.3, PDF p. 129) → bell-inequalities
- Experiments implement the CHSH game and confirm entanglement-based strategies. The 2022 Nobel Prize in Physics (Aspect, Clauser, Zeilinger) recognised Bell-test experiments on entangled photons (L4.3, PDF p. 129) → bell-inequalities
- The source says CHSH is named after Clauser, Horne, Shimony, Holt (1969 paper, described as an experiment) and Tsirelson first formulated it as a game (L4.3, PDF pp. 113, 124) → bell-inequalities

## Not covered (qubits-and-circuits section)
- Single-qubit gates as Bloch-sphere rotations (R_x, R_y, R_z, Euler decompositions): not in the parts read except the R_y remark in the CHSH section.
- Solovay-Kitaev and explicit universality proofs: stated as out of scope in L6.2.
- Quantum circuits for the quantum Fourier transform or Grover (Unit II) were not read for this domain.

## Level (qubits-and-circuits section)
University (advanced undergraduate / intro graduate), but Lessons 3 to 4 are readable by a motivated beginner who has seen the linear algebra of Lessons 1 and 2.

## quantum-algorithms

Accessed (this section): full text of Unit II from the extracted text: Lesson 5 (query algorithms), Lesson 6.1-6.2 (cost, asymptotics; 6.3 not re-read), Lesson 7 (spectral theorem, phase estimation, QFT, Shor) and Lesson 8 (Grover). Locations "L<lesson>.<section>, PDF p. N" (PDF page = book page + 6, using the page markers of the extracted text).

### query-model-and-oracles
- In the usual model the whole input is given to the computation. In the query model the input is available only as a function, accessed by queries, like random access to the bits of the input (L5.1, PDF pp. 134-135) → query-model-and-oracles
- The input is called an oracle or black box: its full description is hidden, and the only way to learn about it is to evaluate it on chosen arguments (L5.1, PDF p. 134) → query-model-and-oracles
- The inputs are functions f: {0,1}^n -> {0,1}^m. A query picks a string x and gets f(x) (L5.1, PDF p. 135) → query-model-and-oracles
- The efficiency measure is simply the number of queries, each at unit cost, ignoring the cost of everything else. This is related to, but not the same as, running time (L5.1, PDF p. 135) → query-model-and-oracles
- Example query problems: OR (is there an x with f(x)=1), Parity (is the number of x with f(x)=1 even or odd), Minimum (lexicographically first output), and the promise problem Unique search (exactly one z with f(z)=1, find z) (L5.1, PDF p. 136) → query-model-and-oracles
- A promise problem gives a guarantee on the input. Inputs violating it are "don't care" inputs for which the algorithm has no requirement (L5.1, PDF p. 136) → query-model-and-oracles
- Contrived problems are still useful: Shor's factoring algorithm was inspired by Simon's algorithm, and extreme cases show the potential and limits of quantum computing (L5.1, PDF pp. 136-137) → query-model-and-oracles
- Classical query gates just compute f. They cannot be used directly in quantum circuits because they would be non-unitary for some f (L5.1, PDF pp. 137-138) → query-model-and-oracles
- Standard (bit) query gate U_f: |x>|y> -> |x>|y XOR f(x)>, where XOR is bitwise. It echoes x and XORs f(x) onto y. It is deterministic, its own inverse and a permutation matrix, hence unitary (L5.1, PDF p. 138) → query-model-and-oracles
- The cost of building the query gates is ignored: it is considered part of preparing the input, not of solving the problem. The query model is a theoretical device to show potential advantages, not a full resource accounting (L5.1, PDF p. 139) → query-model-and-oracles
- Phase query gate: Z_f|x> = (-1)^{f(x)}|x>. It can be implemented with one U_f query plus a workspace qubit prepared in |->, which stays in |-> and can be reused (L8.2, PDF pp. 240-241) → query-model-and-oracles, phase-kickback
- Grover's algorithm is formalized in the query model, but it works with any f for which a Boolean circuit exists, because a Boolean circuit for f can be turned into a quantum circuit for U_f using workspace qubits that start and end in |0> (L8.2, PDF p. 239) → query-model-and-oracles
- When many algorithms are compared by query count, the source says counting queries is the same as giving query gates unit cost and all other gates (e.g. Hadamard) zero cost (L6.2, PDF pp. 173-174) → query-model-and-oracles

### phase-kickback
- Setting (Deutsch circuit): with the target qubit in |-> and the other qubit in |+>, U_f maps the state to |-> tensor ((-1)^{f(0)}|0> + (-1)^{f(1)}|1>)/sqrt2. The target qubit stays |->, while the information about f ends up in the phases of the other qubit. This is called phase kickback (L5.2, PDF pp. 141-142) → phase-kickback
- The key identity is |0 XOR a> - |1 XOR a> = (-1)^a (|0> - |1>), checked for a = 0 and a = 1 (L5.2, PDF p. 141) → phase-kickback
- Second explanation: |b XOR c> = X^c|b>, so U_f(|psi>|a>) = (X^{f(a)}|psi>)|a>. Since X|-> = -|->, one gets U_f(|->|a>) = (-1)^{f(a)}|->|a> (L5.2, PDF p. 143) → phase-kickback
- The point is that |-> is an eigenvector of X with eigenvalue -1. The source says phase kickback is generalized to other unitaries in Lesson 7 (L5.2, PDF p. 143) → phase-kickback
- Generalization: if |psi> is an eigenvector of U with eigenvalue e^{2 pi i theta} and a control qubit is in |+>, controlled-U gives |psi> tensor (|0> + e^{2 pi i theta}|1>)/sqrt2. The eigenvalue is "kicked" into the phase of the control, while the eigenvector register is unchanged (L7.2, PDF p. 198) → phase-kickback
- Why the first Hadamard is needed: it puts the control in a superposition so the kickback is a relative phase. A global phase would have no effect on measurement probabilities (L7.2, PDF pp. 199-200) → phase-kickback
- Why the second Hadamard is needed: before it, measuring the control gives 0 and 1 with probability 1/2 each and says nothing about theta. The second Hadamard turns the phase into an outcome probability by interference (L7.2, PDF p. 200) → phase-kickback
- Phase kickback is used to build Z_f from U_f in Grover's algorithm (L8.2, PDF pp. 240-241) → phase-kickback
- The Deutsch-Jozsa analysis uses "exactly the same phase kickback" to turn the query into the state |-> tensor (2^{-n/2} sum over x of (-1)^{f(x)}|x>) (L5.3, PDF pp. 146-147) → phase-kickback, deutsch-jozsa
- Simon's algorithm does not use phase kickback: the lower m qubits enter the query gate in |0> (L5.4, PDF p. 154) → phase-kickback, bernstein-vazirani-and-simon

### deutsch-jozsa
- Deutsch's problem: given f: {0,1} -> {0,1}, output 0 if f is constant and 1 if f is balanced (the two output values occur equally often). It is the parity problem with n = 1, i.e. the parity (XOR) of the two bits f(0), f(1) (L5.2, PDF pp. 139-140) → deutsch-jozsa
- Classically, every query algorithm must query both f(0) and f(1), since knowing one bit tells nothing about the parity. Two queries are optimal (L5.2, PDF p. 140) → deutsch-jozsa
- Deutsch's algorithm uses one query: initial state |1>|0> (target in |1>), H on both qubits, U_f, H on the control, measure. Outcome 0 means constant, 1 means balanced. The final state is (-1)^{f(0)} |-> times |0> if f(0) XOR f(1) = 0, and times |1> otherwise, so the answer is correct with probability 1 (L5.2, PDF pp. 140-142) → deutsch-jozsa
- The source calls this a "modest" advantage, one query against two, but a quantifiable advantage of quantum over classical (L5.2, PDF p. 140) → deutsch-jozsa
- Deutsch-Jozsa problem: given f: {0,1}^n -> {0,1}, promised to be constant or balanced, output 0 for constant and 1 for balanced. Other functions (e.g. a function with value 1 on only one of four inputs) are "don't care" inputs (L5.3, PDF pp. 144-145) → deutsch-jozsa
- Deutsch-Jozsa circuit: n qubits in |0> and one in |1>, H on all, one query U_f, H on the n qubits, measure those n. Classical post-processing takes the OR of the n outcomes: all outcomes 0 means constant, otherwise balanced (L5.3, PDF pp. 144-145) → deutsch-jozsa
- Action of a layer of Hadamards on n qubits: H^{(x)n}|x> = 2^{-n/2} sum over y of (-1)^{x_{n-1}y_{n-1}+...+x_0 y_0}|y> (L5.3, PDF p. 146) → deutsch-jozsa
- Analysis: the probability that all n measurement outcomes are 0 is |2^{-n} sum over x of (-1)^{f(x)}|^2. It is 1 if f is constant (sum is +/-2^n) and 0 if f is balanced (the +1 and -1 terms cancel). So the algorithm is always correct when the promise holds (L5.3, PDF p. 147) → deutsch-jozsa
- Classical deterministic algorithms need 2^{n-1}+1 queries in the worst case, since after 2^{n-1} equal answers both "constant" and "balanced" are still possible. This is an exponential advantage for the quantum algorithm over deterministic classical ones (L5.3, PDF pp. 147-148) → deutsch-jozsa
- The catch: a classical randomized algorithm that queries k random strings and answers "constant" if all values agree is always right on constant f and wrong on balanced f with probability only 2^{-k+1}. With k = 11 it is right with probability above 99.9% (the source text prints this figure, the percent sign was lost in extraction). So the advantage over probabilistic algorithms is only "rather modest" (L5.3, PDF p. 148) → deutsch-jozsa

### bernstein-vazirani-and-simon
- Binary dot product: x . y = x_{n-1}y_{n-1} XOR ... XOR x_0 y_0, i.e. the parity of the bits of x at the positions where y has a 1. It is symmetric (L5.3, PDF p. 148) → bernstein-vazirani-and-simon
- Bernstein-Vazirani problem: f: {0,1}^n -> {0,1} is promised to satisfy f(x) = s . x for some hidden string s. Output s. Also called the Fourier sampling problem (L5.3, PDF pp. 148-149) → bernstein-vazirani-and-simon
- The Deutsch-Jozsa circuit (without the OR post-processing) solves it with one query. H^{(x)n}|x> = 2^{-n/2} sum_y (-1)^{x.y}|y>, and the final state is |-> tensor |s>, because the sum over x of (-1)^{(s XOR y).x} / 2^n is 1 if y = s and 0 otherwise. The measurement reveals s (L5.3, PDF pp. 149-151) → bernstein-vazirani-and-simon, deutsch-jozsa
- The identity used: (s.x) XOR (y.x) = (s XOR y).x, and 2^{-n} sum over x of (-1)^{z.x} = 1 if z = 0^n and 0 otherwise (for z not 0^n the dot product is 0 for exactly half of the x) (L5.3, PDF pp. 150-151) → bernstein-vazirani-and-simon
- Classically at least n queries are needed (information argument: each query gives one bit about the n bits of s). n queries suffice by querying the n strings with a single 1. So the advantage is 1 query versus n (L5.3, PDF p. 151) → bernstein-vazirani-and-simon
- Nomenclature: the algorithm is really the Deutsch-Jozsa algorithm, though often called the "Bernstein-Vazirani algorithm". Bernstein and Vazirani went on to define the recursive Fourier sampling problem, the first known query problem with a super-polynomial quantum advantage over probabilistic algorithms. Its hard part is proving the classical lower bound (L5.3, PDF pp. 151-152) → bernstein-vazirani-and-simon, quantum-complexity
- Simon's problem: f: {0,1}^n -> {0,1}^m with the promise that there is a string s such that f(x) = f(y) iff (x = y or x XOR s = y). Output s (L5.4, PDF p. 153) → bernstein-vazirani-and-simon
- If s = 0^n then f is one-to-one. If s is not 0^n then f is two-to-one, with the two inputs of an output having the form w and w XOR s. The correct s is unique. The source says the problem is artificial, "tailor-made" to be easy for quantum and hard for classical computers (L5.4, PDF p. 153) → bernstein-vazirani-and-simon
- Quantum circuit: n qubits in |0> with H, the m lower qubits in |0> go into U_f, then H on the n qubits, measure them. The state before measurement is 2^{-n} sum_x sum_y (-1)^{x.y}|f(x)>|y> (L5.4, PDF pp. 154-155) → bernstein-vazirani-and-simon
- Analysis: the probability of measuring y is 2^{-2n} sum over z in range(f) of |sum over x in f^{-1}({z}) of (-1)^{x.y}|^2. If s = 0^n, y is uniform. If s is not 0^n, y is uniform over the 2^{n-1} strings with y.s = 0 and never has y.s = 1 (L5.4, PDF pp. 156-158) → bernstein-vazirani-and-simon
- Classical post-processing: run the circuit k = n + 10 times to get strings y^1..y^k, form the k x n binary matrix M. Then M v = 0 mod 2 for the vector v of s, so s is in the null space of M mod 2. With k = n + r the null space contains only 0^n and s with probability at least 1 - 2^{-r} (above 99.9% for r = 10) (L5.4, PDF pp. 158-159) → bernstein-vazirani-and-simon
- The null space of M mod 2 is computed efficiently by Gaussian elimination, which works the same mod 2 as over the reals or complex numbers (L5.4, PDF pp. 159-160) → bernstein-vazirani-and-simon
- Classical difficulty: any probabilistic query algorithm with fewer than 2^{n/2-1} - 1 queries fails with probability at least 1/2. The intuition is that unless two queried inputs have the same output, one only learns that s is not the XOR of two queried strings. So Simon's algorithm needs a number of queries linear in n, while any classical algorithm needs exponentially many: an exponential separation even against probabilistic algorithms (L5.4, PDF p. 160) → bernstein-vazirani-and-simon, quantum-complexity
- Simon's algorithm inspired Shor's factoring algorithm (L5.4, PDF p. 152; L5.1, PDF p. 137) → bernstein-vazirani-and-simon, shor-algorithm

### quantum-fourier-transform
- Preview (before the general definition): the 4x4 matrix with columns |phi_y> = (1/2) sum_x e^{2 pi i xy/4}|x> is the 4-dimensional discrete Fourier transform, called QFT_4 (L7.2, PDF pp. 198-199) → quantum-fourier-transform
- Define omega_N = e^{2 pi i/N}. The N-dimensional QFT is QFT_N = N^{-1/2} sum over x,y of omega_N^{xy} |x><y|. It is the matrix of the discrete Fourier transform, with the factor 1/sqrt(N) included so that it is unitary (L7.2, PDF p. 208) → quantum-fourier-transform
- It is defined for any positive integer N, although only N = 2^m is needed for phase estimation. QFT_2 is the Hadamard matrix (L7.2, PDF pp. 206, 208-209) → quantum-fourier-transform
- Unitarity: the columns are orthonormal; the inner product of two columns is a geometric series that sums to 0 when the columns differ (points spread round the unit circle cancel) and to 1 when equal (L7.2, PDF pp. 209-210) → quantum-fourier-transform
- Example matrices are given for N = 1, 2, 3, 4, 8 (L7.2, PDF pp. 208-209) → quantum-fourier-transform
- Controlled-phase gate: diag(1,1,1,e^{i alpha}). It is symmetric in control and target (L7.2, PDF pp. 210-211) → quantum-fourier-transform
- Recursive circuit for N = 2^m: (1) apply QFT_{2^{m-1}} to the m-1 lower qubits, (2) use the top qubit as control to apply controlled-phase gates with angles from pi/2 up to pi/2^{m-1}, (3) a Hadamard on the top qubit, (4) a permutation of qubits. The base case m = 1 is a Hadamard (L7.2, PDF pp. 211-213) → quantum-fourier-transform
- Correctness rests on the identity (-1)^{ab} omega_{2^{m-1}}^{xy} omega_{2^m}^{ay} = omega_{2^m}^{(2x+a)(2^{m-1}b+y)} (L7.2, PDF pp. 213-214) → quantum-fourier-transform
- Gate count s_m = s_{m-1} + (2m-1) with s_1 = 1, which gives s_m = m^2 (counting each controlled-phase gate as one gate). Using only floor(m/2) swaps still gives O(m^2). With the standard gate set the cost remains quadratic in m (L7.2, PDF pp. 214-215) → quantum-fourier-transform
- The sub-quadratic approximation: P_alpha is very close to the identity for small alpha, so most controlled-phase gates can be dropped with little loss of accuracy (L7.2, PDF p. 215) → quantum-fourier-transform
- Relation to FFT: the source says the circuit "is essentially the fast Fourier transform in the form of a quantum circuit". The classical FFT efficiently computes the DFT and is considered one of the most important algorithms ever discovered. The QFT circuit is based on the same underlying structure (L7.2, PDF pp. 207, 214) → quantum-fourier-transform
- The inverse QFT is obtained by replacing each gate by its inverse and reversing the order (L7.2, PDF p. 212) → quantum-fourier-transform
- Three viewpoints on the DFT: a linear map, a classical computation on a vector of complex numbers, or (the one used) a unitary operation on a quantum system (L7.2, PDF p. 207) → quantum-fourier-transform
- ⚠️ The source defines QFT over Z_N for any N and builds the circuit only for N = 2^m. It does not give a separate treatment of QFT on Z_2^n (the Hadamard transform is treated separately, as H^{(x)n}, in L5.3). The link between QFT_2^m and H^{(x)m} is not stated beyond QFT_2 = H (L7.2, PDF p. 208) → quantum-fourier-transform

### phase-estimation
- Spectral background: a normal matrix M (MM† = M†M) has a spectral decomposition M = sum_k lambda_k |psi_k><psi_k| over an orthonormal basis. Unitary and Hermitian matrices are normal. Then M|psi_j> = lambda_j |psi_j>, so lambda_j is an eigenvalue and |psi_j> an eigenvector (L7.1, PDF pp. 191-193) → phase-estimation
- Eigenvalues of a unitary have absolute value 1 (they lie on the unit circle), because unitaries preserve the norm (L7.1, PDF p. 194) → phase-estimation
- Phase estimation problem: given a unitary circuit for an n-qubit U and an n-qubit state |psi> promised to be an eigenvector, output an approximation to theta in [0,1) with U|psi> = e^{2 pi i theta}|psi>. Note that the input includes a quantum state, and that theta = 1 is identified with theta = 0 (L7.1, PDF pp. 195-196) → phase-estimation
- Phase estimation is typically a subproblem inside a larger computation, such as factoring (L7.1, PDF p. 195) → phase-estimation
- One control qubit: H on the control, controlled-U, H on the control, measure. The outcome probabilities are p_0 = cos^2(pi theta) and p_1 = sin^2(pi theta). This gives theta to one bit of accuracy and is exact if theta is 0 or 1/2 (L7.2, PDF pp. 197-199) → phase-estimation
- Using controlled-U^2 instead (two controlled-U gates) effectively doubles theta to 2 theta, which shifts the binary point and gives information about the second binary digit of theta (L7.2, PDF pp. 200-201) → phase-estimation
- Two control qubits: controlled-U on the first, controlled-U^2 on the second, giving the state 2^{-1} sum_{x=0}^{3} e^{2 pi i x theta}|x> on the controls. If theta = y/4 these four states are an orthonormal basis, so applying the inverse of QFT_4 and measuring gives y without error. For other theta the most likely outcome is the closest y/4, with probability just above 40% (L7.2, PDF pp. 202-206) → phase-estimation
- General procedure (Figure 7.14): m control qubits in |0^m>, H on each, controlled-U^{2^k} on control k (k = 0..m-1), then inverse QFT_{2^m} on the controls and measure. The register |psi> is left unchanged (L7.2, PDF pp. 215-216) → phase-estimation
- Before the inverse QFT the controls hold 2^{-m/2} sum_x e^{2 pi i x theta}|x>. If theta = y/2^m exactly, this is QFT_{2^m}|y>, so the inverse QFT gives |y> and the measurement reveals y exactly (L7.2, PDF pp. 216-217) → phase-estimation
- General theta: outcome y has probability p_y = |2^{-m} sum_x e^{2 pi i x (theta - y/2^m)}|^2. This is a geometric series, analysed by comparing arc and chord lengths on the unit circle (L7.2, PDF pp. 217-218) → phase-estimation
- Success probability bound 1: if y/2^m is one of the two best m-bit approximations to theta (|theta - y/2^m| <= 2^{-(m+1)}), then p_y >= 4/pi^2 (about 0.405), for every m (L7.2, PDF pp. 218-219) → phase-estimation
- Success probability bound 2: if |theta - y/2^m| is at least 2^{-m} (and at most 1/2) then p_y <= 1/4. The source calls this bound crude, because the probability is usually much lower (L7.2, PDF p. 219) → phase-estimation
- Take-away: close approximations are likely (over 40%) and ones off by more than 2^{-m} are unlikely (at most 25%). Repeating the procedure and taking the most common outcome gives an approximation within 1/2^m with error decreasing exponentially in the number of runs. The eigenstate is not disturbed, so it can be reused (L7.2, PDF p. 220) → phase-estimation
- Precision versus number of control qubits: the number of controlled-U copies is 2^m - 1 if U^k is built by repetition, so accuracy costs exponentially in m, unless U^k has a more efficient circuit (as in Shor's algorithm, where modular exponentiation gives it) (L7.2, PDF pp. 215-216) → phase-estimation
- Phase estimation can also be run on an input state that is not an eigenvector. The measured result then corresponds to a random eigenvector in the decomposition of the input. The source uses this in order finding, with |1> as input (L7.3, PDF p. 232) → phase-estimation
- Hadamard roles: the first layer makes the superposition on which the kickback acts, the inverse QFT converts the phase encoded in the amplitudes into a standard-basis outcome (L7.2, PDF pp. 199-200, 205) → phase-estimation, phase-kickback

### shor-algorithm
- Structure of Shor's algorithm in this course: reduce integer factorization to order finding (classical), solve order finding with phase estimation (quantum). The source says Shor did not describe it in terms of phase estimation but this is "a natural and intuitive way" to explain it (L7.3, PDF pp. 220-222) → shor-algorithm
- Integer factorization problem: given N >= 2 output its prime factorization. The fundamental theorem of arithmetic makes it unique (L6.1, PDF p. 162) → shor-algorithm
- Classical difficulty: trial division costs O(n^2 2^{n/2}) for n-bit N. The number field sieve, the fastest known classical algorithm, is believed (not proven) to cost 2^{O(n^{1/3} (lg n)^{2/3})}, which the source says is still exponential-type scaling. RSA1024 (309 digits) remains unfactored, whereas RSA250 was factored in 2020 with thousands of CPU core-years (L6.1, PDF pp. 163-164; L6.2, PDF pp. 180-181) → shor-algorithm, quantum-complexity
- Z_N = {0..N-1} with addition and multiplication mod N is a ring. Z*_N = elements a with gcd(a,N) = 1 form a group under multiplication, and every a in Z*_N has some power equal to 1 (L7.3, PDF pp. 222-223) → shor-algorithm
- Order finding: given N and a with gcd(N,a) = 1, output the smallest positive r with a^r = 1 mod N (the order of a modulo N) (L7.3, PDF pp. 223-224) → shor-algorithm
- Multiplication-by-a operation M_a|x> = |ax mod N> is a permutation matrix, so unitary (inverse M_{a^{-1}}, computed by extended Euclid). For N = 15, a = 2 an example table is given (L7.3, PDF p. 224) → shor-algorithm
- Eigenvectors: |psi_j> = r^{-1/2} sum_k omega_r^{-jk}|a^k> has M_a|psi_j> = omega_r^j |psi_j>, for j = 0..r-1. Eigenvalue 1 for j = 0 and e^{2 pi i/r} for j = 1 (L7.3, PDF pp. 225-226) → shor-algorithm, phase-estimation
- Phase estimation on M_a with eigenvector |psi_1> gives an approximation to theta = 1/r. Take the reciprocal of the estimate and round to the nearest integer. Example: r = 6, m = 5 gives y = 5 (about 68% chance), 32/5 = 6.4, rounding to 6. With m = 4 the best approximation 3/16 gives 5.33 and the wrong value 5 (L7.3, PDF pp. 226-229) → shor-algorithm
- Precision needed: it suffices that |y/2^m - 1/r| < 1/(2r(r+1)); since r < N, an error at most 1/(2N^2) suffices. Taking m = 2 lg(N) + 1 gives high success probability (m = 2 lg(N) gives at least 40%) (L7.3, PDF pp. 229-230) → shor-algorithm
- Implementation of M_a^{2^k}: do not iterate M_a, but compute b = a^{2^k} mod N classically by repeated squaring and use the circuit for M_b. The circuit for M_a is built from reversible, garbage-free multiplication and division, with cost O(n^2) where n = lg(N-1) bits. For a general circuit U this trick would not be available (L7.3, PDF pp. 226-228) → shor-algorithm
- Because |psi_1> is hard to prepare, run phase estimation on |1> instead, using |1> = r^{-1/2} sum_k |psi_k>. The result is the same as picking k in {0..r-1} uniformly at random and estimating k/r (L7.3, PDF pp. 230-233) → shor-algorithm
- Continued fractions: given N and alpha in (0,1), there is at most one fraction u/v (0 <= u, v < N, v nonzero, gcd(u,v) = 1) with |alpha - u/v| < 1/(2N^2). The continued fraction algorithm finds it with a Boolean circuit of size O((lg N)^3). It gives k/r in lowest terms, so only a divisor v of r is learned (nothing from k = 0) (L7.3, PDF p. 231) → shor-algorithm
- Recovering r: if k is random, the least common multiple of the denominators v seen over a few runs equals r with high probability, and the failure probability drops exponentially with the number of samples (L7.3, PDF pp. 231-232) → shor-algorithm
- Total quantum cost: each controlled M_a^{2^k} costs O(n^2), there are m = O(n) of them, so O(n^3). Hadamards contribute O(n), the inverse QFT O(n^2), so controlled operations dominate: O(n^3). The classical computations (modular powers, continued fractions) are also O(n^3). This assumes standard arithmetic algorithms; asymptotically faster ones improve it (L7.3, PDF p. 233) → shor-algorithm
- Factoring by order finding is classical: split N recursively (test primality first). Even N and perfect powers are easy to split classically, so the order-finding method is for N odd and not a prime power (L7.3, PDF pp. 233-234) → shor-algorithm
- Splitting algorithm: pick random a in {2..N-1}; if d = gcd(a,N) > 1 output d and N/d; else find the order r of a modulo N; if r is even compute d = gcd(a^{r/2} - 1, N) and output d, N/d if d > 1; otherwise fail (L7.3, PDF p. 234) → shor-algorithm
- Failure happens if r is odd or if r is even and gcd(a^{r/2} - 1, N) = 1. For a random a the failure probability is at most 2^{-(m-1)} where m is the number of distinct prime factors of N, so at most 1/2 for each run. After t runs the success probability is at least 1 - 2^{-t} (L7.3, PDF pp. 234-235) → shor-algorithm
- Why it works: (a^{r/2} - 1)(a^{r/2} + 1) = a^r - 1, which N divides, so the prime factors of N divide one factor or the other. A nontrivial factor arises unless all factors divide the same term (L7.3, PDF p. 235) → shor-algorithm
- ⚠️ Not covered: the discrete logarithm problem is not mentioned in the parts read (Lessons 5 to 8). The source relates Shor's algorithm only to factoring and order finding.

### grover-search
- Unstructured search: given f: {0,1}^n -> {0,1}, find x with f(x) = 1 (a solution), or report that none exists. f is efficiently computable but otherwise arbitrary, a "needle in a haystack". Notation N = 2^n. The OR problem only asks whether a solution exists (L8.1, PDF pp. 238-240) → grover-search
- Classical cost: N evaluations for a deterministic algorithm, and O(N) even for a probabilistic algorithm with high success probability. Grover's algorithm needs O(sqrt(N)) evaluations, done in superposition, with iteration and interference (L8.1, PDF pp. 238-239) → grover-search
- The source states honestly that the quadratic advantage "seems unlikely" to give a practical advantage soon, since classical hardware is much faster. It notes that FFT and fast sorting offer a little less than a quadratic advantage over naive methods and are very important (L8 intro, PDF pp. 237-238) → grover-search
- Algorithm: (1) start Q in |0^n> and apply H to every qubit, giving |u>, the uniform superposition; (2) apply t times the Grover operation G = H^{(x)n} Z_OR H^{(x)n} Z_f; (3) measure in the standard basis (L8.2, PDF p. 242) → grover-search
- Z_f|x> = (-1)^{f(x)}|x> costs one query. Z_OR|x> = |x> if x = 0^n and -|x> otherwise. It needs no queries and is independent of f. Z_OR = 2|0^n><0^n| - I, so H^{(x)n} Z_OR H^{(x)n} = 2|u><u| - I (L8.2-8.3, PDF pp. 241-242, 246) → grover-search
- Applying to search: choose t, run the algorithm, then query f on the output x. If f(x) = 1 output x, otherwise rerun (possibly with another t) or declare "no solution" (L8.2, PDF p. 243) → grover-search
- Analysis: A_1 = {x: f(x)=1} and A_0 = {x: f(x)=0}. |A_0>, |A_1> are the uniform superpositions over each, and |u> = sqrt(|A_0|/N)|A_0> + sqrt(|A_1|/N)|A_1> = cos(theta)|A_0> + sin(theta)|A_1> with theta = arcsin(sqrt(|A_1|/N)). The state stays in the real span of |A_0>, |A_1> (L8.3, PDF pp. 244-249) → grover-search
- Z_f acts on that plane as Z_f|A_0> = |A_0> and Z_f|A_1> = -|A_1>, a reflection about the line parallel to |A_0>. The operator 2|u><u| - I is a reflection about the line along |u>. The product of two reflections is a rotation by twice the angle between the lines, here 2 theta (L8.3, PDF pp. 246, 249-251) → grover-search
- Result: G^t|u> = cos((2t+1)theta)|A_0> + sin((2t+1)theta)|A_1>. The state is rotated by 2 theta per iteration towards |A_1> (L8.3, PDF p. 249) → grover-search
- Choosing t: the probability to measure a solution is sin^2((2t+1)theta). Aim for (2t+1)theta close to pi/2, so t is about pi/(4 theta) - 1/2, and the recommended value is t = floor(pi/(4 theta)). It depends on the number of solutions s = |A_1| (L8.4, PDF pp. 251-252) → grover-search
- Unique solution (s = 1): theta = arcsin(1/sqrt(N)), about 1/sqrt(N) for large N, so t = floor(pi sqrt(N)/4) iterations and queries, that is O(sqrt(N)). Success probability p(N,1) = sin^2((2t+1)theta), with a table of values for N = 2 to 65536 (0.5 for N = 2, exactly 1 for N = 4, and above 0.99 from N = 32 on). It is not monotonic in N. p(N,1) >= 1 - 1/N is stated (without proof) (L8.4, PDF pp. 252-254) → grover-search
- Even a bound p >= 1/2 is enough, because the output can be checked with one query. After m runs the failure probability is at most 2^{-m}, with O(m sqrt(N)) queries (L8.4, PDF p. 254) → grover-search
- Multiple solutions: theta grows with s. Using the t chosen for s = 1 when s = 4 is catastrophic (success tends to 0 as N grows) because the state rotates twice as fast and overshoots towards -|A_0>. With the recommended t = floor(pi/(4 theta)) the success is high, and p(N,s) >= 1 - s/N and p(N,s) >= s/N are stated (not proved) (L8.4, PDF pp. 254-256) → grover-search
- Query count with s solutions: t <= (pi/4) sqrt(N/s), so O(sqrt(N/s)) queries (L8.4, PDF p. 256) → grover-search
- Unknown number of solutions: (a) pick t uniformly at random in {1..floor(pi sqrt(N)/4)}, which finds a solution with probability above 40% (analysis not given), repeated to boost; (b) a refined method picks t uniformly from {1..T} with T growing exponentially (T -> ceil(5T/4) works, doubling does not). It finds a solution with O(sqrt(N/s)) queries when s >= 1 and needs O(sqrt(N)) queries to detect that s = 0 (L8.4, PDF p. 257) → grover-search
- Trivial cases: if f is constant (no solutions or all strings are solutions), then Z_f|u> = +/-|u> and G|u> = +/-|u>, so the measurement always gives a uniform random string whatever t is (L8.4, PDF pp. 257-258) → grover-search
- Observation: replacing f by NOT f gives Z_g = -Z_f, which only changes the global phase, so the algorithm does not care which strings are solutions, only that it can tell them apart (L8.3, PDF p. 245) → grover-search
- Optimality: in the query model Grover's algorithm is asymptotically optimal. No query algorithm solving search, or even unique search, can use asymptotically fewer than O(sqrt(N)) queries in the worst case. This was proved rigorously in several ways and the lower bound was known before Grover's algorithm (L8.5, PDF p. 258) → grover-search, quantum-complexity
- Amplitude amplification: the technique of composing two reflections and iterating to rotate a state can be generalized, e.g. applied to another quantum algorithm to boost its success probability quadratically faster than classically possible. Grover's algorithm is also used as a subroutine and combined with other algorithms (L8.5, PDF p. 258) → grover-search
- ⚠️ Not covered: the amplitude amplification is only mentioned in one paragraph, without a circuit or analysis (L8.5, PDF p. 258).

### quantum-complexity
- Aim of the course: seek exponential or at least super-polynomial quantum advantages, ideally polynomial-cost quantum algorithms for problems not known to have polynomial-cost classical algorithms. Only a few examples are currently known (L6.2, PDF p. 182) → quantum-complexity
- Polynomial (but not super-polynomial) advantages are interesting but less compelling given the gap between quantum and classical technology. Grover's algorithm gives a quadratic advantage for unstructured search (L6.2, PDF p. 182) → quantum-complexity
- Cost is measured as the number of elementary operations in circuits as a function of input length. Because circuits have fixed size, an algorithm is a family of circuits {C_n}, and the cost is t(n) = size(C_n) (L6.2, PDF pp. 168-174) → quantum-complexity
- Polynomial cost means O(n^c) for a constant c. This is used as a loose abstraction of "efficient". Known classical factoring algorithms have exponential cost. NP-complete problems are not known (and widely conjectured not to be able) to have polynomial-cost algorithms. The exponential-time hypothesis says that no NP-complete problem has a sub-exponential algorithm (L6.2, PDF pp. 180-181) → quantum-complexity
- Uniformity: a circuit family must be easy to describe, otherwise polynomial size would not mean efficiency. The source says all families in the course have this property (L6.2, PDF pp. 182-183) → quantum-complexity
- Big-O: g(n) = O(h(n)) if g(n) <= c h(n) for all n >= n_0. Examples: addition O(n), multiplication O(n^2) with the standard algorithm, GCD (Euclid) O(nm), modular exponentiation O(n^3) (L6.2, PDF pp. 177-180) → quantum-complexity
- Summary of query separations in Lesson 5: Deutsch-Jozsa is exponential against deterministic classical algorithms but only modest against randomized ones. Bernstein-Vazirani is 1 versus n. Recursive Fourier sampling was the first super-polynomial separation against probabilistic algorithms. Simon is exponential against probabilistic algorithms (L5.3, PDF pp. 147-152; L5.4, PDF p. 160) → quantum-complexity
- Query advantages do not automatically carry over: the standard (non-query) model gives inputs explicitly, and it is "much more difficult" to show advantages there. Shor's factoring algorithm is the main example the course gives of a polynomial-cost quantum algorithm for a problem with no known polynomial-cost classical algorithm (L6 intro, PDF p. 161; L7.3, PDF pp. 220-233) → quantum-complexity
- ⚠️ Not covered: the complexity class BQP is not named, nor are P, NP formally defined, in the parts read (Unit II). Only informal remarks on polynomial vs exponential cost and NP-complete problems were found. Any BQP/class relationship would need another source.

### post-quantum-cryptography
- The security of the RSA public-key cryptosystem rests on the computational difficulty of integer factoring: an efficient factoring algorithm would break it (L6.1, PDF p. 164) → post-quantum-cryptography
- Illustrative sizes: the RSA Factoring Challenge number RSA1024 (309 decimal digits, 1024 bits) has no known factors, and the number field sieve factored the 250-digit RSA250 in 2020 with thousands of core-years on tens of thousands of machines (L6.1, PDF pp. 163-164) → post-quantum-cryptography
- The source stresses that nothing rules out a fast classical factoring algorithm, apart from failure to find one so far (L6.1, PDF p. 166) → post-quantum-cryptography
- Link to Shor: a polynomial-cost quantum algorithm for factoring (O(n^3) quantum cost with standard arithmetic for n-bit N, Lesson 7.3) means that the factoring assumption underlying RSA does not hold against a large enough quantum computer. ⚠️ The source does not itself draw this conclusion for RSA in Lesson 7. It only states the RSA-factoring link in L6.1 and the Shor cost in L7.3 (L6.1, PDF p. 164; L7.3, PDF p. 233) → post-quantum-cryptography, shor-algorithm
- ⚠️ Not covered: no discussion of post-quantum cryptographic schemes, key sizes under Grover, or elliptic-curve/discrete-log systems in Lessons 5 to 8. Grover is mentioned only as a quadratic speedup for unstructured search (L8 intro, PDF p. 237).

## Not covered (quantum-algorithms section)
- hamiltonian-simulation: no Hamiltonian simulation, product formulas or e^{-iHt} material in Lessons 5 to 8 (Unit II). The book as read has no Hamiltonian-evolution material (see earlier notes). Not covered.
- Discrete logarithm and the hidden subgroup problem: not mentioned.
- BQP and formal complexity classes: not named in Unit II.
- Lesson 6.3 (classical computations on quantum computers, reversible circuits for query gates) was not re-read for this section. See the qubits-and-circuits section for the parts already noted.

## Level (quantum-algorithms section)
University (advanced undergraduate / intro graduate). Full derivations are given (state-by-state analysis of Deutsch-Jozsa, Simon, QFT circuit, phase estimation probability bounds, Grover rotation), with some results stated without proof (continued fractions, Grover success bounds, classical lower bounds). Requires comfort with complex numbers, tensor products and basic number theory.
