---
concept: unitary-and-hermitian-matrices
title: "Matrices unitarias y hermíticas"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
Las puertas cuánticas son matrices **unitarias (unitary)**, que conservan la norma; las magnitudes medibles se representan con matrices **hermíticas (Hermitian)** [@watrous-2025, L1.2, p. 25; @de-wolf-2026, §1.2.2, p. 17].

### Explicación
`U` es unitaria si `U U† = I` y `U† U = I`, es decir `U† = U⁻¹`; para matrices cuadradas las dos condiciones son equivalentes [@watrous-2025, L1.2, pp. 24-25]. (`U†` es el traspuesto conjugado, de [matrices y aplicaciones lineales](matrices-and-linear-maps.md).) De forma equivalente, `U` conserva la norma de todos los vectores, `‖U|ψ⟩‖ = ‖ψ‖`: las unitarias son exactamente las aplicaciones lineales que llevan vectores de estado cuánticos a vectores de estado cuánticos, igual que las matrices estocásticas lo hacen con vectores de probabilidad [@watrous-2025, L1.2, p. 25].

Por eso una puerta es unitaria: debe conservar la norma del vector de amplitudes, de modo que las probabilidades sigan sumando 1. Además toda unitaria es invertible, así que las operaciones cuánticas son reversibles, a diferencia de la medida [@de-wolf-2026, §1.2.3, p. 19].

`A` es hermítica si `A = A†` [@watrous-2025, L3.2, pp. 85-86]; Axler las llama autoadjuntas (self-adjoint) [@axler-2024, def. 7.10, PDF p. 251]. En la práctica, las matrices hermíticas representan magnitudes medibles (observables) [@de-wolf-2026, §1.2.2, p. 17].

Las dos propiedades son independientes: una matriz puede tener una, otra o ambas.

### Ejemplo
- La puerta de Hadamard `H = (1/√2)[[1,1],[1,-1]]` es unitaria: `H†H = I`, que Watrous verifica a mano [@watrous-2025, L1.2, pp. 25-26]. Actúa como `H|0⟩ = |+⟩`, `H|1⟩ = |-⟩`, `H|+⟩ = |0⟩`, `H|-⟩ = |1⟩` [@watrous-2025, L1.2, p. 27]. `H` también es hermítica, así que `H² = I`.
- `X` (NOT), `Y`, `Z` y la identidad son a la vez unitarias y hermíticas [@de-wolf-2026, App. A.9, p. 210]. `Z = diag(1,-1)` cumple `Z|1⟩ = -|1⟩` [@watrous-2025, L1.2, pp. 25-26].
- `S = diag(1, i)` es unitaria pero **no** hermítica: su traspuesto conjugado es `diag(1, -i)`, distinto de `S`.

### Para seguir
[Valores y vectores propios](eigenvalues-and-eigenvectors.md) explica qué dicen estas matrices sobre direcciones y resultados de medida. La capa 2 de este concepto da cuatro caracterizaciones de unitaria y presenta los proyectores.

## Comprensión {#layer-2}

### Idea clave
Una matriz es unitaria si y solo si sus columnas (o sus filas) forman una base ortonormal, y los proyectores hermíticos definen la medida proyectiva [@watrous-2025, L3.2, pp. 83-87].

### Explicación
Para una matriz cuadrada `U` son equivalentes: es unitaria; sus columnas forman una base ortonormal; sus filas forman una base ortonormal [@watrous-2025, L3.2, pp. 83-85]; conserva los productos interiores y por tanto las normas [@de-wolf-2026, App. A.4, p. 206; @axler-2024, def. 7.51, 7.53, PDF pp. 278-279]. La prueba mira `U†U` como la matriz de productos interiores de las columnas. Consecuencia útil: cualquier conjunto ortonormal de `m` vectores en dimensión `n` puede ser las primeras `m` columnas de alguna unitaria [@watrous-2025, L3.2, pp. 83-85].

Una isometría conserva la norma (y es inyectiva); es unitaria si además es invertible, y para matrices no cuadradas `M†M = I` no implica `MM† = I` [@axler-2024, def. 7.44, 7.49, PDF pp. 276-277; @watrous-2025, L1.2, pp. 24-25].

Los valores propios distinguen las dos familias. Los de una unitaria tienen módulo 1 [@axler-2024, 7.54, PDF p. 280]; los de una hermítica son reales, pues `λ‖v‖² = ⟨Tv,v⟩ = ⟨v,Tv⟩ = conj(λ)‖v‖²` [@axler-2024, 7.12, PDF p. 251]. La analogía es: número complejo ↔ operador; conjugado ↔ adjunto; real ↔ autoadjunto; circunferencia unidad ↔ unitario [@axler-2024, §7D, PDF p. 280]. Ver [valores y vectores propios](eigenvalues-and-eigenvectors.md).

Ambas son casos de las matrices normales: `A` es normal si `AA* = A*A`, y las unitarias y las hermíticas lo son, pero no al revés: `[[2,-3],[3,2]]` es normal y no autoadjunta [@axler-2024, def. 7.18, 7.19, PDF pp. 253-255; @de-wolf-2026, App. A.5, p. 207].

