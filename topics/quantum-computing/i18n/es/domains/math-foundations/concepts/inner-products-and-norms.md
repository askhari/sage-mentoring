---
concept: inner-products-and-norms
title: "Producto interior, norma y ortogonalidad"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
La **norma (norm)** mide la longitud de un vector y el **producto interior (inner product)** mide cuánto se parecen dos. Los estados cuánticos son los vectores de norma 1, y las probabilidades de medida salen de productos interiores [@watrous-2025, L1.2, pp. 18-19; @de-wolf-2026, §1.2.2, p. 16].

### Explicación
La norma de un vector de `C^n` es la raíz de la suma de los módulos al cuadrado: `‖v‖ = √(Σ|v_i|²)`, la longitud euclídea de siempre [@de-wolf-2026, App. A.3, p. 206]. Los vectores de estado cuánticos son exactamente los vectores de norma 1 [@watrous-2025, L1.2, pp. 18-19].

El producto interior de dos vectores es `⟨v|w⟩ = Σ_i conj(v_i)·w_i`: la fila conjugada de `v` por la columna `w` [@de-wolf-2026, App. A.3, p. 206; @watrous-2025, L3.2, p. 80]. Se conjuga porque con módulos `‖z‖² = Σ|z_k|²`, y por eso intercambiar los argumentos conjuga el resultado [@axler-2024, §6A, PDF pp. 200-201]. Se cumple `⟨ψ|ψ⟩ = ‖ψ‖²` [@watrous-2025, L3.2, p. 81].

Dos vectores son **ortogonales (orthogonal)** si `⟨v|w⟩ = 0`, y **ortonormales (orthonormal)** si además tienen norma 1 [@de-wolf-2026, App. A.3, p. 206]. En `R²`, `⟨u,v⟩ = ‖u‖‖v‖cos θ`, de ahí que ortogonal signifique perpendicular [@axler-2024, def. 6.10, 6.11, PDF p. 205].

Esto sirve para la regla de Born: al medir `|φ⟩ = Σα_j|j⟩` en la base computacional se obtiene `j` con probabilidad `|α_j|²`, por lo que el vector de amplitudes debe tener norma 1 [@de-wolf-2026, §1.2.2, p. 16]. Si se mide en otra base ortonormal `{ψ_j}`, la probabilidad es `|⟨φ|ψ_j⟩|²` [@de-wolf-2026, §1.2.2, p. 17].

### Ejemplo
- `⟨0|1⟩ = 0` y `⟨0|0⟩ = 1`: la base estándar es ortonormal.
- `⟨+|-⟩ = (1/√2)(1/√2) + (1/√2)(-1/√2) = 1/2 - 1/2 = 0`: `|+⟩` y `|-⟩` son ortogonales y forman otra base ortonormal [@watrous-2025, L3.2, p. 83].
- Con complejos: `ψ = (1, i)ᵀ`, `φ = (1, 1)ᵀ` dan `⟨ψ|φ⟩ = conj(1)·1 + conj(i)·1 = 1 - i`, mientras que `⟨φ|ψ⟩ = 1 + i`; son conjugados entre sí.
- Medir `|+⟩` en la base estándar da `|⟨0|+⟩|² = (1/√2)² = 1/2`.

### Errores frecuentes
- *"El producto interior es simétrico."* `⟨v|w⟩ = conj(⟨w|v⟩)`. Para una probabilidad da igual, porque se usa el módulo al cuadrado.

### Para seguir
[Matrices y aplicaciones lineales](matrices-and-linear-maps.md) estudia las operaciones que actúan sobre estos vectores. La capa 2 de este concepto muestra por qué las bases ortonormales son tan cómodas.

## Comprensión {#layer-2}

### Idea clave
En una base ortonormal los coeficientes de un vector son simples productos interiores y la norma se reparte entre ellos (Parseval); la regla de Born en cualquier base es exactamente eso [@axler-2024, 6.30, 6.31, PDF pp. 218-219].

