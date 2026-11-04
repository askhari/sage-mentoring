---
concept: quantum-circuits
title: "Circuitos cuánticos y medida"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
Un **circuito cuántico (quantum circuit)** es una red sin bucles de cables (qubits) y puertas (unitarias o medidas) por la que la información fluye de izquierda a derecha; es la representación estándar de un algoritmo cuántico [@watrous-2025, L3.1, PDF pp. 69-70, 73; @de-wolf-2026, §2.1.2, p. 27].

### Explicación
Los cables son qubits y las puertas son operaciones unitarias o medidas en la base estándar; hay un cable horizontal por qubit, y las puertas se evalúan en el orden en que aparecen [@watrous-2025, L3.1, PDF pp. 69-70, 73; @de-wolf-2026, §2.1.2, p. 27]. Una persona programa dibujando (o escribiendo) un circuito.

Los circuitos suelen empezar con todos los qubits en `|0⟩`, aunque pueden empezar con otros estados; en los cables se puede anotar el estado de entrada y el de salida [@watrous-2025, L3.1, PDF p. 73]. Al final se miden algunos o todos los qubits en la base estándar para obtener una salida clásica [@de-wolf-2026, §2.1.2, p. 27; @preskill-ph219, ch.5 §5.3, pp. 22-23].

Los cables de bits clásicos se dibujan con doble línea. Una puerta de medida escribe el resultado de la base estándar en un bit clásico y deja el qubit en `|0⟩` o `|1⟩`; en la forma compacta, la medida toma el qubit y lo sustituye por un bit clásico [@watrous-2025, L3.1, PDF pp. 76-77]. Una puerta con control clásico se aplica o no según el valor de ese bit; es lo que hace Bob en la teleportación [@watrous-2025, L4.1, PDF p. 98].

Para ampliar el sistema no se bifurca un cable (eso no es unitario): se añade un qubit nuevo, llamado *ancilla* [@aaronson-2018, Lec4, p. 3]. Los qubits de trabajo inicializados a `|0⟩` son habituales [@watrous-2025, L3.3, PDF p. 96].

Para pasar del dibujo a las matrices, el circuito `H, S, H, T` (de izquierda a derecha) tiene como operador total el producto `T·H·S·H`: la última puerta multiplica por la izquierda [@watrous-2025, L3.1, PDF p. 73]. Con entrada `|0⟩`, el resultado es `((1+i)/2)|0⟩ + (1/√2)|1⟩`; el cálculo paso a paso está en [puertas de un qubit](single-qubit-gates.md).

El orden de los qubits sigue la misma convención que en [estados de varios qubits](multi-qubit-states.md): Qiskit pone `q_0` arriba y a la derecha de la cadena; Watrous lo usa en todo su texto y lo describe como la inversión de una convención más común [@watrous-2025, L3.1, PDF p. 74].

### Ejemplo
El par de Bell: dos cables, `|00⟩` de entrada, `H` en el primero y `CNOT` con control en el primero. En matrices (orden de base `00, 01, 10, 11`, primer qubit a la izquierda):

```
H⊗I = (1/√2)·[[1,0, 1, 0],        CNOT·(H⊗I) = (1/√2)·[[1,0, 1, 0],
              [0,1, 0, 1],                            [0,1, 0, 1],
              [1,0,-1, 0],                            [0,1, 0,-1],
              [0,1, 0,-1]]                            [1,0,-1, 0]]
```

La matriz del circuito completo es el producto de la de `CNOT` por `I⊗H` en la convención de Qiskit (o `H⊗I`, si el primer qubit va a la izquierda) [@watrous-2025, L3.1, PDF pp. 75-76]. Su primera columna es `(1,0,0,1)ᵀ/√2 = |φ⁺⟩`; las demás columnas son `|ψ⁺⟩`, `|φ⁻⟩`, `|ψ⁻⟩`, de modo que la unitaria convierte la base estándar en la base de Bell [@preskill-ph219, ch.4 §4.1.1, pp. 6-8; @watrous-2025, L3.1, PDF pp. 74-76]. Ver [entrelazamiento](entanglement.md) para el diagrama paso a paso.

### Para seguir
La capa 2 relaciona estos circuitos con los booleanos, explica por qué se puede aplazar la medida y define tamaño y profundidad.

## Comprensión {#layer-2}

### Idea clave
Un circuito cuántico generaliza el booleano con puertas unitarias pequeñas y reversibles; toda medida puede aplazarse al final, así que un cálculo es una parte unitaria seguida de una lectura [@de-wolf-2026, §2.1.1-2.1.2, pp. 25-27; @watrous-2025, L6.2, PDF pp. 171-172].

