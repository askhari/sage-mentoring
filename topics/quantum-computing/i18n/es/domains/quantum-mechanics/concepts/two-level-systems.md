---
concept: two-level-systems
title: "Sistemas de dos niveles (espín 1/2)"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
Un **sistema de dos niveles (two-level system)** es el sistema cuántico no trivial más pequeño: su espacio de estados tiene dos dimensiones. Hay "más de una forma de mirarlo", porque se puede medir en distintas bases, y el espín 1/2 y la polarización del fotón son sus ejemplos físicos principales [@preskill-ph219, ch.2 §2.2, p. 8].

### Explicación
El experimento que lo muestra es el de Stern-Gerlach. En 1922, Stern y Gerlach enviaron átomos de plata por un campo magnético no homogéneo y vieron momentos magnéticos cuantizados con dos valores; el momento del átomo de plata es el de su único electrón exterior [@zwiebach-mit-8-05, ch.2 §1, pp. 1, 3]. Un momento magnético en un gradiente de campo siente una fuerza proporcional a `μ_z`. Clásicamente se esperaría una mancha continua; en cambio aparecen dos picos separados, así que `S_z` solo toma los valores `±ħ/2`, y eso define el **espín 1/2 (spin one-half)** [@zwiebach-mit-8-05, ch.2 §1, pp. 4-5]. El espín intrínseco del electrón no es una bola de carga que gira: el electrón se trata como puntual [@zwiebach-mit-8-05, ch.2 §1, pp. 2-3].

Encadenando tres cajas se ve que los valores de `S_z` y `S_x` no coexisten (los tres experimentos están en [@zwiebach-mit-8-05, ch.2 §1, pp. 5-7]):

1. Dos máquinas `z` en serie, bloqueando `S_z = −ħ/2` tras la primera: todos salen de la segunda con `S_z = +ħ/2`.
2. Un haz `S_z = +ħ/2` entra en una máquina `x`: se divide más o menos mitad y mitad.
3. Se bloquea `S_x = +ħ/2` y el haz `S_x = −ħ/2` entra en otra máquina `z`: salen mitad con `+ħ/2` y mitad con `−ħ/2`. El filtro `S_z` anterior no deja memoria: una partícula no tiene a la vez valores de `S_x` y `S_z`.

![Secuencia de Stern-Gerlach z, x, z](../../../../../assets/diagrams/stern-gerlach-zxz.es.svg)

El modelo matemático es un espacio vectorial complejo de dimensión 2 con base ortonormal `|z;+⟩ = (1,0)ᵀ` y `|z;−⟩ = (0,1)ᵀ` [@zwiebach-mit-8-05, ch.2 §2, pp. 7-8]. Los estados `x` son superposiciones: `|x;±⟩ = (|z;+⟩ ± |z;−⟩)/√2` y `|y;±⟩ = (|z;+⟩ ± i|z;−⟩)/√2`; sin números complejos no habría estados `y` [@zwiebach-mit-8-05, ch.2 §2, pp. 11-12]. Un estado `|z;+⟩` da 50/50 en `x`, y una superposición de `|x;+⟩` y `|x;−⟩` bien elegida vuelve a dar `|z;+⟩` con certeza; un bit probabilístico clásico no se comporta así [@preskill-ph219, ch.2 §2.2.1, p. 14].

La otra realización es la polarización del fotón. Un fotón polarizado a un ángulo `α` es `cosα|x⟩ + sinα|y⟩`, y un polarizador según `x` da `|x⟩` con probabilidad `cos²α` [@zwiebach-mit-8-04, LN1 §3, pp. 7-8]. Un estado general es `α|x⟩ + β|y⟩`, con solo el cociente `β/α` físico [@zwiebach-mit-8-04, LN1 §4, pp. 10-11].

Un qubit es exactamente un sistema de dos niveles: el espín del electrón y la polarización del fotón son dos realizaciones físicas [@preskill-ph219, ch.2 §2.2, p. 8; §2.2.2, pp. 14-15]. El cálculo con un qubit es el álgebra de estas matrices 2×2; se estudia como abstracción en [el qubit](../../qubits-and-circuits/concepts/qubit.md) y en [la esfera de Bloch](../../qubits-and-circuits/concepts/bloch-sphere.md). Cómo se construyen qubits reales (superconductores, iones, fotones…) se ve en el ámbito de hardware.

