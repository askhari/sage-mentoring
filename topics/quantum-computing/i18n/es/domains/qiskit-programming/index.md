---
domain: qiskit-programming
title: "Programación con Qiskit"
---

# Programación con Qiskit

Este ámbito lleva a código lo que ya sabes de [qubits, puertas y circuitos](../qubits-and-circuits/index.md) y de [algoritmos cuánticos](../quantum-algorithms/index.md). **Qiskit** es el SDK de código abierto de IBM Quantum para escribir, transformar y ejecutar circuitos; nació en 2017 y su versión 1.0 es la que describe el artículo de arquitectura del propio equipo [@javadi-abhari-2024, p. 1]. Está pensado para quien ya programa: se explica la forma de pensar (circuito, transpilación, primitiva, trabajo en un dispositivo) y los costes reales de cada decisión, no solo la sintaxis.

## Versiones del código

Todo el código de este ámbito usa **solo la API actual** y está **probado con `qiskit 2.6.1`, `qiskit-aer 0.18.2` y `qiskit-ibm-runtime 0.51.0`** (más `scipy 1.18.1` para los optimizadores), en Python 3.13. Las documentaciones de IBM fijan versiones distintas página a página (2.3, 2.5.2, 2.6.1 para Qiskit; 0.43 a 0.47 para el runtime), de modo que conviene mirar la versión indicada en cada página [@qiskit-docs, versiones, release notes]. En la fecha de redacción, 2026-11-04, las últimas versiones publicadas eran Qiskit SDK 2.6 y `qiskit-ibm-runtime` 0.51.0 [@qiskit-docs, /api/qiskit/release-notes; /api/qiskit-ibm-runtime/release-notes].

Los bloques que necesitan una cuenta de IBM (`QiskitRuntimeService`, dispositivos reales) **no se han podido ejecutar**: se marcan en un comentario y se limitan a lo que describe la documentación. Los demás se ejecutaron tal cual, usando el simulador local y los *dispositivos falsos (fake backends)* de `qiskit_ibm_runtime.fake_provider`, que funcionan sin cuenta [@qiskit-docs, /guides/local-testing-mode]. Las salidas que se muestran son reales; las que dependen del azar (conteos, estimaciones con shots) cambian de una ejecución a otra.

**Qué ya no existe.** Si sigues un tutorial antiguo, desconfía de lo siguiente. En Qiskit 1.0 desaparecieron `qiskit.execute` (se usa `transpile()` y `backend.run()`, o una primitiva), `BasicAer` (ahora `qiskit.providers.basic_provider`), `bind_parameters()` (ahora `assign_parameters()`), los módulos `algorithms` y `opflow`, y las primitivas V1 se sustituyeron por las V2; `Aer` pasó a ser el paquete separado `qiskit_aer` [@qiskit-docs, /guides/qiskit-1.0-features; /guides/metapackage-migration]. En 2.0 se eliminaron `c_if` (sustituido por `if_test`), la duración por instrucción y todo el módulo `qiskit.pulse`, y el transpilador dejó de aceptar `backend_properties`, `inst_map` o `basis_gates` sueltos [@qiskit-docs, /guides/qiskit-2.0]. Además, desde 1.0 `pip install qiskit` no instala Aer [@qiskit-docs, /guides/metapackage-migration].

## Por qué importa

Un algoritmo en la pizarra y un resultado en un dispositivo real están separados por varias capas: el circuito abstracto hay que reescribirlo con las puertas nativas y la conectividad del chip, ejecutarlo con un contrato claro (muestras o valores esperados) y tratar el ruido de lo que sale. Qiskit estructura ese camino en cuatro pasos, los *patrones de Qiskit (Qiskit patterns)*: mapear el problema a circuitos y operadores, optimizar (transpilar) para el dispositivo, ejecutar con las primitivas y postprocesar [@qiskit-docs, /guides/intro-to-patterns; @javadi-abhari-2024, §II.7, p. 4]. Los conceptos de este ámbito siguen justamente ese camino.

## Cómo se conectan los conceptos

1. [Construir circuitos en Qiskit](concepts/qiskit-circuits.md): el objeto central; todo lo demás gira a su alrededor [@javadi-abhari-2024, Fig. 2, p. 5].
2. [Simuladores y vectores de estado](concepts/simulators-and-statevectors.md): probar sin hardware, y entender hasta dónde llega la simulación clásica.
3. [Primitivas: Sampler y Estimator](concepts/primitives-sampler-estimator.md): las dos formas de pedir un resultado, muestras o valores esperados.
4. [Transpilación](concepts/transpilation.md): adaptar el circuito al dispositivo.
5. [Ejecutar en hardware real (IBM Quantum)](concepts/running-on-hardware.md): cuentas, dispositivos, modos de ejecución.
6. [Mitigación de errores](concepts/error-mitigation.md): qué hacer con el ruido sin corregirlo del todo.
7. [Algoritmos variacionales (VQE, QAOA)](concepts/variational-algorithms.md): el uso típico de todo lo anterior en un bucle híbrido clásico-cuántico.
8. [La era NISQ](concepts/nisq-era.md): el marco que explica por qué todo esto es como es.

## Orden de estudio recomendado

- **Camino práctico (primer contacto):** circuitos, simuladores, y después [La era NISQ](concepts/nisq-era.md), que tiene capa 1 y da el motivo de todo lo demás. Con eso puedes escribir, simular y entender por qué los resultados de un dispositivo real salen "sucios".
- **Camino profesional:** circuitos, simuladores, primitivas, transpilación, ejecución en hardware, algoritmos variacionales y, al final, mitigación de errores (solo tiene capa profesional, y usa todo lo anterior). Los algoritmos variacionales solo exigen las primitivas, así que pueden estudiarse justo después de ellas y antes de pasar al hardware.
- Los conceptos de [observables](../quantum-mechanics/concepts/observables.md), [decoherencia](../quantum-mechanics/concepts/decoherence.md), [conjuntos universales de puertas](../qubits-and-circuits/concepts/universal-gate-sets.md) y [estimación de fase](../quantum-algorithms/concepts/phase-estimation.md) se usan como base; no se repiten aquí.

## Una advertencia sobre las fuentes

- El artículo de arquitectura de Qiskit [@javadi-abhari-2024] está escrito por el propio equipo de IBM y describe Qiskit 1.0: se usa para el diseño, no para el detalle de la API actual.
- Las cifras de hardware de [@preskill-2018] son de 2018 y se presentan como tales.
- Las afirmaciones de [@cerezo-2021] sobre que los algoritmos variacionales son la mejor esperanza de ventaja a corto plazo son opinión de los autores y se atribuyen.
- Las lecciones de IBM Quantum Learning se obtuvieron mediante un resumen automático: sus cifras exactas se usan solo con cautela [@ibm-quantum-learning, nota de acceso].

## Hacia dónde sigue

[Cómo se construyen los ordenadores cuánticos](../quantum-hardware/index.md) explica qué hay detrás de un dispositivo como los que se usan aquí, y [corrección de errores](../error-correction/index.md) explica la alternativa de fondo al ruido que este ámbito solo mitiga.
