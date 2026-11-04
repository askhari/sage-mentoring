---
concept: color-wheel
title: "La rueda de color"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
La **rueda de color (color wheel)** ordena los [matices](hue.md) en un círculo cerrado, de modo que se pasa del rojo al amarillo, al verde, al azul, al morado y de nuevo al rojo sin saltos [@cleland-1921, pp. ~13-14]. Los vecinos dan matices intermedios y los opuestos se neutralizan en gris [@munsell-1905, ¶56, ¶61].

### Explicación
La guía de Konica Minolta describe la rueda como la disposición en círculo de la sucesión continua de matices [@konica-minolta-pcc, Parte I-4]. Es el modo natural de representar el matiz, porque la CIE define el matiz como un anillo cerrado: los matices intermedios aparecen como mezclas de dos vecinos [@cie-e-ilv, 17-22-067].

Munsell propone leerla así: cinco matices principales (rojo, amarillo, verde, azul y morado) repartidos a distancias iguales, y entre cada pareja un matiz intermedio (amarillo-rojo, verde-amarillo, azul-verde, morado-azul y rojo-morado), con lo que quedan diez posiciones [@munsell-1905, ¶56-58]. Dos ideas se leen directamente en el dibujo:

- **Vecinos:** dos matices contiguos, al mezclarse, dan un matiz intermedio que conserva algo de ambos [@munsell-1905, ¶56].
- **Opuestos:** una línea que va de un matiz por el centro hasta el lado contrario encuentra su opuesto. Al mezclar dos opuestos se obtiene un gris, y el centro de la rueda es un gris medio [@munsell-1905, ¶61]. En el círculo de Munsell, el opuesto del rojo es el azul verdoso (*blue-green*) [@munsell-1905, ¶61].

![Círculo de diez matices tipo Munsell con líneas que unen cada matiz con su opuesto a través del gris central](../../../../../assets/diagrams/hue-circle.es.svg)

### Ejemplo
El arcoíris muestra los matices en fila, de rojo a violeta. La rueda cierra esa fila con los morados y magentas, que no están en el arcoíris, y así queda un círculo en el que cada color tiene dos vecinos.

### Para seguir
La capa 2 explica por qué una rueda es un mapa y no una ley, y qué deja fuera. Para las otras dos dimensiones, véanse el [valor](value.md) y el [croma](chroma.md).

## Comprensión {#layer-2}

### Idea clave
Una rueda es un mapa, no una ley: todas representan el matiz como ángulo, pero cambian la colocación de los matices y los opuestos. Su idea de fondo viene del círculo de Newton: el ángulo marca el matiz y el radio, la distancia al blanco o gris central [@newton-1704, Libro I, Parte II, Prop. VI, Prob. II].

### Explicación
Hay muchas ruedas porque se ordenan con criterios distintos (véase [por qué hay varias ruedas](color-wheel-models.md)). En la rueda de Munsell, la distancia entre matices es la misma entre pasos, y las parejas opuestas se eligieron porque, al hacerlas girar en un disco de Maxwell, se mezclaban en un gris neutro [@munsell-1905, ¶105-116; @briggs-dimensions, 112.php].

El precedente es el círculo de Newton, con los siete colores del prisma en la circunferencia y el blanco en el centro. Para saber qué color da una mezcla de luces se calcula el centro de gravedad de las cantidades de cada color: la dirección desde el centro hacia ese punto indica el matiz y la distancia al centro indica la "plenitud o intensidad" del color, es decir, cuánto se aleja del blanco [@newton-1704, Libro I, Parte II, Prop. VI, Prob. II]. Una mezcla a mitad de camino entre el borde y el centro equivale al amarillo más intenso diluido con una cantidad igual de blancura [@newton-1704, Libro I, Parte II, Prop. VI, Prob. II]. Esa es la idea de las ruedas actuales (véase [croma](chroma.md)).

