---
source: axler-2024
concepts: [complex-numbers, vectors-and-dirac-notation, inner-products-and-norms, matrices-and-linear-maps, unitary-and-hermitian-matrices, eigenvalues-and-eigenvectors, tensor-products]
---

Accessed: full text (Springer Open Access PDF, extracted text). Locations give the book's section and item number (e.g. "def. 6.2") plus the PDF page ("PDF p.", = book page + 18). Chapters 1-7 and §9D were read in the relevant parts; the rest of the book was not read.

Notation note: Axler writes F for R or C (def. 1.6) and works with abstract vector spaces and linear maps rather than with matrices. Nearly every theorem is stated for both F = R and F = C, and he points out where the two cases differ.

## Complex numbers (§1A, §4)

- A complex number is an ordered pair of reals written a+bi. Addition is componentwise. Multiplication is (a+bi)(c+di) = (ac-bd)+(ad+bc)i. The formula is motivated by assuming i^2 = -1 and using the usual arithmetic rules. He advises rederiving it rather than memorizing it (def. 1.1, ex. 1.2, §1A, PDF pp. 20-21) → complex-numbers
- C has the usual field properties: commutativity, associativity, identities, additive inverse, multiplicative inverse for nonzero numbers, and distributivity. Subtraction and division are defined from these (1.3, 1.5, §1A, PDF pp. 21-22) → complex-numbers
- Real part, imaginary part, conjugate and absolute value. Conjugate: conj(z) = Re z - (Im z)i. Absolute value: |z| = sqrt((Re z)^2 + (Im z)^2). Example: z = 3+2i has conjugate 3-2i and |z| = sqrt(13) (def. 4.1-4.3, §4 intro, PDF p. 138) → complex-numbers
- Identifying z with (Re z, Im z) identifies C with R^2. |z| is the distance from the origin. C is a 1-dimensional complex vector space and also a 2-dimensional real vector space. A number is real if and only if it equals its conjugate (§4 after 4.3, PDF p. 138; also §2C, PDF p. 63) → complex-numbers
- Identities of conjugate and absolute value: z + conj(z) = 2 Re z; z·conj(z) = |z|^2; conj(wz) = conj(w)·conj(z); |wz| = |w||z|; |conj(z)| = |z|; triangle inequality |w+z| <= |w|+|z| (4.4, PDF p. 139) → complex-numbers
- Fundamental theorem of algebra: every nonconstant polynomial over C has a zero in C, and so factors into degree-1 factors. The result is false over R (for example 1+x^2) and false over the rationals. Axler says this failure explains the differences between linear algebra over R and over C (4.12, 4.13, §4, PDF pp. 143-145) → complex-numbers
- Polynomials with real coefficients have their nonreal zeros in conjugate pairs (4.14, PDF p. 145) → complex-numbers
- Complex scalars matter for operators: every operator on a finite-dimensional nonzero complex vector space has an eigenvalue. A rotation of R^2 by 90 degrees has none over R, but over C it has eigenvalues i and -i (5.19, 5.9, PDF pp. 153-154, 161) → complex-numbers, eigenvalues-and-eigenvectors

## Vectors, vector spaces, basis, dimension (ch. 1-2)

Axler does not use Dirac (bra-ket) notation anywhere in the parts read. Vectors are written v, inner products as ⟨u,v⟩, and the adjoint as T*. The relation ⟨Tv,w⟩ = ⟨v,T*w⟩ (def. 7.1) plays the role of the bra-ket identity, but the book does not make that connection.

