---
concept: eigenvalues-and-eigenvectors
title: "Valores y vectores propios"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
Un **vector propio (eigenvector)** de `A` es un vector no nulo que `A` no gira, solo lo estira o cambia su fase: `Av = λv`. El escalar `λ` es el **valor propio (eigenvalue)** [@de-wolf-2026, App. A.5, p. 207].

### Explicación
Se excluye `v = 0` porque `T0 = λ0` para cualquier `λ`; los vectores propios de `λ` son los elementos no nulos de `null(T - λI)` [@axler-2024, def. 5.5, 5.8, PDF pp. 152-153]. El conjunto de valores propios es el **espectro (spectrum)** [@de-wolf-2026, App. A.5, p. 207]. La motivación es estudiar un operador restringiéndolo a subespacios invariantes; uno de dimensión 1, `span(v)`, significa `Tv = λv` [@axler-2024, §5A, PDF p. 152].

Diagonalizar significa escribir la matriz en una base de vectores propios; entonces es diagonal y las entradas son los valores propios [@axler-2024, 5.48-5.51, PDF p. 181].

En computación cuántica los resultados posibles de medir un observable son sus valores propios, y los estados que dan un resultado con certeza son sus vectores propios. También las unitarias tienen valores propios de módulo 1, que son fases [@de-wolf-2026, §1.2.2, p. 17; App. A.4, p. 207]. La física detrás se explica en el ámbito de mecánica cuántica.

### Ejemplo
Puertas de un qubit:

- `Z = diag(1,-1)`: `Z|0⟩ = |0⟩` (valor propio `+1`) y `Z|1⟩ = -|1⟩` (valor propio `-1`) [@watrous-2025, L1.2, pp. 25-26].
- `X = [[0,1],[1,0]]`: `X|+⟩ = |+⟩` (valor `+1`) y `X|-⟩ = -|-⟩` (valor `-1`). Se comprueba multiplicando.
- Las matrices de Pauli tienen valores propios ±1 [@de-wolf-2026, App. A.9, p. 210].

Con un estado de dos qubits: `|φ⟩ = (|00⟩+|11⟩)/√2` queda intacto al medir `Z⊗Z` porque es un vector propio de valor `+1` [@de-wolf-2026, §1.2.2, p. 17].

### Errores frecuentes
- *"Un valor propio cero significa que el vector propio es cero."* El vector propio nunca es nulo; el valor propio sí puede serlo.

### Para seguir
[Producto tensorial](tensor-products.md) explica cómo se combinan varios sistemas. La capa 2 de este concepto responde por qué existen los valores propios y cuándo se puede diagonalizar.

## Comprensión {#layer-2}

### Idea clave
Sobre `C`, todo operador de un espacio de dimensión finita no nulo tiene algún valor propio, pero no todo operador es diagonalizable; los normales son exactamente los unitariamente diagonalizables [@axler-2024, 5.19, PDF p. 161; @de-wolf-2026, App. A.5, p. 207].

### Explicación
La existencia se demuestra considerando la lista `v, Tv, …, Tⁿv`, que debe ser dependiente, y usando el teorema fundamental del álgebra, sin determinantes [@axler-2024, 5.19, PDF p. 161; prefacio, PDF p. 14]. Sobre `R` falla: la rotación de 90 grados en `R²` no tiene valores propios reales, pero sobre `C` tiene `i` y `-i` [@axler-2024, 5.9, PDF p. 153]. Esa es una razón más para trabajar con complejos (ver [números complejos](complex-numbers.md)). La dimensión finita es necesaria [@axler-2024, 5.20, PDF p. 161].

Resultados básicos:

- En dimensión finita, `λ` es valor propio si y solo si `T - λI` no es inyectiva, ni sobreyectiva, ni invertible [@axler-2024, 5.7, PDF p. 153].
- Vectores propios de valores propios distintos son linealmente independientes; hay como mucho `dim V` valores propios distintos [@axler-2024, 5.11, 5.12, PDF p. 154].
- El **espacio propio (eigenspace)** es `E(λ,T) = null(T-λI)`; los de valores distintos forman una suma directa [@axler-2024, 5.52, 5.54, PDF p. 182].
- Matrices semejantes (`A = SBS⁻¹`) comparten valores propios; los valores propios de `A*` son los conjugados de los de `A` [@de-wolf-2026, App. A.5, pp. 207-208].

Una matriz es diagonalizable cuando `A = SDS⁻¹`, y eso ocurre si y solo si tiene `d` vectores propios linealmente independientes, que son las columnas de `S` [@de-wolf-2026, App. A.5, pp. 207-208]. Equivalencias: `V` tiene base de vectores propios; `V` es suma directa de los espacios propios; las dimensiones de estos suman `dim V` [@axler-2024, 5.55, PDF p. 183]. Si hay `dim V` valores distintos, es diagonalizable [@axler-2024, 5.58, PDF p. 184].