### Ejemplo
Un átomo de plata sale de una máquina `z` con `S_z = +ħ/2`. En la base del modelo, su estado es `(1,0)ᵀ`; como `|x;±⟩ = (|z;+⟩ ± |z;−⟩)/√2`, una máquina `x` lo reparte 50/50 [@zwiebach-mit-8-05, ch.2 §1-2, pp. 5-8, 11-12]. Es el segundo experimento visto como un cálculo con vectores de dos componentes.

### Errores frecuentes
- *"El espín es la rotación del electrón sobre sí mismo."* No: el electrón se trata como puntual [@zwiebach-mit-8-05, ch.2 §1, pp. 2-3].

### Para seguir
La capa 2 introduce las matrices de Pauli y el espín en cualquier dirección. Con el estado de dos niveles ya puedes pasar a [el qubit](../../qubits-and-circuits/concepts/qubit.md).

## Comprensión {#layer-2}

### Idea clave
Las matrices de Pauli, junto con la identidad, forman una base de todas las matrices 2×2 hermíticas y describen el espín en cualquier dirección. Toda unitaria 2×2 de determinante 1 es una rotación de espín, y de ahí cada puerta de un qubit [@zwiebach-mit-8-05, ch.2 §2, pp. 10-11; @preskill-ph219, ch.2 §2.2.1, pp. 11-12].

### Explicación
Las matrices de Pauli son `σ₁ = [[0,1],[1,0]]`, `σ₂ = [[0,−i],[i,0]]`, `σ₃ = [[1,0],[0,−1]]`, con `Sᵢ = (ħ/2)σᵢ`; junto con la identidad forman una base real de todas las matrices 2×2 hermíticas [@zwiebach-mit-8-05, ch.2 §2, pp. 10-11]. Cada una se eleva al cuadrado a la identidad, tiene traza cero y las distintas anticonmutan: `{σᵢ,σⱼ} = 2δᵢⱼ·1` y `σᵢσⱼ = δᵢⱼ·1 + iε_ijk σₖ` [@zwiebach-mit-8-05, ch.2 §3, pp. 13-14]. En forma vectorial, `(a·σ)(b·σ) = (a·b)1 + i(a×b)·σ`, de donde `(n·σ)² = 1` para un vector unitario `n` [@zwiebach-mit-8-05, ch.2 §3, p. 15]. Son [observables](observables.md) con valores propios `±1` [@zwiebach-mit-8-05, ch.2 §3, p. 13].

Para `n = (sinθ cosφ, sinθ sinφ, cosθ)`, el espín en la dirección `n` es `S_n = n·S = (ħ/2)[[cosθ, sinθ e^{−iφ}],[sinθ e^{iφ}, −cosθ]]`, con estados propios `|n;+⟩ = cos(θ/2)|+⟩ + sin(θ/2)e^{iφ}|−⟩` y `|n;−⟩ = −sin(θ/2)e^{−iφ}|+⟩ + cos(θ/2)|−⟩`, ortonormales [@zwiebach-mit-8-05, ch.2 §4, pp. 16-18]. Después de normalizar y descartar la fase global, el estado de espín tiene dos parámetros reales, que son los ángulos polar `θ` y azimutal `φ` [@preskill-ph219, ch.2 §2.2.1, pp. 8-9]. Esto es el origen de la esfera de Bloch (ver [matrices densidad](density-matrices.md) para el caso mixto).

Los operadores de espín cumplen `[S_x,S_y] = iħS_z` y cíclicas, la misma álgebra que el momento angular orbital [@zwiebach-mit-8-05, ch.2 §2, p. 9]; con las matrices `(ħ/2)σ_i` se comprueba explícitamente [@zwiebach-mit-8-05, ch.2 §2, p. 11, ec. 2.27]. Los estados `|n;±⟩` cumplen `S_n|n;±⟩ = ±(ħ/2)|n;±⟩` [@zwiebach-mit-8-05, ch.2 §4, pp. 16-17]. Ver [incertidumbre y no conmutatividad](uncertainty-and-noncommutativity.md).

Los generadores de rotación del espín 1/2 son `J_k = σ_k/2`; una rotación `θ` alrededor de `n` es `U = cos(θ/2)I − i sin(θ/2)n·σ`, y toda unitaria 2×2 de determinante 1 tiene esa forma [@preskill-ph219, ch.2 §2.2.1, pp. 11-12]. Eso conecta con la [evolución unitaria](unitary-time-evolution.md): cualquier puerta de un qubit es una rotación de espín salvo fase global.

