---
concept: photonic-qubits
title: "Qubits fotónicos"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
Un *qubit fotónico (photonic qubit)* se codifica en la luz, normalmente en cuál de dos modos está un fotón. Los fotones son excelentes para comunicar, pero su falta de interacción hace muy difíciles las puertas de dos qubits [@slussarenko-2019, §I.B, p. 2; p. 1].

### Explicación
La codificación más habitual es la de *doble raíl (dual-rail)*: un solo fotón que puede estar en uno de dos modos, por ejemplo dos polarizaciones o dos caminos, y el qubit es "en cuál de los dos". Otras codificaciones usan el instante de llegada (*time-bin*), la frecuencia o la forma espacial del haz [@slussarenko-2019, §I.B, p. 2]. Mover la población entre los dos modos y aplicar fases relativas se hace con interferometría y es fácil y de muy alta fidelidad [@slussarenko-2019, pp. 1-2].

Los fotones atraen porque viajan a la velocidad de la luz y casi no interactúan con el entorno: son qubits "voladores" limpios, necesarios para redes y computación distribuida [@slussarenko-2019, p. 1]. En los [criterios de DiVincenzo](divincenzo-criteria.md), los criterios 6 y 7 (comunicación) se cumplen de forma natural con fotones [@divincenzo-2000, p. 7]. Además, un procesador fotónico no necesita convertir qubits estacionarios en voladores, a diferencia de las demás plataformas [@slussarenko-2019, §IV, p. 11].

Esa misma falta de interacción es el problema. Una puerta de dos qubits necesita una fase condicional de π entre fotones, un efecto no lineal extremadamente débil a nivel de un solo fotón. Se puede imitar con óptica lineal más medida, pero la puerta resultante es *probabilística* (se anuncia o se poselecciona el éxito) [@slussarenko-2019, p. 2]. Los fotones cumplen aproximadamente cinco de los siete criterios de DiVincenzo: lo difícil son las puertas de dos qubits deterministas y la pérdida de fotones (más a veces la necesidad de una memoria óptica), que añade sobrecarga [@slussarenko-2019, p. 1]. La pérdida es la principal fuente de ruido en óptica [@slussarenko-2019, pp. 8, 10].

Un ordenador fotónico tiene tres piezas: fuentes de fotones, un circuito de óptica lineal (guías de onda, divisores, desfasadores) y detectores [@slussarenko-2019, §II, pp. 2-8]. Conviene no confundir dos cosas distintas: un ordenador fotónico universal por puertas (todavía no existe a escala) y una máquina de muestreo de bosones, de propósito especial, como Jiuzhang (2020), que no ejecuta circuitos programables [@zhong-2020, p. 10].

### Ejemplo
El interferómetro de Mach-Zehnder de [principio de superposición](../../quantum-mechanics/concepts/superposition-principle.md) es justo una puerta de un qubit fotónico: un divisor de haz 50/50 hace de Hadamard y un desfasador en un camino hace de puerta de fase [@bartolucci-2023, §II.A, p. 4].

### Para seguir
La capa 2 explica cómo se logra una puerta de dos qubits con óptica lineal, las piezas reales (detectores, fuentes, chips integrados) y el caso de Jiuzhang. Los [experimentos de ventaja cuántica](quantum-advantage-experiments.md) tratan cómo se valora el muestreo de bosones.

## Comprensión {#layer-2}

### Idea clave
Con óptica lineal, detectores y realimentación clásica se pueden hacer puertas no deterministas y, de ahí, computación por medida o por fusión. Detectores, fuentes y pérdidas fijan lo que se puede construir [@slussarenko-2019, §I.B, p. 2; §II-III, pp. 2-10; @bartolucci-2023, §I.A, p. 2].

### Explicación
Knill, Laflamme y Milburn (KLM, 2001) mostraron que basta óptica lineal, detección de fotones individuales y realimentación clásica: la interferencia condicionada a detecciones anunciadas crea una fase no lineal en el número de fotones y permite puertas no deterministas, con un esquema de "repetir hasta tener éxito" y teleportación de las puertas exitosas [@slussarenko-2019, §I.B, p. 2; p. 8]. El número de recursos crece linealmente con el número de qubits, pero la sobrecarga de fotones auxiliares y circuitos es grande porque las puertas son no deterministas [@slussarenko-2019, p. 2]. KLM demostró que el procesado óptico es escalable, pero una máquina completa con corrección de errores no era construible entonces [@slussarenko-2019, §III, p. 8].

