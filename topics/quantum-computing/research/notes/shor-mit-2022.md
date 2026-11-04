---
source: shor-mit-2022
concepts: [query-model-and-oracles, deutsch-jozsa, bernstein-vazirani-and-simon, quantum-fourier-transform, phase-estimation, shor-algorithm, grover-search, hamiltonian-simulation, quantum-complexity, post-quantum-cryptography, phase-kickback]
---

Accessed: extracted text of lecture notes L16-L26 (Shor, MIT 8.370/18.435, Fall 2022); pages are those of each lecture's own numbering. Level: university. Notes are terse and contain several typos (flagged below).

## Hadamard transform, oracles, Deutsch-Jozsa (L16)

- The Hadamard transform is H applied to each of n qubits; on |0^n> it gives the uniform superposition of all 2^n basis strings with amplitude 2^(-n/2) (L16, p. 1) → deutsch-jozsa
- On a general basis state, H^(⊗n)|j> = 2^(-n/2) sum_k (-1)^(j·k)|k>, where j·k counts positions where both strings have a 1; the sign comes from the |1> terms carrying a minus (L16, pp. 1-2) → deutsch-jozsa
- Definitions: f is constant if f(x)=f(y) for all x,y; balanced if it gives 0 and 1 equally often. The DJ problem promises f is one of these and asks which (L16, p. 2) → deutsch-jozsa
- Classical deterministic cost: you need 2^(n-1)+1 evaluations (one more than half), by the urn argument; seeing 2^(n-1) equal values does not rule out a non-constant f (L16, p. 2) → deutsch-jozsa
- ⚠️ Inconsistent: p. 4 later says the best deterministic classical algorithm takes "around 2^(n/2)" queries/gates; the exact figure derived on p. 2 is 2^(n-1)+1 (L16, pp. 2, 4) → deutsch-jozsa
- A phase oracle maps |x> to (-1)^f(x)|x>; a bit oracle maps |x>|0> to |x>|f(x)> with the answer in a separate register (L16, p. 2) → query-model-and-oracles
- A phase oracle can be built from a bit oracle: compute f(x) into an ancilla, apply Z to it to get (-1)^f(x), then uncompute f; the ancilla returns to |0>. The notes say the two oracle types are in fact equivalent but do not prove it (L16, pp. 2-3) → query-model-and-oracles
- In the circuit "compute, Z on the ancilla, uncompute", the information about f(x) is moved into the phase of the input register (L16, pp. 2-3) → phase-kickback
- DJ algorithm: start |0^n>, apply H^(⊗n), apply the phase oracle, apply H^(⊗n), measure (L16, p. 3) → deutsch-jozsa
- Analysis: final amplitude of |0^n> is 2^(-n) sum_j (-1)^f(j) (since j·0=0). Constant f gives probability 1 of seeing |0^n>; balanced f gives amplitude 0. So output 0^n means constant, anything else means balanced (L16, pp. 3-4) → deutsch-jozsa
- Cost: one oracle call and a number of gates linear in n, versus the classical deterministic cost: an exponential separation for deterministic algorithms (L16, p. 4) → deutsch-jozsa
- Shor's own caveat: DJ is not a convincing proof of quantum advantage, since a randomized classical algorithm with 20-30 queries errs with tiny probability. Its importance is that it led to Simon's algorithm (L16, p. 4) → deutsch-jozsa
- The same caveat frames the query-complexity comparison: deterministic vs randomized classical query counts differ, and the quantum advantage must be assessed against randomized algorithms (L16, p. 4) → query-model-and-oracles

## Classical complexity (L17)

