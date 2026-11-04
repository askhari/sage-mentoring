---
concept: primitives-sampler-estimator
title: "Primitivas: Sampler y Estimator"
format: 2
---

## Comprensión {#layer-2}

### Idea clave
Casi todo lo que se le pide a un ordenador cuántico es una de dos cosas: muestrear cadenas de bits o estimar el valor esperado de un [observable](../../quantum-mechanics/concepts/observables.md). Qiskit las encapsula en dos *primitivas (primitives)*, `Sampler` y `Estimator`, con una interfaz común [@qiskit-docs, /guides/primitives; @javadi-abhari-2024, §II.6, p. 4].

### Explicación
Las primitivas son la manera de evaluar circuitos en Qiskit y definen una interfaz común aunque las implementaciones difieran mucho [@javadi-abhari-2024, §II.6, p. 4]. El *Sampler* devuelve resultados de medida (bitstrings) del registro de salida; el *Estimator* devuelve valores esperados ya postprocesados [@javadi-abhari-2024, §III.C, p. 7].

¿Por qué una abstracción y no `backend.run`? La interfaz de una primitiva toma un circuito (posiblemente parametrizado) y uno o varios observables y devuelve estimaciones. Así, un estimador distinto, por ejemplo uno con mitigación de errores incluida, se puede ofrecer como primitiva, es decir, como un ejecutor efectivo de ordenadores cuánticos [@javadi-abhari-2024, §II.6, p. 4]. El código del usuario no cambia al pasar del simulador al hardware: cambia la implementación.

Las de referencia son `StatevectorSampler` y `StatevectorEstimator`; hay envoltorios para cualquier backend (`BackendSamplerV2`, `BackendEstimatorV2`), implementaciones de Aer y las de IBM Runtime. La interfaz `run()` es común, pero las opciones difieren [@qiskit-docs, /guides/primitives]. Aquí usamos las de referencia para aprender y las de Runtime para [hardware](running-on-hardware.md).

El Estimator trabaja con observables escritos como suma de productos de Pauli con coeficientes reales, `H = Σ cᵢ Pᵢ`. Por linealidad, `⟨H⟩` es la suma ponderada de los valores esperados de cada término [@peruzzo-2014, Eqs. 1-2, p. 1]. Cada producto de Pauli se mide como un cálculo cuántico independiente y el procesador clásico suma los resultados con sus pesos [@peruzzo-2014, Fig. 1, p. 2]. En Qiskit, los observables son `Pauli`, `SparsePauliOp`, `PauliList` o cadenas, organizados en una matriz [@qiskit-docs, /guides/primitive-input-output]. Para que el Estimator sea eficiente, el número de términos de Pauli no nulos debe crecer a lo sumo polinomialmente con los qubits [@ibm-quantum-learning, "Cost functions"]; para un hamiltoniano químico con `n` orbitales hay del orden de `n⁴` cadenas de Pauli distintas [@cerezo-2021, §IV.B, p. 17].

La unidad de trabajo es el PUB. Una primitiva recibe una lista de *PUBs (primitive unified blocks)*, una tupla por circuito:

- Estimator: `(circuito, observables, valores de parámetros, precisión opcional)`.
- Sampler: `(circuito con medidas, valores de parámetros, shots opcionales)` [@qiskit-docs, /guides/primitive-input-output].

Los datos de un PUB se combinan con las reglas de difusión (*broadcasting*) de NumPy; un único `SparsePauliOp` cuenta como un elemento, y el Estimator devuelve un valor por cada elemento de la forma resultante. El resultado es un `PrimitiveResult` con un `PubResult` por PUB; en el Estimator, `data` contiene `evs` y `stds`, y el Sampler devuelve un `BitArray` por registro clásico (`meas` por defecto) con `get_counts()`, además de `slice_bits`, `slice_shots`, `expectation_values` y máscaras para postselección [@qiskit-docs, /guides/primitive-input-output].

