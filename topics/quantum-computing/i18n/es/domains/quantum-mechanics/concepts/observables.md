---
concept: observables
title: "Observables"
format: 2
---

## Comprensión {#layer-2}

### Idea clave
Una magnitud medible (energía, posición, espín) se representa con un operador hermítico: sus valores propios son los resultados posibles y sus estados propios forman una base ortonormal completa [@preskill-ph219, ch.2 §2.1, p. 4; @zwiebach-mit-8-04, LN9 §1, pp. 1-3].

### Explicación
Un **observable (observable)** es un operador hermítico (también llamado autoadjunto): `A = A†`, es decir, `⟨φ|A|ψ⟩ = ⟨ψ|A|φ⟩*` [@preskill-ph219, ch.2 §2.1, p. 4]. Los valores posibles de la medida son sus valores propios [@zwiebach-mit-8-04, LN6 §2, p. 4; LN9 §1, p. 1]. Si no recuerdas qué es una matriz hermítica o un valor propio, repasa [matrices unitarias y hermíticas](../../math-foundations/concepts/unitary-and-hermitian-matrices.md) y [valores y vectores propios](../../math-foundations/concepts/eigenvalues-and-eigenvectors.md).

Lo hermítico es lo que garantiza que los resultados sean números reales: los valores propios de un operador hermítico son reales, y también lo es su valor esperado; el valor esperado en uno de sus estados propios es ese valor propio [@zwiebach-mit-8-04, LN9 §1, pp. 1-2]. Además, los estados propios de valores propios distintos son ortogonales y pueden elegirse ortonormales, y forman una base completa: el teorema espectral enunciado en 8.04 y demostrado en 8.05 para dimensión finita [@zwiebach-mit-8-04, LN9 §1, pp. 2-3].

Esa base da la representación espectral, `A = Σₙ aₙEₙ = Σₙ |n⟩aₙ⟨n|`, con `Eₙ` proyectores ortogonales (`EₙEₘ = δₙₘEₙ`); el proyector sobre `|ψ⟩` es `|ψ⟩⟨ψ|` [@preskill-ph219, ch.2 §2.1, p. 5, ecs. 2.4-2.6]. Así el observable se conecta con la [regla de Born](born-rule-measurement.md): medir `A` en `|ψ⟩` da `aₙ` con probabilidad `⟨ψ|Eₙ|ψ⟩` y deja el estado en `Eₙ|ψ⟩` normalizado [@preskill-ph219, ch.2 §2.1, p. 5].

El promedio de los resultados es el valor esperado, `⟨A⟩ = Σₙ aₙ Prob(aₙ) = ⟨ψ|A|ψ⟩` [@preskill-ph219, ch.2 §2.1, p. 6, ec. 2.9]. Es el promedio sobre muchas copias preparadas igual [@zwiebach-mit-8-04, LN8 §2, pp. 4-5; LN9 §1, p. 4]. Para quien programa, es lo que estima un cálculo de "valor esperado" tras muchas repeticiones del circuito. Su dispersión es la incertidumbre `(ΔQ)² = ⟨Q²⟩ − ⟨Q⟩²`, que es cero exactamente cuando el estado es un estado propio de `Q` [@zwiebach-mit-8-04, LN9 §2, pp. 6-7].

En computación cuántica, medir en la base de cómputo es medir el observable cuyos estados propios son `|0⟩` y `|1⟩` (el `Z`). Las matrices de Pauli son los observables hermíticos básicos de un espín 1/2 (véase [puertas de un qubit](../../qubits-and-circuits/concepts/single-qubit-gates.md)) [@zwiebach-mit-8-05, ch.2 §2, pp. 10-11]. Los hamiltonianos son operadores hermíticos con unidades de energía y gobiernan la [evolución](unitary-time-evolution.md) [@zwiebach-mit-8-05, ch.6 §2.2, p. 15].

Al combinar observables hay una restricción. La suma de operadores hermíticos es hermítica, pero el producto `AB` solo lo es si `A` y `B` conmutan; `AB + BA` e `i(AB − BA)` siempre lo son [@preskill-ph219, ch.2 §2.1, pp. 4-5]. Si no conmutan, no hay base común de estados propios: es el tema de [incertidumbre y no conmutatividad](uncertainty-and-noncommutativity.md).

### Ejemplo
- Espín: `S_z = (ħ/2)diag(1,−1)` es hermítica con estados propios `|z;±⟩` y valores propios `±ħ/2` [@zwiebach-mit-8-05, ch.2 §2, pp. 8-9]. Cualquier matriz 2×2 hermítica se construye con la identidad y las tres matrices de Pauli con coeficientes reales [@zwiebach-mit-8-05, ch.2 §2, pp. 9-10]; los valores propios de cada `σᵢ` son `±1`, porque `σᵢ² = 1` y `tr σᵢ = 0` [@zwiebach-mit-8-05, ch.2 §3, p. 13]. Los detalles están en [sistemas de dos niveles](two-level-systems.md).
- Posición y momento: `x̂` multiplica por `x` y `p̂ = (ħ/i)∂/∂x`, con ondas planas como estados propios. Operadores ↔ matrices, funciones de onda ↔ vectores, estados propios ↔ vectores propios [@zwiebach-mit-8-04, LN5 §1, pp. 1-2; §2, pp. 5-6].