- F^n is the set of lists (x1..xn) of n elements of F. Addition and scalar multiplication are coordinatewise. C^n cannot be pictured, but algebra in it is as easy as in R^2 or R^3 (def. 1.11-1.13, 1.18, §1A, PDF pp. 24, 27) → vectors-and-dirac-notation
- A vector space over F is an abstract structure with addition and scalar multiplication. R^n is a vector space over R and C^n is one over C. Its elements need not be lists: they can be functions, sequences or polynomials. F^n is the motivating example (def. 1.22, ex. 1.23-1.25, §1B, PDF pp. 31-32) → vectors-and-dirac-notation
- A linear combination is a sum of scalar multiples a1v1+...+amvm. The span is the set of all linear combinations, and it is the smallest subspace containing the list (2.2, 2.4, 2.6, §2A, PDF pp. 46-47) → vectors-and-dirac-notation
- Linear independence: the only way to get 0 as a linear combination is with all coefficients 0. Equivalently, every vector in the span has exactly one representation (2.15, §2A, PDF p. 50) → vectors-and-dirac-notation
- A basis is a linearly independent list that spans V. A list is a basis if and only if every v can be written uniquely as a combination of it (2.26, 2.28, §2B, PDF p. 57). The standard basis of F^n has a 1 in the kth slot and 0 elsewhere (2.27, PDF p. 57) → vectors-and-dirac-notation
- Every finite-dimensional space has a basis. Every spanning list can be reduced to a basis, and every independent list can be extended to one (2.30-2.32, §2B, PDF pp. 58-59) → vectors-and-dirac-notation
- All bases of a finite-dimensional space have the same length. That common length is the dimension. dim F^n = n (2.34-2.36, §2C, PDF p. 62) → vectors-and-dirac-notation
- A linearly independent list of length dim V is automatically a basis, and a subspace of full dimension equals the whole space (2.38, 2.39, §2C, PDF p. 63) → vectors-and-dirac-notation
- Dimension depends on the scalar field. C has dimension 1 over C but 2 over R (§2C remark, PDF p. 63) → vectors-and-dirac-notation, complex-numbers

## Inner products and norms (ch. 6)

- Motivation: the norm of x in R^n is the square root of the sum of squares, and the dot product is x·y = sum of x_k y_k. For C^n the norm uses absolute values, ||z||^2 = sum |z_k|^2. So the inner product of w with z must conjugate one argument, and swapping the two arguments conjugates the result (§6A, PDF pp. 200-201) → inner-products-and-norms
- Definition 6.2: an inner product on V (over R or C) satisfies positivity, definiteness (⟨v,v⟩ = 0 only for v = 0), additivity and homogeneity in the first slot, and conjugate symmetry ⟨u,v⟩ = conj⟨v,u⟩ (def. 6.2, PDF p. 201) → inner-products-and-norms
- ⚠️ Convention. Axler is linear in the first slot and conjugate-linear in the second. He notes that many physicists use the opposite convention, with homogeneity in the second slot (note after 6.2, PDF p. 202). Quantum texts use the physics convention, so the learner must watch the order of arguments → inner-products-and-norms
- The Euclidean inner product on F^n is the sum of w_k times conj(z_k). Inner products also exist on function spaces, for example ∫fg on continuous functions on [-1,1] (ex. 6.3, PDF p. 202) → inner-products-and-norms
- The norm is ||v|| = sqrt⟨v,v⟩. Then ||v|| = 0 only for v = 0, and ||λv|| = |λ|·||v|| (def. 6.7, 6.9, PDF p. 204). Axler advises working with squared norms, which is easier (PDF p. 204) → inner-products-and-norms
- Orthogonal means ⟨u,v⟩ = 0. 0 is orthogonal to every vector and is the only vector orthogonal to itself. In R^2, ⟨u,v⟩ = ||u|| ||v|| cos θ, which is why orthogonal means perpendicular (def. 6.10, 6.11, PDF p. 205) → inner-products-and-norms
- Pythagorean theorem: if u and v are orthogonal, then ||u+v||^2 = ||u||^2 + ||v||^2. This holds in any inner product space (6.12, PDF p. 205) → inner-products-and-norms
- Orthogonal decomposition: for v ≠ 0, u = (⟨u,v⟩/||v||^2) v + w with w orthogonal to v (6.13, PDF p. 206) → inner-products-and-norms
- Cauchy-Schwarz: |⟨u,v⟩| <= ||u|| ||v||, with equality if and only if one vector is a scalar multiple of the other. It is proved from the orthogonal decomposition and the Pythagorean theorem. The triangle inequality ||u+v|| <= ||u||+||v|| follows (6.14, 6.17, PDF pp. 207-208) → inner-products-and-norms
- An orthonormal list has norm-1 vectors that are pairwise orthogonal. The standard basis of F^n is orthonormal (6.22, 6.23, PDF p. 215) → inner-products-and-norms
- ||a1e1+...+amem||^2 = |a1|^2+...+|am|^2 for an orthonormal list. Orthonormal lists are therefore linearly independent. An orthonormal list of length dim V is an orthonormal basis (6.24, 6.25, 6.28, PDF pp. 216-217) → inner-products-and-norms
- If e1..en is an orthonormal basis, then v = sum ⟨v,e_k⟩ e_k and ||v||^2 = sum |⟨v,e_k⟩|^2 (Parseval). The coefficients are just inner products, with no linear system to solve. This makes an n-dimensional inner product space behave like F^n (6.30, 6.31, PDF pp. 218-219) → inner-products-and-norms
- Gram-Schmidt turns a linearly independent list v1..vm into an orthonormal list e1..em with the same span at every step k. It subtracts from v_k its components along earlier vectors and then normalizes (6.32, PDF p. 219). Consequences: every finite-dimensional inner product space has an orthonormal basis, and every orthonormal list extends to one (6.35, 6.36, PDF pp. 220-221) → inner-products-and-norms
- Riesz representation: in finite dimensions, every linear functional φ on V has the form φ(u) = ⟨u,v⟩ for a unique v. It is proved using an orthonormal basis (6.42, PDF p. 223) → inner-products-and-norms

