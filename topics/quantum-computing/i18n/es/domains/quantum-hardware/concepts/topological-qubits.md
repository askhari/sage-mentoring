---
concept: topological-qubits
title: "Qubits topológicos"
format: 2
---

## Comprensión {#layer-2}

### Idea clave
Un *qubit topológico (topological qubit)* guardaría la información no en un lugar concreto, sino repartida entre cuasipartículas muy separadas, de modo que el ruido local no la pueda leer ni estropear. A diferencia de las demás plataformas del ámbito, en las fuentes usadas no hay hoy un qubit topológico demostrado [@eisert-2025, Sec. III, p. 5; @aghaee-2025, p. 8].

### Explicación
Es la propuesta más antigua de robustez intrínseca [@eisert-2025, Sec. III, p. 5]. Lo que hay es una teoría muy elegante y experimentos en discusión; esta página explica la teoría y deja claro cuál es el estado de la evidencia.

La teoría parte de los *anyones (anyons)*. En tres dimensiones solo existen bosones y fermiones, porque dar una vuelta completa de una partícula alrededor de otra se puede deshacer; en dos dimensiones esa vuelta no se puede deshacer, así que intercambiar partículas idénticas puede dar una fase arbitraria [@nayak-2008, p. 3]. Los intercambios de `N` partículas en 2+1 dimensiones se clasifican por el *grupo de trenzas (braid group)*, infinito y no conmutativo [@nayak-2008, pp. 3-4]. En los anyones *no abelianos*, cuando `N` cuasipartículas fijas tienen un espacio degenerado de estados fundamentales, cada intercambio actúa como una matriz unitaria sobre ese espacio, y esas matrices no conmutan [@nayak-2008, p. 4]. Esto es lo que permite calcular trenzando.

Los anyones solo aparecen como cuasipartículas emergentes en un sistema de muchos cuerpos bidimensional (una *fase topológica de la materia*); los electrones, átomos y fotones son siempre bosones o fermiones, aunque estén confinados en un plano [@nayak-2008, p. 6].

De ahí vendría la reducción de errores. El espacio computacional es el de estados fundamentales degenerados, separado de las excitaciones por un salto de energía (*gap*); una perturbación local (fonones, interacción hiperfina) no tiene elementos de matriz no triviales dentro de ese espacio, así que la decoherencia por ruido local se suprime. El qubit no es local: se almacena en el número cuántico compartido de varias cuasipartículas lejanas [@nayak-2008, p. 9]. Y la puerta depende solo de la clase topológica de la trenza, no de pequeñas ondulaciones del camino: las trenzas son discretas, de modo que no hay un error de "girar 90,01 grados" [@nayak-2008, pp. 9-10]. Es tolerancia a fallos "a nivel de hardware", sin necesidad de corrección de errores por software, pero es la descripción del caso ideal [@nayak-2008, p. 10].

Quedan errores. Las cuasipartículas no deseadas, creadas térmicamente o atrapadas por el desorden, pueden provocar una trenza equivocada [@nayak-2008, pp. 10-11]. Un par excitado que solo rodea a una cuasipartícula existente no daña el qubit; hace falta que trence al menos dos cuasipartículas computacionales [@nayak-2008, pp. 11, 59-60]. La probabilidad de error escala como `exp(−Δ/2T)` para pares térmicos (con `Δ` el gap) o `exp(−ΔL/v)` para virtuales con tamaño de qubit `L`, por lo que se debe operar a temperatura muy por debajo del gap [@nayak-2008, pp. 11, 60].

El modelo más sencillo con anyones no abelianos usa los *anyones de Ising*: tres tipos (1, σ, ψ) con la regla de fusión `σ × σ = 1 + ψ`; cuatro σ que se fusionan en 1 generan un espacio de dimensión 2, el qubit topológico más simple [@nayak-2008, p. 5]. En un superconductor `p+ip`, un vórtice de medio cuanto de flujo atrapa un modo de energía cero cuyo operador es su propio conjugado, es decir, un *modo cero de Majorana (Majorana zero mode, MZM)* [@nayak-2008, pp. 30-31]. Dos MZM definen un sistema de dos niveles cuyos dos canales de fusión corresponden a la paridad fermiónica del par [@nayak-2008, p. 31]. Es decir, el qubit sería la **paridad** de un par de modos de Majorana.

