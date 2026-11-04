---
source: google-2025
concepts: [superconducting-qubits, coherence-and-fidelity, quantum-advantage-experiments, hardware-landscape, surface-code, threshold-theorem, decoding, logical-qubit-experiments, resource-estimation, quantum-noise-channels]
---

Accessed: arXiv:2408.13687v1 (24 Aug 2024, dated 27 Aug 2024), full main text, pp. 1-7 (Supplementary Information NOT read). This is the preprint, not the Nature 638 (2025) final version; numbers may differ slightly in the published paper. The text never uses the name "Willow" and does not state the paper's DOI (the only DOI given is the data deposit, 10.5281/zenodo.13273331, p. 7); the Nature DOI (10.1038/s41586-024-08449-y) is not confirmed by this text. Claims are by the authors, all from Google Quantum AI (company-authored; declared no competing interests, p. 7).

## Devices (superconducting-qubits, hardware-landscape)
- The authors report two superconducting transmon processors: a 72-qubit one (distance-5 code, repetition codes, real-time decoding) and a 105-qubit one with similar performance (distance-7 code). Both are square grids of transmons (p. 1) → superconducting-qubits
- On the 105-qubit device the mean T1 is 68 µs and T2,CPMG is 89 µs, which the authors attribute to better fabrication, participation-ratio engineering and circuit-parameter optimization (p. 2) → coherence-and-fidelity
- Higher coherence is said to improve the fidelity of all operations; per-component error distributions (1-qubit gates, CZ, measurement, data-qubit idle) are shown only graphically in Fig. 1b, so no gate/readout numbers are in the text (p. 2, Fig. 1b) → coherence-and-fidelity
- The paper contains no explicit statement comparing 1-qubit vs 2-qubit gate error or duration with numbers; it only says CZ (two-qubit) errors, local plus correlated, are the largest contributors to the error budget (p. 4) → coherence-and-fidelity
- Intro: the authors say many-qubit platforms had only recently shown 99.9% entangling-gate fidelity, far from the below-1e-10 error rates needed for many applications (p. 1) → hardware-landscape
- Superconducting qubits are fast, with gate operations of tens to hundreds of ns, giving a speed advantage but making decoding hard; the surface-code cycle here is 1.1 µs (pp. 1, 5) → superconducting-qubits
- Intro states that no quantum processor had definitively shown below-threshold performance before; other platforms have shown individual QEC features (refs. 14-20, e.g. trapped-ion real-time FT QEC, ref. 14) (p. 1) → hardware-landscape
- Two-level-system (TLS) defects can couple to qubits and cause transient fluctuations; the authors use a frequency optimization that forecasts TLS defect frequencies, plus recalibration every four runs (p. 4) → superconducting-qubits
- Gap-engineered Josephson junctions are credited by the authors for mitigating high-energy impact events (p. 4) → superconducting-qubits
- No random circuit sampling (RCS) remark was found in the main text; the only related pointer is ref. [10] (random circuits in arbitrary geometries, a trapped-ion paper) cited for 99.9% gates (pp. 1, 9) → quantum-advantage-experiments

