---
concept: running-on-hardware
title: "Ejecutar en hardware real (IBM Quantum)"
---

## Comprensión {#layer-2}

**El flujo completo.** Ejecutar en un ordenador cuántico real sigue los cuatro pasos de los *patrones de Qiskit (Qiskit patterns)*: (1) *mapear* el problema a circuitos y operadores; (2) *optimizar*, es decir, [transpilar](transpilation.md) a un circuito ISA para el dispositivo; (3) *ejecutar* con un [Sampler o un Estimator](primitives-sampler-estimator.md), opcionalmente en un `Batch` o `Session` y con supresión y mitigación; (4) *postprocesar* (visualizar, mitigar la lectura, marginalizar, postseleccionar) [@qiskit-docs, /guides/intro-to-patterns; @javadi-abhari-2024, §II.7, p. 4]. Los patrones pueden iterar (bucle alrededor de los tres últimos pasos, como en los [algoritmos variacionales](variational-algorithms.md)) o incrustar cómputo cuántico en grandes cálculos clásicos [@javadi-abhari-2024, §II.7, p. 4].

**Cuenta, servicio y dispositivo.** Hace falta una cuenta de IBM Cloud y un acceso a IBM Quantum Platform. Cada cuenta tiene *instancias*, identificadas por un CRN y vinculadas a una región, que fija dónde se ejecutan los trabajos; una misma clave de API sirve en todas las regiones [@qiskit-docs, /guides/cloud-setup]. `QiskitRuntimeService(channel, token, instance)` crea el servicio; el canal por defecto es `ibm_quantum_platform`, y `channel="local"` no necesita autenticación [@qiskit-docs, /guides/initialize-account]. Las credenciales se guardan una vez con `save_account` [@qiskit-docs, /guides/hello-world].

Un dispositivo se representa con un *backend*, y su `Target` modela la ISA, las propiedades y las restricciones [@ibm-quantum-learning, "Hardware"]; el `Target` es un modelo abstracto de la máquina con las instrucciones disponibles, sus tiempos y sus tasas de error [@javadi-abhari-2024, §II.3, p. 3]. Se obtiene con `backend.target` y de él un mapa de acoplamiento con `target.build_coupling_map()` [@javadi-abhari-2024, §IV.B, p. 7].

```python
# NECESITA UNA CUENTA DE IBM: no se ha podido ejecutar en esta redacción.
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime.executor_estimator import Estimator

# QiskitRuntimeService.save_account(token="...", instance="...")  # una sola vez
service = QiskitRuntimeService()
backend = service.least_busy(simulator=False, operational=True, min_num_qubits=127)

bell = QuantumCircuit(2); bell.h(0); bell.cx(0, 1)
isa = generate_preset_pass_manager(backend=backend, optimization_level=3).run(bell)
obs = [SparsePauliOp(p).apply_layout(isa.layout) for p in ("ZZ", "XX")]

estimator = Estimator(mode=backend)
estimator.options.default_shots = 5000
job = estimator.run([(isa, obs)])
print(job.job_id())               # el trabajo puede recuperarse más tarde con este id
result = job.result()[0]
print(result.data.evs, result.data.stds)
```

Es la estructura del ejemplo "hello world" de la documentación: circuito Bell, observables como `SparsePauliOp`, transpilar, `estimator.run([(isa_circuit, mapped_observables)])`, `job.job_id()` y lectura de `evs` y `stds` [@qiskit-docs, /guides/hello-world]. `service.least_busy(...)` elige un dispositivo [@qiskit-docs, /guides/hello-world]. (Las opciones `default_shots` y las clases `executor_estimator.Estimator` corresponden a las primitivas del lado del cliente de `qiskit-ibm-runtime` 0.50.0 o posterior [@qiskit-docs, /guides/hello-world; /guides/local-testing-mode].)

**Ensayar el mismo código sin cuenta.** Con un dispositivo falso, el mismo flujo corre en local. Este bloque sí se ha ejecutado (5 qubits, `FakeManilaV2`):

```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime.executor_estimator import Estimator
from qiskit_ibm_runtime.executor_sampler import Sampler
from qiskit_ibm_runtime.fake_provider import FakeManilaV2

backend = FakeManilaV2()          # instantánea de un dispositivo; sin cuenta
bell = QuantumCircuit(2); bell.h(0); bell.cx(0, 1)
pm = generate_preset_pass_manager(optimization_level=3, backend=backend, seed_transpiler=1)
isa = pm.run(bell)
obs = [SparsePauliOp(p).apply_layout(isa.layout) for p in ("ZZ", "XX")]

est = Estimator(mode=backend)
est.options.default_shots = 4000
est.options.resilience_level = 0  # sin mitigación, para ver el ruido bruto
res = est.run([(isa, obs)]).result()[0]
print(res.data.evs)

meas = bell.copy(); meas.measure_all()
print(Sampler(mode=backend).run([(pm.run(meas),)], shots=4000).result()[0].data.meas.get_counts())
```

