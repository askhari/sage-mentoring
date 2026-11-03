---
concept: state-vector-postulate
title: "El estado cuántico como vector"
---

## Fundamentos {#layer-1}

**El primer postulado.** En mecánica cuántica el estado de un sistema aislado se describe con un vector de un espacio vectorial complejo con producto interior, llamado **espacio de Hilbert (Hilbert space)**. La completitud del espacio solo importa en dimensión infinita [@preskill-ph219, ch.2 §2.1, pp. 3-4]. Para lo que sigue usarás espacios de dimensión finita, que son los de [vectores y notación de Dirac](../../math-foundations/concepts/vectors-and-dirac-notation.md).

**Por qué un vector.** Los estados se pueden sumar y multiplicar por números complejos (es el [principio de superposición](superposition-principle.md)), y eso es justo lo que define un espacio vectorial complejo [@zwiebach-mit-8-04, LN1 §2, p. 5; §4, p. 10].

**Ejemplo con el espín.** El estado general de un espín 1/2 es `|Ψ⟩ = c₁|z;+⟩ + c₂|z;−⟩` con `c₁, c₂` complejos, representado por la columna `(c₁, c₂)ᵀ`. El producto interior es `⟨α|β⟩ = α₁*β₁ + α₂*β₂` y la base es ortonormal; la normalización exige `|c₁|² + |c₂|² = 1` [@zwiebach-mit-8-05, ch.2 §2, pp. 7-8, 11]. Es lo que verás como `α|0⟩ + β|1⟩` en el [qubit](../../qubits-and-circuits/concepts/qubit.md).

**La función de onda.** Para una partícula en el espacio, el estado es la función de onda `Ψ(x,t)`, que es compleja: la ecuación de Schrödinger contiene `i` explícitamente y no admite soluciones reales [@zwiebach-mit-8-04, LN1 §2, p. 5; LN5 §1, p. 4]. Los números complejos no se miden, así que `Ψ` se relaciona con lo observable solo a través de probabilidades calculadas con `|Ψ|²` [@zwiebach-mit-8-04, LN1 §2, p. 5]. OpenStax insiste en que `Ψ` es "una herramienta" de cálculo, no algo directamente observable [@openstax-physics-3, §7.3].

**Normalización.** La partícula debe encontrarse en algún sitio: `∫|Ψ|² dx = 1` [@openstax-physics-3, §7.1]. En un vector, es el análogo de que tenga norma 1 (ver [producto interior y norma](../../math-foundations/concepts/inner-products-and-norms.md)).

**Por qué importa en computación cuántica.** Todo el cálculo cuántico se escribe con este objeto: el estado de un registro de qubits es un vector de amplitudes complejas de norma 1, y los simuladores de estados exactos almacenan ese vector `[unverified]`. Las puertas son operaciones que transforman este vector ([evolución unitaria](unitary-time-evolution.md)) y la medida lo convierte en probabilidades ([regla de Born](born-rule-measurement.md)).

## Comprensión {#layer-2}

**Estados como rayos.** Estrictamente, un estado es un **rayo (ray)**: la clase de vectores que difieren en un factor complejo no nulo; por convención se elige uno de norma 1, y la fase global no tiene significado físico (`|ψ⟩` y `e^{iα}|ψ⟩` son el mismo estado) [@preskill-ph219, ch.2 §2.1, p. 4]. Zwiebach lo dice con `Ψ` y `αΨ`, que describen la misma física [@zwiebach-mit-8-04, LN6 §1, p. 2]. Watrous añade que las matrices densidad eliminan esa ambigüedad: `|ψ⟩` y `e^{iθ}|ψ⟩` dan la misma matriz [@watrous-2025, L9.1, PDF pp. 267-268].

**Fase global frente a fase relativa.** La fase global no importa, pero la fase relativa entre términos de una superposición sí: cualquier combinación `a|φ⟩ + b|ψ⟩` es un estado y la fase relativa entre `a` y `b` es físicamente significativa [@preskill-ph219, ch.2 §2.1, p. 4]. Este es el origen de la interferencia.

**Contar parámetros.** Un estado de polarización `α|x⟩ + β|y⟩` tiene dos números complejos, pero el factor global es irrelevante, así que solo importa el cociente `β/α`: un número complejo o dos reales, que coincide con los dos parámetros reales de la polarización elíptica clásica [@zwiebach-mit-8-04, LN1 §4, pp. 10-11]. Para un qubit, normalización y fase global dejan dos parámetros reales, que son los ángulos de la dirección del espín [@preskill-ph219, ch.2 §2.2.1, pp. 8-9; §2.2, p. 8].

