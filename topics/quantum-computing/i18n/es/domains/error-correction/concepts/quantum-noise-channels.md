---
concept: quantum-noise-channels
title: "Ruido cuántico y canales de error"
format: 2
---

## Comprensión {#layer-2}

### Idea clave
Un qubit puede sufrir un continuo de errores, pero al medir el síndrome ese continuo se reduce a cuatro opciones de Pauli (`I`, `X`, `Y`, `Z`): un código que corrige `X` y `Z` corrige cualquier error sobre un qubit [@de-wolf-2026, §21.3, p. 197 [185]].

### Explicación
Se asumen [las matrices de densidad](../../quantum-mechanics/concepts/density-matrices.md) y [la coherencia y la fidelidad](../../quantum-hardware/concepts/coherence-and-fidelity.md); aquí no se repiten.

En un bit clásico solo hay un error posible, voltearlo. Un qubit puede sufrir una rotación diminuta de cualquier ángulo, y además el entorno puede interactuar con él. Corregir errores cuánticos es más difícil por tres motivos: no se pueden copiar los estados ([no clonación](../../qubits-and-circuits/concepts/no-cloning.md)), hay un continuo de errores posibles y mirar el estado para comprobarlo puede colapsarlo [@de-wolf-2026, §21.3, p. 196 [184]]. La salida es que el continuo se reduce a cuatro opciones.

Esas cuatro opciones son las matrices de Pauli leídas como errores: `I` es no error, `X` es un volteo de bit (*bit-flip*), `Z` es un volteo de fase (*phase-flip*) e `Y = iXZ` es ambos a la vez, salvo una fase global [@de-wolf-2026, §21.3, pp. 196-197 [184-185]; @watrous-2025, L13.1, PDF p. 383]. Este modelo cubre una gama amplia de errores de un qubit [@fowler-2012, p. 4].

La reducción se llama discretización de errores (*error discretization*). Las cuatro matrices de Pauli generan todas las matrices 2×2, así que cualquier error unitario sobre un qubit se escribe `E = a₀I + a₁X + a₂Y + a₃Z`, con los módulos al cuadrado sumando 1. Por linealidad, un código que corrige `X` y `Z` (y por tanto `Y`) en un qubit corrige cualquier error unitario sobre ese qubit; lo mismo vale para `k` qubits con productos tensoriales de `k` Paulis [@de-wolf-2026, §21.3, p. 197 [185]].

Lo que lo hace físico es la propia medida. Al medir el síndrome, el estado `E|palabra⟩` colapsa a uno en el que ocurrió un error de Pauli concreto (o ninguno), con probabilidad igual al módulo al cuadrado de su coeficiente, y entonces se deshace [@watrous-2025, L13.3, PDF pp. 402-405; @de-wolf-2026, §21.4, p. 199 [187]]. Tras corregir, el estado queda como producto: la codificación queda limpia y la aleatoriedad (la entropía) se queda en los qubits de síndrome, que se descartan o se reinician [@watrous-2025, L13.3, PDF p. 404].

Si el error no es unitario, porque viene de interactuar con el entorno, se toma una representación de Kraus del canal, se expande cada matriz 2×2 de Kraus en `I, X, Y, Z` y el mismo argumento de síndrome y corrección vale. Los canales de desfase (*dephasing*), despolarizante (*depolarizing*) y de reinicio (*reset*) son ejemplos; los detalles son más enrevesados y se omiten [@watrous-2025, L13.3, PDF pp. 405-406]. Los errores no unitarios también se pueden corregir, aunque no se tratan en las notas de De Wolf [@de-wolf-2026, §21.3, nota 2, p. 197 [185]]. Para el desfase y su relación con T1 y T2, ver [decoherencia](../../quantum-mechanics/concepts/decoherence.md) y [coherencia y fidelidad](../../quantum-hardware/concepts/coherence-and-fidelity.md).

Para analizar un código hace falta además un modelo de cuándo ocurren los errores. El estándar es que cada qubit sufre un error con probabilidad `p`, de forma independiente y sin correlaciones; en el análisis del código de Shor se toma como peor caso los errores `Y` [@watrous-2025, L13.2, PDF p. 400]. Sobre `S` qubits y `T` pasos de tiempo, con puertas en paralelo sobre qubits disjuntos, una puerta imperfecta se modela como puerta perfecta seguida de un error de ese tipo, lo que no es del todo general [@de-wolf-2026, §21.3, p. 196 [184]].