```text
[0.936 0.9225]
{'00': 1923, '11': 1951, '10': 62, '01': 64}
```

(Salida de una ejecución; los valores varían.) Los dos valores esperados no llegan a 1 y aparecen `01` y `10`, que un par de Bell ideal no produciría: es el ruido del dispositivo falso. En nuestras pruebas con la versión 0.51.0, el modo local ejecuta este código con ruido; con un dispositivo falso de 127 qubits y estas primitivas la simulación local falló por falta de memoria, de modo que usamos uno de 5 qubits. Para circuitos pequeños, la propia documentación sugiere un dispositivo falso para evitar la cola [@qiskit-docs, /guides/hello-world].

**Modos de ejecución.** Se eligen con `mode=` [@qiskit-docs, /guides/execution-modes]:

| Modo | Qué es | Cuándo |
|---|---|---|
| Job (`mode=backend`) | una única petición de primitiva | una ejecución suelta |
| Batch | trabajos independientes enviados juntos; sin garantía de orden ni acceso exclusivo | muchos circuitos independientes |
| Session | acceso exclusivo mientras dura; bloquea además trabajos de calibración | trabajo iterativo (bucles variacionales) |

En batch y session, el primer trabajo espera igualmente en la cola normal, así que ninguno ayuda a un trabajo único [@qiskit-docs, /guides/execution-modes]. Los usuarios del plan Open no pueden enviar trabajos de sesión, y los trabajos de prueba (*dry run*) no admiten sesión [@qiskit-docs, /guides/execution-modes; /guides/run-jobs-session].

**Por qué está así diseñado.** Las primitivas pueden implementarse en un entorno de ejecución con cómputo cuántico y clásico estrechamente acoplados; la co-ubicación reduce la latencia de tareas como optimizar circuitos para supresión de errores, circuitos extra para mitigación, postprocesado y actualización de parámetros [@javadi-abhari-2024, §III.C, p. 7]. Se distingue el cómputo clásico "en tiempo real" (mientras los qubits son coherentes) del "casi en tiempo real" (parámetros, compilación, mitigación) [@javadi-abhari-2024, §II.5, p. 3].

**Qué hardware hay detrás.** Los procesadores de IBM son qubits [superconductores](../../quantum-hardware/concepts/superconducting-qubits.md) de tipo transmón en una red heavy-hex, con flotas de más de 100 qubits [@ibm-quantum-learning, "Running quantum circuits"]. La base de puertas cambia según la familia: en el resumen de IBM, Eagle usa `ecr, id, rz, sx, x` y Heron usa `cz, id, rz, sx, x` [@ibm-quantum-learning, "Hardware"]. Un ejemplo de dispositivo tipo Eagle da `T1` mediano ~285 µs, `T2` ~173 µs, y las tasas de error ordenadas de menor a mayor: un qubit, dos qubits, lectura [@ibm-quantum-learning, "Hardware"]; ver [coherencia y fidelidad](../../quantum-hardware/concepts/coherence-and-fidelity.md). La profundidad importa porque las puertas llevan tiempo y la [decoherencia](../../quantum-mechanics/concepts/decoherence.md) limita la profundidad viable [@ibm-quantum-learning, "Running quantum circuits"]. Un ejemplo real del artículo de arquitectura: un dispositivo de 127 qubits (transmones de frecuencia fija, heavy-hex, resonancia cruzada) en el que la medida duró 1400 ns y la retroalimentación 1060 ns [@javadi-abhari-2024, §IV.A, p. 7; App. A, p. 17]. Preskill ya preveía en 2018 que los ordenadores cuánticos cercanos serían dispositivos de propósito especial a los que la mayoría accedería por la nube [@preskill-2018, §6, p. 7].

**Errores frecuentes.**

- *"Una sesión me ahorra la cola."* No: el primer trabajo de un batch o una sesión espera como cualquier otro [@qiskit-docs, /guides/execution-modes].
- *"Puedo enviar un circuito cualquiera al dispositivo."* Debe ser ISA [@qiskit-docs, /guides/transpile].
- *"Los resultados del dispositivo coinciden con el simulador."* En un ejemplo de VQE de IBM Quantum Learning, el resultado en hardware se alejó varios puntos porcentuales del obtenido en el simulador [@ibm-quantum-learning, "Instances and extensions"].

## Profesional {#layer-3}

