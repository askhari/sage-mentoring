---
concept: simulators-and-statevectors
title: "Simuladores y vectores de estado"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
Un *simulador (simulator)* es un programa clásico que calcula lo que haría un ordenador cuántico; el más sencillo guarda el *vector de estado (statevector)*, la lista completa de las `2ⁿ` amplitudes de `n` qubits. Sirve para escribir y comprobar circuitos sin cuenta, sin cola y sin ruido [@watrous-2025, L2.2, PDF p. 55].

### Explicación
El vector de estado es el que se describe en [estados de varios qubits](../../qubits-and-circuits/concepts/multi-qubit-states.md) [@watrous-2025, L2.2, PDF p. 55]. En Qiskit, `Statevector` (del módulo `qiskit.quantum_info`) calcula el estado ideal de un circuito, útil para comprobar un resultado sin el ruido del hardware [@qiskit-docs, /api/qiskit/qiskit.quantum_info.Statevector; @ibm-quantum-learning, "Bits, gates, and circuits"]. `probabilities` da las probabilidades de la base de cómputo, `sample_counts(shots)` muestrea sin modificar el estado y `expectation_value(oper)` es exacto [@qiskit-docs, /api/qiskit/qiskit.quantum_info.Statevector].

Esto marca la diferencia entre simulador y hardware. Con el vector de estado ves las amplitudes completas; un dispositivo real solo entrega, en cada shot, una cadena de bits al azar según la [regla de Born](../../quantum-mechanics/concepts/born-rule-measurement.md), y el estado no se puede leer directamente. Por eso el simulador es una herramienta de depuración, no un modelo de lo que obtendrás.

Su límite es el tamaño. El vector de estado crece de forma exponencial: añadir un qubit duplica el número de amplitudes [@de-wolf-2026, §1.3, p. 20]. La documentación de IBM indica que la simulación con ruido cuesta exponencialmente más al aumentar los qubits y que la mayoría de portátiles no pasan mucho de unos 32 qubits [@qiskit-docs, /guides/local-testing-mode]. Preskill señalaba que unos 50 qubits superan lo que los mayores supercomputadores pueden simular por fuerza bruta, un umbral difuso porque el coste también depende de la profundidad del circuito [@preskill-2018, §4.1, p. 5 y nota 2].

Para evaluar circuitos con el mismo formato que en hardware, Qiskit trae primitivas de referencia que simulan el estado de forma ideal en local: `StatevectorSampler` y `StatevectorEstimator` (en `qiskit.primitives`). No modelan el ruido de un dispositivo, así que sirven para prototipos [@qiskit-docs, /guides/simulate-with-qiskit-sdk-primitives; /guides/primitives]. Se estudian en el siguiente nivel del ámbito.

### Ejemplo
El estado de un par de Bell, sin medir, y 1000 shots simulados:

```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

bell = QuantumCircuit(2)
bell.h(0)
bell.cx(0, 1)

sv = Statevector(bell)               # estado ideal, sin medir
print(sv.data)                       # las 2**2 = 4 amplitudes
print(sv.probabilities())            # probabilidades en la base de cómputo
counts = sv.sample_counts(1000)      # 1000 shots simulados (varían entre ejecuciones)
print({str(k): int(v) for k, v in counts.items()})
```

```text
[0.70710678+0.j 0.        +0.j 0.        +0.j 0.70710678+0.j]
[0.5 0.  0.  0.5]
{'00': 504, '11': 496}
```

Las amplitudes son `1/√2` en `00` y en `11`, de modo que las probabilidades son 0,5 y 0,5 y solo aparecen esas dos cadenas. Lo mismo con una primitiva de referencia, que necesita un circuito con medidas:

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

bell = QuantumCircuit(2)
bell.h(0); bell.cx(0, 1)
bell.measure_all()                   # un Sampler necesita medidas