Una rueda plana, sin embargo, omite el valor y, en la mayoría de los dibujos, también el croma. Munsell comparaba los diagramas planos que omiten el croma con un mapa de Suiza sin montañas [@munsell-1905, ¶14]. La rueda de matices corresponde a una sola rebanada horizontal a un valor dado, el "ecuador" del sólido de color [@munsell-1905, ¶31].

### Ejemplo
El círculo de Newton sirve para mezclar luces, no polvos de pintor. Los polvos de colores, al mezclarse, absorben buena parte de la luz y dan un resultado sucio, gris o pardo [@newton-1704, Libro I, Parte II, Prop. V, Exper. 15].

### Errores frecuentes
- *"La rueda predice la mezcla de dos pinturas."* Su origen está en la mezcla de luces, como se vio en el ejemplo [@newton-1704, Libro I, Parte II, Prop. VI].
- *"La rueda describe todo el color."* Solo representa el matiz, una rebanada del sólido [@munsell-1905, ¶31].

### Para seguir
[Por qué hay varias ruedas](color-wheel-models.md) compara las ruedas más usadas y qué pregunta responde cada una. La capa 3 trata cuántos matices distinguir y cuándo no basta una rueda.

## Profesional {#layer-3}

### Idea clave
El número de divisiones de una rueda depende de la finalidad, y los opuestos solo dan gris si están equilibrados en valor y croma; para comunicar un color hace falta pasar del ángulo a una notación numérica [@munsell-1905, ¶59-60, ¶72-77].

### Explicación
Munsell consideraba suficientes diez pasos para la enseñanza elemental [@munsell-1905, ¶59-60]. En la versión de Cleland de 1921 cada uno de esos diez pasos principales se subdivide en diez (numerados de 1 a 10), que se considera aproximadamente la menor diferencia que distingue un ojo entrenado; el 5 marca el matiz "simple" y el 10, el compuesto [@cleland-1921, p. ~14]. De ahí salen los 100 matices de una rueda Munsell completa; esa cifra es un cálculo (10 × 10) y no una afirmación de la fuente.

Un par opuesto solo da gris si está equilibrado. Munsell avisa de que dos opuestos solo se neutralizan si tienen el mismo valor y un croma equilibrado, y que, si no, queda un tinte que indica cuál de los dos sobra [@munsell-1905, ¶72-77, ¶105-116]. Si una mezcla de opuestos no llega a gris, la rueda no está "fallando": lo que falla es la igualdad de valor y croma entre las dos pinturas.

Cuando hay que trasladar un color a números (para pedir pintura, comparar lotes o comunicar un color a otra persona), la rueda deja de servir y hace falta una notación como [Munsell](munsell-system.md) o [CIELAB](cielab-basics.md), donde el ángulo de matiz de la rueda pasa a ser un número en una escala.

### Ejemplo
Para acercarse a un color objetivo con la rueda, Briggs describe este método [@briggs-dimensions, 109.php]:

1. Elegir dos pinturas que estén a ambos lados del objetivo en el círculo de matices.
2. Igualar el valor de ambas.
3. Mezclar.

Para encontrar el complementario de una pintura, el más directo de la mayoría está aproximadamente en el lado opuesto del círculo Munsell [@briggs-dimensions, 063.php]. Si la mezcla con ese opuesto no llega a gris, se revisa primero la igualdad de valor y croma.

### Las fuentes discrepan
Cerca del eje que va del amarillo al azul violáceo, el camino de la mezcla de pinturas se curva a través de verdes de croma medio, y el opuesto del círculo deja de ser el complementario [@briggs-dimensions, 063.php]. Briggs es una fuente de fiabilidad C, de modo que sus indicaciones sirven de pista de trabajo y no de regla.

### Para seguir
[El sistema Munsell](munsell-system.md) convierte el círculo de matices, el valor y el croma en una notación medida; su capa 3 la usa con datos de pinturas reales.
