---
concept: probability-basics
title: "Probabilidad básica"
---

## Fundamentos {#layer-1}

Un estado **probabilístico (probabilistic)** de un sistema representa nuestro conocimiento sobre su estado clásico, y se escribe como un **vector de probabilidad (probability vector)**: entradas reales no negativas que suman 1. Para un bit, `Pr(0) = 3/4` y `Pr(1) = 1/4` es el vector `(3/4, 1/4)` [@watrous-2025, L1.1, pp. 11-12]. Al medir se ve un único estado clásico `a` y la descripción pasa a ser `|a⟩`; eso cambia nuestro conocimiento, no el sistema [@watrous-2025, L1.1, pp. 12-13].

**Operaciones.** Una operación probabilística es una **matriz estocástica (stochastic matrix)**: entradas no negativas y cada columna suma 1; son exactamente las matrices que siempre llevan vectores de probabilidad a vectores de probabilidad [@watrous-2025, L1.1, pp. 16-17]. Ejemplo: `[[1,1/2],[0,1/2]] = ½·identidad + ½·constante-0`, una elección aleatoria entre operaciones deterministas [@watrous-2025, L1.1, p. 17].

**El paralelo con lo cuántico.** El estado cuántico tiene la misma forma, pero con **amplitudes** complejas cuyos módulos al cuadrado suman 1 [@watrous-2025, L1.2, p. 18]. La medida en la base estándar da `a` con probabilidad `|⟨a|ψ⟩|²` (regla de Born), coherente porque esas probabilidades suman 1 para un vector unitario [@watrous-2025, L1.2, p. 23; L2.2, pp. 55-56]. Por eso aparecen aquí las probabilidades: la medida convierte amplitudes en un reparto de probabilidades sobre los estados clásicos [@de-wolf-2026, §1.2.2, p. 16].

**Ejemplo.** `|+⟩ = (|0⟩+|1⟩)/√2` da 0 con probabilidad `|1/√2|² = 1/2` y 1 con `1/2`; `|-⟩` da exactamente las mismas probabilidades, pese a ser otro estado [@watrous-2025, L1.2, pp. 23-24].

## Comprensión {#layer-2}

**Diferencia clave entre probabilidades y amplitudes.** Las probabilidades son no negativas y se suman; las amplitudes pueden tener signo o fase. Las fases no cambian las probabilidades de la base estándar, pero sí el estado: aplicando `H` y midiendo se distingue `|+⟩` de `|-⟩` con certeza [@watrous-2025, L1.2, p. 27]. Una matriz estocástica lleva probabilidades a probabilidades; una unitaria lleva amplitudes a amplitudes (ver [matrices unitarias y hermíticas](unitary-and-hermitian-matrices.md)). Composición: aplicar `M₁` y luego `M₂` es `M₂M₁`, también estocástica; el orden importa [@watrous-2025, L1.1, pp. 17-18].

**Variables aleatorias y esperanza.** Una variable aleatoria discreta `X` toma el valor `x_i` con probabilidad `p_i`; la esperanza es `E[X] = Σ p_i x_i`, la varianza `Var[X] = E[(X-E[X])²] = E[X²] - E[X]²` y `σ` la desviación típica. La esperanza es lineal: `E[Σ a_j X_j] = Σ a_j E[X_j]`; para independientes, `E[XY] = E[X]E[Y]` [@de-wolf-2026, App. B.2, p. 212]. La esperanza del resultado de un observable `M` es `Tr(M|φ⟩⟨φ|)` [@de-wolf-2026, §1.2.2, p. 17].

**Estados conjuntos, marginales y condicionados.**

- Un estado probabilístico de `(X,Y)` asigna una probabilidad a cada par; `½|00⟩ + ½|11⟩` tiene bits correlados (siempre iguales) [@watrous-2025, L2.1, pp. 34-35].
- **Independencia:** `Pr((X,Y)=(a,b)) = Pr(X=a)Pr(Y=b)`, equivalente a que el vector conjunto sea un producto tensorial. La correlación es la falta de independencia [@watrous-2025, L2.1, pp. 35-37]. Ver [producto tensorial](tensor-products.md).
- **Marginal:** `Pr(X=a) = Σ_b Pr((a,b))`. Es obligado: si no, medir `Y` cambiaría las estadísticas de `X` y permitiría señalizar más rápido que la luz [@watrous-2025, L2.1, p. 41].
- **Condicionada:** `Pr(Y=b | X=a) = Pr((a,b))/Pr(X=a)`; en el vector, se toma la parte correspondiente a `a` y se normaliza por la suma de sus entradas. Ejemplo: `Pr(X=0) = 7/12` y `Y|X=0 = 6/7|1⟩ + 1/7|3⟩` [@watrous-2025, L2.1, pp. 41-43].
- La medida parcial cuántica hace lo análogo, normalizando por la norma en lugar de por la suma [@watrous-2025, L2.2, pp. 55-57].

