---
concept: qubit
title: "El qubit"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
Un **qubit** es el equivalente cuántico del bit: un sistema con dos estados de base, `|0⟩` y `|1⟩`, que puede estar en cualquier superposición `α|0⟩ + β|1⟩` con `|α|² + |β|² = 1` [@de-wolf-2026, §1.3, p. 19; @watrous-2025, L1.2, PDF pp. 19-23].

### Explicación
Físicamente, un qubit es un [sistema de dos niveles](../../quantum-mechanics/concepts/two-level-systems.md); aquí lo tratamos como la abstracción de programación que se construye encima. Su estado es un vector unitario de amplitudes `α` y `β`, que son números complejos (ver [números complejos](../../math-foundations/concepts/complex-numbers.md) y [vectores y notación de Dirac](../../math-foundations/concepts/vectors-and-dirac-notation.md)) [@watrous-2025, L1.2, PDF pp. 19-23].

Los estados de base `|0⟩ = (1, 0)ᵀ` y `|1⟩ = (0, 1)ᵀ` se corresponden con los dos estados de un bit clásico: medir `|0⟩` da `0` con certeza, y medir `|1⟩` da `1` [@watrous-2025, L1.2, PDF p. 24]. Entre ellos hay un continuo de superposiciones. Las dos más usadas son el estado *más* `|+⟩ = (|0⟩ + |1⟩)/√2` y el estado *menos* `|−⟩ = (|0⟩ − |1⟩)/√2`; al medir `|+⟩` en la base estándar salen `0` y `1` con probabilidad 1/2 cada uno [@watrous-2025, L1.2, PDF pp. 19-23].

Al medir en la base estándar, la probabilidad de cada resultado es el cuadrado del módulo de su amplitud ([regla de Born](../../quantum-mechanics/concepts/born-rule-measurement.md)). Por eso un signo negativo o una `i` en la amplitud no cambian las probabilidades en esa base [@watrous-2025, L1.2, PDF pp. 23-24].

Aun así, `|+⟩` y `|−⟩` dan las mismas probabilidades 1/2, 1/2 y son estados distintos: si se aplica antes la puerta Hadamard, el resultado distingue uno de otro con certeza [@watrous-2025, L1.2, PDF pp. 23-24, 27]. La diferencia es una **fase relativa**. La **fase global** (multiplicar todo el estado por un número de módulo 1) no se puede observar, pero la relativa sí. Aaronson lo compara con desplazar el universo entero 20 pies a la izquierda: nada cambia [@aaronson-2018, Lec3, p. 4]. Por eso todo estado de qubit equivale, salvo fase global, a uno con coeficiente real no negativo en `|0⟩` [@watrous-2025, L9.3, PDF p. 275].

Además de `{|0⟩, |1⟩}` y `{|+⟩, |−⟩}`, los estados `|+i⟩ = (|0⟩ + i|1⟩)/√2` y `|−i⟩ = (|0⟩ − i|1⟩)/√2` forman una tercera base; quedan en el eje `y` de la [esfera de Bloch](bloch-sphere.md) [@watrous-2025, L9.3, PDF p. 279].

Una advertencia de vocabulario: "qubit" se refiere al estado de un sistema de dimensión 2. Para un registro de varios, de Wolf recomienda no llamarlo "un qubit": "de `n` qubits" solo se usa como adjetivo [@de-wolf-2026, §1.3, nota 6, p. 19]. Los registros se estudian en [estados de varios qubits](multi-qubit-states.md).

### Ejemplo
Con amplitudes complejas, `(1+2i)/3 |0⟩ − (2/3)|1⟩` es un estado válido porque `|1+2i|²/9 + 4/9 = 5/9 + 4/9 = 1` [@watrous-2025, L1.2, PDF pp. 19-20]. Al medirlo en la base estándar, la regla de Born da `0` con probabilidad 5/9 y `1` con probabilidad 4/9 [@watrous-2025, L1.2, PDF pp. 23-24].

### Errores frecuentes
- *"`|+⟩` y `|−⟩` son lo mismo porque miden igual."* Dan las mismas probabilidades en la base estándar, pero se distinguen con una puerta Hadamard previa [@watrous-2025, L1.2, PDF p. 27].
- *"Un qubit es un valor con dos números."* Son dos amplitudes complejas, pero con la normalización y descartando la fase global solo quedan dos parámetros reales [@preskill-ph219, ch.2 §2.2.1, pp. 8-9]; se ven como los dos ángulos de la esfera de Bloch.

### Para seguir
Para ver el qubit como un punto en una esfera, sigue con [la esfera de Bloch](bloch-sphere.md); para transformarlo, con [las puertas de un qubit](single-qubit-gates.md).

## Comprensión {#layer-2}

### Idea clave
El estado de un qubit varía en un continuo, pero cada medida da un resultado discreto; lo que lo distingue de un bit aleatorio es que sus amplitudes pueden ser negativas o complejas y, por eso, interferir [@watrous-2025, L1.2, PDF p. 18; @aaronson-2018, Lec3, p. 1].

### Explicación
El continuo nunca se observa directamente: solo sirve para calcular probabilidades. Aaronson señala que lo mismo ocurre con una distribución de probabilidad clásica [@aaronson-2018, Lec3, p. 1]. Con las amplitudes pasa algo parecido: de Wolf argumenta que enviar `α₀, α₁` por un canal clásico es imposible porque podrían requerir precisión ilimitada para escribirse; y las amplitudes se comportan más como probabilidades que como longitudes: Bob solo obtiene lo que podría medir [@de-wolf-2026, §1.5, p. 22; @aaronson-2018, Lec10, p. 3].

