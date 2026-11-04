---
concept: pigment-mixing-behavior
title: "Cómo se mezclan de verdad los pigmentos (Kubelka-Munk)"
format: 2
---

## Comprensión {#layer-2}

### Idea clave
En una pintura, las partículas de pigmento absorben y dispersan la luz de forma compleja, y el resultado de mezclar es muy poco lineal [@sochorova-2021, p. 1, §1]. El modelo de Kubelka-Munk describe esa doble acción con dos constantes: absorción y dispersión.

### Explicación
Azul y amarillo dan verde porque ambas clases de partículas absorben y dispersan la luz repetidas veces dentro de la pintura, dejando salir sobre todo longitudes de onda verdes [@sochorova-2021, p. 2, §2, Fig. 3]. Esto continúa lo que se vio en [mezcla sustractiva](subtractive-mixing.md): ahí la absorción es la parte conocida; aquí entra la dispersión.

El modelo de Kubelka-Munk describe una capa plana y mate de pintura con dos flujos de luz, uno hacia abajo y otro hacia arriba. Cada rebanada fina quita una fracción fija de luz por absorción (constante *s*) y otra por dispersión (constante *r*; los textos posteriores escriben *K* para la absorción y *S* para la dispersión). La luz dispersada pasa al flujo contrario, y la absorbida no vuelve [@kubelka-munk-1931, pp. 1-2, §1]. Para una capa gruesa, el aspecto de una pintura acromática depende solo de la razón entre absorción y dispersión, *s/r*, no de los valores absolutos [@kubelka-munk-1931, p. 3, §2]. Además, *r* y el espesor *X* solo aparecen como producto *rX*, lo que coincide con que una pintura se puede aclarar con un aglutinante transparente sin cambiar el albedo de la capa si se aplica sobre la misma superficie [@kubelka-munk-1931, p. 5, §3].

Para predecir una mezcla hace falta una regla que el artículo de 1931 no trata. Ese artículo solo menciona el negro de humo en blanco, donde *s/r* crece en proporción a la cantidad de negro [@kubelka-munk-1931, p. 3, §2]. La regla de mezcla es posterior: en el modelo usado en gráficos, los coeficientes de absorción *K(λ)* y dispersión *S(λ)* de cada pigmento se miden de antemano, y los de la mezcla son la suma ponderada por concentración de los de cada pigmento (regla atribuida a Duncan, 1940) [@sochorova-2021, p. 2, §2, Eq. 1]. La reflectancia se calcula después con la ecuación de Kubelka-Munk para una capa lo bastante gruesa como para ocultar el fondo [@sochorova-2021, p. 3, Eq. 2].

Lo importante es que el promedio lineal se hace en *K* y *S*, no en la reflectancia ni en el RGB, así que el color de la mezcla no es el promedio de los colores [@sochorova-2021, p. 3, §2]. Este modelo coincide con mezclas reales de azul cobalto y amarillo Hansa, mientras que RGB, RYB, el sustractivo y el híbrido no [@sochorova-2021, p. 3, Fig. 5; p. 4, Fig. 6]. También reproduce la ganancia de saturación y el cambio de matiz de los [tintes](tints-shades-tones.md) [@sochorova-2021, p. 3, Fig. 4].

Una consecuencia visible son las líneas de mezcla curvas. Las luces mezcladas caen sobre líneas rectas de un diagrama de cromaticidad, pero las líneas de mezcla de la pintura son "erráticas" y suelen curvarse en una rueda [@handprint-macevoy, color14, "Mixing Lines"]. En el modelo, los colores mezclados se curvan lejos del gris y conservan saturación, y aparecen matices secundarios; en RGB la trayectoria es una recta [@sochorova-2021, p. 10, Fig. 14; p. 11, §6].

![Mezclas de azul y amarillo: en pintura pasan por verdes; en mezcla óptica pasan por grises amarillentos; puntos de los dos colores cada vez más pequeños y trayectorias en el plano a*b*](../../../../../assets/diagrams/blue-yellow-mixing.es.svg)

### Ejemplo
Con azul cobalto y amarillo Hansa, el modelo de Kubelka-Munk reproduce el verde que sale de la pintura real. RGB, RYB, el modelo sustractivo puro y el híbrido no lo logran [@sochorova-2021, p. 3, Fig. 5; p. 4, Fig. 6].

