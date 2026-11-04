---
concept: quantization-and-wave-particle
title: "Cuantización y dualidad onda-partícula"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
La energía de la luz se intercambia en paquetes indivisibles (fotones) y la materia se comporta como una onda de longitud `λ = h/p`. "Onda" y "partícula" no son dos tipos de objeto, sino dos comportamientos de un mismo objeto cuántico, y según el experimento aparece uno u otro [@openstax-physics-3, §6.6].

### Explicación
La física clásica trata la luz como una onda continua y la materia como partículas con posición y velocidad definidas. A principios del siglo XX varios experimentos mostraron que ninguna de las dos imágenes basta.

El primero es el de la radiación de una cavidad. Planck (1900) supuso que los osciladores de las paredes solo pueden tener energías `E = nhf`, es decir, intercambian energía en paquetes de `hf` (**cuantización, *quantization***). Con ello reproducía el espectro medido, que la teoría clásica predecía divergente a longitudes de onda cortas (la "catástrofe ultravioleta"). La constante `h` vale 6,626×10⁻³⁴ J·s [@openstax-physics-3, §6.1]. Planck vio al principio la cuantización como un artificio matemático; Einstein le dio sentido físico como partículas de luz [@openstax-physics-3, §6.1].

Esas partículas son los **fotones (photons)**. En el efecto fotoeléctrico existe una frecuencia umbral por debajo de la cual no sale corriente, la corriente crece con la intensidad y la energía de los electrones no depende de la intensidad [@zwiebach-mit-8-04, LN3 §1, p. 1]. Einstein (1905) lo explicó con cuantos de energía `hν`: más intensidad significa más fotones por segundo, no fotones más energéticos [@zwiebach-mit-8-04, LN3 §1, pp. 1-2]. La energía de un fotón depende solo de su color, `E = hν`, y un "cuanto" de luz es un paquete indivisible de energía e impulso, no una partícula clásica con posición y velocidad definidas [@zwiebach-mit-8-04, LN1 §3, pp. 5-6]. En la dispersión Compton (rayos X sobre electrones) la longitud de onda cambia, y esto convenció a casi todos los escépticos de que los fotones llevan impulso `p = h/λ` [@zwiebach-mit-8-04, LN3 §2, pp. 3-5].

La materia hace el camino inverso. De Broglie (1924) propuso que toda partícula de impulso `p` tiene una longitud de onda `λ = h/p`; si `h → 0` el carácter ondulatorio desaparece, así que es una propiedad puramente cuántica [@zwiebach-mit-8-04, LN3 §3, p. 6]. Se ha observado difracción de electrones (Davisson-Germer, 1927), interferencia de electrones de uno en uno en la doble rendija e interferencia de moléculas de cientos de átomos [@zwiebach-mit-8-04, LN3 §3, p. 6]. En la doble rendija cada electrón llega a un punto concreto, pero las franjas aparecen gradualmente aunque pasen de uno en uno [@openstax-physics-3, §6.6].

Para computación cuántica, esto explica por qué existe una teoría nueva: la energía se intercambia en paquetes discretos y los objetos pequeños interfieren como ondas. La interferencia, que se desarrolla en el [principio de superposición](superposition-principle.md), es la herramienta con la que los algoritmos cuánticos amplifican respuestas correctas, ordenando las amplitudes para que las erróneas se cancelen y la correcta se refuerce [@aaronson-2018, Lec16, p. 3; Lec18, pp. 1-2]. Los fotones, además, son uno de los candidatos físicos a qubit (ver [sistemas de dos niveles](two-level-systems.md)).

### Ejemplo
Un solo electrón se lanza contra una doble rendija. Cada electrón deja un punto concreto en la pantalla, como una partícula. Pero si se acumulan muchos, aunque hayan pasado de uno en uno, los puntos dibujan poco a poco franjas de interferencia, como una onda [@openstax-physics-3, §6.6]. El mismo objeto se comporta como partícula al llegar y como onda al propagarse.

### Errores frecuentes
- *"El electrón es una bolita que además ondula."* Un cuanto no es una partícula clásica con posición y velocidad definidas [@zwiebach-mit-8-04, LN1 §3, pp. 5-6]. El comportamiento se describe con una función de onda cuyo módulo al cuadrado da probabilidades ([regla de Born](born-rule-measurement.md)).
- *"Cuantizado significa pequeño."* Significa discreto: la energía de la luz de un color se aumenta añadiendo fotones, no haciendo más grande el fotón [@zwiebach-mit-8-04, LN1 §3, pp. 5-6].

### Para seguir
Lo siguiente es el [principio de superposición](superposition-principle.md): cómo se suman las ondas de probabilidad y por qué eso produce interferencia. La capa 2 de este concepto da las relaciones de De Broglie y el criterio para saber cuándo notar las ondas.

## Comprensión {#layer-2}