## Linear maps and matrices (ch. 3)

- A linear map T: V→W is additive and homogeneous (T(u+v) = Tu+Tv, T(λv) = λTv). L(V,W) is the set of such maps, and an operator is a linear map from V to V. Examples include the identity, zero and differentiation maps (def. 3.1-3.3, §3A, PDF pp. 70-71) → matrices-and-linear-maps
- A linear map is determined by what it does to a basis (linear map lemma 3.4, cited in §3C, PDF p. 87). Matrices are an efficient way to record those values (§3C, PDF p. 87) → matrices-and-linear-maps
- The matrix of T with respect to a basis v1..vn of V and a basis w1..wm of W is the m×n matrix whose kth column holds the coefficients of Tv_k in the w basis. It depends on T and on both bases. For F^n→F^m with the standard bases, the kth column is T applied to the kth standard basis vector (def. 3.31, PDF pp. 87-88) → matrices-and-linear-maps
- Matrix multiplication is defined so that the matrix of a composition equals the product of matrices, M(ST) = M(S)M(T). Entry (j,k) is row j of A times column k of B. It is not commutative (def. 3.41, 3.43, PDF pp. 91-92). Axler computes this as the motivation for the definition, with the same bases fixed throughout (3.81, PDF p. 109) → matrices-and-linear-maps
- Once bases are fixed, T↔M(T) is an isomorphism from L(V,W) to F^(m,n). Hence dim L(V,W) = (dim V)(dim W). M(Tv) = M(T)M(v), so every linear map can be viewed as matrix-times-column-vector. The matrix depends on the basis (3.71, 3.72, PDF p. 105; M(Tv) formula, PDF pp. 106-107) → matrices-and-linear-maps
- A theme Axler flags for later chapters is choosing a basis that makes the matrix as simple as possible (§3D after the M(Tv) result, PDF p. 107) → matrices-and-linear-maps
- Two finite-dimensional spaces over F are isomorphic if and only if they have the same dimension. Every n-dimensional space is isomorphic to F^n. An isomorphism is an invertible linear map, thought of as relabeling (3.69, 3.70, PDF pp. 104-105) → matrices-and-linear-maps, vectors-and-dirac-notation
- Change of basis. The matrix of the identity operator between two bases is invertible, and the two directions are inverses of each other (3.82). If A = M(T,(u)), B = M(T,(v)) and C = M(I,(u),(v)), then A = C^(-1) B C (3.84, §3D, PDF pp. 110-111). On an n-dimensional space, ST = I if and only if TS = I (3.68, PDF p. 103) → matrices-and-linear-maps
- The inverse of a product reverses the order: (AC)^(-1) = C^(-1) A^(-1) (§3D after 3.80, PDF p. 109) → matrices-and-linear-maps