La computación por medida evita parte del problema. En la de "un camino" se construye primero, con operaciones no deterministas, un estado entrelazado multifotónico (*estado de clúster, cluster state*); después el cálculo usa solo puertas de un qubit, medidas y realimentación clásica, que encajan con la óptica [@slussarenko-2019, §III.B, p. 10]. Los esquemas de clúster necesitan menos recursos que muchos otros y son más tolerantes a la pérdida que KLM; los clústeres se construyen por *fusión* no determinista, y por debajo de cierto umbral de nodos o enlaces perdidos la teoría de la percolación sigue dando un recurso universal [@slussarenko-2019, p. 10].

La computación basada en fusión (FBQC) lleva esa idea más lejos. Bartolucci y colaboradores (PsiQuantum, fabricante, y **solo con simulaciones**, no experimentos) proponen un modelo con dos primitivas: generar estados de recurso pequeños de tamaño constante (del orden de 10 qubits) y hacer medidas proyectivas entrelazantes ("fusiones") entre qubits de distintos estados [@bartolucci-2023, abstract, p. 1; §I.A, p. 2]. Una *fusión de Bell* es una medida proyectiva de dos qubits de `X₁X₂` y `Z₁Z₂`, destructiva [@bartolucci-2023, §II, p. 3]. En óptica lineal es simple pero no determinista: falla con una probabilidad `p_fail` (50 % en la versión básica, 25 % con un par de Bell auxiliar, `1/2ⁿ` con `2ⁿ − 2` fotones extra) y entonces da solo medidas de un qubit [@bartolucci-2023, §II.A, p. 4; §VI.C.2, p. 14]. Se distinguen tres resultados: éxito, fallo (anunciado; no crea entrelazamiento ni añade ruido) y borrado (por errores como la pérdida de un fotón) [@bartolucci-2023, §II.A, Fig. 2, p. 4].

La idea clave es que el código de corrección de errores trata directamente el no determinismo junto con los demás errores, sin repetir hasta tener éxito [@bartolucci-2023, abstract; §II.A, p. 3]. Cada qubit se crea y se mide casi enseguida, lo que limita la acumulación de errores y reduce el procesado clásico; los autores consideran que la vida muy corta del qubit es una virtud ante la pérdida, que es el error dominante [@bartolucci-2023, §I, p. 1; §VII.C, p. 16]. Las redes de fusión implementan un código de superficie en forma 3D, con las fusiones repetidas haciendo de medidas de estabilizadores repetidas [@bartolucci-2023, §I.B, p. 2; §V.C, p. 9]; ver [código de superficie](../../error-correction/concepts/surface-code.md).

Todo esto depende de componentes reales. Empezando por los detectores, no hay ninguno ideal; se caracterizan por eficiencia, tiempo de reinicio, jitter, cuentas oscuras y resolución en número de fotones [@slussarenko-2019, §II.A, pp. 2-3]:

| Detector | Datos (2019) |
|---|---|
| Fotodiodos de avalancha de Si | reinicio <100 ns, eficiencia hasta ~65 %, sin resolución de número, no para bandas de telecom |
| Nanohilos superconductores (SNSPD) | reinicio ~40 ns, eficiencia ~0,93, recientemente ≥0,95 en telecom, a 0,8-3 K |
| Sensores de borde de transición (TES) | resuelven hasta ~20 fotones, eficiencia 0,95-0,98, pero lentos (reinicio ~µs) |

Un ordenador práctico probablemente necesite ciclos de reloj de 10 ns o menos [@slussarenko-2019, p. 3]. Y "óptica a temperatura ambiente" no incluye a los detectores: los SNSPD funcionan a 0,8-3 K [@slussarenko-2019, p. 3].

Las fuentes son el otro cuello de botella. Se necesitan muchas (N entre ~10 y 10¹¹) fuentes simultáneas de fotones únicos a demanda, bien colectados, puros, indistinguibles y compatibles con materiales de poca pérdida, y ninguna fuente lo cumple todo [@slussarenko-2019, §II.B, p. 3]. La conversión paramétrica espontánea (*SPDC*) produce fotones anunciados o pares entrelazados de forma probabilística, con eficiencia de anuncio de ~10-15 % en cristales simples; con cristales polarizados periódicamente y ajuste de velocidad de grupo se llegó a eficiencias >0,8, pureza ≥0,997 y fidelidad de estado entrelazado >0,99 [@slussarenko-2019, pp. 4-5]. La probabilidad de par por pulso se limita a ~1 % porque más potencia crea ruido de multipares, y combinar `n` fuentes tiene probabilidad `ξⁿ`, que no escala [@slussarenko-2019, p. 5]. La *multiplexación* (espacial o temporal) se acerca a una fuente determinista con eficiencia `1 − (1 − ξ)ⁿ`, limitada por las pérdidas de los conmutadores; una demostración dio ~0,6 de probabilidad de fotón único en la fibra de salida [@slussarenko-2019, pp. 5-6]. Los puntos cuánticos emiten a demanda y brillan, pero acoplan a fibra al ~33 % o menos y cada punto emite fotones distinguibles [@slussarenko-2019, p. 5].

