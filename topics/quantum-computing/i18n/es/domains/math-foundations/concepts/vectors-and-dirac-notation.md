---
concept: vectors-and-dirac-notation
title: "Vectores y notación de Dirac (bra-ket)"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
El estado de un sistema cuántico es un vector columna de amplitudes complejas, y la notación de Dirac lo escribe como un **ket** `|ψ⟩`; su fila conjugada es el **bra** `⟨ψ|` [@watrous-2025, L1.2, p. 20].

### Explicación
`C^n` es el conjunto de listas de `n` números complejos ([números complejos](complex-numbers.md)); se suman y se multiplican por un escalar componente a componente [@axler-2024, def. 1.11-1.13, 1.18, PDF pp. 24, 27]. En computación cuántica se escriben como **columnas**. Un **espacio vectorial (vector space)** es la estructura abstracta con suma y multiplicación por escalar, y `C^n` es un espacio vectorial sobre `C` [@axler-2024, def. 1.22, PDF pp. 31-32]. Es difícil dibujar `C^n`, pero el álgebra en él es tan fácil como en `R²` o `R³` [@axler-2024, §1A, PDF p. 24].

Los estados clásicos de un sistema forman un conjunto finito `Σ` (un bit es `{0,1}`) y los índices del vector se etiquetan con él [@watrous-2025, L1.1, pp. 10-11]. El **ket (ket)** `|a⟩` es el vector columna con un 1 en la posición `a` y 0 en el resto; todo vector es combinación lineal de ellos [@watrous-2025, L1.1, p. 12]. El **bra (bra)** `⟨a|` es la fila con un 1 en la posición `a`, y `⟨a|b⟩` vale 1 si `a = b` y 0 si no [@watrous-2025, L1.1, pp. 15-16].

En general `⟨ψ|` es el **traspuesto conjugado (conjugate transpose)** de `|ψ⟩`, y `⟨a|ψ⟩` es la entrada de `|ψ⟩` en la posición `a` [@watrous-2025, L1.2, p. 20]. De Wolf lo expresa igual: `|v⟩` es el vector y `⟨v|` es `v*` [@de-wolf-2026, App. A.10, p. 210].

Un **qubit** es un sistema con estados clásicos `{0,1}` [@watrous-2025, L1.2, p. 19]. Sus dos estados de base son `|0⟩ = (1,0)ᵀ` y `|1⟩ = (0,1)ᵀ` [@de-wolf-2026, §1.3, p. 19]. Los estados más famosos son `|+⟩ = (|0⟩+|1⟩)/√2 = (1/√2, 1/√2)ᵀ` y `|-⟩ = (|0⟩-|1⟩)/√2 = (1/√2, -1/√2)ᵀ`. "Superposición" y "combinación lineal" son esencialmente sinónimos al hablar de estados cuánticos [@watrous-2025, L1.2, p. 20].

El estado de un sistema cuántico es un vector de amplitudes `α₀|0⟩ + … + α_{N-1}|N-1⟩` en un espacio de Hilbert de dimensión `N` [@de-wolf-2026, §1.2.1, p. 15]. Un registro de `n` qubits es un vector de `2^n` componentes con 1 en la posición `x` para el estado `|x⟩` (contando desde 0) [@de-wolf-2026, §1.3, p. 19].

### Ejemplo
Un vector como combinación de kets: `(3/4, 1/4) = 3/4|0⟩ + 1/4|1⟩` [@watrous-2025, L1.1, p. 12].

El bra de `(1+2i)/3 |0⟩ - (2/3)|1⟩` es `(1-2i)/3 ⟨0| - (2/3)⟨1|`: se traspone y se conjuga cada entrada [@watrous-2025, L1.2, pp. 20-21].

### Errores frecuentes
- *"`|ψ⟩` es un número o un vector fila."* Es una columna; la fila es `⟨ψ|`, que además lleva conjugación.

### Para seguir
[Producto interior, norma y ortogonalidad](inner-products-and-norms.md) combina un bra y un ket para obtener un número. La capa 2 de este concepto trata bases, dimensión y por qué conviene la notación de Dirac.

## Comprensión {#layer-2}

### Idea clave
La base estándar no es la única: cambiar de base cambia las coordenadas del vector, no el vector, y la notación de Dirac permite escribir familias de estados sin fijar una base [@watrous-2025, L1.2, pp. 21-22].

### Explicación
Para hablar de bases hacen falta algunas definiciones:

- Una combinación lineal es `a₁v₁ + … + a_mv_m`; el *span* es el conjunto de todas ellas [@axler-2024, 2.2, 2.4, PDF pp. 46-47].
- Una lista es linealmente independiente si la única forma de obtener 0 es con todos los coeficientes 0; equivale a que cada vector del span tenga una única representación [@axler-2024, 2.15, PDF p. 50].
- Una **base (basis)** es una lista independiente que genera el espacio; equivale a que todo `v` se escriba de forma única como combinación de ella. La base estándar de `F^n` tiene un 1 en la posición `k` [@axler-2024, 2.26-2.28, PDF p. 57].
- Todas las bases de un espacio de dimensión finita tienen la misma longitud: la **dimensión**; `dim F^n = n` [@axler-2024, 2.34-2.36, PDF p. 62].

La dimensión depende del cuerpo de escalares: `C` tiene dimensión 1 sobre `C` pero 2 sobre `R` [@axler-2024, §2C, PDF p. 63].

Con esto se ve que hay otras bases. La base de Bell, con cuatro estados, es una base de `C⁴`: todo vector de 4 componentes es combinación lineal de ellos [@watrous-2025, L2.2, p. 53]. También `{|+⟩, |-⟩}` es base de `C²` [@watrous-2025, L3.2, p. 83].

Los elementos de un espacio vectorial no tienen por qué ser listas (pueden ser funciones o polinomios) [@axler-2024, ex. 1.23-1.25, PDF pp. 31-32]. Sin embargo, todo espacio de dimensión `n` es isomorfo a `F^n` [@axler-2024, 3.69, 3.70, PDF pp. 104-105]. Por eso en la práctica se trabaja siempre con columnas de amplitudes.

Esa abstracción explica el valor de la notación de Dirac: permite escribir vectores grandes o parcialmente especificados y no obliga a fijar un orden de los estados clásicos [@watrous-2025, L1.2, pp. 21-22].

### Ejemplo
La superposición uniforme sobre un conjunto de estados clásicos `Σ` es `1/√|Σ|` por la suma de todos los `|a⟩` [@watrous-2025, L1.2, pp. 21-22]. Y en la base de Bell, `|00⟩ = (|φ⁺⟩ + |φ⁻⟩)/√2` [@watrous-2025, L2.2, p. 53].

### Para seguir
La capa 3 recoge las reglas de escritura y la correspondencia con Axler. Antes, [producto interior](inner-products-and-norms.md) explica por qué las bases ortonormales son tan cómodas.

## Profesional {#layer-3}

### Idea clave
En la práctica la notación de Dirac tiene reglas de uso (no anidar kets, no omitir `⊗` cuando haya ambigüedad) y no coincide con la de Axler, aunque sus ideas se corresponden [@de-wolf-2026, App. A.10, p. 210].

### Explicación
Reglas de escritura que evitan errores. No se anidan kets dentro de bras o kets (`⟨u|(α|v⟩+β|w⟩)⟩` no significa nada) y no conviene usar "qubit" como sustantivo para un registro de varios [@de-wolf-2026, App. A.10, p. 210; nota 6 de §1.3, p. 19]. Además, omitir el signo `⊗` entre kets puede ser peligrosamente ambiguo [@de-wolf-2026, App. A.10, p. 210]. Watrous define `|φ⟩|ψ⟩` y `|φ⊗ψ⟩` como `|φ⟩⊗|ψ⟩` [@watrous-2025, L2.1, pp. 38-39]. Ver [producto tensorial](tensor-products.md).

Cuándo usar Dirac y cuándo columnas. Para sistemas pequeños y números concretos las columnas y matrices son transparentes; para familias de estados con `n` arbitrario (superposición uniforme, estados del algoritmo de Deutsch-Jozsa) la notación de Dirac es la herramienta estándar [@watrous-2025, L1.2, pp. 21-22].

El orden de los índices es una elección, normalmente la predeterminada [@watrous-2025, L1.1, pp. 10-11]. En sistemas de varios qubits esa elección determina el orden de las entradas del vector y es fuente clásica de errores con Qiskit (ver [producto tensorial](tensor-products.md)).

### Ejemplo
Elegir la notación según el objeto: una unitaria de 6×6 con 20 entradas no nulas es más clara escrita como matriz que como 20 términos de Dirac [@watrous-2025, L2.2, p. 63]; la superposición uniforme sobre `n` qubits, en cambio, solo cabe de forma compacta en notación de Dirac [@watrous-2025, L1.2, pp. 21-22].

### Las fuentes discrepan
Axler no usa notación de Dirac en ninguna parte (escribe `v`, `⟨u,v⟩` y `T*`), pero su relación `⟨Tv,w⟩ = ⟨v,T*w⟩` desempeña el papel de la identidad bra-ket [@axler-2024, def. 7.1, PDF pp. 246-247]. Al leer un teorema de Axler hay que traducirlo: `⟨u,v⟩` de Axler corresponde a `⟨v|u⟩` de la convención de física (ver [producto interior](inner-products-and-norms.md)).

### Para seguir
[Producto interior, norma y ortogonalidad](inner-products-and-norms.md), capa 3, detalla esa convención de conjugación.