**Error típico.** Pensar que las amplitudes *son* probabilidades. Son sus raíces "con fase": la probabilidad es `|α|²`, y la fase carga información que la probabilidad borra.

**Independencia de operaciones.** Dos operaciones independientes `M` sobre `X` y `N` sobre `Y` se combinan como `M⊗N`, y el producto tensorial de matrices estocásticas es estocástico [@watrous-2025, L2.1, pp. 44-49].

## Profesional {#layer-3}

Las medidas cuánticas son aleatorias y los algoritmos se diseñan para que la respuesta correcta tenga probabilidad alta. Las siguientes herramientas, de los apéndices de De Wolf, son las que se usan para analizar y reducir el error.

**Cota de la unión (union bound).** `Pr[A∨B] ≤ Pr[A] + Pr[B]`, y para `T` sucesos `Pr[A₁∨…∨A_T] ≤ Σ Pr[A_i]` [@de-wolf-2026, App. B.2, p. 212]. Si `T` subrutinas aleatorias fallan cada una con probabilidad `≤ 1/(3T)`, la probabilidad de que ninguna falle es `≥ 2/3` aunque los fallos sean dependientes [@de-wolf-2026, App. B.2, p. 213].

**Desigualdades de cola.** Markov: `Pr[X ≥ kμ] ≤ 1/k` para `X` no negativa. Chebyshev: `Pr[|X-μ| ≥ kσ] ≤ 1/k²`. Chernoff/Hoeffding: para una suma de `n` variables `{0,1}` i.i.d. con media `np`, `Pr[|X-μ| ≥ αn] ≤ 2e^{-2α²n}` [@de-wolf-2026, App. B.2, p. 213].

**Convención de error.** "Probabilidad de error `≤ 1/3`" se entiende en el peor caso sobre todas las entradas: acierta con probabilidad `≥ 2/3` sobre las monedas y/o medidas cuánticas [@de-wolf-2026, App. B.2, p. 213].

**Reducción del error por repetición.** Para un algoritmo con salida 0/1 y error `≤ 1/3`, se ejecuta `n = O(log(1/ε))` veces (con `n` impar) con aleatoriedad fresca y se vota por mayoría; Chernoff da error `≤ ε` [@de-wolf-2026, App. B.2, p. 213]. Con `α = 1/6`, `2e^{-2α²n} = 2e^{-n/18} ≤ ε` se cumple para `n ≥ 18 ln(2/ε)` (despeje propio de la desigualdad citada). En la práctica se repite un circuito muchas veces ("shots") y cada ejecución se trata como una muestra independiente [unverified].

**Tiempo esperado frente a peor caso.** Un tiempo esperado `T` se convierte en un algoritmo de tiempo `3T` en el peor caso y error `≤ 1/3` cortando a los `3T` pasos, por Markov [@de-wolf-2026, App. B.2, p. 213].

**Desigualdades auxiliares.** `1 + x ≤ e^x` para todo real `x`; para `ε_j ∈ [0,1]`, `1 - Σε_j ≤ Π(1-ε_j) ≤ e^{-Σε_j}` [@de-wolf-2026, App. B.1, p. 212].

**Matices que conviene recordar.**

- Las probabilidades de una medida tienen la forma `⟨φ|P_j|φ⟩ = ‖P_j|φ⟩‖² = Tr(P_j|φ⟩⟨φ|)` para proyectores [@de-wolf-2026, §1.2.2, p. 16]; el caso estándar es `|α_j|²`.
- El argumento de no clonación también vale para estados probabilísticos: clonar un estado desconocido no es lineal y ninguna matriz estocástica lo hace [@watrous-2025, L3.3, pp. 94-95].
- Distintos observadores pueden tener vectores de probabilidad distintos del mismo sistema, porque el vector describe conocimiento [@watrous-2025, L1.1, pp. 12-13].

La estimación de probabilidades a partir de un número finito de shots se trata en el ámbito de [programación con Qiskit](../../qiskit-programming/index.md).
