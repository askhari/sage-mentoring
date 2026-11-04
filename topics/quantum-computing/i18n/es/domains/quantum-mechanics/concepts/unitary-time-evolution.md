---
concept: unitary-time-evolution
title: "Evolución temporal unitaria (ecuación de Schrödinger)"
format: 2
---

## Comprensión {#layer-2}

### Idea clave
Un sistema cerrado evoluciona con un operador unitario, `|ψ(t')⟩ = U(t',t)|ψ(t)⟩`, que conserva la norma del estado. En forma diferencial es la ecuación de Schrödinger, `iħ ∂|Ψ⟩/∂t = H|Ψ⟩`, con `H` hermítico [@preskill-ph219, ch.2 §2.1, p. 6; @zwiebach-mit-8-05, ch.6 §2.1-2.2, pp. 10-14].

### Explicación
El postulado de la dinámica dice que, para un sistema cerrado, el estado evoluciona con un operador unitario (imagen de Schrödinger) [@preskill-ph219, ch.2 §2.1, p. 6]. Zwiebach lo postula igual: existe un `U(t,t₀)` unitario, igual para todos los estados iniciales y único [@zwiebach-mit-8-05, ch.6 §2.1, p. 10]. Unitaria significa `U†U = 1`, y eso conserva la norma del estado [@zwiebach-mit-8-05, ch.6 §2.1, pp. 10-11]; ya conoces estas matrices en [matrices unitarias y hermíticas](../../math-foundations/concepts/unitary-and-hermitian-matrices.md). Cumple `U(t₀,t₀) = 1`, la composición `U(t₂,t₀) = U(t₂,t₁)U(t₁,t₀)` y la inversa `U(t₀,t) = U†(t,t₀)` [@zwiebach-mit-8-05, ch.6 §2.1, pp. 11-12].

Esto es lo que hace de las puertas cuánticas operaciones unitarias: Watrous las define como las matrices que conservan la norma [@watrous-2025, L1.2, PDF p. 25]. Por eso un circuito sin medidas es una unitaria total, reversible. La física dice cómo se consigue una puerta: se enciende un hamiltoniano durante un tiempo (ver la capa 3).

La forma diferencial es la ecuación de Schrödinger, `iħ ∂|Ψ⟩/∂t = H|Ψ⟩`, con `H` hermítico y con unidades de energía [@zwiebach-mit-8-05, ch.6 §2.2, p. 14]. Con `ħ = 1`, `d|ψ⟩/dt = −iH|ψ⟩`, o `|ψ(t+dt)⟩ = (I − iH dt)|ψ(t)⟩`, unitaria a primer orden, y la evolución finita es un producto de tales pasos [@preskill-ph219, ch.2 §2.1, p. 6]. Para una partícula, `H = p̂²/2m + V(x,t)` es el operador de energía [@zwiebach-mit-8-04, LN1 §1, pp. 3-4; LN5 §2, p. 4]. En el espacio de posiciones la ecuación es `−(ħ²/2m)∂²Ψ/∂x² + UΨ = iħ ∂Ψ/∂t` [@openstax-physics-3, §7.3].

La unitaridad implica esa ecuación. Derivando `|Ψ,t⟩ = U|Ψ,t₀⟩` se obtiene `∂ₜ|Ψ,t⟩ = Λ|Ψ,t⟩` con `Λ = (∂ₜU)U†`; derivar `UU† = 1` muestra que `Λ` es antihermítico, y definir `H = iħΛ` da un operador hermítico [@zwiebach-mit-8-05, ch.6 §2.2, pp. 12-14]. Zwiebach identifica `H` con el hamiltoniano porque la energía es conjugada al tiempo y porque `d⟨Q⟩/dt = ⟨[Q,H]⟩/(iħ)` imita la ecuación clásica con corchetes de Poisson [@zwiebach-mit-8-05, ch.6 §2.2, p. 14].

Para `H` constante la solución es `U(t,t₀) = exp[−iH(t−t₀)/ħ]`, con la exponencial de matriz definida por su serie de Taylor [@zwiebach-mit-8-05, ch.6 §2.3, pp. 15-16]. Se calcula con la [descomposición en valores propios](../../math-foundations/concepts/eigenvalues-and-eigenvectors.md): cada componente de energía gira su fase a velocidad `E_j`. En el espacio de posiciones, si el potencial `U` no depende del tiempo, se separan variables: `Ψ(x,t) = ψ(x)e^{−iEt/ħ}`, con `E` la energía total real [@openstax-physics-3, §7.3].

La probabilidad total `N(t) = ∫|Ψ|²dx` permanece en 1 porque `H` es hermítico [@zwiebach-mit-8-04, LN6 §2, pp. 3-4]. Además, es una ley local, `∂ρ/∂t + ∂J/∂x = 0`, con corriente de probabilidad `J = (ħ/m) Im(Ψ*∂Ψ/∂x)`, análoga a la conservación de la carga [@zwiebach-mit-8-04, LN6 §3-4, pp. 5-8]. (Los apuntes 8.04 no usan la palabra "unitaria": solo muestran la conservación de la probabilidad con `H` hermítico.)

Por último, la ecuación es lineal y de primer orden en el tiempo: `Ψ` en un instante inicial determina `Ψ` en todos los tiempos, y por eso admite soluciones complejas, a diferencia de una ecuación de onda de segundo orden [@zwiebach-mit-8-04, LN1 §1, pp. 3-4; LN5 §1, p. 4; §2, p. 7]. La evolución es determinista; la aleatoriedad la introduce la [medida](born-rule-measurement.md).

