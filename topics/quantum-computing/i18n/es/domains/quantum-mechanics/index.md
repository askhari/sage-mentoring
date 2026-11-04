---
domain: quantum-mechanics
title: "Fundamentos de mecánica cuántica"
format: 2
---

# Fundamentos de mecánica cuántica

Este ámbito reúne la física que hay detrás de la computación cuántica: por qué el mundo microscópico no se describe con la mecánica clásica, qué reglas tiene la teoría y cómo se conectan con los qubits y las puertas que verás después. Está pensado para quien programa: usa las matemáticas del ámbito anterior ([matemáticas para lo cuántico](../math-foundations/index.md)) en lugar de repetirlas, y cada concepto explica desde el principio para qué sirve en computación cuántica.

## Por qué importa

Un algoritmo cuántico se lee como álgebra lineal con reglas de medida, pero esas reglas vienen de la física. Preskill resume la mecánica cuántica de sistemas cerrados en cinco axiomas: estados, observables, medida, dinámica y sistemas compuestos [@preskill-ph219, ch.2 §2.1, p. 3]. Cada axioma corresponde a una pieza del cálculo cuántico: el estado es el vector de amplitudes, la dinámica son las puertas unitarias, la medida da la salida aleatoria, y los sistemas compuestos llevan al entrelazamiento. Y como los dispositivos reales no están aislados, hace falta además el marco de sistemas abiertos (matrices densidad y decoherencia), que explica el ruido [@preskill-ph219, ch.2 §2.1, p. 3].

## Cómo se conectan los conceptos

1. [Cuantización y dualidad onda-partícula](concepts/quantization-and-wave-particle.md): los experimentos que obligaron a abandonar la física clásica (fotoeléctrico, Compton, De Broglie).
2. [Principio de superposición](concepts/superposition-principle.md): las amplitudes se suman y producen interferencia; la herramienta central de los algoritmos.
3. [El estado cuántico como vector](concepts/state-vector-postulate.md): el primer axioma; el estado como vector complejo de norma 1, con fase global irrelevante y fase relativa decisiva.
4. [Medida y regla de Born](concepts/born-rule-measurement.md): el cuadrado del módulo da probabilidades; por eso los circuitos se repiten (*shots*).
5. [Observables](concepts/observables.md): las magnitudes medibles como operadores hermíticos y sus valores propios.
6. [Evolución temporal unitaria](concepts/unitary-time-evolution.md): la dinámica determinista; origen físico de las puertas.
7. [Sistemas de dos niveles (espín 1/2)](concepts/two-level-systems.md): el ejemplo más pequeño y el que se convierte en el qubit; se puede leer pronto como ilustración.
8. [Incertidumbre y no conmutatividad](concepts/uncertainty-and-noncommutativity.md): por qué hay medidas incompatibles.
9. [Matrices densidad y estados mixtos](concepts/density-matrices.md): estados con ruido o de subsistemas.
10. [Decoherencia](concepts/decoherence.md): cómo el entorno destruye la coherencia; el problema que la corrección de errores resuelve.

## Orden de estudio recomendado

Sigue la lista. Los cuatro primeros conceptos son de capa 1 y se pueden leer sin conocimientos de física más allá de las matemáticas del ámbito anterior; "sistemas de dos niveles" también tiene capa 1 y se puede leer después de "El estado cuántico como vector" para tener un ejemplo concreto. Observables, evolución, incertidumbre, matrices densidad y decoherencia empiezan en capa 2. Después sigue el ámbito [Qubits, puertas y circuitos](../qubits-and-circuits/index.md), que convierte estas ideas en abstracciones de programación: el qubit, la esfera de Bloch y las puertas.

## Fundamentos {#layer-1}

La capa de fundamentos presenta la física mínima para seguir un algoritmo cuántico. Empieza por los experimentos que obligaron a abandonar la mecánica clásica, sigue con el principio de superposición y la interferencia, y formaliza el estado como un vector de norma 1 cuyo cuadrado de amplitud da probabilidades al medir. Cierra con el sistema de dos niveles, el ejemplo más pequeño y el que se convierte en el qubit. Se apoya en las matemáticas del ámbito anterior (vectores, producto interior, probabilidad).

## Comprensión {#layer-2}

La capa de comprensión completa los cinco axiomas y explica por qué los circuitos reales se desvían del modelo ideal. Primero los observables como operadores hermíticos, la evolución unitaria que da origen a las puertas y la incertidumbre como consecuencia de que los operadores no conmutan. Después las matrices densidad, que describen estados con ruido o partes de un sistema mayor, y la decoherencia, que usa esa herramienta para explicar la pérdida de coherencia. Se apoya en la capa de fundamentos de este ámbito y en los valores propios y las matrices hermíticas.

## Profesional {#layer-3}

La capa profesional lleva el formalismo a criterios de uso: medidas generales (POVM), observables de subsistemas y su estimación, hamiltonianos que se convierten en puertas, canales cuánticos y modelos de ruido con sus parámetros `T₁` y `T₂`, y cuándo conviene un vector de estado o una matriz densidad. Se apoya en las dos capas anteriores y enlaza con los ámbitos de hardware y corrección de errores.

## Qué verás aquí y qué no

- Se presenta la física al nivel necesario para computación cuántica. Las fuentes principales son los cursos 8.04 y 8.05 de MIT [@zwiebach-mit-8-04, LN1-LN9; @zwiebach-mit-8-05, ch.2, ch.6], los apuntes de Preskill [@preskill-ph219, ch.2-3], el libro de Watrous [@watrous-2025, L9-L12], OpenStax como apoyo introductorio [@openstax-physics-3, §6-7] y la revisión de Zurek sobre decoherencia [@zurek-2003, §I-IX].
- Las interpretaciones de la mecánica cuántica (qué es "realmente" el colapso) se presentan de forma neutra, atribuyendo cada posición a su fuente.
- Lagunas: las fuentes consultadas no desarrollan la precesión de un espín en un campo magnético, ni demuestran la cota de Heisenberg general a partir del conmutador; en esos puntos el texto lo indica.
