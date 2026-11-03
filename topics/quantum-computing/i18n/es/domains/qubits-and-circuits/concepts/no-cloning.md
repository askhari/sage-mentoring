---
concept: no-cloning
title: "Teorema de no clonación"
---

## Comprensión {#layer-2}

**Enunciado.** No existe ninguna unitaria `U` ni estado fijo `|φ⟩` tales que `U(|ψ⟩|φ⟩) = |ψ⟩|ψ⟩` para todo estado cuántico `|ψ⟩` [@watrous-2025, L3.3, PDF pp. 93-94]. De Wolf lo plantea para un qubit: no hay una unitaria de dos qubits que lleve `|φ⟩|0⟩` a `|φ⟩|φ⟩` para todo `|φ⟩` [@de-wolf-2026, §1.5, p. 23; ejercicio 1.12, p. 24]. Aaronson lo llama fácil de demostrar pero fundamental [@aaronson-2018, Lec7, p. 3].

**Qué dice y qué no.**

- Habla de un estado *dado y desconocido*. Si se sabe cómo se preparó, basta repetir el procedimiento [@aaronson-2018, Lec7, p. 3].
- Es un resultado de copia *perfecta*. No dice nada contra la copia aproximada con precisión limitada, que existe y tiene sus propias cotas [@watrous-2025, L3.3, PDF p. 94].
- Los estados de una base ortonormal conocida *sí* se pueden copiar. Con `CNOT` y el objetivo en `|0⟩`, `|a⟩|0⟩ → |a⟩|a⟩` para `a = 0, 1`, pero el mismo circuito falla con `|+⟩` [@watrous-2025, L3.3, PDF pp. 94-95].

**Demostración 1: la linealidad.** Si `U` clonara `|0⟩` y `|1⟩` (`U|0⟩|φ⟩ = |00⟩`, `U|1⟩|φ⟩ = |11⟩`), por linealidad llevaría `|+⟩ = (|0⟩+|1⟩)/√2` a `(|00⟩+|11⟩)/√2`. Pero un clon verdadero de `|+⟩` sería `|+⟩|+⟩ = (|00⟩+|01⟩+|10⟩+|11⟩)/2`, otro vector [@watrous-2025, L3.3, PDF p. 94]. Dicho de otra manera: clonar es cuadrático en las amplitudes, no lineal, así que no puede ser unitario [@aaronson-2018, Lec7, p. 3]. Es justo el resultado de aplicar `CNOT` a `|+⟩|0⟩`: un [par de Bell](entanglement.md), no dos copias independientes [@aaronson-2018, Lec7, p. 4; @preskill-ph219, ch.4 §4.5.2, pp. 40-41].

**Demostración 2: los productos interiores.** Las unitarias conservan los productos interiores, pero clonar *eleva al cuadrado* el producto interior: si `|ψ⟩|0⟩ → |ψ⟩|ψ⟩` y `|φ⟩|0⟩ → |φ⟩|φ⟩`, entonces `⟨ψ|φ⟩ = ⟨ψ|φ⟩²`, que solo se cumple si el producto interior es 0 o 1. Por eso solo se pueden clonar estados de una única base ortonormal [@aaronson-2018, Lec7, p. 4]. Preskill lo demuestra con el caso más general (con una ancilla extra `F` y estados de entorno `|e⟩, |f⟩`): la unitariedad da `⟨ψ|φ⟩ = ⟨ψ|φ⟩²⟨e|f⟩`, de modo que `|⟨ψ|φ⟩| = 1` siempre que `⟨ψ|φ⟩ ≠ 0`; ninguna máquina unitaria copia dos estados no ortogonales distintos [@preskill-ph219, ch.4 §4.5.2, p. 41]. La prueba solo usa la unitariedad, y cubre cualquier espacio de Hilbert mayor con ancillas [@preskill-ph219, ch.4 §4.5.2, p. 41].

**Un análogo clásico.** No es específico de la información cuántica: con una moneda sesgada desconocida, de la que solo se conoce un resultado, no se puede simular un segundo lanzamiento independiente; esa operación no sería estocástica porque no es lineal. Lo mismo para un número aleatorio entre 1 y 10 [@watrous-2025, L3.3, PDF pp. 94-95; @aaronson-2018, Lec7, p. 4]. Lo que sí se puede copiar es la información clásica [@aaronson-2018, Lec7, pp. 4-5].

**Consecuencias.**