- "Efficient" is conventionally equated with polynomial time in the input length n. Shor says this is an imperfect proxy: n^24 is impractical, while the simplex algorithm is exponential in the worst case but fast in practice (L17, p. 1) → quantum-complexity
- Motivation for polynomial time: different machine models (Turing machine, RAM) differ by only polynomial factors, so the class P is model-independent (Cobham) (L17, p. 1) → quantum-complexity
- BPP is the class solvable with high probability by a polynomial-time randomized algorithm; it contains P, though it is not proved larger and some think they are equal (L17, p. 1 and footnote) → quantum-complexity
- BQP is the class solvable with high probability by a quantum computer in polynomial time. The bounded-error (randomized) version is the natural one because quantum computation is inherently probabilistic; deterministic quantum classes depend on model details (L17, p. 1) → quantum-complexity
- NP is the class of problems with a polynomial-time verifier taking the instance plus a "witness". It must reject every instance without the property, and for each instance with it, some witness must be accepted. Example: 3-colorability, with a coloring as the witness (L17, pp. 1-2) → quantum-complexity
- NP-complete problems are those such that a polynomial-time solution would solve all of NP. 3-SAT is the master problem; 3-colorability is shown NP-complete by mapping any 3-SAT formula to a polynomially larger graph that is 3-colorable iff the formula is satisfiable (L17, p. 2) → quantum-complexity
- Belief: BQP is not contained in NP, and quantum computers are not believed to solve NP-complete problems in polynomial time, so BQP and NP are thought incomparable (Venn diagram with co-NP, PSPACE, EXPTIME) (L17, p. 3) → quantum-complexity
- Quantum PSPACE equals PSPACE, so quantum computing cannot reduce space needs by more than a polynomial factor (L17, p. 3) → quantum-complexity
- Only P ≠ EXPTIME is provable among the diagram's classes, which shows how hard separating complexity classes is (L17, p. 3) → quantum-complexity

## Simon's algorithm (L18)

- Simon's problem: f maps n-bit strings to n-bit strings, is 2-to-1, and f(x)=f(x⊕c) for a hidden string c; find c. It was invented to show quantum can beat classical, not from an application (L18, p. 1) → bernstein-vazirani-and-simon
- Classical: finding a collision x1,x2 with f(x1)=f(x2) gives c=x1⊕x2. After t queries, at most t(t-1)/2 candidate values of c are eliminated, so certainty needs t ≈ 2^((n+1)/2); the median randomized cost is also about 2^(n/2) (L18, pp. 1-2) → bernstein-vazirani-and-simon
- Oracle for Simon: O_f|x>|z> = |x>|z⊕f(x)>, which is reversible (L18, p. 2) → query-model-and-oracles
- Algorithm: two n-qubit registers in |0>, apply H^(⊗n) to the first, apply O_f, apply H^(⊗n) to the first, measure (the first register is the one used) (L18, p. 2) → bernstein-vazirani-and-simon
- Analysis: only j and j⊕c give the same f value, so the amplitude of |k>|f(j)> is 2^(-n)(-1)^(j·k)(1+(-1)^(c·k)). Each measured k satisfies c·k=0 (mod 2), and every such k is equally likely (probability 1/2^(n-1)) (L18, pp. 3-4) → bernstein-vazirani-and-simon
- Repeating collects n-1 linearly independent vectors perpendicular to c; solving by Gaussian elimination over Z_2 (row-echelon form, then back-substitution, choosing the free coordinate so c is nonzero) determines c. Worked example gives c=01010 (L18, pp. 4-5) → bernstein-vazirani-and-simon
- Over Z_2 a vector can be perpendicular to itself (e.g. 1010011·1010011=0 mod 2), unlike over R or C (L18, p. 4) → bernstein-vazirani-and-simon
- Cost: the probability that the i-th sample is dependent on the previous ones is below 1/2, so the expected number of samples is under 2n and total time is O(n^2); a finer analysis gives under n+2 expected samples. Classical is at least about 2^(n/2): an exponential advantage (L18, p. 5) → bernstein-vazirani-and-simon
- Why the oracle matters even though the second register is never looked at: without it the two H layers cancel (H^2=I). This is explained by "back action" (L18, p. 5) → phase-kickback
- Back action: CNOT on |->|-> leaves the target unchanged and changes the control, giving |+>|-> (L18, p. 6) → phase-kickback
- Identities: HσzH=σx and HσxH=σz; a CNOT sandwiched between H on both qubits equals a controlled-Z, which is symmetric in control and target, hence H⊗H·CNOT·H⊗H reverses the CNOT's direction (L18, pp. 6-7) → phase-kickback
- General principle stated: if system A affects system B, B also affects A; consequently a quantum system cannot be measured without disturbing it (L18, p. 7) → phase-kickback
- ⚠️ The notes do not use the name "phase kickback" nor derive the standard |x>|-> → (-1)^f(x)|x>|-> form. Closest material is the ancilla-Z construction (L16) and "back action" (L18). Bernstein-Vazirani is not treated in L16-L26 as a separate algorithm (L18) → bernstein-vazirani-and-simon

