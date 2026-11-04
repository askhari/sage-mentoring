---
source: nist-fips-203
concepts: [post-quantum-cryptography]
---

Accessed: full text of FIPS 203 (final, 13 Aug 2024) from local extraction; read front matter, §1-3, §8, App. C. Pseudocode sections (§4-7) skipped except for a summary.

## Why the standard exists
- The key-establishment schemes in NIST SP 800-56A (discrete-log) and SP 800-56B (integer factorization) are vulnerable to attacks by sufficiently capable quantum computers; ML-KEM is an approved alternative believed secure even against a large-scale fault-tolerant quantum computer (§1.1, p. 1) → post-quantum-cryptography
- If large-scale quantum computers are built, many common public-key systems are at risk: both key establishment and digital signatures based on integer factorization and discrete logarithms (finite fields and elliptic curves) (§1.2, p. 1) → post-quantum-cryptography
- In 2016 NIST began a public Post-Quantum Cryptography (PQC) Standardization process; 82 candidates were submitted and, after three rounds, NIST chose four algorithms to protect sensitive US government information well into the future, including after cryptographically relevant quantum computers appear (§1.2, p. 1) → post-quantum-cryptography
- The abstract says ML-KEM is "believed" secure at present, even against adversaries with a quantum computer. This is a belief based on current analysis, not a proof (Abstract, p. iii; §1.1) → post-quantum-cryptography

## What a KEM is
- A KEM is a set of algorithms (KeyGen, Encaps, Decaps) with which two parties establish a shared secret key over a public channel. That key is then used with symmetric-key algorithms for encryption and authentication (Abstract; §1.1, p. 1; §3.1, p. 12) → post-quantum-cryptography
- KeyGen and Encaps are probabilistic, and Decaps is deterministic. A KEM also comes with a collection of parameter sets that trade security against efficiency (§3.1, p. 12) → post-quantum-cryptography
- Protocol flow: Alice runs KeyGen to get an encapsulation key (can be public) and a decapsulation key (private). Bob uses the encapsulation key in Encaps, which gives him a shared secret key K and a ciphertext. He sends the ciphertext to Alice. Alice runs Decaps with her decapsulation key and the ciphertext to get K' (Announcement item 3, p. i; §3.1, p. 13, Fig. 1) → post-quantum-cryptography
- The standard deliberately avoids the terms "public key" and "private key" and uses encapsulation key, decapsulation key, encryption key, decryption key and shared secret key instead (§3.2, p. 15) → post-quantum-cryptography
- The shared secret key produced by ML-KEM is always 256 bits (32 bytes). It can be used directly as a symmetric key, or further keys can be derived from it in an approved manner (SP 800-108, SP 800-56C) (§3.3, p. 16; App. C.1) → post-quantum-cryptography
- Correctness: without corruption or interference, K' = K with overwhelming probability. A decapsulation failure (K' ≠ K) has probability 2^-138.8 (ML-KEM-512), 2^-164.8 (ML-KEM-768) and 2^-174.8 (ML-KEM-1024) (§3.2, p. 14-15, Table 1) → post-quantum-cryptography
- The security guarantees of a KEM hold only under conditions set in SP 800-227. These include keeping the randomness, the decapsulation key and the shared secret key secret. Conforming to the standard does not by itself make an implementation secure (Announcement item 13, p. iii) → post-quantum-cryptography

## ML-KEM and its origin
- ML-KEM is derived from the round-three version of the CRYSTALS-KYBER KEM, a submission to the NIST PQC process. Kyber is described as a lattice-based KEM (§1.1-1.2, p. 1) → post-quantum-cryptography
- The name ML-KEM comes from the Module Learning With Errors assumption on which it is based (§1.2, p. 1) → post-quantum-cryptography
- Approval and effect: published and effective on 13 Aug 2024. The approving authority is the Secretary of Commerce, and the maintainer is NIST's Information Technology Laboratory (Announcement items 4-5, 11, p. i, iii) → post-quantum-cryptography
- The FIPS applies to US federal information systems (not national security systems), and its use is open to private and commercial organizations. It is to be used wherever federal applications need shared-secret key establishment, unless another FIPS or SP specifies an alternative mechanism (Announcement item 6, p. ii) → post-quantum-cryptography
- Differences from Kyber (round 3) that change input-output behavior: the shared secret key has a fixed 256-bit length. A different variant of the Fujisaki-Okamoto transform is used (the ciphertext hash is no longer included in the key derivation). The extra hashing of the randomness m is dropped because approved randomness generation is required. Explicit input checks were added (App. C.1, p. 47) → post-quantum-cryptography
- Change from the draft: FIPS 203 ipd was posted on 24 Aug 2023. After comments, domain separation was added in K-PKE.KeyGen so that a seed for one security level cannot be misused for another. An accidental swap of the matrix indices was reversed to match Kyber (App. C.2, p. 47) → post-quantum-cryptography
- NIST has two patent license agreements so that the licensed patents are freely available to implementers of ML-KEM as published by NIST (Announcement item 10, p. ii) → post-quantum-cryptography
- Planned maintenance: NIST will reevaluate the standard every five years, and sooner if a technology breakthrough or a mathematical weakness is found (Announcement item 13, p. iii) → post-quantum-cryptography

