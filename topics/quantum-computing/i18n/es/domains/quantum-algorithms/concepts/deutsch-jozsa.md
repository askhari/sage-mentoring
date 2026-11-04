---
concept: deutsch-jozsa
title: "Algoritmo de Deutsch-Jozsa"
---

## Fundamentos {#layer-1}

**El problema más pequeño: Deutsch.** Te dan una caja negra `f: {0,1} → {0,1}` (ver [modelo de consultas](query-model-and-oracles.md)). Hay que decir si `f` es *constante* (`f(0) = f(1)`) o *equilibrada (balanced)* (da 0 en una entrada y 1 en la otra). Es el problema de la paridad con `n = 1`: el XOR de `f(0)` y `f(1)` [@watrous-2025, L5.2, PDF pp. 139-140].

- *Clásicamente* hacen falta dos consultas: conocer un solo bit no dice nada de la paridad [@watrous-2025, L5.2, PDF p. 140].
- *Cuánticamente* basta **una**. Circuito: objetivo en `|1⟩` y control en `|0⟩`, Hadamard en ambos, una consulta `U_f`, Hadamard en el control y medida. El resultado 0 significa "constante" y 1 "equilibrada", y la respuesta es correcta con probabilidad 1 [@watrous-2025, L5.2, PDF pp. 140-142].

Watrous lo califica de ventaja "modesta" (una consulta frente a dos), pero cuantificable [@watrous-2025, L5.2, PDF p. 140].

**El problema general.** Ahora `f: {0,1}ⁿ → {0,1}`, con la *promesa* de que es constante o equilibrada (valor 1 exactamente en la mitad de las entradas). Hay que decir cuál. Cualquier otra función (por ejemplo, una que valga 1 en una sola de cuatro entradas) es una entrada "no importa" [@watrous-2025, L5.3, PDF pp. 144-145].

**El circuito.** `n` qubits en `|0⟩` y uno auxiliar en `|1⟩`; Hadamard en todos; **una** consulta `U_f`; Hadamard en los `n` primeros; medir esos `n`. Si todos los resultados son 0, la función es constante; si no, equilibrada [@watrous-2025, L5.3, PDF pp. 144-145].

![Circuito de Deutsch-Jozsa](../../../../../assets/diagrams/deutsch-jozsa-circuit.es.svg)

**Cuánto se gana.** Un algoritmo clásico *determinista* necesita `2^{n−1} + 1` consultas en el peor caso: tras ver `2^{n−1}` valores iguales todavía son posibles "constante" y "equilibrada" [@watrous-2025, L5.3, PDF pp. 147-148]. El cuántico usa una. Es una separación exponencial frente a los clásicos deterministas.

**Pero ojo.** Un algoritmo clásico *aleatorio* que consulta `k` cadenas al azar y responde "constante" si todos los valores coinciden acierta siempre en funciones constantes y falla en las equilibradas con probabilidad solo `2^{−k+1}`; con `k = 11` acierta con probabilidad superior al 99,9 % [@watrous-2025, L5.3, PDF p. 148]. Por eso la ventaja frente a los algoritmos probabilísticos es modesta. Shor lo dice sin rodeos: no es una prueba convincente de ventaja cuántica; su importancia es que condujo al algoritmo de Simon [@shor-mit-2022, L16, p. 4].

## Comprensión {#layer-2}

**Por qué funciona: interferencia.** Una capa de Hadamard sobre `n` qubits actúa como `H^{⊗n}|x⟩ = 2^{−n/2} Σ_y (−1)^{x·y}|y⟩`, donde `x·y` es el producto escalar binario [@watrous-2025, L5.3, PDF p. 146; @shor-mit-2022, L16, pp. 1-2]. El análisis tiene tres pasos:

1. Tras la primera capa, el estado es la superposición uniforme de las `2ⁿ` cadenas [@de-wolf-2026, §2.4.1, pp. 30-31].
2. La consulta, con el auxiliar en `|−⟩`, usa el [retroceso de fase](phase-kickback.md): deja `|−⟩ ⊗ 2^{−n/2} Σ_x (−1)^{f(x)}|x⟩` [@watrous-2025, L5.3, PDF pp. 146-147].
3. La segunda capa vuelve a hacer una Hadamard; la amplitud de `|0ⁿ⟩` es `2^{−n} Σ_x (−1)^{f(x)}` [@de-wolf-2026, §2.4.1, pp. 30-31; @shor-mit-2022, L16, pp. 3-4].

Si `f` es constante, la suma vale `±2ⁿ` y la amplitud es `±1`: se mide `0ⁿ` con certeza. Si es equilibrada, los términos `+1` y `−1` se cancelan y la amplitud es 0: nunca se mide `0ⁿ`. Por tanto el algoritmo acierta siempre cuando se cumple la promesa [@watrous-2025, L5.3, PDF p. 147]. La regla que resume Aaronson: poner todo en superposición con Hadamards, consultar como oráculo de fase, cambiar de base con otra ronda de Hadamards y medir; "si no sabes qué hacer a continuación, una ronda de Hadamards es siempre una buena apuesta" [@aaronson-2018, Lec17, p. 7].