## Eigenvalues and eigenvectors (ch. 5) and real eigenvalues (ch. 7)

- Motivation: study an operator by restricting it to invariant subspaces. A one-dimensional invariant subspace span(v) means Tv = λv for some scalar λ (§5A, PDF p. 152) → eigenvalues-and-eigenvectors
- Definitions 5.5 and 5.8: λ is an eigenvalue of T if Tv = λv for some nonzero v, and that v is an eigenvector. v = 0 is excluded because T0 = λ0 for every λ. Eigenvectors are exactly the nonzero elements of null(T - λI) (PDF pp. 152-153) → eigenvalues-and-eigenvectors
- In finite dimensions, λ is an eigenvalue if and only if T-λI is not injective, not surjective, and not invertible (5.7, PDF p. 153) → eigenvalues-and-eigenvectors
- Eigenvectors for distinct eigenvalues are linearly independent. So an operator has at most dim V distinct eigenvalues (5.11, 5.12, PDF p. 154) → eigenvalues-and-eigenvectors
- Existence over C: every operator on a finite-dimensional nonzero complex vector space has an eigenvalue. The proof uses the list v, Tv, ..., T^n v, which must be dependent, and then the fundamental theorem of algebra, with no determinants. Over R it fails (90-degree rotation, 5.9). Finite dimension is also necessary (multiplication by z on P(C), 5.20) (5.19, 5.20, PDF p. 161). Axler chose this determinant-free route on purpose and says it gives more insight into why eigenvalues exist (preface for instructors, PDF p. 14) → eigenvalues-and-eigenvectors
- Eigenspace E(λ,T) = null(T-λI). Eigenspaces for distinct eigenvalues form a direct sum, and the sum of their dimensions is at most dim V (5.52, 5.54, PDF p. 182) → eigenvalues-and-eigenvectors
- Diagonalizable means that T has a diagonal matrix in some basis. The diagonal entries are then the eigenvalues. Example: T(x,y) = (41x+7y, -20x+74y) is diagonal in the basis (1,4),(7,5) with entries 69 and 46 (5.48-5.51, PDF p. 181) → eigenvalues-and-eigenvectors
- Equivalent conditions for diagonalizability: V has a basis of eigenvectors; V is the direct sum of the eigenspaces; the eigenspace dimensions add up to dim V (5.55, PDF p. 183). With dim V distinct eigenvalues, T is diagonalizable (5.58, PDF p. 184) → eigenvalues-and-eigenvectors
- Not all complex operators are diagonalizable. T(a,b,c) = (b,c,0) has only the eigenvalue 0 and a 1-dimensional eigenspace (5.57, PDF p. 184). Over C, every operator has an upper-triangular matrix in some basis (5.47, PDF p. 178) → eigenvalues-and-eigenvectors
- Every eigenvalue of a self-adjoint operator is real, shown by λ||v||^2 = ⟨Tv,v⟩ = ⟨v,Tv⟩ = conj(λ)||v||^2. Axler says this is interesting only when F = C (7.12, PDF p. 251) → eigenvalues-and-eigenvectors, unitary-and-hermitian-matrices
- Every eigenvalue of a unitary operator has absolute value 1 (7.54, PDF p. 280) → eigenvalues-and-eigenvectors, unitary-and-hermitian-matrices
- Eigenvectors of a normal operator (for example a self-adjoint one) for distinct eigenvalues are orthogonal (7.22, PDF p. 256) → eigenvalues-and-eigenvectors, unitary-and-hermitian-matrices

## Adjoint, self-adjoint, normal, unitary, spectral theorem (ch. 7)

