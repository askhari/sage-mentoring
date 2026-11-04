---
concept: multi-qubit-states
title: "Estados de varios qubits"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
Un registro de `n` qubits se describe con un único vector unitario de `2ⁿ` amplitudes, indexado por las cadenas de `n` bits, y no con `n` vectores de dos [@watrous-2025, L2.2, PDF p. 55; L2.1, PDF pp. 32-33].

### Explicación
Los estados clásicos de `n` bits son las cadenas de `n` bits; con 10 bits hay 1024, de `0000000000` a `1111111111` [@watrous-2025, L2.1, PDF pp. 32-33]. El estado cuántico de `n` sistemas es un vector unitario indexado por esas cadenas [@watrous-2025, L2.2, PDF p. 55].

Con dos qubits, los cuatro estados de base son `|00⟩, |01⟩, |10⟩, |11⟩`, productos tensoriales de estados de base de un qubit; un estado general es `a₀₀|00⟩ + a₀₁|01⟩ + a₁₀|10⟩ + a₁₁|11⟩` con `Σ|aᵢⱼ|² = 1` [@de-wolf-2026, §1.3, p. 19]. Como columna, el orden es `00, 01, 10, 11`, con el símbolo de la izquierda más significativo [@watrous-2025, L2.1, PDF p. 35]. Medir los dos qubits da la cadena `ab` con probabilidad `|a_ab|²` [@aaronson-2018, Lec5, p. 2].

La forma más sencilla de juntar dos qubits es el producto tensorial (ver [producto tensorial](../../math-foundations/concepts/tensor-products.md)): `|φ⟩⊗|ψ⟩` tiene amplitudes `⟨ab|π⟩ = ⟨a|φ⟩⟨b|ψ⟩` [@watrous-2025, L2.1, PDF pp. 37-38]. Un producto significa que "los estados no tienen nada que ver entre sí" [@watrous-2025, L2.2, PDF p. 51]; es el análogo de la independencia estadística de variables aleatorias [@de-wolf-2026, §1.3, p. 20].

Pero no todo estado es un producto. `(|00⟩ + |11⟩)/√2` no se puede escribir como `|φ⟩⊗|ψ⟩`: habría que tener a la vez `⟨0|φ⟩⟨1|ψ⟩ = 0` y `⟨0|φ⟩⟨0|ψ⟩ ≠ 0`, y eso es una contradicción [@watrous-2025, L2.2, PDF p. 52]. Los estados que no son producto se llaman **entrelazados** ([entrelazamiento](entanglement.md)). Con tres qubits hay ejemplos famosos, `GHZ` y `W`, que tampoco son productos (véase el ejemplo) [@watrous-2025, L2.2, PDF p. 54].

Si se mide solo un qubit de un estado conjunto, el resultado `a` tiene probabilidad igual a la norma al cuadrado de la parte del vector pegada a `|a⟩`, y el resto se colapsa a esa parte normalizada [@watrous-2025, L2.2, PDF pp. 55-57]. Es una medida proyectiva con proyectores `|0⟩⟨0|⊗I` y `|1⟩⟨1|⊗I` [@de-wolf-2026, §1.3, p. 20]. Con la regla de Aaronson: se descartan las amplitudes incompatibles con el resultado y se renormaliza [@aaronson-2018, Lec5, p. 2].

Una puerta sobre un qubit actúa como la identidad sobre los demás, así que su matriz es un producto tensorial con `I`; por ejemplo, `I⊗H` o `H⊗I` en dos qubits [@watrous-2025, L3.1, PDF p. 75]. "Hadamard sobre el tercer qubit" significa eso mismo [@aaronson-2018, Lec3, p. 1; Lec5, p. 3].

Queda una convención que conviene fijar: Qiskit etiqueta los qubits `(q_{n−1}, …, q_0)`, con `q_0` a la derecha de la cadena y arriba del circuito; Watrous lo describe como una inversión de la convención más común y fuente habitual de confusión [@watrous-2025, L2.1, PDF p. 33; L3.1, PDF p. 74]. En estas páginas escribimos el primer qubit a la izquierda del ket, como en la mayor parte de la literatura; cuando haga falta la convención de Qiskit, se avisa.

