---
concept: quantization-and-wave-particle
title: "Cuantización y dualidad onda-partícula"
---

## Fundamentos {#layer-1}

La física clásica trata la luz como una onda continua y la materia como partículas con posición y velocidad definidas. A principios del siglo XX varios experimentos mostraron que ninguna de las dos imágenes basta. Esta sección resume los tres que importan.

**La energía llega en paquetes (cuantización, *quantization*).** Planck (1900) supuso que los osciladores de las paredes de una cavidad solo pueden tener energías `E = nhf`, es decir, intercambian energía en paquetes de `hf`; con ello reproducía el espectro medido de la radiación, que la teoría clásica predecía divergente a longitudes de onda cortas (la "catástrofe ultravioleta") [@openstax-physics-3, §6.1]. La constante `h` vale 6,626×10⁻³⁴ J·s [@openstax-physics-3, §6.1]. Planck vio al principio la cuantización como un artificio matemático; Einstein le dio sentido físico como partículas de luz [@openstax-physics-3, §6.1].

**La luz se comporta como partículas (fotones, *photons*).** En el efecto fotoeléctrico existe una frecuencia umbral por debajo de la cual no sale corriente, la corriente crece con la intensidad y la energía de los electrones no depende de la intensidad [@zwiebach-mit-8-04, LN3 §1, p. 1]. Einstein (1905) lo explicó con cuantos de energía `hν`: más intensidad significa más fotones por segundo, no fotones más energéticos [@zwiebach-mit-8-04, LN3 §1, pp. 1-2]. La energía de un fotón depende solo de su color, `E = hν`, y un "cuanto" de luz es un paquete indivisible de energía e impulso, no una partícula clásica con posición y velocidad definidas [@zwiebach-mit-8-04, LN1 §3, pp. 5-6]. En la dispersión Compton (rayos X sobre electrones) la longitud de onda cambia, y esto convenció a casi todos los escépticos de que los fotones llevan impulso `p = h/λ` [@zwiebach-mit-8-04, LN3 §2, pp. 3-5].

**La materia se comporta como ondas.** De Broglie (1924) propuso que toda partícula de impulso `p` tiene una longitud de onda `λ = h/p`; si `h → 0` el carácter ondulatorio desaparece, así que es una propiedad puramente cuántica [@zwiebach-mit-8-04, LN3 §3, p. 6]. Se ha observado difracción de electrones (Davisson-Germer, 1927), interferencia de electrones de uno en uno en la doble rendija e interferencia de moléculas de cientos de átomos [@zwiebach-mit-8-04, LN3 §3, p. 6]. En la doble rendija, cada electrón llega a un punto concreto, pero las franjas aparecen gradualmente aunque pasen de uno en uno [@openstax-physics-3, §6.6].

**Idea central.** "Onda o partícula" no son dos tipos de objeto, sino dos comportamientos de un mismo objeto cuántico; según el experimento aparece uno u otro [@openstax-physics-3, §6.6].

**Por qué importa en computación cuántica.** Este concepto explica por qué existe una teoría nueva: la energía se intercambia en paquetes discretos y los objetos pequeños interfieren como ondas. La interferencia, que se desarrolla en el [principio de superposición](superposition-principle.md), es la herramienta con la que los algoritmos cuánticos amplifican respuestas correctas [unverified]. Los fotones, además, son uno de los candidatos físicos a qubit (ver [sistemas de dos niveles](two-level-systems.md)).

## Comprensión {#layer-2}

**De la energía al impulso: las relaciones de De Broglie.** Las relaciones `p = ħk` y `E = ħω` valen para todas las partículas; Zwiebach da tres motivaciones: la velocidad de grupo del paquete de ondas iguala la de la partícula, la coherencia relativista de los cuadrivectores y el acuerdo con `E = hν` para fotones [@zwiebach-mit-8-04, LN4 §1, pp. 3-4]. El impulso del fotón y la longitud de onda de De Broglie son la misma relación `p = h/λ` vista desde la luz y desde la materia [@openstax-physics-3, §6.3, §6.5].