**Elegir el modo de ejecución.** Criterios, a partir de lo que documenta IBM [@qiskit-docs, /guides/execution-modes; /guides/run-jobs-session]:

- *Bucle variacional (optimizador clásico llamando a la QPU muchas veces):* `Session`, porque permite el intercambio frecuente clásico-cuántico sin volver a la cola en cada actualización de parámetros [@qiskit-docs, /guides/run-jobs-session; @ibm-quantum-learning, "Cost functions"]. Fija `max_time` mayor que el trabajo más largo; el TTL máximo predeterminado es de 8 horas en Premium y el TTL interactivo, 60 s. Cierra con `session.close()` o un gestor de contexto; los trabajos en cola se ejecutan igualmente [@qiskit-docs, /guides/run-jobs-session].
- *Muchos circuitos independientes (barridos, tomografía):* `Batch`.
- *Pruebas o un único circuito:* modo `Job`.
- *Plan Open:* no hay sesiones; los lotes y los trabajos únicos son la opción.

Cuando termina el TTL, los trabajos encolados fallan [@qiskit-docs, /guides/execution-modes]. Una sesión bloquea los trabajos de calibración, lo que tiene un coste de oportunidad para otros usuarios [@qiskit-docs, /guides/execution-modes]. Demasiados envíos seguidos pueden provocar el error 1217 [@ibm-quantum-learning, "Cost functions"].

**Elegir el dispositivo.** `least_busy` minimiza la espera, pero no la calidad. El número de qubits no es la única medida: cuentan la precisión de las puertas, su velocidad, la precisión de la medida, la conectividad y el rendimiento de fabricación [@preskill-2018, §4.2, p. 5]. En la práctica se comparan el error de las puertas de dos qubits, el error de lectura y el tamaño de la región conectada del dispositivo con lo que necesita el circuito transpilado (ver [transpilación](transpilation.md)). IBM menciona métricas de dispositivo como QuOps, circuitos por segundo, EPLG y CLOPS [@ibm-quantum-learning, "Running quantum circuits"] sin que las notas den su definición [unverified].

**Coste y presupuesto de tiempo de QPU.** Los trabajos de prueba (*dry run*) en un dispositivo simulado en la nube devuelven datos aleatorios con el esquema correcto e informan `job.usage()` sin gastar hardware; requieren un plan de pago [@qiskit-docs, /guides/local-testing-mode]. Úsalos para estimar el uso antes de lanzar un experimento caro. Reduce el coste primero con transpilación, y después con la elección de opciones de mitigación (ver [mitigación de errores](error-mitigation.md)): por ejemplo, ZNE con tres factores de ruido cuesta aproximadamente 3 veces más [@qiskit-docs, /guides/configure-error-mitigation].

**Errores de postprocesado.** Cuenta las fuentes de error cuando interpretes un resultado: un ejemplo de QAOA de 5 nodos en IBM señala el algoritmo aproximado con pocas capas, el muestreo finito y el error de lectura; más shots reducen el error de muestreo pero no los otros [@ibm-quantum-learning, "Utility-scale QAOA"]. Un hardware ruidoso da evaluaciones no deterministas del coste, que pueden impedir la convergencia de un optimizador [@ibm-quantum-learning, "Cost functions"].

**Servicios de más alto nivel.** Las *Qiskit Functions* son servicios construidos por socios (funciones de circuito como Algorithmiq TEM, Q-CTRL o Qedma QESEM, y funciones de aplicación para optimización y química) y los *addons* de Qiskit (Qiskit Mitigation, aprendizaje de ruido, diagonalización cuántica basada en muestras) ofrecen componentes para tu propio flujo [@qiskit-docs, /guides]. Criterio: si tu problema encaja con una función de aplicación, sirve para empezar; para investigación o comprensión, el flujo propio con primitivas es más transparente.

**Límites del modelo de ejecución actual.** El ISA de Heron no da tiempos para las expresiones clásicas ni para ramas de control de flujo, y el modelo serializa todo el control de flujo, lo que perjudica los circuitos dinámicos cortos; los autores del artículo prevén ramas de igual duración, bucles contables y la instrucción `stretch` de OpenQASM [@javadi-abhari-2024, App. B, pp. 18-19]. Estos detalles describen Qiskit 1.0 y Heron en 2024: comprueba el estado actual.

**Registro de experimentos.** El identificador de cada trabajo permite recuperarlo más tarde [@qiskit-docs, /guides/hello-world]. Anota además la versión de Qiskit y del runtime, el dispositivo, las opciones y la semilla del transpilador (es una recomendación de este curso, no de las fuentes) para que otra persona pueda repetir el flujo.