## Security basis (MLWE)
- ML-KEM's security rests on the presumed hardness of Module Learning With Errors (MLWE). It generalizes the LWE problem introduced by Regev in 2005, and MLWE's hardness is itself tied to the presumed hardness of certain problems in module lattices (§3.2, p. 13) → post-quantum-cryptography
- LWE in outline: the input is random "noisy" linear equations in a secret vector x over Z_q^n, and the task is to recover x. The noise makes standard methods such as Gaussian elimination intractable. Publishing many noisy equations lets others encrypt, which yields an asymmetric scheme (§3.2, p. 13) → post-quantum-cryptography
- MLWE replaces Z_q^n with a module R_q^k, the k-fold product of the polynomial ring R_q = Z_q[X]/(X^256 + 1), with n = 256 and q = 3329. The secret is an element of R_q^k (§2.3, p. 5; §3.2, p. 13) → post-quantum-cryptography
- Construction: first a public-key encryption scheme (K-PKE) is built from MLWE. Then the Fujisaki-Okamoto transform turns it into a KEM that is believed to be IND-CCA2 secure. K-PKE alone is not IND-CCA2-secure and must not be used stand-alone (§3.2-3.3, p. 13-15) → post-quantum-cryptography
- The number-theoretic transform (NTT) is used for much faster polynomial multiplication (§3.2, p. 14) → post-quantum-cryptography
- A proof of asymptotic security in a heuristic model exists (cited to the Kyber paper). The security strength of each parameter set is estimated from current cryptanalysis (§3.2, p. 14) → post-quantum-cryptography

## Parameter sets (§8, p. 39-40; §3.2, p. 14)
- There are three parameter sets, in order of increasing security and decreasing performance: ML-KEM-512 (security category 1), ML-KEM-768 (category 3) and ML-KEM-1024 (category 5). The categories are defined in SP 800-57 Part 1 → post-quantum-cryptography
- Variable parameters (k, η1, η2, du, dv): 512 has (2, 3, 2, 10, 4), 768 has (3, 2, 2, 10, 4) and 1024 has (4, 2, 2, 11, 5). The constants are n = 256 and q = 3329 (Table 2, p. 39). The value k sets the matrix and vector dimensions → post-quantum-cryptography
- Sizes in bytes (Table 3, p. 39), given as encapsulation key / decapsulation key / ciphertext / shared secret. For 512: 800 / 1632 / 768 / 32. For 768: 1184 / 2400 / 1088 / 32. For 1024: 1568 / 3168 / 1568 / 32 → post-quantum-cryptography
- Security strength is not given as a single number such as "128 bits". Each set is claimed to be at least as hard to break as a generic block cipher or hash function of a prescribed size, under any realistic computational model (§8, p. 39-40) → post-quantum-cryptography
- The random bit generator must have a security strength of at least 128 bits (512), 192 bits (768) and 256 bits (1024) (§3.3, p. 16; Table 2) → post-quantum-cryptography
- Guidance: when first protecting data, use the strongest feasible parameter set to reduce the risk of costly later transitions to higher security. NIST recommends ML-KEM-768 as the default, with a large security margin at reasonable cost. Other sets may be used where this is impractical or more security is needed (§8, p. 40) → post-quantum-cryptography
- All three parameter sets are approved to protect sensitive, non-classified US federal communication systems (§1.1, p. 1) → post-quantum-cryptography

## Hybrid, combined use, and related standards
- A combined KEM that includes ML-KEM as a component might not meet IND-CCA2 security. Implementers must assess the security of any procedure that applies SP 800-56C key derivation to ML-KEM combined with another key-establishment method. Further guidance on combined KEMs is in SP 800-227 (§3.3, p. 16) → post-quantum-cryptography
- The standard says additional KEMs may be specified and approved in the future in FIPS or NIST SPs (Announcement item 3, p. i) → post-quantum-cryptography
- ML-KEM is distinct from the digital-signature side: §1.2 (p. 1) says signatures based on factoring and discrete logs are also at risk and that four algorithms were selected overall. The note covers only the KEM and does not name FIPS 204 or FIPS 205 (§1.2, p. 1) → post-quantum-cryptography
- ML-KEM uses the NIST hash and XOF functions SHA3-256, SHA3-512, SHAKE128 and SHAKE256 from FIPS 202 (§4.1, p. 18) → post-quantum-cryptography

## Not found in this source
- FIPS 204 and FIPS 205 are not mentioned by name.
- Nothing is said about migration timelines or deprecation dates for RSA/ECC, and no hybrid-deployment protocol (e.g. TLS) is described.
- Shor's algorithm is not named.
- Concepts requested but not covered: none beyond the gaps above.
- Level: specialist standard. Sections 1-3 and 8 are readable at university or introductory-plus level, and §4-7 are implementer-oriented.
