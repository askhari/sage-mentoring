---
concept: entanglement
title: "Entrelazamiento"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
Un estado de varios qubits está **entrelazado (entangled)** cuando no se puede escribir como producto tensorial de estados de cada qubit [@de-wolf-2026, §1.3, p. 20]. El ejemplo básico es el par de Bell `(|00⟩ + |11⟩)/√2`, que se fabrica con `H` y `CNOT` [@aaronson-2018, Lec5, p. 4].

### Explicación
Para vectores de estado, "entrelazado" y "no producto" son equivalentes (ver [estados de varios qubits](multi-qubit-states.md)) [@watrous-2025, L2.2, PDF p. 52]. Todo cálculo cuántico interesante lo lleva "de acompañante" [@aaronson-2018, Lec16, p. 3].

El estado `|φ⁺⟩ = (|00⟩ + |11⟩)/√2` se llama par EPR (por Einstein, Podolsky y Rosen). Ningún qubit tiene un valor clásico al principio; pero si se mide el primero y sale `0`, el estado colapsa a `|00⟩` y el segundo queda fijado también [@de-wolf-2026, §1.3, p. 20].

Los **cuatro estados de Bell** son
`|φ⁺⟩ = (|00⟩+|11⟩)/√2`, `|φ⁻⟩ = (|00⟩−|11⟩)/√2`, `|ψ⁺⟩ = (|01⟩+|10⟩)/√2`, `|ψ⁻⟩ = (|01⟩−|10⟩)/√2`.
Todos están entrelazados y forman una base ortonormal de dos qubits [@watrous-2025, L2.2, PDF p. 53; L3.1, PDF p. 76].

Un par de Bell se fabrica partiendo de `|00⟩`, aplicando `H` al primer qubit y luego `CNOT` con el primero como control [@aaronson-2018, Lec5, p. 4; @watrous-2025, L3.1, PDF pp. 74-76].

![Circuito H + CNOT que crea un estado de Bell](../../../../../assets/diagrams/bell-circuit.es.svg)

Las matrices están en [puertas de un qubit](single-qubit-gates.md) y [de dos qubits](two-qubit-gates.md); el circuito completo se ve en [circuitos cuánticos](quantum-circuits.md). Las cuatro entradas de base dan los cuatro estados de Bell: `|00⟩ → |φ⁺⟩`, `|01⟩ → |ψ⁺⟩`, `|10⟩ → |φ⁻⟩`, `|11⟩ → |ψ⁻⟩`; de modo que `H` más `CNOT` convierte la base estándar en la base de Bell [@preskill-ph219, ch.4 §4.1.1, pp. 6-8; @watrous-2025, L3.1, PDF pp. 74-76].

Conviene separar el entrelazamiento de la mera correlación. El estado clásico "con probabilidad 1/2, `00`; con probabilidad 1/2, `11`" (dos bits aleatorios perfectamente correlacionados) *no* está entrelazado. Frases como "medir uno afecta al otro" o "cada uno recuerda al otro" también valen para ese estado clásico, así que no capturan el entrelazamiento [@watrous-2025, L4, PDF pp. 100-101]. Tampoco es correcto pensar que Alice tiene "`|00⟩/√2`" y Bob "`|11⟩/√2`": la intuición buena es una moneda compartida con amplitudes `1/√2` en lugar de probabilidades `1/2` [@de-wolf-2026, §1.5, nota 9, p. 22].

Lo que distingue al entrelazamiento es lo que se puede hacer con él y que ninguna correlación clásica permite [@watrous-2025, L4, PDF p. 101]. Tres ejemplos de este ámbito son la teleportación, la codificación superdensa y el juego CHSH.

### Ejemplo
Traza del circuito de Bell, paso a paso [@aaronson-2018, Lec5, p. 4; @watrous-2025, L3.1, PDF pp. 74-76]:

1. `|00⟩`
2. tras `H` en el primer qubit: `(|0⟩+|1⟩)/√2 ⊗ |0⟩ = (|00⟩ + |10⟩)/√2`
3. tras `CNOT` (invierte el segundo qubit cuando el primero es `1`): `(|00⟩ + |11⟩)/√2 = |φ⁺⟩`

### Errores frecuentes
- *"Entrelazado equivale a correlacionado."* El par clásico `½|00⟩ + ½|11⟩` está correlacionado y no entrelazado [@watrous-2025, L4, PDF pp. 100-101].
- *"Alice tiene `|00⟩/√2` y Bob `|11⟩/√2`."* Lo correcto es una moneda compartida con amplitudes en lugar de probabilidades [@de-wolf-2026, §1.5, nota 9, p. 22].