- *La información cuántica no se puede enviar solo por un canal clásico*: si se pudiera, un segundo receptor copiaría el mensaje clásico y obtendría una copia del qubit [@watrous-2025, L4.1, PDF p. 97]. Hace falta entrelazamiento: ver [teleportación cuántica](quantum-teleportation.md).
- *La teleportación no clona*: el original acaba en `|b⟩` tras la medida de Alice y el e-bit se consume [@watrous-2025, L4.1, PDF p. 98]. La copia aparece en Bob solo después de que la medida de Alice destruya el original [@preskill-ph219, ch.4 §4.4.2, p. 32].
- *No se pueden distinguir estados no ortogonales sin perturbarlos*: es la base de la seguridad de la distribución cuántica de claves [@preskill-ph219, ch.4 §4.5.2, p. 39].
- *Argumento indirecto*: con copias ilimitadas, Bob podría hacer tomografía para saber en qué base midió Alice y señalar más rápido que la luz, lo que contradice el teorema de no comunicación [@aaronson-2018, Lec7, p. 3]. Preskill lo dice igual: con copias perfectas se medirían `⟨σ₁⟩`, `⟨σ₂⟩`, `⟨σ₃⟩` y se hallaría la matriz densidad, lo que contradice lo anterior; no puede existir una "fotocopiadora cuántica" perfecta [@preskill-ph219, ch.4 §4.5.2, p. 40].
- *Borrar tampoco se puede*: no existe una unitaria de un qubit que lleve todo `|φ⟩` a `|0⟩` [@de-wolf-2026, ejercicio 1.13, p. 24].
- Un límite relacionado: los estados no ortogonales no se pueden discriminar perfectamente [@watrous-2025, L3.3, PDF pp. 95-98].

**Errores frecuentes.**

- *"`CNOT` copia un qubit."* Copia estados de base, no superposiciones [@aaronson-2018, Lec7, p. 4].
- *"Es un límite de la tecnología."* Sigue de la linealidad y la unitariedad, no de la ingeniería [@preskill-ph219, ch.4 §4.5.2, p. 41].
- *"Teleportar es copiar y pegar."* El original queda destruido [@de-wolf-2026, §1.5, p. 23].

## Profesional {#layer-3}

**Aplicación: dinero cuántico (Wiesner).** Cada billete lleva un número de serie clásico y `n` qubits no entrelazados, cada uno en uno de cuatro estados (dos bases); el banco guarda la base de datos de los estados previstos. Verificar es medir cada qubit en su base. Un falsificador que adivina las bases tiene una probabilidad de éxito exponencialmente pequeña. La seguridad frente a cualquier falsificador se demostró mucho después (Molina, Vidick y Watrous) [@aaronson-2018, Lec7, pp. 5-6]. El problema práctico es la decoherencia: los qubits aguantan, en el mejor caso, una hora en laboratorio, y mucho menos en una cartera; el dinero necesita ser a la vez no clonable y verificable [@aaronson-2018, Lec7, p. 5].

**Aplicación: seguridad de BB84.** Alice envía uno de `|↑_z⟩, |↓_z⟩, |↑_x⟩, |↓_x⟩`; cualquier espionaje que deje los estados sin perturbar produce estados idénticos en el sistema de Eve y por tanto ninguna información sobre la clave; copiar solo el par ortogonal sí sería posible [@preskill-ph219, ch.4 §4.5.1-4.5.2, pp. 38-40]. Es la lógica de los protocolos de clave cuántica; ver [criptografía post-cuántica](../../quantum-algorithms/concepts/post-quantum-cryptography.md) para el otro lado, el de los ataques cuánticos a la criptografía clásica.

**Qué implica para programar.** (1) No existe una instrucción de "copiar qubit": para guardar un valor intermedio hay que moverlo, y la basura de un cálculo se elimina descomputando, no borrando ([circuitos cuánticos](quantum-circuits.md); la puerta que "copia" un bit clásico en una ancilla es `CNOT`, que solo vale para estados de base [@watrous-2025, L3.3, PDF pp. 94-95]). (2) Aprender las amplitudes de un estado desconocido exige muchas copias *preparadas*, no una copia leída: se necesitan tres ejes de medida sobre muchas copias [@preskill-ph219, ch.2 §2.2.1, p. 13].

**Copia aproximada.** El teorema excluye la copia perfecta, no la aproximada, que existe con cotas propias [@watrous-2025, L3.3, PDF p. 94]. Mientras las medidas "mide y reenvía" por canal clásico alcanzan fidelidad media a lo sumo 2/3, la teleportación llega a fidelidad 1 consumiendo un e-bit [@preskill-ph219, ch.4 §4.4.2, pp. 30-32].

**Nota sobre la teoría.** La demostración con ancillas de Preskill es la más general. De Wolf deja la prueba como ejercicio (con una pista en su Apéndice C) [@de-wolf-2026, §1.5, p. 23].
