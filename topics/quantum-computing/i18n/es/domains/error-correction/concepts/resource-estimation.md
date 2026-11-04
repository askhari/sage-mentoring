---
concept: resource-estimation
title: "Estimación de recursos (p. ej., romper RSA)"
format: 2
---

## Profesional {#layer-3}

### Idea clave
Una **estimación de recursos (resource estimation)** traduce un algoritmo en una máquina (qubits físicos y tiempo) a partir de unos supuestos de hardware; es una función de sus hipótesis, y solo se puede leer junto con ellas [@gidney-2025, resumen, p. 1; @fowler-2012, pp. 2-3, 52-53].

### Explicación
Se asumen [las puertas tolerantes a fallos y los estados mágicos](fault-tolerant-gates.md) y [el algoritmo de Shor](../../quantum-algorithms/concepts/shor-algorithm.md). Este concepto empieza en la capa profesional.

Todas las estimaciones de las fuentes siguen la misma cadena, con variaciones:

1. *Del algoritmo al circuito lógico:* número de qubits lógicos y de puertas no Clifford (Toffoli, `T` o `CCZ`). Para Shor, ver [el algoritmo de Shor](../../quantum-algorithms/concepts/shor-algorithm.md).
2. *Del error objetivo a la distancia:* el circuito tiene `L` operaciones por qubit lógico y se necesita que la probabilidad total de fallo sea baja; eso fija el error lógico por ronda y, con `ε_d ≈ A (p/p_th)^((d+1)/2)`, la distancia `d` (ver [teorema del umbral](threshold-theorem.md)).
3. *De la distancia a los qubits:* parches de superficie (`≈ 2d²` cada uno), más las fábricas de estados mágicos (ver [código de superficie](surface-code.md) y [puertas tolerantes a fallos](fault-tolerant-gates.md)).
4. *Del recuento de puertas al tiempo:* ciclo de la máquina, tiempo de reacción del control, cuántas fábricas hay en paralelo.

Dos estimaciones de factorización muestran la cadena con sus supuestos:

| | Fowler *et al.* (2012) | Gidney (2025, preprint v1) |
|---|---|---|
| Tarea | factorizar 2000 bits | factorizar RSA de 2048 bits |
| Error físico | `10⁻³` por paso | `0,1 %` (depolarizante uniforme) |
| Ciclo de código de superficie | 200 ns | 1 µs |
| Tiempo de reacción del control | no consta en las notas | 10 µs |
| Conectividad | vecinos próximos 2D | rejilla cuadrada de vecinos próximos |
| Resultado | ≈ `10⁹` qubits físicos, ≈ 26,7 h | `897 864` qubits ("un millón"), < 1 semana (4,96 días) |

Fuentes: [@fowler-2012, pp. 2, 52-53]; [@gidney-2025, resumen, p. 1; §3.2, pp. 18-20].

Los supuestos de Fowler: `N = 2000`, medida de 100 ns y una Toffoli completada en 3 tiempos de medida con 7 puertas `T`; y un circuito de Shor con `2N` qubits lógicos y `40N³` Toffoli secuenciales [@fowler-2012, pp. 2, 52]. Los de Gidney son los de su artículo de 2019 y, por tanto, la comparación con Gidney-Ekerå 2019 (20 millones de qubits y 8 horas) es a igualdad de hipótesis de hardware [@gidney-2025, resumen, p. 1; §4, p. 21]. Con esa base:

- Qubits: `20 000 000 / 897 864 ≈ 22` veces menos (la fuente habla de ≈ 20×) [@gidney-2025, resumen, p. 1].
- Tiempo: de 8 horas a `4,96 × 24 = 119 h`, unas 15 veces más.
- Volumen espacio-tiempo: `2·10⁷ × 8 h = 1,6·10⁸` qubit-hora frente a `897 864 × 119 h ≈ 1,07·10⁸`: solo ≈ 1,5 veces menos. Es decir, gran parte del recorte de qubits se pagó con tiempo (cálculo propio). Se atribuye el mayor tiempo a más puertas Toffoli y menos fábricas de estados mágicos que en 2019, y el menor número de qubits a la aritmética de residuos aproximada, los códigos de superficie *yoked* para qubits inactivos y el cultivo de estados mágicos [@gidney-2025, resumen, p. 1; §4, p. 21].