**Coste.** Una consulta cuántica y `O(n)` operaciones más, con certeza [@de-wolf-2026, §2.4.1, p. 31]. La solución original de Deutsch-Jozsa usaba dos consultas; la de una consulta se atribuye a Cleve y colaboradores [@de-wolf-2026, §2.4.1, p. 31].

**Una diferencia de enfoque: ¿con error o sin él?** El clásico necesita `N/2 + 1` consultas deterministas, con `N = 2ⁿ` [@de-wolf-2026, §2.4.1, p. 31]. Pero un clásico aleatorio que mira dos posiciones al azar y dice "constante" si coinciden acierta siempre en constantes y la mitad de las veces en equilibradas: al permitir error, la separación desaparece [@de-wolf-2026, §2.4.1, p. 31]. La separación vale solo frente a algoritmos clásicos *sin error* [@de-wolf-2026, §2.4.1, p. 31].

**Errores frecuentes.**

- *"Deutsch-Jozsa prueba que lo cuántico es exponencialmente más rápido."* Solo frente a clásicos deterministas exactos, en un modelo de consultas y con promesa [@watrous-2025, L5.3, PDF p. 148; @shor-mit-2022, L16, p. 4].
- *"Se prueban todas las entradas a la vez."* La consulta es una sola; la ventaja viene de que las `2ⁿ` contribuciones interfieran. Ver [circuitos cuánticos](../../qubits-and-circuits/concepts/quantum-circuits.md), donde se explica que medir una superposición da una sola salida.
- *"Si miro la salida distinta de `0ⁿ` sé qué función es."* Solo sabes que es equilibrada; no hay más información [@watrous-2025, L5.3, PDF pp. 144-145].
- Cifras inconsistentes en la literatura: unas notas dicen que el mejor clásico determinista necesita `2^{n−1}+1` consultas y, más abajo, "alrededor de `2^{n/2}`"; la cifra exacta derivada es la primera [@shor-mit-2022, L16, pp. 2, 4].

**Relación con otros conceptos.** El mismo circuito, sin el postproceso con `OR`, resuelve el problema de [Bernstein-Vazirani](bernstein-vazirani-and-simon.md) [@watrous-2025, L5.3, PDF pp. 149-151]. Deutsch-Jozsa con `n = 1` es una instancia del problema del subgrupo oculto [@de-wolf-2026, ej. 6.1, p. 63].

## Profesional {#layer-3}

**Qué papel juega en la práctica.** Ningún problema real se parece a "constante o equilibrada": es un algoritmo pedagógico y una plantilla. Pero la plantilla *Hadamard, oráculo de fase, Hadamard, medir* aparece de nuevo en [Bernstein-Vazirani](bernstein-vazirani-and-simon.md), en Simon y, con otro papel de la segunda capa, en [Grover](grover-search.md) [@watrous-2025, L5.3-L5.4, PDF pp. 144-160; L8.2, PDF p. 242]. El mensaje que conviene retener es de método: ¿qué patrón de signos `(−1)^{g(x)}` produce el oráculo y qué cambio de base lo convierte en un resultado legible?

**Cómo evaluar la ventaja.**

- *Frente a qué clásico:* exacto (determinista), aleatorio con error pequeño o la mejor solución conocida. La ventaja de Deutsch-Jozsa existe solo en el primer caso; un aleatorio con 20-30 consultas ya falla con probabilidad ínfima [@shor-mit-2022, L16, p. 4]. Aaronson añade que, por esa razón, hasta 1994 casi nadie se interesó por la computación cuántica [@aaronson-2018, Lec17, pp. 6-7].
- *Exactitud cuántica:* "sin error" depende del conjunto de puertas. La clase `EQP` (tiempo polinómico cuántico exacto) se considera poco interesante precisamente por eso [@de-wolf-2026, §13.2, pp. 122-123].
- *Modelo:* es una separación de consultas, no de circuitos [@de-wolf-2026, §2.4, p. 29]. Ver [complejidad cuántica](quantum-complexity.md).

**El truco de Deutsch por parejas.** La paridad de `n` bits se obtiene con `n/2` consultas dividiendo la entrada en bloques de 2 bits, aplicando Deutsch a cada bloque y combinando clásicamente [@aaronson-2018, Lec17, p. 6]. Esto es óptimo: `Parity` necesita `≥ n/2` consultas incluso con error acotado [@childs-qa, §21.5, pp. 99-100]. Es un ejemplo de problema en el que el truco cuántico da solo un factor 2.

**Qué construir para practicarlo.** Un buen ejercicio de programación es construir el oráculo `U_f` para una `f` constante y para otra equilibrada, y comprobar que el circuito da `0ⁿ` solo en el primer caso. Los detalles de código están en [programación con Qiskit](../../qiskit-programming/index.md).