### Para seguir
La capa 2 explica qué ocurre con cada qubit por separado y qué no puede hacer el entrelazamiento. Después, [teleportación](quantum-teleportation.md), [codificación superdensa](superdense-coding.md) y el [juego CHSH](bell-inequalities.md) muestran para qué sirve.

## Comprensión {#layer-2}

### Idea clave
En un par de Bell cada qubit por separado es completamente aleatorio y la información está en las correlaciones; crear o eliminar entrelazamiento exige una puerta de dos qubits, y el entrelazamiento no permite enviar señales [@watrous-2025, L9.4, PDF p. 286; @preskill-ph219, ch.4 §4.1.1, pp. 4-8].

### Explicación
Watrous reconoce que entrelazamiento se define como correlación cuántica no clásica, esencialmente por lo que *no* es, y que es difícil de explicar con intuición [@watrous-2025, L4, PDF p. 100]. La forma operativa de la definición es la de la capa anterior (no producto); la forma conceptual es la lista de tareas que permite.

En el par de Bell, el estado de un solo qubit es el completamente mezclado `I/2` [@watrous-2025, L9.4, PDF p. 286]: cualquier medida local, según cualquier eje, da un bit aleatorio, y no revela cuál de los estados de Bell se preparó [@preskill-ph219, ch.4 §4.1.1, p. 4]. Es lo que llamamos entrelazamiento máximo. La información está en las correlaciones, no en las partes (véase [matrices densidad](../../quantum-mechanics/concepts/density-matrices.md)).

Esas correlaciones son dos bits: uno de *paridad* (`φ` frente a `ψ`) y uno de *fase* (`+` frente a `−`), que ninguna de las dos partes puede leer localmente. Las mediciones locales en `z` revelan la paridad pero alteran la fase, y las locales en `x` hacen lo contrario; para leer los dos hace falta una operación conjunta [@preskill-ph219, ch.4 §4.1.1, pp. 5-6]. Esto es la base de [teleportación](quantum-teleportation.md) y [codificación superdensa](superdense-coding.md).

Las unitarias locales sobre una parte pueden convertir un estado maximalmente entrelazado en otro cualquiera, sin cambiar `ρ_A = ρ_B = I/2` [@preskill-ph219, ch.4 §4.1.1, pp. 5-6]. Alice puede pasar de `|φ⁺⟩` a `(|00⟩−|11⟩)/√2` aplicando solo `Z` a su qubit [@de-wolf-2026, §17.2, p. 159]. También, aplicar `U` a la mitad de Alice de un par EPR equivale a aplicar `Uᵀ` a la mitad de Bob [@de-wolf-2026, ejercicios 17.1 y 17.3, p. 163].

Lo que no se puede con operaciones locales es crear entrelazamiento. Con operaciones locales y comunicación clásica ninguna secuencia de pasos puede subir el número de Schmidt de un estado puro por encima de 1, así que un estado separable sigue siéndolo [@preskill-ph219, ch.4 §4.6, p. 42]. Hace falta una puerta de dos qubits como `CNOT` ([puertas de dos qubits](two-qubit-gates.md)), que es la parte "no local" que crea o elimina entrelazamiento [@preskill-ph219, ch.4 §4.1.1, pp. 6-8]. Los qubits no tienen por qué interaccionar directamente: un qubit intermedio o la teleportación bastan [@aaronson-2018, Lec10, p. 4].

Tampoco permite señalar más rápido que la luz: medir una mitad de un par EPR no cambia lo que ve Bob [@de-wolf-2026, §1.1, p. 13; §17.1, p. 157]. Si Alice mide en otra base (con Hadamard antes), el qubit de Bob queda en otro par de estados, lo que parece una señal instantánea; la salida es que las estadísticas de Bob son las mismas, lo que lleva al teorema de no comunicación [@aaronson-2018, Lec5, pp. 4-5; Lec14, p. 2].

Por último, el entrelazamiento es monógamo. Si el qubit de Alice está maximalmente entrelazado con el de Bob, no puede estarlo también con el de Charlie; en el estado `W`, ningún par está maximalmente entrelazado, aunque hay algo de entrelazamiento entre A-B y A-C [@aaronson-2018, Lec10, p. 5]. En el estado `GHZ`, a diferencia de tres bits clásicos correlacionados, el entrelazamiento solo es visible con los tres qubits [@aaronson-2018, Lec10, pp. 4-5].

