---
concept: vectors-and-dirac-notation
title: "Vectores y notación de Dirac (bra-ket)"
---

## Fundamentos {#layer-1}

`C^n` es el conjunto de listas de `n` números complejos; se suman y se multiplican por un escalar componente a componente [@axler-2024, def. 1.11-1.13, 1.18, PDF pp. 24, 27]. En computación cuántica se escriben como **columnas**. Un **espacio vectorial (vector space)** es la estructura abstracta con suma y multiplicación por escalar; `C^n` es un espacio vectorial sobre `C` [@axler-2024, def. 1.22, PDF pp. 31-32]. Es difícil dibujar `C^n`, pero el álgebra en él es tan fácil como en `R²` o `R³` [@axler-2024, §1A, PDF p. 24].

**Ket y bra.** Los estados clásicos de un sistema forman un conjunto finito `Σ` (un bit es `{0,1}`) y los índices del vector se etiquetan con él [@watrous-2025, L1.1, pp. 10-11]. El **ket (ket)** `|a⟩` es el vector columna con un 1 en la posición `a` y 0 en el resto; todo vector es combinación lineal de ellos, por ejemplo `(3/4, 1/4) = 3/4|0⟩ + 1/4|1⟩` [@watrous-2025, L1.1, p. 12]. El **bra (bra)** `⟨a|` es la fila con un 1 en la posición `a`, y `⟨a|b⟩` vale 1 si `a = b` y 0 si no [@watrous-2025, L1.1, pp. 15-16]. En general `⟨ψ|` es el **traspuesto conjugado (conjugate transpose)** de `|ψ⟩`, y `⟨a|ψ⟩` es la entrada de `|ψ⟩` en la posición `a` [@watrous-2025, L1.2, p. 20]. De Wolf lo expresa igual: `|v⟩` es el vector y `⟨v|` es `v*` [@de-wolf-2026, App. A.10, p. 210].

**Ejemplo con un qubit.** Un **qubit** es un sistema con estados clásicos `{0,1}` [@watrous-2025, L1.2, p. 19], y `|0⟩ = (1,0)ᵀ`, `|1⟩ = (0,1)ᵀ` [@de-wolf-2026, §1.3, p. 19]. Los estados más famosos son
`|+⟩ = (|0⟩+|1⟩)/√2 = (1/√2, 1/√2)ᵀ` y `|-⟩ = (|0⟩-|1⟩)/√2 = (1/√2, -1/√2)ᵀ` [@watrous-2025, L1.2, p. 20].

"Superposición" y "combinación lineal" son esencialmente sinónimos al hablar de estados cuánticos [@watrous-2025, L1.2, p. 20].

**Ejemplo de bra.** El bra de `(1+2i)/3 |0⟩ - (2/3)|1⟩` es `(1-2i)/3 ⟨0| - (2/3)⟨1|`: se traspone y se conjuga cada entrada [@watrous-2025, L1.2, pp. 20-21].

**Para qué sirve.** El estado de un sistema cuántico es un vector de amplitudes `α₀|0⟩ + … + α_{N-1}|N-1⟩` en un espacio de Hilbert de dimensión `N` [@de-wolf-2026, §1.2.1, p. 15]. Un registro de `n` qubits es un vector de `2^n` componentes con 1 en la posición `x` para el estado `|x⟩` (contando desde 0) [@de-wolf-2026, §1.3, p. 19].

## Comprensión {#layer-2}

**Combinación lineal, span, independencia, base, dimensión.**

- Una combinación lineal es `a₁v₁ + … + a_mv_m`; el *span* es el conjunto de todas ellas [@axler-2024, 2.2, 2.4, PDF pp. 46-47].
- Una lista es linealmente independiente si la única forma de obtener 0 es con todos los coeficientes 0; equivale a que cada vector del span tenga una única representación [@axler-2024, 2.15, PDF p. 50].
- Una **base (basis)** es una lista independiente que genera el espacio; equivale a que todo `v` se escriba de forma única como combinación de ella. La base estándar de `F^n` tiene un 1 en la posición `k` [@axler-2024, 2.26-2.28, PDF p. 57].
- Todas las bases de un espacio de dimensión finita tienen la misma longitud: la **dimensión**; `dim F^n = n` [@axler-2024, 2.34-2.36, PDF p. 62].