## Quantum Fourier transform (L19-L20)

- The DFT/FFT relation: the QFT is the DFT acting on the amplitudes (the DFT takes input amplitudes to output amplitudes); the FFT shares structure with the QFT circuit. The DFT/Fourier series background is omitted from the notes (L19, p. 1) → quantum-fourier-transform
- Definition: with n=2^L, QFT |j> → n^(-1/2) sum_k e^(2πi jk/n)|k>; the inverse uses e^(-2πi jk/n). Matrix entries are ω^(jk)/√n with ω=e^(2πi/n); the inverse is the same with ω→ω^(-1) (L19, p. 1) → quantum-fourier-transform
- Unitarity follows from sum_k ω^(kl) = n if l is a multiple of n, else 0 (geometric series with ω^n=1) (L19, pp. 1-2) → quantum-fourier-transform
- Applications named: phase estimation, factoring and discrete log (L19, p. 1) → quantum-fourier-transform
- Gate decomposition: only Hadamards and controlled-R_j gates are needed, with R_j = diag(1, e^(2πi/2^j)), j=2..L (L19, p. 2) → quantum-fourier-transform
- Product form: with binary fractions 0.a1a2…, QFT|j1…jL> = 2^(-L/2) ⊗ (|0> + e^(2πi 0.j_s j_{s+1}…j_L)|1>), s running over the qubits. Derivation is in L20 pp. 1-2: substitute the binary expansions of j and k, drop integer multiples of 2πi in the exponent, and factor the sum over k as a tensor product (L19, p. 2; L20, pp. 1-2) → quantum-fourier-transform
- Circuit: for qubit s, apply H (giving phase 0.j_s) then controlled-R_2, R_3, … from the later qubits j_{s+1}…j_L to extend to 0.j_s…j_L. Qubits must be processed in order so later ones are still available; output qubits come out in reversed order. The notes show L=4 and refer to the textbook p. 219 for the general case (L19, pp. 2-3) → quantum-fourier-transform
- The reversed circuit gives the inverse QFT, which is the complex conjugate of the QFT (L19, p. 4) → quantum-fourier-transform
- Controlled-R_l for large l is very close to the identity, so dropping those gates gives a good approximate QFT with far fewer gates (L19, p. 4) → quantum-fourier-transform
- ⚠️ The notes give no explicit gate count (about L^2/2 controlled rotations + L Hadamards follows from the circuit shape but is not stated) and do not discuss FFT's N log N cost → quantum-fourier-transform

## Phase estimation (L20)