### Ejemplo
`|φ⁺⟩` y `|φ⁻⟩` solo se distinguen por el signo de `|11⟩`. Medir los dos qubits en `z` da `00` o `11` con probabilidad 1/2 en ambos casos, así que las medidas locales en `z` leen la paridad (`φ`) pero no la fase (`+` o `−`); para leer las dos hace falta una operación conjunta [@preskill-ph219, ch.4 §4.1.1, pp. 5-6].

### Errores frecuentes
- *"Dos partículas entrelazadas se mandan mensajes."* No hay señal: las estadísticas de Bob no cambian [@de-wolf-2026, §1.1, p. 13; §17.1, p. 157].
- *"Si los estados individuales están definidos, el conjunto es producto."* En un estado entrelazado las partes no tienen estado puro propio (`I/2` en el par de Bell) [@watrous-2025, L9.4, PDF p. 286].

### Para seguir
La capa 3 trata el entrelazamiento como recurso contable, su papel al programar y cómo se comprueba en el laboratorio.

## Profesional {#layer-3}

### Idea clave
El entrelazamiento se cuenta como recurso (en *e-bits*) y se verifica en el laboratorio violando desigualdades de Bell; entrelazar qubits lejanos es caro, no instantáneo [@watrous-2025, L4, PDF p. 101; @hensen-2015, pp. 3-5].

### Explicación
En teoría de la información cuántica se mide en *e-bits*: `|φ⁺⟩` cuenta como un e-bit aunque use dos qubits. "Compartir un e-bit" es que Alice tiene `A`, Bob tiene `B` y `(A,B)` está en `|φ⁺⟩`. El análogo clásico es un bit de aleatoriedad compartida (útil, por ejemplo, en criptografía, pero no entrelazada) [@watrous-2025, L4, PDF p. 101]. Las tareas se resumen como desigualdades de recursos: `1 e-bit + 2 bits clásicos ≥ 1 qubit` (teleportación) y `1 e-bit + 1 qubit ≥ 2 bits clásicos` (codificación superdensa) [@preskill-ph219, ch.4 §4.4.2, p. 32].

Para estados puros de dos partes, estar entrelazado equivale a violar alguna desigualdad de Bell; para estados mixtos la relación es más sutil [@preskill-ph219, ch.4 §4.3.4, p. 24]. Un estado mixto es separable si y solo si es una mezcla convexa de productos (correlaciones puramente clásicas); además, un mismo estado separable puede tener una descomposición en estados puros entrelazados, como `I⊗I/4` [@preskill-ph219, ch.4 §4.6, pp. 41-42].

Al programar, el entrelazamiento va "de acompañante" en un cálculo cuántico; sin él, el vector de estado es un producto de `n` estados de un qubit y se simula con del orden de `2n` números (ver [estados de varios qubits](multi-qubit-states.md)) [@aaronson-2018, Lec16, p. 3]. Además, la gestión de qubits auxiliares es un problema de entrelazamiento: si un subcircuito deja entrelazado el registro de trabajo con el de datos, la interferencia prevista se destruye, y por eso los qubits auxiliares deben reponerse a `|0⟩` ([circuitos cuánticos](quantum-circuits.md)) [@de-wolf-2026, ejercicio 2.11, p. 33].

Al razonar sobre un protocolo conviene preguntar *quién* tiene cada mitad y *qué* operaciones son locales; casi todos los argumentos (teleportación, superdensa, CHSH) son de ese tipo. Y al cambiar de base de Bell basta con una Pauli local (`I, X, Y, Z`), no con tocar las dos mitades [@preskill-ph219, ch.4 §4.4.1, pp. 28-29].

### Ejemplo
El primer experimento sin lagunas lo hicieron Hensen y colaboradores en 2015 con espines de electrones en centros NV separados 1280 m, usando un esquema de entrelazamiento heraldado; se obtuvieron unos pocos eventos por hora porque la probabilidad de éxito por intento era de unos `6,4×10⁻⁹` [@hensen-2015, pp. 3-5]. Entrelazar qubits lejanos es un recurso caro, no un gesto instantáneo; detalle en [desigualdades de Bell](bell-inequalities.md). Otra cifra de escala: se ha demostrado entrelazamiento a unas 150 millas y, con satélites chinos, a un par de miles de millas [@aaronson-2018, Lec5, p. 4].

### Para seguir
[Desigualdades de Bell y juego CHSH](bell-inequalities.md) explica qué se comprueba exactamente en esos experimentos; [teleportación](quantum-teleportation.md) y [codificación superdensa](superdense-coding.md) usan el e-bit como recurso.
