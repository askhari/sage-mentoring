---
concept: state-vector-postulate
title: "El estado cuántico como vector"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
El estado de un sistema cuántico aislado es un vector de norma 1 de un espacio vectorial complejo con producto interior, el **espacio de Hilbert (Hilbert space)**. Sus componentes son las amplitudes, y su módulo al cuadrado da probabilidades [@preskill-ph219, ch.2 §2.1, pp. 3-4; @zwiebach-mit-8-04, LN1 §2, p. 5].

### Explicación
Es el primer postulado de la teoría. La completitud del espacio solo importa en dimensión infinita [@preskill-ph219, ch.2 §2.1, pp. 3-4]; aquí se usan espacios de dimensión finita, los de [vectores y notación de Dirac](../../math-foundations/concepts/vectors-and-dirac-notation.md).

Que sea un vector se sigue de la superposición: los estados se pueden sumar y multiplicar por números complejos (es el [principio de superposición](superposition-principle.md)), y eso es justo lo que define un espacio vectorial complejo [@zwiebach-mit-8-04, LN1 §2, p. 5; §4, p. 10].

Para una partícula en el espacio, el estado es la función de onda `Ψ(x,t)`, que es compleja: la ecuación de Schrödinger contiene `i` explícitamente y no admite soluciones reales [@zwiebach-mit-8-04, LN1 §2, p. 5; LN5 §1, p. 4]. Los números complejos no se miden, así que `Ψ` se relaciona con lo observable solo a través de probabilidades calculadas con `|Ψ|²` [@zwiebach-mit-8-04, LN1 §2, p. 5]. OpenStax insiste en que `Ψ` es "una herramienta" de cálculo, no algo directamente observable [@openstax-physics-3, §7.3].

La partícula debe encontrarse en algún sitio, así que `∫|Ψ|² dx = 1` [@openstax-physics-3, §7.1]. En un vector, esta **normalización** equivale a que tenga norma 1 (ver [producto interior y norma](../../math-foundations/concepts/inner-products-and-norms.md)).

En computación cuántica todo el cálculo se escribe con este objeto: el estado de un registro de qubits es un vector de amplitudes complejas de norma 1, y los simuladores de estados exactos almacenan ese vector [@aaronson-2018, Lec16, p. 2]. Las puertas son operaciones que transforman este vector (evolución unitaria, capa 2) y la medida lo convierte en probabilidades ([regla de Born](born-rule-measurement.md)).

### Ejemplo
El estado general de un espín 1/2 es `|Ψ⟩ = c₁|z;+⟩ + c₂|z;−⟩` con `c₁, c₂` complejos, representado por la columna `(c₁, c₂)ᵀ`. El producto interior es `⟨α|β⟩ = α₁*β₁ + α₂*β₂`, la base es ortonormal y la normalización exige `|c₁|² + |c₂|² = 1` [@zwiebach-mit-8-05, ch.2 §2, pp. 7-8, 11]. Es lo que verás como `α|0⟩ + β|1⟩` en el [qubit](../../qubits-and-circuits/concepts/qubit.md).

### Errores frecuentes
- *"Las amplitudes son probabilidades."* Son números complejos cuyo módulo al cuadrado es la probabilidad [@zwiebach-mit-8-04, LN1 §2, p. 5].
- *"Un estado es una propiedad medible."* El vector no se mide directamente; solo se mide a través de observables ([medida](born-rule-measurement.md)).

### Para seguir
[Medida y regla de Born](born-rule-measurement.md) explica cómo se leen las amplitudes. La capa 2 de este concepto precisa qué parte del vector es físicamente relevante: la fase global no, la relativa sí.

## Comprensión {#layer-2}

### Idea clave
Estrictamente, un estado es un rayo: vectores que difieren en un factor complejo no nulo describen el mismo estado. La fase global no tiene significado físico, pero la fase relativa entre términos de una superposición sí, y es el origen de la interferencia [@preskill-ph219, ch.2 §2.1, p. 4].

### Explicación
Un estado es un **rayo (ray)**: la clase de vectores que difieren en un factor complejo no nulo; por convención se elige uno de norma 1, y `|ψ⟩` y `e^{iα}|ψ⟩` son el mismo estado [@preskill-ph219, ch.2 §2.1, p. 4]. Zwiebach lo dice con `Ψ` y `αΨ`, que describen la misma física [@zwiebach-mit-8-04, LN6 §1, p. 2]. Watrous añade que las matrices densidad eliminan esa ambigüedad: `|ψ⟩` y `e^{iθ}|ψ⟩` dan la misma matriz [@watrous-2025, L9.1, PDF pp. 267-268].

Lo que sí cuenta es la fase relativa. Cualquier combinación `a|φ⟩ + b|ψ⟩` es un estado y la fase relativa entre `a` y `b` es físicamente significativa [@preskill-ph219, ch.2 §2.1, p. 4].

Esto permite contar parámetros. Un estado de polarización `α|x⟩ + β|y⟩` tiene dos números complejos, pero el factor global es irrelevante, así que solo importa el cociente `β/α`: un número complejo o dos reales, que coincide con los dos parámetros reales de la polarización elíptica clásica [@zwiebach-mit-8-04, LN1 §4, pp. 10-11]. Para un qubit, normalización y fase global dejan dos parámetros reales, que son los ángulos de la dirección del espín [@preskill-ph219, ch.2 §2.2.1, pp. 8-9; §2.2, p. 8].

