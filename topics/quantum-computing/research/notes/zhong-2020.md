---
source: zhong-2020
concepts: [quantum-advantage-experiments, photonic-qubits]
---

Accessed: full text of the arXiv:2012.01625 submitted version (v1, Dec 2020; 23 pp, main text pp. 1-10), read from the local extraction. The 80+ page supplement was NOT read. Page numbers are arXiv pages. The authors are USTC (Hefei) with SIMIT and Tsinghua co-authors, so the claims below are the authors' own reports. Numbers are from the Jiuzhang 2020 device. Caveat: this is the submitted version, not the final Science text (the paper's notes added mention revisions).

## Task and definitions
- The authors define quantum computational advantage as a speedup so large that no classical computer could do the task in reasonable time, and that classical algorithmic or hardware improvements are unlikely to overturn it. They say this is also called "quantum supremacy" and they use the first term. (p. 2) → quantum-advantage-experiments
- Sampling tasks were proposed as near-term demonstrations, because running Shor's algorithm needs a fault-tolerant machine that is a long-term goal. (p. 2) → quantum-advantage-experiments
- Boson sampling (Aaronson-Arkhipov) sends non-classical light through a linear optical network and measures the output with single-photon detectors. The output state is entangled in photon number and path, and its dimension grows exponentially with photons and modes. (pp. 2-3) → quantum-advantage-experiments
- The best known classical approach computes one output probability (a matrix permanent) at a time, and at least one permanent is needed per sample. (p. 3) → quantum-advantage-experiments
- Gaussian boson sampling (GBS) feeds single-mode squeezed states, which can be prepared deterministically, into an m-mode interferometer and samples with threshold detectors. The output distribution is tied to the Torontonian, a #P-hard matrix function (an infinite sum of Hafnians). (p. 3) → quantum-advantage-experiments
- The authors mention possible applications of GBS (graph problems, point processes, quantum chemistry, molecular docking, random numbers). They say it is not itself a practical application yet. (pp. 3, 10) → quantum-advantage-experiments

## Context: the Sycamore comparison and the sample-size loophole
- The authors describe the 53-qubit superconducting experiment as producing a million noisy samples (~0.2% fidelity) in 200 s, with a first estimate of ~10,000 years classically. A later improved classical algorithm was argued to need only a few days to compute all 2^53 amplitudes and give ideal samples. (p. 2) → quantum-advantage-experiments
- They point out that this advantage depends on sample size: if ~10^10 samples were requested, the advantage would reverse. They compare this to loopholes in Bell tests and say that advantage claims need a long-term competition between classical simulation and quantum devices. They say boson sampling avoids this loophole. (p. 2) → quantum-advantage-experiments
- Their state-space dimension (~10^30) is stated to be 14 orders of magnitude above the superconducting experiment and 16 above the earlier 20-photon single-photon boson sampler. (p. 8) → quantum-advantage-experiments
- Earlier boson-sampling experiments used probabilistic, post-selected photons from parametric down-conversion (PDC), then quantum-dot on-demand single-photon sources, which reached 14-photon detection. Scaling remained a challenge. (p. 3) → quantum-advantage-experiments

## Experiment and numbers (Jiuzhang, 2020)
- 25 PPKTP crystals produce 25 two-mode squeezed states, equivalent to 50 single-mode squeezed states (SMSS) through the hybrid-encoding unitary. They go into a 100-mode interferometer and 100 detectors. (pp. 1, 4) → quantum-advantage-experiments
- Reported outcome: up to 76 output clicks, output state-space dimension ~10^30, and sampling ~10^14 times faster than the state-of-the-art simulation on supercomputers. (p. 1) → quantum-advantage-experiments
- With all 25 TMSS inputs the mean click number is 43. In 200 s they got 3,097,810 43-click events and one 76-click event. (pp. 7-8) → quantum-advantage-experiments
- The authors split the regimes into easy (full output distribution measurable), sparse (above about 4 clicks, most outputs have zero events, so only sampling is possible) and intractable. (p. 7) → quantum-advantage-experiments
- The paper's list of challenges: many SMSS sources with high squeezing, indistinguishability and collection efficiency; a large, deep, fully connected interferometer with near-unity transmission; phase control of all sources, since GBS relies on coherent superposition of photon numbers; high-efficiency detectors; validation of sparse samples. (p. 4) → quantum-advantage-experiments

