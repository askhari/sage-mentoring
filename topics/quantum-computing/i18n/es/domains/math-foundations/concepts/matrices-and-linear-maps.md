---
concept: matrices-and-linear-maps
title: "Matrices y aplicaciones lineales"
---

## Fundamentos {#layer-1}

Una **aplicación lineal (linear map)** `T` es una función entre espacios vectoriales que es aditiva y homogénea: `T(u+v) = Tu + Tv` y `T(λv) = λTv`. Un **operador (operator)** es una aplicación lineal de un espacio en sí mismo [@axler-2024, def. 3.1-3.3, PDF pp. 70-71]. Una **matriz (matrix)** es la forma de anotar una aplicación lineal una vez elegidas las bases: la columna `k` contiene el resultado de aplicar `T` al `k`-ésimo vector de la base; para `F^n → F^m` con bases estándar, es `T` aplicada al `k`-ésimo vector estándar [@axler-2024, def. 3.31, PDF pp. 87-88]. Basta saber qué hace `T` con una base para saberlo todo [@axler-2024, §3C, PDF p. 87].

**Ejemplo con una matriz compleja de 2×2.** Sea `S = diag(1, i) = [[1,0],[0,i]]`. Aplicada a `|+⟩ = (1/√2, 1/√2)ᵀ`: `S|+⟩ = (1/√2, i/√2)ᵀ`. La primera entrada se multiplica por 1 y la segunda por `i`. `S` es la puerta de fase `P_{π/2}` [@watrous-2025, L1.2, p. 26].

**Producto de matrices.** La entrada `(j,k)` de `AB` es la fila `j` de `A` por la columna `k` de `B`, y se define así para que la matriz de una composición sea el producto de matrices, `M(ST) = M(S)M(T)`. No es conmutativo [@axler-2024, def. 3.41, 3.43, PDF pp. 91-92]. Si se aplica primero `M₁` y luego `M₂`, el resultado es `M₂M₁`: la última operación va a la izquierda [@watrous-2025, L1.1, p. 17].

**Para qué sirve en computación cuántica.** Cada operación sobre un estado cuántico es una aplicación lineal, es decir, multiplicar el vector de estado por una matriz `N×N` compleja [@de-wolf-2026, §1.2.3, p. 18]. Las **puertas cuánticas (quantum gates)** son esas matrices (ver [matrices unitarias y hermíticas](unitary-and-hermitian-matrices.md)), y un circuito es un producto de ellas.

## Comprensión {#layer-2}

**El producto exterior y las matrices como sumas de `|c⟩⟨d|`.** El **producto exterior (outer product)** `|b⟩⟨a|` es una columna por una fila: una matriz con un único 1 en la fila `b`, columna `a`. Por ejemplo `|0⟩⟨1| = [[0,1],[0,0]]` [@watrous-2025, L1.1, p. 15]. Como `⟨a|b⟩` vale 1 o 0, toda matriz es una suma de términos `|c⟩⟨d|`; una función determinista `f` es la matriz `Σ_a |f(a)⟩⟨a|` [@watrous-2025, L1.1, pp. 14-16]. Con `f` = NOT sale `X = |1⟩⟨0| + |0⟩⟨1|`. En general, la entrada `(a,b)` de `M` es `⟨a|M|b⟩` [@watrous-2025, L2.1, p. 47]. De Wolf define el producto exterior de `v` y `w` como `vw*` [@de-wolf-2026, App. A.3, p. 206].

**La no conmutatividad, con números.** Sea `H = (1/√2)[[1,1],[1,-1]]` y `X = [[0,1],[1,0]]`. Entonces `HX = (1/√2)[[1,1],[-1,1]]`, mientras que `XH = (1/√2)[[1,-1],[1,1]]`: no son iguales, así que el orden de las puertas importa [@axler-2024, def. 3.43, PDF p. 92; @watrous-2025, L1.1, pp. 17-18]. (Los productos son cálculo directo.)

**Dos formas equivalentes de aplicar una puerta.** Puedes multiplicar la matriz por el vector o usar la linealidad sobre la base estándar sin escribir la matriz (por ejemplo, calcular `T|+⟩` a partir de `T|0⟩` y `T|1⟩`) [@watrous-2025, L1.2, pp. 27-28].

