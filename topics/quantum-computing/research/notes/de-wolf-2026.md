---
source: de-wolf-2026
concepts: [complex-numbers, vectors-and-dirac-notation, inner-products-and-norms, matrices-and-linear-maps, unitary-and-hermitian-matrices, eigenvalues-and-eigenvectors, tensor-products, probability-basics]
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
