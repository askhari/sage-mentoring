---
concept: superposition-principle
title: "Principio de superposición"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
Si un sistema cuántico puede estar en el estado A y en el estado B, también puede estar en una combinación de ambos, con coeficientes complejos llamados amplitudes. Una **superposición (superposition)** da A o B al medir, nunca un valor intermedio, y los coeficientes fijan las probabilidades [@zwiebach-mit-8-04, LN1 §4, p. 10].

### Explicación
La superposición viene de la linealidad. En una ecuación lineal, si `u₁` y `u₂` son soluciones, `αu₁ + βu₂` también lo es. La teoría de Maxwell es lineal (muchas ondas electromagnéticas coexisten sin molestarse), mientras que la mecánica de Newton y la relatividad general no lo son [@zwiebach-mit-8-04, LN1 §1, pp. 1-3]. La ecuación de Schrödinger es lineal, así que `αΨ₁ + βΨ₂` es solución para `α, β` complejos [@zwiebach-mit-8-04, LN1 §1, pp. 3-4].

Al medir, si un estado "A" siempre da el valor `a` y un estado "B" siempre da `b`, una superposición de ambos da `a` o `b`. Multiplicar el estado por un número complejo no nulo no cambia la física [@zwiebach-mit-8-04, LN1 §4, p. 10].

Una analogía ayuda con la parte de la suma, aunque no con el fenómeno: dos ondas en un estanque se suman, y donde coinciden las crestas el agua sube y donde una cresta cae sobre un valle se anulan. La diferencia esencial es que en lo cuántico lo que se suma son amplitudes complejas, y la probabilidad sale del cuadrado de su módulo.

El experimento que lo muestra es el interferómetro de Mach-Zehnder. Un fotón individual interfiere consigo mismo. La explicación alternativa, interferencia entre dos fotones, implicaría "dos fotones que dan ninguno", y la conservación de la energía lo prohíbe. Por eso el fotón está en una superposición de "rama superior" y "rama inferior" [@zwiebach-mit-8-04, LN1 §4, p. 9].

![Interferómetro de Mach-Zehnder con las amplitudes en cada tramo](../../../../../assets/diagrams/mach-zehnder-amplitudes.es.svg)

La superposición y la interferencia son los ingredientes de los algoritmos cuánticos: preparar muchas posibilidades a la vez y hacer que las amplitudes se refuercen o se anulen para que la respuesta buscada sea la probable [@aaronson-2018, Lec16, p. 3; Lec18, pp. 1-2]. Los detalles están en el ámbito de algoritmos. Aquí se aprende el fenómeno físico; la forma matemática del estado está en [el estado cuántico como vector](state-vector-postulate.md) y la versión para un qubit en [el qubit](../../qubits-and-circuits/concepts/qubit.md).

### Ejemplo
Un átomo con `S_z` definido, `|z;+⟩`, es una superposición de los dos estados de `S_x`: `|z;+⟩ = (|x;+⟩ + |x;−⟩)/√2`. Por eso, al medir `S_x`, salen los dos valores con amplitud `1/√2` cada uno [@zwiebach-mit-8-05, ch.2 §1-2, pp. 5-6, 12]. El mismo estado es "definido" en un eje y superposición en el otro.

### Errores frecuentes
- *"Una superposición es un sistema que está en A o en B y no sabemos cuál."* Eso es una mezcla; la superposición tiene interferencia (se ve en la capa 2).
- *"Un qubit contiene todos los valores a la vez y los lee todos."* Al medir se obtiene `a` o `b`, nunca un intermedio [@zwiebach-mit-8-04, LN1 §4, p. 10]. La [regla de Born](born-rule-measurement.md) da las probabilidades.

### Para seguir
[El estado cuántico como vector](state-vector-postulate.md) da la forma matemática de una superposición. La capa 2 de este concepto resuelve el interferómetro como álgebra lineal.

## Comprensión {#layer-2}

### Idea clave
La interferencia sale de sumar amplitudes antes de elevar al cuadrado, y un solo interferómetro basta para verlo como álgebra lineal con matrices 2×2. La superposición no es una mezcla estadística: se distingue porque la fase relativa es medible [@zwiebach-mit-8-04, LN2 §1, pp. 1-6; LN1 §4, p. 12].

### Explicación
En el Mach-Zehnder, el estado es un vector de dos amplitudes `(α, β)` para el haz superior e inferior, con `|α|² + |β|² = 1`. Un desfasador multiplica una amplitud por `e^{iδ}`, y un divisor de haz equilibrado es una matriz 2×2 de la forma `(1/√2)[[1,1],[1,-1]]` (salvo convención de signos); la linealidad fija su acción sobre cualquier superposición [@zwiebach-mit-8-04, LN2 §1, pp. 1-4]. Esa matriz es la de la puerta de Hadamard, `H = (1/√2)[[1,1],[1,-1]]` [@watrous-2025, L1.2, PDF pp. 25-26]; ver [puertas de un qubit](../../qubits-and-circuits/concepts/single-qubit-gates.md).

