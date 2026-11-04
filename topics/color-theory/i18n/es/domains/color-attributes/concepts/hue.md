---
concept: hue
title: "Matiz (hue)"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
El **matiz (hue)** es lo que distingue un color de otro (un rojo de un amarillo, de un verde, de un azul o de un morado) sin decir nada de lo claro ni de lo fuerte que es [@munsell-1905, ¶21]. Es una sensación, y los matices forman un anillo cerrado [@cie-e-ilv, 17-22-067].

### Explicación
La definición oficial de la CIE es parecida a la de Munsell: el matiz es el atributo de la percepción por el cual una zona se ve como uno de los colores rojo, amarillo, verde o azul, o como una mezcla de dos de ellos contiguos, dispuestos en un anillo cerrado [@cie-e-ilv, 17-22-067].

De esa definición salen dos ideas. La primera es que el matiz es una **sensación**, no una propiedad física: la luz tiene longitudes de onda, y lo que vemos es un matiz (véase [luz y espectro visible](../../light-and-vision/concepts/light-spectrum.md)).

La segunda es que el matiz **no dice nada de lo claro ni de lo fuerte** que es el color [@munsell-1905, ¶21]. Esas dos cualidades son otras dimensiones, el [valor](value.md) y el [croma](chroma.md).

Como el matiz se cierra sobre sí mismo, se ordena en un círculo, la [rueda de color](color-wheel.md): entre el rojo y el amarillo hay matices intermedios (los naranjas), y entre el azul y el rojo, los morados.

![Círculo de diez matices tipo Munsell, de 5R a 5RP, con el gris neutro en el centro](../../../../../assets/diagrams/hue-circle.es.svg)

### Ejemplo
Un limón maduro, un plátano y una flor de diente de león son "amarillos" aunque uno sea más claro, otro más apagado y otro más vivo. Lo que comparten es el matiz, y lo que los separa son el valor y el croma.

### Errores frecuentes
- *"Un rosa pálido y un granate son colores de familias distintas."* Son el mismo matiz (rojo) con valores muy distintos; el lenguaje corriente los separa por el valor [@cleland-1921, p. ~15].

### Para seguir
El [valor](value.md) explica lo claro u oscuro que es un color con el mismo matiz. La capa 2 de este concepto precisa qué matices son "únicos" y por qué el anillo se cierra.

## Comprensión {#layer-2}

### Idea clave
Hay cuatro matices "únicos" (rojo, verde, amarillo y azul) en dos pares opuestos, y el resto se describe como mezcla de vecinos [@cie-e-ilv, 17-22-068]. El anillo de matices no coincide con el espectro: se cierra con los morados y magentas [@newton-1704, Libro I, Parte II, Prop. VI, Prob. II].

### Explicación
La CIE llama *matiz único (unique hue)* a un matiz que no se puede describir con nombres de otros matices. Son cuatro y forman dos pares opuestos, rojo-verde y amarillo-azul [@cie-e-ilv, 17-22-068]. Esa estructura de pares opuestos enlaza con los [procesos oponentes](../../light-and-vision/concepts/opponent-process.md) del sistema visual. El naranja o el morado, en cambio, se describen como mezclas de los matices vecinos.

El anillo se cierra porque incluye los morados y magentas, que no son luz de una sola longitud de onda, mientras que el espectro es una recta con un extremo rojo y otro violeta. Newton ya lo notó: si la mezcla cae cerca del segmento que une los extremos rojo y violeta, el resultado no es un color prismático sino un púrpura [@newton-1704, Libro I, Parte II, Prop. VI, Prob. II].

Además, el matiz que se percibe no es una propiedad fija del estímulo. La CIE define el *color percibido (perceived colour)* como lo que se describe con matiz, claridad (o brillo) y colorido (o saturación o croma), y precisa que depende del espectro, del tamaño, la forma, la estructura y el entorno del estímulo y de la adaptación y la experiencia del observador [@cie-e-ilv, 17-22-040]. Por eso el matiz puede cambiar con la luz o con lo que rodea al color (véase [el color de la luz](../../light-and-vision/concepts/illuminant-color.md)).

Los nombres de matiz, por último, son culturales y vagos. Cleland evitaba en su libro "naranja", "rosa" y "violeta" y usaba nombres como "amarillo-rojo", porque los nombres corrientes (ciruela, oliva, ratón) no son precisos [@cleland-1921, pp. ~13, 17-18]. Munsell glosaba amarillo-rojo como "lo que se llama popularmente naranja" y rojo-morado como "ciruela" [@munsell-1905, ¶58].

