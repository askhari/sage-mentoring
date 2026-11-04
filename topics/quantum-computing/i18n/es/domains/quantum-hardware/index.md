---
domain: quantum-hardware
title: "Cómo se construyen los ordenadores cuánticos"
---

# Cómo se construyen los ordenadores cuánticos

Este ámbito explica qué hay detrás de los dispositivos en los que se ejecutan los circuitos de [qubits, puertas y circuitos](../qubits-and-circuits/index.md) y de [programación con Qiskit](../qiskit-programming/index.md): qué es físicamente un qubit en cada tecnología, qué números describen su calidad y qué se ha demostrado de verdad. Está pensado para quien programa: el objetivo no es diseñar un chip, sino saber leer una ficha técnica, entender por qué un circuito sale "sucio" en un dispositivo y juzgar un anuncio.

## Por qué importa

Un circuito ideal no sabe nada de ruido. En la práctica, lo que limita cuántas puertas se pueden ejecutar son las fidelidades de las puertas de dos qubits, la lectura y la coherencia, y cada tecnología las logra de una manera distinta. El propio Preskill advertía en 2018 de que el número de qubits no es la única medida de un dispositivo: cuentan también la precisión de las puertas, su velocidad, la precisión de la medida, la conectividad y el rendimiento de fabricación [@preskill-2018, §4.2, p. 5]. Y casi todo lo que aparece en la prensa (un récord de qubits, una "ventaja cuántica", un "qubit lógico") se puede interpretar bien solo si se conocen las plataformas y sus métricas. Este ámbito te da ese vocabulario con cifras fechadas.

## Cómo se conectan los conceptos

1. [Criterios de DiVincenzo](concepts/divincenzo-criteria.md): la lista de requisitos que debe cumplir cualquier tecnología [@divincenzo-2000, p. 2 §III]. Es el esqueleto con el que se comparan las demás.
2. [Coherencia (T1, T2) y fidelidad de puertas](concepts/coherence-and-fidelity.md): las métricas comunes (T1, T2, fidelidad de puertas, lectura) y el cálculo de cuántas puertas caben. Incluye el caso resuelto de "probabilidad de éxito de un circuito".
3. Cuatro plataformas con capa 1, cada una con el criterio que le cuesta más:
   - [Qubits superconductores](concepts/superconducting-qubits.md): circuitos eléctricos fabricados con litografía y enfriados casi al cero absoluto; los más rápidos [@kjaergaard-2020, §2, pp. 3-4].
   - [Qubits de iones atrapados](concepts/trapped-ion-qubits.md): átomos con carga, idénticos entre sí, con la mejor coherencia y fidelidad en 2019, pero lentos [@bruzewicz-2019, pp. 3-5].
   - [Qubits de átomos neutros](concepts/neutral-atom-qubits.md): átomos sujetos con pinzas de luz, que se entrelazan por bloqueo de Rydberg, con registros muy grandes [@henriet-2020, pp. 4-5, 10; @saffman-2025, pp. 5-6].
   - [Qubits fotónicos](concepts/photonic-qubits.md): qubits en luz, buenos para comunicar, difíciles para puertas de dos qubits [@slussarenko-2019, pp. 1-2].
4. Dos plataformas con primera capa 2 (necesitan los conceptos anteriores):
   - [Qubits de espín en semiconductores](concepts/spin-qubits.md): espines de electrones o huecos en puntos cuánticos, apuesta por la integración con la industria del silicio [@stano-2022, p. 1].
   - [Qubits topológicos](concepts/topological-qubits.md): la propuesta de protección intrínseca, con un estado de evidencia que hay que leer con cuidado [@nayak-2008, pp. 9-10; @aghaee-2025, p. 8].
5. [Experimentos de ventaja cuántica](concepts/quantum-advantage-experiments.md): qué se ha reclamado (Sycamore 2019, Jiuzhang 2020, y después), cómo respondió la simulación clásica y cómo evaluar una reclamación.
6. [Comparativa y estado actual del hardware](concepts/hardware-landscape.md): todo junto, con una tabla fechada, cómo leer la ficha de un proveedor y qué plataforma mirar según la carga de trabajo.

## Orden de estudio recomendado

