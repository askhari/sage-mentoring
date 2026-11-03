---
concept: qubit
title: "El qubit"
---

## Fundamentos {#layer-1}

**Idea.** Un **qubit** es el equivalente cuántico del bit: un sistema con dos estados de base, `|0⟩` y `|1⟩`, que puede estar en cualquier superposición de ambos [@de-wolf-2026, §1.3, p. 19]. Es, físicamente, un [sistema de dos niveles](../../quantum-mechanics/concepts/two-level-systems.md); aquí lo tratamos como la abstracción de programación que se construye encima.

**El estado.** Un estado de qubit es un vector unitario `α|0⟩ + β|1⟩` con `|α|² + |β|² = 1` [@watrous-2025, L1.2, PDF pp. 19-23]. Los números `α` y `β` se llaman amplitudes y son complejos (ver [números complejos](../../math-foundations/concepts/complex-numbers.md) y [vectores y notación de Dirac](../../math-foundations/concepts/vectors-and-dirac-notation.md)). Ejemplos:

- `|0⟩ = (1, 0)ᵀ` y `|1⟩ = (0, 1)ᵀ`. Medir `|0⟩` da `0` con certeza, y medir `|1⟩` da `1`; así se conectan con los estados clásicos de un bit [@watrous-2025, L1.2, PDF p. 24].
- El estado *más* `|+⟩ = (|0⟩ + |1⟩)/√2`: al medir en la base estándar salen `0` y `1` con probabilidad 1/2 cada uno [@watrous-2025, L1.2, PDF pp. 19-23].
- El estado *menos* `|−⟩ = (|0⟩ − |1⟩)/√2`.
- Con amplitudes complejas, `(1+2i)/3 |0⟩ − (2/3)|1⟩` es un estado válido porque `|1+2i|²/9 + 4/9 = 5/9 + 4/9 = 1` [@watrous-2025, L1.2, PDF pp. 19-20].

**Medir.** Al medir en la base estándar, la probabilidad de cada resultado es el cuadrado del módulo de su amplitud ([regla de Born](../../quantum-mechanics/concepts/born-rule-measurement.md)). Por eso un signo negativo o una `i` en la amplitud no cambian las probabilidades en esa base [@watrous-2025, L1.2, PDF pp. 23-24].

**Dos estados que se confunden al medir pero no son iguales.** `|+⟩` y `|−⟩` dan las mismas probabilidades 1/2, 1/2 en la base estándar, y sin embargo son estados distintos: si se aplica antes la puerta Hadamard, el resultado distingue uno de otro con certeza [@watrous-2025, L1.2, PDF pp. 23-24, 27]. La diferencia entre ambos es una **fase relativa**; la **fase global** (multiplicar todo el estado por un número de módulo 1) no se puede observar, pero la relativa sí. Aaronson lo compara con desplazar el universo entero 20 pies a la izquierda: nada cambia [@aaronson-2018, Lec3, p. 4]. Por eso todo estado de qubit equivale, salvo fase global, a uno con coeficiente real no negativo en `|0⟩` [@watrous-2025, L9.3, PDF p. 275].

**Otra base.** Además de `{|0⟩, |1⟩}` y `{|+⟩, |−⟩}`, los estados `|+i⟩ = (|0⟩ + i|1⟩)/√2` y `|−i⟩ = (|0⟩ − i|1⟩)/√2` forman una tercera base; quedan en el eje `y` de la [esfera de Bloch](bloch-sphere.md) [@watrous-2025, L9.3, PDF p. 279].

**Una advertencia de vocabulario.** "Qubit" se refiere al estado de un sistema de dimensión 2. Para un registro de varios, de Wolf recomienda no llamarlo "un qubit": "de `n` qubits" solo se usa como adjetivo [@de-wolf-2026, §1.3, nota 6, p. 19]. Los registros se estudian en [estados de varios qubits](multi-qubit-states.md).

**Siguiente paso.** Para ver el qubit como un punto en una esfera, sigue con [la esfera de Bloch](bloch-sphere.md); para transformarlo, con [las puertas de un qubit](single-qubit-gates.md).

## Comprensión {#layer-2}

**Un continuo con salidas discretas.** El estado de un qubit varía en un continuo, pero cada medida solo da un resultado discreto: el continuo nunca se observa directamente, solo sirve para calcular probabilidades. Aaronson señala que lo mismo ocurre con una distribución de probabilidad clásica [@aaronson-2018, Lec3, p. 1]. Con las amplitudes pasa algo parecido: de Wolf argumenta que enviar `α₀, α₁` por un canal clásico es imposible porque podrían requerir precisión ilimitada para escribirse [@de-wolf-2026, §1.5, p. 22], y Aaronson observa que las amplitudes se comportan más como probabilidades que como longitudes: Bob solo obtiene lo que podría medir [@aaronson-2018, Lec10, p. 3].

