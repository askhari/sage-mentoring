---
concept: saturation-and-colorfulness
title: "Saturación, croma y colorido"
---

## Comprensión {#layer-2}

En pintura, en programas de dibujo y en libros de texto se usan "saturación", "croma", "intensidad" y "viveza" como si dijeran lo mismo. En el vocabulario de la CIE son cosas distintas, y conocer la diferencia ayuda a entender de qué se habla en cada fuente. Este concepto parte del [croma](chroma.md) ya visto.

**Tres conceptos de la CIE.** Los tres miden cuán cromático se ve un color, pero con distinto punto de referencia [@cie-e-ilv, 17-22-072, 17-22-073, 17-22-074]:

| Término | Qué es | Referencia |
|---|---|---|
| Colorido (colourfulness) | El atributo por el cual el color percibido de una zona parece más o menos cromático | Ninguna: es absoluto |
| Saturación (saturation) | El colorido de una zona juzgado en proporción a su propio brillo | El brillo de esa misma zona |
| Croma (chroma) | El colorido de una zona juzgado en proporción al brillo de una zona de referencia, iluminada de forma similar, que parece gris, blanca o muy transparente | El brillo de un blanco o gris de referencia |

[@cie-e-ilv, 17-22-072, 17-22-073, 17-22-074]

**Qué cambia con la luz.** La CIE añade una nota a cada definición. El colorido, a una cromaticidad dada, suele aumentar al aumentar la luminancia (salvo con brillos muy altos) [@cie-e-ilv, 17-22-072]. La saturación, con cromaticidad fija y niveles de luz fotópicos, se mantiene casi constante cuando cambia la luminancia [@cie-e-ilv, 17-22-073]; y lo mismo se dice del croma de un color relacionado [@cie-e-ilv, 17-22-074]. Dicho en pintura: si se enciende más luz sobre una pintura, el colorido sube, pero el croma y la saturación casi no cambian. Briggs lo resume diciendo que el colorido y el brillo describen la luz que viene de partes de un objeto, mientras que el croma y la claridad describen el color atribuido al objeto mismo [@briggs-dimensions, 1117.php], y que el colorido equivale formalmente a la saturación por el brillo [@briggs-dimensions, 017.php].

**Qué implica la definición de saturación.** Como la saturación se mide respecto al brillo del propio color, un color muy oscuro y de croma alto puede ser muy saturado, y un color claro con el mismo croma lo será menos. Es una consecuencia lógica de la definición de la CIE, no una afirmación de las fuentes sobre pinturas concretas [@cie-e-ilv, 17-22-073] [unverified]. La guía de Konica Minolta, por su parte, no distingue saturación de croma ni de colorido, y no usa las definiciones de la CIE [@konica-minolta-pcc, Parte I-4, I-6]: es un tratamiento divulgativo y simplificado.

**Cómo hablan otras fuentes.**
- **Munsell (1905)** no hace la distinción moderna: no aparece "saturación" en los pasajes consultados. Usa *chroma*, la fuerza de un color [@munsell-1905, ¶23]. Rechaza "intensidad" porque es un grado y no una cualidad, y "pureza" para los pigmentos [@munsell-1905, Apéndice al cap. I].
- **Newton (1704)** habla de "plenitud o intensidad" (*Fulness or Intenseness*) de un color, que mide con la distancia del punto de la mezcla al centro blanco del círculo [@newton-1704, Libro I, Parte II, Prop. VI, Prob. II].
- **Artistas y programas.** Los artistas suelen decir "saturación" para referirse al croma. En los espacios digitales HSB/HSV la "S" es una saturación relativa, y en HLS funciona, en la práctica, como un croma relativo [@briggs-dimensions, Google Sites, p. 1; 093.php].

**Idea errónea habitual.** "Un color saturado es un color claro y vivo". La saturación y el croma no dicen nada del [matiz](hue.md), y se relacionan con el [valor](value.md) de maneras distintas: el croma se juzga respecto a un blanco de referencia y la saturación, respecto al brillo del propio color.

## Profesional {#layer-3}

**Leer bien una cifra de "saturación".** Cuando una ficha técnica, una app o un tutorial dan un número de saturación, hay que averiguar si es (a) la saturación de la CIE (relativa al propio brillo), (b) el croma (relativo a un blanco de referencia, como en Munsell o en la *C*\* de CIELAB) o (c) la "S" de un modelo de ordenador como HSB. Briggs avisa de que la palabra se usa con poco rigor en los sistemas digitales [@briggs-dimensions, 017.php, 093.php]. Para pintar, lo útil es comparar croma, que es lo que publican los fabricantes en sus tablas [@justpaint-munsell-cielab, tabla Williamsburg] (véase [El sistema Munsell](munsell-system.md) y [CIELAB para pintores](cielab-basics.md)).

**Una serie de sombras.** Briggs señala un caso en el que las dos medidas se separan: en una serie en la que el croma baja al bajar el valor, la saturación puede mantenerse constante; y el pigmento negro apaga una mezcla más rápido de lo que la oscurece [@briggs-dimensions, 101.php] (fuente de fiabilidad C, localización de la segunda afirmación incierta). Lectura práctica: si al oscurecer un color con negro se ve "más apagado", lo que cae es el croma [unverified].

**Qué decir en un taller o en una ficha.** Para comunicar un color, es más fiable dar matiz, valor y croma (en Munsell) o *L*\*, *C*\* y *h* (en CIELAB) que decir "más saturado". Las tablas de Williamsburg y Golden dan los datos en esos términos [@justpaint-munsell-cielab, tabla Williamsburg; listado Golden]. Si un cliente o un compañero pide "más saturación" en una pintura, conviene preguntar si quiere más croma (alejarse del gris), un valor más claro u oscuro, o más luz sobre la obra, porque cada uno se corrige de manera distinta [unverified].
