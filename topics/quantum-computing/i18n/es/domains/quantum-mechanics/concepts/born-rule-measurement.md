---
concept: born-rule-measurement
title: "Medida y regla de Born"
---

## Fundamentos {#layer-1}

**La medida cuántica es aleatoria.** Un fotón que llega a un polarizador orientado con un ángulo `α` respecto a su polarización lo atraviesa con probabilidad `cos²α`, y nadie puede predecir qué fotón pasa, aunque todos sean idénticos [@zwiebach-mit-8-04, LN1 §3, pp. 6-7]. Cada fotón se absorbe o se transmite entero (un fotón fraccionario tendría otra frecuencia), así que la fracción clásica `cos²α` de la energía de la onda se convierte en una probabilidad para cada fotón [@zwiebach-mit-8-04, LN1 §3, p. 7].

**La regla de Born (Born rule).** Born observó que en experimentos de dispersión las partículas permanecen enteras y propuso que `|Ψ(x,t)|² d³x` es la probabilidad de encontrar la partícula en ese volumen al medir en el instante `t` [@zwiebach-mit-8-04, LN5 §3, p. 8]. Dicho para estados discretos: si el estado es `Σ αᵢ|i⟩`, la medida da el resultado `i` con probabilidad `|αᵢ|²` [@zwiebach-mit-8-04, LN1 §4, p. 10]. Con la normalización `Σ|αᵢ|² = 1` las probabilidades suman 1 (ver [producto interior y norma](../../math-foundations/concepts/inner-products-and-norms.md) y [probabilidad básica](../../math-foundations/concepts/probability-basics.md)).

**Colapso.** Tras la medida, el estado pasa a ser `|i⟩` (a esto se le llama "colapso"), y repetir la medida enseguida da el mismo resultado con certeza [@zwiebach-mit-8-04, LN1 §4, p. 10; LN9 §1, p. 3].

**Ejemplo con espín.** Un átomo con espín en `|z;+⟩` medido a lo largo de `x` da `±ħ/2` con probabilidad 1/2 cada uno, porque `⟨x;±|z;+⟩ = 1/√2` [@zwiebach-mit-8-05, ch.2 §2, p. 12, ec. 2.34]. Para un qubit en `a|0⟩ + b|1⟩` medido en la base `{|0⟩,|1⟩}` los resultados tienen probabilidad `|a|²` y `|b|²`, y no se pueden determinar `a` y `b` a partir de una sola medida [@preskill-ph219, ch.2 §2.2, p. 8].

**Por qué importa en computación cuántica.** Un programa cuántico termina midiendo, y la salida es aleatoria. Como una sola medida no revela las amplitudes, los circuitos se ejecutan muchas veces y se estiman las probabilidades a partir de la frecuencia de cada resultado: son las repeticiones (*shots*) que verás en [programación con Qiskit](../../qiskit-programming/index.md). Un buen algoritmo cuántico se diseña para que la respuesta correcta tenga probabilidad alta: la clase `BQP` exige error `≤ 1/3` en toda entrada [@de-wolf-2026, §13.2, p. 123], y por ejemplo Deutsch-Jozsa acierta con probabilidad 1 si se cumple la promesa [@watrous-2025, L5.3, PDF p. 147].

## Comprensión {#layer-2}

**La regla en forma de proyectores.** Para medir un observable `A` con proyectores `Eₙ` sobre sus espacios propios, el resultado `aₙ` sale con probabilidad `‖Eₙ|ψ⟩‖² = ⟨ψ|Eₙ|ψ⟩` y el estado posterior es `Eₙ|ψ⟩` normalizado [@preskill-ph219, ch.2 §2.1, p. 5, ecs. 2.7-2.8]. Watrous lo formula igual para una familia de proyecciones `Πₐ` que suman la identidad [@watrous-2025, L3.2, PDF p. 87]. La medida en la base estándar es el caso `Πₐ = |a⟩⟨a|` [@watrous-2025, L3.2, PDF p. 87]. Con valores propios degenerados, el colapso proyecta sobre la suma de las componentes degeneradas, renormalizada [@zwiebach-mit-8-04, LN9 §1, pp. 3-4]. Los resultados posibles de un observable son sus [valores propios](../../math-foundations/concepts/eigenvalues-and-eigenvectors.md); véase [observables](observables.md).

