---
concept: single-qubit-gates
title: "Puertas de un qubit (Pauli, Hadamard, fase)"
---

## Fundamentos {#layer-1}

**Idea.** Una **puerta (gate)** es una operación unitaria sobre pocos qubits, el análogo cuántico de una puerta lógica [@de-wolf-2026, §1.4, p. 21]. Una puerta de un qubit es una matriz unitaria 2×2 (ver [matrices unitarias y hermíticas](../../math-foundations/concepts/unitary-and-hermitian-matrices.md)): conserva la norma del vector, así que lleva estados válidos a estados válidos [@watrous-2025, L1.2, PDF p. 25]. Se aplica multiplicando la matriz por el vector del estado.

**Las puertas básicas.**

| Puerta | Matriz | Qué hace |
|---|---|---|
| `X` (NOT, *bit flip*) | `[[0,1],[1,0]]` | intercambia `\|0⟩` y `\|1⟩` |
| `Z` (*phase flip*) | `[[1,0],[0,−1]]` | deja `\|0⟩` y cambia el signo de `\|1⟩` |
| `Y` | `[[0,−i],[i,0]]` | combina ambas, con una `i` |
| `H` (Hadamard) | `(1/√2)[[1,1],[1,−1]]` | convierte la base `{0,1}` en la `{+,−}` y al revés |
| `P_θ` (fase) | `diag(1, e^{iθ})` | multiplica `\|1⟩` por `e^{iθ}` |

Referencias: `X`, `Z`, `Y` [@watrous-2025, L1.2, PDF pp. 25-26; @de-wolf-2026, §1.4, p. 21]; `H` [@watrous-2025, L1.2, PDF pp. 26-27]; `P_θ` [@watrous-2025, L1.2, PDF p. 26]. Casos especiales de la fase: `Z = P_π`, `S = P_{π/2}` y `T = P_{π/4}`; la identidad es `P_0` [@watrous-2025, L1.2, PDF p. 26; @de-wolf-2026, §1.4, p. 21]. Con esta convención `S = diag(1, i)` (ver la nota sobre fases en la capa 2).

**Matrices que actúan.** Con `|0⟩ = (1,0)ᵀ` y `|1⟩ = (0,1)ᵀ`:

- `X|0⟩ = (0,1)ᵀ = |1⟩`, y `X|1⟩ = |0⟩`.
- `Z|0⟩ = |0⟩`, `Z|1⟩ = −|1⟩`. Sobre `|+⟩` da `|−⟩`: `Z(|0⟩+|1⟩)/√2 = (|0⟩−|1⟩)/√2`.
- `H|0⟩ = (1/√2)(1,1)ᵀ = |+⟩`, `H|1⟩ = (1/√2)(1,−1)ᵀ = |−⟩`, `H|+⟩ = |0⟩`, `H|−⟩ = |1⟩` [@watrous-2025, L1.2, PDF pp. 26-27]. Tras `H|0⟩` o `H|1⟩`, medir da una moneda justa [@de-wolf-2026, §1.4, p. 21].
- `T|1⟩ = ((1+i)/√2)|1⟩`, y por linealidad `T|+⟩ = (|0⟩ + ((1+i)/√2)|1⟩)/√2` [@watrous-2025, L1.2, PDF pp. 27-28].

**Interferencia.** `H` aplicada a `|+⟩` devuelve `|0⟩` porque las amplitudes de `|1⟩` tienen signos opuestos y se cancelan; es la misma interferencia que la de ondas de luz o de sonido [@de-wolf-2026, §1.4, p. 21]. Hacer `H` dos veces sobre `|0⟩` termina en `|0⟩` con certeza [@aaronson-2018, Lec3, p. 4; Lec4, p. 3]. Esta cancelación entre amplitudes, que no existe con probabilidades, es lo que explota casi cualquier algoritmo cuántico.

