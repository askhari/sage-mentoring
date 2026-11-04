---
source: nist-ir-8547
concepts: [post-quantum-cryptography, shor-algorithm]
---

Accessed: full text of NIST IR 8547 (final, October 2026) via local extraction, pp. 1-32 (printed pages i-25). Page numbers below are the printed document pages (PDF page = printed + 7 for the body).

## Threat and why it is urgent
- NIST says future quantum computing may break current cryptographic algorithms; post-quantum cryptography (PQC) is the new methods protecting against both classical and quantum computers (§1, p. 1) → post-quantum-cryptography
- The transition starts before a "cryptanalytically relevant quantum computer" exists (a quantum computer able to attack real systems infeasible classically; glossary, p. 25) (§1, p. 1) → post-quantum-cryptography
- "Harvest now, decrypt later" (HNDL): adversaries collect encrypted data now to decrypt it when quantum technology matures; since sensitive data keeps value for years, this is a main reason for urgency (§1, p. 1) → post-quantum-cryptography
- Mosca's theorem: if X = years data must stay secure, Y = years to complete the transition, Z = years until a cryptanalytically relevant quantum computer exists, one must start migrating before X + Y exceeds Z; examples of long-term-sensitive data are government secrets and medical records (§3, p. 8) → post-quantum-cryptography
- Signatures are not vulnerable to HNDL, yet moving to PQ signatures is still urgent because the transition is long, complex and needs many parties to coordinate (§3, p. 8) → post-quantum-cryptography
- Authentication stays secure as long as the algorithms and keys are secure at the moment authentication is performed, so it can keep using quantum-vulnerable algorithms until a capable quantum computer appears, then must switch immediately (§3.1.2, p. 9) → post-quantum-cryptography
- In network protocols, key-establishment keys are short-lived (forward secrecy) but the symmetric keys they produce protect confidentiality, so HNDL must be considered when scheduling key-establishment migration; authentication may be migrated at a different time (§3.1.3, p. 9) → post-quantum-cryptography
- Email/document encryption (S/MIME, OpenPGP) is subject to HNDL like any confidentiality application (§3.1.4, p. 10) → post-quantum-cryptography
- Past cryptographic transitions from standardization to full integration took 10 to 20 years (§1, p. 1; §3, p. 8) → post-quantum-cryptography