El mismo estado se puede expandir en la base propia de distintos observables: `Σαᵢψᵢ` con `αᵢ = (ψᵢ,Ψ)` y `Σ|αᵢ|² = 1` [@zwiebach-mit-8-04, LN9 §1, pp. 3-4]. La función de onda en el espacio de momentos `Φ(k)` se obtiene por transformada de Fourier y conserva la información, con `∫|Ψ|²dx = ∫|Φ|²dk` (Parseval) [@zwiebach-mit-8-04, LN8 §1, pp. 1-3]. Elegir base es como elegir coordenadas, no cambia el estado.

Una onda plana tiene `|Ψ|² = 1`, su integral es infinita y por eso no puede representar una sola partícula; superponer ondas planas da paquetes normalizables [@zwiebach-mit-8-04, LN6 §1, p. 2]. Las soluciones aceptables son continuas y no divergen en el infinito [@openstax-physics-3, §7.3].

Para varios sistemas, el espacio de Hilbert del compuesto es el producto tensorial `H_A ⊗ H_B`, y partes preparadas de forma independiente dan un estado producto [@preskill-ph219, ch.2 §2.1, pp. 6-7]. Esto se ve en [producto tensorial](../../math-foundations/concepts/tensor-products.md) y [estados de varios qubits](../../qubits-and-circuits/concepts/multi-qubit-states.md).

### Ejemplo
Para el estado `|ψ⟩ = α|x⟩ + β|y⟩` de polarización, multiplicar ambos coeficientes por `e^{iα}` no cambia nada, pero cambiar solo la fase de `β` sí cambia el estado: el cociente `β/α` es el dato físico [@zwiebach-mit-8-04, LN1 §4, pp. 10-11; @preskill-ph219, ch.2 §2.1, p. 4].

### Errores frecuentes
- *"La fase no importa."* Solo la global; la relativa es la que produce interferencia [@preskill-ph219, ch.2 §2.1, p. 4].

### Para seguir
La capa 3 trata las simetrías y las fases, y qué hacer cuando el vector no basta (subsistemas y ruido).

## Profesional {#layer-3}

### Idea clave
Como los estados son rayos, las fases globales son una convención y hay que comparar estados salvo fase global. Y el vector solo vale para sistemas aislados: para un subsistema se necesita la matriz densidad [@preskill-ph219, ch.2 §2.2.1, p. 9; §2.3.1, p. 17].

### Explicación
Las representaciones de simetrías solo necesitan cumplirse salvo una fase. El teorema de Wigner dice que una simetría conserva `|⟨φ|ψ⟩|` y por tanto se representa (con elecciones de fase) por un operador unitario o antiunitario [@preskill-ph219, ch.2 §2.2.1, p. 9].

La fase global de un estado propio no es observable, así que se escoge la forma más sencilla; por ejemplo `|e₁;−⟩ = −|x;−⟩` y `|e₂;−⟩ = i|y;−⟩` describen los mismos estados físicos [@zwiebach-mit-8-05, ch.2 §4, pp. 17-18]. Ninguna fórmula única de `|n;±⟩` evita la ambigüedad de fase sobre toda la esfera [@zwiebach-mit-8-05, ch.2 §4, nota 3, p. 18]. En la práctica, al comparar resultados de simuladores o tomografía se comparan estados salvo fase global, por ejemplo con `|⟨φ|ψ⟩|`.

Aunque parezca irrelevante, una fase global puede acabar siendo observable. Girar un espín 1/2 un ángulo `2π` da `−I`: el estado cambia de signo, y se observa con una rotación controlada de `2π`, que lleva un espín de control en superposición a un estado ortogonal [@preskill-ph219, ch.2 §2.2.1, p. 12, ec. 2.34]. La idea de que una fase del objetivo puede acabar como fase relativa del control se retoma en [retroceso de fase](../../quantum-algorithms/concepts/phase-kickback.md).

El postulado vale para sistemas aislados. Si solo se observa una parte de un sistema mayor, los estados no son rayos, las medidas no son proyecciones ortogonales y la evolución no es unitaria [@preskill-ph219, ch.2 §2.3.1, p. 17]. Aunque el todo esté en un rayo, un subsistema en general no lo está [@preskill-ph219, ch.2 §2.3.1, p. 21]. La herramienta correcta es la [matriz densidad](density-matrices.md).

Zwiebach describe el estado como un vector unitario de `H` cuya punta recorre una trayectoria con el tiempo [@zwiebach-mit-8-05, ch.6 §2, pp. 10-11].

La decisión de representación es: vector de estado para sistema cerrado y estado puro conocido; matriz densidad para ruido, subsistemas o mezclas. Reaparece en simulación (ver [simuladores y vectores de estado](../../qiskit-programming/concepts/simulators-and-statevectors.md)).

### Ejemplo
Dos simuladores devuelven para el mismo circuito `|ψ⟩` y `−|ψ⟩`. No hay discrepancia física: son el mismo rayo. Para compararlos se calcula `|⟨φ|ψ⟩|`, que vale 1 si coinciden salvo fase global [@preskill-ph219, ch.2 §2.2.1, p. 9; @zwiebach-mit-8-05, ch.2 §4, pp. 17-18].

### Para seguir
El siguiente paso del ámbito es [medida y regla de Born](born-rule-measurement.md), y las matrices densidad se desarrollan en su propio concepto.
