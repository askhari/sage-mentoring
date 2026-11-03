---
domain: qubits-and-circuits
title: "Qubits, puertas y circuitos"
---

# Qubits, puertas y circuitos

Este es el ámbito donde la matemática y la física de los dos anteriores se convierten en un modelo de programación: el **qubit** como unidad de información, las **puertas** como instrucciones y el **circuito** como programa. Está pensado para quien programa: usa el álgebra lineal de [matemáticas para lo cuántico](../math-foundations/index.md) (notación de Dirac, matrices unitarias, productos tensoriales) y las reglas de [fundamentos de mecánica cuántica](../quantum-mechanics/index.md) (superposición, regla de Born, sistemas de dos niveles, decoherencia) sin repetirlas.

## Por qué importa

Un algoritmo cuántico se escribe como un circuito: unos qubits que empiezan en `|0⟩`, una secuencia de puertas y una medida final que devuelve bits clásicos [@preskill-ph219, ch.5 §5.3, pp. 22-23; @de-wolf-2026, §2.1.2, pp. 26-27]. Todo lo que viene después (algoritmos, programación con Qiskit, hardware, corrección de errores) se apoya en este lenguaje. Además, el ámbito incluye los tres protocolos que muestran *qué se gana* con el entrelazamiento, y que no tienen equivalente clásico: [teleportación](concepts/quantum-teleportation.md), [codificación superdensa](concepts/superdense-coding.md) y el juego CHSH de las [desigualdades de Bell](concepts/bell-inequalities.md) [@watrous-2025, L4, PDF p. 101].

## Cómo se conectan los conceptos

Los conceptos forman dos bloques: construir un circuito (1-7) y entender qué se puede y qué no se puede hacer con él (8-12).

1. [El qubit](concepts/qubit.md): el estado `α|0⟩ + β|1⟩`, la fase relativa y la medida.
2. [Esfera de Bloch](concepts/bloch-sphere.md): los estados de un qubit como puntos de una esfera; las puertas como giros.
3. [Puertas de un qubit](concepts/single-qubit-gates.md): `X`, `Y`, `Z`, `H`, `S`, `T` como matrices unitarias 2×2.
4. [Estados de varios qubits](concepts/multi-qubit-states.md): `2ⁿ` amplitudes, estados producto y orden de los qubits.
5. [Entrelazamiento](concepts/entanglement.md): estados que no son producto; el par de Bell paso a paso.
6. [Puertas de dos qubits](concepts/two-qubit-gates.md): `CNOT` y puertas controladas, la fuente de entrelazamiento.
7. [Circuitos cuánticos y medida](concepts/quantum-circuits.md): cables, puertas, medidas, tamaño y profundidad.
8. [Teorema de no clonación](concepts/no-cloning.md): por qué no se copia un qubit desconocido.
9. [Conjuntos universales de puertas](concepts/universal-gate-sets.md): qué repertorio basta para aproximar cualquier unitaria.
10. [Teleportación cuántica](concepts/quantum-teleportation.md): enviar un estado con un e-bit y dos bits clásicos.
11. [Codificación superdensa](concepts/superdense-coding.md): enviar dos bits con un qubit y un e-bit.
12. [Desigualdades de Bell y juego CHSH](concepts/bell-inequalities.md): el entrelazamiento supera a cualquier estrategia clásica.

## Orden de estudio recomendado

Sigue la lista. Los siete primeros conceptos tienen capa 1 y se leen en este orden porque cada uno usa el anterior: `qubit` y `esfera de Bloch` describen un qubit; `puertas de un qubit` lo transforman; `estados de varios qubits` y `entrelazamiento` pasan a dos; `puertas de dos qubits` y `circuitos` los unen en programas. Si vas con prisa, el camino mínimo hasta el par de Bell es: qubit, puertas de un qubit, estados de varios qubits, puertas de dos qubits, entrelazamiento.

Los cinco últimos empiezan en capa 2. `No clonación` y `conjuntos universales` pueden leerse en cualquier orden tras los circuitos; la teleportación necesita entrelazamiento, circuitos y no clonación; la codificación superdensa, entrelazamiento y circuitos; las desigualdades de Bell, solo entrelazamiento.

## Una convención que conviene fijar desde el principio

En estas páginas el primer qubit se escribe a la izquierda del ket (`|01⟩` es el qubit 0 en `0`, el qubit 1 en `1`, en orden de lectura). Qiskit usa la convención inversa: `q_0` arriba en el circuito y a la derecha de la cadena; Watrous la describe como una inversión de la convención más común y una fuente frecuente de confusión [@watrous-2025, L3.1, PDF p. 74]. Se avisa cada vez que importa; ver [producto tensorial](../math-foundations/concepts/tensor-products.md).

## Hacia dónde sigue

Con este ámbito dominado, [algoritmos cuánticos](../quantum-algorithms/index.md) usa circuitos para resolver problemas; [programación con Qiskit](../qiskit-programming/index.md) los escribe en código; [cómo se construyen los ordenadores cuánticos](../quantum-hardware/index.md) explica qué dispositivos físicos implementan qubits y puertas; y [corrección de errores](../error-correction/index.md) explica cómo proteger la información cuando el ruido deteriora las puertas.
