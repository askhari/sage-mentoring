---
concept: subtractive-mixing
title: "Mezcla sustractiva"
---

## Fundamentos {#layer-1}

El color de un objeto depende de lo que absorbe y de lo que refleja: un objeto azul a la luz blanca se ve azul, uno negro absorbe todo, y un objeto azul iluminado solo con luz roja se ve negro porque absorbe el rojo [@openstax-college-physics-2e, §26.3, Fig. 26.12] (ver [por qué los objetos tienen color](../../light-and-vision/concepts/light-matter-interaction.md)). La **mezcla sustractiva (subtractive mixing)** parte de esa idea: cada material que se añade quita (absorbe) más luz, de modo que la mezcla absorbe más que cualquiera de sus componentes. Por eso las mezclas de pintura tienden a oscurecerse y a apagarse [@handprint-macevoy, color18a, "Subtractive Mixtures Always Increase Light Absorptance"]. Newton lo observó con polvos de colores: mezclados no dan un blanco brillante, sino un tono apagado (gris, pardo), porque los polvos absorben buena parte de la luz [@newton-1704, Prop. V, Exper. 15].

Los primarios sustractivos modernos son cian, amarillo y magenta; el trío tradicional rojo-amarillo-azul estaba limitado por los pigmentos que había en cada época [@handprint-macevoy, color18a, "The CYM Subtractive 'Primary' Colors"].

**Ejemplo cotidiano.** Amarillo más azul da verde: cada pintura absorbe parte del espectro y lo que queda se ve verde. Al contrario que con luces (ver [mezcla aditiva](additive-mixing.md)), cada ingrediente quita luz en lugar de añadirla.

**Importante: la pintura solo es *aproximadamente* sustractiva.** Macevoy califica la teoría sustractiva de aproximación, no de teoría rigurosa [@handprint-macevoy, color18a, "Subtractive Color Mixture"]. Un modelo sustractivo puro solo considera absorción, pero en una pintura real las partículas de pigmento también dispersan (scattering) la luz; por eso un modelo sustractivo puro predice un resultado más oscuro, menos saturado y de otro matiz que la pintura real [@sochorova-2021, pp. 3-4, §2]. La capa 2 y [cómo se mezclan de verdad los pigmentos](pigment-mixing-behavior.md) explican esa diferencia.

![Tres luces roja, verde y azul solapadas sobre negro, que dan amarillo, cian, magenta y blanco en el centro, junto a tres filtros cian, magenta y amarillo solapados sobre blanco, que dan azul, verde, rojo y negro en el centro](../../../../../assets/diagrams/additive-vs-subtractive-overlaps.es.svg)

## Comprensión {#layer-2}

**Absorber no es lo mismo que dispersar.** Kubelka y Munk construyeron su modelo de una capa de pintura sobre esa distinción: la absorción elimina luz de forma permanente, mientras que la dispersión solo la redirige, y el artículo presenta esto como la diferencia central con la visión anterior, que no separaba ambas [@kubelka-munk-1931, p. 2, §1; nota 6, p. 7]. Una teoría de filtros apilados contiene solo absorción; una pintura contiene las dos.

**Por qué falla la regla simple.** Sochorova y colaboradores comparan varios modelos con mezclas reales de azul cobalto y amarillo Hansa: el modelo sustractivo puro y el híbrido sustractivo-aditivo (que da resultados más claros pero sigue fallando en el matiz) no coinciden con la pintura, y tampoco la interpolación RYB, que según ellos da colores lejanos al comportamiento real [@sochorova-2021, pp. 3-4, §2, Figs. 5-6]. En el modelo que sí coincide, el verde sale de que ambas clases de partículas absorban y dispersen la luz repetidamente dentro de la pintura hasta que emergen sobre todo longitudes de onda verdes [@sochorova-2021, p. 2, §2, Fig. 3].

**El grano de verdad.** El modelo sí capta lo esencial: añadir un absorbente fuerte, como negro de humo en un blanco, sube la absorción en proporción a la cantidad añadida sin cambiar apenas la dispersión [@kubelka-munk-1931, p. 3, §2]. Y un blanco casi perfecto es muy sensible a trazas de colorante [@kubelka-munk-1931, pp. 3-4, §2, Fig. 1].

**Luz frente a pigmento.** Munsell señalaba que la luz espectral recombinada da blanco, mientras que las mezclas de pigmentos dan gris [@munsell-1905, ¶92-93]. Es la misma diferencia que separa la mezcla aditiva de la sustractiva.

**Errores frecuentes.** (1) "La pintura es CMY y punto": en impresión, las tintas cian, amarillo y magenta se superponen sustractivamente dentro de cada punto [@handprint-macevoy, color18a, "Partitive Mixture"], pero eso no convierte cada mezcla de tubos en predecible. (2) "El color visual del tubo basta para predecir la mezcla": pinturas con el mismo aspecto mezclan distinto [@handprint-macevoy, color18a, "Substance Uncertainty"].

## Profesional {#layer-3}

**Usar el modelo sustractivo como brújula.** Para el taller, la mezcla sustractiva sirve para anticipar la *dirección*: mezclar siempre cuesta luz y croma, y cuanto más separados están los colores en la rueda, más se paga [@handprint-macevoy, color13 y color14, "saturation costs"]. No sirve para calcular el resultado: Macevoy recomienda usar la rueda como guía direccional, no como calculadora [@handprint-macevoy, mix].

**Qué hace un profesional cuando importa la precisión.** Se miden los coeficientes de absorción y dispersión de cada pigmento y se calcula la mezcla (véase [pigment-mixing-behavior](pigment-mixing-behavior.md)); el procedimiento y sus límites están en esa capa 3. Y se comprueba siempre en una muestra seca, porque las mezclas cambian al secar [@handprint-macevoy, color13 y tech17].

**Dónde buscar más.** El capítulo sobre mezcla aditiva y sustractiva en tecnología del color es Berns, cap. 10 §C, de lectura adicional [@berns-2019].
