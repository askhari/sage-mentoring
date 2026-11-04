---
concept: divincenzo-criteria
title: "Criterios de DiVincenzo"
---

## Fundamentos {#layer-1}

**Qué son.** Los *criterios de DiVincenzo (DiVincenzo criteria)* son una lista de requisitos que debe cumplir un sistema físico para servir como ordenador cuántico. David DiVincenzo, investigador de IBM, los publicó en el año 2000 a partir de discusiones con colegas durante varios años, y se usan para comparar las muchas propuestas de realización física [@divincenzo-2000, p. 2 §III]. Son **cinco** requisitos para computar y **dos** más para comunicar información cuántica; los cinco primeros bastan para computar [@divincenzo-2000, p. 1; p. 2 §III; p. 6 §IV].

**Una analogía con un ordenador clásico.** Para construir un ordenador clásico necesitas bits que aguanten su valor, una forma de ponerlos a cero al empezar, puertas lógicas, y una forma de leer el resultado. Los criterios son esa misma lista, adaptada a qubits. Recuerda que un [qubit](../../qubits-and-circuits/concepts/qubit.md) puede ser cualquier sistema cuántico de dos niveles: el espín de un electrón, los dos estados de un átomo, la polarización de un fotón [@divincenzo-2000, p. 2 §III.1].

| N.º | Requisito | En palabras llanas |
|---|---|---|
| 1 | Sistema físico escalable con qubits bien caracterizados | Muchos qubits, y se sabe con precisión cómo se comportan y cómo se acoplan entre sí [@divincenzo-2000, p. 2] |
| 2 | Inicialización a un estado de partida, como \|000…⟩ | Poder empezar siempre desde el mismo estado conocido [@divincenzo-2000, p. 3 §III.2] |
| 3 | Tiempos de decoherencia mucho más largos que el tiempo de una puerta | El qubit aguanta lo bastante para hacer muchas operaciones antes de olvidarse [@divincenzo-2000, p. 3 §III.3] |
| 4 | Conjunto universal de puertas | Un repertorio de operaciones suficiente para cualquier [circuito cuántico](../../qubits-and-circuits/concepts/quantum-circuits.md) [@divincenzo-2000, pp. 4-5 §III.4] |
| 5 | Medida específica de cada qubit | Poder leer el resultado de un qubit concreto sin molestar al resto [@divincenzo-2000, p. 6 §III.5] |
| 6 | Convertir qubits estacionarios en "voladores" y viceversa | Solo para comunicar [@divincenzo-2000, p. 7 §IV] |
| 7 | Transmitir qubits voladores sin estropearlos | Solo para comunicar [@divincenzo-2000, p. 7 §IV] |

Los qubits voladores son casi siempre fotones [@divincenzo-2000, p. 7]. Un ordenador que no se comunica con otros solo necesita los cinco primeros; la criptografía cuántica solo necesita el séptimo [@divincenzo-2000, p. 7 §IV].

**Para qué sirve la lista.** Es una herramienta de comparación: cuando alguien propone un tipo de qubit, se comprueba cuál de los cinco puntos cumple bien y cuál es el cuello de botella. En los demás conceptos de este ámbito la usamos así: cada plataforma ([superconductores](superconducting-qubits.md), [iones](trapped-ion-qubits.md), [átomos neutros](neutral-atom-qubits.md), [espines](spin-qubits.md), [fotones](photonic-qubits.md), [topológicos](topological-qubits.md)) tiene un criterio que le cuesta más.

**Un ejemplo concreto.** Un ion atrapado cumple los criterios de este modo: se inicializa con una técnica óptica (bombeo óptico) y enfriamiento del movimiento; se lee observando si emite luz (fluorescencia dependiente del estado); las puertas universales salen de rotaciones de un qubit más una puerta entrelazante; y una coherencia mucho más larga que las puertas cubre el criterio 3 [@bruzewicz-2019, pp. 2-3].

## Comprensión {#layer-2}

**Por qué cada criterio es como es.**