## Surface code and threshold (surface-code, threshold-theorem)
- A surface code of distance d uses 2d²-1 physical qubits per logical qubit (p. 1) → surface-code
- The distance-7 memory uses 49 data qubits, 48 measure qubits and 4 extra leakage-removal qubits (101 total); it is run in the ZXXZ surface-code variant, prepared in the X_L or Z_L basis, with repeated syndrome-extraction cycles, then final data-qubit measurement and a decoder check (p. 2) → surface-code
- Distance-3 (9 subgrids) and distance-5 (4 subgrids) codes are taken from the same 105-qubit grid for comparison with d=7 (Fig. 1a, p. 2) → surface-code
- Scaling law: logical error ε_d ∝ (p/p_thr)^((d+1)/2), so below threshold (p << p_thr) the logical error falls exponentially with distance (Eq. 1, p. 1) → threshold-theorem
- Error suppression factor Λ = ε_d/ε_(d+2) ≈ p_thr/p, the reduction when the distance grows by 2; Λ > 1 means below threshold (p. 1) → threshold-theorem
- Result on the 105-qubit device: Λ = 2.14 ± 0.02 with neural-network decoder (ε_7 = 1.43e-3 per cycle) and Λ = 2.04 ± 0.02 with ensembled matching synthesis (ε_7 = 1.71e-3), fitted by linear regression of ln ε_d vs d, up to 250 cycles (pp. 1-3) → threshold-theorem
- Detection probability (bulk weight-4 stabilizer comparisons) as a measure of physical error: 7.7%, 8.5%, 8.7% for d = 3, 5, 7; the increase is attributed to finite-size effects and parasitic couplings (p. 2) → threshold-theorem
- Error-injection experiments: curves for d=3, 5, 7 cross near ~20% detection probability, the crossover regime; below it, higher distance gives faster logical error reduction. Fitted power laws reach only ~80% of the ideal (d+1)/2 exponent, hypothesized to come from excess correlations (p. 3, Fig. 2b) → threshold-theorem
- Simulations of the measured noise model (with leakage and stray interactions) agree reasonably with experiment and give Λ_sim = 2.25 ± 0.02, simulated up to d = 11 (Fig. 1d inset, pp. 2-3) → threshold-theorem
- Stability: over 16 repeats across 15 hours on the 72-qubit device, mean Λ = 2.18 ± 0.07 (best 2.31 ± 0.02); larger codes were less sensitive to fluctuating qubits (p. 4, Fig. 2e) → surface-code

## Logical qubit results (logical-qubit-experiments)
- Distance-7, 101 qubits: 0.143% ± 0.003% logical error per error-correction cycle (abstract, p. 1) → logical-qubit-experiments
- Beyond break-even: the d=7 logical lifetime is 291 ± 6 µs vs the constituent physical qubits' median 85 ± 7 µs and best 119 ± 13 µs, a factor of 2.4 ± 0.3 over the best one (p. 3) → logical-qubit-experiments
- The authors note that comparing logical and physical qubits is subtle because their noise differs, so they use a lifetime metric averaged uniformly over pure states (refs. 16, 24) (p. 3) → logical-qubit-experiments
- They state this extends earlier break-even results from bosonic codes to multi-qubit codes, and is a step toward break-even for logical operations, which this paper does not demonstrate (it is a memory only) (pp. 3, 7) → logical-qubit-experiments
- Experiments run up to 10^6 cycles without performance degradation, and are repeatable over hours (p. 6) → logical-qubit-experiments

## Error budget and noise (coherence-and-fidelity, quantum-noise-channels)
- Simulation-based error budget for 1/Λ on the 72-qubit device (Fig. 2c, graphical): components are CZ error, CZ stray interactions, data idle during measurement/reset, measurement and reset, leakage, and single-qubit gates. It overpredicts Λ by 20%, so some effects are uncaptured (pp. 3-4) → coherence-and-fidelity
- Both local and correlated CZ errors are the largest contributors; the authors conclude that improving coherence and calibration is key (p. 4) → coherence-and-fidelity
- Correlated errors (leakage, and stray CZ interactions inducing ZZ and swap-like errors) are about 17% of the budget; the authors expect their importance to grow as error rates fall (p. 4) → quantum-noise-channels
- Leakage to higher transmon states is a correlated error source; mitigated by multi-level reset on measure qubits and data-qubit leakage removal (DQLR), which swaps leakage onto measure or extra qubits each cycle (pp. 2, 4) → quantum-noise-channels
- Enabling DQLR leaves d=3 little changed but raises d=5 Λ by 35%, while detection probability drops only 12%; so detection probability is a good proxy for Λ only when errors are uncorrelated. The authors call leakage removal crucial for transmon surface codes (p. 4, Fig. 2d) → quantum-noise-channels
- Earlier work (ref. 17) found high-energy impact events about every 10 s, with error bursts giving a ~1e-6 logical floor; here the authors report this is mitigated (gap-engineered junctions) and error per cycle in repetition codes goes far below 1e-6 (p. 4) → quantum-noise-channels
- Distance-29 repetition code (2e10 total cycles, 5.5 h of runtime): Λ = 8.4 ± 0.1 between d=5 and 11, but from d>=15 the suppression departs from exponential, with an apparent floor of ~1e-10 logical error per cycle (p. 4) → quantum-noise-channels
- Cause of the floor: rare, spatially localized (~30 qubits) correlated error bursts, six seen in 2e10 cycles (~once an hour, ~3e9 cycles), decaying with a time constant of ~370-400 µs. They differ from earlier high-energy impacts (every few seconds, decaying over tens of ms). The authors say the origin is not understood (pp. 1, 4-5, Fig. 3d) → quantum-noise-channels
- A second, milder failure mode: one or two detectors jump >3x in detection probability, then recover after tens or hundreds of cycles, possibly from transient TLSs or coupler excitations (p. 4) → quantum-noise-channels
- Repetition-code error injection matches O(p^((d+1)/2)) scaling: halving detection probability reduces logical error 250x at d=15, in line with p^8 (p. 5, Fig. 3b) → threshold-theorem

