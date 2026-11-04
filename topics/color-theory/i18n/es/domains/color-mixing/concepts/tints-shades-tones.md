---
concept: tints-shades-tones
title: "Aclarar, oscurecer y agrisar (tints, shades, tones)"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
En el uso corriente, un **tinte (tint)** es un color mezclado con blanco, una **sombra (shade)** es un color mezclado con negro y un **tono (tone)** es un color mezclado con gris [unverified]. Cambian el [valor](../../color-attributes/concepts/value.md) y el [croma](../../color-attributes/concepts/chroma.md) del color de partida.

### Explicación
Esta clasificación popular se apoya en tres cantidades: la blancura, la negrura y la cromaticidad [@briggs-dimensions, Google Sites, p. 1]. El tinte se entiende como un intermedio entre el blanco y el color puro [@briggs-dimensions, 1117.php]. Briggs es aquí una fuente de fiabilidad baja.

De las tres dimensiones del color se mueven dos: el valor (lo claro u oscuro) y el croma (lo vivo o apagado). El efecto práctico es distinto según lo que se añada. El blanco da pasteles y nunca da los colores oscuros y apagados como el marrón o el ocre. El negro baja a la vez la claridad y el croma y es el camino hacia esos colores apagados [@handprint-macevoy, color12, "Unsaturated color zones"].

![Un azul mezclado en siete pasos con blanco, con gris y con negro, y una gráfica de claridad frente a croma con el camino de cada escalera](../../../../../assets/diagrams/tint-ladder.es.svg)

### Ejemplo
Rojo más blanco da rosa (un tinte). Rojo más una pizca de negro da granate (una sombra). Rojo más gris da un rojo apagado, "empolvado" (un tono).

### Errores frecuentes
- *"Tinte, sombra y tono son términos precisos."* Son cómodos en el taller, pero imprecisos para medir. "Shade" debería significar solo un valor oscurecido, y para hablar de lo claro u oscuro el término adecuado es "valor" [@munsell-1905, ¶22, Apéndice I].
- *"Tone y key sirven para hablar del color."* Vienen de la música y enturbian el lenguaje del color [@munsell-1905, ¶4-6].

### Las fuentes discrepan
Los términos populares son cómodos pero imprecisos. Munsell quería sustituir tint, tone, shade, purity e intensity por los términos medidos matiz, valor y croma [@munsell-1905, Apéndice I].

### Para seguir
La capa 2 de este concepto muestra que añadir blanco no es simplemente "mover hacia arriba" en pintura real. Antes, [colores complementarios](complementary-colors.md) enseña la tercera forma de bajar el croma.

## Comprensión {#layer-2}

### Idea clave
En pintura real, añadir blanco no solo sube el valor: el croma puede subir un poco al principio y el matiz se desplaza, como en el azul ftalo, que pasa de púrpura a turquesa [@sochorova-2021, p. 1, §1; p. 3, Fig. 4].

### Explicación
En un programa RGB, un color mezclado con blanco pierde saturación de forma directa. El modelo de Kubelka-Munk reproduce en cambio la ganancia de croma y el desplazamiento de matiz para el magenta de quinacridona y el azul ftalo, mientras que los degradados RGB hacia el blanco se ven grises y apagados [@sochorova-2021, p. 3, Fig. 4; p. 8, Fig. 11; p. 9, §4]. Este comportamiento es una propiedad del pigmento, que "revela su naturaleza", y no solo del blanco [@sochorova-2021, p. 1, §1].

El matiz tampoco se queda quieto. El blanco desplaza los naranjas y los amarillos profundos hacia el amarillo y los rojos hacia el violeta; el negro o el gris pueden desplazarlos de otro modo [@handprint-macevoy, color12].

Los blancos y negros de tubo no son ideales. El blanco de titanio mide valor 10 / croma 1,1 y el negro de carbón valor 1 / croma 0,3 en las tablas de acrílicas, así que el negro de tubo no es valor 0 [@justpaint-munsell-cielab, listado Golden]. Los negros de carbón son en realidad grises oscuros con una reflectancia de unos 20 [@handprint-macevoy, color11 y color13].