Entre las hermíticas destacan los proyectores. Una proyección es una matriz hermítica e idempotente (`Π² = Π`); `|ψ⟩⟨ψ|` con `‖ψ‖ = 1` lo es, y también cualquier suma de `|ψ_k⟩⟨ψ_k|` sobre un conjunto ortonormal [@watrous-2025, L3.2, pp. 85-86]. Sus valores propios son 0 o 1 [@de-wolf-2026, App. A.5, p. 208].

Una medida proyectiva es un conjunto de proyectores `Π_a` que suman `I`. El resultado `a` tiene probabilidad `‖Π_a|ψ⟩‖²` y el estado pasa a `Π_a|ψ⟩/‖Π_a|ψ⟩‖`; medir en la base estándar es el caso `Π_a = |a⟩⟨a|` [@watrous-2025, L3.2, p. 87; @de-wolf-2026, §1.2.2, p. 16].

### Ejemplo
Medida proyectiva en la base estándar con `Π_0 = |0⟩⟨0|` y `Π_1 = |1⟩⟨1|` sobre `|+⟩`: `Π_0|+⟩ = |0⟩/√2`, de norma `1/√2`, así que el resultado 0 tiene probabilidad `1/2` y el estado pasa a `|0⟩` (cálculo directo con la fórmula citada) [@watrous-2025, L3.2, p. 87].

### Errores frecuentes
- *"Las puertas cuánticas son hermíticas."* Algunas lo son (Pauli, Hadamard), pero la propiedad general es la unitaridad; `S` y `T` no son hermíticas.
- *"Unitaria y estocástica son lo mismo."* Una matriz unitaria y estocástica a la vez es exactamente una matriz de permutación [@watrous-2025, L1.2, p. 29].

### Para seguir
La capa 3 usa el teorema espectral para observables y para `e^{-iHt}`. Antes, [valores y vectores propios](eigenvalues-and-eigenvectors.md) construye esas ideas desde cero.

## Profesional {#layer-3}

### Idea clave
El teorema espectral hace que unitarias y hermíticas sean diagonalizables en una base ortonormal; de él salen los observables y la evolución `U = e^{-iHt}` [@axler-2024, 7.31, PDF p. 264; @de-wolf-2026, §9.1, p. 83].

### Explicación
Axler considera el teorema espectral probablemente la herramienta más útil para operadores en espacios con producto interior [@axler-2024, §7B, PDF p. 261]. En versión compleja: `T` es normal si y solo si hay una base ortonormal de vectores propios, es decir, es diagonal en alguna base ortonormal [@axler-2024, 7.31, PDF p. 264]. Para hermíticas, los valores propios son reales [@de-wolf-2026, App. A.5, p. 208]. Para unitarias, hay una base ortonormal de vectores propios con valores propios de módulo 1 [@axler-2024, 7.55, PDF p. 280].

Un observable `M = Σ λ_i P_i` (valores reales distintos) es hermítico y su valor esperado es `Tr(M|φ⟩⟨φ|)`; todo hermítico tiene descomposición espectral, de modo que los observables corresponden uno a uno con las matrices hermíticas. `Z = |0⟩⟨0| - |1⟩⟨1|` es el observable de la base computacional [@de-wolf-2026, §1.2.2, p. 17]. Ver [valores y vectores propios](eigenvalues-and-eigenvectors.md).

Con la descomposición espectral se obtienen puertas a partir de hamiltonianos. Si `A` es hermítica, `e^{-iA}` es unitaria [@de-wolf-2026, nota 1, §9.1, p. 83]. La evolución temporal bajo un hamiltoniano `H` independiente del tiempo es `U = e^{-iHt}` aplicada al estado inicial, y la simulación hamiltoniana consiste en encontrar un circuito pequeño que aproxime `e^{iHt}` con error `ε` [@de-wolf-2026, §9.1, pp. 83-84].

Otras construcciones útiles: una unitaria sobre el sistema más un auxiliar puede implementar cualquier medida proyectiva, completando `M = Σ_k |k⟩⟨0| ⊗ Π_k` hasta una unitaria [@watrous-2025, L3.2, pp. 88-91]. Y no existe una unitaria que clone un estado desconocido, porque clonar no es lineal [@watrous-2025, L3.3, pp. 93-94].

### Ejemplo
`Z = |0⟩⟨0| - |1⟩⟨1|` da `e^{-iZt} = diag(e^{-it}, e^{it})`, que salvo fase global es una puerta de fase `P_{2t}` (aplicando `f(A) = Σ f(λ_j)|a_j⟩⟨a_j|`).

Otros casos concretos: `R = HSH` cumple `R² = X`, una raíz cuadrada de NOT que no existe con un bit clásico [@watrous-2025, L1.2, pp. 28-29]. La matriz de la transformada de Fourier de 4 puntos `(1/2)[[1,1,1,1],[1,i,-1,-i],[1,-1,1,-1],[1,-i,-1,i]]` es unitaria y desempeña un papel clave en algoritmos [@watrous-2025, L1.2, p. 29].

### Las fuentes discrepan
En Axler, `A*` es la adjunta; en física `A†`. Con bases no ortonormales, la matriz del adjunto no es el traspuesto conjugado [@axler-2024, def. 7.9, PDF p. 250]. Axler no usa el término "hermítica" en lo leído y "matriz unitaria" solo aparece en §7D [@axler-2024, def. 7.56, PDF p. 281].

### Para seguir
[Valores y vectores propios](eigenvalues-and-eigenvectors.md), capa 3, desarrolla la descomposición espectral y las funciones de matrices.
