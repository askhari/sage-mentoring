---
concept: uncertainty-and-noncommutativity
title: "Incertidumbre y no conmutatividad"
format: 2
---

## Comprensión {#layer-2}

### Idea clave
Dos observables que no conmutan, `[A,B] = AB − BA ≠ 0`, no pueden tener valores definidos a la vez. La incertidumbre de Heisenberg, `ΔxΔp ≥ ħ/2`, es el caso de posición y momento, que cumplen `[x̂,p̂] = iħ` [@zwiebach-mit-8-04, LN5 §2, pp. 5-8; @openstax-physics-3, §7.2].

### Explicación
El **conmutador (commutator)** de dos operadores es `[A,B] = AB − BA`. El orden importa, igual que con matrices; los operadores conmutan cuando `[A,B] = 0` [@zwiebach-mit-8-04, LN5 §2, p. 5]. Para observables hermíticos (ver [observables](observables.md)), el producto `AB` solo es hermítico si conmutan [@preskill-ph219, ch.2 §2.1, pp. 4-5].

Aplicando los operadores a una función de prueba se obtiene `[x̂,p̂] = iħ`, llamada la relación de conmutación más fundamental de la mecánica cuántica; en 3D, `[x̂ᵢ,p̂ⱼ] = iħδᵢⱼ` [@zwiebach-mit-8-04, LN5 §2, pp. 5-8]. Ninguna matriz de dimensión finita puede satisfacer `[x̂,p̂] = iħ·1`, así que posición y momento necesitan matrices de dimensión infinita [@zwiebach-mit-8-04, LN5 §2, p. 6].

En espines la no conmutatividad es finita y concreta. Las matrices de Pauli no conmutan: `[σ₁,σ₂] = 2iσ₃` y cíclicas, con `Sᵢ = (ħ/2)σᵢ` [@zwiebach-mit-8-04, LN5 §2, p. 6]. En general `[σᵢ,σⱼ] = 2iε_ijk σₖ` y el anticonmutador se anula para `i ≠ j` [@zwiebach-mit-8-05, ch.2 §3, pp. 12-14]. Los operadores de espín cumplen la misma álgebra que el momento angular: `[Sₓ,S_y] = iħS_z` y cíclicas [@zwiebach-mit-8-05, ch.2 §2, p. 9]. Las rotaciones alrededor de ejes distintos no conmutan, y de ahí el álgebra `[J_k,J_l] = iε_klm J_m` [@preskill-ph219, ch.2 §2.2.1, p. 11].

Esa álgebra tiene una traducción física. El experimento 3 de Stern-Gerlach la muestra: filtrar por `Sₓ` borra el valor anterior de `S_z`, así que ambos no pueden ser definidos a la vez [@zwiebach-mit-8-05, ch.2 §1, pp. 6-7]. Cuando un estado es propio de `Q`, `ΔQ = 0` [@zwiebach-mit-8-04, LN9 §2, pp. 6-7]; un estado propio de `S_z` no lo es de `Sₓ`. Es la versión de qubits de "no se pueden medir con certeza `Z` y `X` a la vez", el origen de las medidas en distintas bases (véase [medida y regla de Born](born-rule-measurement.md)).

Para posición y momento, el resultado es el principio de incertidumbre de Heisenberg, `Δx Δp ≥ ħ/2`: una posición precisa implica poco conocimiento del momento y al revés [@openstax-physics-3, §7.2]. Zwiebach lo enuncia como consecuencia del conmutador [@zwiebach-mit-8-04, LN5 §2, p. 6; LN7 §1, p. 3].

La causa está en las ondas. Un paquete de ondas es una superposición de ondas planas con pesos `Φ(k)` (la transformada de Fourier de `Ψ`); un `Δk` estrecho exige un `Δx` ancho, con `ΔxΔk ≈ 1`, propiedad de la transformada de Fourier y no específicamente cuántica [@zwiebach-mit-8-04, LN7 §1, pp. 1-3]. La parte cuántica es `p = ħk`, que lo convierte en `ΔxΔp ≈ ħ` [@zwiebach-mit-8-04, LN7 §1, p. 3]. Con definiciones precisas, `ΔxΔp ≥ ħ/2`; un paquete gaussiano alcanza el mínimo `ħ/2` [@openstax-physics-3, §7.2]. No viene de imprecisión del aparato, sino de la naturaleza ondulatoria de la materia; una onda plana de momento definido tiene posición totalmente indeterminada [@openstax-physics-3, §7.2].

