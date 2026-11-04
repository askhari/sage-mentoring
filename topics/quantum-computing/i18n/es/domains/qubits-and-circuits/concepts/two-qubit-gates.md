---
concept: two-qubit-gates
title: "Puertas de dos qubits (CNOT y controladas)"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
La **CNOT (controlled-NOT)** invierte un qubit objetivo si y solo si el qubit de control vale `1`: `|a⟩|b⟩ → |a⟩|a ⊕ b⟩`. Es la puerta de dos qubits básica, porque un producto de puertas de un qubit nunca hace que un qubit afecte a otro [@watrous-2025, L3.1, PDF pp. 70, 72; @aaronson-2018, Lec5, p. 3].

### Explicación
Las puertas de un qubit no bastan: un producto tensorial de ellas nunca consigue que un qubit afecte a otro, y hacen falta operaciones así para que haya interacción [@aaronson-2018, Lec5, p. 3].

La `CNOT` tiene un qubit de **control** y uno de **objetivo (target)**. Es decir, `|0⟩|b⟩ → |0⟩|b⟩` y `|1⟩|b⟩ → |1⟩|1−b⟩` [@de-wolf-2026, §1.4, pp. 21-22]. En los diagramas, el control es un punto negro unido por una línea al objetivo, que se dibuja como un círculo con un `+` (`⊕`) [@watrous-2025, L3.1, PDF pp. 70, 72; @de-wolf-2026, §2.1.2, p. 27].

Con el control como primer qubit y el orden de base `00, 01, 10, 11`, su matriz permuta los dos últimos estados de base [@de-wolf-2026, §1.4, pp. 21-22]:

```
CNOT = [[1,0,0,0],
        [0,1,0,0],
        [0,0,0,1],
        [0,0,1,0]]
```

Si se intercambian los papeles (control = segundo qubit), la matriz cambia, así que el orden de los sistemas importa [@watrous-2025, L2.1, PDF pp. 44-45]; con la convención de Qiskit, con el control en el qubit de arriba (el segundo de la cadena), la matriz es `[[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]]` [@watrous-2025, L3.1, PDF p. 75]. No se puede escribir como producto tensorial de dos puertas de un qubit [@watrous-2025, L2.2, PDF p. 66].

La idea se generaliza a las puertas controladas. La controlada-`U` aplica `U` al objetivo si el control es `|1⟩`: `|0⟩⟨0|⊗I + |1⟩⟨1|⊗U`, y `CNOT` es el caso `U = X` [@watrous-2025, L2.2, PDF pp. 66-68; @preskill-ph219, ch.5 §5.4.3, p. 35]. Para una `U` de `n` qubits es la matriz por bloques `diag(I, U)` de tamaño `2^{n+1}` [@de-wolf-2026, §1.4, p. 22]. Ejemplos de la familia: controlada-`Z` (aplica `Z` al objetivo), la puerta de **Toffoli** (CCNOT, dos controles) y la de **Fredkin** (controlada-`SWAP`) [@watrous-2025, L3.1, PDF pp. 72-73]. Toffoli lleva `|a⟩|b⟩|c⟩` a `|a⟩|b⟩|c ⊕ (a∧b)⟩` [@watrous-2025, L6.3, PDF pp. 177-178]; invierte el tercer bit solo si los dos primeros son `1` [@de-wolf-2026, §2.1.2, p. 26].

### Ejemplo
Tres casos de `CNOT`:

- Sobre estados de base se comporta como un XOR reversible: `CNOT|10⟩ = |11⟩`, `CNOT|11⟩ = |10⟩`.
- Sobre una superposición en el control crea entrelazamiento: `CNOT(|+⟩⊗|0⟩) = CNOT (|00⟩+|10⟩)/√2 = (|00⟩+|11⟩)/√2 = |φ⁺⟩`. Esa es exactamente la segunda mitad del circuito que fabrica un [par de Bell](entanglement.md): `H` sobre el primer qubit y después `CNOT` [@aaronson-2018, Lec5, p. 4].
- `CNOT|0⟩|0⟩ = |0⟩|0⟩` y `CNOT|1⟩|0⟩ = |1⟩|1⟩`: con el objetivo en `|0⟩`, `CNOT` "copia" estados de base. No copia `|+⟩`, como se explica en el teorema de no clonación [@watrous-2025, L3.3, PDF pp. 94-95].

### Errores frecuentes
- *"La matriz de `CNOT` es única."* Depende de qué qubit es el control y del orden de la cadena [@watrous-2025, L3.1, PDF p. 75].

