---
concept: value
title: "Valor / claridad (value, lightness)"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
El **valor (value)** es lo claro u oscuro que es un color, con independencia de su matiz y de su croma [@munsell-1905, ¶21-22]. Se mide en una escala de diez pasos, de negro (0) a blanco (10) [@cleland-1921, pp. ~14-15].

### Explicación
El valor es la dimensión que se ve en una fotografía en blanco y negro: aunque se quite el color, siguen distinguiéndose las zonas claras de las oscuras. En la guía de Konica Minolta se dice lo mismo con otras palabras: la claridad es lo luminoso u oscuro que es un color y se puede juzgar con independencia del matiz [@konica-minolta-pcc, Parte I-4].

Munsell lo midió con una escala vertical de diez pasos, de negro (0) a blanco (10), con nueve grises entre ambos, y el valor medio es 5 [@cleland-1921, pp. ~14-15; @munsell-1905, ¶31]. Los pasos se fijaron con un fotómetro [@cleland-1921, p. ~15].

Conviene separar dos palabras que se usan mal: "tinte" (*tint*) y "sombra/oscurecido" (*shade*). Munsell propone reservar *tint* para un valor claro y *shade* para uno más oscuro, y prefiere la palabra *valor* para hablar de la luz que refleja un color [@munsell-1905, ¶22 y Apéndice al cap. I].

### Ejemplo
Un limón amarillo es más claro que un pomelo amarillo y que una cereza roja [@konica-minolta-pcc, Parte I-4]. Un granate y un rosa son el mismo matiz (rojo) con valores muy distintos: el valor es lo que hace que el lenguaje corriente hable de "granate" y de "rosa" como si fueran colores diferentes [@cleland-1921, p. ~15].

### Para seguir
El [croma](chroma.md) es la tercera dimensión: lo fuerte o apagado que es un color una vez fijados matiz y valor. La capa 2 de este concepto distingue brillo y claridad y explica por qué el valor depende del contexto.

## Comprensión {#layer-2}

### Idea clave
Lo que en pintura se llama valor corresponde a la **claridad (lightness)** de la CIE, no al brillo: se juzga respecto a un blanco iluminado igual, y por eso depende del entorno [@cie-e-ilv, 17-22-059, 17-22-063].

### Explicación
La CIE distingue dos conceptos. El *brillo (brightness)* es el atributo por el cual una zona parece emitir, transmitir o reflejar más o menos luz, y no se limita a las fuentes de luz [@cie-e-ilv, 17-22-059]. La *claridad (lightness)* es el brillo de una zona juzgado en relación con una zona blanca (o muy transparente) iluminada de forma parecida; solo los colores "relacionados", vistos en un contexto, tienen claridad [@cie-e-ilv, 17-22-063]. Briggs resume la diferencia así: las luces son "brillantes" o "tenues" (*dim*), las superficies son "claras" u "oscuras" [@briggs-dimensions, 016.php].

Como la claridad se juzga respecto a un blanco iluminado de la misma manera, un papel gris a la sombra y un blanco al sol pueden devolver al ojo la misma luz y, sin embargo, verse muy distintos. El valor, por tanto, es una propiedad del objeto percibido en su entorno, no un número que se lea en la luz que llega al ojo (véase [por qué los objetos tienen color](../../light-and-vision/concepts/light-matter-interaction.md)).

La relación entre valor y [matiz](hue.md) también importa, porque los colores puros no tienen el mismo valor. En el espectro, las longitudes de onda de los extremos rojo y morado se ven oscuras y el amarillo verdoso se ve casi blanco [@munsell-1905, ¶94].

Para medir la claridad en un instrumento se usa *L*\* de CIELAB, que la aproxima [@cie-e-ilv, 17-23-076]; la guía de Konica Minolta lo describe como el eje de claridad [@konica-minolta-pcc, Parte I-7].

### Ejemplo
Newton ilustró la dependencia del contexto con un polvo grisáceo que, puesto al sol, se veía más blanco que un papel blanco a la sombra [@newton-1704, Libro I, Parte II, Prop. V, Exper. 15]. Los dos devolvían al ojo una luz comparable, pero el ojo juzga cada uno respecto al blanco de su propia iluminación.

### Errores frecuentes
- *"Los colores vivos son claros."* El valor y el [croma](chroma.md) son independientes: un color puede ser a la vez muy oscuro y muy intenso (la capa 3 da casos medidos).
- *"El valor es el brillo."* La CIE no tiene una entrada "valor"; sus equivalentes son el brillo y la claridad, y en pintura corresponde a la claridad [@cie-e-ilv, 17-22-059, 17-22-063].

