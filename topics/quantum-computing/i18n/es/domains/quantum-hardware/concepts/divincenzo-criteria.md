---
concept: divincenzo-criteria
title: "Criterios de DiVincenzo"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
Los *criterios de DiVincenzo (DiVincenzo criteria)* son la lista de requisitos que debe cumplir un sistema físico para servir como ordenador cuántico: cinco para computar y dos más para comunicar. Sirven para comparar las muchas propuestas de realización física [@divincenzo-2000, p. 2 §III].

### Explicación
David DiVincenzo, investigador de IBM, publicó la lista en el año 2000 a partir de discusiones con colegas durante varios años. Los cinco primeros requisitos bastan para computar; los otros dos solo hacen falta para comunicar información cuántica [@divincenzo-2000, p. 1; p. 2 §III; p. 6 §IV].

Para construir un ordenador clásico necesitas bits que aguanten su valor, una forma de ponerlos a cero al empezar, puertas lógicas y una forma de leer el resultado. Los criterios son esa misma lista adaptada a qubits. Recuerda que un [qubit](../../qubits-and-circuits/concepts/qubit.md) puede ser cualquier sistema cuántico de dos niveles: el espín de un electrón, los dos estados de un átomo, la polarización de un fotón [@divincenzo-2000, p. 2 §III.1].

| N.º | Requisito | En palabras llanas |
|---|---|---|
| 1 | Sistema físico escalable con qubits bien caracterizados | Muchos qubits, y se sabe con precisión cómo se comportan y cómo se acoplan entre sí [@divincenzo-2000, p. 2] |
| 2 | Inicialización a un estado de partida, como \|000…⟩ | Poder empezar siempre desde el mismo estado conocido [@divincenzo-2000, p. 3 §III.2] |
| 3 | Tiempos de decoherencia mucho más largos que el tiempo de una puerta | El qubit aguanta lo bastante para hacer muchas operaciones antes de olvidarse [@divincenzo-2000, p. 3 §III.3] |
| 4 | Conjunto universal de puertas | Un repertorio de operaciones suficiente para cualquier [circuito cuántico](../../qubits-and-circuits/concepts/quantum-circuits.md) [@divincenzo-2000, pp. 4-5 §III.4] |
| 5 | Medida específica de cada qubit | Poder leer el resultado de un qubit concreto sin molestar al resto [@divincenzo-2000, p. 6 §III.5] |
| 6 | Convertir qubits estacionarios en "voladores" y viceversa | Solo para comunicar [@divincenzo-2000, p. 7 §IV] |
| 7 | Transmitir qubits voladores sin estropearlos | Solo para comunicar [@divincenzo-2000, p. 7 §IV] |

Los qubits voladores son casi siempre fotones. Un ordenador que no se comunica con otros solo necesita los cinco primeros; la criptografía cuántica solo necesita el séptimo [@divincenzo-2000, p. 7 §IV].

Por eso la lista es sobre todo una herramienta de comparación: cuando alguien propone un tipo de qubit, se comprueba cuál de los cinco puntos cumple bien y cuál es su cuello de botella. En el resto del ámbito la usamos así: cada plataforma ([superconductores](superconducting-qubits.md), [iones](trapped-ion-qubits.md), [átomos neutros](neutral-atom-qubits.md) y [fotones](photonic-qubits.md), y más adelante los espines y los qubits topológicos) tiene un criterio que le cuesta más.

### Ejemplo
Un ion atrapado cumple los criterios así:

1. *Inicialización (2):* bombeo óptico y enfriamiento del movimiento.
2. *Medida (5):* se observa si el ion emite luz (fluorescencia dependiente del estado).
3. *Puertas (4):* las puertas universales salen de rotaciones de un qubit más una puerta entrelazante.
4. *Coherencia (3):* una coherencia mucho más larga que las puertas cubre el criterio 3 [@bruzewicz-2019, pp. 2-3].