### Errores frecuentes
- *"Un observable es el resultado."* El observable es el operador; el resultado es uno de sus valores propios.
- *"El valor esperado es un resultado posible."* No necesariamente: es un promedio ponderado por probabilidades [@zwiebach-mit-8-04, LN9 §1, p. 4]. Por ejemplo `⟨x⟩` y `⟨p⟩` pueden ser cero para estados simétricos [@openstax-physics-3, §7.1].

### Para seguir
[Evolución temporal unitaria](unitary-time-evolution.md) muestra cómo cambia el estado entre medidas, y [incertidumbre y no conmutatividad](uncertainty-and-noncommutativity.md) qué pasa cuando dos observables no conmutan. La capa 3 trata observables de subsistemas y medidas generales.

## Profesional {#layer-3}

### Idea clave
En un registro, medir un solo qubit es medir `M_A ⊗ I_B`, y su valor esperado depende solo del estado reducido. En la práctica los valores esperados de operadores de Pauli se estiman midiendo en varios ejes y repitiendo [@preskill-ph219, ch.2 §2.3.1, p. 18; §2.2.1, p. 13].

### Explicación
Un observable sobre el subsistema A de un sistema A+B se escribe `M_A ⊗ I_B` [@preskill-ph219, ch.2 §2.3.1, p. 18]. Es el operador que se mide cuando solo se mide un qubit de un registro; véase [producto tensorial](../../math-foundations/concepts/tensor-products.md). Su valor esperado es `tr(M_A ρ_A)` con `ρ_A` el estado reducido, lo que enlaza con las [matrices densidad](density-matrices.md) [@preskill-ph219, ch.2 §2.3.1, p. 18].

Para un qubit, `⟨n·σ⟩` en un estado puro da la componente del espín según `n`, y medir según `n` equivale a rotar `n` a `z` y medir en `z`; hacen falta tres ejes para reconstruir el estado a partir de muchas copias [@preskill-ph219, ch.2 §2.2.1, p. 13]. Para cada dirección unitaria `n`, `S_n = n·S` es hermítica, de traza cero y con eigenvalores `±ħ/2`, como exige la equivalencia física de todas las direcciones [@zwiebach-mit-8-05, ch.2 §4, p. 16]. La estimación de valores esperados de operadores de Pauli con este procedimiento es lo que hacen las [primitivas Sampler y Estimator](../../qiskit-programming/concepts/primitives-sampler-estimator.md): el Estimator calcula valores esperados de observables sobre el estado que prepara un circuito [@qiskit-docs, /docs/en/guides/primitives].

Un operador que conmuta con el hamiltoniano se conserva: `A_H = A_S` y su valor esperado es constante [@zwiebach-mit-8-05, ch.6 §3.2, pp. 20-22]; en la imagen de Schrödinger, `[Q,H] = 0` para el generador de una simetría, de modo que simetrías y leyes de conservación se corresponden [@preskill-ph219, ch.2 §2.2.1, p. 10]. Se retoma en [evolución unitaria](unitary-time-evolution.md). Y los conmutadores corresponden a `iħ` veces los corchetes de Poisson clásicos, `[A,B] ⇔ iħ{A,B}_pb` [@zwiebach-mit-8-05, ch.6 §2.2, pp. 14-15].

Para decidir entre observable y medida general:

- Cantidad física con valores reales que se promedia (energía, magnetización): observable hermítico y valor esperado.
- Resultados de un dispositivo concreto, incluidas medidas imperfectas: POVM con la probabilidad `Tr(Pₐρ)` [@watrous-2025, L11.1, PDF p. 330]. Para observables con muchos resultados o medidas no repetibles, los POVM generalizan la idea (ver [medida y regla de Born](born-rule-measurement.md)).

### Ejemplo
Para estimar `⟨X⟩` de un qubit en un circuito, se rota el eje `x` a `z` con una puerta de cambio de base y se mide en `z` muchas veces: la media de los resultados `±1` estima `⟨X⟩`; con `⟨X⟩`, `⟨Y⟩` y `⟨Z⟩` se reconstruye el estado [@preskill-ph219, ch.2 §2.2.1, p. 13; @qiskit-docs, /docs/en/guides/primitives].

### Las fuentes discrepan
El formalismo de Watrous en las partes consultadas no tiene un "observable" aparte: describe la medida con proyecciones y matrices semidefinidas positivas que suman la identidad; los proyectores son hermíticos, y el único uso de la descomposición espectral en lo leído es la discriminación óptima de estados [@watrous-2025, L3.2, PDF pp. 85-86; L11.3, PDF p. 348]. Preskill y Zwiebach, en cambio, parten del operador hermítico.

### Para seguir
Continúa con [incertidumbre y no conmutatividad](uncertainty-and-noncommutativity.md) para la consecuencia de que dos observables no conmuten.
