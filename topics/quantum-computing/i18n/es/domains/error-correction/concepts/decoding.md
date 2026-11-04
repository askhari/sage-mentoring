---
concept: decoding
title: "Decodificación"
format: 2
---

## Profesional {#layer-3}

### Idea clave
Un **decodificador (decoder)** es un algoritmo clásico que convierte los síndromes medidos en una corrección; tiene que ser lo bastante preciso para que el error lógico caiga con la distancia y lo bastante rápido para seguir el ritmo de los ciclos, o el atasco hace crecer el tiempo de cálculo [@bravyi-2024, p. 5; @google-2025, p. 5].

### Explicación
Se asume [el código de superficie](surface-code.md): síndromes, cadenas de errores y rondas repetidas. Este concepto empieza directamente en la capa profesional.

El decodificador recibe los síndromes y devuelve una estimación del error, o de la corrección que hay que aplicar. Tiene éxito si su estimación coincide con el error real salvo un producto de estabilizadores (ambos actúan igual sobre todos los estados lógicos) y falla si difieren en un operador lógico no trivial [@bravyi-2024, p. 5; §6, p. 16]. Basta con encontrar un error *equivalente* al real, no el exacto [@fowler-2012, p. 11, nota 12]. En los códigos de [estabilizadores](stabilizer-formalism.md) la regla genérica es elegir un Pauli por síndrome, naturalmente el de menor peso consistente con él, lo que corrige todo error de peso menor que `d/2`; pero calcularlo es difícil en general, incluso para códigos clásicos [@watrous-2025, L14.3, PDF pp. 434-437]. Una regla más fina elige el error más probable según el modelo de ruido, que puede no ser el de menor peso [@watrous-2025, L14.3, PDF pp. 434-435]. En los códigos pequeños, decodificar es solo una tabla: medir el síndrome en la base estándar y aplicar la corrección que dicta [@de-wolf-2026, §21.4, p. 198 [186]]; ver [código de Shor](shor-code.md).

En el código de superficie, la estructura permite emparejar extremos. Una cadena de errores deja síndromes `−1` solo en sus extremos. El decodificador empareja los `−1` y aplica correcciones a lo largo de los caminos más cortos entre pares: la corrección más el error forman un lazo cerrado, que funciona si es contraíble y falla si da la vuelta al toro (o va de borde a borde en el parche plano) [@watrous-2025, L15.2, PDF pp. 462-463]. Con muchos `−1`, se calcula un emparejamiento perfecto de peso mínimo (*minimum-weight perfect matching*, MWPM) con el algoritmo de Edmonds, que es eficiente en un ordenador clásico [@watrous-2025, L15.2, PDF p. 463]. Funciona bien con errores dispersos y falla cuando crece la densidad de errores y la longitud de las cadenas, porque la decodificación es un problema inverso sin solución única [@fowler-2012, pp. 8, 11]. Con ruido independiente de Pauli equiprobable (`X`, `Y`, `Z`) y síndrome perfecto, simulaciones muestran que este decodificador, no óptimo, funciona bien por debajo de un ruido de alrededor del 10 %; un `L` mayor no cambia mucho el punto de equilibrio pero hace caer más rápido el error por debajo de él [@watrous-2025, L15.2, PDF p. 463]. Con errores de circuito y de medida el umbral es mucho menor (0,57 % por paso en el modelo de Fowler) [@fowler-2012, pp. 11-12].

Con medidas ruidosas, hay que decodificar en el espacio y el tiempo. Un error de medida aparece como un cambio de síndrome aislado que desaparece en el ciclo siguiente; los errores de datos persisten. Se distinguen por su patrón en el espacio y el tiempo, y establecer un valor de medida exige varios ciclos [@fowler-2012, pp. 7-8, Fig. 2]. En la práctica se trabaja con eventos de detección (el cambio del síndrome entre ciclos consecutivos), que además hacen la matriz de decodificación más dispersa [@bravyi-2024, p. 17]. En fusión fotónica, la misma idea aparece como un grafo de síndrome cuyas aristas son resultados de fusión y se decodifica con emparejamiento de peso mínimo o con *union-find*; allí un decodificador lento no afecta al umbral porque las fusiones avanzan sin esperar [@bartolucci-2023, §V.D, p. 9; §VII.B, p. 16].

