---
concept: nisq-era
title: "La era NISQ"
---

## Fundamentos {#layer-1}

**Qué significa.** *NISQ* son las siglas de *Noisy Intermediate-Scale Quantum* (cuántico ruidoso de escala intermedia), un término que acuñó John Preskill en 2018 para la etapa que se abría entonces [@preskill-2018, §4.1, pp. 4-5]. *Intermedia* significa aproximadamente de 50 a unos pocos cientos de qubits; *ruidoso* significa que el control de los qubits es imperfecto [@preskill-2018, §4.1, pp. 4-5]. Y, en concreto, las puertas son ruidosas y **no están protegidas por corrección de errores cuánticos** [@preskill-2018, §4.2, p. 5].

**Por qué 50 qubits.** Es un hito porque supera lo que los mayores supercomputadores clásicos pueden simular por fuerza bruta; Preskill reconoce que es un umbral difuso, porque el coste de simulación depende también de la profundidad del circuito [@preskill-2018, §4.1, p. 5 y nota 2]. Vuelve sobre ello en [simuladores y vectores de estado](simulators-and-statevectors.md).

**Ejemplo cotidiano en Qiskit.** Si ejecutas un par de Bell en un simulador ideal, solo salen `00` y `11`. Si lo haces en un dispositivo real, o en un dispositivo falso con ruido, aparecen un pequeño porcentaje de `01` y `10` que un circuito ideal nunca daría. Eso es "ruidoso" en la práctica: con un dispositivo falso de 5 qubits, por ejemplo, obtuvimos `{'00': 1923, '11': 1951, '10': 62, '01': 64}` en 4000 shots (varía entre ejecuciones; el código está en [ejecutar en hardware real](running-on-hardware.md)). Cada puerta falla una pequeña fracción de veces, y los fallos se acumulan a lo largo del circuito.

**Lo que se puede esperar.** Preskill sostiene que NISQ probablemente no cambiará el mundo por sí mismo: es un paso hacia tecnología más potente, útil para explorar la física de muchos cuerpos, con aplicaciones comerciales inciertas [@preskill-2018, §4.1, p. 5; §8, p. 15]. Confía en un impacto sustancial en décadas, pero no en el potencial comercial de los próximos 5 a 10 años [@preskill-2018, §1, p. 1]. Las tecnologías realmente transformadoras tendrán probablemente que ser tolerantes a fallos [@preskill-2018, §8, p. 16].

**La palabra "ruidoso" no se refiere solo a los qubits.** Observar un sistema lo perturba de forma incontrolable, de modo que los qubits tienen que estar casi aislados y, al mismo tiempo, interactuar con fuerza, ser controlables y poder leerse [@preskill-2018, §3.2, p. 4]; ese conflicto es la raíz del problema, que desarrolla [decoherencia](../../quantum-mechanics/concepts/decoherence.md).

## Comprensión {#layer-2}

**Cuánto aguanta un circuito.** Preskill da una regla de pulgar: con un error de puerta de dos qubits del 0,1 % o peor, no se espera que funcionen circuitos con mucho más de unas 1000 puertas de dos qubits, porque el ruido ahoga la señal [@preskill-2018, §4.2, p. 5]. En general, en un circuito con `G` puertas un solo fallo en cualquier punto puede arruinar el resultado, así que el circuito no es fiable si el error por puerta es mucho mayor que `1/G`; el propio autor dice que puede ser demasiado pesimista para algunos algoritmos [@preskill-2018, §6.4, p. 9]. Cai et al. lo formalizan con fallos de Pauli independientes de probabilidad `p_f`: la probabilidad de ejecución sin fallos es `P₀ = Π(1−p_f) ≈ e^{−λ}`, con `λ = Σ p_f` el número medio de fallos por ejecución [@cai-2023, Sec. II.C, p. 5]. Con `p = 0,1 %` por puerta:

```python
import math

p = 1e-3                      # 0,1 % de fallo por puerta de dos qubits
for G in (100, 1000, 5000):
    print(G, round((1 - p) ** G, 4), round(math.exp(-p * G), 4))   # (1-p)^G ≈ e^(-λ), λ = p·G
```

```text
100 0.9048 0.9048
1000 0.3677 0.3679
5000 0.0067 0.0067
```

Con 100 puertas, el 90 % de las ejecuciones salen limpias; con 1000, solo el 37 %; con 5000, el 0,7 %. Por eso el tamaño útil de un circuito sin mitigación es del orden de `1/p` puertas, en línea con la regla de Preskill. Preskill proyecta circuitos de unos 100 qubits y profundidad inferior a 100, quizá mucho menos [@preskill-2018, §6.2, p. 8].

**Cifras de 2018 frente a hoy.** En 2018, el error de puerta de dos qubits en los mejores dispositivos de iones atrapados y superconductores estaba por encima del 0,1 %, a menudo mucho peor, y el error de medida rondaba el 1 % en superconductores y era mucho mejor en iones [@preskill-2018, §4.2, p. 5]. Son números de 2018: las notas de IBM Quantum Learning citan, para un dispositivo tipo Eagle, un error mediano de `ECR` de ~6,9·10⁻³ y de `SX` de ~2,3·10⁻⁴ (cifras de un resumen, a tomar con cautela) [@ibm-quantum-learning, "Hardware"]. Para el estado actual del hardware, consulta [comparativa y estado actual del hardware](../../quantum-hardware/concepts/hardware-landscape.md).

**El número de qubits no es la medida.** Cuentan también la precisión de las puertas, la velocidad, la precisión de la medida, la conectividad y el rendimiento de fabricación [@preskill-2018, §4.2, p. 5]. Por eso, en Qiskit, la [transpilación](transpilation.md) y la elección del dispositivo importan tanto como su tamaño.

**Estrategias NISQ.** Dos respuestas:

- **Algoritmos con circuitos cortos:** los [algoritmos variacionales](variational-algorithms.md) sustituyen una evolución larga por muchas cortas. Peruzzo et al. los propusieron porque la estimación de fase exigía una coherencia muy por encima de las decenas a centenares de puertas posibles a corto plazo [@peruzzo-2014, p. 1]. La parte cuántica es pequeña y de profundidad fija, y la búsqueda la hace el ordenador clásico [@peruzzo-2014, p. 5]. Preskill nombra como lo concreto a probar los algoritmos híbridos cuántico-clásicos de optimización [@preskill-2018, §8, p. 15].
- **Mitigación de errores:** Preskill apuntaba que los métodos de mitigación podrían importar mucho en la era NISQ aunque no hubiera corrección de errores [@preskill-2018, §6.4, p. 9]; hoy hay técnicas concretas, desarrolladas en [mitigación de errores](error-mitigation.md), pero con sobrecargas que crecen con el tamaño del circuito [@cai-2023, Sec. II.D, p. 5].

**Supremacía y ventaja.** Preskill define *supremacía cuántica (quantum supremacy)* como una tarea que un dispositivo cuántico puede hacer y ningún dispositivo clásico existente o fácilmente previsible, sea o no útil; una *ventaja cuántica (quantum speedup)* suele significar vencer al mejor hardware clásico con el mejor algoritmo clásico, y los ordenadores clásicos siguen mejorando, de modo que lo cuántico persigue un objetivo móvil [@preskill-2018, §6, p. 7]. Y como los dispositivos NISQ son imperfectos, puede ser difícil validar que la respuesta es correcta, sobre todo en simulación cuántica [@preskill-2018, §6, p. 7]. Ver [experimentos de ventaja cuántica](../../quantum-hardware/concepts/quantum-advantage-experiments.md).