- Problem: given unitary U and eigenvector |v_θ> with U|v_θ>=e^(iθ)|v_θ>, approximate θ. Accuracy requires being able to compute high powers U^(2^l) efficiently (L20, p. 2) → phase-estimation
- Example where powers are cheap: U multiplies s by g mod p, so U^k just multiplies by g^k mod p (L20, p. 2) → phase-estimation
- Idea: create 2^(-L/2) sum_k e^(ikθ)|k>. If θ=2πm/2^L this is a QFT basis state, so applying the inverse QFT and measuring in the standard basis gives j with θ=2πj/2^L (L20, pp. 2-3) → phase-estimation
- Circuit: L control qubits each in |+>, controlled-U, U^2, U^4, …, U^(2^(L-1)) acting on |v_θ>, so for k=k_{L-1}…k_0 the eigenvector receives U^k and the phase e^(ikθ) is imprinted on |k> (L20, p. 3) → phase-estimation
- Phase imprinted onto the control register by controlled-U^k acting on an eigenvector is the kickback mechanism that phase estimation relies on (L20, p. 3) → phase-kickback
- Accuracy when θ is not a multiple of 2π/2^L: the probability of j is a geometric-sum expression bounded by about 1/(π α)^2 for outcomes j more than α from j'=2^L θ/(2π); so j is tightly concentrated around the true value. Shor says more precise analyses exist (L20, p. 4) → phase-estimation
- The eigenvector is left unchanged by the phase estimation circuit, which matters for later applications (L20, p. 4) → phase-estimation
- Factoring and discrete log are presented via phase estimation, rather than the original direct use of the QFT (L20, p. 1) → phase-estimation

## Shor's algorithm (L21-L23)

- Historical/context: the first quantum algorithm to draw wide attention, since internet security (RSA) depends on factoring hardness (L21, p. 1) → shor-algorithm
- Discovery: Simon's algorithm finds periods over Z_2^n (f(x)=f(x⊕c)) with the Hadamard transform, which is the Fourier transform over Z_2^n; factoring needs period finding over Z (f(x)=f(x+c)), using the Fourier transform over Z_{2^n}. Shor says the real discovery was more convoluted (L21, p. 1) → shor-algorithm
- Reduction to a square-root-of-1 problem: find A,B with A^2≡B^2 (mod N) but A≢±B; then N divides (A-B)(A+B) but neither factor, so P divides one and Q the other, and gcd(N, A-B) gives a prime factor. This is also what the quadratic sieve does (L21, p. 1) → shor-algorithm
- Order finding: for a coprime to N, the sequence a^k mod N is periodic with period r, a^r≡1 (mod N). If r is even, (a^(r/2))^2≡1; if a^(r/2)≢-1, we get a factor via gcd. Otherwise retry with another a (L21, pp. 1-2; L22, p. 1) → shor-algorithm
- Examples with N=33: a=2 has r=10 but 2^5+1=33, so fails; a=5 has r=10 and 5^5≡23, with 22 divisible by 11 and 24 by 3, so it succeeds (L21, p. 2; L22, p. 1) → shor-algorithm
- The Euclidean algorithm computes gcds by repeated remainders; the extended Euclidean algorithm back-substitutes to find inverses (example 5^(-1)≡20 mod 33) (L22, pp. 1-2) → shor-algorithm
- ⚠️ In the Euclidean-algorithm example the text says "gcd(24, 9)" but the table shown computes gcd(33, 24)=3 (L22, p. 1) → shor-algorithm
- U_a|y mod N> = |ay mod N> is made reversible by combining a classical circuit for multiplication by a and one for a^(-1) (found by extended Euclid) (L21, p. 2; L22, p. 2) → shor-algorithm
- U_a^(2^k)=U_(a^(2^k) mod N), where a^(2^k) mod N is computed classically by repeated squaring, so phase estimation applies (L21, pp. 2-3) → shor-algorithm
- Eigenvectors of U_a: |ζ_k> = r^(-1/2) sum_s e^(2πi ks/r)|a^s mod N> (eigenvalue e^(-2πik/r) as written), r of them; and |1> = r^(-1/2) sum_k |ζ_k>. So phase estimation started on |1> returns a random k/r estimate, with the register left near |ζ_k> (L21, p. 3) → shor-algorithm
- For an L-bit N use phase estimation with 2L qubits, because k and r each have at most L bits and 2L bits of k/r are needed to identify them; the result d/2^(2L) is close to k/r (L21, p. 3) → shor-algorithm
- The continued fraction algorithm converts d/2^(2L) into k/r. Worked example: 615/2048 has continued-fraction terms 3,3,33,1,5; convergents 1/3, 3/10, 100/333; denominator 333 is too large for N=33, so 3/10 gives r=10 (L22, pp. 3-4) → shor-algorithm
- Theorem: if |R - p/q| ≤ 1/(2q^2) then p/q is a convergent of R (proved via a lemma on neighbouring fractions with p'q - pq' = 1 and the mediant (p+p')/(q+q')) (L22, pp. 4-7) → shor-algorithm
- ⚠️ L22 p. 3 says "L ≈ 2 log N" and then "2L = 2048", mixing L and 2^L notation for the number of bits/size; read as using a register with 2^(2L)≈2048 states, consistent with L21 (L22, p. 3) → shor-algorithm
- Chinese remainder theorem: for coprime P,Q, residues mod N=PQ correspond one-to-one to pairs (mod P, mod Q). The order r is the lcm of r_P and r_Q (L22, pp. 7-8) → shor-algorithm
- Success probability: a random a yields a factor (r even and a^(r/2)≠-1) with probability at least 1/2, since failure requires the powers of 2 dividing r_P(a) and r_Q(a) to be equal, which has probability at most 1/2 (L22, p. 8) → shor-algorithm
- ⚠️ Typos in L22 worked examples (e.g. "53 mod 77" vs "60 mod 77", "mod 11" where mod 7 intended); the argument itself is as stated above (L22, pp. 7-8) → shor-algorithm
- Discrete log (L23): for a prime P with generator g, every nonzero h equals g^x mod P; find x. Example: 2 is a generator mod 11, 3 is not (3^5≡1). No formal reduction to factoring exists, but each improvement for one has been followed by an analogue for the other; both support public-key cryptography (L23, p. 1) → shor-algorithm
- Quantum discrete log via phase estimation on two unitaries: U_g:|y>→|gy> has eigenvectors |v_k> = (P-1)^(-1/2) sum_l e^(2πikl/(P-1))|g^l> with eigenvalue e^(-2πik/(P-1)); |1> is the uniform sum of the |v_k>. Phase estimation gives a random k and its eigenvector. Shor notes this presentation differs from the original and from Nielsen-Chuang (L23, pp. 2-3) → shor-algorithm
- |v_k> is also an eigenvector of U_h (h=g^x) with eigenvalue e^(-2πikx/(P-1)); a second phase estimation on |v_k> gives kx mod (P-1). If gcd(k,P-1)=1, x = k^(-1)(kx) mod (P-1); otherwise rerun. Example: P=31, g=3, k=7, kx=12 gives x=6, and 3^6≡16 (L23, p. 4) → shor-algorithm
- Precision: take 2^L at least a small factor larger than P (about 20P suffices, 2P probably does not) (L23, p. 3) → shor-algorithm
- Test of whether g is a generator mod P: compute the period of g^k and check it is P-1; Shor says there is no efficient classical test, but Diffie-Hellman only needs something that looks like a generator (L23, p. 1) → shor-algorithm
- ⚠️ The notes give no overall polynomial gate-count statement for factoring (only that the number of trials is polynomial/expected constant and each step is efficient) → shor-algorithm

