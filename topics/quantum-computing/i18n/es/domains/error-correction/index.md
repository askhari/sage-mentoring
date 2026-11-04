---
domain: error-correction
title: "Corrección de errores y tolerancia a fallos"
---

# Corrección de errores y tolerancia a fallos

Este ámbito explica cómo se puede calcular de forma fiable con componentes que fallan. Los ámbitos anteriores mostraron que [un dispositivo real](../quantum-hardware/index.md) tiene errores y que, sin corregirlos, la [mitigación](../qiskit-programming/concepts/error-mitigation.md) solo estira lo que se puede hacer en la [era NISQ](../qiskit-programming/concepts/nisq-era.md). Aquí está la respuesta de fondo: codificar cada qubit en muchos, medir solo lo necesario para detectar errores y operar sobre los datos codificados sin exponerlos. Está pensado para quien programa: el objetivo es saber leer una afirmación del tipo "demostramos un qubit lógico" o "romper RSA necesita un millón de qubits", y calcular un presupuesto de distancia, de qubits y de tiempo.

## Por qué importa

Preskill defendía en 2018 que la corrección de errores es la base para creer que los ordenadores cuánticos escalan, y que las tecnologías transformadoras serán probablemente tolerantes a fallos, aunque esté lejos [@preskill-2018, §2, p. 2; §8, p. 16]. El resultado teórico que lo sostiene es el [teorema del umbral](concepts/threshold-theorem.md): si el error por operación es menor que un valor constante, se puede calcular durante tanto tiempo como se quiera con una sobrecarga polilogarítmica [@eisert-2025, Sec. III, p. 4]. De Wolf lo llama la respuesta principal a los escépticos, y añade que no se conoce un obstáculo fundamental, pero sí un problema de ingeniería extremadamente difícil [@de-wolf-2026, §21.6, p. 201 [189]]. Y casi todo lo que se oye sobre el futuro de la computación cuántica (cuántos qubits harían falta para romper RSA, cuándo se espera un ordenador útil) es una consecuencia de las cuentas de este ámbito.

## Cómo se conectan los conceptos

1. [Ruido cuántico y canales de error](concepts/quantum-noise-channels.md): por qué un continuo de errores se reduce a cuatro (`I`, `X`, `Y`, `Z`) y qué modelos de ruido se usan. Es el vocabulario del resto del ámbito.
2. [Códigos de repetición](concepts/repetition-codes.md): el punto de entrada para quien no ha visto corrección de errores. Votación clásica, y luego comprobaciones de paridad que no miden los datos. Tiene capa 1.
3. [Código de Shor de 9 qubits](concepts/shor-code.md): apila los dos códigos de repetición para proteger de cualquier error en un qubit [@watrous-2025, L13.2, PDF pp. 391, 397-399].
4. [Formalismo de estabilizadores](concepts/stabilizer-formalism.md): el lenguaje común de todos los códigos modernos (generadores, síndrome, distancia, operadores lógicos, Clifford).
5. [Teorema del umbral](concepts/threshold-theorem.md): por qué la corrección acaba ayudando, la fórmula `ε_d ≈ A (p/p_th)^((d+1)/2)` y cómo elegir la distancia a partir de un error objetivo.
6. [Código de superficie](concepts/surface-code.md): el código que se ejecuta hoy en hardware, y su comparación con los qLDPC.
7. [Decodificación](concepts/decoding.md): el cálculo clásico que convierte un síndrome en una corrección, con su presupuesto de tiempo.
8. [Puertas tolerantes a fallos y estados mágicos](concepts/fault-tolerant-gates.md): cómo computar sobre datos codificados; por qué las puertas `T` son lo caro.
9. [Experimentos con qubits lógicos](concepts/logical-qubit-experiments.md): lo que Google, Harvard/QuEra y otros han demostrado, con la letra pequeña.
10. [Estimación de recursos](concepts/resource-estimation.md): qubits y tiempo para un algoritmo real, y cómo leer una estimación.

## Orden de estudio recomendado