- The adjoint T* of T: V→W is the unique map with ⟨Tv,w⟩ = ⟨v,T*w⟩ for all v,w. Existence comes from the Riesz representation theorem. T* is linear (def. 7.1, 7.4, §7A, PDF pp. 246-247) → unitary-and-hermitian-matrices
- Properties: (S+T)* = S*+T*; (λT)* = conj(λ)T*; (T*)* = T; (ST)* = T*S*; I* = I; (T^(-1))* = (T*)^(-1). Because of the conjugate, T↦T* is conjugate-linear over C (7.5, PDF p. 248) → unitary-and-hermitian-matrices
- The conjugate transpose A* of a matrix has entries (A*)_jk = conj(A_kj). With respect to orthonormal bases, the matrix of T* is the conjugate transpose of the matrix of T. Caution: this can fail for non-orthonormal bases (def. 7.7, 7.9, PDF pp. 249-250) → unitary-and-hermitian-matrices
- Also, null T* = (range T)^⊥ and range T* = (null T)^⊥ (7.6, PDF p. 249) → unitary-and-hermitian-matrices
- Self-adjoint (Hermitian) means T = T*, equivalently ⟨Tv,w⟩ = ⟨v,Tw⟩ for all v,w. In an orthonormal basis, this means the matrix equals its conjugate transpose (def. 7.10, PDF p. 251; example 7.11). Analogy: the adjoint plays the role of complex conjugation, so self-adjoint operators correspond to real numbers (§7A, PDF p. 251) → unitary-and-hermitian-matrices
- Over C, T is self-adjoint if and only if ⟨Tv,v⟩ is real for every v. Over C, ⟨Tv,v⟩ = 0 for all v forces T = 0. Over R this fails (90-degree rotation) (7.13, 7.14, PDF p. 252) → unitary-and-hermitian-matrices
- Normal means TT* = T*T. Every self-adjoint operator is normal, but not conversely: the matrix [[2,-3],[3,2]] is normal and not self-adjoint. T is normal if and only if ||Tv|| = ||T*v|| for all v. A normal operator and its adjoint share the same eigenvectors (def. 7.18, 7.19, 7.20, 7.21(e), PDF pp. 253-255) → unitary-and-hermitian-matrices
- Over C, T is normal if and only if T = A+iB with A, B commuting self-adjoint operators (its "real and imaginary parts") (7.23, PDF p. 256) → unitary-and-hermitian-matrices
- Spectral theorem, intro. The nicest operators are those with an orthonormal basis of eigenvectors, which means a diagonal matrix in an orthonormal basis. The theorem says which operators these are, and Axler calls it probably the most useful tool for operators on inner product spaces. He notes it extends to certain infinite-dimensional spaces and is central in functional analysis (§7B intro, PDF p. 261) → unitary-and-hermitian-matrices
- Real spectral theorem: for F = R, T is self-adjoint if and only if T has a diagonal matrix in some orthonormal basis, if and only if V has an orthonormal basis of eigenvectors. The proof uses the minimal polynomial and Schur's theorem (7.29, PDF p. 263; 7.27, PDF p. 262) → unitary-and-hermitian-matrices
- Complex spectral theorem: for F = C, T is normal if and only if V has an orthonormal basis of eigenvectors, if and only if T has a diagonal matrix in some orthonormal basis. The proof starts from Schur's theorem (every complex operator is upper-triangular in some orthonormal basis, 6.38). Normality (||Te_k|| = ||T*e_k||) then forces the off-diagonal entries to vanish (7.31, PDF p. 264; 6.38, PDF p. 222) → unitary-and-hermitian-matrices
- Example of the complex theorem: the normal operator with matrix [[2,-3],[3,2]] has orthonormal eigenbasis (i,1)/√2 and (-i,1)/√2, with eigenvalues 2+3i and 2-3i. It is not self-adjoint, so its eigenvalues are not real (ex. 7.33, PDF p. 265) → unitary-and-hermitian-matrices, eigenvalues-and-eigenvectors
- Isometry means a linear map that preserves norms, ||Sv|| = ||v||, and it is therefore injective. Equivalent conditions: S*S = I; ⟨Su,Sv⟩ = ⟨u,v⟩ (inner products preserved); S maps an orthonormal basis to an orthonormal list; the columns of its matrix (in orthonormal bases) are orthonormal (def. 7.44, 7.49, PDF pp. 276-277) → unitary-and-hermitian-matrices
- A unitary operator is an invertible isometry of V to itself. Equivalent conditions: S*S = SS* = I; S^(-1) = S*; S maps an orthonormal basis to an orthonormal basis; the rows (and columns) of its matrix in an orthonormal basis are orthonormal; S* is unitary (def. 7.51, 7.53, PDF pp. 278-279) → unitary-and-hermitian-matrices
- A unitary matrix is an n×n matrix whose columns form an orthonormal list in F^n. Equivalently its rows are orthonormal, ||Qv|| = ||v|| for all v, and Q*Q = QQ* = I (def. 7.56, 7.57, PDF p. 281). A rotation matrix [[cos θ, -sin θ],[sin θ, cos θ]] is unitary (ex. 7.52, PDF p. 278) → unitary-and-hermitian-matrices
- Unitary operators correspond to the unit circle in C (|z| = 1 ⇔ conj(z)z = 1). Over C, S is unitary if and only if V has an orthonormal basis of eigenvectors whose eigenvalues all have absolute value 1. This follows from the complex spectral theorem, because unitary operators are normal (7.54, 7.55, PDF p. 280) → unitary-and-hermitian-matrices
- Analogy table in Axler: complex z ↔ operator S; conj(z) ↔ S*; real ↔ self-adjoint; nonnegative reals ↔ "positive" operators; unit circle ↔ unitary (§7D, PDF p. 280) → unitary-and-hermitian-matrices