**Ejemplo con varias puertas.** El circuito `H, S, H, T` aplicado a `|0⟩` (se escribe `T·H·S·H` como producto de matrices, la última puerta a la izquierda) da `((1+i)/2)|0⟩ + (1/√2)|1⟩` [@watrous-2025, L3.1, PDF p. 73]. Paso a paso: `H|0⟩ = |+⟩`; `S|+⟩ = (|0⟩ + i|1⟩)/√2`; otra `H` da `((1+i)/2)|0⟩ + ((1−i)/2)|1⟩`; y `T` multiplica la amplitud de `|1⟩` por `(1+i)/√2`, con lo que `((1−i)/2)·((1+i)/√2) = 1/√2`.

**Un cuadrado que da NOT.** `R = H·S·H` cumple `R² = X`: es una raíz cuadrada de NOT, imposible con una única operación clásica sobre un bit [@watrous-2025, L1.2, PDF pp. 28-29]. Necesita números complejos [@aaronson-2018, Lec4, pp. 1-2].

**Por dónde seguir.** Para ver estas puertas como giros de una esfera, [la esfera de Bloch](bloch-sphere.md); para actuar sobre dos qubits, [puertas de dos qubits](two-qubit-gates.md).

## Comprensión {#layer-2}

**Por qué unitarias.** Una matriz es unitaria si y solo si conserva la norma de todo vector; son exactamente las aplicaciones lineales que llevan vectores de estado cuánticos a vectores de estado cuánticos, como las matrices estocásticas hacen con vectores de probabilidad [@watrous-2025, L1.2, PDF p. 25]. Como son invertibles, la evolución unitaria nunca destruye información [@aaronson-2018, Lec4, p. 2]. Las únicas matrices a la vez unitarias y estocásticas son las de permutación; las operaciones deterministas y unitarias se llaman reversibles [@watrous-2025, L1.2, PDF p. 29]. Detrás está la [evolución temporal unitaria](../../quantum-mechanics/concepts/unitary-time-evolution.md).

**Identidades útiles.** (Se comprueban multiplicando matrices.)

- `H = (X + Z)/√2` y `H² = I`; además `H·X·H = Z` y `H·Z·H = X` [@preskill-ph219, ch.4 §4.1.1, p. 7; @de-wolf-2026, §1.4 y ejercicio 1.3, p. 23]. "Hadamard cambia `X` por `Z`" explica por qué sirve para medir en otra base: aplicar `H` y luego medir en `z` equivale a medir en `x` [@aaronson-2018, Lec4, p. 1].
- `S² = Z` y `T² = S`, porque `P_θ·P_θ = P_{2θ}` (de la definición de `P_θ`).
- `H·R_θ·H = R_{−θ}` para la rotación real `R(θ) = [[cosθ, −sinθ],[sinθ, cosθ]]` [@de-wolf-2026, ejercicio 1.5, p. 23].
- `H` es hermítica y su propia inversa, y `H^{⊗n}|0ⁿ⟩` da la superposición uniforme de todas las cadenas de `n` bits; en general `H^{⊗n}|i⟩ = 2^{−n/2} Σ_j (−1)^{i·j} |j⟩` [@de-wolf-2026, §2.1.2, p. 26]. Esta fórmula es la base de varios algoritmos ([Deutsch-Jozsa](../../quantum-algorithms/concepts/deutsch-jozsa.md), [Bernstein-Vazirani y Simon](../../quantum-algorithms/concepts/bernstein-vazirani-and-simon.md)).

**Rotaciones y fase global.** Cada puerta es, salvo fase global, un giro de la [esfera de Bloch](bloch-sphere.md): `U = cos(θ/2)I − i sin(θ/2) n·σ`, y toda unitaria 2×2 de determinante 1 tiene esa forma [@preskill-ph219, ch.2 §2.2.1, pp. 11-12]. `X`, `Y`, `Z` son medias vueltas [@aaronson-2018, Lec7, p. 2], `H` es una media vuelta alrededor de `(x+z)/√2` [@preskill-ph219, ch.4 §4.1.1, p. 7] y `S`, `T` son rotaciones en `z` de `π/2` y `π/4` [@preskill-ph219, ch.5 §5.4.3, p. 35].

