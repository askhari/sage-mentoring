---
concept: trapped-ion-qubits
title: "Qubits de iones atrapados"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
Un *ion atrapado (trapped ion)* es un átomo con carga eléctrica, suspendido en el vacío con campos eléctricos, cuyo par de niveles internos hace de qubit. Los iones son idénticos entre sí y ofrecen la mejor coherencia y las mejores fidelidades (cifras de 2019), a cambio de puertas lentas [@bruzewicz-2019, pp. 2-5].

### Explicación
Un ion es un átomo al que se le ha quitado un electrón. Cada ion es un qubit: se eligen dos de sus niveles internos de energía como `|0⟩` y `|1⟩` [@bruzewicz-2019, pp. 2, 10-13]. Los iones de una misma especie e isótopo son idénticos, así que necesitan la misma frecuencia de control y tienen la misma coherencia; esto reduce la calibración frente a los superconductores, cuyas frecuencias varían con la fabricación [@bruzewicz-2019, p. 4].

Imagina una fila de cuentas idénticas suspendidas en el aire y unidas por una cuerda elástica invisible. Con luz láser puedes empujar una cuenta concreta (puerta de un qubit). Si sacudes dos cuentas a la vez de la forma adecuada, la cuerda comparte la sacudida y las entrelaza (puerta de dos qubits). En el dispositivo real esa "cuerda" es el movimiento colectivo de la cadena de iones, vibraciones cuantizadas que actúan como un bus que acopla los estados internos [@bruzewicz-2019, p. 13].

Las tres operaciones básicas son:

- *Preparar:* el *bombeo óptico (optical pumping)* deja el ion en un estado conocido, y el enfriamiento láser reduce su movimiento [@bruzewicz-2019, pp. 2-3; pp. 15-16].
- *Operar:* los pulsos de microondas o de láser giran un ion; los pulsos láser que excitan el movimiento compartido entrelazan dos [@bruzewicz-2019, pp. 16-18].
- *Leer:* un estado "brillante" dispersa muchos fotones de un láser y uno "oscuro" casi ninguno; contando fotones se distingue `|0⟩` de `|1⟩` (*fluorescencia dependiente del estado*) [@bruzewicz-2019, p. 22].

Con las cifras de 2019, los iones tienen la mejor relación entre tiempo de coherencia y tiempo de puerta (~10⁶) y las mejores fidelidades de puertas de un qubit, de preparación y medida (SPAM) y de lectura de todas las plataformas, según los autores de la revisión [@bruzewicz-2019, pp. 4-5]. Las puertas de un qubit llegaron al 99,9999 % y las de dos qubits al 99,9 % [@bruzewicz-2019, p. 4; Tabla I, p. 18]. El precio es la velocidad: las puertas de dos qubits tardan 10-100 µs, frente a decenas de ns en superconductores [@bruzewicz-2019, pp. 3-4].

### Ejemplo
El H2 de Quantinuum (2023) es una máquina de iones con 32 qubits, descrita por los propios fabricantes [@moses-2023, abstract, p. 1]. Los números de este concepto son de dos fechas: 2019 (revisión independiente del MIT Lincoln Laboratory) y 2023 (artículo del fabricante); cuando leas "hoy" en un anuncio, mira de qué año son.

### Para seguir
La capa 2 explica las trampas, cómo se codifica el qubit, por qué las puertas son lentas y cómo se intenta escalar. Otra plataforma de capa 1 para contrastar son los [átomos neutros](neutral-atom-qubits.md).

## Comprensión {#layer-2}

### Idea clave
El movimiento compartido de la cadena sirve de bus para entrelazar, y de él vienen tanto la conectividad total como la lentitud. Escalar exige pasar de una cadena larga a trampas con transporte (QCCD) o a enlaces fotónicos [@bruzewicz-2019, pp. 13, 27-30].

### Explicación
Las *trampas de Paul* usan un campo de radiofrecuencia oscilante y son la plataforma principal para computación; las de Penning (campos estático eléctrico y magnético) sostienen cristales 2D de cientos de iones, pero rotan y son difíciles de direccionar individualmente [@bruzewicz-2019, p. 7]. En una trampa lineal de Paul existe una línea de campo RF nulo, de modo que una cadena de iones evita el "micromovimiento" en exceso y los iones pueden moverse a lo largo del eje, base de las arquitecturas con transporte [@bruzewicz-2019, p. 7]. Las trampas de superficie ponen todos los electrodos en un plano, aptas para microfabricación y CMOS, a cambio de menor profundidad de trampa [@bruzewicz-2019, p. 9].

