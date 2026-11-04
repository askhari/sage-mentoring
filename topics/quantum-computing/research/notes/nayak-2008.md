---
source: nayak-2008
concepts: [topological-qubits]
---

Accessed: full extracted text of arXiv:0707.1889v2 (28 Mar 2008), Nayak, Simon, Stern, Freedman, Das Sarma, Rev. Mod. Phys. 80 (2008). Read abstract, Sec. I-II fully, Sec. III.B (p+ip), Sec. IV.A-B, IV.D, V. Skipped the TQFT/CFT math (III.A, III.C-G, IV.C). Page numbers are arXiv pages. All experimental status statements are as of early 2008 (text written 2007).

## Basic idea: anyons and braiding
- In 3+1 D only bosons and fermions are possible, because winding one particle fully around another can be shrunk to nothing; in 2+1 D the winding cannot be removed, so exchanging identical particles can give an arbitrary phase (anyons) (p. 3).
- Exchanges of N particles in 2+1 D are classified by the braid group, which is infinite and non-commuting (swapping order of exchanges gives different results); this richness is what makes computing by braiding possible (pp. 3-4) → topological-qubits
- Non-Abelian braiding statistics: when N quasiparticles at fixed positions have a degenerate ground-state space, each exchange acts as a unitary matrix on that space, and these matrices do not commute (p. 4) → topological-qubits
- Requirements for non-Abelian anyons: (1) degenerate N-quasiparticle ground states (degeneracy lifted exponentially in separation), (2) braiding gives a unitary whose non-Abelian part depends only on the braid topology, (3) braiding is the only way to act on the degenerate space while the particles are far apart (p. 7) → topological-qubits
- Anyons only arise as emergent quasiparticles in a 2D many-body system (a "topological phase of matter"); electrons, atoms, photons are always bosons or fermions even when confined to a plane (p. 6) → topological-qubits
- Fusion: bringing two anyons together can give several outcomes (fusion channels); the channel is the internal state used to store information. Two particles cannot change their fusion channel by braiding only with each other; a third particle is needed (pp. 5-6) → topological-qubits
- Ising anyons have three types (1, sigma, psi) with fusion sigma x sigma = 1 + psi; four sigmas fusing to 1 span a 2-dimensional space, the simplest case of a topological qubit (p. 5). Exchange phases for Ising anyons are quoted on p. 6 → topological-qubits

## Why topological protection reduces errors
- Background in the review: quantum error correction by redundancy works, but with estimated thresholds of about 1e-4 to 1e-6 per operation; the authors say it is "presently unclear" whether local-qubit computers can ever reach fault tolerance this way (p. 8) → topological-qubits
- The authors split errors into those during processing (imprecise unitaries) and during storage (environment decoherence); a topological quantum computer is claimed to be protected against both (p. 9) → topological-qubits
- Protection mechanism: the computational space is the degenerate ground-state manifold, separated from excitations by an energy gap; any local perturbation (e.g. electron-phonon or hyperfine interactions) has no nontrivial matrix elements inside it, so decoherence from local noise is suppressed (p. 9) → topological-qubits
- A topological qubit is non-local: it is stored in the shared internal quantum number of several well-separated quasiparticles, in contrast to local physical qubits (p. 9) → topological-qubits
- Gate errors from imprecision are avoided because the gate depends only on the topological class of the braid, not on path wiggles; braids are discrete (either encircle or not), so there is no small-angle error like rotating by 90.01 degrees (pp. 9-10) → topological-qubits
- The authors present this as fault tolerance "at the level of hardware" without needing software error correction (p. 10) → topological-qubits
- Remaining error sources: unintended extra quasiparticles that create the wrong braid, either thermally excited quasiparticle-quasihole pairs or quasiparticles trapped by disorder/impurities/density or field deviations (pp. 10-11) → topological-qubits
- Thermally created pairs that wander around one existing quasiparticle, or annihilate one and replace it, do not corrupt the qubit; an error needs a pair to braid at least two computational quasiparticles (pp. 11, 59-60) → topological-qubits
- Error probability scales roughly as exp(-Delta/2T) for thermal quasiparticles (Delta = gap) or exp(-Delta L/v) for virtual ones with qubit size L; so operation must be at temperature well below the gap (pp. 11, 60) → topological-qubits
- The authors caution that real error rates are not well predicted: other small gaps (neutral fermions), spatially varying gap in disordered samples, and variable-range hopping can dominate; a complete theory of quasiparticle transport does not exist (p. 60) → topological-qubits
- The authors' simple estimate for a 5/2 qubit: gap about 500 mK, T about 5 mK gives error rate about 1e-15, which they call overly optimistic (p. 18) → topological-qubits

