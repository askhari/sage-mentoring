---
concept: spin-qubits
title: "Qubits de espín en semiconductores"
---

## Comprensión {#layer-2}

**Qué son.** Un *qubit de espín (spin qubit)* en un semiconductor codifica `|0⟩` y `|1⟩` en el espín de un electrón (o de un hueco) atrapado en un *punto cuántico (quantum dot)*, una región de unos 100 nm definida con electrodos de puerta sobre un chip. Es la misma idea de [sistema de dos niveles](../../quantum-mechanics/concepts/two-level-systems.md) del espín, pero con el electrón fijado por electrodos fabricados con técnicas de la microelectrónica [@burkard-2023, §I, p. 3; §II.A, pp. 4-5]. La razón para perseguirlos es su compatibilidad con la fabricación industrial de silicio [@stano-2022, p. 1]; la meta es la escala: Burkard y colaboradores razonan que un ordenador con corrección de errores completa podría necesitar del orden de 10⁶ qubits físicos y que puntos de ~100 nm permiten matrices densas hechas por la industria [@burkard-2023, §I, p. 3].

**Cuatro maneras de codificar un qubit.** La revisión de Burkard y colaboradores (publicada en 2023; preprint de 2021, así que todos sus experimentos son anteriores a 2022) los clasifica por cuántos espines codifican un qubit [@burkard-2023, §II, p. 4; Fig. 2, p. 5]. Dos de los autores son de HRL Laboratories, así que no son independientes del campo.

| Tipo | Idea | Control | Lectura |
|---|---|---|---|
| Un espín (Loss-DiVincenzo, LD) | `|0⟩`, `|1⟩` = espín abajo/arriba de un electrón | campo magnético alterno transversal; acoplo por intercambio `J` entre puntos vecinos para puertas de dos qubits [@burkard-2023, §II.A, pp. 4-5] | tunelamiento selectivo de espín a un depósito (Elzerman), con campo de ~10 T en GaAs [@burkard-2023, §II.A, pp. 4-5] |
| Dos espines (singlete-triplete, ST0) | `|S⟩` y `|T0⟩` de dos electrones en un doble punto | pulsos de tensión en banda base (`J`); necesita un gradiente de campo para el segundo eje [@burkard-2023, §II.C, pp. 7-8] | bloqueo de espín de Pauli, que convierte la diferencia singlete/triplete en una configuración de carga que lee un sensor [@burkard-2023, §II.C, p. 8] |
| Tres espines (exchange-only, EO) | tres espines con espín total 1/2 | solo intercambio da control universal, con dos ejes a 120° en la esfera de Bloch; sin campos oscilantes ni micromagnetos [@burkard-2023, §II.D, pp. 8-9] | igual que ST; el bloqueo de espín no distingue el estado fugado `S=3/2` del `|1⟩` codificado [@burkard-2023, §II.D, p. 9] |
| Donantes | espín nuclear o electrónico de un átomo dopante (31P) | el nuclear tiene un cociente giromagnético ~2000 veces menor que el electrón, lo que lo hace muy coherente [@burkard-2023, §II.B, pp. 5-6] | |

Hay variantes híbridas con carácter de carga (flopping-mode, cuadrupolo de carga, spin-carga) que ganan dipolo eléctrico y control rápido a cambio de más exposición al ruido de carga [@burkard-2023, §II.E, pp. 9-10]. Stano y colaboradores resumen la clasificación en tres: espín-1/2 (LD), singlete-triplete (ST) e híbrido (HY, que incluye EO y RX) [@stano-2022, p. 2].

**Cómo se hace una puerta.** El intercambio `J` aparece cuando las funciones de onda de dos electrones se solapan, y los distintos tipos de qubit lo usan de algún modo [@burkard-2023, §II, p. 4]. Cuando se hace "puerta de uno" o "de dos" depende de la funcionalidad, así que la frontera es borrosa [@stano-2022, p. 8]. Para girar un único espín con un campo eléctrico se usa la *resonancia de espín dipolar eléctrica (EDSR)*, muy eficaz en huecos, con puertas de hasta GHz; en electrones hacen falta micromagnetos (gradientes de campo grandes) o materiales con fuerte acoplamiento espín-órbita [@stano-2022, p. 8].

