---
concept: phase-kickback
title: "Retroceso de fase (phase kickback)"
format: 2
---

## Comprensión {#layer-2}

### Idea clave
En una puerta controlada, el qubit objetivo puede quedar intacto mientras la información que "calcula" pasa a la **fase** del control. Este *retroceso de fase (phase kickback)* convierte una consulta de bits en una consulta de fase, y es el mecanismo de la [estimación de fase](phase-estimation.md) [@watrous-2025, L5.2, PDF pp. 141-143].

### Explicación
Se parte de la consulta estándar `U_f|x⟩|y⟩ = |x⟩|y⊕f(x)⟩` del [modelo de consultas](query-model-and-oracles.md). La clave es la identidad, que se comprueba mirando `a = 0` y `a = 1`:

```
|0 ⊕ a⟩ − |1 ⊕ a⟩ = (−1)^a (|0⟩ − |1⟩)
```

[@watrous-2025, L5.2, PDF p. 141]. Con el objetivo en `|−⟩ = (|0⟩−|1⟩)/√2`, el resultado es

```
U_f |x⟩|−⟩ = (−1)^{f(x)} |x⟩|−⟩
```

El qubit objetivo sigue en `|−⟩`; la información sobre `f(x)` ha ido a la fase de `|x⟩` [@watrous-2025, L5.2, PDF pp. 141-143; @de-wolf-2026, §2.4, pp. 29-30]. Aaronson lo presenta como la equivalencia entre el oráculo XOR y el de fase [@aaronson-2018, Lec17, p. 2].

Hay una lectura más estructural. Como `|b⊕c⟩ = X^c|b⟩`, se tiene `U_f(|ψ⟩|a⟩) = (X^{f(a)}|ψ⟩)|a⟩`. Y `|−⟩` es un **vector propio (eigenvector)** de `X` con valor propio `−1`, de modo que `X^{f(a)}|−⟩ = (−1)^{f(a)}|−⟩` [@watrous-2025, L5.2, PDF p. 143]. Esta lectura es la que se generaliza: lo que importa no es el estado `|−⟩` en sí, sino que sea vector propio de la operación controlada.

Así, si `|ψ⟩` es vector propio de una unitaria `U` con valor propio `e^{2πiθ}` y el qubit de control está en `|+⟩`, la puerta `controlled-U` da `|ψ⟩ ⊗ (|0⟩ + e^{2πiθ}|1⟩)/√2`: el valor propio "retrocede" a la fase del control y el registro del vector propio no cambia [@watrous-2025, L7.2, PDF p. 198]. Es la misma idea que en el oráculo con `U = X`, `θ = 1/2`.

El control debe estar en superposición. Si estuviera en `|0⟩` o `|1⟩`, la fase `e^{2πiθ}` sería una fase *global* sin efecto en las probabilidades de medida; el primer Hadamard lo pone en superposición para que el retroceso sea una fase *relativa* [@watrous-2025, L7.2, PDF pp. 199-200]. Y esa fase relativa aún no se ve al medir: antes del segundo Hadamard, medir el control da 0 y 1 con probabilidad 1/2 y no dice nada de `θ`; el segundo Hadamard la convierte en probabilidad por interferencia [@watrous-2025, L7.2, PDF p. 200].

### Ejemplo
Con `n = 1`, `f(0)=0`, `f(1)=1`, control en `|+⟩` y objetivo en `|−⟩`: el control pasa de `(|0⟩+|1⟩)/√2` a `(|0⟩−|1⟩)/√2`, es decir, de `|+⟩` a `|−⟩`, mientras el objetivo sigue en `|−⟩` (cálculo propio a partir de la identidad citada). Es el estado que da Deutsch al final del paso de consulta [@watrous-2025, L5.2, PDF pp. 141-142].

### Errores frecuentes
- *"El qubit objetivo no cambia, luego no pasa nada."* Pasa: cambia el control. Shor lo explica como "acción de retroceso" (*back action*): un `CNOT` sobre `|−⟩|−⟩` deja el objetivo igual y cambia el control, y `(H⊗H)·CNOT·(H⊗H)` invierte la dirección del `CNOT`; si un sistema afecta a otro, el otro también afecta al primero [@shor-mit-2022, L18, pp. 6-7].
- *"Con el objetivo en `|+⟩` también hay retroceso."* No: `U_f(|i⟩|+⟩) = |i⟩|+⟩` para cualquier `f`. Ese contraste permite elegir en qué parte del estado actúa la consulta de fase [@de-wolf-2026, §2.4, footnote 7, p. 30; @aaronson-2018, Lec17, p. 2].
- *"Todos los algoritmos de consultas lo usan."* El de Simon no: los qubits inferiores entran a la puerta de consulta en `|0⟩` [@watrous-2025, L5.4, PDF p. 154].