En las sombras el croma cae: "los colores pierden saturación en las sombras" [@handprint-macevoy, color11, "Hue, lightness and saturation"]. Para sombras se sugiere añadir un neutro oscuro casi neutro, como un tinte neutro o negro marfil o de humo [@handprint-macevoy, color11, "Hue, lightness and saturation"]. Diluir también cuenta, porque la dilución apaga las mezclas saturadas [@handprint-macevoy, color13, "Tints and Shades"].

Las escalas de grises se pueden hacer mezclando negro y blanco, pero el error de mezcla limita a un pintor a unos once valores utilizables [@handprint-macevoy, color11, "Painting values"].

### Ejemplo
Una escalera de azul ftalo con blanco no sube en línea recta hacia el pastel: el color pasa de púrpura a turquesa y gana croma al principio [@sochorova-2021, p. 3, Fig. 4].

### Errores frecuentes
- *"Añadir blanco solo aclara."* También desplaza el matiz y, al principio, puede subir el croma [@sochorova-2021, p. 3, Fig. 4].
- *"El negro de tubo es valor 0."* Mide valor 1 [@justpaint-munsell-cielab, listado Golden].

### Las fuentes discrepan
Briggs observa que el negro apaga una mezcla más rápido de lo que baja su claridad, pero la localización de esa afirmación es dudosa [@briggs-dimensions, 101.php].

### Para seguir
La capa 3 convierte esto en una herramienta de taller, la escalera de tinte, y en un criterio para elegir qué añadir.

## Profesional {#layer-3}

### Idea clave
Haz tu propia escalera de cada pigmento con tu blanco: muestra su "naturaleza" y es la práctica habitual para construir una base de datos de colorantes [@sochorova-2021, p. 1, §1; @zhao-berns-2006, resumen].

### Explicación
En el trabajo profesional se hace una escalera de cada pigmento con blanco en concentraciones crecientes, y se ajusta por mínimos cuadrados un coeficiente de absorción y otro de dispersión por colorante [@zhao-berns-2006, resumen]. Para artistas de acrílico y óleo bastan dos muestras (la pintura pura y una mezcla con blanco, con mejor resultado hacia un 40-60 % de pigmento) en vez de la escalera completa [@zhao-berns-2006, resumen].

Para elegir qué añadir, el criterio es este: el blanco sube el valor y lleva a los pasteles; para ir a marrones, ocres y verdes dorados hay que pasar por el negro, un gris o un complementario, no por el blanco [@handprint-macevoy, color12]. Los pigmentos oscuros y de croma alto son los que más cambian en la escalera: el azul ultramar al óleo mide en masa valor 0,32 y croma 18,16 [@justpaint-munsell-cielab, tabla Williamsburg]. Cuánto sube el valor y qué croma queda con cada proporción de blanco hay que medirlo en la propia muestra, porque no se deduce del color del tubo [unverified].

Una foto de la muestra puede engañar: el turquesa más saturado del azul ftalo con blanco queda fuera de lo que muestra un monitor sRGB habitual [@sochorova-2021, p. 5, §3.1].

### Ejemplo
Para decidir qué dimensión cambiar:
1. Solo valor: agua o blanco.
2. Valor y croma a la vez: negro.
3. Croma sin tocar el valor: un complementario o un neutro del mismo valor (véase [complementarios](complementary-colors.md)).
4. Para un color objetivo, se hace en pasos y se mide contra una muestra seca (véase [mezclar un color objetivo](target-color-mixing.md)).

### Para seguir
La fuerza tintórea de cada pigmento, que determina cuánto blanco hace falta, se trata en el ámbito de pinturas y pigmentos. Dentro de este, [mezclar un color objetivo](target-color-mixing.md) reúne todo el procedimiento.