Cuando hay puertas entre parches, los síndromes dejan de ser independientes. Una CNOT transversal entre dos parches propaga errores físicos de forma determinista de uno a otro, así que los síndromes de ambos quedan correlacionados. Se decodifican los dos qubits lógicos a la vez con un grafo de decodificación con aristas extra e hiperaristas que unen los estabilizadores de ambos bloques: con decodificación convencional por separado (emparejamiento independiente en cada código) el error de Bell crece con la distancia, y con la correlacionada cae [@bluvstein-2024, p. 3, Figs. 2b,d]. Para el estado GHZ lógico, el peso del emparejamiento correlacionado sirve también para ordenar los eventos de síndrome en un descarte deslizante [@bluvstein-2024, p. 4]. Google usa un conjunto de decodificadores de emparejamiento correlacionado con síntesis de emparejamiento, con pesos de aristas ajustados con aprendizaje por refuerzo, y un decodificador por red neuronal ajustado con datos del procesador [@google-2025, p. 2].

Además de acertar, el decodificador debe llegar a tiempo. Debe seguir el ritmo de generación de síndromes, porque algunas operaciones lógicas son no deterministas y dependen de resultados de medidas lógicas; si va retrasado, el atasco provoca un aumento exponencial del tiempo de cálculo [@google-2025, p. 5]. El decodificador se complica con la distancia: los síndromes por ciclo crecen cuadráticamente con `d`, y se espera que la decodificación por capas o ventanas lleve los métodos precisos a tiempo real [@google-2025, pp. 6-7]. El procesado clásico limita la tasa de rondas de detección a unos `10⁶`-`10⁷ Hz` (con relojes clásicos de unos 3 GHz), con un ciclo objetivo de `200 ns` [@fowler-2012, p. 39]. En la estimación de Gidney el tiempo de reacción del control es de `10 µs`, una hipótesis más [@gidney-2025, resumen, p. 1].

Los códigos qLDPC necesitan otro decodificador. Los códigos bicicleta de IBM no tienen una estructura de emparejamiento. Se usa *propagación de creencias con postprocesado de estadísticas ordenadas* (BP-OSD): una fase fuera de línea construye un modelo de ruido linealizado enumerando los fallos individuales (unos `98·n·N_c`), y una fase en línea resuelve el problema de decodificación de peso mínimo de un código lineal clásico. Su solución exacta es NP-difícil, así que se hace con BP (una estimación por paso de mensajes de las marginales) seguida de OSD, que elige el conjunto de información más fiable con un algoritmo voraz [@bravyi-2024, §6, pp. 16-18]. Como los códigos son CSS, `X` y `Z` se decodifican por separado con matrices dispersas `(6,35)`; para `[[144,12,12]]` con 12 ciclos tienen unas 8800 columnas [@bravyi-2024, p. 18]. Los autores advierten de que un BP-OSD de propósito general puede no ser lo bastante rápido para corrección en tiempo real y piden un decodificador que aproveche la estructura de estos códigos [@bravyi-2024, p. 31]. Es el precio de la mayor eficiencia en qubits (ver [código de superficie](surface-code.md)).

Para decidir (criterio propio a partir de lo anterior):

