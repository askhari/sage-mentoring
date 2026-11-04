---
concept: illuminant-color
title: "El color de la luz (iluminante, temperatura de color)"
format: 2
---

## Comprensión {#layer-2}

### Idea clave
El color que vemos depende del objeto y de la luz que lo ilumina. Esa luz tiene su propio espectro, que se normaliza con iluminantes estándar y se resume, de forma aproximada, con la temperatura de color [@openstax-college-physics-2e, §26.3; @cie-e-ilv, 17-23-021].

### Explicación
El color depende de dos cosas: el objeto ([lo que refleja y absorbe](light-matter-interaction.md)) y la luz. Las fuentes de luz tienen color propio según las longitudes de onda que emiten: un láser de He-Ne es de un rojo puro, el Sol tiene un espectro amplio y amarillento, las lámparas fluorescentes son blanco azuladas y las incandescentes, blanco rojizas [@openstax-college-physics-2e, §26.3, Fig. 26.13].

En el uso técnico, un iluminante (illuminant) es una radiación con una distribución espectral de potencia relativa definida, especificada en el rango de longitudes de onda relevante para el color percibido de los objetos; fuera del uso técnico, la palabra suele significar cualquier luz que cae sobre un cuerpo o escena [@cie-e-ilv, 17-23-018]. Esta definición se apoya en la [distribución espectral](light-spectrum.md) de la luz.

La CIE normaliza algunos iluminantes: el A corresponde a la radiación planckiana a unos 2 855,5 K, y el D65 representa una fase de la luz del día con temperatura de color correlacionada de unos 6 500 K. Se recomienda usarlos cuando proceda para obtener resultados comparables [@cie-e-ilv, 17-23-021].

Para resumir una luz con un número se usa la temperatura de color. Un radiador planckiano (Planckian radiator, cuerpo negro) es un radiador térmico ideal que absorbe toda la radiación incidente y emite el máximo posible a cada longitud de onda a su temperatura [@cie-e-ilv, 17-24-004]. La ley de Wien dice que los cuerpos más calientes tienen su máximo a longitudes de onda más cortas (λmax·T = 2,898×10⁻³ m·K), y un cuerpo que se calienta brilla rojo apagado, luego naranja y después en todo el espectro visible [@openstax-physics-3, Vol. 3 §6.1].

La **temperatura de color (colour temperature, Tc)** es la temperatura del radiador planckiano cuya radiación tiene la misma cromaticidad que el estímulo. La **temperatura de color correlacionada (CCT)** es la del radiador planckiano de cromaticidad más próxima, y no debe usarse si la cromaticidad de la fuente se aleja demasiado del lugar geométrico planckiano. Se mide en kelvin [@cie-e-ilv, 17-23-067, 17-23-068].

El ojo, por último, compensa aproximadamente los cambios del color de los estímulos, sobre todo cuando cambia el iluminante; es la adaptación cromática (chromatic adaptation) [@cie-e-ilv, 17-22-013]. Es lenta, a diferencia de la inducción cromática, casi instantánea [@cie-e-ilv, 17-22-075]. Por eso un cuarto con luz cálida deja de parecer tan amarillo a los pocos minutos; esa observación cotidiana no figura en las notas [unverified]. El tema se prolonga en la constancia del color, de otro ámbito [@openstax-college-physics-2e, §26.3].

### Ejemplo
Las llamas azuladas son más calientes que las amarillentas. La ley de Wien lo respalda: un cuerpo rojo (Betelgeuse) es más frío que uno azul (Rigel) [@openstax-physics-3, Vol. 3 §6.1]. Así, "cálido" en el lenguaje del pintor (rojizo) corresponde a temperaturas de color bajas, lo contrario de la intuición de "calor".

### Errores frecuentes
- *"Luz blanca es una sola cosa."* Puede tener espectros muy distintos que parecen blancos.
- *"La CCT describe la luz entera."* Es un resumen de un solo número; no describe el espectro completo, y dos luces con la misma CCT pueden renderizar los colores de manera distinta (idea que las notas no recogen) [unverified].

### Las fuentes discrepan
Los textos de física consultados no explican la temperatura de color como término ni los espectros de lámparas LED o fluorescentes en detalle [@openstax-physics-3, Vol. 3 §6.1]. Para ello hay que acudir a la terminología de la CIE.

### Para seguir
La capa 3 aplica todo esto a la elección de la luz de estudio. Antes, [metamerismo](metamerism.md) muestra qué le pasa a una igualación cuando cambia el iluminante.

## Profesional {#layer-3}

### Idea clave
Un cuadro cambia al pasar de la luz del día a una luz cálida porque cambia la distribución espectral de la luz que lo ilumina; el ojo solo corrige en parte, con la adaptación cromática [@cie-e-ilv, 17-24-064, 17-23-018, 17-22-013].

### Explicación
Lo que sí está respaldado: el color depende de la iluminación [@openstax-college-physics-2e, §26.3]; los iluminantes estándar existen para obtener resultados comparables [@cie-e-ilv, 17-23-021]; la luz del día tiene una CCT de unos 6 500 K en D65 y la incandescente (iluminante A) de unos 2 855,5 K [@cie-e-ilv, 17-23-021]. De ello se deduce que pintar con una luz cálida y mostrar el cuadro con una fría cambia el espectro de la luz que llega a cada pigmento.

El color visto es el resultado de esa luz y de la reflectancia de cada pintura [@cie-e-ilv, 17-24-064; @openstax-college-physics-2e, §26.3]. Cuánto se nota para cada pigmento concreto depende de su curva, que varía entre pigmentos (se verá en el ámbito de pinturas).

Qué luz conviene elegir en el estudio (norte, LED de CCT determinada, índice de reproducción cromática) es una decisión de oficio que las notas no abordan [unverified].

### Ejemplo
Un pintor ha terminado un cuadro con luz cálida y va a exhibirlo en una sala de luz fría. Para decidir:
1. Anotar con qué luz se ha pintado y con cuál se exhibirá [unverified].
2. Revisar el cuadro bajo más de una luz antes de darlo por terminado: es la protección práctica frente al [metamerismo](metamerism.md) [unverified].
3. Para comparar o documentar un color, usar un iluminante normalizado (como D65) en lugar de "luz de día" sin especificar [@cie-e-ilv, 17-23-021].

### Para seguir
Lectura adicional: Berns, cap. 7 "Lighting" (iluminantes estándar, CCT, reproducción del color) [@berns-2019]; Fairchild, §3.3 [@fairchild-2013]. Cierra el ámbito con [metamerismo](metamerism.md).
