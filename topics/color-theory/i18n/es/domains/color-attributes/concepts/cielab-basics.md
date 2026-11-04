---
concept: cielab-basics
title: "CIELAB para pintores"
format: 2
---

## Profesional {#layer-3}

### Idea clave
CIELAB convierte una medida con instrumento en tres números (*L*\*, *a*\*, *b*\*), aproximadamente uniformes para la percepción. Sirve para comunicar un color y para calcular la diferencia entre dos (Δ*E*), con límites que hay que conocer [@cie-e-ilv, 17-23-076, 17-23-077].

### Explicación
Este concepto empieza directamente en la capa profesional. Parte del [sistema Munsell](munsell-system.md), porque los fabricantes de pintura publican hoy los dos juntos, y de los [procesos oponentes](../../light-and-vision/concepts/opponent-process.md), porque los ejes de CIELAB siguen la lógica rojo-verde y amarillo-azul.

El *espacio CIE 1976 L\*a\*b\* (CIELAB)* es un espacio de color tridimensional, aproximadamente uniforme desde el punto de vista perceptual, con coordenadas rectangulares *L*\*, *a*\* y *b*\* que se calculan a partir de los valores triestímulo X, Y, Z del color relativos a los de un blanco especificado [@cie-e-ilv, 17-23-076]. Las fórmulas son:

*L*\* = 116 f(Y/Y<sub>n</sub>) − 16

*a*\* = 500 [f(X/X<sub>n</sub>) − f(Y/Y<sub>n</sub>)]

*b*\* = 200 [f(Y/Y<sub>n</sub>) − f(Z/Z<sub>n</sub>)]

donde f es la raíz cúbica por encima de (6/29)³ y lineal por debajo [@cie-e-ilv, 17-23-076]. Lo relevante para quien pinta es que **no hay muestras físicas ni ojo humano comparando**, sino una medida con instrumento convertida a tres números.

Cada eje tiene un significado:

- *L*\* aproxima la claridad (el [valor](value.md)) [@cie-e-ilv, 17-23-076].
- *a*\* va del verde (negativo) al rojo (positivo) y *b*\* del azul (negativo) al amarillo (positivo); el centro es acromático y la saturación aumenta al alejarse de él [@konica-minolta-pcc, Parte I-7].
- El croma se deriva de *a*\* y *b*\*, y el ángulo de matiz es *h*<sub>ab</sub> = arctan(*b*\*/*a*\*) [@cie-e-ilv, 17-23-076].

La versión cilíndrica, *L*\**C*\**h*, usa la misma gráfica en coordenadas polares: *C*\* es el croma, 0 en el centro y creciente con la distancia, y *h* es el ángulo en grados desde el eje +*a*\* (0° rojo, 90° amarillo, 180° verde, 270° azul) [@konica-minolta-pcc, Parte I-8]. La fórmula usual es *C*\*<sub>ab</sub> = √(*a*\*² + *b*\*²) (cálculo propio, no extraído de esa fuente) [@justpaint-munsell-cielab, tabla Williamsburg, cálculos].

La CIE definió CIELAB en 1976 como un espacio uniforme para resolver que distancias iguales en el diagrama x,y de CIE Yxy no correspondían a diferencias percibidas iguales [@konica-minolta-pcc, Parte I-7]. Es uno de los espacios más populares para medir el color de los objetos [@konica-minolta-pcc, Parte I-7]. Solo es "aproximadamente" uniforme, no perfectamente [@cie-e-ilv, 17-23-076].

Con él se mide la diferencia de color. La CIE la define como la distancia euclidiana entre dos puntos del espacio [@cie-e-ilv, 17-23-077]:

Δ*E*\*<sub>ab</sub> = √(Δ*L*\*² + Δ*a*\*² + Δ*b*\*²)

El número indica el tamaño de la diferencia, no su dirección. Para saber en qué sentido se aleja una muestra, se descompone en *L*\**C*\**h* [@konica-minolta-pcc, Parte I-11]. Como tolerancia, la idea de fondo del control de calidad es fijar un patrón y aceptar una muestra si su Δ*E* no pasa de un límite. En un taller sirve para comprobar que dos lotes de la misma pintura coinciden o para comparar una mezcla con el color objetivo.

Para elegir entre sistemas:

| Necesidad | Sistema |
|---|---|
| Comparar a ojo con muestras físicas, o describir cómo se ve una mezcla | Munsell |
| Comunicar o archivar una medida, o calcular una diferencia entre dos pinturas | CIELAB (*L*\**a*\**b*\*, *L*\**C*\**h*) |
| Predecir cómo se verá un color en un contexto distinto (otro fondo, otra luz) | Un modelo de apariencia del color; CIELAB es un ejemplo sencillo y tiene limitaciones |

[Cuadro de síntesis propia a partir de las fuentes citadas; para el modelo de apariencia, @fairchild-2013, cap. 10, §10.3-10.4, solo índice] [unverified]

### Ejemplo
Los datos de Williamsburg (óleo, 6 mil) incluyen Munsell y *L*\**a*\**b*\* para cada pintura [@justpaint-munsell-cielab, tabla Williamsburg]. Calculando *C*\*<sub>ab</sub> y *h*<sub>ab</sub> a partir de *a*\* y *b*\* (cálculo propio) se obtiene:

| Pintura | Munsell (H V/C) | *L*\* | *a*\* | *b*\* | *C*\*<sub>ab</sub> | *h*<sub>ab</sub> |
|---|---|---|---|---|---|---|
| Azul ultramar | 9,01 PB 0,32/18,16 | 4,78 | 24,88 | −37,90 | 45 | 303° |
| Amarillo de cadmio limón | 9,06 Y 9,05/12,69 | 89,99 | −8,36 | 94,94 | 95 | 95° |
| Rojo de cadmio claro | 9,29 R 5,13/17,97 | 51,19 | 64,23 | 70,20 | 95 | 48° |
| Ocre amarillo | 9,62 YR 5,55/8,69 | 55,50 | 18,84 | 52,68 | 56 | 70° |
| Sombra natural | 6,41 Y 1,83/1,18 | 18,68 | 0,42 | 7,03 | 7 | 87° |

[@justpaint-munsell-cielab, tabla Williamsburg; *C*\* y *h* calculados]

Tres lecturas que sirven en el taller:

1. **Valor y *L*\* van a la par, con un factor de unos 10.** En la tabla, valor 0,32 corresponde a *L*\* 4,78, valor 5,13 a 51,19 y valor 9,73 a 98,24, es decir, aproximadamente *L*\* ≈ 10 × valor [@justpaint-munsell-cielab, tabla Williamsburg; cálculo sobre las filas]. Con ello se explica por qué el azul ultramar de tubo es tan oscuro (*L*\* 4,78, por debajo del negro de marfil con 10,83) y por qué el amarillo de cadmio es claro (*L*\* 83 a 90) [@justpaint-munsell-cielab, tabla Williamsburg].
2. **El croma Munsell y *C*\* no son proporcionales entre matices.** El amarillo de cadmio medio tiene croma Munsell 16,78 y *C*\*<sub>ab</sub> ≈ 113; el ultramar, con croma Munsell 18,16 (superior), solo llega a *C*\*<sub>ab</sub> ≈ 45 [@justpaint-munsell-cielab, tabla Williamsburg, cálculo sobre las filas]. Por eso no se puede convertir una cifra de croma de un sistema al otro con un único factor.
3. **El ángulo de matiz de CIELAB no es el matiz Munsell.** El ultramar (9,01 PB) tiene *h* ≈ 303° y el cadmio limón (9,06 Y), ≈ 95° (cálculo propio): en los dos sistemas el mismo lugar del círculo tiene números distintos, y conviene no mezclar escalas [@justpaint-munsell-cielab, tabla Williamsburg].

Un ejemplo de diferencia de color, de la guía de Konica Minolta: una manzana patrón con *L*\* 43,31, *a*\* 47,63, *b*\* 14,12 y otra muestra con 47,34, 44,58 y 15,16 dan Δ*L*\* = +4,03, Δ*a*\* = −3,05, Δ*b*\* = +1,04 y Δ*E*\*<sub>ab</sub> = 5,16. Descompuesta en *L*\**C*\**h*, la misma pareja da Δ*L*\* = +4,03 (más clara), Δ*C*\* = −2,59 (menos croma) y Δ*H*\* = +1,92 (hacia el amarillo) [@konica-minolta-pcc, Parte I-11].

### Errores frecuentes
- *"Un Δ*E* bajo garantiza que se ven iguales."* El Δ*E*\*<sub>ab</sub> trata la tolerancia como un círculo perfecto en todos los matices y saturaciones, pero la discriminación humana es elíptica, así que los valores del colorímetro pueden no coincidir con el juicio visual [@konica-minolta-pcc, Parte V-2].
- *"La sensibilidad a las diferencias es igual en todo el espacio."* Es baja con saturación alta, varía con el matiz y la de claridad alcanza su máximo cerca de *L*\* 50 [@konica-minolta-pcc, Parte V-2].
- *"Los *L*\**a*\**b*\* de una ficha se interpretan solos."* El PDF de Williamsburg no indica iluminante ni observador [@justpaint-munsell-cielab, tabla Williamsburg]; sin ellos, los valores no son completamente interpretables. Los instrumentos calculan con iluminantes estándar de la CIE como C o D65 y con un observador estándar [@konica-minolta-pcc, Parte I-13]. Un colorímetro mide siempre con la misma fuente y geometría, a diferencia del ojo, cuya percepción cambia con el fondo o la luz [@konica-minolta-pcc, Parte I-10]. Para el metamerismo hace falta un espectrofotómetro [@konica-minolta-pcc, Parte III-1]. Véase [metamerismo](../../light-and-vision/concepts/metamerism.md).

### Las fuentes discrepan
Las fuentes no fijan una tolerancia general. La guía de Konica Minolta muestra parejas que se ven idénticas y aun así dan Δ*E*\*<sub>ab</sub> de 0,77, 0,18 y 0,15, y **no da umbrales de tolerancia** [@konica-minolta-pcc, Parte I-12]. El valor de corte aceptable hay que fijarlo según el uso; no se ha encontrado en las fuentes un valor general [unverified].

Las pinturas, además, cambian al secar: según un resumen de la metodología de Golden, el óleo y el acrílico cambian de valor o de color al secar [unverified].

Por las limitaciones del Δ*E*\*<sub>ab</sub> hay fórmulas posteriores de diferencia de color (CMC, CIEDE2000), que el libro de Berns trata en su cap. 5 [@berns-2019]; aquí solo se señalan como lectura adicional.

### Para seguir
Para llevar estos datos a la práctica, [mezclar un color objetivo](../../color-mixing/concepts/target-color-mixing.md) reúne matiz, valor y croma en un procedimiento de taller. Como lectura adicional: Fairchild, cap. 3 §3.8-3.9 (espacios de color y especificación de diferencias de color) [@fairchild-2013]; Berns, cap. 4 §G (espacios aproximadamente uniformes: CIELAB, CIELUV) [@berns-2019]; CIE 015, informe de colorimetría [@cie-015-2018]; la tesis de Okumura sobre una base de datos de pinturas acrílicas [@okumura-2005].