### Errores frecuentes
- *"Si dos pinturas se ven iguales, mezclarán igual."* Pueden tener curvas de reflectancia distintas y mezclar de otra forma [@handprint-macevoy, color18a, "Substance Uncertainty"]. Incluso dos amarillos de reflectancia casi idéntica pueden mezclar distinto por su índice de refracción [@handprint-macevoy, color18a, "Particle size, refractive index and hiding power"].
- *"Mezclar es promediar colores."* El promedio se hace en las constantes de absorción y dispersión, no en los colores [@sochorova-2021, p. 3, §2].
- *"Las mezclas son estables."* La reflectancia cambia al secar y con el espesor [@handprint-macevoy, color18a, "Substance Uncertainty"].

### Para seguir
[Mezcla óptica](optical-mixing.md) estudia el caso contrario, en el que los colores no se mezclan en la pintura. La capa 3 de este concepto cubre los datos, los límites del modelo y la práctica de taller.

## Profesional {#layer-3}

### Idea clave
Los profesionales miden coeficientes de absorción y dispersión por colorante, pero en el taller no calculan: hacen muestras secas con sus propios tubos, porque el aspecto del tubo no predice la mezcla [@handprint-macevoy, color13 y tech17].

### Explicación
El modelo de dos constantes caracteriza cada colorante con un coeficiente unitario de absorción y otro de dispersión, ajustados por mínimos cuadrados con todas las muestras de una escalera de tintes, razón por la que el blanco forma parte de la caracterización. Bastan dos muestras por colorante (la pintura pura, o tono en masa (masstone), y una mezcla con blanco) en pinturas acrílicas y al óleo de artista [@zhao-berns-2006, resumen]. Los coeficientes de los acrílicos que usan Sochorova y colaboradores proceden de la base de datos espectral de pinturas de artista de Berns (2016), medidos en 36 longitudes de onda de 380 a 750 nm [@sochorova-2021, p. 7, §3.2].

Mezclar tiene un coste. Mezclar pinturas muy separadas en la rueda cuesta saturación. Las líneas de mezcla de primarios sustractivos se curvan hacia fuera (menos pérdida de croma de la esperada), mientras que las de primarios de tipo aditivo (naranja, verde, violeta) se curvan hacia dentro, con mayores pérdidas de croma y de claridad [@handprint-macevoy, color13 y color14; color18b, "The Relative Effects of Color Mixtures"]. Es una observación de taller sobre acuarelas, no una regla universal.

El modelo tiene límites que importan al pintar:
1. Supone una capa gruesa que oculta el fondo y trata la mezcla homogénea de pintura opaca. Las capas translúcidas, como las veladuras de acuarela, quedan para trabajo futuro [@sochorova-2021, p. 3, Eq. 2; p. 10, §5].
2. Los coeficientes proceden de acrílicos brillantes. El brillo enriquece los colores, por lo que el método puede sobrestimar la saturación en un medio más mate, como la acuarela seca [@sochorova-2021, p. 8, §3.3].
3. Para uso en software, necesita muchos más canales que tres y costosas integrales espectrales por píxel [@sochorova-2021, p. 2, §1].
4. Su teoría trata sobre todo capas mates y sin color; las capas coloreadas solo se rozan [@kubelka-munk-1931, p. 1, Introducción; p. 14, §9].

### Ejemplo
En el taller se hace una muestra seca con los tubos propios y se espera al menos diez minutos antes de juzgarla, porque las mezclas cambian al secar [@handprint-macevoy, color13 y tech17].

### Las fuentes discrepan
Briggs, fuente de fiabilidad baja, indica que en las mezclas de complementarios el camino se curva por verdes de croma medio cerca del eje amarillo-azul violáceo [@briggs-dimensions, 063.php]. Las observaciones de Macevoy sobre curvatura son de acuarela y las de Sochorova y colaboradores, de acrílico brillante, así que no son directamente comparables [@handprint-macevoy, color13 y color14; @sochorova-2021, p. 8, §3.3].

### Para seguir
El libro de Berns tiene un capítulo sobre materiales de pintura, de lectura adicional [@berns-2016]. Para llevar esto a una mezcla concreta, véase [mezclar un color objetivo](target-color-mixing.md).