Dentro de la trampa, el qubit puede codificarse de cuatro maneras según la separación de niveles [@bruzewicz-2019, pp. 2, 10-13]:

| Tipo | Separación | Ventajas y límites |
|---|---|---|
| Zeeman | MHz | Estructura simple y vida casi infinita, pero muy sensible al campo magnético; 300 ms de coherencia (2,1 s con desacoplamiento dinámico) con blindaje de mu-metal [@bruzewicz-2019, p. 11] |
| Hiperfino | GHz | Los estados "reloj" (`m_F = 0`) son insensibles al campo a primer orden; el reloj de 171Yb⁺ da segundos de coherencia, y hasta 600 s con desacoplamiento dinámico [@bruzewicz-2019, p. 12] |
| Estructura fina | THz | Vidas de segundos, limitadas por la fuga más que por la relajación; usan láseres Raman en el infrarrojo [@bruzewicz-2019, p. 13] |
| Óptico | cientos de THz | Coherencia ~0,2 s, limitada por el ruido de fase del láser y, en última instancia, por la vida del nivel superior (1 a decenas de s); lectura casi con eficiencia unidad [@bruzewicz-2019, pp. 12-13] |

Los niveles extra implican fuga y láseres de rebombeo, y los iones pueden perderse de la trampa (vidas de horas a meses), por lo que hace falta recargar [@bruzewicz-2019, p. 4].

Para entrelazar se usa el bus de movimiento: para `N` iones hay `3N` modos de movimiento (fonones) que acoplan los estados internos [@bruzewicz-2019, p. 13]. Las puertas se basan en ellos:

- *Cirac-Zoller (1995):* exige enfriar al estado fundamental del movimiento y direccionar iones individuales; las primeras demostraciones dieron fidelidades del 71-77 % [@bruzewicz-2019, pp. 17-18].
- *Mølmer-Sørensen (MS):* luz bicromática cerca de las bandas laterales que aplica una fuerza dependiente del estado; el movimiento describe un lazo cerrado en el espacio de fases y deja una fase geométrica. No necesita enfriar al estado fundamental y puede usar haces globales; es la base de las mejores puertas de dos qubits [@bruzewicz-2019, pp. 18-19].
- *Fase geométrica de Leibfried:* similar, pero no excita transiciones entre estados del qubit y no sirve para qubits insensibles al campo a primer orden [@bruzewicz-2019, p. 19].

Esas puertas son lentas por una razón física. Por debajo del periodo de la trampa (frecuencias de MHz), las puertas excitan varios modos a la vez y la fase óptica importa; los intentos más rápidos pagan fidelidad (las de menos de 500 ns solo llegaron al 60 % y las basadas en pulsos ultrarrápidos, al 76 %) [@bruzewicz-2019, p. 20]. En una cadena larga, las puertas se enlentecen al crecer el número de iones porque disminuye el parámetro de Lamb-Dicke, se debilita el acoplo y se aglomeran los modos; en 2019 no se habían demostrado puertas con modulación para cadenas de más de 5 iones [@bruzewicz-2019, pp. 6, 27]. Además, el calentamiento anómalo del movimiento (ruido eléctrico mucho mayor que el esperado) crece aproximadamente como `d⁻⁴` con la distancia al electrodo, y enfriar los electrodos a ~4 K lo reduce unos dos órdenes de magnitud [@bruzewicz-2019, pp. 14-15].

La lectura es mejor que la puerta: la fluorescencia da lecturas de >99,99 % en menos de 200 µs, o 99,93 % en 11 µs con detectores de nanohilos superconductores, que necesitan criogenia; la eficiencia total de detección es de solo ~2-4 % por la óptica [@bruzewicz-2019, p. 4; pp. 24-25]. El problema es medir una ancilla a mitad del circuito: dispersa fotones que decoherencian a los iones de datos vecinos, lo que importa para la corrección de errores, y se resuelve con una segunda especie o con *shelving* [@bruzewicz-2019, pp. 24, 32-33].

Para escalar hay tres caminos:

