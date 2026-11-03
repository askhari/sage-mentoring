---
concept: unitary-time-evolution
title: "Evolución temporal unitaria (ecuación de Schrödinger)"
---

## Comprensión {#layer-2}

**El postulado de la dinámica.** Para un sistema cerrado, el estado evoluciona con un operador unitario: `|ψ(t')⟩ = U(t',t)|ψ(t)⟩` (imagen de Schrödinger) [@preskill-ph219, ch.2 §2.1, p. 6]. Zwiebach lo postula igual: existe un `U(t,t₀)` unitario, igual para todos los estados iniciales y único [@zwiebach-mit-8-05, ch.6 §2.1, p. 10]. Unitaria significa `U†U = 1`, y eso conserva la norma del estado [@zwiebach-mit-8-05, ch.6 §2.1, pp. 10-11]; ya conoces estas matrices en [matrices unitarias y hermíticas](../../math-foundations/concepts/unitary-and-hermitian-matrices.md). Propiedades: `U(t₀,t₀) = 1`, composición `U(t₂,t₀) = U(t₂,t₁)U(t₁,t₀)` e inversa `U(t₀,t) = U†(t,t₀)` [@zwiebach-mit-8-05, ch.6 §2.1, pp. 11-12].

**Por qué importa en computación cuántica.** Las puertas cuánticas son operaciones unitarias: Watrous las define como las matrices que conservan la norma [@watrous-2025, L1.2, PDF p. 25]. Por eso un circuito sin medidas es una unitaria total, reversible. La física dice cómo se consigue una puerta: se enciende un hamiltoniano durante un tiempo (ver abajo).

**La ecuación de Schrödinger.** Es la forma diferencial: `iħ ∂|Ψ⟩/∂t = H|Ψ⟩` con `H` hermítico y con unidades de energía [@zwiebach-mit-8-05, ch.6 §2.2, p. 14]; con `ħ = 1`, `d|ψ⟩/dt = −iH|ψ⟩`, o `|ψ(t+dt)⟩ = (I − iH dt)|ψ(t)⟩`, unitaria a primer orden, y la evolución finita es un producto de tales pasos [@preskill-ph219, ch.2 §2.1, p. 6]. Para una partícula, `H = p̂²/2m + V(x,t)` es el operador de energía [@zwiebach-mit-8-04, LN1 §1, pp. 3-4; LN5 §2, p. 4], y la ecuación en el espacio de posiciones es `−(ħ²/2m)∂²Ψ/∂x² + UΨ = iħ ∂Ψ/∂t` [@openstax-physics-3, §7.3].

**De unitaria a Schrödinger.** Derivando `|Ψ,t⟩ = U|Ψ,t₀⟩` se obtiene `∂ₜ|Ψ,t⟩ = Λ|Ψ,t⟩` con `Λ = (∂ₜU)U†`; derivar `UU† = 1` muestra que `Λ` es antihermítico, y definir `H = iħΛ` da un operador hermítico: la evolución unitaria implica la ecuación de Schrödinger [@zwiebach-mit-8-05, ch.6 §2.2, pp. 12-14]. Zwiebach identifica `H` con el hamiltoniano porque la energía es conjugada al tiempo y porque `d⟨Q⟩/dt = ⟨[Q,H]⟩/(iħ)` imita la ecuación clásica con corchetes de Poisson [@zwiebach-mit-8-05, ch.6 §2.2, p. 14].

**Solución para `H` constante.** `U(t,t₀) = exp[−iH(t−t₀)/ħ]`, con la exponencial de matriz definida por su serie de Taylor [@zwiebach-mit-8-05, ch.6 §2.3, pp. 15-16], que se calcula con la [descomposición en valores propios](../../math-foundations/concepts/eigenvalues-and-eigenvectors.md): cada componente de energía gira su fase a velocidad `E_j` (ver su capa profesional). En el espacio de posiciones, si el potencial `U` no depende del tiempo, se separan variables: `Ψ(x,t) = ψ(x)e^{−iEt/ħ}`, con `E` la energía total real [@openstax-physics-3, §7.3].

**Conservación de probabilidad.** La probabilidad total `N(t) = ∫|Ψ|²dx` permanece en 1 porque `H` es hermítico [@zwiebach-mit-8-04, LN6 §2, pp. 3-4]. Además, es una ley local, `∂ρ/∂t + ∂J/∂x = 0`, con corriente de probabilidad `J = (ħ/m) Im(Ψ*∂Ψ/∂x)`, análoga a la conservación de la carga [@zwiebach-mit-8-04, LN6 §3-4, pp. 5-8]. (Los apuntes 8.04 no usan la palabra "unitaria": solo muestran la conservación de la probabilidad con `H` hermítico.)