En computación cuántica, la no conmutatividad es la razón de que haya bases de medida incompatibles: un qubit tiene tres observables de Pauli que no conmutan, y medir uno borra la información de los otros. Por eso la información de un estado (incluida su fase) solo se recupera midiendo en varias bases con muchas copias [@preskill-ph219, ch.2 §2.2.1, p. 13]. Y por eso las puertas de un qubit (rotaciones de espín) no conmutan en general (ver [puertas de un qubit](../../qubits-and-circuits/concepts/single-qubit-gates.md)).

### Ejemplo
Un estado propio de `S_z` se mide en `S_x`: sale `±ħ/2` al 50 %, y después ya no tiene `S_z` definido. Como `[S_x,S_y] = iħS_z` y cíclicas, ningún par de componentes del espín puede fijarse a la vez [@zwiebach-mit-8-05, ch.2 §1, pp. 6-7; §2, p. 9].

### Errores frecuentes
- *"Es culpa de que el aparato perturba el sistema."* La incertidumbre viene de la naturaleza ondulatoria [@openstax-physics-3, §7.2].
- *"Que `AB ≠ BA` es un defecto."* Es exactamente lo que ocurre con las matrices: el orden importa.

### Para seguir
La capa 3 da órdenes de magnitud, la relación general entre dos observables y criterios para usar el conmutador en la práctica. Después, [matrices densidad](density-matrices.md) trata los estados con ruido.

## Profesional {#layer-3}

### Idea clave
El conmutador `[A,B]` permite decidir cómo se usan y cómo evolucionan las magnitudes: un operador que conmuta con `H` se conserva, y `X`, `Y` y `Z` anticonmutan por pares [@zwiebach-mit-8-05, ch.6 §3.2, pp. 20-22; ch.2 §3, pp. 13-14].

### Explicación
Los conmutadores corresponden a `iħ` veces los corchetes de Poisson clásicos, con `[x,p] = iħ` y `{x,p}_pb = 1` [@zwiebach-mit-8-05, ch.6 §2.2, pp. 14-15]. En la imagen de Heisenberg, un operador que conmuta con `H` se conserva [@zwiebach-mit-8-05, ch.6 §3.2, pp. 20-22]. Además, `iħ d⟨Q⟩/dt = ⟨[Q,H]⟩` [@zwiebach-mit-8-04, LN8 §3, p. 6]; el tema se ve en [evolución unitaria](unitary-time-evolution.md).

Para dos observables cualesquiera `A` y `B` se cumple `ΔAΔB ≥ ½|⟨[A,B]⟩|` [unverified]; con `[x,p] = iħ` se recupera `ΔxΔp ≥ ħ/2`, y con las reglas de conmutación de Pauli se obtiene la versión para el espín.

En medida, un puntero con paquete de ondas estrecho (anchura `Δx`) tiene una dispersión de velocidad de `~ħ/(mΔx)`, lo que da un "límite estándar cuántico" de resolución `~√(ħt/m)`; un puntero pesado lo hace despreciable [@preskill-ph219, ch.3 §3.1.1, p. 5].

La relación energía-tiempo, `ΔEΔt ≥ ħ/2`, dice que los estados de vida corta tienen energía mal definida, de ahí que los estados excitados de vida corta den líneas espectrales anchas [@openstax-physics-3, §7.2].

Cómo decidir en la práctica:

- Dos observables conmutan: se pueden definir a la vez `[unverified]`. No es el caso de `X`, `Y` y `Z`, que anticonmutan por pares [@zwiebach-mit-8-05, ch.2 §3, pp. 13-14].
- Se necesita reconstruir un estado: medir en varios ejes y repetir [@preskill-ph219, ch.2 §2.2.1, p. 13].
- Se va a invertir un orden de puertas: comprobar si conmutan; en general no, igual que las rotaciones alrededor de ejes distintos [@preskill-ph219, ch.2 §2.2.1, p. 11].

### Ejemplo
Para una incertidumbre de velocidad de `1,0×10⁻³ m/s`, el `Δx` mínimo es de unos 5,8 cm para un electrón y de unos `8,8×10⁻³³ m` para una bola de bolera de 6 kg [@openstax-physics-3, §7.2]. Confinar un electrón en 0,1 nm da una energía del orden de `ħ²/(8mL²) ≈ 0,95 eV`, consistente en orden de magnitud con la energía de ionización de unos 10 eV [@openstax-physics-3, §7.2].

### Para seguir
Continúa con [matrices densidad y estados mixtos](density-matrices.md), que describe lo que se ve cuando el sistema no está aislado.
