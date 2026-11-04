---
concept: stabilizer-formalism
title: "Formalismo de estabilizadores"
format: 2
---

## Comprensión {#layer-2}

### Idea clave
El **formalismo de estabilizadores (stabilizer formalism)** describe un código no con sus estados sino con un puñado de operadores de Pauli que lo dejan invariante; detectar y corregir errores pasa a ser un cálculo de commutación con esos operadores [@watrous-2025, L14.3, PDF pp. 420-421, 431-432].

### Explicación
Se asumen [los valores y vectores propios](../../math-foundations/concepts/eigenvalues-and-eigenvectors.md) y [el código de Shor](shor-code.md), el ejemplo con el que se motiva este lenguaje. En el código de Shor hay ocho comprobaciones, cada una definida a mano; para un código con cientos de qubits eso es inmanejable.

El lenguaje parte de los operadores de Pauli. Los operadores `I, X, Y, Z` son unitarios y hermíticos; distintos no identidad anticonmutan; cada uno elevado al cuadrado da `I`; el producto de dos distintos es `±i` veces el tercero [@watrous-2025, L14.1, PDF p. 408]. Una operación de Pauli de `n` qubits es un producto tensorial de `n` Paulis; su *peso (weight)* es el número de factores distintos de la identidad, y los códigos se diseñan para corregir errores hasta un peso máximo [@watrous-2025, L14.1, PDF p. 409]. Las matrices `I, X, Y, Z` con fases `1, i, −1, −i` forman un grupo de 16 elementos, y `⟨XX, ZZ⟩` solo tiene cuatro porque `XX` y `ZZ` conmutan [@watrous-2025, L14.1, PDF pp. 409-410]. El grupo de Pauli de `n` qubits es `{±1, ±i} × {I,X,Y,Z}^{⊗n}`, de tamaño `4^{n+1}` [@de-wolf-2026, §20.1, p. 185 [173]].

Un Pauli no identidad de `n` qubits tiene solo los valores propios `+1` y `−1`, cada uno con un subespacio de rango `2^{n−1}`. Medirlo es una medida proyectiva de un observable con esos dos resultados (ver [observables](../../quantum-mechanics/concepts/observables.md)): `ZZ` sobre un estado de Bell da `+1` sin colapsar a `|00⟩` ni a `|11⟩` [@watrous-2025, L14.1, PDF pp. 410-412]. Cualquier observable de Pauli se mide sin destruir el estado con un circuito de estimación de fase con un qubit de control, y cuanto menor es el peso, más pequeño es el circuito; medir un producto de observables `Z` equivale a calcular una paridad [@watrous-2025, L14.1, PDF pp. 412-414]. Aquí vuelve la [estimación de fase](../../quantum-algorithms/concepts/phase-estimation.md).

Un estado `|ψ⟩` está estabilizado por un Pauli `P` (que no sea `±I`) si `P|ψ⟩ = |ψ⟩`. Cada estabilizador independiente reduce a la mitad la dimensión del subespacio de estados que fija, y `n` estabilizadores independientes de `n` qubits fijan un solo estado salvo fase global: un *estado estabilizador (stabilizer state)* [@de-wolf-2026, §20.1, p. 185 [173]]. Por ejemplo, `|0⟩` está estabilizado por `Z`, `|1⟩` por `−Z`, `|+⟩` por `X`, `|−⟩` por `−X`, y los pares de Bell también son estados estabilizadores [@de-wolf-2026, §20.1, p. 185 [173]]. Los estabilizadores deben conmutar entre sí (si anticonmutaran no tendrían un estado propio común con valor `+1`) y `−I` no puede pertenecer al grupo que generan [@de-wolf-2026, §20.1, pp. 185-186 [173-174]].