### Para seguir
[Coherencia (T1, T2) y fidelidad de puertas](coherence-and-fidelity.md) convierte el criterio 3 en números que se pueden calcular. La capa 2 de este concepto explica por qué cada criterio es como es.

## Comprensión {#layer-2}

### Idea clave
Cada criterio nace de una necesidad de la corrección de errores: qubits conocidos con exactitud, qubits frescos continuos, coherencia mucho mayor que el tiempo de puerta, puertas universales en paralelo y una medida que no perturbe al resto [@divincenzo-2000, pp. 2-6].

### Explicación
El criterio 1 pide qubits "bien caracterizados": que se conozca con exactitud el hamiltoniano interno del qubit y sus acoplamientos a otros niveles, a otros qubits y a los campos de control. Si el qubit tiene niveles extra, el control debe mantener muy baja la probabilidad de entrar en ellos, y "muy baja" la fija lo que tolere la corrección de errores [@divincenzo-2000, p. 2]. Esa es la raíz de la *fuga (leakage)* que aparece en [coherencia y fidelidad](coherence-and-fidelity.md).

La inicialización (2) no se necesita solo al principio: la corrección de errores consume un suministro continuo de qubits frescos de baja entropía, como `|0⟩`. Hay dos caminos, enfriar hasta el estado fundamental o medir, que es otra forma de enfriar. La termalización natural nunca es más rápida que la decoherencia, así que es demasiado lenta para corregir errores; el enfriamiento por medida puede ser mucho más rápido [@divincenzo-2000, p. 3].

De ahí sale el criterio 3: lo que cuenta es el **cociente** entre coherencia y tiempo de puerta, no el tiempo absoluto. Gracias a la corrección de errores cuánticos (1995-96), la coherencia necesaria no crece con la longitud del cálculo. Solo cuenta la decoherencia "relevante": que un electrón pierda rápido su coherencia orbital no importa si el qubit está codificado en el espín. Y depende del sistema concreto, porque un espín junto a la superficie de un dispositivo puede comportarse distinto que en el interior [@divincenzo-2000, p. 4].

Para las puertas (4), los algoritmos son secuencias de operaciones sobre pocos qubits (normalmente tres como mucho), pero un dispositivo solo ofrece ciertos hamiltonianos. Las puertas de tres qubits se reducen a puertas de uno y dos, y las interacciones de dos qubits pueden ser de un solo tipo, la CNOT [@divincenzo-2000, pp. 4-5]. Cuando la CNOT no está disponible directamente, hay que mostrar una secuencia que la sintetice con la interacción disponible y puertas de un qubit [@divincenzo-2000, p. 5]. Es la idea de los [conjuntos universales de puertas](../../qubits-and-circuits/concepts/universal-gate-sets.md) y de las [puertas de dos qubits](../../qubits-and-circuits/concepts/two-qubit-gates.md) vista desde el hardware.

Si los qubits no se acoplan directamente, un "qubit bus" (vibración de una cadena de iones, un fotón de cavidad) media la interacción, pero añade canales de decoherencia durante la puerta. La corrección de errores exige además poder operar en paralelo sobre una fracción finita de qubits [@divincenzo-2000, p. 5].

La medida (5) ideal devuelve 0 con la probabilidad correcta sin perturbar al resto del ordenador. Una medida rápida, del orden de 10⁻⁴ del tiempo de decoherencia, simplifica la corrección de errores [@divincenzo-2000, p. 6]. En cuanto a la comunicación (6-7), en 2000 el criterio 6 era "el realmente difícil": solo el esquema de Kimble con fotones de cavidad era lo bastante concreto como para planear experimentos [@divincenzo-2000, p. 7].

Los mismos criterios reaparecen en la literatura de cada tecnología. Los iones atrapados han cumplido los cinco con alta fidelidad, según sus autores, y esencialmente desde 2004 [@bruzewicz-2019, pp. 2-3]. Los qubits de espín los han cumplido, según la revisión de Burkard y colaboradores [@burkard-2023, §I, p. 2]. Los fotones cumplen aproximadamente cinco de los siete: lo difícil viene de la débil interacción fotón-fotón (puertas deterministas de dos qubits) y de la pérdida de fotones [@slussarenko-2019, p. 1].