## Decoding (decoding)
- Decoders must keep pace with syndrome generation because some logical operations are non-deterministic, depending on logical measurement results; if the decoder lags, the backlog causes an exponential blow-up in computation time (p. 5) → decoding
- Offline high-accuracy decoders: a neural-network decoder fine-tuned on processor data, and an ensemble of correlated minimum-weight perfect matching decoders with matching synthesis; edge weights tuned via reinforcement learning (p. 2) → decoding
- Real-time decoder: a specialized Sparse Blossom variant (matching), streaming over fixed-size graph buffers with parallel threads over spacetime blocks (10-cycle blocks) fused to a global matching, plus greedy edge reweighting for Y-type error correlations (pp. 5-6, Fig. 4) → decoding
- Real-time decoder latency, the time from receiving the last syndrome round to the returned correction, averages 63 ± 17 µs for d=5, constant for up to 10^6 cycles (~1.1 s), against a 1.1 µs cycle (pp. 1, 6) → decoding
- Accuracy trade-off for d=5 (72-qubit device): real-time ε_5 = 0.35% ± 0.01%, Λ = 2.0 ± 0.1; offline neural network ε_5 = 0.269% ± 0.008%, Λ = 2.18 ± 0.09. The NN needs ~24 µs per cycle vs the <1.1 µs per cycle required in real time (p. 6) → decoding
- The latency does not yet include feeding back into the logical circuit, but will set the reaction time for non-Clifford gates. The real-time decoding was not done on the d=7 code (p. 6) → decoding
- Decoding gets harder at larger distance because syndrome measurements per cycle grow quadratically with d. The authors expect layered or windowed decoding to make high-accuracy methods real-time (pp. 6-7) → decoding

## Projections (resource-estimation)
- Extrapolating the Fig. 1d fit, a 1e-6 logical error rate would need a distance-27 logical qubit with 1457 physical qubits (p. 6) → resource-estimation
- Halving physical error rates is projected to improve d=27 logical performance by about four orders of magnitude, reaching algorithmically relevant rates (p. 7) → resource-estimation
- The authors cite fault-tolerant application targets (refs. 11, 12) and say overheads should shrink with better QEC protocols and decoders; they call the current approach resource-intensive and the ~1e-10 floor a limit for large circuits (pp. 1, 4, 6-7) → resource-estimation
- Open challenges listed: logical computation (not only memory), and scaling calibration, real-time decoding and logical compilers to multi-surface-code operations (p. 7) → resource-estimation

## Not covered / level
- Requested but not covered: quantum-advantage-experiments (no RCS discussion in the main text); the Willow name, total qubit-count marketing figures and T1/gate numbers from the final Nature version (gate/readout error values appear only in Fig. 1b, unread numerically); the Nature DOI.
- Level: specialist (experimental QEC paper, written for researchers).
