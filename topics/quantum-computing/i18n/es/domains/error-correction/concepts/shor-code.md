---
concept: shor-code
title: "Código de Shor de 9 qubits"
---

- Se asume [el código de repetición](repetition-codes.md) en sus dos versiones (bit-flip y phase-flip). No confundir este código con [el algoritmo de Shor](../../quantum-algorithms/concepts/shor-algorithm.md): comparten autor, no objetivo.

## Comprensión {#layer-2}

**La idea: apilar los dos códigos de repetición.** El [código de bit-flip](repetition-codes.md) protege contra `X` y el de phase-flip contra `Z`. El *código de Shor de 9 qubits (Shor's 9-qubit code)* los concatena: primero se codifica el qubit con el código de phase-flip (el código *externo*, a tres qubits) y luego cada uno de esos tres se codifica con el código de bit-flip (el código *interno*). Resultan tres bloques de tres qubits [@watrous-2025, L13.2, PDF p. 391].

**Las palabras de código.** `|0⟩` se codifica como `(|000⟩ + |111⟩)^{⊗3} / (2√2)` y `|1⟩` como `(|000⟩ − |111⟩)^{⊗3} / (2√2)` [@watrous-2025, L13.2, PDF p. 391]. De Wolf escribe lo mismo con `1/√8` y precisa que el espacio de código es el subespacio de dimensión 2 generado por ambos dentro del espacio de dimensión `2⁹` [@de-wolf-2026, §21.4, p. 197 [185]].

**Cómo corrige cada tipo de error.**

- *Volteos de bit (`X`).* Cada bloque se trata aparte con el síndrome de repetición de siempre; se corrige hasta un `X` por bloque [@watrous-2025, L13.2, PDF p. 394]. En cada bloque `|000⟩ ± |111⟩`, el qubit en minoría señala dónde está el volteo [@de-wolf-2026, §21.4, p. 198 [186]].
- *Volteos de fase (`Z`).* Una `Z` en cualquier qubit de un bloque equivale a una `Z` sobre el qubit correspondiente del código externo antes de la codificación interna. Se compara el signo relativo de los tres bloques, y el bloque cuyo signo difiere es el afectado [@watrous-2025, L13.2, PDF pp. 394-397; @de-wolf-2026, §21.4, p. 198 [186]].
- *Degeneración.* El síndrome de fase dice qué *bloque* falló, no qué qubit, y basta aplicar `Z` a cualquier qubit de ese bloque para arreglarlo. Watrous lo llama un ejemplo de degeneración: se corrigen errores sin identificarlos de forma única [@watrous-2025, L13.2, PDF p. 396]. De Wolf no usa la palabra, pero su síndrome de fase es igual de grueso a propósito [@de-wolf-2026, §21.4, p. 198 [186]].
- *Ambos a la vez (`Y`).* Las correcciones de `X` y de `Z` son independientes y se pueden hacer en cualquier orden, porque `XZ = −ZX` difiere solo por una fase global [@watrous-2025, L13.2, PDF pp. 397-399].

El resultado: el código corrige un `X`, un `Z` o ambos en cualquiera de los nueve qubits, y por la [discretización de errores](quantum-noise-channels.md) cualquier error en un solo qubit. También corrige varios `X` si caen en bloques distintos [@watrous-2025, L13.2, PDF pp. 397-399]. En la versión de De Wolf, una sola unitaria actúa sobre 9 + 4 + 2 = 15 qubits: 4 auxiliares para la posición del volteo de bit (un número de 0 a 9) y 2 para el bloque del volteo de fase (de 0 a 3) [@de-wolf-2026, §21.4, p. 198 [186]].

**¿Cuándo vale la pena?** Con errores de Pauli independientes de probabilidad `p` por qubit (y los `Y` como peor caso), el código tiene éxito si como mucho uno de los nueve qubits recibe un error, por lo que el error lógico es

```
p_L = 1 − (1−p)⁹ − 9p(1−p)⁸
```

[@watrous-2025, L13.2, PDF pp. 400-402]. Solo mejora al qubit sin proteger por debajo de un punto de equilibrio cercano a `p ≈ 0,0323` (alrededor del 3,2 %), frente al 50 % del código clásico de 3 bits [@watrous-2025, L13.2, PDF pp. 400-402]. Con `p = 0,01`:

- `(0,99)⁹ ≈ 0,9135` y `9 · 0,01 · (0,99)⁸ ≈ 0,0830`.
- `p_L ≈ 1 − 0,9135 − 0,0830 = 0,0034`, es decir, unas tres veces menos que el 1 % de un qubit sin proteger (cálculo propio con la fórmula citada).

Para `p` pequeño, `p_L` se parece a `36p²` (las 36 parejas de errores entre 9 qubits, `9·8/2`; cálculo propio): una supresión cuadrática, la misma de [la repetición](repetition-codes.md) pero con más lugares donde fallar. De Wolf lo advierte: al codificar, el número de lugares con error pasa de 1 a 9 (15 con las auxiliares, más los pasos de síndrome y corrección), así que el código solo ayuda cuando `p` es tan pequeño que dos o más errores son menos probables que uno en el qubit sin proteger [@de-wolf-2026, §21.4, p. 199 [187]]. Eso conecta con el [teorema del umbral](threshold-theorem.md).

**Cada ronda necesita ancillas nuevas.** Las auxiliares se usan una vez y se descartan: De Wolf compara la corrección de errores con un frigorífico que expulsa el ruido hacia qubits auxiliares desechables [@de-wolf-2026, §21.4, p. 199 [187]].

**Errores frecuentes.**

- *"El código de Shor es el que se usa en los ordenadores actuales."* Watrous lo llama un descubrimiento brillante, el primer código cuántico corrector de errores, pero no un buen código en términos prácticos [@watrous-2025, L13.2, PDF pp. 401-402].
- *"Corrige cualquier error en cualquier número de qubits."* Corrige un error arbitrario en *un* qubit (y varios `X` en bloques distintos); dos errores en el mismo bloque pueden provocar un error lógico, como en la repetición [@watrous-2025, L13.2, PDF pp. 397-399].
- *"El fallo es un error en un qubit de los datos."* Un fallo significa que un Pauli no trivial actúa sobre el qubit lógico [@watrous-2025, L13.2, PDF pp. 401-402].

## Profesional {#layer-3}

**El código visto como estabilizador.** Tiene ocho generadores: seis comprobaciones `ZZ` dentro de los bloques (`ZZIIIIIII`, `IZZIIIIII` y así hasta `IIIIIIIZZ` sin cruzar bloques) y dos generadores `X` de peso 6 (`XXXXXXIII` y `IIIXXXXXX`) [@watrous-2025, L14.3, PDF p. 423]. Con nueve qubits físicos y ocho generadores independientes, el espacio de código tiene dimensión `2^{9−8} = 2`: un qubit lógico [@watrous-2025, L14.3, PDF pp. 425-428]. Los operadores lógicos tienen peso 3: `X` lógico es `ZIIZIIZII` y `Z` lógico es `XXXIIIIII` (ambos de peso 3) [@watrous-2025, L16.2, PDF p. 479]. Esto da distancia 3, es decir un código [[9, 1, 3]] en la notación `[[n, k, d]]` del [formalismo de estabilizadores](stabilizer-formalism.md) (cálculo propio con las definiciones de Watrous: `n = 9`, `k = 1`, y `d` es el menor peso de un error no detectable).

**Por qué no se usa tal cual.**

1. *Comprobaciones pesadas.* Los generadores `X` de peso 6 son medidas conjuntas de seis qubits: circuitos mayores, con más lugares donde fallar. Compárese con las comprobaciones de peso 4 y locales del [código de superficie](surface-code.md) [@watrous-2025, L15, PDF pp. 439, 451].
2. *Eficiencia.* Nueve qubits para uno lógico y distancia 3. El código más corto que protege un qubit lógico contra un error tiene 5 físicos, y existen códigos "asintóticamente buenos" que codifican `k` lógicos en `O(k)` físicos y corrigen errores en una fracción constante de los qubits [@de-wolf-2026, §21.4, p. 199 [187]]. Además, ningún código protege un qubit lógico contra errores en hasta `k` qubits con solo `2k` físicos (ejercicio 6 de De Wolf), y hay una cota de recuento `2^k Σ_{i≤w} C(n,i) 3^i ≤ 2^n` para códigos que corrigen errores de peso `w` [@de-wolf-2026, ej. 6 y 8, pp. 201-203 [189-191]].
3. *No escala por sí solo.* Su error lógico cae como `p²` y no como `p^((d+1)/2)` con `d` creciente; para llegar a `10⁻¹²` hay que concatenar de nuevo (`9ᵏ` qubits tras `k` niveles) o cambiar de familia. Ver [teorema del umbral](threshold-theorem.md).

**Lo que sí enseña, y hoy se usa.**

- *Concatenación.* Es el ejemplo mínimo de la técnica que prueba el teorema del umbral [@watrous-2025, L16.3, PDF p. 489].
- *Códigos CSS.* El código de Shor, el de Steane y el código tórico son todos CSS, es decir, con generadores solo de tipo `X` o solo de tipo `Z` [@watrous-2025, L15.1, PDF pp. 444-446]. Esa separación explica por qué `X` y `Z` se decodifican por separado en los códigos que sí se construyen: el [código de superficie](surface-code.md) y los códigos bicicleta (*bivariate bicycle*) de IBM [@watrous-2025, L16.2, PDF p. 483; @bravyi-2024, pp. 7, 18].
- *Códigos pequeños de detección.* Los experimentos de átomos neutros usan bloques `[[8,3,2]]` que detectan errores en lugar de corregirlos [@bluvstein-2024, pp. 5-6]; ver [experimentos con qubits lógicos](logical-qubit-experiments.md).

**Cómo decidir (criterio propio a partir de lo anterior).** Si el objetivo es aprender, el código de Shor es el mejor ejemplo para recorrer a mano todo el ciclo (codificar, introducir un error, extraer síndrome, corregir). Si el objetivo es una memoria cuántica física, se parte del [código de superficie](surface-code.md) por sus comprobaciones locales de peso 4 y su umbral cercano al 1 % [@fowler-2012, p. 2], o de un código qLDPC de mayor tasa de codificación `k/n` si el hardware admite conexiones de largo alcance (ver la comparación en el [código de superficie](surface-code.md)). Si se necesita un código en el que todas las puertas de Clifford sean transversales, el de Steane `[[7,1,3]]` tiene esa propiedad [@watrous-2025, L16.2, PDF p. 479]; véase [puertas tolerantes a fallos](fault-tolerant-gates.md).

**Para seguir.** Los generadores aparecen una y otra vez; el [formalismo de estabilizadores](stabilizer-formalism.md) les da un lenguaje común.