### Ejemplo
Dos casos que muestran el porqué de los criterios:

- *Una medida poco eficiente se compensa con recursos.* Se copia el valor del qubit con CNOT en muchos qubits y se miden todos; con una eficiencia del 1 % basta con cientos de copias [@divincenzo-2000, p. 6].
- *Un electrón compartido entre dos puntos cuánticos no forma dos qubits.* La regla de superselección prohíbe superponer números de partículas distintos, así que es un solo qubit (electrón a la izquierda o a la derecha). Es la trampa clásica del criterio 1 [@divincenzo-2000, p. 2].

### Errores frecuentes
- *"Si se cumplen los cinco criterios, ya hay un ordenador útil."* No. Los iones los cumplen desde 2004 y, en 2019, el mayor registro completamente controlado era de 20 iones [@bruzewicz-2019, pp. 2-3]. En la práctica la escalabilidad exige más: modularidad, integración, corrección de errores, una arquitectura con conectividad, tratamiento de la pérdida de iones y direccionamiento y lectura escalables [@bruzewicz-2019, §I.E, pp. 5-6].
- *"La lista dice qué plataforma ganará."* DiVincenzo escribió que nadie puede decir qué tecnología ganará y que preguntarlo quizá sea contraproducente [@divincenzo-2000, p. 7 §V]. Veinte años después, los revisores de iones y de espines siguen diciendo que es pronto para decidir [@bruzewicz-2019, p. 5; @burkard-2023, §VIII, pp. 51-52].
- *"Es una lista de cinco números."* Solo el criterio 3 lleva una cifra, y es un cociente estimado en 2000 [@divincenzo-2000, p. 4]; el resto son requisitos cualitativos que cada plataforma debe satisfacer con su propia métrica (ver [coherencia y fidelidad](coherence-and-fidelity.md)).

### Las fuentes discrepan
Las cifras de 2000 y las de hoy no son comparables sin más. DiVincenzo estimó que si el tiempo de decoherencia es unas 10⁴ a 10⁵ veces el tiempo de reloj de la puerta la corrección de errores puede funcionar, y él mismo lo llamó exigente [@divincenzo-2000, p. 4]. Dio también como error aleatorio tolerable por puerta unos 10⁻⁴ a 10⁻⁵ [@divincenzo-2000, p. 5]. Dio también unas 10 ancillas por qubit computacional, con crecimiento solo logarítmico [@divincenzo-2000, p. 4].

Los umbrales que se manejan hoy dependen del código y del modelo de ruido: para el código de superficie, de orden 10⁻² en el error de puertas de dos qubits según simulaciones [@krantz-2019, p. 35; @eisert-2025, Box 2, p. 5]. Conviene tratar las cifras de 2000 como estimaciones de su época; el tema se desarrolla en el [teorema del umbral](../../error-correction/concepts/threshold-theorem.md).

### Para seguir
La capa 3 usa los criterios como auditoría de un anuncio o de una plataforma y añade los requisitos de ingeniería que la lista no recoge.

## Profesional {#layer-3}

### Idea clave
En la práctica los criterios sirven para hacer preguntas incómodas a un anuncio o un artículo: qué criterio le cuesta más a cada plataforma y qué requisitos de ingeniería quedan fuera de la lista (medida a mitad de circuito, conectividad, calibración, apoyo clásico).

### Explicación
Lo que las fuentes identifican como lo más difícil en cada plataforma:

- *Superconductores:* escala y cableado. Los autores de la revisión de 2019-20 estiman que las técnicas actuales llegan a unos 1000 qubits y que más allá hacen falta electrónica de control criogénica y decodificadores en línea [@kjaergaard-2020, §5.3, p. 23].
- *Iones:* la escalabilidad (criterio 1) y la velocidad; la carga de control óptico y electrónico frena el crecimiento [@bruzewicz-2019, p. 5].
- *Átomos neutros:* inicialización y lectura lentas. El registro se reconstruye en cada ciclo, que en 2020 duraba unos 200 ms [@henriet-2020, p. 6; p. 12]. La lectura por imagen sigue siendo órdenes de magnitud más lenta que las puertas [@saffman-2025, p. 17; p. 21].
- *Espines:* la fabricación, porque tienen las exigencias más estrictas por su tamaño [@burkard-2023, §VIII, p. 51].
- *Fotones:* el criterio 4 en su versión determinista (puertas de dos qubits) y la pérdida [@slussarenko-2019, p. 1].
- *Topológicos:* el criterio 1; la primera pregunta es si existe un qubit bien caracterizado (ver [qubits topológicos](topological-qubits.md)).

Además, las fuentes del ámbito añaden de forma implícita requisitos que conviene tratar como criterios de ingeniería:

- *Medida a mitad de circuito y reinicio.* La corrección de errores mide ancillas durante el circuito; en iones y átomos esa medida puede perturbar a los qubits vecinos por la luz dispersa, y se resuelve con una segunda especie, con transporte a una zona de lectura o escondiendo los datos [@bruzewicz-2019, p. 24; @saffman-2025, pp. 18-19; @moses-2023, §II D, p. 4].
- *Conectividad.* Preskill citaba ya en 2018 la conectividad y el rendimiento de fabricación como medidas de calidad además del número de qubits [@preskill-2018, §4.2, p. 5]; ver [transpilación](../../qiskit-programming/concepts/transpilation.md).
- *Carga de calibración.* En Sycamore (2019) hubo que ajustar más de 100 parámetros por qubit, con unas 36 horas de puesta en marcha tras enfriar y unas 4 horas diarias de mantenimiento [@arute-2019, VI A-B, pp. 11-14]; los iones de una misma especie son idénticos y necesitan la misma frecuencia, lo que reduce la calibración [@bruzewicz-2019, p. 4].
- *Apoyo clásico.* El decodificador en tiempo real tiene que seguir el ritmo del hardware; si no, el ordenador se frena [@eisert-2025, Sec. III, pp. 4-5; @google-2025, p. 5].

### Ejemplo
Qué criterio manda depende de lo que quieras hacer (esta clasificación es un criterio propio basado en los puntos anteriores, no una taxonomía de las fuentes):

1. *Programar y probar algoritmos hoy:* manda la fidelidad de las puertas de dos qubits y la conectividad, porque fijan cuántas puertas caben (ver el cálculo en [coherencia y fidelidad](coherence-and-fidelity.md)).
2. *Experimentos de corrección de errores:* mandan la medida a mitad de circuito, la velocidad del ciclo y la fidelidad frente al umbral ([experimentos con qubits lógicos](../../error-correction/concepts/logical-qubit-experiments.md)).
3. *Máquinas de gran escala:* manda la escalabilidad de los puntos 1 y 3 de DiVincenzo con coste razonable (cableado, láseres, fabricación).

Y tres señales de alarma al leer un anuncio con los criterios en la mano:

- Un número de qubits sin cifras de fidelidad de puertas y de lectura solo habla del criterio 1.
- Una cifra de "coherencia" sin el tiempo de puerta (criterio 3) no dice si cuenta para algo. Un qubit muy rápido no es bueno si no se compara con su coherencia, y uno muy coherente es menos atractivo si sus puertas son muy lentas [@stano-2022, p. 7].
- Un "qubit" sin demostración de puertas ni de lectura (criterios 4 y 5) no es todavía un qubit de computación; es el caso de los [qubits topológicos](topological-qubits.md).

### Para seguir
[Comparativa y estado actual del hardware](hardware-landscape.md) pone todas las plataformas bajo las mismas métricas y con fecha.