1. *Presupuesto de latencia.* Parte del tiempo de reacción que asume tu estimación (10 µs en Gidney) y comprueba que tu decodificador, con su paralelismo, cabe y lo hace de forma sostenida, no solo de media [@gidney-2025, resumen, p. 1; @google-2025, pp. 5-6].
2. *Throughput antes que latencia.* El decodificador debe consumir el síndrome a la tasa de ciclo; si no, el atasco crece sin límite [@google-2025, p. 5].
3. *Precisión frente a velocidad.* Un decodificador más preciso reduce la distancia necesaria (un 13 % de qubits de diferencia en el ejemplo siguiente), pero ha de funcionar a velocidad de reloj.
4. *Correlaciones.* Si hay puertas transversales entre parches o ruido correlacionado, la decodificación independiente pierde: usa un grafo conjunto [@bluvstein-2024, p. 3].
5. *Qué decodificador está dentro del "perfecto".* El teorema del umbral supone procesado clásico perfecto [@watrous-2025, L16.1, PDF p. 473]; la ingeniería real tiene que cumplirlo con hardware (por ejemplo, una FPGA que decodifica en tiempo real y realimenta [@bluvstein-2024, p. 2]).

### Ejemplo
Los datos de Google (código de superficie de `d = 5` en el procesador de 72 qubits, ciclo de 1,1 µs):

- *Emparejamiento en tiempo real (Sparse Blossom con ventanas):* error lógico `ε₅` `0,35 % ± 0,01 %`, `Λ` `2,0 ± 0,1`, latencia media `63 ± 17 µs` [@google-2025, pp. 1, 5-6].
- *Red neuronal (fuera de línea):* error lógico `ε₅` `0,269 % ± 0,008 %`, `Λ` `2,18 ± 0,09`, unos `24 µs` por ciclo [@google-2025, p. 6].

Aritmética propia con esas cifras:

- *Latencia frente a ciclo.* `63 µs / 1,1 µs ≈ 57` ciclos de síndrome. La latencia es el tiempo desde la última ronda hasta la corrección; el decodificador de tiempo real consigue que sea constante hasta `10⁶` ciclos (≈ 1,1 s) [@google-2025, pp. 1, 6]. Esa latencia pesa sobre todo en las operaciones que dependen del resultado (razonamiento propio): fijará el tiempo de reacción de las puertas no Clifford, y la cifra todavía no incluye la realimentación al circuito lógico [@google-2025, p. 6].
- *Rendimiento.* La red neuronal necesita `24 µs` por ciclo y la tasa de síndromes exige menos de `1,1 µs`: unas `24 / 1,1 ≈ 22` veces demasiado lenta para tiempo real [@google-2025, p. 6].
- *Coste de la precisión.* Un error 30 % mayor (`0,35 / 0,269 ≈ 1,30`) y una `Λ` algo menor. Con `Λ` más baja se necesitan más pasos de distancia para el mismo objetivo: en la receta del [teorema del umbral](threshold-theorem.md), pasar de `Λ = 2,14` (`ε₇ = 1,43·10⁻³`) a `Λ = 2,04` (`ε₇ = 1,71·10⁻³`, el decodificador de emparejamiento de síntesis de la máquina de 105 qubits) lleva de `d = 63` a `d = 67` para `10⁻¹²`, o de 7937 a 8977 qubits (+13 %; cálculo propio, mismo método que allí) [@google-2025, pp. 1-3].

Ambas filas son de `d = 5` en el procesador de 72 qubits; la decodificación en tiempo real no se hizo en el código de `d = 7` [@google-2025, p. 6].

### Las fuentes discrepan
Las redes neuronales y los decodificadores correlacionados se describen en las fuentes solo por su rendimiento; los detalles internos (por ejemplo, el decodificador de Bluvstein y colaboradores, cuyos detalles remiten a otro artículo en preparación) no están en las notas [@bluvstein-2024, p. 3]. Tampoco hay en ellas una comparación independiente de decodificadores en el mismo hardware.

### Para seguir
[Puertas tolerantes a fallos](fault-tolerant-gates.md) explica por qué las puertas no Clifford atan el reloj lógico al decodificador, y [estimación de recursos](resource-estimation.md) muestra cómo el tiempo de reacción entra en la cuenta.