**Qué no se espera de NISQ.** Preskill considera probablemente fuera de alcance: la inversión de matrices (HHL), que puede ser demasiado cara sin corrección de errores; los sistemas de recomendación cuánticos, demasiado costosos de validar; y la simulación precisa de moléculas y materiales grandes, que puede exigir corrección de errores [@preskill-2018, §6.6-6.9, pp. 11-13]. Tampoco se espera que resuelvan eficientemente instancias difíciles de problemas NP-difíciles [@preskill-2018, §3.1, p. 3] (ver [complejidad cuántica](../../quantum-algorithms/concepts/quantum-complexity.md)). Los recocedores cuánticos (*quantum annealers*), como el D-Wave 2000Q de unos 2000 qubits, no son máquinas basadas en circuitos, y no hay todavía una teoría o experimento convincente de que superen al mejor hardware y algoritmos clásicos [@preskill-2018, §6.3, pp. 8-9].

**Errores frecuentes.**

- *"NISQ significa que los ordenadores cuánticos no sirven."* Es una etapa: un paso hacia máquinas tolerantes a fallos [@preskill-2018, §8, p. 15-16].
- *"Más qubits, mejor máquina."* La calidad cuenta [@preskill-2018, §4.2, p. 5].
- *"Los términos NISQ y VQE ya estaban en el artículo de Peruzzo."* No: el artículo de 2013-2014 no usa el término NISQ, que no existía [@peruzzo-2014, texto completo].

## Profesional {#layer-3}

**Cómo se evalúa una afirmación NISQ.** Preguntas que ayudan a leer un artículo o una nota de prensa:

1. **¿Cuántas puertas de dos qubits tiene el circuito transpilado y cuál es el error por puerta?** Con la cuenta de `e^{−λ}` de arriba se sabe cuántas ejecuciones salen limpias. Un resultado sobre un circuito que supera con holgura `1/p` puertas solo puede ser creíble si hay mitigación y se razona el sesgo.
2. **¿La salida es un valor esperado?** La mitigación se aplica a valores esperados y no a salidas de un solo disparo (fase, factorización) [@cai-2023, Sec. II.A, p. 3].
3. **¿Cuál es la línea base clásica?** La ventaja se mide frente al mejor algoritmo y hardware clásicos, que mejoran [@preskill-2018, §6, p. 7].
4. **¿Cómo se verifica?** Más allá de unas decenas de qubits ya no se puede simular con ruido en un portátil [@qiskit-docs, /guides/local-testing-mode]; se comparan observables de valor conocido o versiones reducidas.
5. **¿El coste de mitigación ha entrado en la cuenta?** ZNE cuesta unas 3 veces; PEC crece exponencialmente con la profundidad [@qiskit-docs, /guides/error-mitigation-and-suppression-techniques].

**Un caso de referencia: "utilidad".** IBM Quantum Learning usa "utilidad" de manera informal para experimentos más allá de la simulación exacta de vector de estado que aun así dan resultados utilizables en hardware ruidoso; esos circuitos son "a escala de utilidad", mientras que la ventaja cuántica se plantea como objetivo a más largo plazo [@ibm-quantum-learning, "Utility I"]. El experimento de referencia simula la dinámica temporal del modelo de Ising de campo transversal 2D con Trotter de primer orden, en 127 qubits y 60 capas (20 pasos), con el observable `⟨Z₆₂⟩`, y usa ZNE con amplificación probabilística de errores (PEA) [@ibm-quantum-learning, "Utility I"]. Kim et al. (2023) usaron ZNE con 127 qubits y 60 capas de puertas de dos qubits, en acuerdo con la simulación clásica [@cai-2023, Sec. III.A, p. 7]. Es una ilustración de qué es NISQ en su mejor versión: circuitos de la escala que toleran el ruido y observables elegidos con cuidado. También de sus límites: ruido que distorsiona fuertemente incluso en 27 qubits, PEA experimental y lenta, resultados que dependen del estado del dispositivo [@ibm-quantum-learning, "Utility I"], y sobrecargas de mitigación (ZNE ~3×, PEC exponencial en la profundidad) que acotan lo práctico [@qiskit-docs, /guides/error-mitigation-and-suppression-techniques]. El experimento Qedma QESEM de 136 qubits sobre un circuito de Ising con patada se conoce solo por un fragmento de búsqueda y no se ha leído [@qiskit-docs, /guides/qedma-qesem].