job = StatevectorSampler().run([bell], shots=1000)
print(job.result()[0].data.meas.get_counts())
```

```text
{'11': 503, '00': 497}
```

En una ejecución real los conteos varían; solo `00` y `11` aparecen, como cabe esperar de un par de Bell.

### Errores frecuentes
- *"El simulador me dice lo que saldrá en el dispositivo."* El simulador de estado es ideal: muestra amplitudes que el hardware no entrega y no incluye ruido [@qiskit-docs, /guides/local-testing-mode].
- *"Con un portátil puedo simular cualquier circuito."* El vector de estado duplica su tamaño con cada qubit [@de-wolf-2026, §1.3, p. 20].

### Para seguir
[La era NISQ](nisq-era.md) explica por qué el dispositivo real no se comporta como este simulador ideal. La capa de comprensión de este concepto añade simulación con ruido y otros métodos.

## Comprensión {#layer-2}

### Idea clave
Una simulación puede ser exacta o por muestreo, e ideal o con ruido. `Statevector` es la herramienta ideal, y Qiskit Aer añade modelos de ruido y métodos alternativos, con un coste que crece con el número de puertas ruidosas [@qiskit-docs, /guides/simulate-with-qiskit-sdk-primitives; /guides/simulate-with-qiskit-aer].

### Explicación
Las primitivas de referencia son exactas por defecto. `StatevectorEstimator` se basa en `quantum_info.Statevector`, y pasarle un `precision` añade un error de tipo ruido de disparo (*shot noise*); `StatevectorSampler` también es exacto por defecto y un argumento `shots` introduce el muestreo [@qiskit-docs, /guides/simulate-with-qiskit-sdk-primitives]. La diferencia importa: un ejemplo de IBM Quantum Learning (resumido) calcula el valor esperado de `H = 2X − Z` en `|+⟩`, cuyo valor exacto es 2, y obtiene 1,9958 con un Sampler y 2,0000 con un Estimator [@ibm-quantum-learning, "Cost functions"].

El módulo `quantum_info` conecta los circuitos con el formalismo matemático: estados (`Statevector`, matriz densidad, estados estabilizadores), operadores (`Operator`, `Clifford`, `Pauli`), canales (Choi, PTM, SuperOp) y medidas de distancia [@javadi-abhari-2024, Fig. 2, p. 5]. Los operadores sirven también como observables, por ejemplo `SparsePauliOp.from_sparse_list`, o `apply_layout` para llevarlos al circuito transpilado [@javadi-abhari-2024, §IV.B, p. 9; §IV.D, p. 11]. Con `Statevector` se pueden construir estados (`from_instruction`, `from_label`), aplicar operadores (`evolve`) y dibujarlos (`draw` admite texto, LaTeX, qsphere, Hinton, Bloch y otros) [@qiskit-docs, /api/qiskit/qiskit.quantum_info.Statevector].

Para añadir ruido hace falta Qiskit Aer. En 1.0, los simuladores `UnitarySimulatorPy` y `StatevectorSimulatorPy` se reemplazaron por `quantum_info.Operator` y `quantum_info.Statevector`; `BasicAer` se movió a `qiskit.providers.basic_provider` (`BasicProvider`, `BasicSimulator`) y `Aer` es el paquete separado `qiskit_aer` [@qiskit-docs, /guides/qiskit-1.0-features; /guides/metapackage-migration]. `AerSimulator` ofrece varios métodos: automático (por defecto), `statevector`, `density_matrix`, `stabilizer` (circuitos Clifford, muy grandes), `extended_stabilizer`, `matrix_product_state`, `unitary`, `superop` y `tensor_network` (solo GPU) [@qiskit-docs, /guides/local-testing-mode; /guides/local-simulators].

Aer incluye también sus propias primitivas V2 en `qiskit_aer.primitives`. Los circuitos deben transpilarse para `AerSimulator`, por ejemplo con `generate_preset_pass_manager(3, AerSimulator())`, y las primitivas de Aer carecen de algunas opciones de IBM, como el nivel de resiliencia [@qiskit-docs, /guides/simulate-with-qiskit-aer].

El efecto del ruido crece con el número de puertas ruidosas: para un `ZZ…Z` de 8 qubits con un ansatz `efficient_su2`, la documentación de IBM cita unos 0,887 en exacto y unos 0,725 con un 2 % de error despolarizante en cada CX, y estima la supervivencia del estado correcto como `(1−p)^m` para `m` puertas CX [@qiskit-docs, /guides/simulate-with-qiskit-aer].

### Ejemplo
Un modelo de ruido se construye con `NoiseModel`. Aquí cada `cx` sufre un [error despolarizante](../../quantum-mechanics/concepts/decoherence.md) del 2 % y comparamos el valor esperado de `ZZZZ` en un estado GHZ de 4 qubits, cuyo valor ideal es 1:

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error
from qiskit_aer.primitives import EstimatorV2 as AerEstimator

n = 4
ghz = QuantumCircuit(n)
ghz.h(0)
for i in range(n - 1):
    ghz.cx(i, i + 1)
obs = SparsePauliOp("Z" * n)

print("ideal:", StatevectorEstimator().run([(ghz, obs)]).result()[0].data.evs)

noise = NoiseModel()
noise.add_all_qubit_quantum_error(depolarizing_error(0.02, 2), ["cx"])
backend = AerSimulator(noise_model=noise)
isa = generate_preset_pass_manager(optimization_level=1, backend=backend).run(ghz)
est = AerEstimator(options={"backend_options": {"noise_model": noise}})
pub = (isa, obs.apply_layout(isa.layout))
print("con ruido:", est.run([pub], precision=0.02).result()[0].data.evs)
```