## Tensor products (§9D)

- Motivation: form a product v⊗w of a vector from V and one from W. It should be distributive, satisfy λ(v⊗w) = (λv)⊗w = v⊗(λw), and send bases e_j and f_k to a basis {e_j⊗f_k}. So dim(V⊗W) should be (dim V)(dim W). The Cartesian product V×W has dimension dim V + dim W, so it does not serve (§9D intro, PDF p. 388) → tensor-products
- Axler's definition is V⊗W := B(V',W'), the bilinear functionals on the dual spaces, with (v⊗w)(φ,τ) = φ(v)τ(w). This definition is basis-free. He remarks that the choice looks abstract and that "the important point is the behavior of these objects" (def. 9.71, PDF pp. 389-390, 372) → tensor-products
- dim(V⊗W) = (dim V)(dim W) (9.72, PDF p. 390). The map v⊗w is bilinear (9.73, PDF p. 390) → tensor-products
- If e1..em is a basis of V and f1..fn a basis of W, then {e_j⊗f_k} is a basis of V⊗W (9.74, PDF p. 391) → tensor-products
- Not every element of V⊗W has the form v⊗w. For dim V > 1 and dim W > 1, the pure tensors are a proper subset, and general elements are finite sums of them (remark after 9.74, citing Exercise 4, PDF p. 391). Representations as sums of pure tensors are not unique (PDF p. 394) → tensor-products
- In F^m⊗F^n, the coordinates of v⊗w in the basis {e_j⊗f_k} are the products v_j w_k. They can be arranged as the m×n matrix with entries v_j w_k (ex. 9.76, PDF p. 392) → tensor-products
- Universal property: every bilinear map Γ: V×W→U corresponds to a unique linear map on V⊗W with Γ̂(v⊗w) = Γ(v,w), and conversely (9.79, PDF p. 393) → tensor-products
- For inner product spaces V and W, there is a unique inner product on V⊗W with ⟨v⊗w, u⊗x⟩ = ⟨v,u⟩⟨w,x⟩. Hence ||v⊗w|| = ||v|| ||w|| (9.80, 9.82, PDF pp. 394-395) → tensor-products, inner-products-and-norms
- If {e_j} and {f_k} are orthonormal bases, then {e_j⊗f_k} is an orthonormal basis of V⊗W (9.83, PDF p. 395) → tensor-products
- Multiple factors: V1⊗...⊗Vm is defined analogously from m-linear functionals, with dim = product of the dim V_k. Axler gives only definitions and statements here and leaves the proofs to the reader (9.85-9.88, PDF pp. 396-397) → tensor-products

## Not covered / level

- Concepts requested but not covered: probability-basics. The table of contents shows no probability material.
- Hermitian terminology: Axler says "self-adjoint" and does not use "Hermitian" in the parts read. Unitary "matrix" appears only in §7D (def. 7.56).
- Level: university (second course in linear algebra, proof-oriented, general F = R or C). It is abstract-first, with no Dirac notation, no tensor products of operators or Kronecker products (only an exercise mentioned in 9D), and no physics context.