### Ejemplo
Un divisor de haz equilibrado actúa como una unitaria 2×2 sobre las amplitudes del haz superior e inferior. Conserva la norma, pero cambia las probabilidades de cada detector: unitaria no significa que las probabilidades de cada resultado queden fijas (ver [superposición](superposition-principle.md)) [@zwiebach-mit-8-04, LN2 §1, pp. 1-4].

### Errores frecuentes
- *"La ecuación de Schrödinger es como una ecuación de ondas clásica."* Contiene `i` y es de primer orden en `t` [@zwiebach-mit-8-04, LN5 §1, p. 4].
- *"Unitario significa que las probabilidades de cada resultado no cambian."* Significa que la norma se conserva; las probabilidades de resultados concretos sí cambian.
- *"Toda evolución es unitaria."* Solo la de sistemas cerrados; un subsistema abierto no evoluciona de forma unitaria (ver [decoherencia](decoherence.md)) [@preskill-ph219, ch.2 §2.3.1, p. 17].

### Para seguir
La capa 3 pasa del hamiltoniano a la puerta concreta, trata el caso de `H(t)` y las imágenes de Schrödinger y Heisenberg.

## Profesional {#layer-3}

### Idea clave
Encender un hamiltoniano durante un tiempo produce una puerta; para un espín 1/2, toda unitaria 2×2 de determinante 1 es una rotación `U = cos(θ/2)I − i sin(θ/2) n·σ`, de modo que cualquier puerta de un qubit es una rotación de espín salvo fase global [@preskill-ph219, ch.2 §2.2.1, pp. 11-12].

### Explicación
Un dispositivo que "enciende" un hamiltoniano cuyos estados propios son estados de polarización circular (o lineal) rota (o desfasa) la polarización de un fotón, y juntos dan cualquier unitaria 2×2 de determinante 1 [@preskill-ph219, ch.2 §2.2.2, p. 16]. Detalle en [sistemas de dos niveles](two-level-systems.md) y [puertas de un qubit](../../qubits-and-circuits/concepts/single-qubit-gates.md). Un espín en un campo magnético aparece como ejemplo de `H(t)` con dirección fija y magnitud variable [@zwiebach-mit-8-05, ch.6 §2.3, p. 16].

Si los `H(t)` en tiempos distintos conmutan, `U = exp[−(i/ħ)∫H dt']`; en general hace falta la serie de la exponencial ordenada en el tiempo [@zwiebach-mit-8-05, ch.6 §2.3, pp. 16-17]. El orden importa: `U(0)e^{tK}` no resolvería la ecuación [@zwiebach-mit-8-05, ch.6 §2.3, p. 16]. Este es el problema que enfrenta cualquier simulación de dinámica: véase [simulación de hamiltonianos](../../quantum-algorithms/concepts/hamiltonian-simulation.md).

En la imagen de Heisenberg, `A_H(t) = U†(t,0) A_S U(t,0)` preserva productos y conmutadores y da los mismos valores esperados [@zwiebach-mit-8-05, ch.6 §3.1, pp. 18-20]. Su ecuación de movimiento `iħ dA_H/dt = [A_H,H_H] + iħ(∂A_S/∂t)_H` muestra que un operador que conmuta con `H` se conserva [@zwiebach-mit-8-05, ch.6 §3.2, pp. 20-22]. De hecho, `iħ d⟨Q⟩/dt = ⟨[Q,H]⟩` para un operador sin dependencia explícita del tiempo [@zwiebach-mit-8-04, LN8 §3, p. 6]. Una simetría debe conmutar con la evolución temporal; infinitesimalmente, `[Q,H] = 0` para su generador `Q`, así que simetrías y leyes de conservación se corresponden [@preskill-ph219, ch.2 §2.2.1, p. 10].

Con matrices densidad, la evolución cerrada es `ρ(t+dt) = ρ(t) − i dt[H,ρ(t)]` [@preskill-ph219, ch.3 §3.5.2, p. 35]; sobre ellas una unitaria actúa por conjugación, `Φ(ρ) = UρU†` [@watrous-2025, L10.1, PDF pp. 297-298]. Todo canal es "añadir ancilla, aplicar unitaria, descartar parte" [@watrous-2025, L10.2, PDF pp. 303-305, 326]: la evolución ruidosa es una unitaria sobre sistema más entorno vista solo desde el sistema, y una unitaria es el canal con una sola matriz de Kraus `A₀ = U` [@watrous-2025, L10.2, PDF p. 313]. Esto motiva la [decoherencia](decoherence.md).

Para decidir el nivel de descripción: dinámica continua (átomos, espines, qubits físicos), parte de `H`; razonar sobre algoritmos, trabaja con las unitarias de las puertas, en tiempos discretos, que es como Watrous trata la evolución en las partes leídas (sin hamiltonianos) [@watrous-2025, L1.2, PDF p. 25]. Ambas descripciones están ligadas por `U = e^{−iHt}`.

### Ejemplo
Una rotación de ángulo `θ` alrededor de `n` en un espín 1/2 es `U = cos(θ/2)I − i sin(θ/2) n·σ`. Para `θ = 2π` da `−I`, la fase global ya vista [@preskill-ph219, ch.2 §2.2.1, pp. 11-12]. Mantener `H` fijo durante un tiempo `t` produce `U = e^{−iHt}`, que implementa esa rotación como puerta.

### Para seguir
Continúa con [sistemas de dos niveles](two-level-systems.md) para ver el ejemplo del espín, o con [matrices densidad](density-matrices.md) y [decoherencia](decoherence.md) para la evolución de sistemas abiertos.
