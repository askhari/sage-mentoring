---
concept: complex-numbers
title: "Números complejos"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
Un **número complejo (complex number)** es un par de reales `a + bi` con `i² = -1`. Las amplitudes de un estado cuántico son números complejos, y el estado es válido cuando la suma de sus módulos al cuadrado es 1 [@watrous-2025, L1.2, p. 18].

### Explicación
La suma se hace componente a componente y el producto sale de aplicar las reglas usuales con `i² = -1`: `(a+bi)(c+di) = (ac-bd) + (ad+bc)i`. Conviene volver a deducirlo en vez de memorizarlo [@axler-2024, def. 1.1, ex. 1.2, PDF pp. 20-21].

Con eso se usan constantemente tres operaciones:

- **Parte real e imaginaria:** de `3+2i`, la parte real es 3 y la imaginaria es 2.
- **Conjugado (complex conjugate):** cambia el signo de la parte imaginaria; el de `3+2i` es `3-2i`.
- **Módulo o valor absoluto (modulus):** `|z| = √((Re z)² + (Im z)²)`; para `3+2i` es `√13` [@axler-2024, def. 4.1-4.3, PDF p. 138].

Si se identifica `z` con el punto `(Re z, Im z)`, `|z|` es la distancia al origen [@axler-2024, §4, PDF p. 138]. Una identidad muy útil es `z · conj(z) = |z|²` [@axler-2024, 4.4, PDF p. 139].

Los números de módulo 1 forman la **circunferencia unidad** y se escriben `e^{iφ} = cos φ + i sin φ`. En general `c = r·e^{iφ}`, con `r = |c|` y `φ` el ángulo con el eje horizontal positivo (forma polar), y el conjugado de `r·e^{iφ}` es `r·e^{-iφ}` [@de-wolf-2026, App. B.1, p. 211].

![Plano complejo con la circunferencia unidad y e^(iφ)](../../../../../assets/diagrams/complex-plane-unit-circle.es.svg)

Esto sirve en computación cuántica porque las **amplitudes (amplitudes)** son números complejos [@de-wolf-2026, §1.2.1, p. 15]. Un vector de estado se define por dos propiedades: sus entradas son complejas y la suma de los módulos al cuadrado es 1 [@watrous-2025, L1.2, p. 18].

### Ejemplo
Producto: `(1+2i)(3-i) = 3 - i + 6i - 2i² = 3 + 5i + 2 = 5 + 5i`.

Estado válido: `(1+2i)/3 |0⟩ - (2/3)|1⟩` cumple `|1+2i|²/9 + 4/9 = 5/9 + 4/9 = 1` [@watrous-2025, L1.2, pp. 19-20].

### Para seguir
[Vectores y notación de Dirac](vectors-and-dirac-notation.md) usa estos números como entradas de columnas y escribe los estados con kets. La capa 2 de este concepto explica por qué hacen falta los complejos y qué papel tienen el módulo y la fase.

## Comprensión {#layer-2}

### Idea clave
El módulo fija las probabilidades de medida y la fase fija cómo interfieren los estados. Una fase global es invisible; una fase relativa cambia el estado [@watrous-2025, L3.3, pp. 91-92].

### Explicación
Primero, por qué complejos y no solo reales. El teorema fundamental del álgebra dice que todo polinomio no constante con coeficientes complejos tiene un cero complejo; es falso sobre los reales (`1+x²`), y a ello se atribuyen las diferencias entre el álgebra lineal real y la compleja [@axler-2024, 4.12, 4.13, PDF pp. 143-145]. La consecuencia que más importa aquí: todo operador sobre un espacio complejo de dimensión finita (no nulo) tiene un valor propio, mientras que una rotación de 90 grados en `R²` no tiene ninguno real pero sí `i` y `-i` sobre `C` [@axler-2024, 5.19, 5.9, PDF pp. 153-161]. Ver [valores y vectores propios](eigenvalues-and-eigenvectors.md).

Para operar con ellos se usan sin parar estas propiedades del conjugado y el módulo: `conj(wz) = conj(w)·conj(z)`, `|wz| = |w||z|`, `|conj(z)| = |z|` y la desigualdad triangular `|w+z| ≤ |w|+|z|` [@axler-2024, 4.4, PDF p. 139]. Un número es real si y solo si es igual a su conjugado [@axler-2024, §4, PDF p. 138]. Una identidad geométrica práctica es `|1 - e^{iθ}| = 2|sin(θ/2)|` [@de-wolf-2026, App. B.1, pp. 211-212].