Pero trenzar no basta. Con anyones de Ising el trenzado solo genera un conjunto finito de rotaciones de tipo 90 grados, de modo que no implementa todas las unitarias [@nayak-2008, pp. 52-53]. La solución propuesta es añadir una puerta de fase π/8 de un qubit y una medida de paridad de dos qubits; la puerta de fase se obtiene acercando dos cuasipartículas, una operación **no topológica** que no puede ser exacta, así que haría falta algo de corrección de errores por software. La exactitud necesaria es modesta (puerta π/8 con ~14 % y medida con ~38 %, citando a Bravyi 2006) [@nayak-2008, p. 53]. Los anyones de Fibonacci sí son universales por trenzado; el candidato que se citaba era el estado `ν = 12/5`, con una sola observación publicada de la meseta bien cuantizada en 2008 y posiblemente abeliano [@nayak-2008, pp. 2, 16, 53-54]. Incluso un hardware topológico perfecto de tipo Ising necesitaría, pues, un recurso no topológico para ser universal (la [universalidad](../../qubits-and-circuits/concepts/universal-gate-sets.md) también tiene su coste aquí).

En cuanto a candidatos, en 2008 los únicos sistemas con alguna evidencia indirecta de anyones no abelianos eran los estados de Hall cuántico fraccionario, y no había evidencia experimental directa [@nayak-2008, pp. 11, 16]. Los candidatos eran `ν = 5/2` (Moore-Read), `ν = 12/5`, superconductores `p+ip` como Sr₂RuO₄, gases ultrafríos y modelos de espines en redes [@nayak-2008, pp. 13-22]. En 2000, DiVincenzo ya mencionaba la computación topológica de Kitaev con anyones no abelianos, pero ningún sistema físico se consideraba que albergase las excitaciones necesarias [@divincenzo-2000, p. 7].

El experimento más citado hoy es el de Microsoft (2024-2025), que mide la **paridad fermiónica** de un estado de energía casi cero en un nanohilo de InAs-Al definido con puertas [@aghaee-2025, abstract, p. 1]. Se describe en el ejemplo.

### Ejemplo
El artículo de Aghaee y colaboradores (Microsoft Azure Quantum; todos los autores son de Microsoft) usa un interferómetro de tres puntos cuánticos acoplado por túnel al hilo, y lee la capacidad cuántica de un punto por reflectometría de radiofrecuencia [@aghaee-2025, nota de acceso; p. 1; p. 2]. Los resultados que reportan [@aghaee-2025, abstract, pp. 3-5]:

- La capacidad cuántica cambia con la paridad hasta ~1 fF, cerca del máximo simulado.
- La señal es bimodal y periódica en flujo con periodo `h/2e` (oscilación de curtosis de 1,7(2) mT frente a 1,7 mT esperados), con una señal telegráfica aleatoria entre dos valores donde hay bimodalidad.
- Relación señal-ruido de 4,9 en una ventana de 90 µs (equivalente a SNR 1 en 3,7 µs), y un error de asignación del 1 % en el tiempo óptimo de medida.
- Un tiempo de permanencia de ~2 ms, que identifican con el tiempo de envenenamiento por cuasipartículas.

Lo que no reportan (según la lectura de las notas sobre el texto principal): control coherente, trenzado o fusión entre dos pares de MZM, tiempo de coherencia de un qubit ni corrección de errores [@aghaee-2025, resumen de las notas, pp. 1-8]. Lo medido es la **lectura** de paridad de una sección de hilo, no una operación de qubit.

Los propios autores:

- afirman un "progreso significativo hacia" un qubit topológico y que la medida es un "ingrediente necesario" y "un paso hacia" la fusión [@aghaee-2025, abstract; p. 1; p. 8];
- describen sus datos como "consistentes con" una medida de paridad codificada en un par de MZM separados ~3 µm [@aghaee-2025, abstract];
- advierten de que la medida **por sí sola no separa** sin ambigüedad los MZM de la fase topológica de estados de Andreev ligados de baja energía finamente sintonizados en la fase trivial; la cuestión se aplaza a una publicación aparte [@aghaee-2025, p. 1; p. 8].

El punto de operación se elige con el *protocolo de salto topológico (topological gap protocol, TGP)*, que solo se cita (referencias 55 y 56 del artículo) y cuya correlación con los datos de capacidad se difiere a un artículo "en preparación" [@aghaee-2025, p. 3; pp. 1, 10-11]. Hay tres controles: inyectar cuasipartículas por otra sección reduce a la mitad el tiempo de permanencia; desconectar los puntos del hilo elimina la señal; y a 0,8 T, bien dentro de la fase trivial, no aparece periodicidad `h/e` [@aghaee-2025, p. 6].

### Errores frecuentes
- *"Topológico significa sin errores."* La protección es contra el ruido local; quedan los errores por cuasipartículas térmicas o atrapadas [@nayak-2008, pp. 10-11]. En el dispositivo de Microsoft el tiempo de envenenamiento por cuasipartículas era de ~2 ms [@aghaee-2025, p. 4; p. 8].
- *"Un fermión de Majorana es una partícula fundamental nueva."* Aquí es una cuasipartícula emergente en un material [@nayak-2008, p. 6; pp. 30-31].
- *"Con trenzar basta para computar."* Con anyones de Ising no [@nayak-2008, pp. 52-53].
- *"Los qubits locales nunca serán tolerantes a fallos, por eso hace falta lo topológico."* Eso era una duda abierta en 2008 (ver el desacuerdo abajo).

