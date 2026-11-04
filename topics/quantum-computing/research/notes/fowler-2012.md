---
source: fowler-2012
concepts: [surface-code, stabilizer-formalism, decoding, fault-tolerant-gates, resource-estimation]
---

Accessed: full text of the arXiv version (PRA 86, 032324; 54 pp., dated 26 Oct 2012), via the extracted text file. Page numbers are PDF pages. All numbers are 2012 estimates under the assumptions stated.

## Stabilizer formalism (as introduced in this paper)
- Qubit errors are modeled as random X (bit-flip) and Z (phase-flip) operators, and Y = ZX is both. This covers a wide range of single-qubit errors (p. 4) → stabilizer-formalism
- Measuring X and Z on the same qubit in turn destroys the state, because they do not commute. Measuring the two-qubit products XaXb and ZaZb avoids this because the products commute (p. 4, Eq. 2) → stabilizer-formalism
- These commuting products are called stabilizers. Their joint eigenstates are the four Bell states for two qubits. A changed eigenvalue signals an error, but in this two-qubit example the error is detected, not located (pp. 4-5, Table II) → stabilizer-formalism
- Repeatedly measuring a complete set of commuting stabilizers forces the system into one unique joint eigenstate, which the paper calls the "quiescent state". Stabilizer codes work from this state, not from a ground state (pp. 5-6) → stabilizer-formalism
- Four-qubit X and Z stabilizers commute because each X stabilizer shares exactly two data qubits with each neighbouring Z stabilizer, giving two minus signs (p. 6, Eq. 3) → stabilizer-formalism
- A Pauli error that anticommutes with a stabilizer flips that stabilizer's measured sign. This is how errors show up as syndrome changes (p. 7, Eqs. 4-5) → stabilizer-formalism
- Logical operators commute with every stabilizer but are not products of stabilizers. They act on the degrees of freedom the stabilizers leave unconstrained. The paper writes the state as |Q>|qL>, with |Q> fixed by the stabilizers and |qL> the logical qubit (pp. 8-10) → stabilizer-formalism
- Multiplying a logical operator by stabilizers gives an equivalent logical operator (up to a sign fixed by the stabilizer outcomes), so there is only one independent XL and one ZL per logical qubit (pp. 9-10, Eqs. 7-8) → stabilizer-formalism
- The paper favors clarity over rigor (p. 1). It does not use [[n,k,d]] notation, CSS terminology or Gottesman-Knill. It only cites Gottesman's Heisenberg-representation paper for Clifford gates (p. 18, footnote 16) → stabilizer-formalism