Módulo y fase juegan papeles distintos. La probabilidad de medir un resultado en la base estándar es el módulo al cuadrado de la amplitud (regla de Born), así que un signo o una fase no cambian esas probabilidades; por eso `|+⟩` y `|-⟩` dan ambos 1/2 y 1/2 [@watrous-2025, L1.2, pp. 23-24]. Pero las fases sí cambian el estado: aplicando `H` y midiendo se distingue `|+⟩` de `|-⟩` con certeza [@watrous-2025, L1.2, p. 27].

De ahí la distinción entre fase global y relativa. Si `|φ⟩ = α|ψ⟩` con `|α| = 1` (es decir `α = e^{iθ}`), ambos estados dan las mismas probabilidades y siguen siendo iguales salvo ese factor bajo cualquier unitaria, por lo que se tratan como el mismo estado. Una fase aplicada solo a algunas entradas es **relativa** y sí importa [@watrous-2025, L3.3, pp. 91-92]. Una fase global no tiene significado físico [@de-wolf-2026, §1.2.2, p. 16].

Las operaciones de fase son el ejemplo básico: `P_θ = diag(1, e^{iθ})` es unitaria, y `S = P_{π/2} = diag(1, i)`, `T = P_{π/4}` y `Z = P_π` son casos particulares [@watrous-2025, L1.2, p. 26]. Ver [matrices unitarias y hermíticas](unitary-and-hermitian-matrices.md).

### Ejemplo
Los estados `|-⟩` y `-|-⟩` difieren en una fase global: son el mismo estado. En cambio `|+⟩ = (|0⟩+|1⟩)/√2` y `|-⟩ = (|0⟩-|1⟩)/√2` difieren en una fase relativa (el signo solo afecta a la entrada de `|1⟩`): dan las mismas probabilidades al medir, pero tras aplicar `H` el primero produce `|0⟩` y el segundo `|1⟩` con certeza [@watrous-2025, L1.2, p. 27; L3.3, pp. 91-92].

### Errores frecuentes
- *"La fase no se ve, luego no importa."* Solo la fase global es invisible; las fases relativas controlan la interferencia.

### Para seguir
La capa 3 usa estas ideas con raíces de la unidad y con la comparación de estados en la práctica.

## Profesional {#layer-3}

### Idea clave
Las raíces de la unidad suman 0 y esa cancelación es la que produce la interferencia destructiva; en la práctica, los estados se comparan salvo fase global [@de-wolf-2026, App. B.1, p. 211; @watrous-2025, L3.3, pp. 91-92].

### Explicación
Las raíces de la unidad y las sumas geométricas aparecen en la transformada de Fourier cuántica y en muchos análisis de algoritmos. La suma `Σ_{j=0}^{m-1} z^j` vale `m` si `z = 1` y `(1 - z^m)/(1 - z)` en otro caso. Para una raíz de la unidad `z = e^{2πir/N}` con `r ∈ {1,…,N-1}`, la suma sobre `j = 0..N-1` es 0 [@de-wolf-2026, App. B.1, p. 211].

Para razonar con fases en la práctica:

- Calcula con la forma polar cuando multipliques (los módulos se multiplican y los ángulos se suman) y con la forma cartesiana cuando sumes. Que `|wz| = |w||z|` garantiza que multiplicar por `e^{iφ}` nunca cambia el módulo [@axler-2024, 4.4, PDF p. 139].
- Al comparar dos estados (por ejemplo, el resultado de dos circuitos supuestamente equivalentes), la igualdad debe entenderse salvo fase global [@watrous-2025, L3.3, pp. 91-92].
- Una puerta de fase `diag(1, e^{iθ})` y la misma multiplicada por `e^{iα}` actúan igual sobre los estados salvo fase global; pero dentro de una puerta *controlada* esa fase pasa a ser relativa. [unverified]

Al contar parámetros hay que recordar que `C` es 1-dimensional sobre `C` y 2-dimensional sobre `R` [@axler-2024, §4, PDF p. 138; §2C, PDF p. 63].

### Ejemplo
Un estado de `n` qubits tiene `2^n` amplitudes complejas, es decir `2^{n+1}` reales, antes de imponer normalización y descartar la fase global, porque cada número complejo vale por dos reales [@axler-2024, §4, PDF p. 138; §2C, PDF p. 63]. Para `n = 2` son 4 amplitudes y 8 reales.

### Las fuentes discrepan
Las fuentes no repasan aritmética compleja más allá de lo citado (Watrous usa conjugado, módulo y fase como herramientas ya conocidas); para más práctica hay que acudir a otro texto.

### Para seguir
[Vectores y notación de Dirac](vectors-and-dirac-notation.md), capa 3, trata las convenciones de escritura de kets y bras.