**Probabilidad con una matriz densidad.** Si el estado es `ρ`, la probabilidad del resultado `a` es `Tr(Πₐρ)`, que para un estado puro coincide con `‖Πₐ|ψ⟩‖²` [@watrous-2025, L11.1, PDF p. 329]. En la medida estándar de un qubit son las entradas diagonales `⟨0|ρ|0⟩` y `⟨1|ρ|1⟩` [@watrous-2025, L11.1, PDF p. 330].

**Por qué hay que repetir.** Como los resultados individuales son impredecibles, las probabilidades solo se determinan repitiendo sobre un conjunto de copias idénticamente preparadas [@zwiebach-mit-8-04, LN9 §1, p. 4; LN1 §4, pp. 11-12]. El valor esperado `⟨Q⟩` es ese promedio sobre muchas copias [@zwiebach-mit-8-04, LN8 §2, pp. 4-5]. El caso de la doble rendija lo ilustra: cada electrón llega a un punto aparentemente aleatorio y el patrón de interferencia aparece estadísticamente [@openstax-physics-3, §6.6]. En computación esto es la razón de los *shots*; cuántos hacen falta se analiza con las cotas de [probabilidad básica](../../math-foundations/concepts/probability-basics.md).

**La medida perturba.** Salvo que `a` o `b` sean cero, la medida de un qubit perturba irrevocablemente el estado [@preskill-ph219, ch.2 §2.2, p. 8]. Un filtro de Stern-Gerlach con una salida bloqueada prepara un estado definido [@zwiebach-mit-8-05, ch.2 §1, p. 5], y después de filtrar `S_x = −ħ/2`, los átomos ya no tienen `S_z = +ħ/2`: al medir `S_z` salen `±ħ/2` con probabilidad 1/2 [@zwiebach-mit-8-05, ch.2 §1, pp. 6-7].

**Dos formas de cambiar un estado.** La evolución unitaria es determinista y la medida es probabilística; la diferencia sin explicar entre ambas es el **problema de la medida (measurement problem)** [@preskill-ph219, ch.2 §2.1, p. 7]. Véase [evolución unitaria](unitary-time-evolution.md).

**Errores frecuentes.**

- *"La probabilidad es `|α|`."* Es `|α|²`.
- *"Los resultados aleatorios se deben a un aparato imperfecto."* Los intentos de explicaciones con variables ocultas son comprobables; tras el trabajo de Bell los experimentos descartan la mayoría de versiones y nadie ha encontrado cómo restablecer el determinismo [@zwiebach-mit-8-04, LN1 §3, p. 7; §5, p. 14].
- *"La medida cambia la amplitud poco a poco."* La regla de Born da probabilidades y el estado posterior es el resultado concreto [@preskill-ph219, ch.2 §2.1, p. 5].

## Profesional {#layer-3}

**Medidas generales (POVM).** Además de las proyectivas, se pueden usar matrices semidefinidas positivas `P₀,…,P_{m−1}` que suman la identidad; el resultado `a` tiene probabilidad `Tr(Pₐρ)`, que es no negativa y suma 1 [@watrous-2025, L11.1, PDF p. 330]. Toda medida proyectiva es general [@watrous-2025, L11.1, PDF p. 330]. Hay ejemplos no proyectivos, como una medida de dos resultados sobre `|+⟩` con probabilidades 5/6 y 1/6, o la medida "tetraédrica" de cuatro resultados `Pₐ = |φₐ⟩⟨φₐ|/2` con cuatro estados en los vértices de un tetraedro de la esfera de Bloch [@watrous-2025, L11.1, PDF pp. 331-333].