Aun así, los errores se propagan. Una puerta de dos qubits copia errores: una `X` en el control de una CNOT se convierte en `X` en los dos qubits, y una `Z` en el objetivo se propaga al control [@watrous-2025, L16.2, PDF pp. 476-477]. Por eso en un circuito real no basta con "una probabilidad `p` por qubit": hay que contar cada lugar donde algo puede fallar (puertas, preparaciones, medidas, esperas) [@watrous-2025, L16.1, PDF pp. 472-473]. Ese es el modelo *a nivel de circuito (circuit-level)*: cada operación falla con probabilidad `p`; una CNOT defectuosa es una CNOT ideal más uno de los 15 Paulis de dos qubits no triviales, a partes iguales (`p/15` cada uno en Fowler); una medida defectuosa voltea el bit clásico del resultado, y una espera añade `X`, `Y` o `Z` al azar [@fowler-2012, pp. 11-12; @bravyi-2024, §6, p. 16].

### Ejemplo
Un pequeño error de fase `diag(1, e^{iφ})` es sobre todo `I` con un componente `Z` pequeño, de modo que basta un código que corrija `Z` para tratarlo [@de-wolf-2026, §21.3, p. 197 [185]; ej. 1, p. 201 [189]].

El canal despolarizante se ve igual de concreto. Con probabilidad `1−p` no pasa nada y con probabilidad `p` el qubit se sustituye por el estado maximamente mezclado `I/2`. En la base de Pauli de la matriz de densidad, el coeficiente de `I` (que vale `1/2`) se conserva y los de `X`, `Y` y `Z` se encogen por el factor `1−p` [@de-wolf-2026, ej. 7, p. 202 [190]].

### Errores frecuentes
- *"Como los errores son continuos, harían falta correcciones analógicas."* La medida del síndrome discretiza el error, y un código que corrige `X` y `Z` corrige cualquier error de un qubit [@de-wolf-2026, §21.3, p. 197 [185]; @watrous-2025, L13.1, PDF p. 386].
- *"Un error pequeño se acumula hasta alterar el qubit lógico."* Un error unitario diminuto no puede cambiar el estado lógico: una operación sobre un solo qubit solo puede sacar el estado del espacio de código, y la detección lo hace colapsar de nuevo [@watrous-2025, L13.3, PDF p. 405].
- *"Todo el ruido es independiente."* Es la hipótesis de partida, no la realidad. Ver la capa profesional.

### Para seguir
La capa 3 muestra dónde falla el modelo independiente en dispositivos reales y cómo elegir el modelo de ruido; el efecto del ruido sobre un código se resume en el [teorema del umbral](threshold-theorem.md).

## Profesional {#layer-3}

### Idea clave
El modelo de errores independientes permite demostrar teoremas y comparar códigos, pero los dispositivos reales tienen correlaciones, errores coherentes y errores localizados que el modelo no ve; hay que elegir el modelo de ruido según lo que se quiera decidir [@watrous-2025, L16.1, PDF pp. 473-474; @google-2025, p. 4].

### Explicación
Los dispositivos reales tienen correlaciones, y existen hipótesis de ruido más débiles que la independencia [@watrous-2025, L16.1, PDF pp. 473-474]. Para decidir si un resultado de un dispositivo se parece al modelo hay que mirar los errores correlacionados, y los experimentos de Google los muestran:

- *Fuga (leakage) y interacciones residuales.* En el procesador de 72 qubits, los errores correlacionados (fuga y acoplamientos residuales entre qubits durante las puertas CZ) suponen alrededor del 17 % del presupuesto de error, y los autores esperan que su peso crezca al bajar el resto [@google-2025, p. 4]. Quitar la fuga de los qubits de datos (DQLR) apenas cambia el código de distancia 3, pero sube Λ un 35 % en el de distancia 5, mientras la probabilidad de detección baja solo un 12 %. La probabilidad de detección es un buen indicador de Λ solo si los errores no están correlacionados [@google-2025, p. 4, Fig. 2d].
- *Ráfagas de errores.* En un código de repetición de distancia 29 (2·10¹⁰ ciclos, 5,5 horas), la supresión deja de ser exponencial a partir de `d ≥ 15` y aparece un suelo cercano a 10⁻¹⁰ de error lógico por ciclo. Lo causan ráfagas raras y localizadas (unos 30 qubits), seis en 2·10¹⁰ ciclos (más o menos una por hora), con decaimiento de unos 370-400 µs; su origen no se entiende [@google-2025, pp. 1, 4-5, Fig. 3d].
- Las inyecciones de errores muestran potencias ajustadas solo al 80 % del exponente ideal `(d+1)/2`, que se atribuyen a correlaciones en exceso [@google-2025, p. 3, Fig. 2b].

