---
concept: qiskit-circuits
title: "Construir circuitos en Qiskit"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
En Qiskit, un [circuito cuántico](../../qubits-and-circuits/concepts/quantum-circuits.md) es un objeto `QuantumCircuit`: un conjunto de qubits más una lista ordenada de instrucciones. Es la pieza central de Qiskit y el resto del marco gira a su alrededor [@qiskit-docs, /guides/construct-circuits; @javadi-abhari-2024, Fig. 2, p. 5].

### Explicación
Para usar Qiskit hace falta el paquete `qiskit`; el simulador `qiskit-aer` se instala aparte [@qiskit-docs, /guides/metapackage-migration]. Un circuito se crea con un número de qubits y se le añaden puertas con métodos: `h` para la [puerta Hadamard](../../qubits-and-circuits/concepts/single-qubit-gates.md) y `cx` para el [CNOT](../../qubits-and-circuits/concepts/two-qubit-gates.md) [@qiskit-docs, /guides/construct-circuits; /guides/hello-world].

Dos números resumen un circuito. La *profundidad (depth)* cuenta las capas de puertas que pueden ejecutarse en paralelo y refleja aproximadamente el tiempo de ejecución [@qiskit-docs, /guides/construct-circuits]. El recuento de puertas dice cuántas hay de cada tipo.

Un circuito que va a devolver bits necesita medidas. `measure_all()` crea él mismo los bits clásicos, en un registro llamado `meas`, y antes inserta una *barrera (barrier)* [@qiskit-docs, /guides/construct-circuits; /guides/primitive-input-output]. La medida sigue la [regla de Born](../../quantum-mechanics/concepts/born-rule-measurement.md): cada ejecución (un *shot*) da una cadena de bits al azar, y para un par de Bell esperaríamos `00` y `11` con probabilidad 1/2 cada una. En [simuladores y vectores de estado](simulators-and-statevectors.md) lo comprobamos.

La trampa más habitual está en el orden de los bits. Qiskit usa la convención *little-endian*: el qubit 0 es el bit de más a la derecha de la cadena, y los tensores se escriben `Q2⊗Q1⊗Q0` [@javadi-abhari-2024, §II.9, p. 4]. Es la misma advertencia que en [estados de varios qubits](../../qubits-and-circuits/concepts/multi-qubit-states.md). Además, los circuitos se dibujan de izquierda a derecha en el tiempo, al revés de cómo se multiplican las matrices [@javadi-abhari-2024, §II.9, p. 4].

Por último, hay una regla que conviene grabarse ya: los circuitos que se envían a un *Sampler* necesitan medidas, y los que se envían a un *Estimator* no deben tenerlas [@qiskit-docs, /guides/construct-circuits]. Ambos se explican en el siguiente nivel de este ámbito.

### Ejemplo
Primero, el par de Bell: un circuito de 2 qubits con `h` en el qubit 0 y un `cx` con control en el 0 y objetivo en el 1.

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

La profundidad es 2 porque `cx` solo puede ejecutarse después de `h`. Para medir, se añade `measure_all()`:

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

Y para ver el orden de los bits, un circuito de 3 qubits con `x` solo en el qubit 0 da `001`, no `100`:

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

### Errores frecuentes
- *"El qubit 0 es el primer bit por la izquierda de la cadena."* En Qiskit es el de más a la derecha: `x` sobre el qubit 0 da `001` [@javadi-abhari-2024, §II.9, p. 4].
- *"Da igual poner medidas o no, según la primitiva."* Un Sampler las necesita y un Estimator no las admite [@qiskit-docs, /guides/construct-circuits].

### Para seguir
[Simuladores y vectores de estado](simulators-and-statevectors.md) permite ejecutar estos circuitos sin hardware y comprobar las probabilidades. La capa de comprensión de este concepto añade parámetros, composición y circuitos dinámicos.

## Comprensión {#layer-2}

### Idea clave
Qiskit entiende "circuito" en sentido amplio: puertas, medidas, reinicios y operadores de alto nivel que pueden mezclarse y componerse como bloques. Un mismo circuito puede dejar valores sin definir (`Parameter`) para reutilizarlo, y puede decidir qué ejecuta mientras corre [@javadi-abhari-2024, §III.A, pp. 4-5; §II.5, p. 3].