## Ising anyons, Majorana modes, and non-universality
- In a p+ip superconductor, a half-flux-quantum (hc/2e) vortex binds a zero-energy mode whose operator is its own conjugate, i.e. a Majorana operator (neutral, equal electron/hole mixture); 2N vortices give 2^N degenerate ground states (2^(N-1) at fixed fermion parity); a vortex has quantum dimension sqrt(2) (pp. 30-31) → topological-qubits
- Two vortices/Majoranas define a two-level system, whose two fusion channels correspond to the pair's fermion parity (empty or filled Dirac fermion); the resulting anyons are Ising anyons (p. 31) → topological-qubits
- Moore-Read (Pfaffian) quasiholes at nu = 5/2 are essentially Ising anyons; 2n quasiholes give 2^(n-1) states and braiding acts as a pi/2 rotation in a spinor representation (p. 13) → topological-qubits
- Qubit in Ising systems: state |0> if a sigma pair fuses to 1, |1> if to psi; 2n quasiparticles hold n-1 qubits (p. 52) → topological-qubits
- Gates available by braiding: exchanging two quasiparticles of the same qubit gives a phase gate; exchanging across qubits gives an entangling operation, and a CNOT can be built from a sequence of braids with 6 quasiparticles (Georgiev) (p. 52) → topological-qubits
- Non-universality: Ising/SU(2)_2 braiding only generates a finite set of 90-degree-type rotations, so it cannot implement all unitaries; braiding alone is not universal (pp. 52-53; Sec. II.B.2, p. 9) → topological-qubits
- Fix: add a single-qubit pi/8 phase gate and a two-qubit (parity) measurement of topological charge. The phase gate comes from bringing two quasiparticles close so their energy splitting acts for a time; this is a non-topological operation that cannot be exact, so some software error correction is needed (p. 53) → topological-qubits
- Required accuracy of those extra operations is modest: pi/8 gate within about 14% and the measurement within about 38%, citing Bravyi (2006) (p. 53) → topological-qubits
- Alternative: topology change of the manifold (Bravyi-Kitaev) or a non-Abelian phase universal by braiding alone (p. 53) → topological-qubits
- Fibonacci anyons (tau x tau = 1 + tau; realized by Z3 parafermion/SU(2)_3 states) are the simplest model universal by braiding alone; a qubit uses 3 quasiparticles; the authors say SU(2)_k theories are universal for all integer k except 1, 2, 4 (pp. 2, 53-54) → topological-qubits
- Systematic braid-approximation error: brute-force search of braids should reach about 1e-5 accuracy for fundamental gates (p. 59) → topological-qubits

## Candidate platforms and experimental status as of 2008
- Overall verdict: the only systems where there is even indirect evidence for non-Abelian anyons are fractional quantum Hall states in 2D electron gases; the authors state there is no direct experimental evidence for non-Abelian quasiparticles (pp. 11, 16) → topological-qubits
- nu = 5/2 FQH state: even-denominator state first seen in 1987; leading candidate is the Moore-Read Pfaffian, supported by numerics (about 80% overlap for 18 electrons; 97% for a Pfaffian/anti-Pfaffian mix at 14 electrons) but with no measurement yet of the expected e/4 quasiparticle charge; alternatives are the anti-Pfaffian and partially polarized states; some 2006-07 numerics raised doubts (pp. 13-15) → topological-qubits
- nu = 12/5: might be the Z3 Read-Rezayi state (universal by braiding), but only one published observation of a well-quantized plateau (Xia et al. 2004), no spin-polarization data, and it may simply be Abelian (p. 16) → topological-qubits
- Proposed 5/2 device: a Hall bar with antidots and constrictions holding quasiholes; a qubit is two quasiholes, read by interferometer conductance, and a single quasiparticle tunnelling between them applies a NOT gate; moving quasiparticles in the bulk to do other gates ("bucket brigade") is an unsolved problem (pp. 16-19, 52) → topological-qubits
- Proposed interference signature: with Moore-Read, odd numbers of localized e/4 quasiparticles suppress the interference pattern and even numbers show it; this was proposed, not yet observed (p. 17) → topological-qubits
- Materials requirements: the gap is small; at 5/2 it was about 25 mK in 1987 and about 600 mK in the best 2007 samples; 2D electrons are hard to cool below about 20 mK (bath can be colder); mobilities of 10-30e6 cm^2/Vs exist, and about 100e6 may be needed for TQC to be feasible (pp. 19-20) → topological-qubits
- p+ip superconductors: called the most transparent route to non-Abelian anyons (vortices are Ising anyons). Sr2RuO4 (Tc about 1.5 K) has evidence for chiral p-wave (triplet pairing, broken time-reversal) but expected edge currents were not found; half-quantum vortices have not been directly observed (pp. 20-22) → topological-qubits
- Ultracold atoms: rotating Bose gases (needs filling nu below about 10 vs. 500 reached in 2004 experiments) and p-wave Feshbach-resonance Fermi gases (bound-state lifetimes too short to thermalize in early experiments); RF absorption could detect Majorana modes in vortices (p. 22) → topological-qubits
- Lattice spin models (Kitaev toric code, honeycomb model, Levin-Wen) show topological phases and anyons, including Fibonacci anyons, but are "artificial-looking" and far from a realistic material; the toric code is Abelian and not enough for computation (pp. 20-21) → topological-qubits
- Challenge named in Sec. V: first find a non-Abelian topological phase in nature; need to create quasiparticles, braid them, and read out their state; the authors think non-Abelian anyons may be observed in the quantum Hall regime "in the near future" (pp. 61-62) → topological-qubits
- Context claims on quantum computing (Shor's algorithm cost, Feynman simulation) appear on pp. 7-8 and are only motivational → topological-qubits

## Limits and flags
- ⚠️ This is a 2008 review. The platform status (5/2 and 12/5 as the main hope; Majorana in nanowires not yet proposed; Sr2RuO4 as p-wave candidate) is outdated and must not be presented as current. In particular the review does not discuss semiconductor-superconductor nanowire Majorana proposals.
- ⚠️ The authors are enthusiasts for the field (Freedman and Nayak are at Microsoft Station Q); optimism like "intrinsically guarantees fault tolerance" (p. 10) describes the theoretical ideal, not demonstrated hardware.

## Not covered
- Requested but absent: Majorana nanowire platforms and the later experimental controversy (post-2008 developments), since this is a 2008 source. Need other sources.
- Level: university / specialist review; Sec. II is written for a general physics audience.