De ahí sale la definición de código. Dados generadores de Pauli `P₁,…,P_r` que (1) conmutan todos, (2) forman un conjunto generador mínimo y (3) fijan algún estado (equivalente a que `−I` no esté en el grupo), el *espacio de código* es el conjunto de estados fijados por todos los generadores (autoespacio `+1`) y el *estabilizador* es el grupo que generan [@watrous-2025, L14.3, PDF pp. 420-421]. El espacio de código tiene dimensión `2^{n−r}`, así que se codifican `n−r` qubits [@watrous-2025, L14.3, PDF pp. 425-428]. Con cuentas:

- *Repetición.* `n = 3`, generadores `ZZI` e `IZZ` (`r = 2`): se codifica `3 − 2 = 1` qubit [@watrous-2025, L14.3, PDF pp. 422-423]. La versión de phase-flip usa `XXI` e `IXX`.
- *Shor.* `n = 9`, `r = 8` (seis `ZZ` y dos de peso 6 de tipo `X`): 1 qubit lógico [@watrous-2025, L14.3, PDF p. 423].
- *Steane.* Generadores `ZZZZIII`, `ZZIIZZI`, `ZIZIZIZ` y sus análogos con `X`: `n = 7`, `r = 6`, 1 qubit lógico [@watrous-2025, L14.3, PDF p. 423].
- *Código de 5 qubits.* `XZZXI` y sus desplazamientos cíclicos: el menor que corrige cualquier error de un qubit [@watrous-2025, L14.3, PDF p. 424; @de-wolf-2026, §21.4, p. 199 [187]].

Medir los generadores como observables da el *síndrome (syndrome)*: todos `+1` significa una codificación válida, y cualquier `−1` señala un error [@watrous-2025, L14.3, PDF pp. 421, 431]. Un error de Pauli `E` puede ser de tres tipos: (1) proporcional a un elemento del estabilizador (inofensivo, síndrome todo `+1`), (2) no proporcional a uno pero conmutando con todos los generadores (un error no detectado que actúa como Pauli lógico; `XXX` en el código de repetición es un `X` lógico), o (3) anticonmutando con algún generador (detectado) [@watrous-2025, L14.2, PDF p. 420; L14.3, PDF pp. 431-432]. Un error que anticonmuta con un estabilizador voltea el signo de su medida [@fowler-2012, p. 7].

La *distancia (distance)* de un código estabilizador es el menor peso de un error no detectable del tipo (2); `[[n, k, d]]` significa `n` qubits físicos, `k` lógicos y distancia `d`. El código de Steane es `[[7, 1, 3]]`: no hay Pauli de peso 1 o 2 que conmute con todos los generadores sin ser trivial, mientras que `IIIIXXX` es un contraejemplo de peso 3 [@watrous-2025, L14.3, PDF pp. 432-434]. Un código de distancia `d` corrige todos los errores de peso hasta `(d−1)/2`: hay `2^r` síndromes y `4^n` Paulis, y elegir para cada síndrome un Pauli de peso mínimo corrige todo error de peso menor que `d/2`. Dos errores son equivalentes si su producto es proporcional a un elemento del estabilizador [@watrous-2025, L14.3, PDF pp. 434-436].

Los *operadores lógicos* conmutan con todos los estabilizadores pero no son productos de ellos; actúan sobre los grados de libertad que los estabilizadores dejan libres. Multiplicar uno por estabilizadores da un operador lógico equivalente, así que solo hay un `X_L` y un `Z_L` independientes por qubit lógico [@fowler-2012, pp. 8-10]. La [siguiente sección del dominio](surface-code.md) los ve como cadenas de qubits a través de una red.

Las operaciones de Clifford (las unitarias construidas con `H`, `S` y CNOT) son, salvo fase, las que transforman Paulis en Paulis por conjugación (`HXH = Z`, `SXS† = Y`); `T` y Toffoli no lo son, y las puertas de Clifford no son universales [@watrous-2025, L14.3, PDF pp. 428-429]. El *teorema de Gottesman-Knill* dice que un circuito de Clifford sobre una entrada de la base estándar y con medidas estándar se puede simular de forma eficiente en un ordenador clásico, siguiendo los `n` estabilizadores (unos `n(2n+2)` bits) en lugar de `2ⁿ` amplitudes [@watrous-2025, L14.3, PDF p. 429; @de-wolf-2026, §20.3, p. 187 [175]]. Ver [conjuntos universales de puertas](../../qubits-and-circuits/concepts/universal-gate-sets.md).

