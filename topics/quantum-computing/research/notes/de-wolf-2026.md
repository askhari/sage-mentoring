---
source: de-wolf-2026
concepts: [complex-numbers, vectors-and-dirac-notation, inner-products-and-norms, matrices-and-linear-maps, unitary-and-hermitian-matrices, eigenvalues-and-eigenvectors, tensor-products, probability-basics, qubit, single-qubit-gates, multi-qubit-states, entanglement, two-qubit-gates, quantum-circuits, no-cloning, universal-gate-sets, quantum-teleportation, superdense-coding, bell-inequalities]
---

Accessed: full text of the arXiv PDF (extracted text). Title page: "Quantum Computing: Lecture Notes", Ronald de Wolf (QuSoft, CWI, University of Amsterdam), arXiv:1907.09415v6 [quant-ph], dated 27 Aug 2026 (PDF p. 1); preface says "August'26" update and copyright "August 2026" (PDF p. 5). ⚠️ The date is 2026 as printed in the extracted text; the caller should confirm against the arXiv listing before fixing the source year in sources.yaml (the entry id says 2023; the January'23 revision is the previous one listed). Page references below: "p. N" = PDF page, with the printed page number in brackets (printed = PDF − 12). Appendix A = linear algebra, Appendix B = other math.

## math-foundations

### Complex numbers
- A complex number is c = a + bi with real a, b and i² = −1 (App. B.1, p. 211 [199]) → complex-numbers
- It can be written in polar form c = r·e^{iφ}, where r = |c| = √(a²+b²) is the magnitude (also called modulus or norm) and φ ∈ [0, 2π) is the angle with the positive horizontal axis when c is viewed as the point (a, b) (App. B.1, p. 211 [199]) → complex-numbers
- Complex numbers of magnitude 1 lie on the unit circle; they are written e^{iφ} = cos φ + i sin φ (App. B.1, p. 211 [199]) → complex-numbers
- The complex conjugate c* is a − ib, equivalently r·e^{−iφ} (App. B.1, p. 211 [199]) → complex-numbers
- Geometric sum: Σ_{j=0}^{m−1} z^j equals m if z = 1 and (1−z^m)/(1−z) otherwise; applied to a root of unity z = e^{2πir/N} with r in {1,…,N−1}, the sum over j = 0..N−1 is 0 (App. B.1, p. 211 [199]) → complex-numbers
- Identity |1 − e^{iθ}| = 2|sin(θ/2)|, seen geometrically by drawing 1 and e^{iθ} as vectors in the complex plane; also cos²θ + sin²θ = 1 and sin 2θ = 2 sin θ cos θ (App. B.1, pp. 211–212 [199–200]) → complex-numbers
- A global phase e^{iθ} multiplying a state does not change any measurement probabilities, so it has no physical significance (§1.2.2, p. 16 [4]) → complex-numbers
- The amplitudes of a quantum state are complex numbers (§1.2.1, p. 15 [3]) → complex-numbers

### Vectors and Dirac notation
- A vector space V over a field F is closed under addition and scalar multiplication; C^d is the d-dimensional complex vector space of column vectors of d complex numbers (App. A.1, p. 205 [193]) → vectors-and-dirac-notation
- Linear independence, span, basis, and dimension (all bases have the same size); fixing an ordered basis lets each vector be written uniquely by its coefficients (App. A.1, p. 205 [193]) → vectors-and-dirac-notation
- A pure quantum state is a superposition |φ⟩ = α₀|0⟩ + … + α_{N−1}|N−1⟩ of classical states, with complex amplitudes α_i; the |i⟩ form an orthonormal basis of an N-dimensional Hilbert space, and the state is the column vector of its amplitudes (§1.2.1, p. 15 [3]) → vectors-and-dirac-notation
- Dirac notation: |v⟩ denotes the vector v (ket) and ⟨v| denotes v* (bra, the conjugate-transpose row vector); an inner product ⟨v|w⟩ is a bra-ket ("bracket") product (App. A.10, p. 210 [198]; §1.2.1, p. 15 [3]) → vectors-and-dirac-notation
- A single qubit is α₀|0⟩ + α₁|1⟩ with |α₀|² + |α₁|² = 1, living in C²; |0⟩ and |1⟩ are identified with the column vectors (1,0)ᵀ and (0,1)ᵀ (§1.3, p. 19 [7]) → vectors-and-dirac-notation
- The n-qubit basis state |x⟩ is the 2^n-dimensional vector with a 1 at position x (counting from 0) and 0 elsewhere; a register is a superposition of the 2^n basis states with squared-amplitude sum 1 (§1.3, p. 19 [7]) → vectors-and-dirac-notation
- Writing guidelines: do not nest kets inside kets or bras (⟨u|(α|v⟩+β|w⟩)⟩ is meaningless); do not use "qubit" as a noun for a multi-qubit register (App. A.10, p. 210 [198]; footnote 6, §1.3, p. 19 [7]) → vectors-and-dirac-notation

### Inner products and norms
- Inner product ⟨v|w⟩ = v*w = Σ_i v_i* w_i, conjugating the first vector (physics convention; mathematicians usually conjugate the second). A vector space with this inner product is a Hilbert space (App. A.3, p. 206 [194]) → inner-products-and-norms
- Vectors are orthogonal if ⟨v|w⟩ = 0; a set is orthogonal if pairwise orthogonal, and orthonormal if in addition all vectors have norm 1 (App. A.3, p. 206 [194]) → inner-products-and-norms
- The norm is ‖v‖ = √⟨v|v⟩ = √(Σ|v_i|²), the usual Euclidean length; it induces the distance ‖v−w‖ (App. A.3, p. 206 [194]) → inner-products-and-norms
- ‖v−w‖² = ‖v‖² + ‖w‖² − ⟨v|w⟩ − ⟨w|v⟩, so for unit vectors the real part of ⟨v|w⟩ equals 1 − ½‖v−w‖²: close unit vectors have inner product near 1 (App. A.3, p. 206 [194]) → inner-products-and-norms
- Cauchy-Schwarz: |⟨a|b⟩| ≤ ‖a‖·‖b‖ (App. A.3, p. 206 [194]; App. B.1, p. 211 [199], with a short proof for real vectors) → inner-products-and-norms
- Born rule: measuring |φ⟩ = Σα_j|j⟩ in the computational basis gives j with probability |α_j|², so the amplitude vector must have Euclidean norm 1 (§1.2.2, p. 16 [4]) → inner-products-and-norms
- Measuring in any orthonormal basis {ψ_j} gives outcome j with probability |⟨φ|ψ_j⟩|²; if |φ⟩ equals a basis vector the outcome is certain (§1.2.2, p. 17 [5]) → inner-products-and-norms
- n-qubit basis states |x⟩, |y⟩ are orthogonal iff x ≠ y, shown either from the 1 at position x or from the product rule ⟨x|y⟩ = ⟨x₁|y₁⟩···⟨x_n|y_n⟩ (§1.3, p. 19 [7]) → inner-products-and-norms, tensor-products

### Matrices and linear maps
- Matrices represent linear maps between vector spaces with chosen bases; A_ij is entry (i,j), Aᵀ the transpose, I_d the identity, A⁻¹ the (unique if it exists) inverse with (AB)⁻¹ = B⁻¹A⁻¹ (App. A.2, pp. 205–206 [193–194]) → matrices-and-linear-maps
- The conjugate transpose (adjoint) A* transposes and conjugates every entry; (AB)* = B*A*. Physicists write A† for A* (App. A.2, p. 206 [194]) → matrices-and-linear-maps
- The outer product of v and w is the matrix vw* (App. A.3, p. 206 [194]); in Dirac notation |v⟩⟨w| (App. A.10, p. 210 [198]) → matrices-and-linear-maps, vectors-and-dirac-notation
- Trace: Tr(A) = Σ_i A_ii of a square matrix; it is additive, cyclic (Tr(AB) = Tr(BA)), e.g. Tr(A vv*) = v*Av, equals the sum of the eigenvalues, and Tr(A⊗B) = Tr(A)Tr(B) (App. A.7, p. 209 [197]) → matrices-and-linear-maps
- Rank = size of a largest linearly independent set of rows; rank(A) = rank(A*) = number of nonzero singular values; A is invertible iff it has full rank (App. A.8, p. 209 [197]) → matrices-and-linear-maps
- Every matrix has a singular value decomposition A = UΣV⁻¹ = Σ_i σ_i u_i v_i*, even non-diagonalizable ones such as [[0,1],[0,0]] (App. A.5, p. 208 [196]) → matrices-and-linear-maps
- Pauli matrices I, X, Y, Z (App. A.9, p. 210 [198]): each is both unitary and Hermitian, so self-inverse, with eigenvalues ±1; distinct non-identity Paulis anti-commute; Y = iXZ. They are orthonormal under the Hilbert-Schmidt inner product (1/d)Tr(A*B), so any 2×2 complex matrix is a combination α₀I+α₁X+α₂Y+α₃Z (real coefficients if Hermitian) → matrices-and-linear-maps, unitary-and-hermitian-matrices
- A quantum operation on a closed system is multiplication of the state vector by an N×N complex matrix U, i.e. it must be linear (§1.2.3, p. 18 [6]) → matrices-and-linear-maps

### Unitary, Hermitian, normal matrices and projectors
- A is unitary if A⁻¹ = A*. Equivalent: A preserves inner products; A preserves norms; A maps unit vectors to unit vectors (App. A.4, p. 206 [194]) → unitary-and-hermitian-matrices
- Eigenvalues of a unitary matrix have absolute value 1 (App. A.4, p. 207 [195]) → unitary-and-hermitian-matrices, eigenvalues-and-eigenvectors
- Quantum operations must preserve the norm of the amplitude vector (probabilities sum to 1), hence are unitary; being invertible they are reversible (apply U⁻¹), whereas measurement is not reversible (§1.2.3, p. 19 [7]) → unitary-and-hermitian-matrices
- A is normal if A*A = AA*; unitary matrices are normal (App. A.5, p. 207 [195]) → unitary-and-hermitian-matrices
- A is Hermitian if A = A*; Hermitian matrices are normal (hence unitarily diagonalizable) and have real eigenvalues (App. A.5, p. 208 [196]) → unitary-and-hermitian-matrices, eigenvalues-and-eigenvectors
- A Hermitian matrix is positive semidefinite (psd) if all eigenvalues are ≥ 0 (positive definite if > 0); equivalently A = C*C for some C. Writing A ⪰ B for "A − B is psd" gives a partial order on Hermitian matrices (App. A.5, p. 208 [196]) → unitary-and-hermitian-matrices
- A projection (projector) has all eigenvalues 0 or 1, equivalently A² = A (App. A.5, p. 208 [196]) → unitary-and-hermitian-matrices
- A projective measurement is a set of projectors P₁…P_m summing to I; they are pairwise orthogonal (P_iP_j = 0 for i≠j). Outcome j has probability ⟨φ|P_j|φ⟩ = ‖P_j|φ⟩‖² = Tr(P_j|φ⟩⟨φ|), and the state collapses to P_j|φ⟩/‖P_j|φ⟩‖ (§1.2.2, p. 16 [4]) → unitary-and-hermitian-matrices
- Measuring in the computational basis is the projective measurement with P_j = |j⟩⟨j|; measuring in another orthonormal basis uses P_j = |ψ_j⟩⟨ψ_j|; projectors may have higher rank (§1.2.2, pp. 16–17 [4–5]) → unitary-and-hermitian-matrices
- An observable M = Σ λ_i P_i (distinct real outcomes λ_i) is Hermitian, and its expected outcome is Tr(M|φ⟩⟨φ|); every Hermitian matrix has a spectral decomposition, so observables correspond one-to-one to Hermitian matrices. Z = |0⟩⟨0| − |1⟩⟨1| is the computational-basis observable (§1.2.2, p. 17 [5]) → unitary-and-hermitian-matrices, eigenvalues-and-eigenvectors

### Eigenvalues, spectral decomposition, functions of matrices
- λ is an eigenvalue of A if Av = λv for some nonzero v (the eigenvector); the set of eigenvalues is the spectrum (App. A.5, p. 207 [195]) → eigenvalues-and-eigenvectors
- Similar matrices (A = SBS⁻¹) share eigenvalues; Schur: every matrix is A = UTU⁻¹ with U unitary and T upper triangular, whose diagonal holds the eigenvalues (App. A.5, p. 207 [195]) → eigenvalues-and-eigenvectors
- A is diagonalizable (A = SDS⁻¹) iff it has d linearly independent eigenvectors, which form the columns of S; not every matrix is diagonalizable (App. A.5, pp. 207–208 [195–196]) → eigenvalues-and-eigenvectors
- If A is unitarily diagonalizable, A = UDU⁻¹, then A = Σ_i λ_i u_i u_i* = Σ_i λ_i |v_i⟩⟨v_i| (spectral decomposition), iff A has an orthonormal set of d eigenvectors (App. A.5, p. 207 [195]; App. A.10, p. 210 [198]) → eigenvalues-and-eigenvectors
- A matrix is normal iff it is unitarily diagonalizable (proved via Schur); a non-normal matrix like [[1,1],[0,2]] can still be diagonalized, but not by a unitary (App. A.5, p. 207 [195]) → eigenvalues-and-eigenvectors, unitary-and-hermitian-matrices
- The eigenvalues of A* are the complex conjugates of those of A (App. A.5, p. 208 [196]) → eigenvalues-and-eigenvectors
- Applying a function f to a normal matrix means applying f to its eigenvalues: if A = VDV⁻¹ then f(A) = V f(D) V⁻¹; with A = Σ λ_j a_j a_j*, e^{−iA} = Σ e^{−iλ_j} a_j a_j*. If A is Hermitian, e^{−iA} is unitary (footnote 1, §9.1, p. 83 [71]) → eigenvalues-and-eigenvectors, unitary-and-hermitian-matrices
- Time evolution under a time-independent Hamiltonian H (the energy observable, a Hermitian matrix) is the unitary U = e^{−iHt} applied to |ψ(0)⟩, solving the Schrödinger equation iℏ d|ψ⟩/dt = H|ψ⟩ with ℏ set to 1 (§9.1, p. 83 [71]) → eigenvalues-and-eigenvectors, unitary-and-hermitian-matrices
- Hamiltonian simulation is the task of finding a small circuit that is ε-close to e^{iHt}; the notes drop the minus sign for convenience (§9.1, p. 84 [72]) → eigenvalues-and-eigenvectors

### Tensor products
- For an m×n matrix A and m'×n' matrix B, A⊗B is the mm'×nn' block matrix with blocks A_ij·B (Kronecker product); the tensor product of two numbers is a number and of two column vectors is a column vector (App. A.6, p. 208 [196]) → tensor-products
- Properties: c(A⊗B) = (cA)⊗B = A⊗(cB); (A⊗B)* = A*⊗B* (order of factors unchanged, same for inverse and transpose); distributive over addition; associative; mixed-product rule (A⊗B)(C⊗D) = (AC)⊗(BD) (App. A.6, p. 209 [197]) → tensor-products
- Tensor product of vector spaces: if V and V' have dimensions d, d' and bases {v_i}, {v'_j}, then V⊗V' is d·d'-dimensional, spanned by all v_i⊗v'_j; applying A to V and B to V' corresponds to A⊗B on the product space (App. A.6, p. 209 [197]) → tensor-products
- Composite quantum systems: H = H_A⊗H_B has dimension NM with basis |i⟩⊗|j⟩; a general state is Σα_ij |i⟩⊗|j⟩ (a "bipartite" state; similarly tripartite etc.) (§1.2.1, p. 15 [3]) → tensor-products
- An n-qubit register lives in the tensor product of n qubit spaces, with 2^n basis states |b₁⟩⊗…⊗|b_n⟩ abbreviated |b₁…b_n⟩ (|1⟩⊗|0⟩ = |1⟩|0⟩ = |1,0⟩ = |10⟩) (§1.3, p. 19 [7]) → tensor-products
- Tensor identities in Dirac notation: (|u⟩⊗|v⟩)* = ⟨u|⊗⟨v| and |v⟩⟨v| ⊗ |w⟩⟨w| = (|v⟩⊗|w⟩)(⟨v|⊗⟨w|); omitting the ⊗ sign can be dangerously ambiguous (App. A.10, p. 210 [198]) → tensor-products, vectors-and-dirac-notation
- An observable A on the first part of a bipartite system acts as A⊗I, and one on the second part as I⊗B; measuring A and B separately differs from measuring the joint observable A⊗B, though the statistics of the product of outcomes coincide (§1.2.2, p. 17 [5]) → tensor-products
- Example: for |φ⟩ = (|00⟩+|11⟩)/√2, separate Z measurements give ++ or −− (state collapses), whereas the joint observable Z⊗Z leaves |φ⟩ undisturbed because it is a +1 eigenstate of Z⊗Z (§1.2.2, p. 17 [5]) → tensor-products, eigenvalues-and-eigenvectors
- The n-qubit Paulis (n-fold tensor products of I, X, Y, Z) number 4^n, form an orthonormal set under the Hilbert-Schmidt inner product, and every 2^n×2^n matrix is a unique linear combination of them (App. A.9, p. 210 [198]) → tensor-products

### Probability basics
- Union bound: Pr[A∨B] ≤ Pr[A] + Pr[B], and for T events, Pr[A₁∨…∨A_T] ≤ Σ Pr[A_i] (App. B.2, p. 212 [200]) → probability-basics
- A discrete random variable X takes value x_i with probability p_i; expectation E[X] = Σ p_i x_i, variance Var[X] = E[(X−E[X])²] = E[X²] − E[X]², standard deviation σ (App. B.2, p. 212 [200]) → probability-basics
- Linearity of expectation: E[Σ a_j X_j] = Σ a_j E[X_j]; for independent X, Y, E[XY] = E[X]E[Y]. Independence means Pr[X=x and Y=y] = Pr[X=x]·Pr[Y=y] (App. B.2, p. 212 [200]) → probability-basics
- Tail bounds (App. B.2, p. 213 [201]): Markov Pr[X ≥ kμ] ≤ 1/k for nonnegative X; Chebyshev Pr[|X−μ| ≥ kσ] ≤ 1/k²; Chernoff/Hoeffding for a sum of n i.i.d. {0,1} variables with mean np: Pr[|X−μ| ≥ αn] ≤ 2e^{−2α²n} → probability-basics
- Measurement outcomes are random: outcome probabilities are the squared amplitudes (Born rule), and observing a state induces a probability distribution on classical states (§1.2.2, p. 16 [4]) → probability-basics
- A randomized algorithm uses coin flips so its output is a random variable; "error probability ≤ 1/3" means worst case over every input: correct with probability ≥ 2/3 over the coins and/or quantum measurements (App. B.2, p. 213 [201]) → probability-basics
- Error reduction by repetition: for a 0/1-output algorithm with error ≤ 1/3, run it n = O(log(1/ε)) times (n odd, with 2e^{−2α²n} ≤ ε for α = 1/6) with fresh randomness and output the majority; the Chernoff bound gives error at most ε (App. B.2, p. 213 [201]) → probability-basics
- Union bound for T randomized subroutines each failing with probability ≤ 1/(3T): even if the failures are dependent, the probability that none fails is ≥ 2/3; if independent, the bound (1−1/(3T))^T ≥ 1 − T/(3T) = 2/3 uses the inequality in B.1 (App. B.2, p. 213 [201]) → probability-basics
- Converting expected running time T into worst-case time 3T with error ≤ 1/3 by cutting off after 3T steps, justified by Markov's inequality (App. B.2, p. 213 [201]) → probability-basics
- Useful inequalities: 1 + x ≤ e^x for all real x; for ε_j ∈ [0,1], 1 − Σε_j ≤ Π(1−ε_j) ≤ e^{−Σε_j} (App. B.1, p. 212 [200]) → probability-basics

## Not covered / level
- Requested but not covered: none. Fewer than 3 claims: none. "Roots of unity" appear in the source only in the geometric-sum example (App. B.1), not as a stand-alone topic (the QFT in Ch. 4 uses them but was not read here).
- Level: university (graduate-level lecture notes for theoretical-CS students); the appendices are terse reminders, not a gentle intro.

## qubits-and-circuits

Chapters read for this section: Ch. 1 (§1.3-1.5, exercises), Ch. 2 (§2.1-2.3, exercises), §13.1, Ch. 17. Claims already in the math-foundations section (n-qubit basis states, Born rule, projective measurement, unitarity, Paulis as unitary/Hermitian) are not repeated.

### Qubit
- A qubit is the quantum counterpart of a bit: a system with two basis states |0⟩, |1⟩, which can be in any superposition of the two (§1.3, p. 19 [7]) → qubit
- The notes warn against using "qubit" for a multi-qubit register: the term refers only to the state of a 2-dimensional system; "n-qubit" is fine as an adjective only (footnote 6, §1.3, p. 19 [7]) → qubit
- Measuring just the first qubit of a larger state is a projective measurement with projectors |0⟩⟨0|⊗I and |1⟩⟨1|⊗I; for (1/√3)|0⟩|φ⟩ + √(2/3)|1⟩|ψ⟩ outcome 0 has probability 1/3 and leaves |0⟩|φ⟩, outcome 1 has probability 2/3 and leaves |1⟩|ψ⟩ (§1.3, p. 20 [8]) → qubit
- Teleportation shows a qubit's amplitudes are not simply readable as classical data: sending α₀, α₁ over a classical channel alone is deemed impossible, intuitively since they may need unbounded precision to write down (§1.5, p. 22 [10]) → qubit
- Experimentally (introduction): the first 2-qubit quantum computer was built in 1997, a 5-qubit device factored 15 in 2001, and leading platforms (superconducting, trapped-ion) act on roughly 100-200 qubits; Google's 2019 "quantum supremacy" sampling task used 53 superconducting qubits (§1.1, p. 14 [2]) → qubit
- ⚠️ No Bloch sphere appears in the portions read (no mention found in Ch. 1-2); single-qubit states are treated purely as vectors in C² (§1.3, p. 19 [7]) → qubit

### Single-qubit gates
- A gate is a unitary acting on a small number of qubits (say at most 3), in analogy to classical logic gates (§1.4, p. 21 [9]) → single-qubit-gates
- Bitflip X (also NOT) swaps |0⟩ and |1⟩, matrix [[0,1],[1,0]]; phaseflip Z puts a minus sign on |1⟩, matrix diag(1,−1); I, X, Y, Z are all 1-qubit gates (§1.4, p. 21 [9]) → single-qubit-gates
- The phase gate R_φ = diag(1, e^{iφ}) rotates the phase of |1⟩ by φ and leaves |0⟩; Z = R_π, and R_{π/4} is commonly called the T-gate (§1.4, p. 21 [9]) → single-qubit-gates
- Hadamard H maps |0⟩ to (|0⟩+|1⟩)/√2 and |1⟩ to (|0⟩−|1⟩)/√2, matrix (1/√2)[[1,1],[1,−1]]; applied to |0⟩ or |1⟩ followed by measurement gives a fair coin (§1.4, p. 21 [9]) → single-qubit-gates
- Interference: H applied to (|0⟩+|1⟩)/√2 returns |0⟩ because the opposite-sign amplitudes of |1⟩ cancel; the notes compare this to interference of light or sound waves (§1.4, p. 21 [9]) → single-qubit-gates
- H is its own inverse (unitary and Hermitian, H = H* = H⁻¹); applying H to each qubit of |0ⁿ⟩ gives the uniform superposition over all n-bit strings, and H^{⊗n}|i⟩ = 2^{−n/2} Σ_j (−1)^{i·j} |j⟩ (Eq. 2.1) (§2.1.2, p. 26 [14]) → single-qubit-gates
- Rotation gate R(θ) = [[cosθ, −sinθ],[sinθ, cosθ]] rotates the amplitude vector counterclockwise by θ; exercises: HXH = Z, and H R_θ H = R_{−θ} (Ex. 1.3 and 1.5, p. 23 [11]; definition used in §17.2, p. 159 [147]) → single-qubit-gates
- Every real 1-qubit unitary is a rotation possibly preceded and followed by Z-gates, and every 1-qubit unitary equals e^{iα}·diag(1,e^{iβ})·rotation(θ)·diag(1,e^{iγ}) (exercises 4 and 5, Ch. 2, p. 32 [20]) → single-qubit-gates

### Multi-qubit states
- A 2-qubit system has the four basis states |00⟩, |01⟩, |10⟩, |11⟩ (tensor products of single-qubit basis states); an n-qubit register has 2ⁿ basis states and amplitudes with squared moduli summing to 1 (§1.3, p. 19 [7]) → multi-qubit-states
- Counting parameters: a joint classical distribution on spaces of size 2ⁿ and 2^m takes 2^{n+m} numbers, a product distribution only 2ⁿ+2^m; likewise a general (possibly entangled) n+m-qubit state needs 2^{n+m} amplitudes versus 2ⁿ+2^m for a product state (§1.3, p. 20 [8]) → multi-qubit-states
- Product states |φ_A⟩⊗|φ_B⟩ are often written |φ_A⟩|φ_B⟩; further abbreviation to |φ_Aφ_B⟩ is only safe when both are computational basis states (footnote 7, §1.3, p. 20 [8]) → multi-qubit-states
- Parallel gates on different parts of a register compose by tensor product; sequential gates by ordinary matrix product (§2.1.2, p. 26 [14]) → multi-qubit-states
- Despite the parameter-count similarity, quantum states are far more powerful than distributions because amplitudes may be negative or complex, enabling interference; amplitudes become probabilities only after squaring (§1.3, p. 20 [8]) → multi-qubit-states
- Analogy: statistical independence of random variables corresponds to non-entanglement of a product state (§1.3, p. 20 [8]) → multi-qubit-states

### Entanglement
- Entanglement means quantum correlations between qubits; a bipartite state is entangled iff it cannot be written as a tensor product |φ_A⟩⊗|φ_B⟩ (§1.3, p. 20 [8]) → entanglement
- The 2-qubit state (|00⟩+|11⟩)/√2 is called an EPR-pair (after Einstein, Podolsky, Rosen); neither qubit has a classical value initially, but measuring the first and seeing 0 collapses the whole state to |00⟩, fixing the second qubit too (§1.3, p. 20 [8]) → entanglement
- Misconception noted: Alice does not hold "|00⟩/√2" and Bob "|11⟩/√2"; the right intuition is a shared random coin flip with amplitudes 1/√2 in place of probabilities 1/2 (footnote 9, §1.5, p. 22 [10]) → entanglement
- Circuit example: H on the first qubit, then CNOT, then Z on the second turns |00⟩ into (|00⟩−|11⟩)/√2, an entangled state (Fig. 2.1, §2.1.2, pp. 27-28 [15-16]) → entanglement
- Entanglement can produce "non-local" effects but cannot signal faster than light; measuring half of an EPR-pair does not change what Bob sees, and a shared coin flip (local realist model) reproduces the computational-basis statistics of that single experiment (intro §1.1, p. 13 [1]; §17.1, p. 157 [145]) → entanglement
- Exercise facts: Alice applying U to her half of an EPR-pair equals Bob applying Uᵀ to his; and (U⊗Ū)|ψ_AB⟩ = |ψ_AB⟩ for n EPR-pairs (Ex. 17.1, 17.3, p. 163 [151]) → entanglement
- State (|00⟩ − |11⟩)/√2 is obtained from an EPR-pair by local operations (Z by Alice); the singlet (|01⟩−|10⟩)/√2 likewise (§17.2, p. 159 [147]; §17.3, p. 161 [149]) → entanglement

### Two-qubit gates
- CNOT negates the second (target) qubit if the first (control) is 1: |0⟩|b⟩→|0⟩|b⟩, |1⟩|b⟩→|1⟩|1−b⟩; matrix permuting the last two basis states (§1.4, pp. 21-22 [9-10]) → two-qubit-gates
- Controlled-U for an n-qubit unitary U is the block matrix diag(I, U) of size 2^{n+1} (§1.4, p. 22 [10]) → two-qubit-gates
- The Toffoli (CCNOT) gate has two controls and negates the third bit only if both are 1 (§2.1.2, p. 26 [14]) → two-qubit-gates
- Toffoli is complete for classical reversible computation: with a fixed 0 on the third wire it gives AND, with fixed 1s on the first two wires it gives NOT, and AND+NOT suffice for any Boolean circuit (§2.1.2, p. 26 [14]) → two-qubit-gates
- In circuit drawings, a control is a dot linked to the target gate; the CNOT target is drawn as ⊕ (§2.1.2, p. 27 [15]) → two-qubit-gates
- Exercises: CNOT is Hermitian and self-inverse; a CNOT can be built from two H gates and one controlled-Z; surrounding CNOT with H⊗H swaps control and target; a SWAP is built from CNOTs; a controlled-U (det U = 1) can be built from CNOTs and A, B, C with ABC = I and AXBXC = U (Ex. 1.4, 2.1-2.3, 2.6, pp. 23, 32 [11, 20]) → two-qubit-gates

### Quantum circuits
- A Boolean circuit is a finite directed acyclic graph of AND/OR/NOT gates with input and designated output nodes; circuit families (one circuit per input size) that are uniformly polynomial correspond exactly to languages in P (§2.1.1, p. 25 [13]) → quantum-circuits
- A quantum circuit generalizes this: the gates are unitaries on at most 2 or 3 qubits; input nodes hold the classical input bits plus extra workspace qubits initialised to |0⟩ (§2.1.2, pp. 26-27 [14-15]) → quantum-circuits
- At the end, some or all qubits are measured in the computational basis to get a classical output; measurement can be treated as a special gate but may be assumed to occur only at the end of the circuit, using one auxiliary qubit per delayed measurement (§2.1.2, p. 27 [15]; Ex. 2.8, p. 32 [20]) → quantum-circuits
- General projective measurements are implemented as a unitary U followed by a computational-basis measurement of the first qubit; to keep the post-measurement state one also applies U⁻¹ afterwards; the circuit for U may be large if the measurement is complicated (§2.1.2, p. 27 [15]) → quantum-circuits
- Because unitaries are reversible, a quantum gate has as many output wires as input wires (unlike AND); the circuit for U⁻¹ is the reversed order of the inverted gates, same size (§2.1.2, p. 27 [15] with footnote 5) → quantum-circuits
- Circuits are drawn with time running left to right, one horizontal wire per qubit (§2.1.2, p. 27 [15]) → quantum-circuits
- Quantum parallelism: a Toffoli-only circuit U from a classical algorithm maps |z⟩|0⟩ to |z⟩|f(z)⟩; applied to a uniform superposition it yields a superposition containing f(z) for all 2ⁿ z with one application, but measuring gives just one random (z, f(z)), so interference and entanglement are needed for real advantage (§2.3, pp. 28-29 [16-17]) → quantum-circuits
- Uncomputation/clean workspace: workspace qubits of a subroutine must be reset to |0⟩ before running it on a superposition, because leftover entanglement between address and workspace registers destroys the intended interference; the exercise shows a phase-query with leftover workspace breaks the HOₓH interference (Ex. 2.11 and comment, p. 33 [21]) → quantum-circuits
- BQP is the class of languages decided with success probability ≥ 2/3 by polynomial-size quantum circuit families (§2.1.2, pp. 27-28 [15-16]) → quantum-circuits

### No-cloning
- Copying an unknown qubit is impossible; this is stated and left as exercise: there is no 2-qubit unitary mapping |φ⟩|0⟩ to |φ⟩|φ⟩ for all qubits |φ⟩ (§1.5, p. 23 [11]; Ex. 1.12, p. 24 [12]) → no-cloning
- Teleportation illustrates the point: the qubit is moved to Bob and destroyed at Alice's side, not copied (§1.5, p. 23 [11]) → no-cloning
- Related exercise: unitaries cannot "delete" information, i.e., there is no 1-qubit unitary mapping every |φ⟩ to |0⟩ (Ex. 1.13, p. 24 [12]) → no-cloning
- ⚠️ The source gives no proof in the text (only the exercise with a hint in App. C) and cites [265] (Wootters-Zurek, per its bibliography numbering, not checked) (§1.5, p. 23 [11]) → no-cloning

### Universal gate sets
- (1) All 1-qubit gates together with CNOT form a universal set: any other unitary can be built from them (§2.2, p. 28 [16]) → universal-gate-sets
- That set is unrealistic since there are continuously many 1-qubit gates and none can be implemented to infinite precision, so one restricts to a small finite set that approximates all 1-qubit gates efficiently (§2.2, p. 28 [16]) → universal-gate-sets
- (2) {CNOT, Hadamard, T = R_{π/4}} is universal in the sense of approximation: any unitary can be approximated arbitrarily well by circuits over these gates (called the "Shor basis" in §13.1) (§2.2, p. 28 [16]; §13.1, p. 121 [109]) → universal-gate-sets
- Solovay-Kitaev theorem: any 1- or 2-qubit gate can be approximated to error ε with polylog(1/ε) gates from the small universal set, so even exponentially small error costs only polynomially many gates (§2.2, p. 28 [16], citing Nielsen-Chuang App. 3) → universal-gate-sets
- (3) {Hadamard, Toffoli} is universal, in the approximate sense, for all unitaries with real entries (§2.2, p. 28 [16]) → universal-gate-sets
- Counting argument: with k gate types each on ≤ 3 qubits, the number of circuits with ≤ C gates is at most (k+1)^C (3C)^{3C} = C^{O(C)}, each circuit computes at most one Boolean function (bounded-error 2/3 sense) (§13.1, p. 121 [109]) → universal-gate-sets
- Consequence: to compute even 1% of all 2^{2ⁿ} Boolean functions on n bits one needs C^{O(C)} ≥ (1/100)·2^{2ⁿ}, hence C ≥ Ω(2ⁿ/n); so almost all functions have circuit complexity near 2ⁿ and few problems are efficiently solvable on a quantum computer. A variant of the Riordan-Shannon classical counting argument (§13.1, p. 121 [109]) → universal-gate-sets
- ⚠️ The §13.1 counting argument is about Boolean functions computed by circuits (with workspace, bounded-error output), not directly about counting "unitaries needing exponentially many gates"; the source does not phrase it as a statement about unitaries (§13.1, p. 121 [109]) → universal-gate-sets
- Elementary-gate-set dependence: the class EQP (exact quantum polynomial time) depends on the allowed gate set, and (footnote in Ch. 14) requiring success probability exactly 1 in QMA would also depend on it (§13.2, p. 122 [110]; footnote 1, §14.1, p. 128 [116]) → universal-gate-sets

### Quantum teleportation
- Setting: Alice holds an unknown qubit α₀|0⟩+α₁|1⟩ and wants Bob to have it; they share an EPR-pair (Alice the left qubit, Bob the right); the protocol uses a classical channel only for communication (§1.5, p. 22 [10]) → quantum-teleportation
- Step 1: Alice applies CNOT (control = her unknown qubit, target = her EPR half) then H on her first qubit; the 3-qubit state is then written as a sum over her four basis outcomes ab of |ab⟩ times a state of Bob's qubit (§1.5, p. 22 [10]) → quantum-teleportation
- Step 2: Alice measures her two qubits in the computational basis and sends the two classical bits ab to Bob; the four outcomes are equally likely (¼ each, from the displayed decomposition) (§1.5, p. 22 [10]) → quantum-teleportation
- Step 3: Bob applies X if b = 1, then Z if a = 1; e.g. for ab = 11 his qubit is α₀|1⟩−α₁|0⟩ and X then Z recovers the original (§1.5, pp. 22-23 [10-11]) → quantum-teleportation
- If Alice's qubit was entangled with other qubits, teleportation preserves that entanglement: Bob's qubit is entangled in the same way (§1.5, p. 23 [11]) → quantum-teleportation
- Teleportation moves rather than copies the qubit (Alice's is destroyed); the introduction notes teleportation has been implemented experimentally as a limited quantum-communication application, defined as sending qubits using entanglement and classical communication (§1.5, p. 23 [11]; §1.1, p. 14 [2]) → quantum-teleportation
- The protocol is given as an early example of a circuit of elementary gates (CNOT, H, measurements and classically-controlled X, Z) (§1.5, p. 22 [10]; §2.1.2, p. 26 [14]) → quantum-teleportation
- Exercise 1.16: if Alice knows the rotation angle θ of the state, one EPR-pair plus 1 classical bit suffices for Bob to obtain |φ⟩, versus 2 bits for teleporting an unknown qubit (Ex. 1.16(d), p. 24 [12]) → quantum-teleportation

### Superdense coding
- Without entanglement, sending a qubit gives Bob at most one bit about Alice's message (footnote 10 attributes this to Holevo's theorem, Ch. 15); with a shared EPR-pair, one transmitted qubit can carry two classical bits (Ex. 1.14, p. 24 [12]) → superdense-coding
- Encoding: Alice, holding bits a, b and her half of an EPR-pair, applies X to her half if a = 1 and then Z if b = 1 (neither for 00, both for 11) (Ex. 1.14(a), p. 24 [12]) → superdense-coding
- Decoding: Alice sends her qubit to Bob, who applies CNOT and Hadamard and measures in the computational basis, getting a on the first qubit and b on the second (Ex. 1.14(b), p. 24 [12]) → superdense-coding
- The four states from the four Pauli operations I, X, Y, Z on Alice's half of an EPR-pair form an orthonormal set (hence perfectly distinguishable by a 4-outcome projective measurement by Bob) (Ex. 1.15(b)(c), p. 24 [12]) → superdense-coding
- Key tool: Tr((C⊗I)|ψ⟩⟨ψ|) = ½Tr(C) for an EPR-pair |ψ⟩ (Ex. 1.15(a), p. 24 [12]) → superdense-coding
- ⚠️ Superdense coding is presented only as an exercise (with a hint-free outline), not worked in the main text (Ex. 1.14, p. 24 [12]) → superdense-coding

### Bell inequalities
- Einstein wanted a "local realist" replacement for quantum mechanics (local: no faster-than-light influence; realist: definite properties); Bell in the 1960s devised entanglement experiments whose predicted outputs no local realist theory can reproduce ("quantum non-locality") (§17.1, pp. 157-158 [145-146]) → bell-inequalities
- Aspect and others did such experiments in the early 1980s with outcomes matching quantum mechanics; they disprove local realist theories rather than prove quantum mechanics, modulo experimental loopholes; one experiment simultaneously closed the two most important loopholes (§17.1, p. 158 [146], footnotes 2-3) → bell-inequalities
- Non-locality disproves the conjunction of locality and realism, not locality alone (footnote 3, §17.1, p. 158 [146]) → bell-inequalities
- Game formulation: Alice and Bob get inputs x, y, may not communicate, may share a classical random variable (local hidden variable, covering all local realist models) or entangled states, and must output a, b with a prescribed correlation (§17.1, p. 158 [146], Fig. 17.1) → bell-inequalities
- CHSH game: win iff a ⊕ b = x ∧ y (§17.2, p. 159 [147]) → bell-inequalities
- Classical bound: a deterministic strategy is fixed by four bits (a₀, a₁, b₀, b₁), and the four winning conditions sum mod 2 to 0 = 1, so at most 3 of 4 inputs can be won; shared randomness is a mixture of deterministic strategies, so 3/4 is the best classical probability (worst-case input), and 3/4 is achievable for every input (Ex. 17.4) (§17.2, p. 159 [147]) → bell-inequalities
- Quantum strategy: share (|00⟩−|11⟩)/√2; Alice rotates her qubit by R(−π/16) if x = 0 and R(3π/16) if x = 1, Bob does the same with y, both measure in the computational basis; the state becomes (cos(θ_A+θ_B)(|00⟩−|11⟩)+sin(θ_A+θ_B)(|01⟩+|10⟩))/√2, so a ⊕ b = 0 with probability cos²(θ_A+θ_B); θ_A+θ_B = ±π/8 when x∧y = 0 and 3π/8 when x∧y = 1, giving success cos²(π/8) ≈ 0.85 on all inputs (§17.2, p. 159 [147]) → bell-inequalities
- Upper bounds on the success probability of classical strategies for a game are called Bell inequalities; this particular one is the CHSH inequality (footnote 4, §17.2, p. 159 [147]) → bell-inequalities
- Tsirelson: cos²(π/8) is optimal for quantum strategies, even with arbitrary amounts of entanglement (§17.2, p. 160 [148]); Ex. 17.7 (p. 164 [152]) derives it by writing the winning probability as ½ + ⅛⟨ψ|C|ψ⟩ with C = A₀⊗B₀ + A₀⊗B₁ + A₁⊗B₀ − A₁⊗B₁ and showing ⟨ψ|C|ψ⟩ ≤ √8 → bell-inequalities
- Other non-local games: magic square game (classical best 8/9, quantum strategy with two EPR-type pairs always wins) and Mermin/GHZ game (classical at most 3/4, quantum wins with certainty) (§17.3, pp. 160-162 [148-150]; Ex. 17.5, p. 164 [152]) → bell-inequalities

## Not covered / level (qubits-and-circuits)
- Requested but not covered: bloch-sphere (no mention in Ch. 1-2). Explicit proofs of no-cloning and superdense coding are only exercises (no worked text). No statement that "most unitaries need exponentially many gates"; only the Boolean-function counting argument (§13.1). Gate Y/S and "phase gate S" are not defined in the main text.
- Claims per concept (this section): qubit 6 (one is a ⚠️ absence note), single-qubit-gates 8, multi-qubit-states 6, entanglement 7, two-qubit-gates 7, quantum-circuits 10, no-cloning 4 (one ⚠️), universal-gate-sets 9 (one ⚠️), quantum-teleportation 8, superdense-coding 6 (one ⚠️), bell-inequalities 10. bloch-sphere 0.
- Level: university (graduate-level lecture notes for theoretical-CS students); Ch. 1 is brief and terse, with several key results left as exercises.
