---
concept: universal-gate-sets
title: "Conjuntos universales de puertas"
---

## Comprensión {#layer-2}

**La pregunta.** Un procesador cuántico no puede implementar cualquier unitaria de golpe; se le da un repertorio pequeño de puertas ([puertas de un qubit](single-qubit-gates.md) y [de dos qubits](two-qubit-gates.md)) y se componen en [circuitos](quantum-circuits.md). Un conjunto de puertas es **universal** si componiéndolas se puede aproximar cualquier unitaria sobre cualquier número de qubits con la precisión que se quiera [@aaronson-2018, Lec16, p. 6; @watrous-2025, L6.2, PDF p. 170]. Con un conjunto finito solo cabe *aproximar*: las unitarias son un continuo y los circuitos, numerables [@aaronson-2018, Lec16, p. 6; @preskill-ph219, ch.5 §5.3.3, pp. 31-32].

**El precedente clásico.** Un conjunto de puertas clásicas es universal si expresa toda función booleana: `NAND` solo basta; `{AND, OR}` no (solo funciones monótonas) y `{NOT, XOR}` tampoco (solo funciones afines módulo 2) [@aaronson-2018, Lec16, p. 5]. `{AND, OR, NOT, FANOUT}` es universal para el cómputo determinista [@watrous-2025, L6.2, PDF p. 171]. Para la versión reversible, `Toffoli` es universal y puede simular `NAND`; ninguna puerta reversible de 2 bits lo es, hacen falta al menos 3 [@aaronson-2018, Lec16, pp. 5-6]. Como toda puerta clásica reversible es también cuántica, un circuito cuántico calcula lo mismo que uno clásico de tamaño parecido usando `Toffoli` [@aaronson-2018, Lec16, p. 6].

**Conjuntos cuánticos habituales.**

| Conjunto | Universal en qué sentido |
|---|---|
| todas las puertas de un qubit + `CNOT` | exacto, pero irreal: hay una infinidad continua de puertas y ninguna se implementa con precisión infinita [@de-wolf-2026, §2.2, p. 28; @preskill-ph219, ch.5 §5.4.2, p. 39] |
| `{CNOT, H, T}` ("base de Shor") | aproximado: toda unitaria se aproxima tanto como se quiera [@de-wolf-2026, §2.2, p. 28; §13.1, p. 121] |
| `{H, Toffoli}` | aproximado, para unitarias con entradas reales [@de-wolf-2026, §2.2, p. 28] |
| `{H, S, Toffoli}` | universal [@preskill-ph219, ch.5 §5.4.1, p. 35; @aaronson-2018, Lec16, p. 7] |
| `{X, Y, Z, H, S, S†, T, T†, CNOT}` + medidas | el conjunto por defecto que adopta Watrous; sus puertas unitarias son universales [@watrous-2025, L6.2, PDF p. 170] |

También `{H, Λ(S)}` es universal [@preskill-ph219, ch.5 §5.4.1, p. 35]. Que cada conjunto es universal no se demuestra aquí: Watrous afirma que la prueba no es simple y no la da [@watrous-2025, L6.2, PDF p. 170]; Preskill las deja como ejercicios [@preskill-ph219, ch.5 §5.4.1, p. 35].

**Cuatro formas de fallar.** Aaronson las ordena así: (1) *sin superposición* (por ejemplo `{CNOT}`, que lleva estados de base a estados de base); (2) *sin entrelazamiento* (`{H}`, o cualquier conjunto de puertas de un qubit); (3) *solo puertas reales* (`{CNOT, H}`, que solo tiene entradas reales); (4) *contenido en el conjunto estabilizador* `{CNOT, H, S}`, que no es obvio: por el teorema de Gottesman-Knill los circuitos estabilizadores sobre `|0…0⟩` se simulan clásicamente en tiempo polinómico [@aaronson-2018, Lec16, pp. 6-7]. Cambiar `H` por casi cualquier otra cosa en ese conjunto da universalidad, y una puerta aleatoria de dos qubits es universal con probabilidad 1 [@aaronson-2018, Lec16, p. 7]. Si hay otras formas de fallar es un problema abierto [@aaronson-2018, Lec16, p. 7].

**Qué significa "universal" y qué no.** La definición no limita el número de puertas necesarias; un argumento de medida muestra que la mayoría de las unitarias tiene un coste extremadamente alto [@watrous-2025, L6.2, PDF p. 170]. Las unitarias arbitrarias de varios qubits se consideran no elementales, porque dar coste unitario a una puerta sobre millones de qubits no es un modelo realista [@watrous-2025, L6.2, PDF p. 170].

**Errores frecuentes.**

- *"Con `H` y `CNOT` ya se puede todo."* No: `{CNOT, H}` solo tiene entradas reales [@aaronson-2018, Lec16, pp. 6-7]; hace falta una puerta como `T`.
- *"Universal quiere decir eficiente."* Universal habla de aproximación; la eficiencia es otra cuestión (capa 3).

## Profesional {#layer-3}