## Cryptography (L21, L23)

- RSA: the receiver publishes N=PQ (two large primes) and encoding needs only N; decoding needs P and Q. This allows secure communication over a public channel without a prior shared secret, and its security rests on the hardness of factoring (L21, p. 1) → post-quantum-cryptography
- Quantum factoring therefore matters because RSA's security depended on factoring hardness; this is why the algorithm attracted attention (L21, p. 1) → post-quantum-cryptography
- Diffie-Hellman key exchange: Alice and Bob agree on a prime P and generator g, pick secrets x and y, exchange g^x and g^y mod P, and both compute g^(xy). An eavesdropper who could take discrete logs could recover x and then the key (L23, pp. 1-2) → post-quantum-cryptography
- It is unproven that recovering g^(xy) from g, g^x, g^y is as hard as discrete log, but nobody knows how, and most cryptographers believe breaking DH would also give discrete logs (L23, p. 2) → post-quantum-cryptography
- Discrete log and factoring are both used for public-key cryptosystems, so the quantum discrete-log algorithm (L23) extends the threat to Diffie-Hellman-type schemes (L23, p. 1) → post-quantum-cryptography
- ⚠️ L21-L26 do not discuss post-quantum schemes, key sizes, or timelines; implications are only stated as above → post-quantum-cryptography