### Explicación
Un circuito de Qiskit admite cualquier operación sobre datos cuánticos o clásicos, incluidos reinicios, puertas y medidas, y también operadores de alto nivel (unitarias, isometrías, Cliffords, transformadas de Fourier) [@javadi-abhari-2024, §III.A, p. 4]. Los niveles de abstracción pueden mezclarse en un mismo circuito, y los circuitos se componen como bloques [@javadi-abhari-2024, §III.A, p. 5]. De ahí que se hable de varios niveles: el problema, el circuito abstracto, el circuito con puertas de la biblioteca estándar y el circuito con las puertas nativas del dispositivo (circuito ISA) [@javadi-abhari-2024, Fig. 1, p. 2]. Convertir uno en otro es el trabajo de la [transpilación](transpilation.md).

Esa flexibilidad se aprovecha primero con los parámetros. Un `Parameter` deja un valor sin definir para reutilizar el mismo circuito; `assign_parameters` devuelve copias con valores fijados, y `ParameterVector` crea grupos de parámetros con nombre [@qiskit-docs, /guides/construct-circuits]. Es la base de los [algoritmos variacionales](variational-algorithms.md), donde un mismo circuito se evalúa miles de veces con ángulos distintos.

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

También se aprovecha componiendo. `compose` fusiona circuitos, acepta una correspondencia de qubits con `qubits=` y devuelve un circuito nuevo salvo que se pida `inplace=True`; `to_gate` y `to_instruction` empaquetan un circuito como una sola operación y `decompose` la expande de nuevo. Los registros con nombre (`QuantumRegister`, `ClassicalRegister`) organizan los bits, y `find_bit` da el índice de un bit y su registro [@qiskit-docs, /guides/construct-circuits]. Para no reescribir patrones comunes hay una biblioteca de circuitos ya hechos, como `efficient_su2` (un ansatz habitual) o `z_feature_map` [@qiskit-docs, /guides/simulate-with-qiskit-aer; /guides/construct-circuits]; `efficient_su2` y `qaoa_ansatz` se usan en los algoritmos variacionales.

Más allá de componer, un circuito puede decidir qué instrucciones ejecuta mientras corre, con control de flujo sobre resultados de medidas mientras los qubits siguen coherentes; es el modelo de los *circuitos dinámicos*, parecido al de OpenQASM 3 [@javadi-abhari-2024, §II.5, p. 3]. En código se usan `if_test`, `for_loop`, `switch` y el módulo `qiskit.circuit.classical.expr` para expresiones sobre bits medidos [@javadi-abhari-2024, §IV.D, p. 10]. Desde 2.0 la condición antigua `c_if` está eliminada [@qiskit-docs, /guides/qiskit-2.0].

Por dentro, un circuito es por defecto una lista de instrucciones; muchos algoritmos de reescritura prefieren un grafo acíclico dirigido (DAG), que hace explícito el orden de las operaciones y el flujo de información. Las puertas comunes son *singletons* y la síntesis de operaciones abstractas se aplaza al transpilador [@javadi-abhari-2024, §III.A, p. 5]. La salida del transpilador es otro circuito, así que se inspecciona con las mismas herramientas [@javadi-abhari-2024, §III.B, p. 6].

Una última convención sorprende: para `CX`, el qubit 0 es el control y el 1 el objetivo, y la matriz resultante puede diferir de la de algunos libros porque el orden de bits está invertido; usar `CX(Q1, Q0)` en el circuito la cambia [@javadi-abhari-2024, §II.9, p. 4].

### Ejemplo
Un circuito dinámico que mide el qubit 0 y, según el resultado, voltea el qubit 1:

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

Paso a paso: `x(0)` deja el qubit 0 en 1; la medida guarda ese 1 en `c[0]`; como el bit vale 1, `if_test` ejecuta la `x(1)`; la segunda medida guarda otro 1 en `c[1]`. Por eso las 100 ejecuciones dan `11`. (Aquí `backend.run` se usa solo para ejecutar un circuito en un simulador; para obtener resultados de interés se usan las [primitivas](primitives-sampler-estimator.md).)

### Errores frecuentes
- *"`measure_all()` y `measure()` son lo mismo."* `measure_all` crea sus propios bits clásicos y una barrera; `measure(qubits, bits)` asigna qubits concretos a bits concretos, y `measure_active` mide solo qubits con operaciones [@qiskit-docs, /guides/construct-circuits].
- *"Un tutorial antiguo con `execute(...)` es válido."* `execute` se eliminó en 1.0 [@qiskit-docs, /guides/qiskit-1.0-features].