### Ejemplo
Munsell sostenía que un color solo queda definido si se dan matiz, valor y croma; si falta una cualidad, el color queda sin definir [@munsell-1905, ¶8, ¶20]. Criticaba las frases que mezclan dimensiones, y esos casos sirven para practicar la separación:

- Un autor escribía que un amarillo "pasa" (*shades*) al verde: eso es un cambio de **matiz**.
- El mismo autor hablaba de "un tono más brillante" cuando quería decir un **croma** más fuerte [@munsell-1905, Apéndice al cap. I].

### Errores frecuentes
- *"El matiz es la longitud de onda."* Una longitud de onda da un matiz espectral, pero no todos los matices son espectrales: los morados y magentas no lo son [@newton-1704, Libro I, Parte II, Prop. VI, Prob. II].

### Las fuentes discrepan
Munsell, en 1905, vinculaba el matiz a la longitud de onda y daba como ejemplo que una longitud de onda produce la sensación de verde y otra la de rojo [@munsell-1905, ¶21]. Esa equivalencia es válida solo para los matices espectrales; la CIE trata el matiz como sensación y lo define sin referirse a longitudes de onda [@cie-e-ilv, 17-22-067].

### Para seguir
La capa 3 pasa a cómo se mide el matiz con instrumentos y cómo se lee en las fichas de pintura. Antes, el [croma](chroma.md) completa las tres dimensiones.

## Profesional {#layer-3}

### Idea clave
En instrumentos y fichas de fabricante el matiz es un ángulo o una notación (CIELAB, Munsell); con croma casi cero pierde sentido, y el nombre comercial de una pintura no garantiza su matiz [@cie-e-ilv, 17-23-076; @justpaint-munsell-cielab, listado Golden].

### Explicación
Los instrumentos expresan el matiz como un ángulo. En CIELAB es el ángulo de matiz *h*<sub>ab</sub> = arctan(*b*\*/*a*\*) [@cie-e-ilv, 17-23-076]; en la guía de Konica Minolta se mide desde el eje +*a*\*: 0° es rojo, 90° amarillo, 180° verde y 270° azul [@konica-minolta-pcc, Parte I-8].

En Munsell, el matiz es la parte de la notación formada por una letra que indica la posición en el círculo [@munsell-1905, ¶40]; ediciones posteriores le anteponen un número, como en 7R [@cleland-1921, p. ~14]. Véase [el sistema Munsell](munsell-system.md) y [CIELAB](cielab-basics.md).

Las fichas de los fabricantes dan el matiz con una de esas dos notaciones; por ejemplo, el azul ultramar de Williamsburg figura con matiz 9,01 PB, y el amarillo de cadmio limón, con 9,06 Y [@justpaint-munsell-cielab, tabla Williamsburg].

Cuando el croma es casi cero, el matiz es irrelevante: el listado de Golden indica "Black" o "White" en lugar de un matiz para las pinturas acromáticas [@justpaint-munsell-cielab, listado Golden].

### Ejemplo
Para acercarse a un color objetivo, Briggs describe un método que compara el matiz con los vecinos del círculo [@briggs-dimensions, 109.php]:

1. Elegir dos pinturas a ambos lados del objetivo en el círculo de matices.
2. Llevar cada una al valor del objetivo.
3. Mezclarlas.
4. Si hace falta, bajar el croma.

El orden es razonable: acertar primero el matiz con el valor ya ajustado y dejar el croma para el final.

### Errores frecuentes
- *"Dos pinturas con el mismo nombre comercial tienen el mismo matiz."* El amarillo de cadmio medio "genuino" de Golden está en 3,0 Y y el "Hue" (imitación) en 1,5 Y [@justpaint-munsell-cielab, listado Golden].
- *"La lectura de matiz es una propiedad de la pintura y nada más."* Depende también de cómo se aplicó (espesor de la película, secado), según un resumen de la metodología de esas tablas [unverified].

### Las fuentes discrepan
Las dos tablas de fabricante tratan de forma distinta las pinturas acromáticas. Golden no da matiz para ellas, mientras que Williamsburg lo da incluso para el blanco de titanio (2,7 GY con croma 0,24) y el negro de marfil (5,16 PB con croma 0,08) [@justpaint-munsell-cielab, listado Golden; tabla Williamsburg]. Esos matices no deben leerse como reales, porque el croma es casi nulo. El método de mezcla del ejemplo procede de una guía de taller de fiabilidad C, así que vale como práctica ilustrativa [@briggs-dimensions, 109.php].

### Para seguir
El [valor](value.md) en su capa 3 muestra, con los mismos datos de fabricante, cuánto varía la claridad entre pinturas del mismo matiz.