```text
ideal: 0.9999999999999998
con ruido: 0.937054682573371   (varía entre ejecuciones)
```

El circuito tiene 3 puertas `cx`, y con ruido el valor baja de 1 a unos 0,94. Observa el patrón de código: se transpila para el backend con ruido y el observable se lleva al circuito transpilado con `apply_layout`.

### Errores frecuentes
- *"Si funciona en el simulador, funcionará en el dispositivo."* Los estados ideales no incluyen ruido ni la conectividad del chip. El modelo de ruido de Aer probablemente es más suave que el real, y una `Session` se acepta pero se ignora en local [@qiskit-docs, /guides/local-testing-mode].
- *"Los simuladores con ruido escalan igual que los ideales."* El coste con ruido crece exponencialmente con el número de qubits [@qiskit-docs, /guides/local-testing-mode].
- *"Un simulador debería reproducir la mitigación de errores."* Las opciones de mitigación de IBM no están disponibles en los simuladores de referencia [@ibm-quantum-learning, "Cost functions"]; la mitigación se trata en la capa profesional.

### Para seguir
La capa profesional organiza estas herramientas en una escalera de pruebas, del ideal al dispositivo real. Antes, [primitivas: Sampler y Estimator](primitives-sampler-estimator.md) explica la interfaz común que usan todas ellas.

## Profesional {#layer-3}

### Idea clave
Prueba de lo ideal a lo real: estado exacto, ruido sintético, dispositivo falso y solo al final el dispositivo. El modo de prueba local de `qiskit-ibm-runtime` permite ejecutar el mismo código cambiando solo el backend, y a escala de cientos de qubits la verificación exacta ya no es posible [@qiskit-docs, /guides/local-testing-mode; @preskill-2018, §6, p. 7].

### Explicación
El *modo de prueba local (local testing mode)* de `qiskit-ibm-runtime` ejecuta localmente el código que irá al dispositivo, cambiando solo el backend. Este puede ser un dispositivo falso (`qiskit_ibm_runtime.fake_provider`, con una instantánea de la conectividad, las puertas base y el ruido) o `AerSimulator`, y `AerSimulator.from_backend(real_backend)` construye el ruido a partir de la calibración [@qiskit-docs, /guides/local-testing-mode]. Un procedimiento razonable para depurar es subir peldaños:

1. **Ideal:** `StatevectorEstimator`/`StatevectorSampler` para comprobar que el circuito hace lo que dice el algoritmo, con valores exactos.
2. **Ruido sintético:** `AerSimulator` con un `NoiseModel` para ver cómo se degrada un resultado según el error por puerta.
3. **Dispositivo falso:** transpilar y ejecutar contra un dispositivo falso, para validar que el flujo completo (transpilación, observables con `apply_layout`, opciones) funciona antes de gastar tiempo de QPU.
4. **Dispositivo real.**

Elegir simulador es una decisión de coste:

- *Ideal exacto con `Statevector`* para pruebas unitarias del circuito y hasta unas decenas de qubits.
- *`stabilizer`* si el circuito es solo Clifford, que permite circuitos muy grandes [@qiskit-docs, /guides/local-testing-mode].
- *Ruido realista:* el coste es exponencial, y un ejemplo de IBM Quantum Learning (resumido) desaconseja ejecutar circuitos mayores sobre dispositivos falsos porque la simulación con ruido es mucho más lenta que la exacta [@ibm-quantum-learning, "Utility I"].
- *Trabajos de prueba en la nube (dry run):* corren en un dispositivo simulado en la nube, devuelven datos aleatorios con el esquema correcto e informan `job.usage()`; requieren un plan de pago (Flex, Premium u On-Prem), mientras que el modo local no necesita cuenta [@qiskit-docs, /guides/local-testing-mode].

El método llega a un límite de verificación: un circuito de cientos de qubits ya no se puede comprobar con un simulador exacto. Es justo el régimen que describe Preskill, donde puede ser difícil validar que la respuesta sea correcta, sobre todo en simulación cuántica [@preskill-2018, §6, p. 7]. En ese régimen se verifican versiones reducidas del problema, observables con valor conocido o circuitos casi Clifford, y no el resultado completo; lo desarrollan [mitigación de errores](error-mitigation.md) y [la era NISQ](nisq-era.md). Los circuitos casi Clifford sirven de referencia porque son simulables exactamente y se usan como datos de entrenamiento para mitigar [@cai-2023, Sec. III.H, p. 19].

Para que las pruebas se puedan repetir, fija las semillas (`seed_simulator`, `seed_transpiler`) y las versiones, porque el resultado de un simulador con ruido depende de ambas. Documenta qué dispositivo falso usaste y con qué versión: cada uno es una instantánea del mapa de acoplamiento, las puertas base y el ruido de un dispositivo real [@qiskit-docs, /docs/en/guides/local-testing-mode].

### Ejemplo
El tercer peldaño de la escalera: un par de Bell con el ruido construido a partir de la calibración de `FakeManilaV2`.

```python
from qiskit import QuantumCircuit
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_aer import AerSimulator
from qiskit_aer.primitives import SamplerV2
from qiskit_ibm_runtime.fake_provider import FakeManilaV2

backend = AerSimulator.from_backend(FakeManilaV2())   # ruido a partir de la calibración
qc = QuantumCircuit(2); qc.h(0); qc.cx(0, 1); qc.measure_all()
isa = generate_preset_pass_manager(optimization_level=3, backend=backend).run(qc)
print(SamplerV2.from_backend(backend).run([isa], shots=2000).result()[0].data.meas.get_counts())
```

```text
{'11': 933, '00': 988, '01': 42, '10': 37}
```

Los conteos `01` y `10` (alrededor del 4 %) son el ruido del dispositivo falso; varían entre ejecuciones. Un par de Bell ideal nunca los produciría, y ese porcentaje es lo que habría que explicar o mitigar antes de pasar al dispositivo real.

### Para seguir
[Ejecutar en hardware real](running-on-hardware.md) usa este mismo flujo contra dispositivos de IBM. [Mitigación de errores](error-mitigation.md) trata qué hacer con el ruido que el simulador acaba de mostrar.
