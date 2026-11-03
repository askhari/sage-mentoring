---
source: watrous-2025
concepts: [complex-numbers, vectors-and-dirac-notation, inner-products-and-norms, matrices-and-linear-maps, unitary-and-hermitian-matrices, tensor-products, probability-basics]
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