### Para seguir
La capa 3 recoge el retroceso como patrón de diseño y sus trampas de implementación. Para verlo funcionar en un algoritmo completo, sigue con [Deutsch-Jozsa](deutsch-jozsa.md).

## Profesional {#layer-3}

### Idea clave
Cuando un cálculo clásico debe reflejarse en **fases** para interferir después, el patrón es preparar un registro auxiliar en un vector propio de la operación, aplicar la operación controlada y dejar que el control reciba la fase [@watrous-2025, L5.2, PDF p. 143; L7.2, PDF p. 198].

### Explicación
El auxiliar es `|−⟩` para `X` y el vector propio de `U` en estimación de fase. El patrón se usa en:

- *Construir el oráculo de fase de Grover:* Aaronson señala que los oráculos de fase son más cómodos para [Grover](grover-search.md) [@aaronson-2018, Lec22, p. 3].
- *Deutsch-Jozsa y Bernstein-Vazirani:* el análisis usa "exactamente el mismo retroceso de fase" para llegar a `|−⟩ ⊗ 2^{−n/2} Σ_x (−1)^{f(x)}|x⟩` [@watrous-2025, L5.3, PDF pp. 146-147]. Ver [Deutsch-Jozsa](deutsch-jozsa.md).
- *Estimación de fase:* aplicar `U^j` a un vector propio con valor propio `e^{2πiφ}` da el factor `e^{2πiφj}` sobre `|j⟩` y deja intacto el vector propio [@de-wolf-2026, §4.6, p. 46; @childs-qa, §4.3, p. 19; @shor-mit-2022, L20, p. 3].

Hay tres trampas de implementación:

1. *Devolver el auxiliar a su estado.* El auxiliar solo "se reutiliza" si queda en `|−⟩` (o en el vector propio). Si entre medias se entrelaza con basura, se pierde la interferencia que el algoritmo necesita [@aaronson-2018, Lec17, p. 4].
2. *Versión controlada.* Si hay que activar la consulta de fase solo para ciertos índices, se usa el contraste `|−⟩` / `|+⟩` del objetivo [@de-wolf-2026, §2.4, footnote 7, p. 30]. Que baste una consulta de fase sin control para simular una consulta estándar se plantea como ejercicio abierto [@de-wolf-2026, ej. 2.10, p. 33].
3. *Una consulta, un `U_f`.* Construir `Z_f` cuesta una consulta `U_f` más el auxiliar [@watrous-2025, L8.2, PDF pp. 240-241]; no se duplica el coste del oráculo.

También hay una lectura física. La estimación de fase se puede ver como una medida de von Neumann: la transformación `|ψ⟩|z⟩ → U^z|ψ⟩|z⟩` es exactamente la evolución bajo `H ⊗ p` para un puntero en la base de momentos [@childs-qa, §27.5, p. 137]. Si recuerdas que el valor propio "se deja escrito" en el puntero, la idea de retroceso se vuelve natural.

El patrón no se fuerza cuando el algoritmo no necesita fases. Simon se apoya en las Hadamard del primer registro y deja la salida de `U_f` en un registro aparte con `|0⟩` [@watrous-2025, L5.4, PDF p. 154]. Aun así, el segundo registro no es adorno: sin la consulta, las dos capas de Hadamard se cancelarían (`H² = I`) [@shor-mit-2022, L18, p. 5].

### Ejemplo
Construir el oráculo de fase de Grover. `Z_f` se obtiene de `U_f` con un qubit de trabajo en `|−⟩`: una sola consulta `U_f` deja el signo `(−1)^{f(x)}` en `|x⟩`, y el qubit de trabajo sigue en `|−⟩`, y puede reutilizarse [@watrous-2025, L8.2, PDF pp. 240-241].

### Para seguir
La [estimación de fase](phase-estimation.md) lleva este patrón a una unitaria cualquiera, con la transformada de Fourier inversa para leer el resultado.