- *Qubits bien caracterizados (1).* "Bien caracterizado" quiere decir que se conoce con exactitud el hamiltoniano interno del qubit y sus acoplamientos a otros niveles, a otros qubits y a los campos de control [@divincenzo-2000, p. 2]. Si el qubit tiene niveles extra, el control debe mantener muy baja la probabilidad de entrar en ellos, y "muy baja" la fija lo que tolere la corrección de errores [@divincenzo-2000, p. 2]. Esto es el origen de la *fuga (leakage)* que verás en [coherencia y fidelidad](coherence-and-fidelity.md). Hay una trampa clásica: un electrón compartido entre dos puntos cuánticos no forma dos qubits, porque la regla de superselección prohíbe superponer números de partículas distintos; es un solo qubit (electrón a la izquierda o a la derecha) [@divincenzo-2000, p. 2].
- *Inicialización (2).* No solo hace falta al principio: la corrección de errores consume un suministro continuo de qubits frescos de baja entropía como `|0⟩` [@divincenzo-2000, p. 3]. Hay dos caminos, enfriar hasta el estado fundamental o medir (que es una forma de enfriar); la termalización natural nunca es más rápida que la decoherencia, así que es demasiado lenta para corregir errores, mientras que el enfriamiento por medida puede ser mucho más rápido [@divincenzo-2000, p. 3].
- *Coherencia frente a tiempo de puerta (3).* Lo que cuenta es el **cociente**, no el tiempo absoluto. DiVincenzo estimó en 2000 que si el tiempo de decoherencia es unas 10⁴ a 10⁵ veces el tiempo de reloj de la puerta, la corrección de errores puede funcionar, y él mismo lo llamó exigente [@divincenzo-2000, p. 4]. Gracias a la corrección de errores cuánticos (1995-96), la coherencia necesaria no crece con la longitud del cálculo [@divincenzo-2000, p. 4]. Solo cuenta la decoherencia "relevante": que un electrón pierda rápido su coherencia orbital no importa si el qubit está codificado en el espín [@divincenzo-2000, p. 4]. La decoherencia además depende del sistema concreto: un espín junto a la superficie de un dispositivo puede comportarse distinto que en el interior [@divincenzo-2000, p. 4].
- *Puertas universales (4).* Los algoritmos son secuencias de operaciones sobre pocos qubits (normalmente tres como mucho), pero un dispositivo solo ofrece ciertos hamiltonianos; las puertas de tres qubits se reducen a puertas de uno y dos, y las interacciones de dos qubits pueden ser de un solo tipo, la CNOT [@divincenzo-2000, pp. 4-5]. Cuando la CNOT no está disponible directamente, hay que mostrar una secuencia que la sintetice con la interacción disponible y puertas de un qubit [@divincenzo-2000, p. 5]; es la idea de los [conjuntos universales de puertas](../../qubits-and-circuits/concepts/universal-gate-sets.md) y de las [puertas de dos qubits](../../qubits-and-circuits/concepts/two-qubit-gates.md) vista desde el hardware. Si los qubits no se acoplan directamente, un "qubit bus" (vibración de una cadena de iones, un fotón de cavidad) media la interacción, pero añade canales de decoherencia durante la puerta [@divincenzo-2000, p. 5]. La corrección de errores exige además poder operar en paralelo sobre una fracción finita de qubits [@divincenzo-2000, p. 5].
- *Medida (5).* La medida ideal devuelve 0 con la probabilidad correcta sin perturbar al resto del ordenador [@divincenzo-2000, p. 6]. Una medida de baja eficiencia puede compensarse con recursos: copiar el valor del qubit con CNOT en muchos qubits y medirlos todos; con una eficiencia del 1 % basta con cientos de copias [@divincenzo-2000, p. 6]. Y una medida rápida, del orden de 10⁻⁴ del tiempo de decoherencia, simplifica la corrección de errores [@divincenzo-2000, p. 6].
- *Comunicación (6-7).* En 2000, el criterio 6 era "el realmente difícil": solo el esquema de Kimble con fotones de cavidad era lo bastante concreto como para planear experimentos [@divincenzo-2000, p. 7].

**Qué dicen las cifras de 2000 y qué no.** El artículo da como error aleatorio tolerable por puerta unos 10⁻⁴ a 10⁻⁵, en el mismo rango que el umbral de decoherencia [@divincenzo-2000, p. 5], y unas 10 ancillas por qubit computacional (con crecimiento solo logarítmico) [@divincenzo-2000, p. 4]. Son estimaciones **de 2000**. Los umbrales de corrección de errores que se manejan hoy dependen del código y del modelo de ruido: para el código de superficie, de orden 10⁻² en el error de puertas de dos qubits según simulaciones [@krantz-2019, p. 35; @eisert-2025, Box 2, p. 5]. No se pueden comparar las dos cifras sin más; el tema se desarrolla en el [teorema del umbral](../../error-correction/concepts/threshold-theorem.md).

**Cómo se aplican a cada plataforma (resumen).** Los mismos criterios aparecen en la literatura de cada tecnología:

- Los iones atrapados han cumplido los cinco criterios con alta fidelidad, según sus autores, y esencialmente desde 2004 [@bruzewicz-2019, pp. 2-3].
- Los qubits de espín han cumplido los criterios, según la revisión de Burkard y colaboradores [@burkard-2023, §I, p. 2].
- Los fotones cumplen aproximadamente cinco de los siete, y lo difícil viene de la débil interacción fotón-fotón (puertas de dos qubits deterministas), más la pérdida de fotones [@slussarenko-2019, p. 1].

**Errores frecuentes.**

- *"Si se cumplen los cinco criterios, ya hay un ordenador útil."* No. Los iones los cumplen desde 2004 y, en 2019, el mayor registro completamente controlado era de 20 iones [@bruzewicz-2019, pp. 2-3]. En la práctica la escalabilidad exige más: modularidad, integración, corrección de errores, una arquitectura con conectividad, tratamiento de la pérdida de iones y direccionamiento y lectura escalables [@bruzewicz-2019, §I.E, pp. 5-6].
- *"La lista dice qué plataforma ganará."* DiVincenzo escribió que nadie puede decir qué tecnología ganará y que preguntarlo quizá sea contraproducente [@divincenzo-2000, p. 7 §V]. Veinte años después, los revisores de iones y de espines siguen diciendo que es pronto para decidir [@bruzewicz-2019, p. 5; @burkard-2023, §VIII, pp. 51-52].
- *"Es una lista de cinco números."* Solo el criterio 3 lleva una cifra, y es un cociente estimado en 2000 [@divincenzo-2000, p. 4]; el resto son requisitos cualitativos que cada plataforma debe satisfacer con su propia métrica (ver [coherencia y fidelidad](coherence-and-fidelity.md)).