1. *Cadena larga con conectividad total:* los ordenadores de 3 y 5 qubits totalmente conectados ejecutaron algoritmos con éxito del 85-95 %; en Bernstein-Vazirani y Hidden Shift superaron en tasa de éxito al dispositivo superconductor de 5 qubits de IBM, aunque más lentos [@bruzewicz-2019, pp. 25-26]. Los procesadores totalmente conectados pueden operar con más fidelidad que los de vecinos más próximos [@burkard-2023, §VII, p. 46].
2. *QCCD (quantum charge-coupled device):* una red 2D de trampas segmentadas con uniones, donde los iones se transportan entre zonas de memoria, interacción, medida y carga [@bruzewicz-2019, pp. 27-28]. Es la arquitectura del H2 [@moses-2023, §I, p. 2].
3. *Enlaces fotónicos:* iones "de comunicación" emiten fotones entrelazados con su estado; la coincidencia en un divisor de haz anuncia entrelazamiento ion-ion. En 2019 la tasa máxima era de ~5 Hz por la baja eficiencia de colección (~0,005) [@bruzewicz-2019, pp. 28-30].

En cuanto a lo hecho con iones hasta 2019: Deutsch-Jozsa (2003), teleportación (2004), QFT semiclásica (2005), Grover en 2 iones, factorización de 15 con 5 iones (2016), VQE para H₂, LiH y H₂O con hasta 11 iones y una simulación analógica de Ising con 53 qubits [@bruzewicz-2019, pp. 25-26]. En corrección de errores solo había demostraciones pequeñas (repetición de 3 qubits, códigos de detección de 4 y 7 iones) [@bruzewicz-2019, pp. 32-33].

### Ejemplo
El H2 de Quantinuum (2023, fabricante) muestra lo que cuesta la conectividad total en una arquitectura QCCD [@moses-2023, nota de acceso]:

- *Arquitectura:* trampa tipo "pista de carreras" lineal con condiciones periódicas, 32 qubits inicialmente, 8 zonas de puerta de las que 4 hacen operaciones cuánticas; 376 electrodos y 268 fuentes de voltaje independientes. Cada qubit es un 171Yb⁺ (estados hiperfinos de reloj) emparejado con un 138Ba⁺ que sirve de refrigerante [@moses-2023, §II A, pp. 2-3; §II B, pp. 3-4].
- *Conectividad arbitraria sin SWAP:* se acercan los iones a la misma zona durante el circuito [@moses-2023, §I, p. 2]. Pero el transporte se lleva en promedio ~60 % del tiempo del circuito; para el circuito de volumen cuántico, el 1 % del tiempo es operación cuántica, el 52 % transporte y el 47 % enfriamiento, con 1,23 s por disparo [@moses-2023, §II E, p. 4; Tabla I, p. 5].
- *Errores por componente (RB):* puertas de un qubit 2,5·10⁻⁵; puertas de dos qubits 1,84·10⁻³; SPAM 1,6·10⁻³ por qubit; fuga 3,9·10⁻⁴ por puerta de dos qubits [@moses-2023, abstract, p. 1; Tabla II, p. 6].
- *Sistema:* error efectivo por puerta de dos qubits de 2,6(2)·10⁻³ en benchmarks de espejo con 32 qubits, que no crece con el número de qubits según los autores [@moses-2023, §IV A, p. 8]; volumen cuántico 2¹⁶ [@moses-2023, §IV B, p. 8]; fidelidad GHZ de 0,82(1) con 32 qubits sin corregir SPAM [@moses-2023, §IV D, p. 10].
- Las puertas de dos qubits siguen siendo la fuente dominante de error, y el tiempo de transporte aumentó respecto al H1, lo que sube el error de memoria [@moses-2023, §VI, p. 15].

### Errores frecuentes
- *"Conectividad total es gratis."* En el H2 se paga con tiempo de transporte (~60 % del circuito) y con error de memoria [@moses-2023, §II E, p. 4; §VI, p. 15].
- *"Lento significa malo."* Los iones son los más lentos y también los de mayor fidelidad (2019); lo que cuenta es el cociente y lo que necesite la carga de trabajo (ver [coherencia y fidelidad](coherence-and-fidelity.md)).
- *"Una cadena puede crecer indefinidamente."* Los modos de movimiento se aglomeran; por eso se pasa a varias zonas (QCCD) y a enlaces entre módulos [@bruzewicz-2019, pp. 27-30; @moses-2023, §I, p. 2].