### Explicación
El producto interior es simétrico conjugado, `⟨ψ|φ⟩ = conj(⟨φ|ψ⟩)`, definido positivo (`⟨ψ|ψ⟩ ≥ 0`, con igualdad solo para el vector cero), lineal en un argumento y conjugado-lineal en el otro [@watrous-2025, L3.2, pp. 81-82]. La norma cumple `‖λv‖ = |λ|‖v‖` [@axler-2024, 6.9, PDF p. 204].

De esas propiedades salen los resultados básicos:

- **Pitágoras:** si `u ⊥ v`, entonces `‖u+v‖² = ‖u‖² + ‖v‖²` [@axler-2024, 6.12, PDF p. 205].
- **Cauchy-Schwarz:** `|⟨u,v⟩| ≤ ‖u‖‖v‖`, con igualdad si y solo si un vector es múltiplo del otro; de ella sale la desigualdad triangular [@axler-2024, 6.14, 6.17, PDF pp. 207-208].
- Para vectores unitarios, `Re⟨v|w⟩ = 1 - ½‖v-w‖²`: vectores unitarios cercanos tienen producto interior cercano a 1 [@de-wolf-2026, App. A.3, p. 206].

Una lista ortonormal es automáticamente linealmente independiente, y una de longitud `dim V` es una base ortonormal [@axler-2024, 6.24, 6.25, 6.28, PDF pp. 216-217]. Toda lista ortonormal se puede extender a una base ortonormal, por ejemplo con Gram-Schmidt [@watrous-2025, L3.2, p. 83].

La ventaja de estas bases es que, si `e₁..e_n` es una base ortonormal, entonces `v = Σ⟨e_k|v⟩ e_k` en notación de física (en la de Axler, `Σ⟨v,e_k⟩ e_k`) y `‖v‖² = Σ|⟨e_k|v⟩|²` (Parseval): los coeficientes son productos interiores, sin resolver ningún sistema lineal [@axler-2024, 6.30, 6.31, PDF pp. 218-219]. Es lo que hace la regla de Born en una base `{ψ_j}`: las amplitudes en esa base son `⟨ψ_j|φ⟩` y la normalización es Parseval.

![Descomposición de un vector en una base ortonormal](../../../../../assets/diagrams/orthonormal-projection.es.svg)

El mismo argumento da la proyección. Para `v ≠ 0`, `u = (⟨u,v⟩/‖v‖²) v + w` con `w` ortogonal a `v` [@axler-2024, 6.13, PDF p. 206]. Con `v` unitario, el término `⟨v,u⟩v` de Axler es en física `|v⟩⟨v|u⟩`, es decir, la matriz proyector `|v⟩⟨v|` aplicada a `u` (ver [matrices unitarias y hermíticas](unitary-and-hermitian-matrices.md)).

Hay una consecuencia física: dos estados no ortogonales (`⟨φ|ψ⟩ ≠ 0`) no se pueden distinguir con certeza; los estados perfectamente distinguibles deben ser ortogonales [@watrous-2025, L3.3, p. 95; la demostración continúa más allá de lo leído].

### Ejemplo
En la base `{|+⟩, |-⟩}` un vector `|φ⟩` tiene amplitudes `⟨+|φ⟩` y `⟨-|φ⟩`, y por Parseval `|⟨+|φ⟩|² + |⟨-|φ⟩|² = ‖φ‖² = 1`. Tomando `|φ⟩ = |0⟩`: `⟨+|0⟩ = 1/√2` y `⟨-|0⟩ = 1/√2`, cuyos cuadrados suman 1 (cálculo directo con los vectores de la capa 1).

### Para seguir
La capa 3 aclara la convención de conjugación, que cambia entre textos, y usa Gram-Schmidt. El siguiente concepto del ámbito es [matrices y aplicaciones lineales](matrices-and-linear-maps.md).

## Profesional {#layer-3}