### Las fuentes discrepan
Munsell criticaba los esquemas de Runge y Chevreul, que ponían rojo, amarillo y azul equidistantes en el mismo nivel de claridad, cuando el amarillo es mucho más claro y el azul mucho más oscuro [@munsell-1905, Apéndice al cap. V].

### Para seguir
La capa 3 usa tablas de pinturas reales para ver cuánto valor tienen los pigmentos y cómo estimar el valor al pintar. Para el croma, véase [croma](chroma.md).

## Profesional {#layer-3}

### Idea clave
El nombre de un pigmento dice poco sobre su valor: en las tablas de fabricante, el azul ultramar sale del tubo más oscuro que un negro, y los negros y blancos de tubo no son 0 ni 10 [@justpaint-munsell-cielab, tabla Williamsburg].

### Explicación
Los datos de Williamsburg (óleo, película de 6 mil) lo muestran con claridad [@justpaint-munsell-cielab, tabla Williamsburg]:

| Pintura | Matiz | Valor Munsell | *L*\* |
|---|---|---|---|
| Azul ultramar | 9,01 PB | 0,32 | 4,78 |
| Azul cobalto | 6,42 PB | 2,25 | 26,58 |
| Rojo de cadmio claro | 9,29 R | 5,13 | 51,19 |
| Amarillo de cadmio medio | 2,73 Y | 8,45 | 83,08 |
| Blanco de titanio | 2,7 GY | 9,73 | 98,24 |

El azul ultramar es más oscuro que el negro de marfil (valor 1,03 y *L*\* 10,83) y, a la vez, tiene un croma muy alto (18,16; véase [croma](chroma.md)); el amarillo de cadmio, en cambio, es claro: su valor en masa (*masstone*, la pintura sin mezclar) es de 8 a 9 [@justpaint-munsell-cielab, tabla Williamsburg]. En esa tabla, además, valor y *L*\* van juntos: aproximadamente *L*\* ≈ 10 × valor (por ejemplo 0,32 ↔ 4,78 y 9,73 ↔ 98,24) [@justpaint-munsell-cielab, tabla Williamsburg; cálculo sobre las filas de la tabla].

Los negros y blancos de tubo tampoco llegan a los extremos de la escala. Los negros de Williamsburg miden valor 0,8 a 1 y el blanco de titanio 9,73 [@justpaint-munsell-cielab, tabla Williamsburg]; los negros de Golden, en torno a 1 [@justpaint-munsell-cielab, listado Golden].

Por último, la lectura de una tabla tiene límites. La tabla de Williamsburg no indica iluminante ni observador [@justpaint-munsell-cielab, tabla Williamsburg]. Según un resumen de la metodología de Golden, las lecturas dependen del espesor: con películas finas poco opacas salen más claras y de más croma [unverified].

### Ejemplo
Se quiere mezclar un azul parecido al cerúleo oscuro de Golden y se dispone de un ultramar claro. Los datos del fabricante dicen que el cerúleo oscuro está en 1,2 PB 3/7,9 y el ultramar claro en 3,0 PB 6,3/7,9: mismo croma, tres puntos de valor de diferencia [@justpaint-munsell-cielab, listado Golden]. Decisión:

1. No basta con acercar el matiz.
2. Hay que comprobar el valor aparte y oscurecer la mezcla hasta igualarlo.

Para estimar el valor mientras se pinta, Briggs defiende que una escala absoluta tiene ventajas prácticas aunque en pintura se trabaje sobre todo con valores relativos [@briggs-dimensions, 112.php, 081.php]. Da también un consejo de taller: los colores de croma alto parecen más claros de lo que son (un efecto de resplandor), de modo que se sobreestima su claridad; entrecerrar los ojos reduce ese resplandor y ayuda a comparar valores [@briggs-dimensions, 081.php, 013.php].

### Las fuentes discrepan
Las escalas de valor no coinciden entre autores. Briggs señala que la mayoría de los negros miden alrededor de 2 en el Munsell moderno y que la escala de Frank Reilly tiene once niveles con el negro y el blanco de pintura en 0 y 10 [@briggs-dimensions, 081.php]. Hay que mirar qué escala usa cada autor o fabricante. Briggs añade que el valor Munsell 10 corresponde a un reflector difuso perfecto, de modo que su equivalente en *L*\* es superior a 100 [@briggs-dimensions, 081.php]. Briggs es una fuente de fiabilidad C: sus consejos de taller son recomendaciones prácticas, no medidas.

### Para seguir
El [sistema Munsell](munsell-system.md) y [CIELAB para pintores](cielab-basics.md) explican con más detalle las dos notaciones de estas tablas.