**Con operadores de medida.** Preskill expresa la medida generalizada con operadores `Mₐ` con `ΣMₐ†Mₐ = I`: el resultado `a` tiene probabilidad `‖Mₐ|ψ⟩‖²`, los estados posteriores no tienen por qué ser ortogonales y la medida no es repetible; los `Eₐ = Mₐ†Mₐ` forman un POVM [@preskill-ph219, ch.3 §3.1.2, pp. 8-10]. Un POVM da probabilidades `p(a) = tr(ρEₐ)` pero no fija el estado posterior [@preskill-ph219, ch.3 §3.1.2, pp. 10-11]. Equivalentemente, con matrices de Kraus `Aₐ`, la probabilidad es `Tr(AₐρAₐ†)` y el estado posterior `AₐρAₐ†` normalizado [@watrous-2025, L11.2, PDF pp. 344-346].

**Toda medida general es una medida proyectiva más una ancilla.** Teorema de Naimark: se añade una ancilla en `|0⟩`, se aplica una unitaria y se mide la ancilla en la base estándar [@watrous-2025, L11.2, PDF pp. 341-343]; análogamente, un POVM es una medida ortogonal sobre sistema más ancilla [@preskill-ph219, ch.3 §3.1.2, pp. 10-11].

**Modelo físico de medida (von Neumann).** Se mide un observable `M` acoplándolo a un puntero (`H ~ λ M ⊗ P`): la posición del puntero queda correlacionada con el valor propio, y leerla proyecta el sistema sobre un estado propio con probabilidad `|⟨a|φ⟩|²`; Stern-Gerlach es el ejemplo para `σ₃` [@preskill-ph219, ch.3 §3.1.1, pp. 5-7]. Si el resultado no se registra, el estado pasa a `Σₐ Eₐ ρ Eₐ` [@preskill-ph219, ch.3 §3.1.1, pp. 7-8]. Esto conecta con la [decoherencia](decoherence.md): una medida cuyo resultado se descarta es equivalente a un canal de defasado completo [@watrous-2025, L11.1, PDF pp. 327-329].

**Medidas en otra base.** Medir a lo largo de un eje `n` equivale a rotar `n` a `z` y medir en `z` [@preskill-ph219, ch.2 §2.2.1, p. 13]. Medir solo en `z` da `|a|` y `|b|` pero no la fase relativa; hacen falta tres ejes para determinar el estado a partir de muchas copias [@preskill-ph219, ch.2 §2.2.1, p. 13]. En la práctica: si tu circuito codifica información en la fase, añade una puerta de cambio de base antes de medir (véase [puertas de un qubit](../../qubits-and-circuits/concepts/single-qubit-gates.md)).

**El problema de la medida: posiciones.** Las fuentes lo tratan así:

- Zwiebach dice que el postulado de medida "sigue la interpretación de Copenhague" [@zwiebach-mit-8-04, LN9 §1, p. 4]; OpenStax añade que es la más enseñada y que el gato de Schrödinger fue una crítica [@openstax-physics-3, §7.1].
- Zurek señala que von Neumann mostró que no hay lugar para un colapso real en modelos de medida puramente unitarios [@zurek-2003, §II, p. 5]. Una premedida unitaria correlaciona aparato y sistema y da un estado entrelazado, no un resultado único [@zurek-2003, §II.A, pp. 5-6].
- Según Zurek, la interpretación de Copenhague pone una frontera cuántico-clásica "por decreto", y Many Worlds deja sin responder la cuestión de la base preferida; la decoherencia aporta esa base [@zurek-2003, §I.A.1-2, pp. 2-4]. Él mismo aclara que su enfoque no es completo ni universalmente aceptado [@zurek-2003, §IX, p. 51].
- Zurek afirma que la regla de Born se deduciría de la envariancia, algo presentado como novedoso y todavía en investigación [@zurek-2003, §I.C, p. 4; §IX, p. 51].

Para programar no hace falta decidir: las distintas posiciones coinciden en las probabilidades de resultado `[unverified]`.

**Criterio práctico.** Si solo necesitas probabilidades de salida: Born con proyectores (o POVM). Si importa el estado posterior (medidas a mitad de circuito, corrección de errores): usa el estado posterior de la medida concreta, que no es único en medidas generales [@watrous-2025, L11.2, PDF pp. 344-346].
