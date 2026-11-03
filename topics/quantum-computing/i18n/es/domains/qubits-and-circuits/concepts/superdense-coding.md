---
concept: superdense-coding
title: "Codificación superdensa"
---

## Comprensión {#layer-2}

**El objetivo.** Alice quiere enviar a Bob dos bits clásicos `c, d` mandándole *un solo qubit*, con ayuda de un e-bit compartido [@watrous-2025, L4.2, PDF pp. 110-111]. Es el primer protocolo que *necesita* entrelazamiento [@aaronson-2018, Lec9, p. 1]. Sin entrelazamiento previo, el teorema de Holevo impide que un qubit lleve más de un bit clásico [@watrous-2025, L4.2, PDF p. 111; @de-wolf-2026, ejercicio 1.14, p. 24, nota 10]. Es el complemento de la [teleportación](quantum-teleportation.md): esta envía un qubit con dos bits clásicos y un e-bit; la superdensa envía dos bits clásicos con un qubit y un e-bit [@watrous-2025, L4.2, PDF p. 110].

**La idea.** Al actuar sobre *su mitad* de un par de Bell, Alice puede llegar a cuatro estados mutuamente ortogonales, que forman una base, de modo que Bob puede distinguirlos [@aaronson-2018, Lec9, p. 1]. Los cuatro estados de Bell salen de aplicar `I, X, Z` o ambas a la mitad de Alice [@watrous-2025, L4.2, PDF pp. 112-113]. Alice elige uno de los cuatro estados de Bell y Bob mide para saber cuál [@watrous-2025, L4.2, PDF p. 112]. Los cuatro estados que producen las Paulis `I, X, Y, Z` sobre la mitad de Alice forman un conjunto ortonormal, perfectamente distinguible por una medida proyectiva de cuatro resultados [@de-wolf-2026, ejercicio 1.15(b)(c), p. 24].

**Codificación.** Alice aplica `Z` si `d = 1` y después `X` si `c = 1` a su qubit `A`, y se lo envía a Bob [@watrous-2025, L4.2, PDF p. 111]. (De Wolf usa el orden `X` y luego `Z` con los bits `a, b`; los estados difieren solo en una fase global [@de-wolf-2026, ejercicio 1.14(a), p. 24].) Partiendo de `|φ⁺⟩ = (|00⟩+|11⟩)/√2` (`A` primero):

| `cd` | Operación de Alice | Estado de `(A, B)` |
|---|---|---|
| 00 | `I` | `\|φ⁺⟩ = (\|00⟩+\|11⟩)/√2` |
| 01 | `Z` | `\|φ⁻⟩ = (\|00⟩−\|11⟩)/√2` |
| 10 | `X` | `\|ψ⁺⟩ = (\|01⟩+\|10⟩)/√2` |
| 11 | `XZ` | `(\|10⟩−\|01⟩)/√2 = −\|ψ⁻⟩` |

Los resultados son `|φ⁺⟩, |φ⁻⟩, |ψ⁺⟩, |ψ⁻⟩` salvo el signo global del último [@watrous-2025, L4.2, PDF pp. 112-113].

**Decodificación.** Bob tiene los dos qubits. Aplica `CNOT` (control `A`, objetivo `B`), luego `H` sobre `A`, y mide ambos en la base estándar [@watrous-2025, L4.2, PDF p. 111; @aaronson-2018, Lec9, p. 2]: es el inverso del circuito que fabrica pares de Bell ([entrelazamiento](entanglement.md)). Comprobación con `|φ⁻⟩`: `CNOT` da `(|00⟩ − |10⟩)/√2 = (|0⟩−|1⟩)/√2 ⊗ |0⟩`; `H` sobre `A` da `|1⟩|0⟩`, es decir `A = 1`, `B = 0`. Las cuatro entradas dan `|00⟩, |10⟩, |01⟩, −|11⟩`: la medida de `B` da `c` y la de `A` da `d` [@watrous-2025, L4.2, PDF pp. 112-113].

**Por qué no viola Holevo.** El qubit enviado tiene, por sí solo, la matriz densidad `I/2` y no lleva información; toda la información está en las correlaciones entre `A` y `B`, así que un espía tendría que capturar los dos qubits [@preskill-ph219, ch.4 §4.4.1, p. 29]. Además, se puede ver como dos transmisiones de qubit en total (la mitad del par se envió antes), coherente con la cota de Holevo de 2 bits por 2 qubits; lo extraño es que el primer qubit se envió antes de conocer el mensaje [@preskill-ph219, ch.4 §4.4.1, p. 29]. Y con cualquier cantidad de e-bits compartidos, un qubit sigue llevando como mucho dos bits clásicos [@aaronson-2018, Lec9, p. 2].

**Errores frecuentes.**

- *"Se comprime información: dos bits en un qubit gratis."* Hace falta un e-bit, que hay que haber enviado antes [@preskill-ph219, ch.4 §4.4.1, p. 29].
- *"Rompe la teoría de la información."* Supera la cota que parecía dar Shannon, pero respeta la de Holevo: con cualquier número de e-bits, un qubit lleva a lo sumo dos bits clásicos [@aaronson-2018, Lec9, p. 2].
- *"Basta con medir el qubit que llega."* Medirlo solo da un bit aleatorio; la información está en la medida conjunta de los dos [@preskill-ph219, ch.4 §4.4.1, p. 29].

## Profesional {#layer-3}

**Resumen con desigualdades de recursos.** `1 e-bit + 1 qubit ≥ 2 bits clásicos` (codificación superdensa) y `1 e-bit + 2 bits clásicos ≥ 1 qubit` (teleportación): ambas gastan un e-bit y son conversas casi exactas [@preskill-ph219, ch.4 §4.4.2, pp. 30, 32; @aaronson-2018, Lec10, p. 1]. La teleportación es óptima [@aaronson-2018, Lec10, p. 1] y la superdensa también: no hay forma de enviar más de dos bits por qubit [@aaronson-2018, Lec9, p. 2]. Que el entrelazamiento duplica la capacidad clásica de un qubit es lo que se demuestra con Holevo [@watrous-2025, L4.2, PDF p. 111].

**Valor práctico.** Watrous señala que cambiar un qubit por dos bits al coste de un e-bit "apenas merece la pena" en la práctica, pero es un uso claro del entrelazamiento [@watrous-2025, L4.2, PDF p. 111]. Aaronson lo llama un factor 2 modesto, aunque rompe la cota que parecía dar Shannon [@aaronson-2018, Lec9, p. 2].

**Confidencialidad.** Como el qubit que viaja está en `I/2`, interceptarlo no da información, pero el atacante aún puede interferir (*jamming*) [@preskill-ph219, ch.4 §4.4.1, p. 29].

**Cómo se programa.** El circuito completo de superdensa son un par de Bell (`H` + `CNOT`), una puerta de Pauli condicional por cada bit y el decodificador (`CNOT` + `H` + medida): ver [circuitos cuánticos](quantum-circuits.md). Alice solo necesita una Pauli local (`I, X, Y, Z`) para elegir el estado de Bell [@preskill-ph219, ch.4 §4.4.1, pp. 28-29].

**Para seguir.** Otra tarea en la que el entrelazamiento supera lo clásico es el juego de [desigualdades de Bell](bell-inequalities.md); las tres tareas (teleportación, superdensa, CHSH) son los ejemplos con los que Watrous muestra para qué sirve el entrelazamiento [@watrous-2025, L4, PDF p. 101].