### Idea clave
Los textos no conjugan el mismo argumento del producto interior: hay que fijar la convención antes de traducir un teorema. Además, el producto interior se factoriza con `⊗` y mide la fidelidad entre estados puros [@watrous-2025, L3.2, pp. 80-82; L12.2, PDF pp. 368-369].

### Explicación
Gram-Schmidt convierte una lista independiente `v₁..v_m` en una ortonormal con el mismo span en cada paso, restando a `v_k` sus componentes sobre los vectores anteriores y normalizando [@axler-2024, 6.32, PDF p. 219]. Garantiza que todo espacio de dimensión finita tiene una base ortonormal y que cualquier lista ortonormal se extiende a una [@axler-2024, 6.35, 6.36, PDF pp. 220-221]. Sirve para completar un conjunto de vectores ortonormales a una matriz unitaria [@watrous-2025, L3.2, p. 85].

El teorema de Riesz cierra el vínculo con la notación de Dirac. En dimensión finita, todo funcional lineal es de la forma `φ(u) = ⟨u,v⟩` para un único `v` [@axler-2024, 6.42, PDF p. 223]. En notación de Dirac es la correspondencia ket ↔ bra, y de ella sale la existencia del adjunto [@axler-2024, def. 7.1, 7.4, PDF pp. 246-247].

Con productos tensoriales, `‖φ⊗ψ‖ = ‖φ‖‖ψ‖` [@watrous-2025, L2.2, p. 51]. Además el producto interior se factoriza: `⟨v⊗w, u⊗x⟩ = ⟨v,u⟩⟨w,x⟩` [@axler-2024, 9.80, 9.82, PDF pp. 394-395]. Así, los estados de base de `n` qubits son ortogonales si y solo si difieren en algún bit [@de-wolf-2026, §1.3, p. 19]. Ver [producto tensorial](tensor-products.md).

La norma induce la distancia `‖v-w‖` [@de-wolf-2026, App. A.3, p. 206]. Junto con la identidad `Re⟨v|w⟩ = 1 - ½‖v-w‖²`, justifica usar `|⟨v|w⟩|` como medida de cuán parecidos son dos estados (salvo fase global). Para estados puros `|⟨φ|ψ⟩|` es la **fidelidad (fidelity)**: vale 0 si los estados son ortogonales y 1 si son iguales salvo fase global [@watrous-2025, L12.2, PDF pp. 368-369].

### Ejemplo
Traducir un resultado entre convenciones. Con Axler: `⟨u,v⟩_Axler = Σ u_k conj(v_k) = ⟨v|u⟩_física`, de modo que al pasar un teorema a notación de física hay que intercambiar los argumentos; el producto euclídeo de Axler es la suma de `w_k` por `conj(z_k)` [@axler-2024, ex. 6.3, PDF p. 202]. Los textos de física escriben `⟨φ|A|ψ⟩`, el producto interior de `|φ⟩` con `A|ψ⟩`, conjugando `φ`.

### Las fuentes discrepan
Axler es lineal en el primer argumento y conjugado-lineal en el segundo, y señala que muchos físicos usan la convención opuesta [@axler-2024, def. 6.2 y nota posterior, PDF p. 202]. De Wolf conjuga el primero (convención de física; los matemáticos suelen conjugar el segundo) [@de-wolf-2026, App. A.3, p. 206]. Watrous también [@watrous-2025, L3.2, pp. 80-82]. El adjunto (`⟨Tv,w⟩ = ⟨v,T*w⟩`) es igual en ambas convenciones; lo que cambia es dónde caen los conjugados al expandir en coordenadas.

Sobre la fidelidad, algunos autores llaman así a su cuadrado, así que conviene comprobar la definición en cada texto [@watrous-2025, L12.2, PDF pp. 368-369].

### Para seguir
[Matrices y aplicaciones lineales](matrices-and-linear-maps.md), capa 3, añade traza, rango y valores singulares.