**Solovay-Kitaev: aproximar sin pagar un precio exponencial.** Para un conjunto universal cerrado bajo inversas, cualquier unitaria de `k` qubits (`k` fijo) se aproxima con error `ε` usando `polylog(1/ε)` puertas, y el circuito se encuentra clásicamente en tiempo `polylog(1/ε)` [@preskill-ph219, ch.5 §5.4.1, pp. 35-36; §5.4.4, pp. 42-43; @de-wolf-2026, §2.2, p. 28; @aaronson-2018, Lec16, p. 8]. Idea de la demostración: se construye un conmutador de grupo `e^{iB}e^{iC}e^{−iB}e^{−iC}` de cuatro elementos de una red `ε` para aproximar el error restante; los errores de orden `ε` se cancelan en el conmutador y la precisión pasa de `ε` a `ε' = C·ε^{3/2}` [@preskill-ph219, ch.5 §5.4.4, pp. 43-45]. El tamaño crece como `[log(1/ε)]^{3,97}`; para `{H, T}` se hace mejor, con `O(log(1/ε))` puertas para cualquier unitaria de un qubit [@preskill-ph219, ch.5 §5.4.4, pp. 44-45]. Consecuencias: un conjunto universal simula a otro con sobrecoste polilogarítmico, y `BQP` no depende del conjunto elegido [@preskill-ph219, ch.5 §5.4.1, pp. 35-36; §5.4.4, pp. 42-43]. Ojo: algunas clases, como `EQP` (tiempo polinómico cuántico exacto), sí dependen del conjunto de puertas [@de-wolf-2026, §13.2, p. 122].

**Por qué hay un problema de conteo.** Las unitarias de `n` qubits son un continuo enorme; los circuitos de `T` puertas son pocos. Contando: llegar a todo `U(2ⁿ)` con precisión `δ` exige un `T` exponencial [@preskill-ph219, ch.5 §5.3.3, pp. 31-33]. Aaronson lo da como versión cuántica del argumento de Shannon: incluso las unitarias diagonales de `n` qubits necesitan unos `2ⁿ` parámetros, mientras que un circuito con pocas puertas tiene pocos parámetros continuos, así que casi todas las unitarias necesitan exponenciales puertas [@aaronson-2018, Lec16, pp. 3-4]. De Wolf da una versión para funciones booleanas: con `k` tipos de puertas sobre ≤ 3 qubits, hay a lo sumo `(k+1)^C (3C)^{3C} = C^{O(C)}` circuitos con `≤ C` puertas, y para calcular siquiera el 1% de las `2^{2ⁿ}` funciones booleanas hace falta `C ≥ Ω(2ⁿ/n)` [@de-wolf-2026, §13.1, p. 121]. Es una versión sobre funciones y no sobre unitarias [@de-wolf-2026, §13.1, p. 121]; sirve para entender por qué pocos problemas son eficientemente resolubles.

**Por qué importa que sea finito.** La tolerancia a fallos solo puede proteger puertas discretas, y por eso se trabaja con un conjunto finito de puertas [@preskill-ph219, ch.5 §5.3, p. 23]; ver [puertas tolerantes a fallos](../../error-correction/concepts/fault-tolerant-gates.md). Que `T` sea la pieza "difícil" lo confirma el resultado de que `{CNOT, H, S}` se simula clásicamente [@aaronson-2018, Lec16, pp. 6-7].

**Elegir `T` y no otro ángulo.** Con `T` (rotación `π/4`), `{CNOT, H, T}` es universal, pero si `T` se sustituye por `T²` (rotación `π/2`), solo queda un subgrupo finito de `SU(2)` (el grupo de simetrías del cubo), así que no es universal; los únicos subgrupos finitos no abelianos de `SO(3)` son los de simetría de polígonos y poliedros regulares [@preskill-ph219, ch.5 §5.4.3, p. 42].

**Dos puertas genéricas bastan.** Dos puertas genéricas no conmutativas generan toda `SU(2)`; dos puertas genéricas de dos qubits, toda `SU(4)`; y una sola puerta genérica de dos qubits basta si se combina con su conjugada por `SWAP` [@preskill-ph219, ch.5 §5.4.3, pp. 41-42]. Con puertas que conmutan, en cambio, el número de potencias necesarias puede ser enorme y el esquema es ineficiente [@preskill-ph219, ch.5 §5.4.3, pp. 39-40].

**De dos qubits a todo.** Toda unitaria `U ∈ U(N)` se factoriza en `N(N−1)/2` unitarias "2×2" que actúan en el espacio de dos estados de base; cada una se reduce a puertas de dos qubits de forma recursiva, y `{Λ(U): U cualquiera de un qubit}` es exactamente universal, y por tanto `CNOT` más puertas de un qubit arbitrarias [@preskill-ph219, ch.5 §5.4.2, pp. 36-39].

**Cómo decidir.** Criterios de uso: (1) *modelo teórico*: usar el conjunto de Watrous o `{CNOT, H, T}` y acotar el coste en puertas; (2) *análisis de recursos*: contar puertas `T` aparte del resto, porque sin una puerta como `T` el conjunto queda dentro del estabilizador y es simulable clásicamente [@aaronson-2018, Lec16, pp. 6-7]; (3) *hardware*: las puertas nativas de cada dispositivo ([transpilación](../../qiskit-programming/concepts/transpilation.md)) se traducen a uno de estos conjuntos, con coste polilogarítmico (Solovay-Kitaev). Ver también [tecnologías de qubits](../../quantum-hardware/concepts/hardware-landscape.md).
