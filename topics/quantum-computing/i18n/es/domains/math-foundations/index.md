---
domain: math-foundations
title: "Matemáticas para lo cuántico"
format: 2
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

## Fundamentos {#layer-1}

La capa de fundamentos recorre los ocho conceptos en el orden de la lista anterior. Empieza por los números complejos, que son los escalares de todo lo demás, sigue con los vectores y la notación de Dirac, y con el producto interior que da norma y ortogonalidad. Después pasa a las matrices, a las unitarias y hermíticas, a los valores propios y al producto tensorial, y cierra con la probabilidad básica como contraste con las amplitudes. No se apoya en nada fuera del ámbito; cada concepto da por sabido solo lo anterior.

## Comprensión {#layer-2}

La capa de comprensión explica el porqué de cada herramienta: por qué hacen falta los complejos, qué distingue la fase global de la relativa, por qué las bases ortonormales simplifican los cálculos, cómo se relacionan unitarias, hermíticas y proyectores, cuándo una matriz se diagonaliza, qué es un estado entrelazado y en qué se parecen y se diferencian probabilidades y amplitudes. Parte de lo visto en fundamentos y mantiene el mismo orden de lectura.

## Profesional {#layer-3}

La capa profesional lleva estas matemáticas al uso diario: convenciones que cambian entre textos y bibliotecas (dónde se conjuga el producto interior, el orden de los qubits en Qiskit), el teorema espectral y `e^{-iHt}`, la traza, el rango y la descomposición en valores singulares, las puertas escritas como productos tensoriales y las cotas de probabilidad con las que se analiza el error de un algoritmo. Se apoya en las dos capas anteriores y en el mismo orden.

## Lecturas complementarias

Las tres fuentes se complementan. Axler da el rigor y los teoremas de álgebra lineal en abstracto, sin notación de Dirac [@axler-2024, §1A, 6A, 7B]. Watrous presenta los mismos objetos directamente con estados cuánticos y notación de Dirac [@watrous-2025, L1.1, L1.2]. De Wolf resume lo necesario en sus apéndices A y B [@de-wolf-2026, App. A, App. B]. Cuando coinciden, se cita la más clara; cuando difieren en convenciones, se dice.