### Explicación
Un circuito booleano es un grafo dirigido acíclico de puertas `AND/OR/NOT`; los circuitos cuánticos lo generalizan: las puertas son unitarias sobre 2 o 3 qubits como mucho, y las entradas son los bits de entrada más qubits auxiliares a `|0⟩` [@de-wolf-2026, §2.1.1-2.1.2, pp. 25-27]. Una puerta cuántica tiene tantas salidas como entradas (a diferencia de `AND`) porque las unitarias son reversibles [@de-wolf-2026, §2.1.2, p. 27].

Las puertas actúan sobre pocos qubits porque la física ofrece interacciones locales, igual que los circuitos clásicos usan puertas pequeñas; existe formalmente una unitaria gigante que resuelve 3SAT, pero hay que construirla con piezas pequeñas [@aaronson-2018, Lec16, p. 2]. Preskill lista las hipótesis del modelo: una descomposición preferida en subsistemas, un conjunto finito de puertas (necesario más adelante porque solo puertas discretas se pueden proteger con tolerancia a fallos) y puertas unitarias con medidas ortogonales, porque las medidas generales (POVM) se simulan sobre sistemas ampliados [@preskill-ph219, ch.5 §5.3, p. 23].

También se exige que entradas y salidas sean sencillas. Una entrada producto es barata de preparar; una entrada entrelazada complicada podría esconder la dificultad del algoritmo. Y cualquier medida colectiva se reduce a una unitaria seguida de una medida estándar, que cuesta puertas [@preskill-ph219, ch.5 §5.3, pp. 23-24]. Una medida proyectiva general se implementa con una unitaria `U` seguida de una medida del primer qubit; para conservar el estado tras medir, se aplica además `U⁻¹` [@de-wolf-2026, §2.1.2, p. 27].

En esa línea, una medida a mitad de circuito se puede aplazar al final con un qubit auxiliar y un `CNOT`, de modo que un cálculo es una parte unitaria seguida de una lectura [@watrous-2025, L6.2, PDF pp. 171-172; @de-wolf-2026, §2.1.2, p. 27; ejercicio 2.8, p. 32; @preskill-ph219, ch.5 §5.3, pp. 23-24].

Como todo es unitario, un circuito se puede invertir: se invierte el orden y cada puerta se sustituye por su inversa, y se obtiene el circuito de `U†`, del mismo tamaño [@watrous-2025, L6.3, PDF p. 181; @de-wolf-2026, §2.1.2, p. 27]. `Toffoli`, `CNOT` y `NOT` son sus propias inversas [@watrous-2025, L6.3, PDF p. 181]. El coste se mide con dos números: el *tamaño*, que es el número de puertas, y la *profundidad (depth)*, el mínimo número de capas en las que las puertas de cada capa actúan sobre cables distintos [@watrous-2025, L6.2, PDF pp. 172-173].

La inversión sirve para meter cómputo clásico dentro del cuántico. Los circuitos cuánticos simulan cualquier circuito booleano con `NOT`, `CNOT` y `Toffoli` más espacio auxiliar, y la basura que quede se elimina ejecutando el circuito a la inversa, porque dejarla arruinaría la interferencia que necesitan los algoritmos [@watrous-2025, L6.3, PDF pp. 177-181]. La interferencia es el recurso central: se trata de ordenar las amplitudes para que las respuestas erróneas se cancelen y la correcta se refuerce; sin eso valdría un ordenador clásico aleatorizado [@aaronson-2018, Lec16, p. 3].

### Ejemplo
Un circuito `U` hecho solo de Toffoli lleva `|z⟩|0⟩` a `|z⟩|f(z)⟩`; aplicado a una superposición uniforme da una superposición con `f(z)` para los `2ⁿ` valores de `z` con una sola aplicación, pero medir da un único par aleatorio `(z, f(z))`, así que hacen falta interferencia y entrelazamiento para una ventaja real [@de-wolf-2026, §2.3, pp. 28-29].

### Errores frecuentes
- *"Un circuito cuántico puede tener bucles o bifurcar cables."* No: es acíclico y los cables no se ramifican [@watrous-2025, L3.1, PDF pp. 69-70; @aaronson-2018, Lec4, p. 3].
- *"Medir a mitad del circuito cambia la potencia del modelo."* Se puede aplazar al final con un qubit auxiliar [@watrous-2025, L6.2, PDF pp. 171-172].
- *"La paralelización cuántica da todos los resultados."* Solo se lee uno [@de-wolf-2026, §2.3, pp. 28-29].