## Profesional {#layer-3}

**La lista como auditoría de una plataforma.** En la práctica, los criterios sirven para hacer preguntas incómodas a un anuncio o un artículo. Para cada plataforma, lo que las fuentes identifican como lo más difícil es:

- *Superconductores:* escala y cableado. Los autores de la revisión de 2019-20 estiman que las técnicas actuales llegan a unos 1000 qubits y que más allá hacen falta electrónica de control criogénica y decodificadores en línea [@kjaergaard-2020, §5.3, p. 23].
- *Iones:* la escalabilidad (criterio 1) y la velocidad; la carga de control óptico y electrónico frena el crecimiento [@bruzewicz-2019, p. 5].
- *Átomos neutros:* inicialización y lectura lentas. El registro se reconstruye en cada ciclo, que en 2020 duraba unos 200 ms [@henriet-2020, p. 6; p. 12], y la lectura por imagen sigue siendo órdenes de magnitud más lenta que las puertas [@saffman-2025, p. 17; p. 21].
- *Espines:* la fabricación, porque tienen las exigencias más estrictas por su tamaño [@burkard-2023, §VIII, p. 51].
- *Fotones:* el criterio 4 en su versión determinista (puertas de dos qubits) y la pérdida [@slussarenko-2019, p. 1].
- *Topológicos:* el criterio 1: la primera pregunta es si existe un qubit bien caracterizado; ver [qubits topológicos](topological-qubits.md).

**Lo que los cinco criterios no recogen y a un profesional le importa.** Las fuentes de este ámbito añaden, de forma implícita, otros requisitos que conviene tratar como criterios de ingeniería:

- *Medida a mitad de circuito y reinicio.* La corrección de errores mide ancillas durante el circuito; en iones y átomos esa medida puede perturbar a los qubits vecinos por la luz dispersa, y se resuelve con una segunda especie, con transporte a una zona de lectura o escondiendo los datos [@bruzewicz-2019, p. 24; @saffman-2025, pp. 18-19; @moses-2023, §II D, p. 4].
- *Conectividad.* Preskill citaba ya en 2018 la conectividad y el rendimiento de fabricación como medidas de calidad además del número de qubits [@preskill-2018, §4.2, p. 5]; ver [transpilación](../../qiskit-programming/concepts/transpilation.md).
- *Carga de calibración.* En Sycamore (2019) hubo que ajustar más de 100 parámetros por qubit, con unas 36 horas de puesta en marcha tras enfriar y unas 4 horas diarias de mantenimiento [@arute-2019, VI A-B, pp. 11-14]; los iones de una misma especie son idénticos y necesitan la misma frecuencia, lo que reduce la calibración [@bruzewicz-2019, p. 4].
- *Apoyo clásico.* El decodificador en tiempo real tiene que seguir el ritmo del hardware; si no, el ordenador se frena [@eisert-2025, Sec. III, pp. 4-5; @google-2025, p. 5].

**Cómo decidir qué criterio manda.** La respuesta depende de lo que quieras hacer:

1. *Programar y probar algoritmos hoy:* manda la fidelidad de las puertas de dos qubits y la conectividad, porque fijan cuántas puertas caben (ver el cálculo en [coherencia y fidelidad](coherence-and-fidelity.md)).
2. *Experimentos de corrección de errores:* mandan la medida a mitad de circuito, la velocidad del ciclo y la fidelidad frente al umbral ([experimentos con qubits lógicos](../../error-correction/concepts/logical-qubit-experiments.md)).
3. *Máquinas de gran escala:* manda la escalabilidad de los puntos 1 y 3 de DiVincenzo con coste razonable (cableado, láseres, fabricación).

Esta clasificación es un criterio propio basado en los puntos anteriores, no una taxonomía de las fuentes.

**Señales de alarma al leer un anuncio con los criterios en la mano.**

- Un número de qubits sin cifras de fidelidad de puertas y de lectura solo habla del criterio 1.
- Una cifra de "coherencia" sin el tiempo de puerta (criterio 3) no dice si cuentan para algo. Stano y colaboradores lo plantean así: un qubit muy rápido no es bueno si no se compara con su coherencia, y uno muy coherente es menos atractivo si sus puertas son muy lentas [@stano-2022, p. 7].
- Un "qubit" sin demostración de puertas ni de lectura (criterios 4 y 5) no es todavía un qubit de computación; es el caso de los [qubits topológicos](topological-qubits.md).

Para ver cómo se comparan todas las plataformas con las mismas métricas, y con fecha, pasa a [comparativa y estado actual del hardware](hardware-landscape.md).