Un tipo especial son los códigos *CSS*, cuyos generadores son todos de tipo `X`/`I` o todos de tipo `Z`/`I`, con los de `Z` conmutando con los de `X`; Steane, Shor y el código tórico lo son [@watrous-2025, L15.1, PDF pp. 444-446]. Los generadores de solo `Z` corresponden a las comprobaciones de paridad de un código clásico lineal [@watrous-2025, L15.1, PDF pp. 440-443]. El de Steane es un código de Hamming `[7,4,3]` para volteos de bit y otro para volteos de fase; `X` y `Z` se corrigen por separado, y a cambio se codifica un solo qubit mientras el de Hamming transporta 4 bits [@watrous-2025, L15.1, PDF pp. 447-448].

### Ejemplo
Un caso ejecutable con Qiskit 2.6 (el módulo `quantum_info` incluye `StabilizerState`; recuerda que Qiskit ordena las etiquetas con el qubit 0 a la derecha, ver [circuitos en Qiskit](../../qiskit-programming/concepts/qiskit-circuits.md)):

```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Pauli, StabilizerState

qc = QuantumCircuit(3)
qc.cx(0, 1)
qc.cx(0, 2)                              # |000> codificado: |000>
checks = [Pauli("ZZI"), Pauli("IZZ")]    # paridades q1q2 y q0q1

for name, extra in [("sin error", None), ("X en q1", "x"), ("Z en q1", "z")]:
    c = qc.copy()
    if extra:
        getattr(c, extra)(1)
    st = StabilizerState(c)
    print(name, [int(st.expectation_value(p).real) for p in checks])
```

Salida: `sin error [1, 1]`, `X en q1 [-1, -1]`, `Z en q1 [1, 1]`. La `X` anticonmuta con las dos comprobaciones y las voltea; la `Z`, que conmuta con ambas, pasa desapercibida, como en la [repetición](repetition-codes.md).

### Errores frecuentes
- *"Los estabilizadores son los estados del código."* Son operadores; los estados del código son sus autoestados con valor `+1`.
- *"Un síndrome todo `+1` garantiza que no hubo errores."* Solo garantiza que no hubo errores de tipo (3); los de tipo (2) pasan desapercibidos [@watrous-2025, L14.3, PDF pp. 431-432].
- *"Todo circuito de Clifford es inútil."* Es simulable de forma eficiente, pero es la base de la corrección: sin una puerta no Clifford como `T` no hay computación universal [@watrous-2025, L14.3, PDF p. 429].

### Para seguir
La capa 3 usa el formalismo para verificar circuitos, simular y elegir un código por sus parámetros. Antes, [el código de superficie](surface-code.md) es el código estabilizador más estudiado en hardware.

## Profesional {#layer-3}

### Idea clave
En la práctica los estabilizadores sirven para verificar circuitos de síndrome, describir qué mide una máquina, seguir errores en software y simular; y tres números (`k/n`, `d` y el peso de los generadores) más la complejidad del decodificador deciden qué código usar [@bravyi-2024, pp. 4-7, 13-16].

### Explicación
Cuatro usos habituales:

1. *Verificar un circuito de síndrome.* Se demuestra la corrección del circuito de extracción de síndrome de un código siguiendo el tableau de estabilizadores del circuito de Clifford, y la simulación de estabilizadores propaga fallos individuales. Una consecuencia que conviene tener presente: la distancia del circuito de síndrome para el código `[[144,12,12]]` de IBM es como mucho 10 (se conjetura 10), menor que la distancia 12 del código, y es la del circuito, no la del código, la que fija la supresión del error [@bravyi-2024, pp. 5-6, 13-16].
2. *Describir qué mide una máquina.* En el código de superficie, las plaquetas de 4 cuerpos de `X` y `Z` son los estabilizadores y conmutan con los operadores lógicos; medirlas detecta errores sin perturbar el estado lógico [@bluvstein-2024, p. 3]. El único estado propio común tras medir repetidamente un conjunto completo de estabilizadores se llama "estado quiescente" [@fowler-2012, pp. 5-6].
3. *Seguir errores en software.* Los errores no se deshacen físicamente: se anotan en el software de control como un marco de Pauli (*Pauli frame*) y se aplican a las medidas posteriores. Las puertas `X` y `Z` lógicas se hacen "en software" [@fowler-2012, pp. 4, 7; p. 18, nota 16].
4. *Simular.* Un circuito de Clifford de `n` qubits se simula con unos `n(2n+2)` bits, frente a las `2ⁿ` amplitudes de un vector de estado [@de-wolf-2026, §20.3, p. 187 [175]]. La barrera aparece con las puertas `T`: el rango estabilizador de `|T⟩^{⊗t}` está acotado por `3^{t/4} ≈ 2^{0,3963 t}` y el rango aproximado ronda `2^{0,228 t}`, por lo que circuitos con `O(log n)` puertas `T` se simulan de forma eficiente [@de-wolf-2026, §20.5, p. 190 [178]]. Eso respalda que el número de puertas `T` mide lo "no clásico" de un circuito, y es una razón de que la contabilidad de recursos las cuente aparte (ver [estimación de recursos](resource-estimation.md)).

Para elegir un código, tres números y un detalle de implementación deciden:

- `k/n` (tasa): el código de superficie tiene `n = d²` qubits de datos para `k = 1` (asintóticamente tasa cero y distancia `√n`), mientras que los buenos códigos qLDPC tienen tasa constante y distancia lineal [@bravyi-2024, pp. 1-2].
- `d` (distancia): fija cuántos errores aguanta.
- *Peso y geometría de los generadores:* el código de superficie tiene comprobaciones de peso 4 locales en 2D; los códigos bicicleta de IBM tienen peso 6 y conexiones no locales [@bravyi-2024, pp. 4, 7].
- *Complejidad del decodificador:* hallar el error de peso mínimo para un síndrome es difícil en general, incluso para códigos clásicos, por lo que se eligen códigos para los que la corrección se calcula de forma eficiente [@watrous-2025, L14.3, PDF pp. 436-437]. Ver [decodificación](decoding.md).

Los estabilizadores describen códigos de qubits con errores de Pauli; los códigos bosónicos (GKP, cat) quedan fuera, y aparecen en las fuentes solo como alternativas de hardware [@eisert-2025, Sec. III, p. 5]. Este curso no desarrolla esa parte.

### Ejemplo
Los códigos bicicleta bivariados son un ejemplo de familia moderna. Son códigos CSS con comprobaciones de peso 6 en las que cada qubit participa en 6 comprobaciones (3 de tipo `X`, 3 de tipo `Z`); el grafo de Tanner (qubits y comprobaciones unidos por aristas) tiene grado 6. Se construyen con matrices de desplazamiento cíclico `x`, `y` (`x^ℓ = y^m = I`) y dos polinomios `A` y `B` de tres monomios cada uno: `H_X = [A | B]`, `H_Z = [Bᵀ | Aᵀ]`, `n = 2ℓm`, y las comprobaciones `X` y `Z` conmutan porque `H_X H_Zᵀ = AB + BA = 0 (mod 2)` [@bravyi-2024, pp. 4, 7]. Para `ℓ = 12`, `m = 6`, `A = x³ + y + y²` y `B = y³ + x + x²` se obtiene el código `[[144, 12, 12]]` [@bravyi-2024, p. 8]. El circuito de síndrome usa `n` ancillas y 7 capas de CNOT, independiente de la longitud del código [@bravyi-2024, pp. 4-5, 12-13]. Para los parámetros de esa familia y su comparación con la superficie, ver [código de superficie](surface-code.md).

### Para seguir
[La decodificación](decoding.md) trata del cálculo clásico que convierte un síndrome en una corrección.