El mismo modelo aparece en otras realizaciones. En el Mach-Zehnder, los estados de camino `(1,0)` y `(0,1)` forman un vector de dos componentes y los divisores de haz y desfasadores actúan como matrices 2×2 [@zwiebach-mit-8-04, LN2 §1, pp. 1-4]; véase [principio de superposición](superposition-principle.md).

### Ejemplo
Con polarizadores: un analizador `x` seguido de uno `y` no deja pasar nada; si se inserta entre ambos un analizador a 45°, pasa aproximadamente 1/8 de los fotones. Esto descarta que cada fotón lleve un bit clásico de polarización [@preskill-ph219, ch.2 §2.2.2, p. 16].

### Errores frecuentes
- *"Cualquier sistema de dos niveles es un espín."* La equivalencia formal vale, pero no todo sistema de dos niveles se transforma como un espinor bajo rotaciones espaciales; el fotón, con espín 1 y sin masa, no es un espinor [@preskill-ph219, ch.2 §2.2.1, p. 14; §2.2.2, pp. 14-15].
- *"Las rotaciones de `2π` no hacen nada."* Dan `−I`, que es global pero observable con un control [@preskill-ph219, ch.2 §2.2.1, p. 12].

### Para seguir
La capa 3 aplica el modelo a qubits físicos y recoge sus límites como modelo de dos niveles.

## Profesional {#layer-3}

### Idea clave
Cualquier qubit físico es un modelo de dos niveles: lo único que cambia es qué observable juega el papel de `σ₃` y qué interacción juega el de `H`. Que solo dos estados importen es una hipótesis que hay que justificar para cada plataforma [@preskill-ph219, ch.2 §2.2.2, p. 16; @krantz-2019, pp. 4-5].

### Explicación
Un dispositivo que activa un hamiltoniano con la forma adecuada rota el estado en el eje que se necesite [@preskill-ph219, ch.2 §2.2.2, p. 16]. El momento magnético del electrón es `μ = −gμ_B S/ħ` con `g = 2` [@zwiebach-mit-8-05, ch.2 §1, pp. 2-3]; un campo magnético hace girar (precesar) el espín alrededor de la dirección del campo (precesión de Larmor) [unverified]. Para el diseño real de qubits, véase el ámbito de hardware ([qubits de espín](../../quantum-hardware/concepts/spin-qubits.md), [qubits de iones atrapados](../../quantum-hardware/concepts/trapped-ion-qubits.md)).

Aplicar el modelo de dos niveles supone que solo dos estados importan, pero los sistemas reales tienen más; el ejemplo siguiente muestra un caso.

Para determinar el estado a partir de muchas copias se necesitan tres ejes, porque medir solo en `z` da `|a|` y `|b|` pero no la fase relativa [@preskill-ph219, ch.2 §2.2.1, p. 13]; en la matriz densidad `ρ(P) = (I + P·σ)/2` esto equivale a medir las tres componentes de `P`, con `⟨n·σ⟩ = n·P` [@preskill-ph219, ch.2 §2.3.2, pp. 21-22]. Con dos espines 1/2, los estados producto `|↑⟩⊗|↓⟩` se combinan por superposición en estados entrelazados [@zwiebach-mit-8-04, LN1 §5, pp. 13-14]; se trata en [entrelazamiento](../../qubits-and-circuits/concepts/entanglement.md).

### Ejemplo
En un oscilador armónico los niveles están equiespaciados y no se puede aislar un par. Los qubits superconductores necesitan anarmonicidad para distinguir la transición 0→1 de la 1→2 [@krantz-2019, pp. 4-5]; solo así se pueden tratar los niveles 0 y 1 como un sistema de dos niveles.

### Las fuentes discrepan
Ninguna fórmula única para `|n;±⟩` evita una ambigüedad de fase en toda la esfera, de modo que la elección es convención [@zwiebach-mit-8-05, ch.2 §4, nota 3, p. 18]. Es útil recordarlo al comparar conversiones entre bases en código.

### Para seguir
Sigue con [el qubit](../../qubits-and-circuits/concepts/qubit.md) en el ámbito siguiente, que convierte el sistema de dos niveles en la unidad básica de información cuántica.