### Para seguir
Con las puertas de [uno](single-qubit-gates.md) y de dos qubits ya se pueden montar [circuitos cuánticos](quantum-circuits.md). La capa 2 explica por qué `CNOT` crea entrelazamiento y qué se puede construir con ella.

## Comprensión {#layer-2}

### Idea clave
`CNOT` convierte un estado producto en uno entrelazado; casi cualquier puerta de dos qubits lo hace, salvo las locales y `SWAP`, y por eso `CNOT` es la puerta de dos qubits por defecto [@aaronson-2018, Lec5, p. 4; @preskill-ph219, ch.5 §5.4.1, p. 34].

### Explicación
En general, una puerta de dos qubits es *entrelazante* si lleva algún estado producto a uno no producto. Las únicas que no lo son son las locales `A⊗B`, `SWAP` y las localmente equivalentes a `SWAP`, `(A⊗B)·SWAP·(C⊗D)`; cualquier otra unitaria de dos qubits es entrelazante y, junto con puertas de un qubit arbitrarias, universal [@preskill-ph219, ch.5 §5.4.1, p. 34]. Este es el hecho que justifica que `CNOT` sea la puerta de dos qubits por defecto ([conjuntos universales](universal-gate-sets.md)).

Por dentro, `CNOT` es hermítica y su propia inversa [@de-wolf-2026, ejercicio 1.4, p. 23; @preskill-ph219, ch.4 §4.1.1, p. 7, ec. 4.12]. Se puede construir con dos `H` y una controlada-`Z`: `H` en el objetivo antes y después de controlada-`Z` [@de-wolf-2026, ejercicios 2.1-2.3, p. 32]. Rodear `CNOT` con `H⊗H` intercambia control y objetivo [@de-wolf-2026, ejercicios 2.1-2.3, p. 32]: la distinción control/objetivo depende de la base. Una controlada-`Z` al inicio del circuito de Bell, o un `SWAP` al final, quita el signo `−1` de la última salida [@watrous-2025, L3.1, PDF p. 76]. Una controlada-fase `Λ(S) = diag(1,1,1,i)` actúa simétricamente sobre los dos qubits aunque su símbolo parezca asimétrico [@preskill-ph219, ejercicio 5.3, p. 48].

`SWAP` (intercambia dos qubits) se construye con tres `CNOT`: `(x, y) → (y, x)` [@preskill-ph219, ch.5 §5.2.2, p. 16, ec. 5.30; @watrous-2025, L6.3, PDF pp. 180-181]. Lo útil de tenerla es que permite acercar qubits lejanos y devolverlos a su sitio, de manera que las restricciones geométricas apenas cambian la complejidad [@preskill-ph219, ch.5 §5.4.1, pp. 33-34].

Del lado clásico, Toffoli es completa para la computación clásica reversible: con un `0` fijo en la tercera línea da `AND`, y con `1` fijos en las dos primeras da `NOT`; con `AND` y `NOT` se construye cualquier circuito booleano [@de-wolf-2026, §2.1.2, p. 26]. También da `COPY` con ancillas fijas, y es no lineal; las puertas reversibles de uno y dos bits son todas afines (`x → Mx + a`) y no pueden ser universales [@preskill-ph219, ch.5 §5.2.2, pp. 15-19]. Con `CNOT` solo se obtienen funciones afines módulo 2 (ni `AND` ni `OR`), y como lleva estados de base a estados de base, no crea superposición [@aaronson-2018, Lec16, p. 6].

### Ejemplo
`SWAP` con tres `CNOT` sobre estados de base: `(x, y)` pasa a `(x, x⊕y)`, luego a `(x⊕(x⊕y), x⊕y) = (y, x⊕y)` y finalmente a `(y, (x⊕y)⊕y) = (y, x)`, con los controles alternados [@preskill-ph219, ch.5 §5.2.2, p. 16, ec. 5.30].

### Errores frecuentes
- *"El qubit de control no cambia nunca."* Solo si está en un estado de base. Con el control en superposición, control y objetivo acaban entrelazados, y ya no se puede decir qué hizo cada uno (ver [entrelazamiento](entanglement.md)).
- *"`CNOT` copia el control."* Solo copia estados de base [@aaronson-2018, Lec7, p. 4]; con superposiciones fabrica un par de Bell, una "copia" entrelazada que no es dos copias independientes [@aaronson-2018, Lec7, p. 4].