Un error cuya posición se conoce es más fácil de corregir; se llama borrado (*erasure*). En átomos neutros, una fuga detectada en un sitio conocido se convierte en un error de borrado, y el umbral de un código puede subir casi un orden de magnitud si los borrados dominan y están sesgados [@saffman-2025, pp. 21-22].

Otra distinción es entre ruido coherente y estocástico. Los errores coherentes (rotaciones unitarias sistemáticas) se acumulan más rápido que los errores de Pauli; una de las formas más eficaces de tratarlos es convertirlos en ruido de Pauli mediante el *twirling* de Pauli: insertar Paulis aleatorios que eliminan los términos fuera de la diagonal y convierten cualquier canal en un canal de Pauli, a menudo con poco coste porque los Paulis insertados se absorben en puertas existentes [@cai-2023, Sec. V.A, p. 27; App. A.2, pp. 32-33]. El truco se plantea en [mitigación de errores](../../qiskit-programming/concepts/error-mitigation.md), pero sirve también para analizar un código. En la otra dirección, un circuito lógico de átomos neutros es más tolerante a errores coherentes y se comporta de forma "inherentemente digital", de acuerdo con la teoría [@bluvstein-2024, p. 7].

Conviene también saber qué clase de error domina, para saber dónde mirar:

- En la simulación de Fowler (2012) las CNOT son la fuente que más cuenta: umbral de 1,25 % por paso si solo fallan las CNOT, frente a 4,3 % para las esperas de qubits de datos y alrededor del 12 % para inicialización, medida y Hadamard de los qubits de medida [@fowler-2012, p. 13, Eq. 13, Figs. 7-8].
- En el experimento de Google los errores de CZ, locales y correlacionados, son los mayores contribuyentes [@google-2025, p. 4].
- La elección de plataforma cambia el perfil: en átomos neutros hay tres canales nuevos (calentamiento, fuga y pérdida) [@saffman-2025, p. 21].

### Ejemplo
Cómo decidir qué modelo usar en una simulación propia:

1. *Para entender un código:* errores de Pauli independientes sobre los qubits de datos y síndrome perfecto. Es el modelo de [repetición](repetition-codes.md) y de [Shor](shor-code.md).
2. *Para estimar un umbral o un coste:* ruido a nivel de circuito, porque es el que incluye los errores de la propia extracción del síndrome; las cifras salen más bajas que con el modelo ingenuo, lo que se atribuye a que incluye más tipos de error [@fowler-2012, pp. 11-12].
3. *Para juzgar un dispositivo:* medir si hay correlaciones, no solo el error medio por puerta. Un `Λ` bueno con ráfagas sin explicar no garantiza el régimen de `10⁻¹²` que necesita un algoritmo (ver [experimentos con qubits lógicos](logical-qubit-experiments.md)).

### Las fuentes discrepan
Las cifras de borrado de Bartolucci y colaboradores (PsiQuantum, solo simulaciones) no son comparables con las de un código de superficie con circuitos: modelan por separado la probabilidad de borrado y la de error de Pauli de cada medida de fusión y obtienen umbrales de 11,98 % frente a borrado y 1,07 % frente a error de Pauli para su red de anillos de 6, en una arquitectura fotónica basada en fusiones [@bartolucci-2023, §I, p. 1; §VI.C.1, p. 13].

Está abierta la cuestión de cómo cambia el umbral con ruido sesgado hacia errores de medida, que según IBM dominan en los qubits superconductores [@bravyi-2024, p. 31].

### Para seguir
El efecto del ruido sobre un código se resume en el [teorema del umbral](threshold-theorem.md), y su versión con dispositivos reales está en [experimentos con qubits lógicos](logical-qubit-experiments.md).