**Linealidad y determinismo.** La ecuación es lineal [@zwiebach-mit-8-04, LN1 §1, pp. 3-4] y de primer orden en el tiempo: `Ψ` en un instante inicial determina `Ψ` en todos los tiempos, y por eso admite soluciones complejas, a diferencia de una ecuación de onda de segundo orden [@zwiebach-mit-8-04, LN5 §1, p. 4; §2, p. 7]. La evolución es determinista; la aleatoriedad la introduce la [medida](born-rule-measurement.md).

**Errores frecuentes.**

- *"La ecuación de Schrödinger es como una ecuación de ondas clásica."* Contiene `i` y es de primer orden en `t` [@zwiebach-mit-8-04, LN5 §1, p. 4].
- *"Unitario significa que las probabilidades de cada resultado no cambian."* Significa que la norma se conserva; las probabilidades de resultados concretos sí cambian (ver [superposición](superposition-principle.md): el divisor de haz cambia las probabilidades).
- *"Toda evolución es unitaria."* Solo la de sistemas cerrados; un subsistema abierto no evoluciona de forma unitaria [@preskill-ph219, ch.2 §2.3.1, p. 17] (ver [decoherencia](decoherence.md)).

## Profesional {#layer-3}

**Del hamiltoniano a la puerta.** Un dispositivo que "enciende" un hamiltoniano cuyos estados propios son estados de polarización circular (o lineal) rota (o desfasa) la polarización de un fotón, y juntos dan cualquier unitaria 2×2 de determinante 1 [@preskill-ph219, ch.2 §2.2.2, p. 16]. Para un espín 1/2, una rotación de ángulo `θ` alrededor de `n` es `U = cos(θ/2)I − i sin(θ/2) n·σ`, y toda unitaria 2×2 de determinante 1 tiene esa forma, así que cualquier puerta de un qubit es una rotación de espín salvo fase global [@preskill-ph219, ch.2 §2.2.1, pp. 11-12]. Detalle en [sistemas de dos niveles](two-level-systems.md) y [puertas de un qubit](../../qubits-and-circuits/concepts/single-qubit-gates.md). Un espín en un campo magnético aparece como ejemplo de `H(t)` con dirección fija y magnitud variable [@zwiebach-mit-8-05, ch.6 §2.3, p. 16].

**`H(t)` dependiente del tiempo.** Si los `H(t)` en tiempos distintos conmutan, `U = exp[−(i/ħ)∫H dt']`; en general hace falta la serie de la exponencial ordenada en el tiempo [@zwiebach-mit-8-05, ch.6 §2.3, pp. 16-17]. El orden importa: `U(0)e^{tK}` no resolvería la ecuación [@zwiebach-mit-8-05, ch.6 §2.3, p. 16]. Este es el problema que enfrenta cualquier simulación de dinámica: véase [simulación de hamiltonianos](../../quantum-algorithms/concepts/hamiltonian-simulation.md).

**Imagen de Heisenberg.** `A_H(t) = U†(t,0) A_S U(t,0)`; preserva productos y conmutadores y da los mismos valores esperados [@zwiebach-mit-8-05, ch.6 §3.1, pp. 18-20]. Su ecuación de movimiento `iħ dA_H/dt = [A_H,H_H] + iħ(∂A_S/∂t)_H` muestra que un operador que conmuta con `H` se conserva [@zwiebach-mit-8-05, ch.6 §3.2, pp. 20-22]. De hecho, `iħ d⟨Q⟩/dt = ⟨[Q,H]⟩` para un operador sin dependencia explícita del tiempo [@zwiebach-mit-8-04, LN8 §3, p. 6]. Con matrices densidad, la evolución cerrada es `ρ(t+dt) = ρ(t) − i dt[H,ρ(t)]` [@preskill-ph219, ch.3 §3.5.2, p. 35]; sobre matrices densidad una unitaria actúa por conjugación, `Φ(ρ) = UρU†` [@watrous-2025, L10.1, PDF pp. 297-298].

**Simetrías y conservación.** Una simetría debe conmutar con la evolución temporal; infinitesimalmente, `[Q,H] = 0` para su generador `Q`, así que simetrías y leyes de conservación se corresponden [@preskill-ph219, ch.2 §2.2.1, p. 10].

**Unitarias como bloque de construcción de todo canal.** Todo canal es "añadir ancilla, aplicar unitaria, descartar parte" [@watrous-2025, L10.2, PDF pp. 303-305, 326]. Así, la evolución ruidosa es una unitaria sobre sistema más entorno vista solo desde el sistema. Una unitaria es un canal con una sola matriz de Kraus `A₀ = U` [@watrous-2025, L10.2, PDF p. 313]. Esto motiva la [decoherencia](decoherence.md).

**Cómo decidir.** Para estudiar dinámica continua (átomos, espines, qubits físicos), parte de `H`; para razonar sobre algoritmos, trabaja con las unitarias de las puertas, en tiempos discretos, que es como Watrous trata la evolución en las partes leídas (sin hamiltonianos) [@watrous-2025, L1.2, PDF p. 25]. Ambas descripciones están ligadas por `U = e^{−iHt}`.