**La base estándar no es la única.** La base de Bell, con cuatro estados, es una base de `C⁴`: todo vector de 4 componentes es combinación lineal de ellos, p. ej. `|00⟩ = (|φ⁺⟩ + |φ⁻⟩)/√2` [@watrous-2025, L2.2, p. 53]. También `{|+⟩, |-⟩}` es base de `C²` [@watrous-2025, L3.2, p. 83]. Cambiar de base cambia las coordenadas, no el vector.

**Por qué la notación de Dirac.** Permite escribir vectores grandes o parcialmente especificados (la superposición uniforme es `1/√|Σ|` por la suma de los `|a⟩`) y no obliga a fijar un orden de los estados clásicos [@watrous-2025, L1.2, pp. 21-22]. No siempre es la mejor elección: una unitaria de 6×6 con 20 entradas no nulas es más clara como matriz que como 20 términos [@watrous-2025, L2.2, p. 63].

**Dependencia del cuerpo de escalares.** `C` tiene dimensión 1 sobre `C` pero 2 sobre `R` [@axler-2024, §2C, PDF p. 63]. Un `C^n` tiene dimensión `n` como espacio complejo.

**Abstracto frente a concreto.** Los elementos de un espacio vectorial no tienen por qué ser listas (pueden ser funciones o polinomios) [@axler-2024, ex. 1.23-1.25, PDF pp. 31-32], pero todo espacio de dimensión `n` es isomorfo a `F^n` [@axler-2024, 3.69, 3.70, PDF pp. 104-105]. Por eso en la práctica se trabaja siempre con columnas de amplitudes.

**Error típico.** Pensar que `|ψ⟩` es "un número" o "un vector fila". Es una columna; la fila es `⟨ψ|`, que además lleva conjugación.

## Profesional {#layer-3}

**Reglas de escritura que evitan errores.** De Wolf avisa de que no se anidan kets dentro de bras o kets (`⟨u|(α|v⟩+β|w⟩)⟩` no significa nada) y de que no conviene usar "qubit" como sustantivo para un registro de varios [@de-wolf-2026, App. A.10, p. 210; nota 6 de §1.3, p. 19]. Además, omitir el signo `⊗` entre kets puede ser peligrosamente ambiguo [@de-wolf-2026, App. A.10, p. 210]; Watrous define `|φ⟩|ψ⟩` y `|φ⊗ψ⟩` como `|φ⟩⊗|ψ⟩` [@watrous-2025, L2.1, pp. 38-39]. Ver [producto tensorial](tensor-products.md).

**Cuándo usar Dirac y cuándo columnas.** Para sistemas pequeños y números concretos (por ejemplo al depurar un circuito de 2 qubits) las columnas y matrices son transparentes; para familias de estados con `n` arbitrario (superposición uniforme, estados del algoritmo de Deutsch-Jozsa, etc.) la notación de Dirac es la herramienta estándar [@watrous-2025, L1.2, pp. 21-22].

**Correspondencia con Axler.** Axler no usa notación de Dirac en ninguna parte (escribe `v`, `⟨u,v⟩` y `T*`), pero su relación `⟨Tv,w⟩ = ⟨v,T*w⟩` desempeña el papel de la identidad bra-ket [@axler-2024, def. 7.1, PDF pp. 246-247]. Cuando leas un teorema en Axler, tradúcelo: `⟨u,v⟩` de Axler corresponde a `⟨v|u⟩` de la convención de física (ver [producto interior](inner-products-and-norms.md)).

**Etiquetas y orden.** El orden de los índices es una elección, normalmente la predeterminada [@watrous-2025, L1.1, pp. 10-11]. En sistemas de varios qubits esa elección determina el orden de las entradas del vector y es fuente clásica de errores con Qiskit (ver [producto tensorial](tensor-products.md)).