## Which algorithms are quantum-vulnerable (and why)
- Signature algorithms ECDSA, EdDSA (FIPS 186) and RSA (adopted from RFC 8017/PKCS #1) are stated to be vulnerable to Shor's Algorithm on a cryptanalytically relevant quantum computer (§2.1.1, p. 3) → shor-algorithm
- Key establishment in SP 800-56A (finite-field and elliptic-curve Diffie-Hellman, MQV, based on discrete logarithm) and SP 800-56B (RSA-based key agreement and transport) is vulnerable to Shor's Algorithm (§2.1.2, p. 4) → shor-algorithm
- The report only states the vulnerability to Shor; it does not explain the mechanism (no discussion of factoring/discrete-log structure) → shor-algorithm
- Vulnerable signature schemes: ECDSA (≥112-bit classical strength), EdDSA (≥128), RSA (≥112) (Table 2, p. 15) → post-quantum-cryptography
- Vulnerable key establishment: finite-field DH/MQV, elliptic-curve DH/MQV, RSA (SP 800-56B), all at ≥112 bits (Table 4, pp. 16-17) → post-quantum-cryptography

## Symmetric cryptography and hashes
- Symmetric standards (hash functions, XOFs, block ciphers such as AES, KDFs, AEADs, DRBGs) are "significantly less vulnerable" to known quantum attacks than public-key standards (§4.1.3, p. 18) → post-quantum-cryptography
- All NIST-approved symmetric primitives with at least 128 bits of classical security are believed to meet at least Category 1 of the PQC security categories; NIST does not expect to transition away from these standards for the PQC migration (§2.1.3, p. 5; §4.1.3, p. 18) → post-quantum-cryptography
- The security categories are defined by reference primitives: Cat. 1 = key search on AES-128, Cat. 2 = collision search on SHA-256, Cat. 3 = AES-192 key search, Cat. 4 = SHA3-384 collision search, Cat. 5 = AES-256 key search (Table 1, p. 15) → post-quantum-cryptography
- Table 6 lists AES-128/192/256 as Categories 1/3/5, so AES key sizes at 128 bits or more are retained; Table 8 gives hash/XOF classical collision and preimage strengths with categories (pp. 18-19) → post-quantum-cryptography
- Only 112-bit-strength symmetric standards are singled out (to be disallowed in 2030), and applications should move off them; SHA-1 is deprecated and will be disallowed in FIPS-validated modules after 2030 (§4.1.3, p. 18; Table 8 fn. 4, p. 18) → post-quantum-cryptography
- ⚠️ Grover's algorithm is never named in this document. The effect on symmetric keys is addressed only indirectly through the categories above (AES-128 is the reference for Category 1), so no explicit "key size halves" statement can be cited here → grover-search (not covered)
- Post-quantum security is described with five broad categories rather than bit strengths, because of uncertainty in predicting costs, speed and memory of future quantum computers (§4.1, pp. 14-15) → post-quantum-cryptography

## Standardized PQC algorithms and roles
- Three PQC standards released: FIPS 203 ML-KEM, FIPS 204 ML-DSA, FIPS 205 SLH-DSA (§1, p. 1) → post-quantum-cryptography
- ML-KEM (FIPS 203, derived from CRYSTALS-Kyber) is a key-encapsulation mechanism, a type of key-establishment scheme to establish a shared secret key over a public channel (§2.1.2, p. 4) → post-quantum-cryptography
- ML-DSA (FIPS 204, from CRYSTALS-Dilithium) and SLH-DSA (FIPS 205, stateless hash-based, from SPHINCS+) are quantum-resistant digital signature schemes (§2.1.1, p. 3) → post-quantum-cryptography
- ML-KEM parameter sets: 512 / 768 / 1024 with classical strength 128 / 192 / 256 bits and categories 1 / 3 / 5; NIST recommends ML-KEM-768 as default (Table 5 and text, p. 17) → post-quantum-cryptography
- ML-DSA-44/65/87 correspond to 128/192/256 bits and categories 2/3/5 (ML-DSA-44 drops to Category 1 if an approved RBG with under 192 bits of security is used); SLH-DSA 128/192/256 maps to categories 1/3/5 (Table 3, p. 16) → post-quantum-cryptography
- SP 800-208 also specifies stateful hash-based signatures LMS/HSS and XMSS/XMSS^MT; they are quantum-resistant but, because each one-time key may sign only once and state must be tracked, are not for general use (maybe firmware/software signing) (§2.1.1, p. 3) → post-quantum-cryptography
- HQC was selected as an alternative KEM to ML-KEM after the fourth round; a FIPS for HQC-KEM is under development, and ML-KEM is currently the only approved public-key PQ key-establishment scheme (§2.1.2, p. 4; §4.1.2, p. 17) → post-quantum-cryptography
- NIST is developing a FIPS for a signature algorithm derived from FALCON as an additional alternative, and is evaluating other candidates in the additional-signatures process (§2.1.1, p. 4) → post-quantum-cryptography
- NIST has no current plans to select further KEMs, and does not anticipate standardizing any further non-quantum-resistant signature or key-establishment schemes (§4.1.1, p. 16; §4.1.2, p. 17) → post-quantum-cryptography

## Transition timeline
- NIST will deprecate quantum-vulnerable public-key cryptography (ECDSA, EdDSA, RSA signatures; finite-field/EC DH and MQV; RSA key establishment) after 2030 and disallow it after 2035 under NIST standards (§4, p. 13; Tables 2 and 4, pp. 15-17) → post-quantum-cryptography
- Previously SP 800-57 Part 1 projected disallowing 112-bit public-key schemes on January 1, 2031; NIST replaced this with the 2030/2035 plan (§4.1.1, p. 15) → post-quantum-cryptography
- Definitions: acceptable, deprecated (usable but with security risk the data owner must weigh), disallowed (no longer allowed), legacy use (only to process already-protected data, e.g. verify signatures/decrypt) (§4.1, p. 14) → post-quantum-cryptography
- NSM-10 set 2035 as the target for completing the federal migration, and that goal remains (§4, p. 13) → post-quantum-cryptography
- EO 14412 and OMB M-26-15: federal high value assets and high impact systems must adopt PQC for key establishment by December 31, 2030 and for digital signatures by December 31, 2031; agencies should mitigate as much quantum risk as feasible by end of 2030; these earlier deadlines are not relaxed by the 2030-2035 window (§1, p. 1; §4, p. 13) → post-quantum-cryptography
- Agencies must support TLS 1.3 no later than January 2, 2030 (§4, p. 13) → post-quantum-cryptography
- Application-specific guidance (e.g. TLS, IKE) may require migration of key establishment earlier than 2035 because of HNDL; TLS 1.3 offers a near-term path including hybrid ML-KEM + classical key exchange, to be reflected in the next SP 800-52 revision (§4.1.2, p. 17; §4.2, p. 20) → post-quantum-cryptography
- Recommended first steps: cryptographic inventories, migration planning, early deployment of PQC products (§1, p. 1) → post-quantum-cryptography

## Hybrid schemes and crypto-agility
- Hybrid solutions combine quantum-resistant and quantum-vulnerable algorithms (or multiple PQC algorithms with different mathematical assumptions); designed to stay secure if at least one component is secure (§3.2, p. 10) → post-quantum-cryptography
- Motives: hedge against a flaw in one component, and compatibility with sector rules that still require legacy algorithms; costs: added complexity, cost and risk; hybrids are expected to be temporary, leading to a second transition to PQC-only (§3.2, p. 10) → post-quantum-cryptography
- Running classical and PQ algorithms side by side via negotiation (one algorithm per session) is not a hybrid solution (§3.2, p. 10) → post-quantum-cryptography
- NIST leaves the choice of hybrid to each application and will accommodate hybrid key establishment and dual signatures in FIPS 140 validation when combined with a NIST-approved scheme (§3.2, pp. 10-11) → post-quantum-cryptography
- Hybrid key establishment: SP 800-56C's generic composite technique concatenates shared secrets (Z' = Z||T); it is allowed even if T comes from an unapproved source; NIST plans to update SP 800-56C so Z can come from FIPS 203 and future PQ standards, and order may be reversed; key combiner guidance is in SP 800-227 (§3.2.1, p. 11) → post-quantum-cryptography
- Hybrid signatures (dual/composite): two or more signatures on one message, all must verify; allowed if at least one component algorithm is NIST-approved (§3.2.2, pp. 11-12) → post-quantum-cryptography
- Crypto agility: the transition requires building long-term cryptographic agility into organizational infrastructure for seamless updates as PQ standards evolve (stated once, §1.1, p. 2) → post-quantum-cryptography
- Embedded impact: devices that cannot update signature-verification code should be designed to require quantum-resistant signatures if they may outlive a cryptanalytically relevant quantum computer; PQC keys/signatures are larger, affecting protocols, libraries, HSMs/TPMs and PKI (§3.1.1, p. 8; §2.2, pp. 5-6) → post-quantum-cryptography

## Change from the 2024 draft
- The document does not itself list changes from the 2024 initial public draft. Visible differences from what the draft is known to say are not stated here; the final text adds Executive Order 14412, OMB M-26-15 deadlines (2030 key establishment / 2031 signatures), HQC selection, the FALCON-derived FIPS plan, Ascon (SP 800-232) in the symmetric tables, and TLS 1.3 date. These are what this report states, not a comparison it makes → post-quantum-cryptography

## Not covered / level
- Requested but not covered: grover-search (Grover never named); shor-algorithm only as a one-line vulnerability statement, no mechanism.
- Level: specialist / policy-technical (government report, readable by intro-level readers for the timeline).