## Validation
- Full certification of large GBS outputs is conjectured to be classically intractable, unlike Shor's algorithm whose answer is easy to check. Validation methods become intractable above ~30 clicks. The authors say they gather circumstantial evidence by ruling out alternative hypotheses. (p. 7-8) → quantum-advantage-experiments
- Small-scale check (3 TMSS inputs, 2 clicks): average fidelity 0.990(1) and total variation distance 0.103(1) against theory, over 23 input configurations. (p. 7) → quantum-advantage-experiments
- Thermal-state and distinguishable-photon hypotheses are excluded by comparing the click-number distribution and two-point correlations C_ij with simulations. The data match theory and differ from both alternatives. (p. 8) → quantum-advantage-experiments
- The heavy output generation (HOG) ratio test excludes the thermal hypothesis for 26-30 clicks. The authors argue that higher-click events suffer relatively less loss, so they should be validated with higher confidence. A revised version extended the validation to 40 clicks (Note added 2). (pp. 8-9, 10) → quantum-advantage-experiments
- The uniform-random hypothesis is excluded by matching samples to the reconstructed theoretical probability curve (Fig. 4H). The authors say the sample density follows the theory, which a uniform sampler could not reproduce. (p. 9) → quantum-advantage-experiments

## Speedup claim and classical cost
- Benchmark on Sunway TaihuLight: one Torontonian takes ~0.03 s at 30 clicks and ~2 days at 50 clicks (256-bit precision). Markov-chain sampling needs ~100 Torontonians per sample. (p. 9) → quantum-advantage-experiments
- Summing the cost over all click-number classes, the authors estimate that TaihuLight would need ~8x10^16 s (2.5 billion years) to produce the 200 s worth of samples, and Fugaku ~2x10^16 s (0.6 billion years). The cost is dominated by 50-70 clicks. (p. 9) → quantum-advantage-experiments
- The authors invite improved classical algorithms to challenge the ~10^14 advantage. They argue that low-rank speedups do not apply because their rank ratio is ~50:75, and that a newer quadratic-speedup algorithm for non-collision GBS does not readily apply since collision modes dominate (Note added 1). Note added 3 mentions a 144-mode follow-up. (pp. 9-10) → quantum-advantage-experiments
- The authors also leave open classical speedups for noisy GBS with photon loss. (p. 10) → quantum-advantage-experiments

## Photonic hardware
- Photonic boson samplers are said to run at room temperature and to be robust to decoherence. (p. 3) → photonic-qubits
- GBS uses squeezed light from PDC, which is Gaussian and can be prepared deterministically. The input is not single photons as in Aaronson-Arkhipov boson sampling. (p. 3) → photonic-qubits
- Source: femtosecond laser (776 nm, 200 fs, 250 kHz, 1.4 W) split to 25 PPKTP crystals. The low repetition rate gives higher pulse energy for strong squeezing and lets detectors recover (~microseconds). (p. 4) → photonic-qubits
- Measured source quality: spectral purity predicted 0.98 (0.99 with a 12 nm filter), measured average pair-wise purity 0.938 (reduced mainly by self-phase modulation), average collection efficiency 0.628. (pp. 4-5) → photonic-qubits
- Phase coherence: GBS needs a fixed phase from the sources to the interferometer, unlike Aaronson-Arkhipov boson sampling. Active locking uses the shared pump beam and a piezo fiber stretcher (phase std 0.04 rad). The interferometer is passively stabilized on a low-expansion glass plate (drift λ/180 in 3.5 h). The estimated visibility loss is below 1%. (p. 5) → photonic-qubits
- Encoding: spatial plus polarization modes give 100 modes from 50 spatial modes (H/V per path). The network is equivalent to 300 beam splitters and 75 mirrors. Path-delay std is 2.6 μm against a coherence length of ~88 μm (0.2% visibility loss). Transmission is 97.7% and output coupling ~90%. (pp. 5-6) → photonic-qubits
- Detection: 100 superconducting nanowire single-photon detectors with average efficiency 81%. Output wave plates apply random polarization rotations, followed by polarizing beam splitters. (p. 6) → photonic-qubits
- Unitary: the interferometer matrix was characterized with a narrow-band laser. The squeezing parameters and relative phases were fitted from small-scale tests, and the reconstructed matrix is unitary and consistent with a Haar-random matrix. (pp. 6-7) → photonic-qubits
- The authors call the device a "special-purpose photonic platform", with a path toward NISQ-era use. It runs one fixed (random) interferometer for sampling and does no gate-based programmable computation. (p. 10) → photonic-qubits
- Suggested upgrades: higher-efficiency detectors, a larger interferometer, and stimulated PDC. They also say the setup (squeezed states, linear network, post-selected measurement) can serve as a factory for Fock, cat and NOON states. (p. 10) → photonic-qubits

## Not covered / notes
- Not covered: universal programmability is not discussed beyond "special-purpose" (p. 10). The paper has no discussion of KLM, MBQC, fusion-based computing or photon-loss error correction. Time-bin encoding is not used.
- ⚠️ "Not a universal programmable computer" is an inference from "special-purpose" and the fixed interferometer. The paper does not state it in those words.
- ⚠️ The paper does not describe 10^14 as definitive. Later classical-simulation rebuttals are not in this source. They are only invited (p. 9).
- Level: specialist (research paper), with an intro section that is accessible.