## Surface code
- History: the surface code descends from Kitaev's toric code. The planar version is due to Bravyi–Kitaev and Freedman–Meyer. Raussendorf et al. showed a CNOT by braiding on a single surface and obtained a threshold of 0.75% per operation for a planar nearest-neighbour implementation (pp. 1-2) → surface-code
- The comparison given is that Steane and Bacon-Shor codes on 2D nearest-neighbour lattices have thresholds of about 2×10^-5 per step. The surface code tolerates roughly 1% per operation, about three orders of magnitude more (p. 2) → surface-code
- Layout: a 2D array of data qubits (hold the state) and measurement qubits. Each data qubit touches two measure-Z and two measure-X qubits. Each measure qubit touches four data qubits, or three at a boundary (p. 5, Fig. 1) → surface-code
- A measure-Z qubit measures the stabilizer ZaZbZcZd of its four neighbours. A measure-X qubit measures XaXbXcXd (p. 5) → surface-code
- Stabilizer cycle circuit: initialize the measure qubit in |g>, then run four CNOTs, then measure. For measure-Z the data qubits are controls and the measure qubit is the target. For measure-X the measure qubit is the control, with a Hadamard before and after. The cycle has 8 steps, all measure qubits run in lock-step, and the CNOT order is fixed (p. 5, Fig. 1b,c) → surface-code
- The array in Fig. 3 has 41 data qubits and 40 independent stabilizers, so one logical qubit remains. The X boundaries are the "smooth" ones and the Z boundaries the "rough" ones (p. 8) → surface-code
- Logical operators: XL is a chain of X operators across the array between the two X boundaries. ZL is a chain of Z operators between the two Z boundaries. They anticommute because they share one data qubit (p. 9, Eq. 9) → surface-code
- Distance d is the minimum number of physical X or Z flips that make up a logical operator. The Fig. 3 array has d = 5. The simulated arrays have d up to 55 (p. 11) → surface-code
- Threshold (2012, authors' own model): the per-step threshold is pth = 0.57%, roughly 4% per full cycle. The simulation uses circuit-level noise with errors on idles, initialization, Hadamard, measurement and CNOT, with CNOT errors drawn from 15 two-qubit Paulis at p/15 each. It is lower than earlier published values mostly because more error types are included (pp. 11-12, Fig. 4) → surface-code
- Below threshold the logical error rate falls exponentially with d. Above it, the rate grows with d (p. 11) → surface-code
- Scaling: PL goes as p^de with de = (d+1)/2 (rounded down for even d). The empirical fit is PL ≈ 0.03 (p/pth)^de per cycle (p. 11, Eqs. 10-11) → surface-code
- Explanation of the scaling: the dominant failures come from (d+1)/2 errors being mistaken for (d-1)/2 errors, with probability ~ p^((d+1)/2) (p. 12, Fig. 5, Eq. 12) → surface-code
- Error classes: CNOT errors (class 2) matter most, with a per-step threshold of 1.25%. Idle data qubit errors (class 0) have a threshold of 4.3%. Measure-qubit init/measure/Hadamard errors (class 1) have a threshold of about 12%, so they matter least (p. 13, Eq. 13, Figs. 7-8) → surface-code
- Qubit count: a minimum of 13 physical qubits makes one logical qubit. A "reasonably fault-tolerant" one needs of order 10^3-10^4 physical qubits (p. 2) → surface-code
- A square patch uses nq = (2d-1)^2 qubits, which grows quickly as p approaches pth. A good target is p ≲ 10^-3 (fidelity above 99.9%). At that point a logical qubit needs 10^3-10^4 physical qubits for PL of 10^-14 to 10^-15 (pp. 12-13, Fig. 6) → surface-code
- For the large-scale estimate, the authors use 2.5 × 1.25 × (2d)^2 physical qubits per logical qubit, giving ≈14,500 at d = 34 and ≈3,600 at d = 17 (App. M, p. 52) → surface-code
- Temporal distance: stabilizer values must be established over about d cycles, and operations that turn stabilizers on or off must be spaced d cycles apart (pp. 13, 21) → surface-code
- Logical qubits in practice are built from holes (defects). Switching off a measure-Z qubit gives a Z-cut hole (smooth/dual defect) and switching off a measure-X qubit gives an X-cut hole (rough/primal defect). A "double-cut" qubit uses two holes and is the type used almost exclusively. Bigger holes and wider spacing raise d (pp. 15-16, 21) → surface-code
- Errors are tracked in classical software and not physically undone. A pending X or Z is carried in the control software and applied to later measurement results (a "Pauli frame"). The paper stresses error detection over active correction (pp. 4, 7) → surface-code

## Decoding
- A syndrome change is a sign change of measure qubits. An X error flips the two adjacent measure-Z outcomes, a Z error flips the two adjacent measure-X outcomes, and Y flips both. A measurement error shows as a single flip that disappears on the next cycle (pp. 7-8, Fig. 2) → decoding
- Data and measurement errors can be told apart by their pattern in space and time. Establishing a measurement value needs several cycles (p. 7) → decoding
- Decoding is an inverse problem with no unique solution, so mistakes become likelier as error density rises. This limits what the code can tolerate (p. 8) → decoding
- Edmonds' minimum-weight perfect-matching algorithm is used to infer the errors. It works well for sparse errors and fails as error density and chain length grow (p. 11) → decoding
- Decoding needs only to find an error equivalent to the real one up to a product of stabilizers, not the exact one (p. 11, footnote 12) → decoding
- Classical processing limits the error-detection round rate to roughly 10^6-10^7 Hz (given ~3 GHz classical clocks). The authors target a 200 ns cycle (p. 39) → decoding
- Errors are also handled during stabilizer manipulations such as moves and braids, using extra before/after comparisons (p. 21) → decoding
- Other improved classical-processing methods are only cited (refs [24-28], p. 2). The paper does not describe them → decoding

## Fault-tolerant gates
- Logical gate set: X, Z, Hadamard, S, T (plus adjoints) and CNOT. Of these only T and T† are non-Clifford. X and Z are applied "in software" by tracking them (p. 18, footnote 16) → fault-tolerant-gates
- Logical qubit initialization and measurement are "easy" in one basis, by turning measure qubits off or on. The other basis is "difficult" and needs a strip of stabilizers to be switched (pp. 18-20) → fault-tolerant-gates
- A qubit hole moves by turning stabilizers off and on over two surface code cycles. The logical operators are redefined to match (pp. 22-23) → fault-tolerant-gates
- Braiding: moving a Z-cut hole around an X-cut hole is a logical CNOT. The paper checks four operator transformations: XL⊗IL→XL⊗XL, IL⊗ZL→ZL⊗ZL, and IL⊗XL and ZL⊗IL unchanged. Closed loops stay unchanged, and open chains leave a loop around the other hole (pp. 26-30, Eqs. 26-34) → fault-tolerant-gates
- Braids between two qubits of the same type do not give a CNOT directly. They need a circuit with an ancilla of the other type and three braid CNOTs, with measurement outcomes interpreted in software (p. 30, Fig. 24) → fault-tolerant-gates
- A single-control, multi-target CNOT takes no more cycles than a single-target one. A braid through several holes takes about 2d cycles (p. 30, Fig. 25) → fault-tolerant-gates
- The logical Hadamard is costlier. It isolates the qubit in a patch ("moat"), applies physical Hadamards on all its data qubits, swaps data and measure qubits to realign, then recreates the holes. The example is d = 7, with repeat counts that depend on d (pp. 31-34, Figs. 26-28, App. J) → fault-tolerant-gates
- S gate: deterministic, using an ancilla |YL> = (|g>+i|e>)/sqrt2 with 2 CNOTs and 2 Hadamards (pp. 34-35, Fig. 29) → fault-tolerant-gates
- T gate: uses an ancilla |AL> = (|g>+e^{iπ/4}|e>)/sqrt2 with a CNOT and a Z measurement. It is probabilistic: about half the time it gives T, and otherwise T†, which an S gate corrects (pp. 35-36, Fig. 30) → fault-tolerant-gates
- Each T gate consumes one distilled |AL> state, and the T sequence in Shor's circuit is essentially incompressible. This is the most resource-intensive part (App. M, p. 52) → fault-tolerant-gates
- State injection: a "short qubit" has an XL chain only one data qubit long, so an arbitrary rotation Rz(θ) can be applied to that single qubit, giving |g>+e^{iθ}|e> (θ = π/2 for Y, π/4 for A). The short qubit is then enlarged (p. 37, Fig. 31, App. K) → fault-tolerant-gates
- The injected state is imprecise, and classical control alone cannot get it below ~10^-14. Distillation is therefore required (p. 37) → fault-tolerant-gates
- Distillation: |YL> uses a 7-qubit Steane-code circuit and |AL> a 15-qubit Reed-Muller circuit. Both are post-selected on stabilizer outcomes (pp. 37-38, Figs. 32-33) → fault-tolerant-gates
- Distillation numbers: for |YL>, input error p becomes about 7p^3, with success probability 1-7p. For |AL>, input error p becomes about 35p^3, with success probability 1-15p (pp. 38-39) → fault-tolerant-gates
- Repeated rounds improve exponentially but need 7^n or 15^n inputs. With p ~ 1%, two rounds give ~10^-15 for |YL> (p. 39). With the 0.5% injected error assumed for |AL>, the first stage gives ≈4×10^-6 and the second ≈3×10^-15 (App. M, p. 52) → fault-tolerant-gates
- Distillation is cheap in time (six logical CNOT cycles for |YL>, at most eight for |AL>) but costly in space (p. 37; see resource estimation) → fault-tolerant-gates
- The paper does not discuss transversal gates, Eastin–Knill or lattice surgery. Its Clifford gates come from braiding and the Hadamard patch procedure → fault-tolerant-gates

## Resource estimation (2012 numbers, 2000-bit Shor factoring)
- Several Shor circuits trade qubit count against Toffoli time (Table I). The footprint grows with total Toffoli count divided by sequential Toffoli count. The paper uses the first row: 2N logical qubits and 40N^3 sequential Toffolis (p. 2) → resource-estimation
- Assumptions: N = 2000 bits (~600 decimal digits), p = 10^-3 per step (about a tenth of threshold), measurement time tM = 100 ns, surface code cycle 200 ns, and a Toffoli completed in 3 tM using 7 T gates (pp. 2, 52) → resource-estimation
- Time: 40N^3 ≈ 3×10^11 sequential Toffolis × 3 × 100 ns gives about 26.7 hours, set by modular exponentiation (pp. 2, 52) → resource-estimation
- Magic-state demand: 7 × 40N^3 = 280N^3 ≈ 2×10^12 |AL> states, with a target error per state well below ≈4×10^-13 (App. M, p. 52) → resource-estimation
- Distances chosen: d2 = 34 for the final distillation stage and for computation qubits (PL ≈ 3×10^-19), and d1 = 17 for the first stage (p. 52) → resource-estimation
- One "AA factory" is ≈800,000 physical qubits, takes ≈500 cycles (~100 µs) and makes about 2 |AL> states. About 1200 factories in parallel give ≈10^9 physical qubits (p. 53) → resource-estimation
- The 4000 computational logical qubits × 14,500 ≈ 58 million physical qubits, under 6% of the total (pp. 2-3, 53) → resource-estimation
- Headline 2012 result: about a billion physical qubits for about a day (pp. 3, 53). Roughly 10^8 physical qubits is called the smallest practical number for a factoring computer (p. 39) → resource-estimation
- Sensitivity: if p improves 10x to 10^-4, the distances drop to 16 and 8 and the total falls to ≈130 million physical qubits, with unchanged run time (pp. 3, 53) → resource-estimation
- A slower cycle needs more qubits or longer runtimes. A 2 ms cycle with no extra qubits would take ~30 years. Logical gate times of 0.1-10 µs are called realistic (pp. 3, 39) → resource-estimation
- A 10^4 × 10^4 qubit array at 100 µm pitch is ~1 × 1 m^2 (pp. 39-40) → resource-estimation
- Physical requirements named: 10-100 ns gates, coherence of at least 1-10 µs, and fidelities of at least 99%. The authors single out superconducting circuits as the best candidate (pp. 39-40) → resource-estimation

## Not covered / caveats
- threshold-theorem: not covered. The paper neither states nor proves it and treats the surface code threshold only numerically (p. 11). Nothing here supports concatenation or the general theorem.
- Also nothing on repetition codes, the Shor code, logical-qubit experiments or neural/real-time decoders.
- Dated numbers: pth = 0.57% is for the authors' own circuit-level model, and the paper elsewhere quotes ~1% per operation (p. 2). Keep the two apart. The ~14,500 qubits per logical qubit and ~10^9 physical qubits for 2000-bit factoring are 2012 estimates, not current best figures.
- The 0.5% state-injection error (pI = 0.005) is an assumption in App. M, not an achieved value.
- Level: university / specialist. Tutorial in style, assumes basic QM, and is long.