## Grover search (L24-L25)

- Grover searches a space of size N for a solution in about √N steps (L24, p. 1) → grover-search
- Motivating example: finding three integers whose cubes sum to 42 (found by Booker and Sutherland using about a million computer hours with a clever classical algorithm); brute force over x,y would need about 10^34 candidates for 17-digit numbers, while Grover would need about 10^17 (L24, p. 1) → grover-search
- Shor adds that clever classical techniques can be combined with Grover ideas for further savings (L24, p. 1) → grover-search
- Oracle: a phase oracle O_p|x> = -|x> if x is a solution, |x> otherwise; built from a checking circuit by setting a flag qubit, applying σz, and uncomputing (L24, p. 1) → query-model-and-oracles
- The search space is labelled 0..N-1, and N may be padded to a power of 2 with dummy elements without greatly changing the running time. Start state is the uniform superposition |ψ> (L24, p. 1) → grover-search
- Grover iteration: (1) oracle O_p, (2) H^(⊗n), (3) 2|0><0|-I, (4) H^(⊗n). Step 3 gives phase +1 on |0> and -1 elsewhere, constructible from Toffoli, σx and σz gates (L24, p. 2) → grover-search
- Steps 2-4 together equal 2|ψ><ψ|-I, which reflects all amplitudes about their average; the oracle step reflects the marked amplitude about 0 (L24, pp. 2-3) → grover-search
- Grover's original intuition: the marked amplitude starts at 1/√N; after the first reflection it is -1/√N, after reflecting about the average (≈1/√N) it becomes 3/√N, and after k iterations about (2k+1)/√N, so O(√N) steps suffice (L24, p. 3) → grover-search
- Geometric picture (textbook-style analysis): with M marked states, define |α> (uniform over unmarked) and |β> (uniform over marked); |ψ> = √((N-M)/N)|α> + √(M/N)|β>, and the state stays in span{|α>,|β>}. The angle θ/2 between |α> and |ψ> has sin(θ/2)=√(M/N), so θ≈2√(M/N) for M≪N (L24, pp. 3-4) → grover-search
- The oracle acts as a reflection (|α>→|α>, |β>→-|β>) and 2|ψ><ψ|-I as a reflection about |ψ>; two reflections whose lines meet at angle φ compose to a rotation by 2φ, so each iteration rotates the state by about θ toward |β> (L24, pp. 4-5) → grover-search
- Number of iterations: about (π/2)/θ ≈ (π/4)√(N/M) (L24, p. 5) → grover-search
- Unknown M: running a random number of iterations (sufficiently large) gives about a 1/2 chance of a marked state. Use random iteration counts in doubling ranges (5-10, 10-20, 20-40, …) to find a marked state in O(√(N/M)) total iterations (L24, p. 5) → grover-search
- ⚠️ The sum in the definition of |ψ> in L24 p. 1 starts at i=1 (typo; it should start at 0 as on p. 2) → grover-search
- Lower bound (L25): for an oracle O_x marking one of N basis states, any algorithm that always outputs x must call the oracle on the order of √N times; first shown for success probability 1, then extended to 1-ε. The proof was developed independently, motivated by whether quantum computers could solve NP-complete problems, and published after Grover's paper (L25, p. 1) → grover-search
- Model: by deferred measurement, an algorithm is alternating unitaries U_j and oracle calls O_x (padding with dummy calls). Compare |ψ_x^k> with the no-oracle run |ψ^k>, and define D_k = sum_x ||ψ_x^k> - |ψ^k>||^2 (L25, p. 1) → grover-search
- Upper bound by induction: D_(k+1) ≤ D_k + 4√D_k + 4 (using unitarity, (O_x-I)|ψ> = -2<x|ψ>|x> and Cauchy-Schwarz), hence D_k ≤ 4k^2 (L25, pp. 2-3) → grover-search
- Lower bound: if the final states for all N values of x are orthonormal, D_t ≥ 2N - 2√N (the minimizing common vector is the uniform superposition of the |e_i>). Combining the two bounds shows t is of order √N (L25, p. 3) → grover-search
- ⚠️ The text states D_t ≤ 2t^2 and concludes t > √N - 1, but the preceding induction gives D_k ≤ 4k^2, which would give t ≳ √(N/2); constants inconsistent, order √N unaffected (L25, p. 3) → grover-search
- Even requiring success only with probability 1/2 still needs order √N queries; the proof is deferred to Nielsen and Chuang (L25, p. 3) → grover-search
- Grover is thus asymptotically optimal for unstructured search (L25, p. 1) → grover-search
- Query-complexity use: lower bounds are proved in the oracle (black-box) model, counting calls to O_x, and show a limit independent of the circuit around it (L25, pp. 1-2) → query-model-and-oracles