**Materiales.**

- *GaAs:* todos sus isótopos tienen espín nuclear (`I = 3/2`), lo que da ruido hiperfino fuerte; T2\* de ~10 ns y T2 de ~1 µs para ST0 [@burkard-2023, §II.B, p. 6; §III.F, p. 18; §VI.B, pp. 43-44].
- *Silicio:* mayoritariamente isótopos sin espín nuclear (28Si, 30Si), con un 4,7 % de 29Si que se puede eliminar por enriquecimiento [@burkard-2023, §III.A.1, p. 10]. Las arquitecturas son Si-MOS, Si/SiGe, FinFET y SLEDGE [@burkard-2023, §III.A.2, pp. 11-12]. Hay que lidiar con los *valles*: el silicio masivo tiene seis mínimos de banda de conducción, y la separación de valles (50-500 µeV en Si-MOS; hasta unos 200-300 µeV en Si/SiGe) suele ser la excitación más baja del punto [@burkard-2023, §III.E, pp. 17-18].
- *Germanio (huecos):* acoplamiento espín-órbita fuerte (control eléctrico rápido sin micromagnetos), hiperfino débil y sin valles; a cambio, mezcla de bandas y gran dependencia del dispositivo [@burkard-2023, §V.A.4, pp. 29-30; §V.E.3, pp. 38-39].

**Coherencia (cifras con fecha de publicación del experimento).** Stano y colaboradores recopilan los valores en tablas hasta 2024-25 y avisan de que eligen un valor "representativo" por experimento, algo subjetivo [@stano-2022, p. 2]:

- *T1:* hasta 57 s para un electrón en GaAs/AlGaAs (agosto de 2018), 43 s para un donante de Si:P (marzo de 2024); hasta 32 ms en huecos de Ge/SiGe [@stano-2022, p. 6; Tabla I, pp. 16-17]. Los autores señalan que un T1 largo no mejora otras figuras de mérito y muestra sobre todo el progreso de la plataforma [@stano-2022, p. 6].
- *T2\* (Ramsey):* hasta 2,4 ms para un donante 28Si:P en el sistema rotante (octubre de 2016); unos 0,12 ms en puntos con puerta de 28Si/SiO₂; 18 µs para un hueco de Ge/SiGe (mayo de 2024); y de decenas de ns en GaAs singlete-triplete [@stano-2022, Tabla I, pp. 17-20].
- *T2 con eco:* 9,2 ms para el donante (rotante, 2016); 1,2 ms para un electrón en 28Si/SiO₂ (octubre de 2014) [@stano-2022, Tabla I, pp. 20-22].
- *Desacoplamiento dinámico:* 0,56 s en 28Si:P (2014), 28 ms en 28Si/SiO₂, 3,1 ms en 28Si/SiGe, 1,9 ms en Ge/SiGe (2024) [@stano-2022, Tabla I-7, p. 22].

Los autores resumen que los valores de T2\* de 2024 abarcan cinco órdenes de magnitud según el tipo de qubit, el material y la protección, y que los espines de impurezas tienen los récords [@stano-2022, p. 5]. Un matiz importante: el T2\* con ruido `1/f` no es una propiedad intrínseca (ver [coherencia y fidelidad](coherence-and-fidelity.md)) [@burkard-2023, §VI.A.3, p. 42].

**Qué limita la coherencia.** Hay dos enemigos:

- *Ruido hiperfino (espines nucleares):* se puede eliminar con enriquecimiento isotópico [@burkard-2023, §VI.D, p. 46].
- *Ruido de carga `1/f`:* los espines se acoplan al ruido eléctrico a través del acoplamiento espín-órbita, los gradientes de micromagnetos o la dependencia del intercambio; en opinión de los autores no se puede eliminar por completo de los dispositivos semiconductores [@burkard-2023, §VI.D, pp. 45-46]. Los dispositivos con micromagnetos tienen T2 y T2\* limitados por la carga, y los huecos también [@burkard-2023, §VI.B, p. 44; §VI.D, pp. 45-46].