Por último, la versión de la interfaz. Las V2 devuelven bitstrings indexados por el nombre del registro clásico, no cuasi-probabilidades, y el Estimator V2 añade un argumento `precision`. En Qiskit 1.0, `Sampler`/`Estimator` pasaron a ser `StatevectorSampler`/`StatevectorEstimator` [@qiskit-docs, /guides/primitives; /guides/qiskit-1.0-features]. Las lecciones de IBM Quantum Learning usan las V2 [@ibm-quantum-learning, "Instances and extensions"].

### Ejemplo
Primero, un Estimator sobre un par de Bell. Los circuitos del Estimator **no** llevan medidas [@qiskit-docs, /guides/construct-circuits]. Para el estado de Bell `(|00⟩+|11⟩)/√2` se esperan `⟨ZZ⟩ = 1`, `⟨XX⟩ = 1` y `⟨ZI⟩ = 0`:

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

`ZZ` y `XX` valen 1 a la vez: es la firma de un [estado entrelazado](../../qubits-and-circuits/concepts/entanglement.md) de Bell, que está correlado en dos bases distintas, mientras que `ZI` vale 0 porque cada qubit por separado está en un estado completamente aleatorio.

Segundo, un barrido de parámetros por difusión. Un solo PUB lleva aquí 5 ángulos para `Ry(θ)`; el valor esperado de `Z` es `cos θ`:

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

Con la precisión `0.05` el Estimator añade ruido de muestreo, por eso `1.02` supera el máximo posible `1`: el valor esperado exacto está acotado, la estimación no.

### Errores frecuentes
- *"El Estimator me da bitstrings."* No: da valores esperados. Para bitstrings, usa el Sampler [@qiskit-docs, /guides/primitives].
- *"Pongo `measure_all()` en el circuito del Estimator."* Los circuitos del Estimator no deben contener medidas [@qiskit-docs, /guides/construct-circuits].
- *"Una estimación a partir de muestras es exacta."* Estimar un valor esperado desde conteos del Sampler arrastra ruido de muestreo: en el ejemplo de `2X − Z` en `|+⟩` (valor exacto 2) salió 1,9958 con el Sampler y 2,0000 con el Estimator [@ibm-quantum-learning, "Cost functions"].
- *"`precision` y `shots` son lo mismo."* El Estimator trabaja con una precisión por PUB, el Sampler con shots por PUB o en `run()` [@qiskit-docs, /guides/qiskit-1.0-features].

### Para seguir
[Transpilación](transpilation.md) explica cómo adaptar el circuito de un PUB al dispositivo antes de ejecutarlo. La capa profesional de este concepto trata de cómo diseñar los PUBs y repartir los shots.

## Profesional {#layer-3}

### Idea clave
Diseñar bien los PUBs es ahorrar medidas: agrupa observables que comutan, reparte los shots según el peso de cada término y elige Sampler o Estimator según la salida que necesites y las técnicas de mitigación que vayas a usar [@cerezo-2021, §IV.B, pp. 17-18; @cai-2023, Sec. II.A, p. 3].

### Explicación
Los observables que comutan y van en PUBs distintos se miden por separado, así que agrúpalos en un mismo PUB para compartir medidas [@qiskit-docs, /guides/primitive-input-output]. Agrupar términos de Pauli que comutan reduce el número de medidas; el reparto en grupos es un problema de coloreado de grafos o de recubrimiento por cliques [@cerezo-2021, §IV.B.1, p. 17]. El agrupamiento *qubit-wise commuting* (QWC) es el más simple, pero no cambia la escala asintótica en química; con comutación general (con cuadráticamente más puertas) las medidas pasan a `n³`, y factorizando los tensores de dos electrones se llega a escala cuadrática o lineal [@cerezo-2021, §IV.B.1, p. 17].