### Las fuentes discrepan
Hay que separar fuentes de épocas y posturas distintas.

La teoría. Los autores de la revisión de 2008 son entusiastas del campo (Freedman y Nayak, de Microsoft Station Q) [@nayak-2008, nota de acceso]. Su estimación sencilla para un qubit de 5/2 (gap ~500 mK, `T` ~5 mK) da un error de ~10⁻¹⁵, que ellos mismos llaman demasiado optimista, porque otros gaps pequeños, un gap variable en muestras desordenadas y saltos de rango variable pueden dominar [@nayak-2008, p. 60; p. 18]. Su estado de las plataformas no es el actual, y la propuesta de nanohilos semiconductores con superconductor que usa Microsoft hoy no estaba en esa revisión [@nayak-2008, nota de acceso].

El argumento de los qubits locales. Nayak y colaboradores citaban umbrales de la corrección por redundancia de 10⁻⁴ a 10⁻⁶ por operación y decían que era "por ahora poco claro" que los ordenadores de qubits locales pudieran llegar a ser tolerantes a fallos [@nayak-2008, p. 8]. El contexto ha cambiado: el código de superficie tiene un umbral de unos 10⁻² según simulaciones [@eisert-2025, Box 2, p. 5]. Además, un preprint de Google de 2024 informa de una memoria lógica por debajo del umbral con `Λ = 2,14` [@google-2025, pp. 1-3]. Eso es solo una memoria, no un ordenador completo, y sigue habiendo sobrecarga; el programa topológico de Microsoft apostaba, según Preskill (2018), por tasas de error mucho menores [@preskill-2018, §7, pp. 14-15; §8, p. 15].

El experimento de Microsoft. Las notas leen la versión v4 de abril de 2024 del preprint, que Legg cita como publicado en Nature 638 en 2025 [@aghaee-2025, nota de acceso; @legg-2025, p. 1]. Un crítico, Legg (comentario en arXiv de marzo de 2025, versión v1, **no revisado por pares** según el texto leído, sin respuesta de Microsoft en esa versión), reanalizó los datos y el código públicos de Microsoft y sostiene [@legg-2025, p. 1; pp. 2-5]:

- que el resultado del TGP cambia al elegir la ventana de campo (para el dispositivo A1, "con gap" entre 1,5-3 T pero "sin gap" si se corta a 1,5-2,2 T, ventana que aún contiene el campo de lectura) o el "cutter";
- que el dispositivo B tiene otras regiones que pasan el TGP, que no se usaron para comprobar la reproducibilidad;
- que los datos de conductancia sin mostrar en el artículo contienen muchos estados de baja energía y conductancia no local grande, lo que interpreta como dispositivos muy desordenados sin gap claro;
- que, por tanto, el TGP no es fiable como detector de gap, el efecto es más probablemente un efecto mesoscópico de desorden finamente sintonizado y las conclusiones centrales del artículo "no son fiables y deberían revisarse".

Legg no dice que haya demostrado que no existan Majorana: dice explícitamente que no discute si la región es topológica, solo si tiene gap [@legg-2025, p. 2; nota de cautela]. Es el análisis de una persona y no está confirmado de forma independiente en las notas [@legg-2025, nota de cautela]. Las notas no cubren desarrollos posteriores a marzo de 2025 (réplicas, versiones nuevas, resultados de otros grupos): para el estado actual hay que mirar fuentes más recientes.

Lo que se puede decir con honestidad no es "Microsoft ha construido un qubit topológico" ni "está refutado". Las fuentes sostienen que hay una medida de paridad en un dispositivo prototipo; que sus autores dicen que no basta por sí sola para demostrar topología; que un crítico cuestiona el protocolo con el que se eligieron los puntos de operación; y que no se ha mostrado ninguna operación de qubit [@aghaee-2025, p. 1; p. 8; @legg-2025, pp. 1-5].

### Para seguir
La capa 3 propone una escalera de evidencia para leer críticamente cualquier anuncio topológico y repasa las implicaciones prácticas. Las [puertas tolerantes a fallos y estados mágicos](../../error-correction/concepts/fault-tolerant-gates.md) retoman el recurso no topológico que necesitaría un hardware de tipo Ising.

## Profesional {#layer-3}

### Idea clave
Esta página sirve para leer críticamente un anuncio: el "qubit" topológico no existe como tal y los pasos intermedios se cuentan con física de la materia condensada. Lo útil es poder decir de cualquier anuncio en qué peldaño de la escalera de evidencia está [@aghaee-2025, p. 1; p. 8].

