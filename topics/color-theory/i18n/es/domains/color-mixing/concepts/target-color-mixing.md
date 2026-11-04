---
concept: target-color-mixing
title: "Mezclar un color objetivo"
format: 2
---

## Profesional {#layer-3}

### Idea clave
Con un color delante (un objeto, una referencia, una muestra) que debes reproducir con tus pinturas, no existe una receta única. Sí hay un procedimiento razonado: describir el objetivo, comprobar que la paleta llega, elegir pigmentos, mezclar por pasos y juzgar sobre una muestra seca [@handprint-macevoy, mix].

### Explicación
Este concepto reúne el ámbito entero. Los pasos 1-4 siguen un método de fiabilidad C basado en acuarela; los pasos 5-6 son en parte consejo de taller sin respaldo propio, como se indica en cada caso [@handprint-macevoy, mix].

**1. Describe el objetivo en tres dimensiones.** Hay que fijar su [matiz](../../color-attributes/concepts/hue.md), [valor](../../color-attributes/concepts/value.md) y [croma](../../color-attributes/concepts/chroma.md); con las tres, un color queda definido [@munsell-1905, ¶8, ¶20]. Se localiza el matiz (la "posición del reloj" en la rueda) y el croma (distancia al centro), y la claridad se trata aparte, ajustándola con agua, blanco o negro [@handprint-macevoy, mix, paso 1]. A ojo hay que ser prudente, porque juzgar un gris medio a ojo es poco fiable: una muestra dada por "media" reflejaba solo el 42 % de la luz, y la diferencia entre personas, e incluso entre ojos, superaba el 10 % [@munsell-1905, ¶65]. Una escala medida o una carta de referencia ayuda ([sistema Munsell](../../color-attributes/concepts/munsell-system.md)).

**2. Comprueba que tu paleta puede llegar.** Las tablas de pinturas dan el valor y croma Munsell de cada una: el amarillo de cadmio medio de Williamsburg mide 8,45 / 16,78 y el ocre amarillo 5,55 / 8,69, de modo que un amarillo de croma alto no sale de un ocre [@justpaint-munsell-cielab, tabla Williamsburg]. Si el objetivo cae fuera del gamut de los primarios, lo más que se logra es el color mezclable más cercano [@sochorova-2021, p. 5, §3]. En pintura, en cambio, otra pintura puede alargar el gamut (véase [primarios](primary-colors.md)).

**3. Elige los pigmentos.** Se eligen dos pinturas cuya línea de mezcla pase fuera del objetivo o cerca del centro (pares que desplazan el matiz para objetivos saturados; pares que desplazan el croma para objetivos apagados) y, si hace falta, una tercera para formar un triángulo alrededor del objetivo [@handprint-macevoy, mix, pasos 2-3]. Otra descripción coincide: escoger pinturas a ambos lados del objetivo en matiz, llevar cada una al valor del objetivo, mezclarlas y después reducir el croma si hace falta [@briggs-dimensions, 109.php]. Las dos pinturas de mezcla fijan matiz y textura; el "color de ajuste" (normalmente la más alejada del objetivo) afina croma y valor [@handprint-macevoy, mix, paso 4]. Para bajar el croma, recuerda los [complementarios](complementary-colors.md) y los neutralizantes; para subir o bajar valor, los [tintes y sombras](tints-shades-tones.md).

**4. Mezcla por pasos.** Empieza más saturado que el objetivo, porque las pinturas se apagan al secar [@handprint-macevoy, mix, paso 4]. Ten en cuenta la fuerza tintórea: una pintura de más fuerza domina la mezcla más allá de su proporción [@handprint-macevoy, mix, "Estimate proportions"]. Diluye en la paleta la pintura más débil para cubrir toda la zona [@handprint-macevoy, mix, paso 6]. Añade gradualmente la dominante, prueba sobre papel y deja secar; añade con moderación el color de ajuste; y descarta el excedente en lugar de perseguir el color [@handprint-macevoy, mix, pasos 7-8].

**5. Prueba una muestra seca, no la mancha húmeda.** Las mezclas cambian al secar y las muestras deben secar al menos diez minutos [@handprint-macevoy, color13 y tech17]. Las mezclas de cadmio y ftalo pueden parecer más frías de lo que son, por lo que conviene juzgar con la muestra seca [@handprint-macevoy, mixtable]. Los acrílicos se oscurecen y saturan ligeramente al secar [@justpaint-munsell-cielab, método, de segunda mano]. Compara la muestra con el objetivo bajo una luz comparable [unverified], porque dos colores que coinciden con una luz pueden no coincidir con otra (véase [metamería](../../light-and-vision/concepts/metamerism.md)).

**6. Si falla, diagnostica por dimensión.** "Es del matiz correcto, pero demasiado clara" apunta al valor; "demasiado viva" al croma. Qué dimensión corregir es una decisión sobre qué pigmento añadir (negro, complementario, agua, blanco), no un reflejo [unverified].

### Ejemplo
Un programa resuelve el problema inverso: dado un color RGB, busca por mínimos cuadrados las concentraciones de cuatro pigmentos que reproducen el objetivo [@sochorova-2021, p. 4, §3, Eq. 9]. Distintas combinaciones de pigmentos pueden dar el mismo RGB, por lo que hay que fijar de antemano un conjunto [@sochorova-2021, p. 4, §3]. Esa es la versión mecánica de limitar tu paleta, y la razón de que una paleta limitada haga las mezclas repetibles. Se obtienen buenos resultados dentro del gamut y un residual para lo que cae fuera [@sochorova-2021, p. 9, §4.2].

Para el modelado cuantitativo y las bases de datos de colorantes, la fuente son Zhao y Berns, que fijan dos muestras por colorante, con mejor resultado hacia un 40-60 % de pigmento en blanco [@zhao-berns-2006, resumen].

### Las fuentes discrepan
Los pasos 1-4 se apoyan en un solo método, el de Macevoy (fiabilidad C, basado en acuarela), y solo el paso 3 tiene una descripción parecida en Briggs, fuente de fiabilidad baja [@handprint-macevoy, mix; @briggs-dimensions, 109.php]. Úsalos como punto de partida y ajusta según tu medio.

### Para seguir
Para llevar este procedimiento a un cuadro completo, véase el ámbito de color y luz en la pintura.