No todo operador lo es. `T(a,b,c) = (b,c,0)` solo tiene el valor propio 0 y un espacio propio de dimensión 1 [@axler-2024, 5.57, PDF p. 184]; `[[0,1],[0,0]]` es otro ejemplo [@de-wolf-2026, App. A.5, p. 208]. Sí es cierto que sobre `C` todo operador es triangular superior en alguna base (Schur) [@axler-2024, 5.47, PDF p. 178].

Diagonalizable tampoco es lo mismo que unitariamente diagonalizable: una matriz es normal si y solo si es unitariamente diagonalizable, y `[[1,1],[0,2]]` se puede diagonalizar, pero no con una unitaria [@de-wolf-2026, App. A.5, p. 207]. Esto conecta con [matrices unitarias y hermíticas](unitary-and-hermitian-matrices.md): los vectores propios de un operador normal con valores propios distintos son ortogonales [@axler-2024, 7.22, PDF p. 256].

### Ejemplo
La matriz normal `[[2,-3],[3,2]]` tiene base ortonormal de vectores propios `(i,1)/√2` y `(-i,1)/√2` con valores `2+3i` y `2-3i`; no es autoadjunta, y por eso sus valores no son reales [@axler-2024, ex. 7.33, PDF p. 265].

### Errores frecuentes
- *"Toda matriz se puede diagonalizar."* `[[0,1],[0,0]]` no se puede.
- *"Diagonalizable y unitariamente diagonalizable son lo mismo."* `[[1,1],[0,2]]` es diagonalizable, pero no con una unitaria.

### Para seguir
La capa 3 convierte esto en la descomposición espectral y en las funciones de matrices como `e^{-iHt}`.

## Profesional {#layer-3}

### Idea clave
Si `A` es unitariamente diagonalizable, `A = Σ λ_i |v_i⟩⟨v_i|`: la descomposición espectral conecta el álgebra lineal con la medida, y permite calcular funciones de matrices como `e^{-iHt}` [@de-wolf-2026, App. A.5, p. 207; §9.1, p. 83].

### Explicación
Si `A` es unitariamente diagonalizable, `A = UDU⁻¹ = Σ λ_i |v_i⟩⟨v_i|`, y eso ocurre exactamente cuando hay `d` vectores propios ortonormales [@de-wolf-2026, App. A.5, p. 207; App. A.10, p. 210]. Los proyectores `|v_i⟩⟨v_i|` definen una medida proyectiva cuyos resultados son los `λ_i` [@de-wolf-2026, §1.2.2, p. 17].

Para una matriz normal, aplicar una función `f` es aplicarla a los valores propios: si `A = VDV⁻¹` entonces `f(A) = Vf(D)V⁻¹`, y con `A = Σ λ_j a_j a_j*`, `e^{-iA} = Σ e^{-iλ_j} a_j a_j*`. Si `A` es hermítica, `e^{-iA}` es unitaria [@de-wolf-2026, nota 1, §9.1, p. 83]. Con esto, la evolución bajo un hamiltoniano `H` es `e^{-iHt}`, solución de la ecuación de Schrödinger con `ℏ = 1` [@de-wolf-2026, §9.1, p. 83]. Encontrar un circuito pequeño a distancia `ε` de `e^{iHt}` es una tarea algorítmica por derecho propio, que se trata en [simulación de hamiltonianos](../../quantum-algorithms/concepts/hamiltonian-simulation.md) [@de-wolf-2026, §9.1, p. 84].

La traza es la suma de los valores propios [@de-wolf-2026, App. A.7, p. 209]. La SVD cubre las matrices que no se diagonalizan [@de-wolf-2026, App. A.5, p. 208].

Para decidir qué aplicar:

- Matriz hermítica o unitaria (observable, puerta, hamiltoniano): usar siempre la descomposición espectral ortonormal.
- Matriz arbitraria no normal: sus valores propios no dicen todo sobre cómo actúa; usa SVD o Schur [@de-wolf-2026, App. A.5, pp. 207-208].

### Ejemplo
Con los valores propios ±1 vistos en la capa 1: `X = |+⟩⟨+| - |-⟩⟨-|` y `Z = |0⟩⟨0| - |1⟩⟨1|` [@de-wolf-2026, §1.2.2, p. 17].

Evolución bajo un hamiltoniano `H`, en tres pasos:

1. Hallar los valores propios `E_j` y vectores propios ortonormales `|a_j⟩` de `H`.
2. `e^{-iHt} = Σ e^{-iE_j t}|a_j⟩⟨a_j|`: cada componente gira su fase a velocidad `E_j`.
3. Para un estado inicial `|ψ⟩ = Σ c_j|a_j⟩`, resulta `Σ c_j e^{-iE_j t}|a_j⟩`.

Los pasos 2-3 son aplicación directa de la fórmula anterior (cálculo propio).

### Para seguir
[Producto tensorial](tensor-products.md), capa 3, trata el orden de los qubits en Qiskit y las puertas multiqubit.