**Más que un bit probabilístico.** Un bit clásico aleatorio se describe con probabilidades no negativas que suman 1; un qubit, con amplitudes que pueden ser negativas o complejas, y por eso pueden cancelarse (interferencia). Toda la diferencia entre información clásica y cuántica sale de ese cambio: entradas complejas con suma de cuadrados de módulos igual a 1 [@watrous-2025, L1.2, PDF p. 18]. Un ejemplo: aplicar Hadamard a `|0⟩` y volver a aplicarla devuelve `|0⟩` con certeza, porque los dos caminos hacia `|1⟩` tienen amplitudes de signo contrario [@aaronson-2018, Lec3, p. 4; Lec4, p. 3]. Un bit probabilístico no hace eso [@preskill-ph219, ch.2 §2.2.1, p. 14].

**Bases complementarias.** Hadamard convierte la base `{0, 1}` en la `{+, −}`. Las dos son complementarias: estar totalmente seguro del resultado en una significa estar totalmente indeciso en la otra [@aaronson-2018, Lec4, p. 1]. La base estándar era una elección de convención: en general, medir en una base ortonormal da cada resultado con probabilidad igual a la proyección al cuadrado del estado sobre el vector de esa base [@aaronson-2018, Lec4, p. 1].

**Estados reales en un plano.** Los estados `|ψ_θ⟩ = cosθ|0⟩ + sinθ|1⟩` dan `|0⟩, |1⟩, |+⟩, |−⟩` para `θ = 0, π/2, π/4, −π/4`, y el producto interior de dos de ellos es el coseno de la diferencia de ángulos [@watrous-2025, L4.3, PDF pp. 111, 118]. Este "círculo" de estados reales se usa en el juego CHSH de [desigualdades de Bell](bell-inequalities.md).

**Medir no es evolucionar.** La evolución unitaria es invertible, determinista y continua; la medida es irreversible, probabilística y discontinua. Conciliarlas es el problema de la medida (*measurement problem*) [@aaronson-2018, Lec4, pp. 2-3]. En programación esto se traduce en una regla práctica: las [puertas](single-qubit-gates.md) se aplican antes y la medida se hace al final, o se registra en un bit clásico ([circuitos y medida](quantum-circuits.md)).

**Distinguir estados.** Dos estados de qubit se distinguen con certeza solo si son ortogonales; para dos no ortogonales, con probabilidades a priori iguales, la mejor base para adivinar divide el ángulo entre los dos vectores por la mitad [@aaronson-2018, Lec5, pp. 1-2]. Es la raíz del [teorema de no clonación](no-cloning.md).

**Errores frecuentes.**

- *"`|+⟩` y `|−⟩` son lo mismo porque miden igual."* Dan las mismas probabilidades en la base estándar, pero se distinguen con una puerta Hadamard previa [@watrous-2025, L1.2, PDF p. 27].
- *"Un qubit es un valor con dos números."* Son dos amplitudes complejas, pero con la normalización y descartando la fase global solo quedan dos parámetros reales [@preskill-ph219, ch.2 §2.2.1, pp. 8-9]; se ven como los dos ángulos de la esfera de Bloch.

## Profesional {#layer-3}

**Qué es realmente un qubit en un dispositivo.** Un qubit es un modelo matemático de dos niveles; el espín del electrón y la polarización del fotón son dos realizaciones físicas [@preskill-ph219, ch.2 §2.2, p. 8; §2.2.2, pp. 14-15]. El tamaño de los dispositivos actuales: de Wolf resume que las plataformas líderes (superconductores, iones atrapados) operan con unos 100-200 qubits, y que el experimento de "supremacía" de Google de 2019 usó 53 qubits superconductores [@de-wolf-2026, §1.1, p. 14]. Cómo se construyen se ve en [qubits superconductores](../../quantum-hardware/concepts/superconducting-qubits.md) y [qubits de iones atrapados](../../quantum-hardware/concepts/trapped-ion-qubits.md); la calidad de un qubit se resume en [coherencia y fidelidad](../../quantum-hardware/concepts/coherence-and-fidelity.md).

**Un qubit solo ya sirve para algo.** Aaronson y Drucker muestran que decidir si una moneda es justa o sesgada necesita del orden de un logaritmo de bits de memoria en el caso clásico, pero basta un qubit: se gira el qubit un ángulo pequeño en cada lanzamiento y se mide al final [@aaronson-2018, Lec5, p. 1]. Es un ejemplo de que el diseño con un solo qubit tiene todavía margen.

**Cuándo el modelo ideal falla.** El qubit real no está aislado: el entorno destruye la coherencia ([decoherencia](../../quantum-mechanics/concepts/decoherence.md)). La corrección de errores existe para proteger qubits lógicos hechos de muchos físicos ([ámbito de corrección de errores](../../error-correction/index.md)).

**Lectura práctica.** Para hacer cuentas con un qubit, escribe el estado como vector columna y usa las matrices de la siguiente sección; para visualizar, usa la esfera de Bloch; para estados de más de un qubit, pasa a los [productos tensoriales](../../math-foundations/concepts/tensor-products.md). El vector de un registro de `n` qubits tiene `2ⁿ` amplitudes ([estados de varios qubits](multi-qubit-states.md)).
