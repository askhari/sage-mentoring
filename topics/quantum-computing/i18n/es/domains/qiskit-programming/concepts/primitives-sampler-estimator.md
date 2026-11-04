---
concept: primitives-sampler-estimator
title: "Primitivas: Sampler y Estimator"
---

## Comprensión {#layer-2}

**Dos preguntas, dos primitivas.** Casi todo lo que se le pide a un ordenador cuántico es una de dos cosas: muestrear cadenas de bits o estimar el valor esperado de un [observable](../../quantum-mechanics/concepts/observables.md) sobre el estado que prepara un circuito. Qiskit las encapsula en dos *primitivas (primitives)*: `Sampler` y `Estimator` [@qiskit-docs, /guides/primitives; @javadi-abhari-2024, §II.6, p. 4]. Son la manera de evaluar circuitos en Qiskit y definen una interfaz común aunque las implementaciones difieran mucho [@javadi-abhari-2024, §II.6, p. 4].

- El *Sampler* devuelve resultados de medida (bitstrings) del registro de salida.
- El *Estimator* devuelve valores esperados ya postprocesados [@javadi-abhari-2024, §III.C, p. 7].

**Por qué una abstracción y no `backend.run`.** La interfaz de una primitiva toma un circuito (posiblemente parametrizado) y uno o varios observables y devuelve estimaciones; así un estimador distinto, por ejemplo uno con mitigación de errores incluida, se puede ofrecer como primitiva, es decir, como un ejecutor efectivo de ordenadores cuánticos [@javadi-abhari-2024, §II.6, p. 4]. El código del usuario no cambia al pasar del simulador al hardware: cambia la implementación.

**Implementaciones.** Las de referencia son `StatevectorSampler` y `StatevectorEstimator`; hay envoltorios para cualquier backend (`BackendSamplerV2`, `BackendEstimatorV2`), implementaciones de Aer y las de IBM Runtime. La interfaz `run()` es común, pero las opciones difieren [@qiskit-docs, /guides/primitives]. Aquí usamos las de referencia para aprender y las de Runtime para [hardware](running-on-hardware.md).

**El Estimator y los observables de Pauli.** Un observable se escribe como suma de productos de Pauli con coeficientes reales, `H = Σ cᵢ Pᵢ`; por linealidad, `⟨H⟩` es la suma ponderada de los valores esperados de cada término [@peruzzo-2014, Eqs. 1-2, p. 1]. Cada producto de Pauli se mide como un cálculo cuántico independiente y el procesador clásico suma los resultados con sus pesos [@peruzzo-2014, Fig. 1, p. 2]. En Qiskit, los observables son `Pauli`, `SparsePauliOp`, `PauliList` o cadenas, organizados en una matriz [@qiskit-docs, /guides/primitive-input-output]. Para que el Estimator sea eficiente, el número de términos de Pauli no nulos debe crecer a lo sumo polinomialmente con los qubits [@ibm-quantum-learning, "Cost functions"]; para un hamiltoniano químico con `n` orbitales hay del orden de `n⁴` cadenas de Pauli distintas [@cerezo-2021, §IV.B, p. 17].

**La unidad de trabajo: el PUB.** Una primitiva recibe una lista de *PUBs (primitive unified blocks)*, una tupla por circuito:

- Estimator: `(circuito, observables, valores de parámetros, precisión opcional)`.
- Sampler: `(circuito con medidas, valores de parámetros, shots opcionales)` [@qiskit-docs, /guides/primitive-input-output].

Los datos se combinan con las reglas de difusión (*broadcasting*) de NumPy; un único `SparsePauliOp` cuenta como un elemento, y el Estimator devuelve un valor por cada elemento de la forma resultante [@qiskit-docs, /guides/primitive-input-output].

**Ejemplo: Estimator sobre un par de Bell.** Los circuitos del Estimator **no** llevan medidas [@qiskit-docs, /guides/construct-circuits]. Para el estado de Bell `(|00⟩+|11⟩)/√2` se esperan `⟨ZZ⟩ = 1`, `⟨XX⟩ = 1` y `⟨ZI⟩ = 0`:

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp

bell = QuantumCircuit(2)             # SIN medidas
bell.h(0); bell.cx(0, 1)

obs = [SparsePauliOp("ZZ"), SparsePauliOp("XX"), SparsePauliOp("ZI")]
res = StatevectorEstimator().run([(bell, obs)]).result()[0]
print(res.data.evs)                  # un valor por observable
print(res.data.stds)                 # ceros: exacto por defecto
print(res.data.evs.shape)
```

```text
[1. 1. 0.]
[0. 0. 0.]
(3,)
```

`ZZ` y `XX` valen 1 a la vez: es la firma de un [estado entrelazado](../../qubits-and-circuits/concepts/entanglement.md) de Bell, que está correlado en dos bases distintas, mientras que `ZI` vale 0 porque cada qubit por separado está en un estado completamente aleatorio. El resultado es un `PrimitiveResult` con un `PubResult` por PUB; en el Estimator, `data` contiene `evs` y `stds` [@qiskit-docs, /guides/primitive-input-output].

**Barridos de parámetros por difusión.** Un solo PUB puede llevar muchos conjuntos de parámetros: aquí 5 ángulos para `Ry(θ)`; el valor esperado de `Z` es `cos θ`:

```python
import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.primitives import StatevectorEstimator, StatevectorSampler
from qiskit.quantum_info import SparsePauliOp

theta = Parameter("theta")
qc = QuantumCircuit(1)
qc.ry(theta, 0)
angles = np.linspace(0, np.pi, 5).reshape(5, 1)       # 5 conjuntos de 1 parámetro

est = StatevectorEstimator(seed=1)
res = est.run([(qc, SparsePauliOp("Z"), angles)], precision=0.05).result()[0]
print(np.round(res.data.evs, 2))                       # estimaciones ruidosas
print(np.round(np.cos(angles.ravel()), 2))             # valor exacto