**Cuándo notar las ondas.** Los efectos ondulatorios son despreciables cuando la longitud de onda de De Broglie es mucho menor que el obstáculo, esto es, cuando `x·p` es mucho mayor que `h` [@zwiebach-mit-8-04, LN3 §3, pp. 6-7]. Con números: una pelota de baloncesto (0,65 kg a 10 m/s) tiene `λ ≈ 10⁻³⁴ m`, indetectable, mientras que un electrón con 1 eV de energía cinética tiene `λ ≈ 1,23 nm` [@openstax-physics-3, §6.5]. Por eso la mecánica cuántica es imprescindible para describir electrones, átomos y fotones y no hace falta para una pelota.

**Qué predice el efecto fotoeléctrico y qué no.** Einstein predijo que la energía máxima de los electrones crece linealmente con la frecuencia: `K_max = hf − φ`, con `φ` la función de trabajo [@openstax-physics-3, §6.2]. Millikan lo confirmó en 1915 y fijó `h` con menos de un 1 % de error, aunque todavía hubo escépticos sobre que la luz estuviera hecha de partículas [@zwiebach-mit-8-04, LN3 §1, p. 2].

**Errores frecuentes.**

- *"El electrón es una bolita que además ondula."* La fuente aclara que un cuanto no es una partícula clásica con posición y velocidad definidas [@zwiebach-mit-8-04, LN1 §3, pp. 5-6]. El comportamiento se describe con una función de onda cuyo módulo al cuadrado da probabilidades ([regla de Born](born-rule-measurement.md)).
- *"Un campo electromagnético clásico es un número fijo de fotones."* No: los campos clásicos corresponden a estados coherentes con número de fotones fluctuante [@zwiebach-mit-8-04, LN3 §3, pp. 6-7].
- *"Cuantizado significa pequeño."* Cuantizado significa discreto: la energía de la luz de un color se aumenta añadiendo fotones, no haciendo más grande el fotón [@zwiebach-mit-8-04, LN1 §3, pp. 5-6].

**Conexión con lo siguiente.** La dualidad prepara el terreno para la descripción matemática: la onda se convierte en un vector de un espacio complejo ([el estado cuántico como vector](state-vector-postulate.md)) y la "partícula" aparece al medir ([medida y regla de Born](born-rule-measurement.md)).

## Profesional {#layer-3}

**Qué hay que quedarse de la historia al programar.** En computación cuántica casi nunca se trabaja con ondas en el espacio: se usan grados de libertad discretos (polarización del fotón, espín, niveles de energía). Zwiebach muestra que la polarización del fotón y el espín del electrón comparten la misma estructura de dos estados [@zwiebach-mit-8-04, LN1 §4, pp. 10-12], y Preskill, que la equivalencia formal con el espín 1/2 vale para cualquier sistema de dos niveles [@preskill-ph219, ch.2 §2.2.1, p. 14]. Lo que sobrevive de la dualidad es el aspecto ondulatorio: sumas de amplitudes con fases que interfieren.

**Criterio práctico: ¿cuándo es relevante lo cuántico?** La regla de la sección anterior (longitud de onda de De Broglie frente a escala del obstáculo) sirve como criterio de orden de magnitud para decidir si un sistema necesita tratamiento cuántico [@zwiebach-mit-8-04, LN3 §3, pp. 6-7]. Para sistemas grandes, la razón por la que no vemos superposiciones macroscópicas la da la [decoherencia](decoherence.md), no una frontera en el tamaño.

**Interferencia con objetos complejos.** La interferencia de moléculas de cientos de átomos [@zwiebach-mit-8-04, LN3 §3, p. 6] y de C₆₀ [@openstax-physics-3, §6.5] indica que la naturaleza ondulatoria no se limita a partículas elementales.

**Fotones como portadores de información.** Cómo se usan los fotones como qubits se trata en el ámbito de hardware ([qubits fotónicos](../../quantum-hardware/concepts/photonic-qubits.md)). Aquí basta el hecho físico de que un fotón no se divide: se absorbe o se transmite entero, porque un fotón fraccionario tendría otra frecuencia [@zwiebach-mit-8-04, LN1 §3, p. 7].

**Lectura recomendada.** Para el recorrido histórico completo con datos numéricos, OpenStax cap. 6 [@openstax-physics-3, §6.1-6.6]; para una presentación matemática más cuidadosa, Zwiebach LN1-LN4 [@zwiebach-mit-8-04, LN1-LN4].