El camino a la escala es la fotónica integrada: chips de guías de onda con densidad de componentes, poca pérdida de propagación y acoplo, reconfiguración rápida e idealmente fuentes y detectores en el chip [@slussarenko-2019, §II.E, p. 6]. Los materiales son vidrio escrito con láser de femtosegundos (circuitos 3D), niobato de litio (fuentes y conmutación electroóptica de GHz) y silicio (denso, de poca pérdida, compatible con fundiciones) [@slussarenko-2019, pp. 6-7]. Un chip de 2018 integraba 16 fuentes de pares, 93 desfasadores, 122 divisores de haz, 256 cruces, 64 acopladores de rejilla y 2 detectores SNSPD; los defectos son la pérdida por absorción, la rugosidad de las guías y el acoplo al chip [@slussarenko-2019, Fig. 2, p. 7; p. 8].

### Ejemplo
Jiuzhang (2020, USTC; autores del propio experimento) es una máquina de muestreo de bosones gaussianos. Usa 25 cristales PPKTP que producen 25 estados comprimidos de dos modos (equivalente a 50 de un modo), un interferómetro de 100 modos y 100 detectores SNSPD de eficiencia media del 81 % [@zhong-2020, pp. 1, 4-6]. La pureza espectral media de los pares medida fue 0,938 y la eficiencia de colección media 0,628; la transmisión del interferómetro, 97,7 %, y el acoplo de salida, ~90 % [@zhong-2020, pp. 4-6].

Es una plataforma fotónica "de propósito especial": ejecuta un único interferómetro fijo [@zhong-2020, p. 10]. Los autores dicen que los muestreadores de bosones fotónicos funcionan a temperatura ambiente y son robustos frente a la decoherencia [@zhong-2020, p. 3]; los detectores son aparte [@slussarenko-2019, p. 3]. Cómo se valora su ventaja está en [experimentos de ventaja cuántica](quantum-advantage-experiments.md).

### Errores frecuentes
- *"Los fotones no decoheren, así que lo fotónico es fácil."* El problema es la pérdida y las puertas de dos qubits [@slussarenko-2019, pp. 1, 8].
- *"Muestreo de bosones = ordenador cuántico fotónico."* Es una máquina de propósito especial [@zhong-2020, p. 10].
- *"Es la plataforma líder."* Ver el desacuerdo abajo.

### Las fuentes discrepan
El resumen de la revisión de 2019 llama a la fotónica "contendiente destacado"; es la opinión de un grupo de esa especialidad, no una comparación neutral [@slussarenko-2019, resumen]. Eisert y Preskill (2025-26) escriben que los qubits fotónicos y de espín pueden ir ahora por detrás de iones, superconductores y átomos, pero podrían dar un salto [@eisert-2025, Sec. III, p. 5].

Los resultados de simulación de FBQC son de la versión v1 (enero de 2021) del artículo; la versión de 2023 puede variar. Con la red de anillo de 6 se obtienen umbrales del 11,98 % frente a borrado y del 1,07 % frente a error de Pauli; con óptica lineal y fusiones potenciadas con pares de Bell, un esquema tolera un 10,4 % de probabilidad de pérdida por fusión, unos 2,7 % de pérdida por fotón [@bartolucci-2023, abstract, p. 1; §I, p. 1; §VI.C.1-2, pp. 13-14]. Los propios autores subrayan que los esquemas son pedagógicos y no están optimizados [@bartolucci-2023, abstract; §VI, p. 9].

### Para seguir
La capa 3 explica qué métricas importan en fotónica (presupuestos de pérdida), qué cambia para quien programa y cómo juzgar un anuncio.

## Profesional {#layer-3}

### Idea clave
En fotónica la ficha técnica son los presupuestos de pérdida y los parámetros de fuentes y detectores, no la fidelidad de puertas. Para quien programa, "programar" es elegir bases de fusión y la corrección actúa sobre resultados clásicos [@bartolucci-2023, §I.A, p. 1; §V.A, p. 7].

### Explicación
Las métricas relevantes son:

- *Pérdida por fotón* (total, de todos los componentes). En la simulación de PsiQuantum el esquema tolera ~2,7 % de pérdida por fotón (10,4 % por fusión) [@bartolucci-2023, §VI.C.2, p. 14].
- *Pureza e indistinguibilidad de las fuentes, eficiencia de anuncio y probabilidad de par.* Los números de la revisión (heralding >0,8, pureza 0,997) son de SPDC en un cristal optimizado, no de un chip completo [@slussarenko-2019, pp. 4-5].
- *Eficiencia, reinicio y jitter del detector:* con SNSPD ~0,93-0,95 y reinicio ~40 ns, operados a 0,8-3 K [@slussarenko-2019, p. 3].
- *Tasa de reloj:* ciclos de ≤10 ns se citan como necesidad práctica [@slussarenko-2019, p. 3].
- *Componentes reconfigurables:* se consideran propensos a error y se prefiere enrutado fijo; los circuitos fotónicos integrados fijos tienen fidelidad mucho mayor que los reconfigurables [@bartolucci-2023, §I.C, p. 3 y nota 1].

Para quien programa, el modelo mental cambia:

- No hay un "circuito" en el sentido de [Qiskit](../../qiskit-programming/concepts/qiskit-circuits.md): en FBQC, "programar" es elegir las bases de las fusiones, y la corrección de errores actúa solo sobre resultados clásicos porque los qubits se destruyen [@bartolucci-2023, §I.A, p. 1; §V.A, p. 7].
- La decodificación clásica se hace a la escala de tiempo lógica, no a la del reloj de fusión, y un decodificador lento no afecta al umbral [@bartolucci-2023, §I.C, p. 3; §VII.B, p. 16]. Contrasta con la [decodificación](../../error-correction/concepts/decoding.md) en superconductores, donde la latencia del decodificador es crítica [@google-2025, p. 5].
- La arquitectura de Bartolucci tiene generadores de estados de recurso, un enrutador de red de fusión con retardos, dispositivos de fusión reconfigurables y un decodificador clásico; la conectividad no necesita ser local [@bartolucci-2023, Fig. 1, p. 2; §VII.C, pp. 16-17].
- La universalidad llega con inyección y destilación de estados mágicos para puertas T [@bartolucci-2023, §VII.A, pp. 15-16]; ver [puertas tolerantes a fallos](../../error-correction/concepts/fault-tolerant-gates.md).

### Ejemplo
Un contraste de pérdidas (cálculo propio, orientativo). En Jiuzhang, si los cuatro factores citados fueran independientes (colección de la fuente 0,628, transmisión 0,977, acoplo de salida ~0,90 y detección 0,81), un fotón sobreviviría con probabilidad de `0,628 × 0,977 × 0,90 × 0,81 ≈ 0,45` [@zhong-2020, pp. 4-6]. Son tareas y modelos de pérdida distintos de los de la simulación de PsiQuantum (2,7 % de pérdida por fotón), así que la comparación solo sirve para ver el orden de magnitud de la distancia entre un experimento de muestreo de 2020 y los requisitos de una simulación de tolerancia a fallos.

Para decidir cuándo mirar la fotónica (criterio propio a partir de lo anterior):

- *Redes y computación distribuida:* es la plataforma natural, porque el fotón es el portador de enlace [@slussarenko-2019, §IV, p. 11]. Otras plataformas necesitan interconversión y quizá ajuste de longitud de onda; los iones, por ejemplo, usan enlaces fotónicos [@bruzewicz-2019, pp. 28-30].
- *Muestreo especializado:* los experimentos de muestreo de bosones gaussianos [@zhong-2020, p. 10].
- *Computación tolerante a fallos a largo plazo:* FBQC es una propuesta de un fabricante con resultados de simulación; no hay en las fuentes una demostración experimental de un qubit lógico fotónico.

Y para juzgar un anuncio fotónico:

1. *¿Experimento o simulación?* Las cifras de umbral de PsiQuantum son de simulaciones Monte Carlo con emparejamiento de peso mínimo, no de hardware [@bartolucci-2023, nota de acceso; §VI.C.1, p. 13].
2. *¿Qué pérdida total hay y cómo se cuenta?* Pregunta si se cuenta la pérdida de fuente, de enrutado y de detección por separado.
3. *¿Se puede verificar la salida?* En muestreo de bosones gaussianos la certificación completa se conjetura intratable, y los métodos de validación dejan de ser viables por encima de ~30 clics [@zhong-2020, pp. 7-8].
4. *¿Quién firma?* PsiQuantum es un fabricante; el artículo de USTC lo firman los autores del experimento; la revisión de 2019 es de un grupo de fotónica (Griffith).
5. *¿Es de propósito especial o universal?* Ver [experimentos de ventaja cuántica](quantum-advantage-experiments.md).

### Las fuentes discrepan
La versión revisada del artículo de Jiuzhang extendió la validación hasta 40 clics, frente a los ~30 de la versión citada arriba [@zhong-2020, p. 10].

### Para seguir
Para el lugar de la fotónica entre las demás plataformas, ver la [comparativa](hardware-landscape.md).