meas = qc.copy(); meas.measure_all()
sres = StatevectorSampler(seed=1).run([(meas, angles)], shots=500).result()[0]
print(sres.data.meas.shape, sres.data.meas.get_counts(0))
```

```text
[ 1.02  0.75  0.02 -0.77 -0.95]
[ 1.    0.71  0.   -0.71 -1.  ]
(5,) {'0': 500}
```

(Con la precisión `0.05` el Estimator añade ruido de muestreo, por eso `1.02` supera el máximo posible `1`: el valor esperado exacto está acotado, la estimación no.) El Sampler devuelve un `BitArray` por registro clásico (`meas` por defecto) con `get_counts()`; también ofrece `slice_bits`, `slice_shots`, `expectation_values` y máscaras para postselección [@qiskit-docs, /guides/primitive-input-output].

**Cambios de V1 a V2.** Las V2 devuelven bitstrings indexados por el nombre del registro clásico, no cuasi-probabilidades, y el Estimator V2 añade un argumento `precision`. En Qiskit 1.0, `Sampler`/`Estimator` pasaron a ser `StatevectorSampler`/`StatevectorEstimator` [@qiskit-docs, /guides/primitives; /guides/qiskit-1.0-features]. Las lecciones de IBM Quantum Learning usan las V2 [@ibm-quantum-learning, "Instances and extensions"].

**Errores frecuentes.**

- *"El Estimator me da bitstrings."* No: da valores esperados. Para bitstrings, usa el Sampler [@qiskit-docs, /guides/primitives].
- *"Pongo `measure_all()` en el circuito del Estimator."* Los circuitos del Estimator no deben contener medidas [@qiskit-docs, /guides/construct-circuits].
- *"Una estimación a partir de muestras es exacta."* Estimar un valor esperado desde conteos del Sampler arrastra ruido de muestreo: en el ejemplo de `2X − Z` en `|+⟩` (valor exacto 2) salió 1,9958 con el Sampler y 2,0000 con el Estimator [@ibm-quantum-learning, "Cost functions"].
- *"`precision` y `shots` son lo mismo."* El Estimator trabaja con una precisión por PUB, el Sampler con shots por PUB o en `run()` [@qiskit-docs, /guides/qiskit-1.0-features].

## Profesional {#layer-3}

**Diseñar los PUBs.** Los observables que comutan y van en PUBs distintos se miden por separado; agrúpalos en un mismo PUB para compartir medidas [@qiskit-docs, /guides/primitive-input-output]. Agrupar términos de Pauli que comutan reduce el número de medidas; el reparto en grupos es un problema de coloreado de grafos o de recubrimiento por cliques [@cerezo-2021, §IV.B.1, p. 17]. El agrupamiento *qubit-wise commuting* (QWC) es el más simple, pero no cambia la escala asintótica en química; con comutación general (con cuadráticamente más puertas) las medidas pasan a `n³`, y factorizando los tensores de dos electrones se llega a escala cuadrática o lineal [@cerezo-2021, §IV.B.1, p. 17].

**Coste en shots.** Estimar una energía con precisión `ε` cuesta `O(1/ε²)` medidas, a diferencia de `O(log(1/ε))` de la [estimación de fase](../../quantum-algorithms/concepts/phase-estimation.md) [@cerezo-2021, §III.A.7, p. 9]; a cambio, la estimación variacional exige coherencia `O(1)` por medida tras preparar el estado [@peruzzo-2014, p. 2]. La asignación de shots por término no debe ser uniforme: lo óptimo es proporcional a `|cᵢ|` por la desviación típica del término, y un muestreo aleatorio con esas probabilidades da estimaciones sin sesgo incluso con un solo shot [@cerezo-2021, §IV.B.2, p. 18]. Las *sombras clásicas (classical shadows)* hacen que cada shot contribuya a todos los observables de Pauli, con un número de medidas logarítmico en el número de términos [@cerezo-2021, §IV.B.3, p. 18]. Esas técnicas no están en las primitivas de Qiskit por defecto [unverified]: se implementan fuera o se eligen al usar un servicio específico.

**Cuándo Sampler, cuándo Estimator.**

- *Sampler:* cuando la salida es la cadena de bits (QAOA para obtener un corte, Grover, Shor). Es eficiente solo para distribuciones dispersas; los shots crecen rápido si la distribución es densa [@ibm-quantum-learning, "Cost functions"].
- *Estimator:* cuando lo que importa es una magnitud física o un coste (VQE, simulación de dinámica). Además, las técnicas de mitigación se aplican a valores esperados: la mitigación de errores no sirve para salidas de un solo disparo como la estimación de fase o Shor [@cai-2023, Sec. II.A, p. 3].

**Primitivas del lado del cliente en el runtime.** A partir de `qiskit-ibm-runtime` 0.50.0 existen primitivas *del lado del cliente* (`qiskit_ibm_runtime.executor_sampler.Sampler` y `executor_estimator.Estimator`), que ejecutan localmente la supresión y la mitigación; antes, `Sampler`/`Estimator` se ejecutaban en el servidor [@qiskit-docs, /guides/local-testing-mode; /guides/hello-world]. En nuestras pruebas con `qiskit-ibm-runtime` 0.51.0, importar `SamplerV2`/`EstimatorV2` desde `qiskit_ibm_runtime` emite un `DeprecationWarning` (obsoletas desde 0.50.0) que apunta a las nuevas clases. Si lees un tutorial con `EstimatorV2(mode=backend)`, ese es el nombre antiguo. En [ejecutar en hardware real](running-on-hardware.md) se usan las nuevas.

**Qué eliges al elegir una implementación.** Las de referencia son exactas y rápidas pero idealizadas; las de Aer simulan ruido pero no aceptan todas las opciones de IBM (por ejemplo el nivel de resiliencia); las de Runtime añaden supresión y mitigación y cuestan tiempo de dispositivo [@qiskit-docs, /guides/primitives; /guides/simulate-with-qiskit-aer]. Aísla la elección en una función de fábrica para poder sustituirla en tests.

**Postprocesado.** El Sampler devuelve conteos que luego se combinan (visualización, mitigación de lectura, marginalización, postselección) en el último paso del patrón [@qiskit-docs, /guides/intro-to-patterns]. Cuidado: tras transpilar, el observable debe seguir el layout: `observable.apply_layout(isa_circuit.layout)` [@qiskit-docs, /guides/hello-world]; lo ves en [transpilación](transpilation.md).