**Reglas de diseño para un programador NISQ.**

- *Presupuesto de puertas:* calcula `λ ≈ p·G` con el recuento de puertas de dos qubits tras [transpilar](transpilation.md) (no antes: el routing añade `SWAP`s), y decide si el circuito es viable sin mitigación, con mitigación barata (lectura, DD, twirling) o inviable.
- *Circuitos poco profundos y problemas locales:* los costes de un VQA deben mantener profundidad y ancillas pequeñas por los errores de puerta, los pocos qubits y las coherencias cortas [@cerezo-2021, §II.A, p. 3].
- *Diseña pensando en el ruido:* los algoritmos cercanos deben diseñarse con resiliencia al ruido, aunque más resiliencia puede hacer el circuito más fácil de simular clásicamente [@preskill-2018, §6.4, pp. 9-10; §8, p. 15].
- *Aprovecha la estructura:* para algunos problemas solo unos pocos lugares del circuito pueden causar un fallo grave (poca profundidad, o errores tempranos que se disipan), y entonces el circuito supera la regla de `1/G` [@preskill-2018, §6.4, p. 9].

**El debate sobre la "mejor esperanza".** Cerezo et al. afirman que los algoritmos variacionales son la estrategia líder para la ventaja cuántica en dispositivos NISQ, porque un enfoque de optimización puede tener en cuenta todas las restricciones a la vez y mantener circuitos poco profundos; es la opinión de los autores y la revisión misma lista problemas abiertos de entrenabilidad y de eficiencia de medida [@cerezo-2021, resumen, p. 1; §I, p. 1; §IV]. Los campos candidatos son química y materiales, física nuclear y de partículas, optimización con QAOA y aprendizaje automático cuántico [@cerezo-2021, §V.A-C, pp. 20-22]. Las condiciones para esa ventaja son evitar mesetas áridas, mantener eficiente el coste de medida y controlar el ruido, y exigen dispositivos mayores y mejores [@cerezo-2021, §IV, p. 15; §V, p. 20; §VI, p. 23]. Preskill, por su parte, dice que no se sabe si QAOA/VQE superarán a los métodos clásicos aproximados bien afinados, y que los dispositivos iniciales pueden quedarse cortos [@preskill-2018, §6.1, p. 8].

**Hacia el final de la era.** La corrección de errores es la base para creer que los ordenadores cuánticos escalan: codifica la información en un estado muy entrelazado para que el entorno no la conozca [@preskill-2018, §2, p. 2; §3.2, p. 4]. Cai et al. describen la mitigación y la corrección como complementarias: la mitigación puede aplicarse además sobre qubits lógicos en una era de tolerancia a fallos temprana, con errores lógicos residuales, y reducir los requisitos de hardware [@cai-2023, Sec. IV.D, p. 26; Sec. V.B, p. 28; Sec. VI, p. 31]. Para una tolerancia a fallos completa, se citan cientos de miles de qubits para problemas científicos clásicamente intratables y millones para los industriales [@cai-2023, Sec. I, p. 2]; la estimación detallada está en [estimación de recursos](../../error-correction/concepts/resource-estimation.md) y el contexto en [teorema del umbral](../../error-correction/concepts/threshold-theorem.md). Preskill propone como objetivo cercano demostrar un qubit con corrección de errores y control mejorado [@preskill-2018, §7, p. 14], algo que retoman los [experimentos con qubits lógicos](../../error-correction/concepts/logical-qubit-experiments.md).

**Cuándo usar NISQ.** Para aprender y prototipar, siempre. Para obtener un resultado útil hoy, la pregunta es si tu problema tolera el presupuesto de puertas y si hay mitigación y verificación suficientes; si no, el código que escribas hoy sigue sirviendo (los circuitos y las primitivas son los mismos) cuando el hardware mejore.
