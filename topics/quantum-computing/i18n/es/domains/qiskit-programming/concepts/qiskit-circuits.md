---
concept: qiskit-circuits
title: "Construir circuitos en Qiskit"
---

## Fundamentos {#layer-1}

**Idea.** En Qiskit, un [circuito cuántico](../../qubits-and-circuits/concepts/quantum-circuits.md) es un objeto `QuantumCircuit`: un conjunto de qubits más una lista ordenada de instrucciones [@qiskit-docs, /guides/construct-circuits]. El circuito es la pieza central de Qiskit y el resto del marco gira a su alrededor [@javadi-abhari-2024, Fig. 2, p. 5]. Para instalar y usar Qiskit hace falta el paquete `qiskit`; el simulador `qiskit-aer` se instala aparte [@qiskit-docs, /guides/metapackage-migration].

**Tu primer circuito: el par de Bell.** Se crea un circuito de 2 qubits y se añaden puertas con métodos: `h` para la [puerta Hadamard](../../qubits-and-circuits/concepts/single-qubit-gates.md) y `cx` para el [CNOT](../../qubits-and-circuits/concepts/two-qubit-gates.md) [@qiskit-docs, /guides/construct-circuits; /guides/hello-world].

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)          # control: qubit 0, objetivo: qubit 1
print(qc.draw("text"))
print("profundidad:", qc.depth(), "puertas:", dict(qc.count_ops()))
```

```text
     ┌───┐     
q_0: ┤ H ├──■──
     └───┘┌─┴─┐
q_1: ─────┤ X ├
          └───┘
profundidad: 2 puertas: {'h': 1, 'cx': 1}
```

La *profundidad (depth)* cuenta capas de puertas que pueden ejecutarse en paralelo y refleja aproximadamente el tiempo de ejecución [@qiskit-docs, /guides/construct-circuits].

**Medir.** Un circuito que va a devolver bits necesita medidas. `measure_all()` crea él mismo los bits clásicos en un registro llamado `meas` y antes inserta una *barrera (barrier)* [@qiskit-docs, /guides/construct-circuits; /guides/primitive-input-output]:

```python
qc.measure_all()
print(qc.draw("text"))
```

```text
        ┌───┐      ░ ┌─┐   
   q_0: ┤ H ├──■───░─┤M├───
        └───┘┌─┴─┐ ░ └╥┘┌─┐
   q_1: ─────┤ X ├─░──╫─┤M├
             └───┘ ░  ║ └╥┘
meas: 2/══════════════╩══╩═
                      0  1 
```

La medida sigue la [regla de Born](../../quantum-mechanics/concepts/born-rule-measurement.md): cada ejecución (un *shot*) da una cadena de bits al azar, y para un par de Bell esperaríamos `00` y `11` con probabilidad 1/2 cada una. En [simuladores y vectores de estado](simulators-and-statevectors.md) lo comprobamos.

**La trampa del orden de los bits.** Qiskit usa la convención *little-endian*: el qubit 0 es el bit de más a la derecha de la cadena, y los tensores se escriben `Q2⊗Q1⊗Q0` [@javadi-abhari-2024, §II.9, p. 4]. Con `x` en el qubit 0 de un circuito de 3 qubits el resultado es `001`, no `100`:

```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(3)
qc.x(0)                      # voltea solo el qubit 0
probs = Statevector(qc).probabilities_dict()
print({str(k): float(v) for k, v in probs.items()})
```

```text
{'001': 1.0}
```

Es la misma advertencia que en [estados de varios qubits](../../qubits-and-circuits/concepts/multi-qubit-states.md). Los circuitos se dibujan de izquierda a derecha en el tiempo, al revés de cómo se multiplican las matrices [@javadi-abhari-2024, §II.9, p. 4].

**Dos reglas que conviene grabarse ya.** Los circuitos que se envían a un *Sampler* necesitan medidas; los que se envían a un *Estimator* no deben tenerlas [@qiskit-docs, /guides/construct-circuits]. Ambos se explican en [primitivas](primitives-sampler-estimator.md).

## Comprensión {#layer-2}

**Qué puede contener un circuito.** Qiskit define "circuito" en sentido amplio: cualquier operación sobre datos cuánticos o clásicos, incluidos reinicios, puertas y medidas, y también operadores de alto nivel (unitarias, isometrías, Cliffords, transformadas de Fourier) [@javadi-abhari-2024, §III.A, p. 4]. Los niveles de abstracción pueden mezclarse en un mismo circuito, y los circuitos se componen como bloques [@javadi-abhari-2024, §III.A, p. 5]. Por eso se habla de varios niveles: el problema, el circuito abstracto, el circuito con puertas de la biblioteca estándar y el circuito con las puertas nativas del dispositivo (circuito ISA) [@javadi-abhari-2024, Fig. 1, p. 2]. Convertir uno en otro es el trabajo de la [transpilación](transpilation.md).

**Parámetros: construir una vez, usar muchas.** Un `Parameter` deja un valor sin definir para reutilizar el mismo circuito; `assign_parameters` devuelve copias con valores fijados, y `ParameterVector` crea grupos de parámetros con nombre [@qiskit-docs, /guides/construct-circuits]. Esto es la base de los [algoritmos variacionales](variational-algorithms.md), donde un mismo circuito se evalúa miles de veces con ángulos distintos.

```python
import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter, ParameterVector