### Explicación
Los anuncios topológicos son los más difíciles de evaluar. Una **escalera de evidencia** (síntesis propia a partir de Nayak, Aghaee y Legg), de abajo arriba:

1. *Un gap en el dispositivo de medida:* aislante de excitaciones de baja energía. Es lo que discute Legg, y lo que el TGP pretende certificar [@legg-2025, pp. 1-2].
2. *Modos de energía cero localizados en los extremos:* la medida requiere que el estado esté soportado en ambos extremos del hilo y débilmente acoplado a otros estados de baja energía, pero no basta para distinguirlo de estados de Andreev finamente sintonizados [@aghaee-2025, p. 1].
3. *Lectura de paridad de un solo disparo:* lo que reporta el artículo (SNR 4,9 en 90 µs, error de asignación del 1 %) [@aghaee-2025, abstract; p. 4].
4. *Coherencia de un qubit de paridad:* no mostrada.
5. *Trenzado o fusión entre dos pares:* no mostrado. El artículo describe su diseño futuro, un hilo de 5 segmentos con 2 superconductores 1D topológicos, cuatro MZM y tres interferómetros, y operación solo por medidas [@aghaee-2025, p. 2; p. 1].
6. *Un conjunto universal de puertas:* con anyones de Ising hace falta añadir una puerta de fase π/8, que no es topológica, y una medida de paridad de dos qubits [@nayak-2008, p. 53].
7. *Corrección de errores en software por encima:* siguiente paso; ver [qubits lógicos](../../error-correction/concepts/logical-qubit-experiments.md).

Las implicaciones prácticas son pocas:

- *Para la programación (criterio propio):* hoy ninguna. Los algoritmos de este ámbito se escriben igual para un qubit físico o lógico; un hardware topológico, de existir, aparecería como un qubit con muy bajo error físico, lo que reduciría la sobrecarga de corrección [@preskill-2018, §7, pp. 14-15; §8, p. 15].
- *Para la planificación de recursos:* los autores del artículo de Microsoft sostienen que los esquemas de solo medidas son un camino hacia máquinas de utilidad con millones de qubits (motivación del artículo, no resultado) [@aghaee-2025, p. 1]. Ver [estimación de recursos](../../error-correction/concepts/resource-estimation.md) para los órdenes de magnitud de otras plataformas.
- *Relación con otras plataformas:* el modelo de fusión de la fotónica también podría aplicarse con proyección de carga anyónica [@bartolucci-2023, §I, p. 1]. Otras líneas de robustez intrínseca son los qubits de gato y los de doble raíl en superconductores [@eisert-2025, Sec. III, p. 5].

Tendrá sentido planear algo cuando haya una demostración de operaciones de qubit con datos públicos y replicables. Hasta entonces, para decisiones de ingeniería, el hardware topológico es un riesgo de investigación, no una opción; compáralo con las demás en la [comparativa](hardware-landscape.md).

### Ejemplo
Según el texto leído, el artículo de Microsoft está en el paso 3 de la escalera, con los pasos 1 y 2 en discusión. Para cualquier anuncio topológico, pregunta:

- ¿Se muestra una operación de qubit (coherencia, puerta, fusión)?
- ¿La evidencia de topología es independiente de la elección del punto de operación?
- ¿Hay réplica independiente?
- ¿Se ha hecho pública la conductancia completa?
- ¿La publicación está revisada por pares y qué versión?

Si la respuesta es "solo una lectura", no se ha demostrado un qubit. Si la respuesta es "hay un artículo crítico", léelo, pero tampoco lo conviertas en una refutación.

### Las fuentes discrepan
Cada parte cita argumentos propios. Aghaee y colaboradores ajustan sus datos a un modelo de MZM con "buena concordancia" [@aghaee-2025, pp. 4, 8]. Sostienen que un par de Majorana "oculto" con acoplo débil daría una señal de capacidad muy suprimida e incompatible con los datos, mientras que un acoplo mayor que la temperatura separa en energía ambos modos y requeriría ajuste fino [@aghaee-2025, p. 6]. Legg dice que la ausencia de un gap claro hace el efecto compatible con desorden mesoscópico [@legg-2025, p. 5].

Para cerrar la cuestión, Legg pide (como crítica, no como lista cerrada) mostrar el gap en los datos de conductancia local y no local sin antisimetrizar, probar la lectura en todas las regiones que pasan el TGP y reportar completo el resultado del TGP [@legg-2025, p. 5; pp. 3-5]. De las dos partes falta una réplica independiente y el seguimiento de la correlación entre capacidad y TGP (el artículo "en preparación") [@aghaee-2025, p. 1]. No hay en las notas una respuesta publicada a Legg [@legg-2025, nota de cautela].

### Para seguir
La [comparativa y estado actual del hardware](hardware-landscape.md) sitúa los qubits topológicos entre las demás plataformas.