Lo que más mueve el resultado son los supuestos:

- *Error físico `p`.* Fowler: de `10⁻³` a `10⁻⁴`, las distancias bajan a 16 y 8 y el total a ≈ 130 millones de qubits, con el mismo tiempo [@fowler-2012, pp. 3, 53].
- *Tiempo de ciclo.* Un ciclo de 2 ms sin añadir qubits tardaría ≈ 30 años [@fowler-2012, pp. 3, 39].
- *Tiempo de reacción del control.* Gidney lo fija en 10 µs; la latencia del decodificador lo determina (ver [decodificación](decoding.md)) [@gidney-2025, resumen, p. 1; @google-2025, p. 6].
- *Conectividad.* Con vecinos próximos 2D: superficie. Con largo alcance (átomos, iones): los qLDPC podrían recortar el coste en órdenes de magnitud [@eisert-2025, Sec. III, p. 4].
- *Modelo de ruido.* Gidney supone ruido depolarizante uniforme; el dispositivo real de Google muestra correlaciones y fugas [@gidney-2025, resumen, p. 1; @google-2025, p. 4].
- *Heurísticas del algoritmo.* Los supuestos 1 y 2 de Gidney no están demostrados [@gidney-2025, §2.1-2.2, pp. 6, 12].
- *Almacenamiento frío.* El rendimiento bajo trabajo en flujo no se simuló en detalle; ~100 000 qubits de holgura [@gidney-2025, §3.2, p. 20].
- *Error de inyección.* Fowler supone 0,5 %, no logrado [@fowler-2012, App. M, p. 52].

Otras estimaciones sirven de referencia:

- `P_L = 10⁻¹¹` (para `10³` qubits lógicos durante `10⁸` pasos) con `p = 10⁻³` pide `d ≈ 19`, unos `10³` qubits físicos por lógico y `10⁶` en total [@eisert-2025, Box 2, p. 5]. Es la escala de aplicaciones útiles: miles de qubits lógicos y miles de millones de operaciones lógicas, con el tiempo de ejecución inflado por rondas de síndrome ruidosas y poco paralelismo lógico [@eisert-2025, Sec. III, p. 4].
- 100 qubits lógicos con superficie de `d = 10` y `p = 0,0008`: error lógico cercano a `10⁻⁶` con 19 900 qubits físicos, más los estados mágicos [@saffman-2025, p. 12].
- Los dispositivos tolerantes a fallos necesitarían cientos de miles de qubits para ciencia clásicamente intratable y millones para problemas industriales [@cai-2023, p. 2]. Ya en 2018 se decía que algoritmos con miles de qubits protegidos (factorizar números de miles de bits) necesitan millones de qubits físicos o más [@preskill-2018, §7, p. 14].
- Memoria de 12 qubits lógicos con 288 qubits (qLDPC) frente a casi 3000 (superficie), con el matiz de las ancillas de acceso y que es memoria sin puertas (ver [código de superficie](surface-code.md)) [@bravyi-2024, pp. 6, 22].
- Extrapolación de Google a `10⁻⁶` con `d = 27` y 1457 qubits [@google-2025, p. 6].

Para leer una estimación, esta lista de comprobación:

1. *Hardware supuesto:* `p`, ciclo, reacción, conectividad. Si cambias uno, la cifra cambia (tabla de arriba).
2. *Qué cuenta como "qubit":* ¿incluye fábricas de estados mágicos, almacenamiento pasivo, holguras? Las fábricas son más del 94 % de los qubits en Fowler [@fowler-2012, pp. 2-3, 53]; en Gidney hay tres regiones.
3. *Qué se compara:* tiempo o volumen espacio-tiempo. Un recorte de qubits puede ser un cambio de tiempo (ver la aritmética arriba).
4. *Qué error lógico objetivo y qué probabilidad de éxito:* `10⁻¹⁵` por ronda frente a 93,3 % de éxito por ejecución [@gidney-2025, §3.2, p. 18].
5. *Qué aproximaciones del algoritmo:* heurísticas sin demostrar, aritmética aproximada [@gidney-2025, §2.1-2.2, pp. 6, 12].
6. *Si es preprint o publicado:* Gidney (2025) es un preprint v1 sin referencia de revista en el momento de consultarlo (4 de noviembre de 2026) [@gidney-2025, nota de acceso]. Fowler es de 2012 y parte de supuestos de hardware distintos (ciclo de 200 ns, otra tarea y otro circuito).
7. *Qué dice el propio autor:* Gidney no ve cómo recortar otro orden de magnitud con las mismas hipótesis y no puede afirmar que 100 000 qubits ruidosos bastasen [@gidney-2025, §4, p. 21].

Una estimación no es una predicción de fecha. Gidney la presenta como una "señal de referencia" del estado del arte, recuerda que "los ataques siempre mejoran" y respalda los plazos de NIST (deprecar tras 2030 y prohibir tras 2035) no porque espere el ordenador en 2030, sino porque la seguridad no debería depender de que el progreso sea lento [@gidney-2025, §4, p. 21]. Ver [criptografía poscuántica](../../quantum-algorithms/concepts/post-quantum-cryptography.md). Para situarse: el qubit lógico de Google usa 101 qubits físicos (ver [experimentos con qubits lógicos](logical-qubit-experiments.md)) [@google-2025, p. 2]. La estimación de Gidney supone varios cientos de físicos por lógico [@gidney-2025, §3.2, pp. 18-20].

### Ejemplo
Reproducir la cuenta de 2012. Con `N = 2000`: `40N³ = 40 · 8·10⁹ = 3,2·10¹¹` Toffoli secuenciales (la fuente dice ≈ `3·10¹¹`), y `3,2·10¹¹ × 3 × 100 ns = 9,6·10⁴ s ≈ 26,7 h` [@fowler-2012, pp. 2, 52]. La demanda de magia es `7 × 40N³ = 280N³ ≈ 2·10¹²` estados `|A_L⟩`, con un error por estado muy por debajo de `4·10⁻¹³`. Se usan `d₂ = 34` para la segunda etapa y los qubits de cómputo (con `P_L ≈ 3·10⁻¹⁹`) y `d₁ = 17` para la primera. Una "fábrica AA" son unos 800 000 qubits físicos, tarda unas 500 rondas (≈ 100 µs) y produce unos 2 estados; unas 1200 fábricas en paralelo dan `1200 × 800 000 ≈ 10⁹` qubits. Los `4000` qubits lógicos de cómputo con ≈ 14 500 qubits cada uno son `58 millones`, menos del 6 % del total [@fowler-2012, p. 52-53]. El tamaño por qubit lógico sale de `2,5 · 1,25 · (2d)²`, es decir 14 500 para `d = 34` y 3600 para `d = 17` [@fowler-2012, App. M, p. 52].

Reproducir la cuenta de 2025 (código probado). La suma de Gidney es exacta con sus tres regiones: el registro de entrada de 1280 qubits en almacenamiento frío (430 físicos cada uno), 131 qubits lógicos en almacenamiento caliente y una región de cómputo de `7 × 18` parches calientes. Un parche caliente de `d = 25` tiene `2(d+1)² = 1352` qubits [@gidney-2025, §3.2, pp. 18-20, Fig. 6]. El programa también reproduce el 93,3 % de probabilidad de no tener errores lógicos y los 4,96 días:

```python
# Reconstrucción del recuento de qubits físicos de Gidney (2025, arXiv v1), §3.2
hot_patch = 2 * (25 + 1) ** 2          # 1352 qubits físicos por qubit lógico "caliente" (d = 25)
cold = 1280 * 430                      # registro de entrada en almacenamiento frío (códigos yoked)
hot = 131 * hot_patch                  # qubits lógicos en almacenamiento caliente
compute = 7 * 18 * hot_patch           # región de cómputo: 7 x 18 parches calientes
print(hot_patch, cold, hot, compute, cold + hot + compute)

# Tiempo y probabilidad de éxito
rounds = 1600 * 12 * 3600 / 1e-6       # qubits lógicos x segundos / rondas de 1 microsegundo
p_ok = 2.718281828 ** (-rounds * 1e-15)
shots_days = 12.07 * 9.2 / 24
print(f"{rounds:.2e} rondas, P(sin error lógico)={p_ok:.3f}, {shots_days:.2f} d, {shots_days / p_ok:.2f} d")
```

Salida: `1352 550400 177112 170352 897864` y `6.91e+13 rondas, P(sin error lógico)=0.933, 4.63 d, 4.96 d`. Las cifras coinciden con las del artículo: 897 864 qubits, `6,9·10¹³` rondas-qubit lógico, 93,3 % de éxito sin error lógico, 12,07 horas por ejecución, 9,2 ejecuciones esperadas, 4,63 días y 4,96 días tras dividir por la probabilidad de éxito [@gidney-2025, §3.2, pp. 18-20]. Esa estructura enseña cómo se lee una estimación:

- *El presupuesto de error es una restricción de diseño.* Un objetivo de `10⁻¹⁵` por qubit lógico y ronda con `6,9·10¹³` rondas da `6,9·10¹³ × 10⁻¹⁵ = 0,069` fallos esperados, y `e^{−0,069} = 0,933` [cálculo propio sobre @gidney-2025, §3.2, p. 18]. Si exigieras `10⁻¹⁴` el éxito caería a `e^{−0,69} ≈ 0,50`.
- *Cada qubit lógico pasivo es caro.* El almacenamiento frío cuesta 430 por qubit frente a 1352 en caliente (≈ 3× más denso) [@gidney-2025, §3.2, p. 18]. Los 1280 qubits de entrada en frío ocupan `550 400` de los `897 864` qubits: el 61 % (cálculo propio).
- *El tiempo lo marca la producción de estados mágicos.* Las seis fábricas de `CCZ` fijan un período de 25 µs, igual al de cirugía de red con `d = 25` [@gidney-2025, §3.2, p. 20].

### Las fuentes discrepan
Las dos estimaciones de factorización no son comparables a ciegas. Pasar de `10⁹` a `897 864` qubits es unas 1100 veces menos, pero con supuestos de hardware distintos (ciclo de 200 ns frente a 1 µs, otro circuito y otra tarea) (cálculo propio); la comparación a igualdad de supuestos es la que hace Gidney con su propio resultado de 2019 [@gidney-2025, resumen, p. 1; @fowler-2012, pp. 2, 52].

La distancia que pide el error objetivo depende del modelo. Para `10⁻¹⁵` con `p = 10⁻³`: la fórmula de Eisert y Preskill (`A = 0,1`, `p_th = 10⁻²`) da `(d+1)/2 = 14` y `d = 27`; el ajuste de Fowler (`A = 0,03`, `p_th = 0,57 %`) da `d = 35`; Gidney usa `d = 25` (los dos primeros, cálculo propio) [@eisert-2025, Box 2, p. 5; @fowler-2012, p. 11; @gidney-2025, §3.2, p. 18]. Los qubits por parche pasan de `2·25² − 1 = 1249` a `2·35² − 1 = 2449`, casi el doble, solo por la elección del modelo. Por eso una estimación solo vale con su modelo de error adjunto.

### Para seguir
Este es el final del ámbito. Las estimaciones conectan con [hardware](../../quantum-hardware/index.md) (qué `p`, qué ciclo) y con [algoritmos](../../quantum-algorithms/index.md) (cuántas Toffoli).