theta = Parameter("theta")
qc = QuantumCircuit(1)
qc.ry(theta, 0)
print(qc.parameters)                                  # parámetros libres
print(qc.assign_parameters({theta: np.pi / 2}).draw("text"))
w = ParameterVector("w", 3)                           # w[0], w[1], w[2]
```

```text
ParameterView([Parameter(theta)])
   ┌─────────┐
q: ┤ Ry(π/2) ├
   └─────────┘
```

**Componer circuitos.** `compose` fusiona circuitos, acepta una correspondencia de qubits con `qubits=` y devuelve un circuito nuevo salvo que se pida `inplace=True`; `to_gate`/`to_instruction` empaquetan un circuito como una sola operación y `decompose` la expande de nuevo [@qiskit-docs, /guides/construct-circuits]. Los registros con nombre (`QuantumRegister`, `ClassicalRegister`) permiten organizar bits, y `find_bit` da el índice de un bit y su registro [@qiskit-docs, /guides/construct-circuits].

**Biblioteca de circuitos.** Circuitos ya hechos, como `efficient_su2` (un ansatz habitual) o `z_feature_map`, evitan reescribir patrones comunes [@qiskit-docs, /guides/simulate-with-qiskit-aer; /guides/construct-circuits]. En [algoritmos variacionales](variational-algorithms.md) se usa `efficient_su2` y `qaoa_ansatz`.

**Circuitos dinámicos.** Un circuito puede decidir qué instrucciones ejecuta mientras corre, con control de flujo sobre resultados de medidas mientras los qubits siguen coherentes; su modelo se parece al de OpenQASM 3 [@javadi-abhari-2024, §II.5, p. 3]. En código se usan `if_test`, `for_loop`, `switch` y el módulo `qiskit.circuit.classical.expr` para expresiones sobre bits medidos [@javadi-abhari-2024, §IV.D, p. 10]. Desde 2.0 la condición antigua `c_if` está eliminada [@qiskit-docs, /guides/qiskit-2.0]:

```python
from qiskit import QuantumCircuit
from qiskit.circuit import QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.transpiler import generate_preset_pass_manager

q, c = QuantumRegister(2, "q"), ClassicalRegister(2, "c")
qc = QuantumCircuit(q, c)
qc.x(0)
qc.measure(0, c[0])
with qc.if_test((c[0], 1)):      # si el bit medido vale 1, voltea el qubit 1
    qc.x(1)