### Para seguir
La capa 3 fija el modelo de coste estándar, la precisión que exigen los circuitos largos y cómo limpiar los qubits de trabajo.

## Profesional {#layer-3}

### Idea clave
El modelo de coste estándar es la familia uniforme de circuitos de tamaño polinómico (`BQP`), y la precisión por puerta debe mejorar linealmente con el tamaño del circuito [@de-wolf-2026, §2.1.2, pp. 27-28; @preskill-ph219, ch.5 §5.3.1, p. 29].

### Explicación
`BQP` es la clase de lenguajes decididos con probabilidad de éxito al menos 2/3 por una familia de circuitos cuánticos de tamaño polinómico [@de-wolf-2026, §2.1.2, pp. 27-28]. Contiene a `BPP` (un `H` más una medida produce un bit aleatorio), se cree que es mayor, pero `BPP ≠ BQP` no está probado porque implicaría `BPP ≠ PSPACE`; además `BQP ⊆ PSPACE` (suma sobre `2^{n(T−1)}` caminos, con memoria `≈ nT log T` bits pero tiempo exponencial) [@preskill-ph219, ch.5 §5.3, pp. 24-26; §5.3.2, pp. 29-31]. Más en [complejidad cuántica](../../quantum-algorithms/concepts/quantum-complexity.md).

Ese modelo ideal supone puertas exactas. Si cada puerta real difiere de la ideal como mucho `ε` en norma, tras `T` puertas el error de estado es como mucho `T·ε` (los errores se suman coherentemente en el peor caso) [@preskill-ph219, ch.5 §5.3.1, pp. 26-28]. Para que un circuito ideal con probabilidad de éxito `1/2 + δ` siga siendo útil hace falta `ε < δ/T`: la precisión debe mejorar linealmente con el tamaño del circuito; la tolerancia a fallos pretende dar puertas lógicas con precisión `≈ 1/T` a partir de puertas físicas de precisión constante [@preskill-ph219, ch.5 §5.3.1, p. 29]. Esto motiva todo el ámbito de [corrección de errores](../../error-correction/index.md).

Tampoco todo es alcanzable. La mayoría de las unitarias, y de los estados, de `n` qubits están fuera del alcance de circuitos de tamaño polinómico: para alcanzar todo `U(2ⁿ)` con precisión `δ` hace falta un `T` exponencial (del orden de `2^{2n}·log(C/δ)/log poly(n)`) [@preskill-ph219, ch.5 §5.3.3, pp. 31-33]. Como los circuitos son numerables y las unitarias un continuo, los circuitos finitos solo aproximan unitarias arbitrarias [@preskill-ph219, ch.5 §5.3.3, pp. 31-32]. De ahí que la pregunta de diseño sea siempre qué unitarias se implementan con polinómicas puertas [@aaronson-2018, Lec16, pp. 2-3].

La limpieza de los subcircuitos es parte del diseño. Los qubits de trabajo de un subcircuito deben reponerse a `|0⟩` antes de usarlo sobre una superposición, porque un entrelazamiento residual entre registro de dirección y de trabajo destruye la interferencia buscada [@de-wolf-2026, ejercicio 2.11 y comentario, p. 33]. La receta es guardar la basura, copiar la salida y ejecutar el circuito a la inversa (descomputación); duplica el número de puertas y requiere memoria del orden del número de puertas, y el juego de piedras (*pebble game*) permite intercambiar tiempo por espacio [@preskill-ph219, ch.5 §5.2.3, pp. 20-22].

Tamaño y profundidad son dos medidas distintas del coste de un circuito [@watrous-2025, L6.2, PDF pp. 172-173]; cómo se traduce cada una en errores de un dispositivo concreto se ve en [coherencia y fidelidad](../../quantum-hardware/concepts/coherence-and-fidelity.md). Los circuitos con medidas y puertas con control clásico se programan y optimizan en [circuitos en Qiskit](../../qiskit-programming/concepts/qiskit-circuits.md) y [transpilación](../../qiskit-programming/concepts/transpilation.md).

### Ejemplo
Presupuesto de precisión: para un circuito de `T` puertas cuya respuesta correcta sale con probabilidad `1/2 + δ`, cada puerta debe tener error `ε < δ/T`; duplicar el tamaño del circuito obliga a reducir a la mitad el error por puerta [@preskill-ph219, ch.5 §5.3.1, p. 29].

### Para seguir
[Complejidad cuántica](../../quantum-algorithms/concepts/quantum-complexity.md) sitúa `BQP` entre las demás clases; [corrección de errores](../../error-correction/index.md) explica cómo se consigue la precisión `≈ 1/T`.