### Ejemplo
Productos de estados de base y de superposición:

- `|0⟩⊗|1⟩ = (1,0)ᵀ ⊗ (0,1)ᵀ = (0,1,0,0)ᵀ = |01⟩`.
- `|+⟩⊗|0⟩ = (|00⟩ + |10⟩)/√2`, es decir, el primer qubit en `|+⟩` y el segundo en `|0⟩`.

Medida parcial: en `(1/√3)|0⟩|φ⟩ + √(2/3)|1⟩|ψ⟩`, el resultado `0` tiene probabilidad 1/3 y deja `|0⟩|φ⟩`; el `1` tiene probabilidad 2/3 y deja `|1⟩|ψ⟩` [@de-wolf-2026, §1.3, p. 20].

Tres qubits sin descomposición en productos: `GHZ = (|000⟩+|111⟩)/√2` y `W = (|001⟩+|010⟩+|100⟩)/√3`; ninguno es producto de tres estados de un qubit [@watrous-2025, L2.2, PDF p. 54].

### Para seguir
La capa 2 explica por qué el registro crece de forma exponencial, cómo se transforman los estados y cómo comprobar si un estado de dos qubits es producto. [Entrelazamiento](entanglement.md) estudia los que no lo son.

## Comprensión {#layer-2}

### Idea clave
El recuento de amplitudes crece como `2ⁿ` salvo que el estado sea producto, y las operaciones se combinan con el producto tensorial; no ser producto es justo lo que habilita el entrelazamiento [@de-wolf-2026, §1.3, p. 20; §2.1.2, p. 26].

### Explicación
Una distribución clásica conjunta sobre espacios de tamaño `2ⁿ` y `2^m` necesita `2^{n+m}` números, mientras que una distribución producto solo `2ⁿ + 2^m`; igual para estados cuánticos: un estado general de `n+m` qubits necesita `2^{n+m}` amplitudes frente a `2ⁿ + 2^m` para un producto [@de-wolf-2026, §1.3, p. 20]. Un estado de `n` qubits sin entrelazamiento es un producto de `n` estados de un qubit y necesita solo del orden de `2n` números [@aaronson-2018, Lec16, p. 3].

A pesar de ese parecido en el recuento, los estados cuánticos son mucho más potentes que las distribuciones porque las amplitudes pueden ser negativas o complejas y producir interferencia; solo se convierten en probabilidades al elevarlas al cuadrado [@de-wolf-2026, §1.3, p. 20].

Las operaciones siguen la misma lógica: puertas en paralelo sobre partes distintas del registro se combinan con el producto tensorial; puertas en secuencia, con el producto de matrices ordinario [@de-wolf-2026, §2.1.2, p. 26]. La propiedad que lo justifica es `(A⊗B)(C⊗D) = (AC)⊗(BD)` [@de-wolf-2026, App. A.6, p. 209]. Pero ni todas las operaciones son productos: `SWAP` y `CNOT` no se pueden escribir como producto tensorial de unitarias, y justo por eso ([puertas de dos qubits](two-qubit-gates.md)) pueden crear entrelazamiento [@watrous-2025, L2.2, PDF p. 66].

Para reconocer cuándo un estado sí es producto hay un criterio directo. Con cuatro amplitudes `aᵢⱼ`, un estado de dos qubits es producto exactamente cuando existen `α₀, α₁, β₀, β₁` con `aᵢⱼ = αᵢβⱼ`; en particular, `a₀₀·a₁₁ = a₀₁·a₁₀` (comprobación directa: ambos lados valen `α₀α₁β₀β₁`). Para vectores de estado, "no ser producto" y "estar entrelazado" son lo mismo; para estados mixtos la cosa es más sutil [@watrous-2025, L2.2, PDF p. 52].