Un bit clásico aleatorio se describe con probabilidades no negativas que suman 1; un qubit, con amplitudes que pueden ser negativas o complejas, y por eso pueden cancelarse (interferencia). Toda la diferencia entre información clásica y cuántica sale de ese cambio: entradas complejas con suma de cuadrados de módulos igual a 1 [@watrous-2025, L1.2, PDF p. 18].

Esa interferencia depende de la base. Hadamard convierte la base `{0, 1}` en la `{+, −}`, y las dos son complementarias: estar totalmente seguro del resultado en una significa estar totalmente indeciso en la otra [@aaronson-2018, Lec4, p. 1]. La base estándar era una elección de convención: en general, medir en una base ortonormal da cada resultado con probabilidad igual a la proyección al cuadrado del estado sobre el vector de esa base [@aaronson-2018, Lec4, p. 1].

Un caso útil son los estados reales de un plano, `|ψ_θ⟩ = cosθ|0⟩ + sinθ|1⟩`: dan `|0⟩, |1⟩, |+⟩, |−⟩` para `θ = 0, π/2, π/4, −π/4`, y el producto interior de dos de ellos es el coseno de la diferencia de ángulos [@watrous-2025, L4.3, PDF pp. 111, 118]. Este "círculo" de estados reales se usa en el juego CHSH de [desigualdades de Bell](bell-inequalities.md).

Medir, además, no es evolucionar. La evolución unitaria es invertible, determinista y continua; la medida es irreversible, probabilística y discontinua. Conciliarlas es el problema de la medida (*measurement problem*) [@aaronson-2018, Lec4, pp. 2-3]. En programación esto se traduce en una regla práctica: las [puertas](single-qubit-gates.md) se aplican antes y la medida se hace al final, o se registra en un bit clásico ([circuitos y medida](quantum-circuits.md)).

Por último, dos estados de qubit se distinguen con certeza solo si son ortogonales; para dos no ortogonales, con probabilidades a priori iguales, la mejor base para adivinar divide el ángulo entre los dos vectores por la mitad [@aaronson-2018, Lec5, pp. 1-2]. Es la raíz del [teorema de no clonación](no-cloning.md).

### Ejemplo
Aplicar Hadamard a `|0⟩` y volver a aplicarla devuelve `|0⟩` con certeza, porque los dos caminos hacia `|1⟩` tienen amplitudes de signo contrario y se cancelan [@aaronson-2018, Lec3, p. 4; Lec4, p. 3]. Un bit probabilístico no hace eso: tras una primera mezcla 50/50, otra mezcla sigue dando 50/50 [@preskill-ph219, ch.2 §2.2.1, p. 14].

### Para seguir
La capa 3 sitúa el qubit en dispositivos reales, con su tamaño actual y sus límites por ruido.

## Profesional {#layer-3}

### Idea clave
Un qubit es un modelo matemático de dos niveles que los dispositivos realizan de formas distintas (espín del electrón, polarización del fotón, circuitos superconductores, iones), y el modelo ideal falla cuando el entorno destruye la coherencia [@preskill-ph219, ch.2 §2.2, p. 8; §2.2.2, pp. 14-15].

### Explicación
Los dispositivos actuales son pequeños: de Wolf resume que las plataformas líderes (superconductores, iones atrapados) operan con unos 100-200 qubits, y que el experimento de "supremacía" de Google de 2019 usó 53 qubits superconductores [@de-wolf-2026, §1.1, p. 14]. Cómo se construyen se ve en [qubits superconductores](../../quantum-hardware/concepts/superconducting-qubits.md) y [qubits de iones atrapados](../../quantum-hardware/concepts/trapped-ion-qubits.md); la calidad de un qubit se resume en [coherencia y fidelidad](../../quantum-hardware/concepts/coherence-and-fidelity.md).

El qubit real no está aislado: el entorno destruye la coherencia ([decoherencia](../../quantum-mechanics/concepts/decoherence.md)). La corrección de errores existe para proteger qubits lógicos hechos de muchos físicos ([ámbito de corrección de errores](../../error-correction/index.md)).

Para hacer cuentas con un qubit, escribe el estado como vector columna y usa las matrices de [puertas de un qubit](single-qubit-gates.md); para visualizar, la esfera de Bloch; para más de un qubit, los [productos tensoriales](../../math-foundations/concepts/tensor-products.md). El vector de un registro de `n` qubits tiene `2ⁿ` amplitudes ([estados de varios qubits](multi-qubit-states.md)).

### Ejemplo
Decidir si una moneda es justa o sesgada necesita del orden de un logaritmo de bits de memoria en el caso clásico, pero basta un qubit: se gira el qubit un ángulo pequeño en cada lanzamiento y se mide al final [@aaronson-2018, Lec5, p. 1]. Es un ejemplo de que el diseño con un solo qubit tiene todavía margen.

### Para seguir
La [esfera de Bloch](bloch-sphere.md) y las [puertas de un qubit](single-qubit-gates.md) llevan este modelo a la geometría y a las matrices; para registros, pasa a [estados de varios qubits](multi-qubit-states.md).