**Transpuesta, conjugada y adjunta.** El **traspuesto conjugado** `A*` (los físicos escriben `A†`) traspone y conjuga cada entrada, y `(AB)* = B*A*` [@de-wolf-2026, App. A.2, p. 206; @watrous-2025, L3.2, p. 86]. La inversa invierte el orden: `(AC)⁻¹ = C⁻¹A⁻¹` [@axler-2024, §3D, PDF p. 109]. Con bases ortonormales, la matriz del adjunto es el traspuesto conjugado; con bases no ortonormales esto puede fallar [@axler-2024, def. 7.7, 7.9, PDF pp. 249-250].

**Isomorfismo entre aplicaciones y matrices.** Con bases fijas, `T ↔ M(T)` es un isomorfismo de `L(V,W)` en `F^{m,n}`, `M(Tv) = M(T)M(v)` y `dim L(V,W) = (dim V)(dim W)` [@axler-2024, 3.71, 3.72, PDF p. 105]. La matriz depende de las bases elegidas [@axler-2024, def. 3.31, PDF pp. 87-88].

**Error típico.** Confundir la aplicación con su matriz. Cambiar de base cambia la matriz, no la aplicación: si `A = M(T,(u))`, `B = M(T,(v))` y `C = M(I,(u),(v))`, entonces `A = C⁻¹BC` [@axler-2024, 3.84, PDF pp. 110-111]. Este cambio de base reaparece al diagonalizar (ver [valores y vectores propios](eigenvalues-and-eigenvectors.md)).

## Profesional {#layer-3}

**Herramientas de matrices que usan los profesionales.**

- **Traza (trace):** `Tr(A) = Σ A_ii`; es aditiva y cíclica (`Tr(AB) = Tr(BA)`), `Tr(A vv*) = v*Av`, es la suma de los valores propios y `Tr(A⊗B) = Tr(A)Tr(B)` [@de-wolf-2026, App. A.7, p. 209]. Con `A` y `v = |φ⟩` esa identidad dice `⟨φ|A|φ⟩ = Tr(A|φ⟩⟨φ|)`, y ya aparece como probabilidad de medida [@de-wolf-2026, §1.2.2, p. 16].
- **Rango (rank):** el tamaño del mayor conjunto de filas linealmente independientes; `rank(A) = rank(A*)` = número de valores singulares no nulos; `A` es invertible si y solo si tiene rango completo [@de-wolf-2026, App. A.8, p. 209].
- **Descomposición en valores singulares (SVD):** toda matriz, incluso no diagonalizable como `[[0,1],[0,0]]`, se escribe `A = UΣV⁻¹ = Σ σ_i u_i v_i*` [@de-wolf-2026, App. A.5, p. 208].
- **Bloques:** Watrous usa matrices por bloques, como `M = Σ_k |k⟩⟨0| ⊗ Π_k`, para construir unitarias que implementan medidas con un qubit auxiliar [@watrous-2025, L3.2, p. 89].

**Las matrices de Pauli como base de las matrices 2×2.** `I, X, Y, Z` son unitarias y hermíticas, con valores propios ±1; las no idénticas se anticonmutan y `Y = iXZ`. Son ortonormales respecto al producto de Hilbert-Schmidt `(1/d)Tr(A*B)`, de modo que toda matriz compleja 2×2 es `α₀I + α₁X + α₂Y + α₃Z`, con coeficientes reales si es hermítica [@de-wolf-2026, App. A.9, p. 210]. De `Y = iXZ` y las matrices anteriores sale `Y = [[0,-i],[i,0]]`.

**Cómo decidir la representación.**

- Matriz densa para pocos qubits y para verificar identidades a mano.
- Suma de productos exteriores `|c⟩⟨d|` cuando la matriz es dispersa o tiene estructura, p. ej. el "incremento módulo 8" `Σ_k |(k+1) mod 8⟩⟨k|`, cuya adjunta es la operación inversa [@watrous-2025, L2.1, pp. 45-46].
- Aplicación en forma de producto de matrices pequeñas (ver [producto tensorial](tensor-products.md)) cuando actúa sobre pocos qubits de un registro grande.

**Cuidado con el orden al leer un circuito.** El circuito se dibuja de izquierda a derecha [@de-wolf-2026, §2.1.2, p. 27 [15]; @watrous-2025, L3.1, PDF pp. 69-70], pero el producto de matrices se escribe de derecha a izquierda [@watrous-2025, L1.1, p. 17]. Y para sistemas de varios qubits, la matriz de una puerta controlada cambia si se intercambian control y objetivo [@watrous-2025, L2.1, pp. 44-45]. Las notas consultadas no cubren los aspectos numéricos (coste del producto de matrices, estabilidad).