**Dos convenciones para `S`.** Preskill escribe `S = exp(−iπZ/4)` en el texto principal y `diag(1, i)` en un ejercicio; las dos matrices difieren en una fase global, así que no deben mezclarse en un mismo cálculo [@preskill-ph219, ch.5 §5.4.3, p. 35; ejercicio 5.3, p. 47]. En esta página `S = diag(1, i)`, igual que `P_{π/2}` de Watrous. La fase global no cambia ninguna probabilidad.

**Por qué números complejos.** `√NOT` no existe con matrices reales; los complejos permiten además aplicar las unitarias de forma continua en el tiempo [@aaronson-2018, Lec4, pp. 1-2]. Aaronson llama a la mecánica cuántica una "isla en el espacio de teorías": con normas distintas de la 2 no se obtiene nada interesante, y los complejos funcionan mejor que los reales o los cuaternios [@aaronson-2018, Lec4, p. 3].

**Errores frecuentes.**

- *"`Z` no hace nada porque no cambia las probabilidades."* Cambia la fase relativa, y eso se vuelve visible con `H` (`Z|+⟩ = |−⟩`) [@watrous-2025, L1.2, PDF p. 27].
- *"Las puertas dependen de que el estado sea conocido."* Son lineales: actúan igual sobre cualquier superposición, por eso `T|+⟩` se calcula con `T|0⟩` y `T|1⟩`.

## Profesional {#layer-3}

**Cualquier puerta de un qubit en tres giros.** Toda unitaria de un qubit se escribe `e^{iα}·diag(1, e^{iβ})·R(θ)·diag(1, e^{iγ})` [@de-wolf-2026, Ch. 2, ejercicios 4-5, p. 32]: dos giros alrededor de `z` y uno intermedio (descomposición de Euler, ver [esfera de Bloch](bloch-sphere.md)). Cómo se traduce esto a las puertas nativas de un dispositivo se ve en [transpilación](../../qiskit-programming/concepts/transpilation.md).

**Qué conjunto de puertas elegir.** Para un modelo realista conviene un conjunto finito: Watrous adopta `X, Y, Z, H, S, S†, T, T†` más `CNOT` y medidas de un qubit, y advierte de que permitir *todas* las puertas de un qubit da un modelo irrealmente potente si se ignora la precisión [@watrous-2025, L6.2, PDF p. 170]. Dentro de ese conjunto, `T` es la pieza que da la universalidad: `{CNOT, H, S}` queda dentro del conjunto *estabilizador*, simulable clásicamente en tiempo polinómico por el teorema de Gottesman-Knill [@aaronson-2018, Lec16, pp. 6-7]. Y no vale cualquier rotación: con `T²` (giro de `π/2`) en lugar de `T`, el conjunto genera solo un subgrupo finito de `SU(2)` [@preskill-ph219, ch.5 §5.4.3, p. 42]. Más en [conjuntos universales de puertas](universal-gate-sets.md).

**Fase global cuando una puerta se controla.** Una rotación de `2π` da `−I`: una fase global, pero observable si se controla la puerta [@preskill-ph219, ch.2 §2.2.1, p. 12]. Al convertir `S` entre convenciones o al construir puertas controladas, esa fase deja de ser inocua; hay que decidir una convención y respetarla.

**Dónde se programa.** Cada puerta de esta página tiene su instrucción en el SDK; ver [circuitos en Qiskit](../../qiskit-programming/concepts/qiskit-circuits.md) para los nombres y para la convención de orden de qubits. Para la calidad con la que un dispositivo real implementa cada puerta, ver [coherencia y fidelidad](../../quantum-hardware/concepts/coherence-and-fidelity.md).