### Ejemplo
El criterio falla en `(|00⟩+|11⟩)/√2`: aquí `a₀₀·a₁₁ = 1/2` pero `a₀₁·a₁₀ = 0`, luego no es producto. Un ejemplo que sí lo es, de Watrous: `(|00⟩ + i|01⟩ − |10⟩ − i|11⟩)/2 = ((|0⟩−|1⟩)/√2) ⊗ ((|0⟩+i|1⟩)/√2)` [@watrous-2025, L2.2, PDF pp. 53-54]; allí `a₀₀·a₁₁ = −i/4 = a₀₁·a₁₀`.

### Errores frecuentes
- *"Un registro de `n` qubits son `n` qubits independientes."* Solo si es producto; en general es un vector de `2ⁿ` amplitudes [@de-wolf-2026, §1.3, p. 20].
- *"Más amplitudes significa más información legible."* Al medir se obtiene una cadena de `n` bits; el vector no se lee directamente ([el qubit](qubit.md)).
- *"Los qubits necesitan estar cerca para formar un estado conjunto."* No hay límite de distancia: un qubit en la Tierra y otro en la Luna forman un estado conjunto, y cada parte solo puede medir su qubit local [@aaronson-2018, Lec5, p. 2].

### Para seguir
La capa 3 trata el coste de simular registros grandes y dos reglas prácticas de programación.

## Profesional {#layer-3}

### Idea clave
Un ordenador clásico simula `n` qubits guardando las `2ⁿ` amplitudes, y ese coste exponencial en memoria fija el límite práctico de los simuladores de vector de estado [@aaronson-2018, Lec16, pp. 1-3].

### Explicación
Como basta con guardar y actualizar las `2ⁿ` amplitudes con cada unitaria, los ordenadores cuánticos no resuelven nada incomputable; a lo sumo falsarían la tesis de Church-Turing *extendida* [@aaronson-2018, Lec16, p. 2]. El coste en memoria es la motivación de Feynman (1982): con 300 qubits hay más amplitudes que átomos en el universo observable [@aaronson-2018, Lec16, pp. 1, 3]. Preskill añade que la dificultad de la simulación clásica viene de la enorme dimensión del espacio, y que los estados típicos del espacio nunca se podrán preparar con recursos razonables [@preskill-ph219, ch.5 §5.3, pp. 25-26, 33]. Esto fija el límite práctico de un simulador de vector de estado ([simuladores y vectores de estado](../../qiskit-programming/concepts/simulators-and-statevectors.md)).

La estructura que hace barata la simulación es la ausencia de entrelazamiento: un cómputo cuántico que nunca lo tuviera sería fácil de simular y no daría ventaja; en la práctica todo cálculo interesante lo lleva "de acompañante" [@aaronson-2018, Lec16, p. 3].

Dos reglas prácticas de programación se siguen de lo anterior:

1. *Fija una convención de orden y úsala siempre* (aquí, primer qubit a la izquierda del ket; en Qiskit, `q_0` a la derecha). Un `CNOT` con el control en el segundo qubit tiene una matriz distinta a otra con el control en el primero [@watrous-2025, L2.1, PDF pp. 44-45].
2. *No uses `|φ_Aφ_B⟩` para productos generales:* la abreviación solo es segura si ambos son estados de base [@de-wolf-2026, §1.3, nota 7, p. 20]; omitir `⊗` puede ser ambiguo y peligroso [@de-wolf-2026, App. A.10, p. 210].

Para más de dos qubits, `GHZ` y `W` son los dos ejemplos canónicos de tres [@watrous-2025, L2.2, PDF p. 54]; sus propiedades de entrelazamiento (por ejemplo, la monogamia) se tratan en [entrelazamiento](entanglement.md). El entrelazamiento multipartito (estados GHZ o "cat", y otros) se encuentra como lectura adicional en [@preskill-ph219, ch.4 §4.8, pp. 48-59].

### Ejemplo
El contraste de escala: guardar un estado general de 300 qubits exigiría más amplitudes que átomos en el universo observable, mientras que un estado producto de 300 qubits necesita del orden de `2·300 = 600` números [@aaronson-2018, Lec16, pp. 1, 3].

### Para seguir
[Entrelazamiento](entanglement.md) explica el recurso que hace costosa esa simulación; [puertas de dos qubits](two-qubit-gates.md) muestra cómo se crea.
