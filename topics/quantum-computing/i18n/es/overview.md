---
title: "Computación cuántica"
---

# Computación cuántica

## Qué es este tema

La computación cuántica (quantum computing), tal como se trata aquí, es el conjunto de conocimientos necesarios para entender y programar ordenadores que procesan información codificada en sistemas cuánticos: la matemática y la física que hay detrás, el modelo de qubits y circuitos, los algoritmos que sacan partido de él, la práctica con Qiskit, las tecnologías con que se construyen los dispositivos y la corrección de errores. El enfoque es el de quien programa: se prioriza saber escribir, leer y juzgar circuitos y afirmaciones, sin perder la base de álgebra lineal y mecánica cuántica.

El punto de partida es que el estado de un sistema cuántico es un vector de números complejos cuyos cuadrados de módulo suman 1, y que de ese cambio salen todas las diferencias con la información clásica [@watrous-2025, L1.2, p. 18]. Un algoritmo cuántico se escribe como un circuito: qubits que empiezan en `|0⟩`, una secuencia de puertas y una medida final que devuelve bits clásicos [@preskill-ph219, ch.5 §5.3, pp. 22-23; @de-wolf-2026, §2.1.2, pp. 26-27]. Y un circuito por sí solo no es más rápido que uno clásico: el recurso central es la interferencia, y sin ella valdría un ordenador clásico aleatorizado [@aaronson-2018, Lec16, p. 3].

## Por qué importa

Hay dos razones prácticas. La primera es la criptografía: Shor es el principal ejemplo que cita Watrous de algoritmo cuántico de coste polinómico para un problema sin algoritmo clásico polinómico conocido [@watrous-2025, L6 intro, PDF p. 161; L7.3, PDF pp. 220-233], y la criptografía de clave pública actual se apoya en la dificultad de esos problemas [@nist-ir-8547, §2], lo que ha puesto en marcha la migración a estándares poscuánticos. La segunda es que el campo está lleno de titulares ("récord de qubits", "ventaja cuántica", "qubit lógico") que solo se interpretan bien con vocabulario: Preskill advertía en 2018 de que el número de qubits no es la única medida de un dispositivo, y cuentan también la precisión de las puertas, su velocidad, la lectura, la conectividad y el rendimiento de fabricación [@preskill-2018, §4.2, p. 5].

Conviene una cautela sobre el estado actual (a 4 de noviembre de 2026, según las fuentes del tema). Preskill defendía en 2018 que la corrección de errores es la base para creer que estos ordenadores escalan y que las tecnologías transformadoras serán probablemente tolerantes a fallos, aunque esté lejos [@preskill-2018, §2, p. 2; §8, p. 16]. Los dispositivos actuales se describen como la era NISQ (noisy intermediate-scale quantum) [@preskill-2018, §4.1, pp. 4-5], las reclamaciones de ventaja se discuten caso por caso, y las estimaciones de recursos para romper RSA son estimaciones bajo supuestos concretos, en un preprint [@gidney-2025, nota de acceso]. Este tema enseña a leer esas afirmaciones, no a darlas por buenas.

## Los siete ámbitos, en orden de estudio

1. **[Matemáticas para lo cuántico](domains/math-foundations/index.md).** Un repaso de álgebra lineal y probabilidad para quien programa: números complejos, vectores y notación de Dirac, matrices unitarias y hermíticas, valores propios y producto tensorial. Es el lenguaje de todo lo demás [@axler-2024, §1A, 6A, 7B; @watrous-2025, L1.1, L1.2].
2. **[Fundamentos de mecánica cuántica](domains/quantum-mechanics/index.md).** La física detrás de las reglas: cuantización, superposición, estado, medida y regla de Born, observables, entrelazamiento y decoherencia. Preskill resume los sistemas cerrados en cinco axiomas y añade el marco de sistemas abiertos para explicar el ruido [@preskill-ph219, ch.2 §2.1, p. 3].
3. **[Qubits, puertas y circuitos](domains/qubits-and-circuits/index.md).** El modelo de programación: el qubit, la esfera de Bloch, las puertas de uno y dos qubits, el entrelazamiento, los circuitos y tres protocolos (teleportación, codificación superdensa y juego CHSH) que no tienen equivalente clásico [@watrous-2025, L4, PDF p. 101].
4. **[Algoritmos cuánticos](domains/quantum-algorithms/index.md).** Dónde hay ventaja y dónde no: Deutsch-Jozsa y Simon dan separaciones exponenciales solo en el modelo de consultas [@de-wolf-2026, §2.4, p. 29], Grover ofrece una ventaja cuadrática y es óptimo [@watrous-2025, L8.5, PDF p. 258], y Shor motiva el interés por la criptografía poscuántica. Incluye simulación de hamiltonianos y complejidad (BQP).
5. **[Programación con Qiskit](domains/qiskit-programming/index.md).** Qiskit es el SDK de código abierto de IBM Quantum [@javadi-abhari-2024, p. 1]. El ámbito sigue sus cuatro pasos (mapear, optimizar, ejecutar, postprocesar) [@qiskit-docs, /guides/intro-to-patterns]: circuitos, simuladores, primitivas, transpilación, ejecución en hardware, mitigación de errores, algoritmos variacionales y la era NISQ. El código está probado con `qiskit 2.6.1`.
6. **[Cómo se construyen los ordenadores cuánticos](domains/quantum-hardware/index.md).** Qué es físicamente un qubit en cada tecnología (superconductores, iones, átomos neutros, fotones, espines, topológicos), qué métricas describen su calidad, qué se ha reclamado como ventaja y cómo leer la ficha de un proveedor. Las cifras van fechadas y muchas fuentes son de fabricantes [@divincenzo-2000, p. 2 §III; @kjaergaard-2020, §2, pp. 3-4].
7. **[Corrección de errores y tolerancia a fallos](domains/error-correction/index.md).** Cómo calcular de forma fiable con componentes que fallan: códigos de repetición, código de Shor, estabilizadores, teorema del umbral, código de superficie, decodificación, puertas tolerantes a fallos y estimación de recursos. El teorema del umbral dice que, con error por operación por debajo de un valor constante, se puede calcular tanto tiempo como se quiera con sobrecarga polilogarítmica [@eisert-2025, Sec. III, p. 4].

