---
concept: additive-mixing
title: "Mezcla aditiva"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
La **mezcla aditiva (additive mixing)** es lo que ocurre al superponer luces de colores: el resultado es la suma de las luces. Luz roja más luz verde se ve amarilla, y las tres luces primarias juntas se ven blancas [@openstax-college-physics-2e, §26.3].

### Explicación
Un televisor en color aprovecha esta suma: sus puntos de fósforo rojos, verdes y azules, en cantidades iguales, producen toda la gama de matices que vemos [@openstax-college-physics-2e, §26.3]. La idea es antigua, porque Newton ya había mostrado que el blanco se compone de todos los colores del espectro [@newton-1704, Prop. V, Exper. 9-13].

Esta regla es de luces, no de pinturas. Con luces, amarillo y azul superpuestos dan blanco, no verde [@handprint-macevoy, color18a, "Additive Color Mixing"]. La pintura sigue otras reglas, que se ven en [mezcla sustractiva](subtractive-mixing.md).

![Tres luces roja, verde y azul solapadas sobre negro, que dan amarillo, cian, magenta y blanco en el centro, junto a tres filtros cian, magenta y amarillo solapados sobre blanco, que dan azul, verde, rojo y negro en el centro](../../../../../assets/diagrams/additive-vs-subtractive-overlaps.es.svg)

### Ejemplo
Una pantalla de móvil vista de cerca solo tiene puntos rojos, verdes y azules. El amarillo que ves en ella no es luz amarilla, sino rojo y verde encendidos a la vez (la razón está en la [visión tricromática](../../light-and-vision/concepts/trichromacy.md)).

### Para seguir
Ahora que la suma de luces está clara, [mezcla sustractiva](subtractive-mixing.md) explica qué pasa cuando lo que se mezcla son materiales que absorben luz, como la pintura.

## Comprensión {#layer-2}

### Idea clave
La mezcla aditiva se suma en el ojo: el color depende de cuánto estimula la luz a cada uno de los tres tipos de cono, y cualquier color de luz puede igualarse con, como mucho, tres luces [@handprint-macevoy, color18a, "Additive Color Mixing"].

### Explicación
El tono resultante depende del patrón de estimulación de los tres tipos de cono, de modo que luces distintas que estimulan los conos igual dan el mismo color [@openstax-college-physics-2e, §26.3]. Un mismo amarillo puede venir de luz amarilla, de rojo más verde o de luz blanca a la que se ha quitado el violeta [@openstax-college-physics-2e, §26.3]. Por eso la mezcla aditiva describe cómo responde el ojo a luces superpuestas, no una propiedad de las luces solas [@handprint-macevoy, color18a, "Additive Color Mixing"].

Esa igualación es lineal: el color de prueba equivale a una suma ponderada de tres primarios, y los pesos son los valores triestímulo [@webvision, "Colour Matches"]. Las consecuencias para colores que parecen iguales con una luz y distintos con otra se tratan en [metamería](../../light-and-vision/concepts/metamerism.md) y en [color de la luz](../../light-and-vision/concepts/illuminant-color.md).

Los primarios RGB son entonces una convención. Los verdaderos primarios aditivos son las respuestas de los conos L, M y S, que no se pueden ver como luces [@handprint-macevoy, color18a, "The True Additive Primaries Are Invisible"]. Además, el conjunto no es único: amarillo, verde y azul también valdrían [@openstax-college-physics-2e, §26.3].

Para predecir el color de una mezcla de luces, Newton colocaba los colores en un círculo, ponderaba cada uno por la cantidad de rayos y buscaba el centro de gravedad [@newton-1704, Prop. VI]. Es el antecedente geométrico de la [rueda de color](../../color-attributes/concepts/color-wheel.md).

### Ejemplo
Los programas de dibujo basados en RGB mezclan azul y amarillo en un gris, porque los espectros de las luces se suman linealmente, mientras que la pintura real da verde [@sochorova-2021, p. 1, §1]. El modelo aditivo describe el programa, no el tubo.

### Errores frecuentes
- *"La rueda de color predice cualquier mezcla."* Con luces funciona bien, pero con pigmentos es mucho menos precisa [@handprint-macevoy, color14, "mixing with a color wheel"].
- *"Los primarios RGB son los únicos posibles."* Son una convención entre varias [@openstax-college-physics-2e, §26.3].

### Para seguir
La capa siguiente de este concepto muestra dónde choca el razonamiento aditivo con el trabajo real de quien pinta (pantallas, límites de la paleta y promedios de puntos).

## Profesional {#layer-3}

### Idea clave
Usa el razonamiento aditivo para luces, pantallas e iluminación del estudio, y no para predecir una mezcla de pintura [@sochorova-2021, p. 10, Fig. 14; p. 11, §6].

### Explicación
La mezcla aditiva importa a quien pinta en dos sitios. El primero es la pantalla: las referencias digitales, las fotos de las obras y las simulaciones de pintura se calculan de forma aditiva, así que sus mezclas no coinciden con las del lienzo. En RGB las mezclas siguen líneas rectas en el espacio RGB, mientras que la pintura sigue trayectorias curvas [@sochorova-2021, p. 10, Fig. 14; p. 11, §6].

El segundo son los límites de la paleta. Algunos colores de pantalla no pueden mezclarse con ningún pigmento conocido y solo se logran proyectando luz [@sochorova-2021, p. 2, §1]. A la inversa, hay mezclas de pigmentos, como un turquesa muy saturado de azul ftalo con blanco, que una pantalla sRGB no puede mostrar [@sochorova-2021, p. 5, §3.1]. Un pintor que compara su muestra con la pantalla debe saber que la pantalla recorta ese color.

Promediar tampoco es siempre sumar. Para juzgar qué tan distintas parecen dos regiones de puntos de color, la distancia euclídea en el cubo RGB sin corregir predecía mejor que modelos basados en luminancia o en CIEDE2000, pero los promedios no bastan: la estadística de los puntos también cuenta [@koenderink-2018, Results; Discussion, Fig. 22].

### Ejemplo
Un pintor fotografía una muestra de azul ftalo con blanco y la compara en pantalla con la referencia. El turquesa más saturado queda fuera de lo que muestra un monitor sRGB, así que la foto enseña un color recortado y la comparación engaña [@sochorova-2021, p. 5, §3.1].

### Para seguir
[Mezcla óptica](optical-mixing.md) desarrolla qué pasa cuando el promedio de puntos se produce en el ojo del espectador. Para la diferencia entre mezcla aditiva y sustractiva en tecnología del color, la lectura adicional es Berns, cap. 10 §C [@berns-2019].