**Fidelidades (con fecha).** Stano y colaboradores recogen en la Tabla III, por plataforma [@stano-2022, §IV.B, p. 11; Tabla III, pp. 30-31]:

| Qubit | 1Q | 2Q |
|---|---|---|
| Electrón en 28Si/SiGe | 99,96 % (septiembre de 2022) | 99,81 % (CZ, abril de 2022) |
| Hueco en Ge/SiGe | 99,992 % (junio de 2023), récord para cualquier qubit de espín | 99,3 % (julio de 2024) |
| Donante 28Si:P | 99,942 % (octubre de 2016); 99,78 % (febrero de 2024) | 90 % (julio de 2019); 82 % (septiembre de 2024) |
| Híbrido (EO) en 28Si/SiGe | 99,89 % (marzo de 2023) | 96,3 % |

Son las mejores cifras: muchas entradas de 2Q son mucho más bajas (83-93 %) [@stano-2022, Tabla III, p. 31]. El patrón general, como en otras plataformas, es que la infidelidad de dos qubits supera en al menos un orden de magnitud la de uno [@stano-2022, §IV.B, p. 11]. La lectura mejora: el récord es casi el 99,99 % para un qubit EO en silicio purificado (marzo de 2022) y 99,96 % para un ST (2024); hasta hace poco la infidelidad de medida estaba por encima de unos pocos por ciento [@stano-2022, p. 11; Tablas III-2 a III-4, pp. 31-33].

**Velocidad.** Un qubit de espín puede ser muy rápido: puertas de un qubit de 0,2 ns (ST en GaAs, 2014), 0,41 ns (hueco, 2023), 40-100 ns en silicio; puertas de dos qubits de 40 ns en 28Si/SiGe (abril de 2022) y de 9 ns en un hueco de Ge (marzo de 2021) [@stano-2022, Tabla II, pp. 26-28]. Pero "un qubit rápido no es automáticamente bueno": por eso la revisión informa del factor de calidad `Q = f_R · T2*`, cuyos valores están sobre todo entre unas pocas unidades y ~100, con unos pocos que se acercan a 1000 (máximo: 558 para un qubit ST en 28Si/SiGe, agosto de 2024) [@stano-2022, p. 7; p. 12; Tabla IV, p. 35].

**Lectura.** Casi toda la lectura es *espín a carga*: la medida directa del espín es indirecta, pasa por detectar una sola carga elemental, que tarda ~100 ns con la sensibilidad típica y marca el límite inferior del tiempo de medida; los tiempos de medida de las tablas abarcan de ~50 ns a 0,2 s [@stano-2022, pp. 8-9]. La lectura dispersiva con un resonador, el mismo método que en los superconductores, desplaza la frecuencia del resonador en `χ = g²/(ω_a − ω_c)` [@burkard-2023, §VII.C, p. 50].

**Escala y madurez.** Stano y colaboradores definen tres niveles: "dispositivo" (puertas y sensado de carga funcionan, pero la operación cuántica es limitada), "simulador" y "procesador" (control en dos ejes, lectura, interacción por pares ajustable, capaz de ejecutar algoritmos de `N` qubits) [@stano-2022, pp. 12-13]. Pasar de un doble punto al primer procesador completamente funcional llevó unos 10-15 años (primeros experimentos hacia 2005); el primer "procesador" más allá de un doble punto llegó en 2021, con electrones en silicio y huecos en germanio [@stano-2022, p. 13, Fig. 10]. Los mayores arreglos a nivel de dispositivo (Tabla V) son de 4×4 huecos en Ge/SiGe (agosto de 2023) y de 12 qubits en Si/SiO₂ (mayo y octubre de 2024), y solo hay operación a nivel de procesador con 3 qubits (GHZ de 3 qubits y una Toffoli) [@stano-2022, Tabla V, pp. 36-37; Tabla II-3, p. 28; Tabla III-5, p. 34]. La primera puerta de 3 qubits se usó en una demostración de corrección de errores (agosto de 2022) [@stano-2022, pp. 7, 13].