### Para seguir
La capa 3 usa `CNOT` para construir puertas controladas mayores y pesa su coste real en dispositivos.

## Profesional {#layer-3}

### Idea clave
Con `CNOT` y puertas de un qubit se construyen puertas controladas arbitrarias, pero las puertas de dos qubits son las más propensas a error y marcan el coste real de un circuito [@de-wolf-2026, ejercicio 2.6, p. 32; @bruzewicz-2019, p. 20].

### Explicación
Una controlada-`U` con `det U = 1` sale de `CNOT` y de matrices `A, B, C` con `ABC = I` y `A·X·B·X·C = U` [@de-wolf-2026, ejercicio 2.6, p. 32]. `Λ²(V)` (doble control) para una `V` de un qubit con `V = U²` se construye con `Λ(U)`, `Λ(U†)` y `CNOT`: el exponente de `U` aplicado es `y − (x ⊕ y) + x = 2xy`; este es el paso clave para fabricar controladas de `n` qubits con puertas de dos [@preskill-ph219, ch.5 §5.4.2, p. 38]. Toffoli se construye con `H`, `T`, `T†` y `CNOT`, de modo que no hace falta que sea nativa [@watrous-2025, L6.3, PDF pp. 177-178].

Casi todas las unitarias de `n` qubits necesitan un número exponencial de puertas (ver [circuitos cuánticos](quantum-circuits.md) y [conjuntos universales](universal-gate-sets.md)) [@aaronson-2018, Lec16, pp. 3-4; @preskill-ph219, ch.5 §5.3.3, pp. 31-33]; por eso el coste de un circuito se mide en puertas de uno y de dos qubits, no en unitarias arbitrarias.

Las puertas de dos qubits son además las más propensas a error en dispositivos reales: en iones, sus errores son al menos un orden de magnitud mayores que los de un qubit [@bruzewicz-2019, p. 20]; en qubits de espín, la infidelidad de dos qubits queda al menos un orden de magnitud por encima, y normalmente más [@stano-2022, §IV.B, p. 11]; y en el chip Sycamore de Google (2019), la mediana era de 0,30-0,60 % frente a 0,13-0,14 % para una puerta de un qubit [@arute-2019, Tabla II, p. 22]. Es lo que se mide como fidelidad de dos qubits en [coherencia y fidelidad](../../quantum-hardware/concepts/coherence-and-fidelity.md).

A la hora de elegir entre variantes equivalentes, `CNOT` y controlada-`Z` lo son hasta puertas de un qubit; `SWAP` equivale a tres `CNOT` [@preskill-ph219, ch.5 §5.2.2, p. 16, ec. 5.30]. La elección práctica depende de la puerta nativa del dispositivo y de qué qubits están conectados (ver [transpilación](../../qiskit-programming/concepts/transpilation.md)): se necesitan `SWAP` cuando dos qubits no son vecinos [@preskill-ph219, ch.5 §5.4.1, pp. 33-34].

Con la convención de Qiskit, el qubit de arriba es `q_0` y va a la derecha de la cadena; una `CNOT` con control en `q_0` y objetivo en `q_1` tiene la segunda matriz de la capa 1 (la de Qiskit) [@watrous-2025, L3.1, PDF pp. 74-75]. Cómo se escribe en código se ve en [circuitos en Qiskit](../../qiskit-programming/concepts/qiskit-circuits.md).

### Ejemplo
Para estimar el coste de una Toffoli en un dispositivo que solo ofrece `CNOT` y puertas de un qubit, se descompone en `H`, `T`, `T†` y `CNOT` [@watrous-2025, L6.3, PDF pp. 177-178]; como las puertas de dos qubits son las de mayor error, el número de `CNOT` de la descomposición, más los `SWAP` si los qubits no son vecinos, domina el presupuesto de errores [@bruzewicz-2019, p. 20; @preskill-ph219, ch.5 §5.4.1, pp. 33-34].

### Las fuentes discrepan
En tiempo, la diferencia entre puertas de uno y de dos qubits depende de la plataforma: en iones, una puerta de uno tarda del orden de µs y una de dos 10-100 µs, pero en espines de silicio son comparables [@bruzewicz-2019, p. 3; @stano-2022, Tabla II, pp. 26-28]. No hay una razón de coste única; hay que mirar la tabla de cada tecnología.

### Para seguir
[Circuitos cuánticos y medida](quantum-circuits.md) reúne puertas de uno y dos qubits en programas completos; [conjuntos universales de puertas](universal-gate-sets.md) precisa qué repertorio basta.