Cada ámbito se apoya en los anteriores, y los conceptos enlazan con los de otros ámbitos que necesitan. El índice de cada ámbito explica el orden recomendado de sus conceptos y las advertencias sobre las fuentes.

## Cómo funcionan las capas

Cada concepto se explica en varias capas, de lo más sencillo a lo más especializado. No hace falta terminar una capa entera para empezar la siguiente:

- **Capa 0 · Orientación:** esta página.
- **Capa 1 · Fundamentos:** qué es cada idea, con ejemplos sencillos y pequeños fragmentos de código o circuitos. [Índice de la capa 1](layers/layer-1.md).
- **Capa 2 · Comprensión:** por qué ocurre, con más matices, excepciones y relaciones entre conceptos. [Índice de la capa 2](layers/layer-2.md).
- **Capa 3 · Profesional:** cifras, criterios para decidir, estimaciones y debates abiertos. [Índice de la capa 3](layers/layer-3.md).

Un concepto empieza en la capa en la que tiene sentido explicarlo: el tema tiene 69 conceptos, de los que 35 empiezan en la capa 1, 28 en la 2 y 6 en la 3. Cada concepto tiene preguntas en todas sus capas, que se pueden practicar en el chat o repasar en Anki.

## Recorridos sugeridos

- **Programar y ejecutar cuanto antes.** Capa 1 de *Qubits, puertas y circuitos* (camino mínimo hasta el par de Bell); después, *Programación con Qiskit*: circuitos, simuladores y la era NISQ. Vuelve a *Matemáticas para lo cuántico* y *Fundamentos de mecánica cuántica* cuando surjan dudas sobre el porqué.
- **Hacia los algoritmos.** *Matemáticas para lo cuántico*, *Fundamentos de mecánica cuántica* y *Qubits, puertas y circuitos* en orden, y después *Algoritmos cuánticos* siguiendo sus tres hilos (consultas, Fourier, límites e impacto). Cierra con la estimación de recursos de *Corrección de errores* para ver qué costaría ejecutarlos.
- **Hardware e industria.** Capa 1 de *Qubits, puertas y circuitos*, la era NISQ de *Programación con Qiskit*, y después *Cómo se construyen los ordenadores cuánticos* y *Corrección de errores*, que enseñan a juzgar un anuncio con sus fechas y supuestos.
- **A fondo.** Recorre los siete ámbitos en orden, cada uno hasta la capa 3, haciendo las preguntas de cada capa antes de pasar a la siguiente.

## Sobre las fuentes

Toda afirmación lleva su fuente, y lo que no se ha podido respaldar se marca en el texto como "sin verificar". Las fuentes se clasifican por fiabilidad: A (manuales, cursos universitarios, normas y documentación oficial), B (artículos y revisiones revisados por pares, y algunos preprints de autores de referencia, señalados como tales en el texto) y C (material de apoyo). La clasificación no depende de quién firma: un artículo revisado por pares escrito por una empresa es B, pero sus afirmaciones se atribuyen a la empresa. En hardware y corrección de errores, muchas fuentes las escriben los propios fabricantes o grupos que defienden su plataforma, y varias cifras proceden de preprints: cada índice de ámbito lo señala.