El coste en shots es el siguiente factor. Estimar una energía con precisión `ε` cuesta `O(1/ε²)` medidas, a diferencia de las `O(log(1/ε))` de la [estimación de fase](../../quantum-algorithms/concepts/phase-estimation.md); a cambio, la estimación variacional exige coherencia `O(1)` por medida tras preparar el estado [@cerezo-2021, §III.A.7, p. 9; @peruzzo-2014, p. 2]. La asignación de shots por término no debe ser uniforme: lo óptimo es proporcional a `|cᵢ|` por la desviación típica del término, y un muestreo aleatorio con esas probabilidades da estimaciones sin sesgo incluso con un solo shot [@cerezo-2021, §IV.B.2, p. 18]. Las *sombras clásicas (classical shadows)* hacen que cada shot contribuya a todos los observables de Pauli, con un número de medidas logarítmico en el número de términos [@cerezo-2021, §IV.B.3, p. 18]. Esas técnicas no están en las primitivas de Qiskit por defecto [unverified]: se implementan fuera o se eligen al usar un servicio específico.

La elección entre las dos primitivas depende de la salida. El Sampler es el adecuado cuando la salida es la cadena de bits; es eficiente solo para distribuciones dispersas, y los shots crecen rápido si la distribución es densa [@ibm-quantum-learning, "Cost functions"]. El Estimator, cuando lo que importa es una magnitud física o un coste; además, las técnicas de mitigación se aplican a valores esperados, y la mitigación de errores no sirve para salidas de un solo disparo como la estimación de fase o Shor [@cai-2023, Sec. II.A, p. 3].

También hay que elegir implementación. Las de referencia son exactas y rápidas pero idealizadas; las de Aer simulan ruido pero no aceptan todas las opciones de IBM (por ejemplo el nivel de resiliencia); las de Runtime añaden supresión y mitigación y cuestan tiempo de dispositivo [@qiskit-docs, /guides/primitives; /guides/simulate-with-qiskit-aer]. Conviene aislar la elección en una función de fábrica para poder sustituirla en tests.

En el runtime hay además una novedad de nombres. A partir de `qiskit-ibm-runtime` 0.50.0 existen primitivas *del lado del cliente* (`qiskit_ibm_runtime.executor_sampler.Sampler` y `executor_estimator.Estimator`), que ejecutan localmente la supresión y la mitigación; antes, `Sampler`/`Estimator` se ejecutaban en el servidor [@qiskit-docs, /guides/local-testing-mode; /guides/hello-world]. En nuestras pruebas con `qiskit-ibm-runtime` 0.51.0, importar `SamplerV2`/`EstimatorV2` desde `qiskit_ibm_runtime` emite un `DeprecationWarning` (obsoletas desde 0.50.0) que apunta a las nuevas clases. Si lees un tutorial con `EstimatorV2(mode=backend)`, ese es el nombre antiguo. En [ejecutar en hardware real](running-on-hardware.md) se usan las nuevas.

Por último, el postprocesado. El Sampler devuelve conteos que luego se combinan (visualización, mitigación de lectura, marginalización, postselección) en el último paso del patrón [@qiskit-docs, /guides/intro-to-patterns]. Cuidado: tras transpilar, el observable debe seguir el layout con `observable.apply_layout(isa_circuit.layout)` [@qiskit-docs, /guides/hello-world]; lo ves en [transpilación](transpilation.md).

### Ejemplo
Elegir primitiva para tres tareas con lo que dicen las fuentes:

1. **QAOA para obtener un corte:** la respuesta es una cadena de bits, así que se lee con el Sampler [@ibm-quantum-learning, "Cost functions"].
2. **VQE o simulación de dinámica:** lo que importa es un coste o una magnitud física, así que se usa el Estimator, que además admite mitigación [@cai-2023, Sec. II.A, p. 3].
3. **Estimación de fase o Shor:** la salida es de un solo disparo, de modo que la mitigación de errores no sirve y el Sampler es el camino natural [@cai-2023, Sec. II.A, p. 3].

### Para seguir
[Algoritmos variacionales](variational-algorithms.md) usa el Estimator dentro de un bucle de optimización. [Ejecutar en hardware real](running-on-hardware.md) lleva estas primitivas a un dispositivo de IBM.