qc.measure(1, c[1])
sim = AerSimulator()
isa = generate_preset_pass_manager(optimization_level=1, backend=sim).run(qc)
print(sim.run(isa, shots=100).result().get_counts())
```

```text
{'11': 100}
```

(Aquí `backend.run` se usa solo para ejecutar un circuito en un simulador; para obtener resultados de interés se usan las [primitivas](primitives-sampler-estimator.md).)

**Cómo guarda Qiskit un circuito por dentro.** Por defecto es una lista de instrucciones; muchos algoritmos de reescritura prefieren un grafo acíclico dirigido (DAG) que hace explícito el orden de las operaciones y el flujo de información. Las puertas comunes son *singletons* y la síntesis de operaciones abstractas se aplaza al transpilador [@javadi-abhari-2024, §III.A, p. 5]. La salida del transpilador es otro circuito, así que se inspecciona con las mismas herramientas [@javadi-abhari-2024, §III.B, p. 6].

**Convenciones que sorprenden.** Para `CX`, el qubit 0 es el control y el 1 el objetivo, y la matriz resultante puede diferir de la de algunos libros porque el orden de bits está invertido; usar `CX(Q1, Q0)` en el circuito la cambia [@javadi-abhari-2024, §II.9, p. 4].

**Errores frecuentes.**

- *"`measure_all()` y `measure()` son lo mismo."* `measure_all` crea sus propios bits clásicos y una barrera; `measure(qubits, bits)` asigna qubits concretos a bits concretos, y `measure_active` mide solo qubits con operaciones [@qiskit-docs, /guides/construct-circuits].
- *"Un tutorial antiguo con `execute(...)` es válido."* `execute` se eliminó en 1.0 [@qiskit-docs, /guides/qiskit-1.0-features].

## Profesional {#layer-3}

**Diseño: qué construir y qué dejar al transpilador.** Qiskit retrasa la síntesis de operaciones de alto nivel (una QFT, un `PauliEvolutionGate`, la estimación de fase con potencias controladas) hasta el transpilador, que puede sintetizarlas directamente para el dispositivo sin pasos intermedios que alarguen la profundidad [@javadi-abhari-2024, §II.4, p. 3; Fig. 3, p. 6]. Criterio: expresa el circuito al nivel más alto que tenga sentido (por ejemplo, [estimación de fase](../../quantum-algorithms/concepts/phase-estimation.md) o [simulación de hamiltonianos](../../quantum-algorithms/concepts/hamiltonian-simulation.md) con bloques abstractos), y baja a puertas concretas solo cuando necesites control sobre el resultado.

**Parametrizar casi siempre.** Cuando el mismo circuito se evalúa muchas veces (barridos, optimización), constrúyelo con `Parameter`s y transpílalo una vez a `optimization_level=3`; solo hay que asignar valores en cada iteración [@qiskit-docs, /guides/construct-circuits]. Qiskit prevé en la interfaz de primitivas varias asignaciones de parámetros para una misma plantilla [@javadi-abhari-2024, §IV.B, p. 7].

**Control de flujo en tiempo real.** Los circuitos dinámicos permiten medir a mitad de circuito y reaccionar: reinicio de ancillas con una `X` condicionada, repetición de pasos, etc. En un experimento de simulación, sustituir una serie de `if` por un único `switch` hizo constante la duración del circuito y se añadieron rotaciones `Z` inversas condicionadas para compensar la diafonía estática [@javadi-abhari-2024, App. A, p. 17]. Hay límites: en el ISA de Heron el modelo de ejecución serializa el control de flujo y no da tiempos para las expresiones clásicas, lo que perjudica los circuitos dinámicos cortos [@javadi-abhari-2024, App. B, pp. 18-19]. Y esos circuitos se ejecutan en [hardware real](running-on-hardware.md), no en el simulador de estado.

**Versionado y migración.** Qiskit es ahora la única distribución `qiskit` (`qiskit-terra` quedó retirada); al migrar se recomienda un entorno virtual nuevo, no una actualización in situ, y desde 2.0 solo hay soporte para plataformas de 64 bits [@qiskit-docs, /guides/metapackage-migration; /guides/install-qiskit]. Las migraciones de nombres más comunes: `bind_parameters` a `assign_parameters`; `cnot`, `toffoli`, `fredkin`, `mct` a `cx`, `ccx`, `cswap`, `mcx`; `QuantumCircuit.qasm()` a `qasm2.dump`/`dumps`; `qiskit.extensions` a `qiskit.circuit.library` [@qiskit-docs, /guides/qiskit-1.0-features]. Si necesitas la duración de un circuito, `Instruction.duration` ya no existe: se usa `Target` o `QuantumCircuit.estimate_duration` [@qiskit-docs, /guides/qiskit-2.0].

**Consejo práctico para reproducibilidad.** Fija las versiones (`qiskit~=2.6`, `qiskit-ibm-runtime~=0.51`) y comprueba la versión indicada en cada página de la documentación, porque no son coherentes entre sí [@qiskit-docs, versiones]. Para circuitos que se envían a un dispositivo recuerda que las ISA solo admiten instrucciones del `Target` del dispositivo; lo desarrolla [transpilación](transpilation.md).