- **Camino rápido (primer contacto):** criterios de DiVincenzo, coherencia y fidelidad, y las capas 1 de superconductores, iones y átomos neutros. Con eso entiendes por qué los resultados de un dispositivo real salen distintos del simulador y qué diferencia a las tres plataformas que Eisert y Preskill consideran más avanzadas [@eisert-2025, Box 1, p. 3].
- **Camino profesional:** el camino rápido más las capas 2 y 3 de cada plataforma, los fotónicos, los espines, los topológicos, los experimentos de ventaja y, para cerrar, la comparativa. Los espines y los topológicos empiezan en la capa 2 porque necesitan el vocabulario de las anteriores.
- **Dependencias con otros ámbitos:** se asume [el qubit](../qubits-and-circuits/concepts/qubit.md), [los circuitos](../qubits-and-circuits/concepts/quantum-circuits.md) y [la decoherencia](../quantum-mechanics/concepts/decoherence.md); los experimentos de ventaja usan [la complejidad cuántica](../quantum-algorithms/concepts/quantum-complexity.md); y la comparativa se apoya en [la era NISQ](../qiskit-programming/concepts/nisq-era.md), [ejecutar en hardware real](../qiskit-programming/concepts/running-on-hardware.md), [transpilación](../qiskit-programming/concepts/transpilation.md) y [mitigación de errores](../qiskit-programming/concepts/error-mitigation.md).

## Una advertencia sobre las cifras y las fuentes

- **Las cifras de hardware envejecen rápido.** Toda cifra va con su año y su dispositivo. Una de 2019 (Sycamore, iones, la revisión de superconductores) no describe el hardware de hoy; cuando una fuente más reciente existe, se muestra la progresión.
- **Muchas fuentes son de fabricantes o de grupos que defienden su plataforma:** Quantinuum [@moses-2023], Pasqal [@henriet-2020], Infleqtion (autor de [@saffman-2025]), QuEra (varios autores de [@bluvstein-2024]), PsiQuantum, con simulaciones y no experimentos [@bartolucci-2023], Microsoft [@aghaee-2025] y Google [@arute-2019; @google-2025]. Se atribuyen en el texto. Las revisiones del MIT Lincoln Laboratory ([@krantz-2019], [@kjaergaard-2020], [@bruzewicz-2019]) y la compilación de datos de espines [@stano-2022] son lo más cercano a independiente; Burkard y colaboradores incluyen autores de HRL Laboratories [@burkard-2023].
- **Los qubits topológicos son un caso aparte.** El artículo de Microsoft [@aghaee-2025] reclama una medida de paridad y "progreso hacia" un qubit topológico, y dice que sus datos por sí solos no determinan si los estados son topológicos; el comentario de Legg [@legg-2025] es la crítica de una persona, en un preprint no revisado por pares. No se afirma que exista un qubit topológico ni que esté refutado.
- **Ventaja y simulación clásica.** La cifra de 10 000 años de [@arute-2019] es una extrapolación de los autores; [@pan-2022] muestrea los mismos circuitos clásicamente; [@zhong-2020] es muestreo de bosones, de propósito especial; [@eisert-2025] es un preprint de perspectiva de 2025-26. La lección es la carrera entre reclamaciones cuánticas y simulación clásica, no un veredicto.
- **Una nota sobre el preprint de Google.** El texto de [@google-2025] es la versión v1 de arXiv (agosto de 2024) y no nombra el procesador; Eisert y Preskill lo llaman Willow [@eisert-2025, Sec. III, p. 4].
- **Poselección no es corrección.** Los titulares de GHZ y XEB lógicos de [@bluvstein-2024] dependen de detección de errores con descarte de datos [@bluvstein-2024, pp. 4, 6-7].

## Hacia dónde sigue

Este ámbito trata a los errores como un dato del dispositivo. [Corrección de errores y tolerancia a fallos](../error-correction/index.md) explica cómo se pueden vencer: el [ruido cuántico y los canales de error](../error-correction/concepts/quantum-noise-channels.md), el [teorema del umbral](../error-correction/concepts/threshold-theorem.md), el [código de superficie](../error-correction/concepts/surface-code.md), las [puertas tolerantes a fallos](../error-correction/concepts/fault-tolerant-gates.md), los [experimentos con qubits lógicos](../error-correction/concepts/logical-qubit-experiments.md) y la [estimación de recursos](../error-correction/concepts/resource-estimation.md).
