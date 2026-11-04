---
concept: matrices-and-linear-maps
title: "Matrices y aplicaciones lineales"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
Una **matriz (matrix)** anota una aplicación lineal una vez elegidas las bases. En computación cuántica, cada operación sobre un estado es multiplicar su vector por una matriz compleja [@axler-2024, def. 3.31, PDF pp. 87-88; @de-wolf-2026, §1.2.3, p. 18].

### Explicación
Una **aplicación lineal (linear map)** `T` es una función entre espacios vectoriales que es aditiva y homogénea: `T(u+v) = Tu + Tv` y `T(λv) = λTv`. Un **operador (operator)** es una aplicación lineal de un espacio en sí mismo [@axler-2024, def. 3.1-3.3, PDF pp. 70-71].

La columna `k` de la matriz contiene el resultado de aplicar `T` al `k`-ésimo vector de la base; para `F^n → F^m` con bases estándar, es `T` aplicada al `k`-ésimo vector estándar [@axler-2024, def. 3.31, PDF pp. 87-88]. Basta saber qué hace `T` con una base para saberlo todo [@axler-2024, §3C, PDF p. 87].

El producto de matrices se define para que la matriz de una composición sea el producto: la entrada `(j,k)` de `AB` es la fila `j` de `A` por la columna `k` de `B`, y `M(ST) = M(S)M(T)`. No es conmutativo [@axler-2024, def. 3.41, 3.43, PDF pp. 91-92]. Si se aplica primero `M₁` y luego `M₂`, el resultado es `M₂M₁`: la última operación va a la izquierda [@watrous-2025, L1.1, p. 17].

Las **puertas cuánticas (quantum gates)** son esas matrices (ver [matrices unitarias y hermíticas](unitary-and-hermitian-matrices.md)), y un circuito es un producto de ellas [@de-wolf-2026, §1.2.3, p. 18].

### Ejemplo
Sea `S = diag(1, i) = [[1,0],[0,i]]`. Aplicada a `|+⟩ = (1/√2, 1/√2)ᵀ`: `S|+⟩ = (1/√2, i/√2)ᵀ`. La primera entrada se multiplica por 1 y la segunda por `i`. `S` es la puerta de fase `P_{π/2}` [@watrous-2025, L1.2, p. 26].

### Para seguir
[Matrices unitarias y hermíticas](unitary-and-hermitian-matrices.md) estudia las matrices que sirven de puertas. La capa 2 de este concepto añade el producto exterior y el cambio de base.

## Comprensión {#layer-2}

### Idea clave
Toda matriz es una suma de productos exteriores `|c⟩⟨d|`, y la matriz depende de la base elegida pero la aplicación no: cambiar de base cambia la matriz, no la aplicación [@watrous-2025, L1.1, pp. 14-16; @axler-2024, 3.84, PDF pp. 110-111].

### Explicación
El **producto exterior (outer product)** `|b⟩⟨a|` es una columna por una fila: una matriz con un único 1 en la fila `b`, columna `a`. Por ejemplo `|0⟩⟨1| = [[0,1],[0,0]]` [@watrous-2025, L1.1, p. 15]. Como `⟨a|b⟩` vale 1 o 0, toda matriz es una suma de términos `|c⟩⟨d|`; una función determinista `f` es la matriz `Σ_a |f(a)⟩⟨a|` [@watrous-2025, L1.1, pp. 14-16]. En general, la entrada `(a,b)` de `M` es `⟨a|M|b⟩` [@watrous-2025, L2.1, p. 47]. De Wolf define el producto exterior de `v` y `w` como `vw*` [@de-wolf-2026, App. A.3, p. 206].

Hay dos formas equivalentes de aplicar una puerta: multiplicar la matriz por el vector o usar la linealidad sobre la base estándar sin escribir la matriz (por ejemplo, calcular `T|+⟩` a partir de `T|0⟩` y `T|1⟩`) [@watrous-2025, L1.2, pp. 27-28].

La adjunta de una matriz respeta el orden del producto al revés. El **traspuesto conjugado** `A*` (los físicos escriben `A†`) traspone y conjuga cada entrada, y `(AB)* = B*A*` [@de-wolf-2026, App. A.2, p. 206; @watrous-2025, L3.2, p. 86]. Igual la inversa: `(AC)⁻¹ = C⁻¹A⁻¹` [@axler-2024, §3D, PDF p. 109]. Con bases ortonormales, la matriz del adjunto es el traspuesto conjugado; con bases no ortonormales esto puede fallar [@axler-2024, def. 7.7, 7.9, PDF pp. 249-250].

La relación entre aplicaciones y matrices es un isomorfismo: con bases fijas, `T ↔ M(T)` lleva `L(V,W)` en `F^{m,n}`, `M(Tv) = M(T)M(v)` y `dim L(V,W) = (dim V)(dim W)` [@axler-2024, 3.71, 3.72, PDF p. 105]. La matriz depende de las bases elegidas [@axler-2024, def. 3.31, PDF pp. 87-88].

