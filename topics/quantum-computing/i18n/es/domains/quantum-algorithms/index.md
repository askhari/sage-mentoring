---
domain: quantum-algorithms
title: "Algoritmos cuánticos"
format: 2
---

# Algoritmos cuánticos

Este es el ámbito donde los circuitos se convierten en soluciones: los **algoritmos cuánticos** son recetas para organizar la interferencia de modo que las respuestas erróneas se cancelen y la correcta se refuerce. Está pensado para quien programa: usa los circuitos de [qubits, puertas y circuitos](../qubits-and-circuits/index.md), el álgebra de [matemáticas para lo cuántico](../math-foundations/index.md) (en especial valores propios y números complejos) y la regla de medida de [fundamentos de mecánica cuántica](../quantum-mechanics/index.md), y no los repite.

## Por qué importa

Un circuito cuántico por sí solo no es más rápido que uno clásico: la interferencia es el recurso central, y sin ella valdría un ordenador clásico aleatorizado [@aaronson-2018, Lec16, p. 3]. Este ámbito enseña dónde sí hay ventaja y, con la misma importancia, dónde no: Deutsch-Jozsa y Simon dan separaciones exponenciales solo en el modelo de consultas [@de-wolf-2026, §2.4, p. 29]; Grover ofrece una ventaja cuadrática y es óptimo [@watrous-2025, L8.5, PDF p. 258]; y Shor es el principal ejemplo que cita Watrous de algoritmo cuántico de coste polinómico para un problema sin algoritmo clásico polinómico conocido [@watrous-2025, L6 intro, PDF p. 161; L7.3, PDF pp. 220-233]. De ese último sale el interés práctico y político del campo: la criptografía de clave pública actual se apoya en la dificultad de factorizar y de calcular logaritmos discretos [@nist-ir-8547, §2.1.1-2.1.2, pp. 3-4].

## Cómo se conectan los conceptos

Hay tres hilos que se cruzan.

**Hilo de consultas (oráculos).**

1. [Modelo de consultas y oráculos](concepts/query-model-and-oracles.md): la entrada como caja negra y el coste como número de consultas.
2. [Retroceso de fase](concepts/phase-kickback.md): cómo una consulta de bits se convierte en una fase.
3. [Algoritmo de Deutsch-Jozsa](concepts/deutsch-jozsa.md): el primer ejemplo con ventaja, y el patrón Hadamard-oráculo-Hadamard.
4. [Algoritmos de Bernstein-Vazirani y de Simon](concepts/bernstein-vazirani-and-simon.md): el mismo patrón extrae estructura oculta; Simon inspiró a Shor [@watrous-2025, L5.4, PDF p. 152].

**Hilo de Fourier (periodos y fases).**

5. [Transformada cuántica de Fourier](concepts/quantum-fourier-transform.md): la DFT como unitaria con `O(n²)` puertas.
6. [Estimación de fase](concepts/phase-estimation.md): lee el valor propio de una unitaria con retroceso de fase y QFT inversa.
7. [Algoritmo de Shor (factorización)](concepts/shor-algorithm.md): reducción clásica a cálculo del orden, y el orden por estimación de fase.

**Hilo de límites e impacto.**

8. [Búsqueda de Grover y amplificación de amplitud](concepts/grover-search.md): ventaja cuadrática con consultas, y la técnica general de amplificación.
9. [Simulación de hamiltonianos](concepts/hamiltonian-simulation.md): el uso más natural de un ordenador cuántico, según la propuesta original de Feynman [@de-wolf-2026, §9.1, pp. 83-84].
10. [Complejidad cuántica (BQP) y límites de la ventaja](concepts/quantum-complexity.md): dónde encaja `BQP` y qué demuestran de verdad los resultados anteriores.
11. [Impacto en la criptografía y criptografía poscuántica](concepts/post-quantum-cryptography.md): qué rompe Shor, qué no, y la migración a estándares poscuánticos.

## Orden de estudio recomendado

Sigue la lista, con estas notas:

- Los dos hilos iniciales (consultas y Fourier) son casi independientes; puedes saltar a la [QFT](concepts/quantum-fourier-transform.md) tras los circuitos, pero la [estimación de fase](concepts/phase-estimation.md) necesita ya el [retroceso de fase](concepts/phase-kickback.md).
- Tienen capa 1 el [modelo de consultas](concepts/query-model-and-oracles.md), [Deutsch-Jozsa](concepts/deutsch-jozsa.md) y [Grover](concepts/grover-search.md), que pueden leerse enseguida; [Shor](concepts/shor-algorithm.md) y la [criptografía](concepts/post-quantum-cryptography.md) también tienen capa 1 y son una buena lectura temprana si te interesa el impacto, aunque su comprensión plena exige los conceptos del hilo de Fourier.
- [Simulación de hamiltonianos](concepts/hamiltonian-simulation.md) solo tiene capa profesional: léela tras la estimación de fase.
- [Complejidad cuántica](concepts/quantum-complexity.md) se entiende mejor al final, cuando ya conoces Shor y Grover.

Camino mínimo para ver una ventaja real de principio a fin: modelo de consultas, Deutsch-Jozsa, Grover y, con prisa, la capa 1 de Shor y de la criptografía.

## Fundamentos {#layer-1}

La capa de fundamentos presenta los algoritmos como ideas que se pueden seguir sin el aparato matemático completo. Empieza por el modelo de consultas y los oráculos, que fijan cómo se cuenta el coste; sigue con Deutsch-Jozsa, el primer ejemplo con ventaja, y con Grover, que muestra una ventaja cuadrática y óptima; y termina con la idea de Shor (reducir factorizar a hallar el orden) y su impacto en la criptografía, con el primer estándar poscuántico. Se apoya en los circuitos de qubits y puertas.

## Comprensión {#layer-2}

La capa de comprensión explica por qué funcionan. Empieza por el retroceso de fase, que convierte una consulta de bits en una de fase, y por Bernstein-Vazirani y Simon, que extraen estructura oculta con el mismo circuito; sigue con la transformada cuántica de Fourier y la estimación de fase, que dan la maquinaria de periodos y fases que usa Shor con detalle, y cierra con la complejidad cuántica y los límites de la ventaja. Se apoya en la capa de fundamentos de este ámbito y en los valores propios y los números complejos.

## Profesional {#layer-3}

La capa profesional lleva los algoritmos a la decisión técnica. Añade la simulación de hamiltonianos, que solo existe en esta capa y da por sabida la estimación de fase; reúne las técnicas de consultas (cotas inferiores, subgrupo oculto, amplificación de amplitud), las estimaciones de recursos de Shor y los plazos y estándares de la migración poscuántica, y enseña a leer un anuncio de ventaja cuántica. Se apoya en las capas anteriores.

## Una advertencia sobre las fuentes

Los apuntes de Shor (MIT) contienen erratas señaladas en las notas de investigación; solo se usan los ejemplos numéricos sin erratas (el caso `N = 33` y las fracciones continuas de `615/2048`, comprobados a mano) [@shor-mit-2022, L21, p. 2; L22, p. 1]. Gidney (2025) es un preprint sin revisión por pares: se cita siempre con sus hipótesis [@gidney-2025, resumen, p. 1].

## Hacia dónde sigue

Con este ámbito dominado, [programación con Qiskit](../qiskit-programming/index.md) lleva estos algoritmos a código; [cómo se construyen los ordenadores cuánticos](../quantum-hardware/index.md) explica qué dispositivos podrían ejecutarlos; y [corrección de errores](../error-correction/index.md) explica cómo se llegaría a la escala que exigen Shor y sus estimaciones de recursos.