**Misma información, distinta base.** El mismo estado se puede expandir en la base propia de distintos observables: `Σαᵢψᵢ` con `αᵢ = (ψᵢ,Ψ)` y `Σ|αᵢ|² = 1` [@zwiebach-mit-8-04, LN9 §1, pp. 3-4]. La función de onda en el espacio de momentos `Φ(k)` se obtiene por transformada de Fourier y conserva la información, con `∫|Ψ|²dx = ∫|Φ|²dk` (Parseval) [@zwiebach-mit-8-04, LN8 §1, pp. 1-3]. Elegir base es como elegir coordenadas, no cambia el estado.

**Ondas planas y paquetes.** Una onda plana tiene `|Ψ|² = 1`, su integral es infinita y por eso no puede representar una sola partícula; superponer ondas planas da paquetes normalizables [@zwiebach-mit-8-04, LN6 §1, p. 2]. Las soluciones aceptables son continuas y no divergen en el infinito [@openstax-physics-3, §7.3].

**Sistemas compuestos.** El espacio de Hilbert de un sistema compuesto es el producto tensorial `H_A ⊗ H_B`, y partes preparadas de forma independiente dan un estado producto [@preskill-ph219, ch.2 §2.1, pp. 6-7]. Esto se ve en [producto tensorial](../../math-foundations/concepts/tensor-products.md) y [estados de varios qubits](../../qubits-and-circuits/concepts/multi-qubit-states.md).

**Errores frecuentes.**

- *"Las amplitudes son probabilidades."* Son números complejos cuyo módulo al cuadrado es la probabilidad [@zwiebach-mit-8-04, LN1 §2, p. 5].
- *"La fase no importa."* Solo la global.
- *"Un estado es una propiedad medible."* El vector no se mide directamente; solo se mide a través de observables ([medida](born-rule-measurement.md)).

## Profesional {#layer-3}

**Simetrías y fases.** Como los estados son rayos, las representaciones de simetrías solo necesitan cumplirse salvo una fase. El teorema de Wigner dice que una simetría conserva `|⟨φ|ψ⟩|` y por tanto se representa (con elecciones de fase) por un operador unitario o antiunitario [@preskill-ph219, ch.2 §2.2.1, p. 9].

**Una consecuencia observable de las fases.** Girar un espín 1/2 un ángulo `2π` da `−I`: el estado cambia de signo. Parece irrelevante por ser fase global, pero se observa con una rotación controlada de `2π`, que lleva un espín de control en superposición a un estado ortogonal [@preskill-ph219, ch.2 §2.2.1, p. 12, ec. 2.34]. La idea de que una fase del objetivo puede acabar como fase relativa del control se retoma en [retroceso de fase](../../quantum-algorithms/concepts/phase-kickback.md).

**Convenciones de fase.** La fase global de un estado propio no es observable, así que se escoge la forma más sencilla; por ejemplo `|e₁;−⟩ = −|x;−⟩` y `|e₂;−⟩ = i|y;−⟩` describen los mismos estados físicos [@zwiebach-mit-8-05, ch.2 §4, pp. 17-18]. Ninguna fórmula única de `|n;±⟩` evita la ambigüedad de fase sobre toda la esfera [@zwiebach-mit-8-05, ch.2 §4, nota 3, p. 18]. En la práctica: al comparar resultados de simuladores o tomografía, compara estados salvo fase global (por ejemplo con `|⟨φ|ψ⟩|`).

**Cuando el vector no basta.** El postulado vale para sistemas aislados. Si solo se observa una parte de un sistema mayor, los estados no son rayos, las medidas no son proyecciones ortogonales y la evolución no es unitaria [@preskill-ph219, ch.2 §2.3.1, p. 17]. La herramienta correcta es la [matriz densidad](density-matrices.md). Aunque el todo esté en un rayo, un subsistema en general no lo está [@preskill-ph219, ch.2 §2.3.1, p. 21].

**Trayectoria del estado.** Zwiebach describe el estado como un vector unitario de `H` cuya punta recorre una trayectoria con el tiempo [@zwiebach-mit-8-05, ch.6 §2, pp. 10-11].

**Cómo decidir la representación.** Vector de estado: sistema cerrado, estado puro conocido. Matriz densidad: ruido, subsistemas, mezclas. Esta decisión reaparece en simulación (ver [simuladores y vectores de estado](../../qiskit-programming/concepts/simulators-and-statevectors.md)).