Por eso conviene no confundir la aplicación con su matriz: si `A = M(T,(u))`, `B = M(T,(v))` y `C = M(I,(u),(v))`, entonces `A = C⁻¹BC` [@axler-2024, 3.84, PDF pp. 110-111]. Este cambio de base reaparece al diagonalizar (ver [valores y vectores propios](eigenvalues-and-eigenvectors.md)).

### Ejemplo
Con `f` = NOT sale `X = |1⟩⟨0| + |0⟩⟨1|` [@watrous-2025, L1.1, pp. 14-16].

La no conmutatividad, con números. Sea `H = (1/√2)[[1,1],[1,-1]]` y `X = [[0,1],[1,0]]`. Entonces `HX = (1/√2)[[1,1],[-1,1]]`, mientras que `XH = (1/√2)[[1,-1],[1,1]]`: no son iguales, así que el orden de las puertas importa [@axler-2024, def. 3.43, PDF p. 92; @watrous-2025, L1.1, pp. 17-18]. (Los productos son cálculo directo.)

### Errores frecuentes
- *"Una aplicación y su matriz son lo mismo."* La matriz depende de las bases; la aplicación, no.

### Para seguir
La capa 3 reúne las herramientas que usan los profesionales (traza, rango, SVD, Pauli). Mientras, [matrices unitarias y hermíticas](unitary-and-hermitian-matrices.md) pasa a las matrices que importan en lo cuántico.

## Profesional {#layer-3}

### Idea clave
Los profesionales manejan las matrices con traza, rango, valores singulares y la base de Pauli, y eligen la representación (densa, suma de productos exteriores o producto de matrices pequeñas) según la estructura del problema [@de-wolf-2026, App. A.5, A.7-A.9].

### Explicación
Herramientas de matrices de uso diario:

- **Traza (trace):** `Tr(A) = Σ A_ii`; es aditiva y cíclica (`Tr(AB) = Tr(BA)`), `Tr(A vv*) = v*Av`, es la suma de los valores propios y `Tr(A⊗B) = Tr(A)Tr(B)` [@de-wolf-2026, App. A.7, p. 209]. Con `v = |φ⟩` esa identidad dice `⟨φ|A|φ⟩ = Tr(A|φ⟩⟨φ|)`, y ya aparece como probabilidad de medida [@de-wolf-2026, §1.2.2, p. 16].
- **Rango (rank):** el tamaño del mayor conjunto de filas linealmente independientes; `rank(A) = rank(A*)` = número de valores singulares no nulos; `A` es invertible si y solo si tiene rango completo [@de-wolf-2026, App. A.8, p. 209].
- **Descomposición en valores singulares (SVD):** toda matriz, incluso no diagonalizable como `[[0,1],[0,0]]`, se escribe `A = UΣV⁻¹ = Σ σ_i u_i v_i*` [@de-wolf-2026, App. A.5, p. 208].
- **Bloques:** Watrous usa matrices por bloques, como `M = Σ_k |k⟩⟨0| ⊗ Π_k`, para construir unitarias que implementan medidas con un qubit auxiliar [@watrous-2025, L3.2, p. 89].

Las matrices de Pauli forman una base de las matrices 2×2. `I, X, Y, Z` son unitarias y hermíticas, con valores propios ±1; las no idénticas se anticonmutan y `Y = iXZ`. Son ortonormales respecto al producto de Hilbert-Schmidt `(1/d)Tr(A*B)`, de modo que toda matriz compleja 2×2 es `α₀I + α₁X + α₂Y + α₃Z`, con coeficientes reales si es hermítica [@de-wolf-2026, App. A.9, p. 210].

La representación se elige así:

- Matriz densa para pocos qubits y para verificar identidades a mano.
- Suma de productos exteriores `|c⟩⟨d|` cuando la matriz es dispersa o tiene estructura, como el "incremento módulo 8" `Σ_k |(k+1) mod 8⟩⟨k|`, cuya adjunta es la operación inversa [@watrous-2025, L2.1, pp. 45-46].
- Producto de matrices pequeñas (ver [producto tensorial](tensor-products.md)) cuando la puerta actúa sobre pocos qubits de un registro grande.

Al leer un circuito hay que cuidar el orden. El circuito se dibuja de izquierda a derecha [@de-wolf-2026, §2.1.2, p. 27 [15]; @watrous-2025, L3.1, PDF pp. 69-70], pero el producto de matrices se escribe de derecha a izquierda [@watrous-2025, L1.1, p. 17]. Y para varios qubits, la matriz de una puerta controlada cambia si se intercambian control y objetivo [@watrous-2025, L2.1, pp. 44-45].

### Ejemplo
De `Y = iXZ` y las matrices anteriores sale `Y = [[0,-i],[i,0]]`, con lo que `I, X, Y, Z` quedan escritas explícitamente [@de-wolf-2026, App. A.9, p. 210].

### Las fuentes discrepan
Las notas consultadas no cubren los aspectos numéricos (coste del producto de matrices, estabilidad).

### Para seguir
[Matrices unitarias y hermíticas](unitary-and-hermitian-matrices.md), capa 3, usa estas herramientas con el teorema espectral.
