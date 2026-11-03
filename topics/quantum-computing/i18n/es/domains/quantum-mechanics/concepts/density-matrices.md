---
concept: density-matrices
title: "Matrices densidad y estados mixtos"
---

## Comprensión {#layer-2}

**El problema.** El vector de estado describe un sistema aislado y bien preparado. Pero a menudo (1) no sabemos exactamente qué estado se preparó, o (2) solo vemos una parte de un sistema mayor. En esos casos los estados no son rayos, las medidas no son proyecciones ortogonales y la evolución no es unitaria [@preskill-ph219, ch.2 §2.3.1, p. 17]. La herramienta es la **matriz densidad (density matrix)** `ρ`.

**Definición.** Un estado general es una matriz `ρ` con traza 1 y semidefinida positiva (`ρ ≥ 0`), formulación que puede describir ruido y el estado de una parte aislada de un sistema [@watrous-2025, L9 intro, PDF pp. 261-262; L9.1, PDF p. 263]. "Semidefinida positiva" equivale a `P = M†M`, a ser hermítica con valores propios no negativos, o a `⟨ψ|P|ψ⟩ ≥ 0` para todo `|ψ⟩`; no significa que las entradas sean no negativas [@watrous-2025, L9.1, PDF pp. 263-264]. (Repaso: [matrices hermíticas](../../math-foundations/concepts/unitary-and-hermitian-matrices.md), [valores propios](../../math-foundations/concepts/eigenvalues-and-eigenvectors.md).)

**Estados puros y mixtos.** Un vector `|ψ⟩` corresponde a `|ψ⟩⟨ψ|`, un estado puro: una proyección de rango 1 con un valor propio 1 y el resto 0, sin incertidumbre; no toda matriz densidad es pura [@watrous-2025, L9.1, PDF pp. 265-267]. Equivalentemente, un estado puro cumple `ρ² = ρ`, y uno mixto `ρ = Σ pₐ|a⟩⟨a|` con dos o más términos tiene `tr ρ² = Σpₐ² < 1`, una mezcla incoherente en la que las fases relativas son inaccesibles [@preskill-ph219, ch.2 §2.3.1, pp. 20-21].

**Cómo leer las entradas.** Las diagonales son las probabilidades de la medida en la base estándar; las no diagonales dicen cuánta superposición hay entre dos estados clásicos, con su fase relativa [@watrous-2025, L9.1, PDF p. 265]. Los estados probabilísticos clásicos son exactamente las matrices diagonales: sin términos no diagonales solo hay aleatoriedad clásica y no hay superposición [@watrous-2025, L9.2, PDF pp. 271-272].

**Mezclar estados.** Una elección aleatoria de estados es la combinación convexa `Σ pₖρₖ`. Promediar vectores de estado no funciona (el resultado puede no tener norma 1, y `(|ψ⟩ + (−|ψ⟩))/2` es cero). Por ejemplo, `(|0⟩⟨0| + |+⟩⟨+|)/2 = [[3/4,1/4],[1/4,1/4]]` [@watrous-2025, L9.2, PDF pp. 268-269].

**La misma matriz con distintos orígenes.** `I/2` surge de `{|0⟩,|1⟩}`, de `{|+⟩,|−⟩}` o de cualquier pareja de estados ortogonales, y ninguna medida distingue las preparaciones [@watrous-2025, L9.2, PDF pp. 269-271]. Un estado puro, en cambio, tiene una única preparación [@preskill-ph219, ch.2 §2.5.2, pp. 28-30]. Es la diferencia con una distribución clásica, que tiene descomposición única.

**Lo que ve un subsistema.** Para `|ψ⟩_AB = a|00⟩ + b|11⟩`, los valores esperados de observables sobre A valen `tr(M_A ρ_A)` con `ρ_A = |a|²|0⟩⟨0| + |b|²|1⟩⟨1|` [@preskill-ph219, ch.2 §2.3.1, p. 18]. En general, `ρ_A = tr_B(|ψ⟩⟨ψ|)` es la **traza parcial (partial trace)**, hermítica, positiva y de traza 1 [@preskill-ph219, ch.2 §2.3.1, pp. 19-20]; se caracteriza por `Tr_B(M⊗N) = Tr(N)M`, y para el e-bit `|φ⁺⟩` el estado reducido de cada qubit es `I/2` [@watrous-2025, L9.4, PDF pp. 285-289]. Aunque el todo esté en un estado puro, un subsistema en general no lo está, y entrelazar A con B hace inaccesibles las fases de A [@preskill-ph219, ch.2 §2.3.1, p. 21]. Un estado puro entrelazado tiene reducido mixto; los cuatro estados de Bell dan `I/2` en cada qubit [@watrous-2025, L9.4, PDF p. 286; L12.1, PDF p. 364]. Ver [producto tensorial](../../math-foundations/concepts/tensor-products.md).

**Ejemplo clave: superposición frente a mezcla.** `(|↑_z⟩ + |↓_z⟩)/√2` da `σ₁ = +1` con certeza, mientras que el conjunto `↑_z/↓_z` a partes iguales es `ρ = I/2` y da 1/2 en todos los ejes [@preskill-ph219, ch.2 §2.3.1, pp. 18-19]. Es el [principio de superposición](superposition-principle.md) en versión matricial: la fase relativa vive en los términos no diagonales.