### Las fuentes discrepan
Los resultados de 2019 son una fotografía de entonces: 99,91 % en 30 µs (9Be⁺, MS), 99,9 % en 100 µs (43Ca⁺, fase geométrica), 99,8 % en 1,6 µs con cientos de mW de luz Raman, y puertas con gradiente de microondas de 99,7 % pero de varios milisegundos [@bruzewicz-2019, pp. 18-20; Tabla I, p. 18]. Las cifras del H2 las produce el fabricante sobre su propia máquina y, según el propio artículo, probablemente ya han sido superadas [@moses-2023, nota de acceso]. Para 2025-26, Eisert y Preskill citan circuitos aleatorios no locales con más de 50 qubits de iones y más de 10 capas, y 12 qubits lógicos en una trampa de 56 qubits, con la salvedad de que la poselección descarta las ejecuciones con errores detectados [@eisert-2025, Sec. IV, p. 6; Sec. III, p. 4].

### Para seguir
La capa 3 trata el rendimiento real (tiempo por disparo), cómo compilar para iones y cómo evaluar un anuncio.

## Profesional {#layer-3}

### Idea clave
En iones el cuello de botella no es la puerta sino el tiempo por disparo, y la compilación se mide en tiempo de transporte, no en SWAP. Se eligen para circuitos profundos de pocos qubits con alta fidelidad [@moses-2023, Tabla I, p. 5; §II E, pp. 4-5].

### Explicación
Un programador debe fijarse en el tiempo por disparo, no solo en el error por puerta. En el H2, un disparo de los circuitos de benchmark de 32 qubits tarda 0,72-1,23 s [@moses-2023, Tabla I, p. 5]. En Sycamore, 200 s dieron 1 millón de muestras, unos 0,2 ms por muestra [@arute-2019, X H, p. 59]. Son circuitos distintos de máquinas distintas y años distintos, pero el orden de magnitud (milisegundos frente a segundos por disparo, un factor de miles) cambia las decisiones: un algoritmo variacional que necesita cientos de miles de ejecuciones es caro en iones, y un circuito profundo con alta fidelidad es barato en iones. En átomos neutros, un ciclo completo de unos 200 ms (5 Hz en 2020) queda también en la zona lenta [@henriet-2020, p. 6; p. 12].

Compilar para iones tiene sus propias reglas:

- *Sin SWAP, con transporte:* el compilador del H2 agrupa las puertas de dos qubits en capas y ordena los qubits con un algoritmo de Sugiyama modificado y una ordenación en burbuja paralela para minimizar el tiempo de transporte [@moses-2023, §II E, pp. 4-5]. Es el análogo del enrutamiento que ya conoces en [transpilación](../../qiskit-programming/concepts/transpilation.md), pero medido en tiempo de transporte y no en puertas SWAP.
- *Puerta nativa con ángulo:* la puerta de dos qubits es una rotación `U_ZZ(θ) = exp(−iθ·ZZ/2)`, y su error baja casi linealmente al reducir el ángulo [@moses-2023, §II C, p. 4; Fig. 3, p. 6].
- *Medida y reinicio a mitad de circuito (MCMR):* disponibles, con diafonía pequeña sobre los vecinos (0,045·10⁻⁴ en medida y 0,038·10⁻⁴ en reinicio) gracias a "esconder el micromovimiento" [@moses-2023, §II D, p. 4; Tabla II, p. 6]. Esto habilita circuitos adaptativos y de corrección de errores.
- *Repetición con 32 qubits:* un código de repetición de distancia 31 (31 de datos y 1 ancilla reutilizada) muestra que mayor distancia da mayor fidelidad lógica, con mejor protección frente a inversión de bit que frente a inversión de fase, lo que los autores leen como ruido sesgado [@moses-2023, §V C, pp. 13-14].

Los límites de escala están en el control y en la pérdida de iones:

- El control óptico y electrónico: láseres, entrega de luz y detección, y número de electrodos (268 fuentes de voltaje para 32 qubits en el H2, unas 8 por qubit, cálculo propio) [@moses-2023, §II A, pp. 2-3; §I, p. 2]. La carga de óptica y electrónica de control frena el escalado, mientras otras plataformas cofabrican el control en el chip [@bruzewicz-2019, p. 5].
- En 2023 se esperan trampas 2D con uniones y enrutado de señales, y acoplar varios chips [@moses-2023, §I, p. 2]; en 2019 una red 2D con calles de transporte general seguía abierta [@bruzewicz-2019, p. 28].
- La pérdida de iones: incluso con vidas de >24 h, una matriz de decenas de miles de iones perdería uno cada pocos segundos, por lo que hace falta recarga rápida [@bruzewicz-2019, p. 6]. En el H2, un par perdido se repone en 10-15 s [@moses-2023, §II B, p. 3].
- El tiempo de factorización: se cita una estimación de ~10 días (1024 bits) o ~100 días (2048 bits) para un ordenador de iones, consecuencia de las puertas lentas [@bruzewicz-2019, p. 4]. Ver [estimación de recursos](../../error-correction/concepts/resource-estimation.md) para cifras de otras plataformas.

### Ejemplo
La ecuación del error de la puerta del H2 es `ε(θ) = (2,9(2)·θ/π + 0,46(6))·10⁻³` [@moses-2023, §II C, p. 4; Fig. 3, p. 6]. De ella salen (cálculo propio):

- `θ = π/2`: `ε ≈ 1,9·10⁻³`.
- `θ = π/10`: `ε ≈ 0,75·10⁻³`, unas 2,5 veces menos.

Así, los algoritmos con muchas rotaciones pequeñas (fases controladas pequeñas de la [QFT](../../quantum-algorithms/concepts/quantum-fourier-transform.md), pasos de Trotter, QAOA) salen más baratos en esta puerta que en una CNOT fija, según los datos de esta máquina de 2023.

Para decidir cuándo elegir iones (criterio propio a partir de lo anterior): a favor, circuitos profundos de pocos qubits con alta fidelidad, conectividad total sin pagar SWAP, medidas a mitad de circuito y rotaciones de ángulo pequeño; en contra, cargas con muchísimas ejecuciones, por el tiempo por disparo, y la perspectiva de escalar más allá de decenas o pocos cientos de qubits con la tecnología de 2023. Contrasta con [superconductores](superconducting-qubits.md) y [átomos neutros](neutral-atom-qubits.md) en la [comparativa](hardware-landscape.md).

Para evaluar un anuncio de iones:

1. *¿La cifra es de puerta, de sistema o de benchmark?* El error de puerta de dos qubits (1,84·10⁻³) y el efectivo en 32 qubits (2,6·10⁻³) difieren porque este incluye memoria y transporte [@moses-2023, §IV, p. 7].
2. *¿El volumen cuántico dice lo que crees?* Se pasa con una probabilidad de salida pesada superior a 2/3 con 2 sigmas, y da `QV = 2ᴺ` (2¹⁶ en el H2, con 200 circuitos de 296 puertas de dos qubits de media) [@moses-2023, §IV B, p. 8]. Para tu circuito, usa el [producto de fidelidades](coherence-and-fidelity.md#layer-3).
3. *¿La fidelidad GHZ está corregida de SPAM?* La del H2 no lo está, y una fidelidad >0,5 solo indica entrelazamiento multipartito [@moses-2023, §IV D, p. 10].
4. *¿Se reclama ventaja?* Los autores del H2 no la reclaman: 32 qubits está dentro de lo simulable clásicamente [@moses-2023, §IV C, p. 9].

Son señales de alarma: "conectividad total" sin decir el coste de transporte; volumen cuántico como único dato; fidelidades de benchmark de componentes sin el efectivo del sistema; "qubits lógicos" sin decir si se descartan ejecuciones; y cifras del fabricante sin una réplica independiente (ver [experimentos con qubits lógicos](../../error-correction/concepts/logical-qubit-experiments.md)).

### Las fuentes discrepan
Los autores del H2 afirman que `QV = 2ᴺ` implica buen rendimiento en muchos circuitos con más de `N` qubits [@moses-2023, §IV B, p. 8]. Es una afirmación del fabricante sobre su propia métrica; conviene contrastarla con el producto de fidelidades para el circuito concreto.

### Para seguir
[Qubits de átomos neutros](neutral-atom-qubits.md) comparte la identidad de los átomos pero cambia el bus de movimiento por interacciones de Rydberg y registros mucho mayores.