**Errores frecuentes.**

- *"Los qubits de espín ya compiten en tamaño con los demás."* No: los mayores arreglos a nivel de procesador tienen 3 qubits; los de más de una decena son de nivel de dispositivo [@stano-2022, pp. 13, 36-37].
- *"Una coherencia larga basta."* Una T2 larga es necesaria pero no suficiente para el control de alta fidelidad [@burkard-2023, §VI.A.6, p. 43].
- *"Hay una tecnología de espín."* Hay varios portadores (electrón, hueco, donante), materiales y codificaciones; los autores de la revisión consideran prematuro decir cuál ganará [@burkard-2023, §VIII, pp. 51-52].

## Profesional {#layer-3}

**Qué significa para quien programa hoy.** Las notas de este tema no describen acceso en la nube a dispositivos de espín, y los resultados citados son experimentos de laboratorio; para cargas de trabajo prácticas, hoy son una plataforma que seguir, no una que usar. Si algún día se programan, el modelo de programación se parecerá al de los superconductores: puertas muy rápidas (decenas de ns) [@stano-2022, Tabla II, pp. 26-28], interacción de intercambio de corto alcance y por tanto vecinos más próximos [@burkard-2023, §IV.F, pp. 24-25], y lectura de espín a carga. Todo lo que sigue es lectura de los dos revisores.

**Trade-offs entre variantes.** Según Burkard y colaboradores: los qubits LD son eficientes y robustos frente al ruido de carga; ST0 y EO permiten control eléctrico en banda base (EO, sin acoplamiento espín-órbita ni micromagnetos); el silicio ofrece coherencia muy alta y el germanio, control eléctrico gracias al espín-órbita; los espines nucleares tienen una coherencia extrema pero el intercambio electrónico es rápido [@burkard-2023, §VIII, pp. 51-52]. Los micromagnetos y los qubits RX dan control cómodo a costa de sensibilidad al ruido de carga; los puntos dulces del intercambio (por ejemplo, detuning cero en ST0) la reducen [@burkard-2023, §VI.D, p. 46].

**Conectividad y escala: los cuellos de botella.**

- *Fabricación.* Burkard y colaboradores afirman que los qubits de espín tienen las exigencias de fabricación más estrictas frente a superconductores, iones y fotónicos, por su pequeño tamaño; por eso el camino a matrices grandes ha sido más lento [@burkard-2023, §VIII, p. 51]. La fabricación sustractiva compatible con la industria se está adoptando, con dispositivos CMOS de nanohilos de fundiciones industriales que muestran operación de un electrón y un qubit [@burkard-2023, §III.C, p. 15].
- *Cableado y direccionamiento.* Es uno de los retos citados, junto con la conectividad para corrección de errores [@burkard-2023, §I, p. 3]. Un experimento usó electrónica de control criogénica integrada (cryo-CMOS) [@stano-2022, Tabla I-3, nota, p. 18].
- *Conectividad.* El intercambio es de corto alcance (puertas entre vecinos). Opciones de largo alcance: transporte de espín (shuttling) o cadenas de SWAP, superintercambio, buses de espín (una cadena de `N` puntos da un acoplo `J/√N`), acoplo capacitivo o dipolar, y cavidades de microondas [@burkard-2023, §IV.F, pp. 24-25; §VII, p. 46]. Se ha alcanzado acoplamiento fuerte espín-fotón en Si/SiGe (resonador de 6,03 GHz), pero en el momento de la revisión faltaba una puerta de dos qubits mediada por cavidad en el dominio temporal [@burkard-2023, §VII.B-D, pp. 48-51].
- *Matrices 2D.* Stano y colaboradores señalan que el escalado es "el mayor reto actual" del campo y que parecen necesarias matrices 2D grandes porque los umbrales de tolerancia a fallos de las matrices 1D siguen siendo demasiado bajos [@stano-2022, p. 12].
- *Umbral y geometría.* Burkard y colaboradores advierten de que no está claro cuándo un qubit es "suficientemente bueno", porque las estimaciones estándar del umbral del código de superficie suponen una geometría y correlaciones de error que no coinciden con los dispositivos de espín actuales [@burkard-2023, §VIII, p. 52]. Ver [teorema del umbral](../../error-correction/concepts/threshold-theorem.md).
- *Temperatura.* Las temperaturas electrónicas típicas en los experimentos son de 50-300 mK; para Elzerman hace falta `k_B·T_e` mucho menor que la energía de Zeeman [@burkard-2023, §V.A.1, nota 4, p. 26]. Algunos resultados clave se citan a 1 K o 1,5 K (en dispositivos de Si/SiO₂ y Ge), según notas de las tablas [@stano-2022, notas de tabla, pp. 17, 30-31]. Las fuentes no ofrecen una afirmación general sobre temperatura de funcionamiento; no se debe presentar "funciona a 1 K" como propiedad de la plataforma.