**Por qué importa en computación cuántica.** Todos los sistemas reales están imperfectamente aislados e intercambian energía e información con un entorno [@preskill-ph219, ch.2 §2.1, p. 3], por lo que un estado "puro" ideal es una aproximación. La matriz densidad permite describir el ruido (ver [decoherencia](decoherence.md)), el estado de un qubit dentro de un registro y los resultados de medidas generales.

**Errores frecuentes.**

- *"Mixto significa superposición."* Una mezcla es ignorancia clásica o la parte de un entrelazado; una superposición tiene fases relativas accesibles.
- *"Cada matriz mixta tiene una descomposición única."* Tiene infinitas [@preskill-ph219, ch.2 §2.5.2, pp. 28-30].

## Profesional {#layer-3}

**La bola de Bloch.** Para un qubit, `ρ(P) = (I + P·σ)/2`, válida si y solo si `|P| ≤ 1`: las matrices densidad de un qubit llenan una bola unidad (la "esfera de Bloch" es, en rigor, una bola), y la superficie `|P| = 1` son los estados puros; `⟨n·σ⟩ = n·P`, y `P` se mide con tres ejes independientes [@preskill-ph219, ch.2 §2.3.2, pp. 21-22]. Con la parametrización de un estado puro `cos(θ/2)|0⟩ + e^{iφ}sin(θ/2)|1⟩`, el vector `(x,y,z)` es unitario; `|0⟩` y `|1⟩` son los polos, `|±⟩` el eje `x` y `|±i⟩` el eje `y`; los estados ortogonales son puntos antípodas, y `I/2` es el centro [@watrous-2025, L9.3, PDF pp. 275-281]. Este concepto se presenta como herramienta de qubits en [esfera de Bloch](../../qubits-and-circuits/concepts/bloch-sphere.md). Zurek usa la misma imagen: cualquier evolución cuántica transforma la esfera en un elipsoide dentro de ella [@zurek-2003, §IV.A.1, p. 15].

**Convexidad.** Los operadores densidad forman un conjunto convexo cuyos puntos extremos son exactamente los estados puros; para `d > 2` la frontera contiene estados no puros, a diferencia de la bola del qubit [@preskill-ph219, ch.2 §2.5.1, pp. 26-28].

**Sin señales más rápidas que la luz.** La ambigüedad de descomposición no permite comunicación: la elección de Bob de medir B en distintas bases prepara conjuntos distintos para Alice pero el mismo `ρ_A`, que no puede distinguir sin el mensaje clásico de Bob [@preskill-ph219, ch.2 §2.5.3, pp. 30-31]. Es la única descripción coherente con la ausencia de señales para el e-bit [@watrous-2025, L9.4, PDF pp. 285-289].

**Descomposición de Schmidt y purificación.** Todo estado puro bipartito es `Σ √pᵢ |i⟩_A|i'⟩_B`; `ρ_A` y `ρ_B` tienen los mismos valores propios no nulos y un número de Schmidt mayor que 1 indica entrelazamiento [@preskill-ph219, ch.2 §2.4, pp. 23-26]. Watrous obtiene lo mismo: el número de términos es el rango del estado reducido [@watrous-2025, L12.1, PDF pp. 358-362]. Para toda `ρ` de `X` existe un estado puro de `(X,Y)` con `Tr_Y = ρ`; dos purificaciones difieren en una unitaria sobre `Y` [@watrous-2025, L12.1, PDF pp. 356-363]. El teorema HJW dice que dos descomposiciones cualesquiera de `ρ_A` vienen de purificaciones relacionadas por una unitaria sobre B, y es la forma general del "borrador cuántico" [@preskill-ph219, ch.2 §2.5.4-2.5.5, pp. 31-36].

**Fidelidad.** Entre dos estados puros es `|⟨φ|ψ⟩|`; la definición general es `F(ρ,σ) = Tr√(√ρ σ √ρ)` y, atención, algunos autores definen la fidelidad como el cuadrado de esta cantidad [@watrous-2025, L12.2, PDF pp. 368-369]. Tenlo en cuenta al comparar cifras de distintos artículos.

**Formulación abierta de la mecánica cuántica.** Un estado es un operador densidad, una medida un POVM (probabilidad `tr(Eₐρ)`) y la dinámica un mapa completamente positivo que conserva la traza; los axiomas cerrados se recuperan con purificaciones y dilataciones [@preskill-ph219, ch.3 §3.3.3, p. 23]. Son los [canales de ruido](../../error-correction/concepts/quantum-noise-channels.md).

**Cómo decidir.** Usa vectores de estado cuando el sistema es cerrado y conocido; usa matrices densidad en cuanto haya ruido, mezcla estadística de preparaciones o subsistemas entrelazados. Una matriz densidad no es "un vector más general" sin más: dos estados dan las mismas estadísticas en toda medida si y solo si sus matrices densidad coinciden [@watrous-2025, L9.1, PDF pp. 267-268].