- **Camino rápido (primer contacto):** [ruido cuántico](concepts/quantum-noise-channels.md) y [códigos de repetición](concepts/repetition-codes.md) (capa 1), luego [Shor](concepts/shor-code.md) y las capas 2 de [umbral](concepts/threshold-theorem.md) y [experimentos con qubits lógicos](concepts/logical-qubit-experiments.md). Con eso entiendes qué significa "por debajo del umbral" y cómo juzgar un titular.
- **Camino de programación y algoritmos:** el camino rápido más [estabilizadores](concepts/stabilizer-formalism.md), [código de superficie](concepts/surface-code.md), la capa 3 de [umbral](concepts/threshold-theorem.md) (elegir la distancia) y la de [estimación de recursos](concepts/resource-estimation.md); después, [decodificación](concepts/decoding.md) y [puertas tolerantes a fallos](concepts/fault-tolerant-gates.md), que empiezan en la capa profesional.
- **Dependencias con otros ámbitos:** se asumen [circuitos](../qubits-and-circuits/concepts/quantum-circuits.md), [matrices de densidad](../quantum-mechanics/concepts/density-matrices.md), [no clonación](../qubits-and-circuits/concepts/no-cloning.md), [conjuntos universales de puertas](../qubits-and-circuits/concepts/universal-gate-sets.md), [valores propios](../math-foundations/concepts/eigenvalues-and-eigenvectors.md), [coherencia y fidelidad](../quantum-hardware/concepts/coherence-and-fidelity.md), [qubits superconductores](../quantum-hardware/concepts/superconducting-qubits.md), [átomos neutros](../quantum-hardware/concepts/neutral-atom-qubits.md) y [el algoritmo de Shor](../quantum-algorithms/concepts/shor-algorithm.md). La estimación de recursos retoma el tema de [criptografía poscuántica](../quantum-algorithms/concepts/post-quantum-cryptography.md).

## Una advertencia sobre las cifras y las fuentes

- **Las cifras dependen de supuestos y envejecen.** Cada umbral y cada estimación va con su modelo de ruido y su año. Fowler (2012) se muestra como histórico frente a Gidney (2025): casi todo cambió entre ambos, desde el recuento de qubits hasta el ciclo de la máquina.
- **Gidney (2025) es un preprint** (arXiv v1) y, el 4 de noviembre de 2026, no tiene referencia de revista en las notas [@gidney-2025, nota de acceso]. Sus resultados valen bajo sus hipótesis: error de puerta de 0,1 %, ciclo de 1 µs y tiempo de reacción de 10 µs.
- **Fuentes con parte interesada.** Los experimentos de Google los hacen y los cuentan sus propios autores [@google-2025, p. 7]; los de átomos neutros incluyen autores de QuEra [@bluvstein-2024, nota de acceso]; la propuesta de códigos bicicleta es de IBM y requiere un hardware (acopladores de largo alcance) que no se ha demostrado [@bravyi-2024, p. 30]; y la fotónica de Bartolucci y colaboradores son simulaciones de PsiQuantum [@bartolucci-2023, §VI, p. 9]. Se atribuyen en el texto. Eisert y Preskill son una perspectiva (preprint) [@eisert-2025, nota de acceso].
- **El preprint de Google es la versión v1 de arXiv.** El texto consultado no nombra el procesador ni confirma el DOI de la versión final; Eisert y Preskill lo llaman Willow [@eisert-2025, Sec. III, p. 4].
- **Poselección no es corrección.** Los titulares de GHZ y XEB lógicos de Bluvstein y colaboradores dependen de detección de errores con descarte de datos [@bluvstein-2024, pp. 4, 6-7].
- **Los umbrales no se pueden comparar a ciegas.** El artículo de IBM da 0,8 % en el resumen y unos 0,7 % (pseudo-umbrales de 0,0065 y 0,0069) en las tablas; pseudo-umbral y umbral son cantidades distintas [@bravyi-2024, p. 1; p. 5; p. 6]. Su ahorro de qubits sale como "más de 10 veces" en la introducción y "casi 15 veces" en la conclusión [@bravyi-2024, pp. 2, 30].
- **Las lecciones de De Wolf sobre este tema son un esbozo** que no cubre el código de superficie: da una cota rigurosa de umbral de ≈ 0,1 % y evidencia numérica de unos pocos por ciento [@de-wolf-2026, §21.1, p. 195 [183]; §21.6, p. 201 [189]]. La teoría de estabilizadores y del umbral está en Watrous [@watrous-2025, L13-L16].
- **Nombres de estados mágicos.** El artículo original de destilación (2005) usa etiquetas distintas a las de hoy; ver [puertas tolerantes a fallos](concepts/fault-tolerant-gates.md).

## Cierre del curso

Este es el último ámbito. Los hilos que se cierran aquí: la [decoherencia](../quantum-mechanics/concepts/decoherence.md) del primer ámbito, que motiva el ruido; las [puertas universales](../qubits-and-circuits/concepts/universal-gate-sets.md), que explican por qué la puerta `T` es la cara; el [algoritmo de Shor](../quantum-algorithms/concepts/shor-algorithm.md), cuyo coste real se calcula con la [estimación de recursos](concepts/resource-estimation.md); y el [hardware](../quantum-hardware/index.md), cuyos `p` y ciclos son los parámetros de esas cuentas. Para practicar con circuitos, ver [programación con Qiskit](../qiskit-programming/index.md).