## Hamiltonian simulation (L26)

- Continuous quantum dynamics differ from the circuit model: time is continuous and everything evolves simultaneously (L26, p. 1) → hamiltonian-simulation
- Schrödinger equation d/dt|ψ> = -iH|ψ> (ħ=1), with solution |ψ(t)> = e^(-iHt)|ψ(0)>. Derived by assuming linear first-order dynamics d|ψ>/dt = A|ψ> and requiring norm conservation, which forces A†=-A, so H=iA is Hermitian (L26, pp. 1-2) → hamiltonian-simulation
- Adding a multiple of the identity to H only adds a global phase, so only relative energies matter; a qubit Hamiltonian can be taken as v·σ (L26, p. 2) → hamiltonian-simulation
- Naive simulation for a small step: e^(-iHΔt) ≈ I - iHΔt via Taylor expansion; alternatively expand in eigenstates of H, each picking up e^(-iEt) (L26, pp. 2-3) → hamiltonian-simulation
- Transverse Ising model, H = sum σz_j σz_{j+1} - g sum σx_j, is a local Hamiltonian (a sum of terms each acting on few qubits). It splits as A+B with all terms in A commuting and all terms in B commuting (L26, p. 3) → hamiltonian-simulation
- If all local terms commute, the unitaries e^(-iH_j t) can be applied sequentially in any order exactly (L26, p. 3) → hamiltonian-simulation
- First-order Trotter: e^(-i(A+B)t) and e^(-iAt)e^(-iBt) differ at order t^2 through the commutator [A,B]; for small t the error is small (L26, pp. 3-4) → hamiltonian-simulation
- Splitting time t into L steps, (e^(-iAt/L)e^(-iBt/L))^L approximates the true evolution with error O(t^2/L), using the operator norm and its triangle-type property for products, so L=O(t^2/ε) steps give error ε (L26, p. 4) → hamiltonian-simulation
- ⚠️ The text writes the commutator and some exponentials without the i in places (e.g. e^(-(A+B)t)); sign and factor conventions are typos, the conclusion is unaffected (L26, pp. 3-4) → hamiltonian-simulation
- Second-order Trotter-Suzuki: repeat e^(-iAt/2)e^(-iBt)e^(-iAt/2); the error per step is O(t^3), so with L steps the error is O(t^3/L^2) and L=O(t^(3/2)/ε^(1/2)). Higher orders exist but get more complicated (L26, pp. 4-5) → hamiltonian-simulation

## Not covered / level
- Concepts requested but not covered in L16-L26: Bernstein-Vazirani as a distinct algorithm (only Simon is treated; BV and L16-style Hadamard transform lemma are the only related items); a named "phase kickback" derivation (only the ancilla-Z construction and "back action" discussion); explicit QFT gate count and FFT cost comparison; post-quantum cryptography proper (only RSA/Diffie-Hellman vulnerability context); Hamiltonian-simulation cost beyond Trotter step counts (no gate counts, no qubitization).
- Source level: university (graduate/advanced undergraduate lecture notes).