### Para seguir
La capa profesional de este concepto trata de qué construir a mano y qué dejar al transpilador. Antes, [primitivas: Sampler y Estimator](primitives-sampler-estimator.md) explica cómo pedir resultados de un circuito.

## Profesional {#layer-3}

### Idea clave
Expresa el circuito al nivel más alto que tenga sentido y deja que el transpilador sintetice las operaciones abstractas para el dispositivo; si lo vas a evaluar muchas veces, parametrízalo y transpílalo una sola vez [@javadi-abhari-2024, §II.4, p. 3; @qiskit-docs, /guides/construct-circuits].

### Explicación
Qiskit retrasa la síntesis de operaciones de alto nivel (una QFT, un `PauliEvolutionGate`, la estimación de fase con potencias controladas) hasta el transpilador, que puede sintetizarlas directamente para el dispositivo sin pasos intermedios que alarguen la profundidad [@javadi-abhari-2024, §II.4, p. 3; Fig. 3, p. 6]. Criterio: expresa el circuito al nivel más alto posible (por ejemplo, [estimación de fase](../../quantum-algorithms/concepts/phase-estimation.md) o [simulación de hamiltonianos](../../quantum-algorithms/concepts/hamiltonian-simulation.md) con bloques abstractos) y baja a puertas concretas solo cuando necesites control sobre el resultado.

Cuando el mismo circuito se evalúa muchas veces (barridos, optimización), constrúyelo con `Parameter`s y transpílalo una vez a `optimization_level=3`; en cada iteración solo hay que asignar valores [@qiskit-docs, /guides/construct-circuits]. La interfaz de primitivas prevé varias asignaciones de parámetros para una misma plantilla [@javadi-abhari-2024, §IV.B, p. 7].

Los circuitos dinámicos añaden control de flujo en tiempo real: medir a mitad de circuito y reaccionar, por ejemplo reiniciando ancillas con una `X` condicionada o repitiendo pasos. En un experimento de simulación, sustituir una serie de `if` por un único `switch` hizo constante la duración del circuito, y se añadieron rotaciones `Z` inversas condicionadas para compensar la diafonía estática [@javadi-abhari-2024, App. A, p. 17]. Hay límites: en el ISA de Heron el modelo de ejecución serializa el control de flujo y no da tiempos para las expresiones clásicas, lo que perjudica los circuitos dinámicos cortos [@javadi-abhari-2024, App. B, pp. 18-19]. Y esos circuitos se ejecutan en [hardware real](running-on-hardware.md), no en el simulador de estado.

Para que el trabajo sea reproducible, fija las versiones (`qiskit~=2.6`, `qiskit-ibm-runtime~=0.51`) y comprueba la indicada en cada página de la documentación, porque no son coherentes entre sí [@qiskit-docs, versiones]. Recuerda también que las ISA solo admiten instrucciones del `Target` del dispositivo; lo desarrolla [transpilación](transpilation.md).

### Ejemplo
Migrar un tutorial antiguo a Qiskit 2.x. Qiskit es ahora la única distribución `qiskit` (`qiskit-terra` quedó retirada); al migrar se recomienda un entorno virtual nuevo, no una actualización in situ, y desde 2.0 solo hay soporte para plataformas de 64 bits [@qiskit-docs, /guides/metapackage-migration; /guides/install-qiskit]. Después, los cambios de nombre más comunes [@qiskit-docs, /guides/qiskit-1.0-features]:

- `bind_parameters` pasa a `assign_parameters`.
- `cnot`, `toffoli`, `fredkin`, `mct` pasan a `cx`, `ccx`, `cswap`, `mcx`.
- `QuantumCircuit.qasm()` pasa a `qasm2.dump`/`dumps`.
- `qiskit.extensions` pasa a `qiskit.circuit.library`.

Y si el código necesita la duración de un circuito, `Instruction.duration` ya no existe: se usa `Target` o `QuantumCircuit.estimate_duration` [@qiskit-docs, /guides/qiskit-2.0].

### Para seguir
[Transpilación](transpilation.md) explica cómo se convierte el circuito abstracto en uno ISA, y [ejecutar en hardware real](running-on-hardware.md) lo que ocurre después.
