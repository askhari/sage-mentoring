---
domain: math-foundations
title: "Matemáticas para lo cuántico"
---

# Matemáticas para lo cuántico

Este ámbito es un repaso de álgebra lineal y probabilidad pensado para quien programa y quiere llegar a la computación cuántica. No es un curso de matemáticas completo: cada concepto explica la matemática y, desde el primer nivel, para qué se usa después (amplitudes, vectores de estado, puertas, probabilidades de medida, sistemas de varios qubits). La física se deja para los ámbitos siguientes.

## Por qué importa

En computación cuántica el estado de un sistema es un vector de números complejos cuyos cuadrados de módulo suman 1; la fuente de Watrous dice que todas las diferencias entre información cuántica y clásica salen de ese cambio [@watrous-2025, L1.2, p. 18]. Las operaciones son matrices unitarias y la medida convierte amplitudes en probabilidades. Con estas piezas se puede leer casi cualquier algoritmo cuántico como lo que es: álgebra lineal con reglas de medida.

## Cómo se conectan los conceptos

1. [Números complejos](concepts/complex-numbers.md): los escalares de todo lo demás; las amplitudes son complejas y la fase importa.
2. [Vectores y notación de Dirac](concepts/vectors-and-dirac-notation.md): el estado como columna de amplitudes y la notación `|ψ⟩`, `⟨ψ|`.
3. [Producto interior, norma y ortogonalidad](concepts/inner-products-and-norms.md): longitud (los estados tienen norma 1), ángulos y probabilidades de medida.
4. [Matrices y aplicaciones lineales](concepts/matrices-and-linear-maps.md): las puertas como matrices que actúan sobre vectores.
5. [Matrices unitarias y hermíticas](concepts/unitary-and-hermitian-matrices.md): las matrices que conservan la norma (puertas) y las que representan magnitudes medibles.
6. [Valores y vectores propios](concepts/eigenvalues-and-eigenvectors.md): las direcciones que una matriz no gira; base de la descomposición espectral y de `e^{-iHt}`.
7. [Producto tensorial](concepts/tensor-products.md): cómo se combinan sistemas; origen del crecimiento exponencial y del entrelazamiento.
8. [Probabilidad básica](concepts/probability-basics.md): vectores de probabilidad como contraste con los de amplitud, y las herramientas para analizar algoritmos que fallan con cierta probabilidad.

## Orden de estudio recomendado

Sigue la lista anterior. Probabilidad básica no depende de los demás y se puede leer antes o en paralelo; resulta más útil después de producto interior y producto tensorial, porque comparte con ellos la idea de estados conjuntos e independencia.

## Fuentes y niveles

Las tres fuentes se complementan. Axler da el rigor y los teoremas de álgebra lineal en abstracto, sin notación de Dirac [@axler-2024, §1A, 6A, 7B]. Watrous presenta los mismos objetos directamente con estados cuánticos y notación de Dirac [@watrous-2025, L1.1, L1.2]. De Wolf resume lo necesario en sus apéndices A y B [@de-wolf-2026, App. A, App. B]. Cuando coinciden, se cita la más clara; cuando difieren en convenciones, se dice.