### Idea clave
Las relaciones `p = ħk` y `E = ħω` valen para toda partícula y fijan cuándo importan las ondas: cuando la longitud de onda de De Broglie no es mucho menor que la escala del problema [@zwiebach-mit-8-04, LN4 §1, pp. 3-4; LN3 §3, pp. 6-7].

### Explicación
Las relaciones de De Broglie, `p = ħk` y `E = ħω`, valen para todas las partículas, y Zwiebach da tres motivaciones: la velocidad de grupo del paquete de ondas iguala la de la partícula, la coherencia relativista de los cuadrivectores y el acuerdo con `E = hν` para fotones [@zwiebach-mit-8-04, LN4 §1, pp. 3-4]. El impulso del fotón y la longitud de onda de De Broglie son la misma relación `p = h/λ` vista desde la luz y desde la materia [@openstax-physics-3, §6.3, §6.5].

De ahí sale un criterio. Los efectos ondulatorios son despreciables cuando la longitud de onda de De Broglie es mucho menor que el obstáculo, esto es, cuando `x·p` es mucho mayor que `h` [@zwiebach-mit-8-04, LN3 §3, pp. 6-7]. Por eso la mecánica cuántica es imprescindible para describir electrones, átomos y fotones y no hace falta para una pelota.

El efecto fotoeléctrico también da una predicción cuantitativa: la energía máxima de los electrones crece linealmente con la frecuencia, `K_max = hf − φ`, con `φ` la función de trabajo [@openstax-physics-3, §6.2]. Millikan lo confirmó en 1915 y fijó `h` con menos de un 1 % de error, aunque todavía hubo escépticos sobre que la luz estuviera hecha de partículas [@zwiebach-mit-8-04, LN3 §1, p. 2].

Este camino prepara la descripción matemática: la onda se convierte en un vector de un espacio complejo ([el estado cuántico como vector](state-vector-postulate.md)) y la "partícula" aparece al medir ([medida y regla de Born](born-rule-measurement.md)).

### Ejemplo
Una pelota de baloncesto (0,65 kg a 10 m/s) tiene `λ ≈ 10⁻³⁴ m`, indetectable. Un electrón con 1 eV de energía cinética tiene `λ ≈ 1,23 nm`, comparable a distancias atómicas [@openstax-physics-3, §6.5].

### Errores frecuentes
- *"Un campo electromagnético clásico es un número fijo de fotones."* Los campos clásicos corresponden a estados coherentes con número de fotones fluctuante [@zwiebach-mit-8-04, LN3 §3, pp. 6-7].

### Para seguir
La capa 3 explica qué conservar de esta historia al programar, donde casi nunca hay ondas en el espacio sino grados de libertad discretos.

## Profesional {#layer-3}

### Idea clave
Al programar, de la dualidad sobrevive el aspecto ondulatorio: sumas de amplitudes con fases que interfieren, sobre grados de libertad discretos como la polarización, el espín o los niveles de energía [@zwiebach-mit-8-04, LN1 §4, pp. 10-12; @preskill-ph219, ch.2 §2.2.1, p. 14].

### Explicación
En computación cuántica casi nunca se trabaja con ondas en el espacio. Zwiebach muestra que la polarización del fotón y el espín del electrón comparten la misma estructura de dos estados [@zwiebach-mit-8-04, LN1 §4, pp. 10-12]. La equivalencia formal con el espín 1/2 vale para cualquier sistema de dos niveles [@preskill-ph219, ch.2 §2.2.1, p. 14].

Que interfieran moléculas de cientos de átomos y de C₆₀ indica que la naturaleza ondulatoria no se limita a partículas elementales [@zwiebach-mit-8-04, LN3 §3, p. 6; @openstax-physics-3, §6.5]. Si no vemos superposiciones macroscópicas, la razón la da la [decoherencia](decoherence.md), no una frontera en el tamaño.

Un hecho físico basta para los qubits fotónicos: un fotón no se divide, se absorbe o se transmite entero, porque un fotón fraccionario tendría otra frecuencia [@zwiebach-mit-8-04, LN1 §3, p. 7]. Cómo se usan los fotones como qubits se trata en el ámbito de hardware ([qubits fotónicos](../../quantum-hardware/concepts/photonic-qubits.md)).

### Ejemplo
Para decidir si un sistema necesita tratamiento cuántico, compara su longitud de onda de De Broglie con la escala del obstáculo, como en la capa anterior [@zwiebach-mit-8-04, LN3 §3, pp. 6-7]. Una pelota (`λ ≈ 10⁻³⁴ m`) se trata clásicamente; un electrón de 1 eV (`λ ≈ 1,23 nm`) o una molécula de C₆₀ que interfiere requieren la teoría cuántica [@openstax-physics-3, §6.5].

### Para seguir
Para el recorrido histórico completo con datos numéricos, OpenStax cap. 6 [@openstax-physics-3, §6.1-6.6]; para una presentación matemática más cuidadosa, Zwiebach LN1-LN4 [@zwiebach-mit-8-04, LN1-LN4]. Siguiente concepto: el [principio de superposición](superposition-principle.md).