**Cómo comparar con las demás plataformas con prudencia.**

- Las mejores fidelidades de puertas de espín de la compilación de Stano (1Q 99,96 %, 2Q 99,81 % en silicio) y los 99,992 % de un qubit en germanio son del mismo orden que las mejores de otras plataformas de este ámbito (por ejemplo, 99,9 % en dos qubits en iones en 2019 y 99,7 % en superconductores en 2020) [@stano-2022, Tabla III, pp. 30-31; @bruzewicz-2019, p. 4; @kjaergaard-2020, Tabla 1, p. 8]. Pero eso son *mejores valores* de una tabla con valores "representativos" elegidos por los autores, no medianas de dispositivo, y no se pueden poner en paralelo con las medianas de Google (2019) o los promedios de Quantinuum (2023) sin decir que son tipos de dato distintos.
- La fidelidad de RB no es la que define el umbral [@stano-2022, p. 9, nota 8], y la conversión entre fidelidad de Clifford y de puerta elemental es dudosa, con razones citadas de 1,875 y 2,57 [@stano-2022, p. 10, nota 13].
- Burkard y colaboradores señalan que el estado de la plataforma es una instantánea de preprint de diciembre de 2021, sin los resultados de 2022-2024 [@burkard-2023, nota de acceso]. Stano y colaboradores recogen valores hasta septiembre de 2024 con algunas entradas de 2025 [@stano-2022, nota de acceso].

**Cuándo mirar los espines (criterio propio a partir de lo anterior).** Si te interesa el hardware a largo plazo, los espines son la apuesta por la densidad y por la integración con la industria CMOS (puntos de ~100 nm, un millón de qubits físicos como orden de magnitud de una máquina con corrección de errores) [@burkard-2023, §I, p. 3]. Eisert y Preskill escriben que los qubits fotónicos y de espín pueden ir ahora por detrás pero podrían dar un salto [@eisert-2025, Sec. III, p. 5]. Hasta entonces, para algoritmos y programación, lo que debes llevarte es el vocabulario: factor de calidad, T2\* frente a eco, fidelidad de RB frente a umbral. Para el lugar de esta plataforma en el conjunto, ver la [comparativa](hardware-landscape.md).

**Señales de alarma.** Una fidelidad "récord" sin decir si es de un par de qubits seleccionado; T2\* citado sin la secuencia (Ramsey, eco, desacoplamiento) ni el tiempo de promediado; la fidelidad de lectura que incluye o excluye preparación (la de 99,975 % para un qubit EO incluye ambas) [@stano-2022, Tabla III-2, p. 31]; y un "procesador" que en realidad es un "dispositivo" de la clasificación de Stano.