Con dos divisores de haz seguidos hay interferencia constructiva y destructiva. Un fotón de entrada llega entero al detector D0 con probabilidad 1 y a D1 con probabilidad 0, por interferencia destructiva en el segundo divisor [@zwiebach-mit-8-04, LN2 §1, pp. 4-6]. Sumar las probabilidades de cada camino como si fuera una mezcla clásica no da este resultado; hay que sumar amplitudes antes de elevar al cuadrado.

Lo que distingue una superposición de una mezcla es la fase relativa. Una superposición igual de espín arriba y abajo en `z` da las mismas estadísticas en `z` que una mezcla 50/50, pero al medir en `x` la superposición da siempre "arriba" y la mezcla da 50/50 [@zwiebach-mit-8-04, LN1 §4, p. 12]. Más detalle en [sistemas de dos niveles](two-level-systems.md); la formalización de la mezcla está en [matrices densidad](density-matrices.md).

El signo relativo importa: `|x;−⟩` se diferencia de `|x;+⟩` en un signo, y eso es justo lo que lo hace ortogonal a `|x;+⟩` [@zwiebach-mit-8-05, ch.2 §2, p. 12]. Recuerda de [números complejos](../../math-foundations/concepts/complex-numbers.md) que una fase global no cuenta, pero la relativa sí.

Un solo átomo puede estar "en ambos haces" con amplitudes distintas; solo el acto de medir (la pantalla detectora) lo obliga a estar en uno [@zwiebach-mit-8-05, ch.2 §1, nota 1, p. 5].

### Ejemplo
Si en el Mach-Zehnder se bloquea una rama, el fotón llega a D1 con probabilidad 1/4 (1/2 queda absorbido por el bloqueo y 1/4 acaba en D0): quitar un camino aumenta la probabilidad de un detector, que antes era 0 [@zwiebach-mit-8-04, LN2 §1, pp. 4-6].

### Errores frecuentes
- *"Es una combinación de probabilidades."* OpenStax compara con una combinación de 0 y 1 con probabilidades `p` y `q = 1 − p`, pero la propia nota advierte que esa comparación es informal [@openstax-physics-3, §7.1]. Los coeficientes son amplitudes, no probabilidades.

### Para seguir
La capa 3 usa estos dos hechos como recurso de cálculo y los conecta con los algoritmos y el entrelazamiento.

## Profesional {#layer-3}

### Idea clave
Dos hechos del interferómetro se usan después de forma abstracta: cambiar una fase relativa cambia las probabilidades de salida, y las amplitudes de caminos distintos se suman antes de elevar al cuadrado [@zwiebach-mit-8-04, LN2 §1, pp. 1-6].

### Explicación
El resto de ámbitos construye sobre ellos: [fase y retroceso de fase](../../quantum-algorithms/concepts/phase-kickback.md), [transformada de Fourier cuántica](../../quantum-algorithms/concepts/quantum-fourier-transform.md), [búsqueda de Grover](../../quantum-algorithms/concepts/grover-search.md).

Un estado de dos partículas es entrelazado si no puede escribirse como producto `(estado de 1) ⊗ (estado de 2)`; `|↑⟩⊗|↓⟩ + |↓⟩⊗|↑⟩` da espines `z` perfectamente anticorrelacionados. Bell (1964) mostró que las correlaciones en varias direcciones no las reproduce ningún conjunto clásico, y el entrelazamiento no permite señales más rápidas que la luz [@zwiebach-mit-8-04, LN1 §5, pp. 12-14]. El tratamiento formal está en [producto tensorial](../../math-foundations/concepts/tensor-products.md) y [entrelazamiento](../../qubits-and-circuits/concepts/entanglement.md).

Para decidir el modelo: si el sistema tiene fase relativa accesible (se puede interferir), se usan vectores de estado; si solo hay ignorancia clásica o entrelazamiento con algo inaccesible, [matrices densidad](density-matrices.md). Una consecuencia de la linealidad, que no se puede copiar un estado desconocido, se trata en [no clonación](../../qubits-and-circuits/concepts/no-cloning.md).

### Ejemplo
La bomba de Elitzur-Vaidman pone en una rama un detector de fotones como disparador. Con una bomba defectuosa todos los fotones acaban en D0; con una funcional, explota con probabilidad 1/2, da D0 con 1/4 y D1 con 1/4. Un clic en D1 certifica que la bomba funciona sin que el fotón la "haya tocado" [@zwiebach-mit-8-04, LN2 §2, pp. 6-7]. Para quien programa, la lección es que la mera presencia de una posibilidad (rama bloqueable) altera el resultado en otra rama.

### Las fuentes discrepan
Zwiebach argumenta que, en cuanto a linealidad, la mecánica cuántica es "más simple" que la clásica: una ecuación lineal con solución para cualquier combinación [@zwiebach-mit-8-04, LN1 §1, p. 3-4; LN5 §2, p. 7]. Preskill, en cambio, ve en esa misma linealidad algo que "parece pedir una explicación" [@preskill-ph219, ch.2 §2.1, p. 7]. No hay una resolución en las fuentes; para programar basta usar la linealidad.

### Para seguir
El siguiente concepto del ámbito es [el estado cuántico como vector](state-vector-postulate.md), y después [medida y regla de Born](born-rule-measurement.md), que dan la forma matemática y las probabilidades de lo visto aquí.
