---
concept: query-model-and-oracles
title: "Modelo de consultas y oráculos"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
En el **modelo de consultas (query model)** la entrada de un problema es una caja negra, un **oráculo (oracle)**, que solo se puede evaluar en argumentos elegidos, y el coste es el número de consultas [@watrous-2025, L5.1, PDF pp. 134-135]. Para consultar en un circuito cuántico se usa la puerta `U_f`, que suma `f(x)` a un registro auxiliar.

### Explicación
En programación normal la entrada se da entera: puedes leerla, recorrerla y analizarla. En este modelo, en cambio, su descripción completa está oculta y la única forma de aprender algo de ella es evaluarla [@watrous-2025, L5.1, PDF p. 134]. Piensa en una función de una biblioteca compilada de la que solo puedes llamar a la API, o en un array enorme al que solo accedes por índice, como en una memoria de acceso aleatorio [@de-wolf-2026, §2.4, p. 29].

Lo que se mide es el número de consultas, cada una a coste unitario, sin contar nada más. Es una medida relacionada con el tiempo de ejecución, pero no es lo mismo [@watrous-2025, L5.1, PDF p. 135]. Las entradas son funciones `f: {0,1}ⁿ → {0,1}ᵐ`: una consulta elige una cadena `x` y recibe `f(x)` [@watrous-2025, L5.1, PDF p. 135].

Los problemas típicos son `OR` (¿hay algún `x` con `f(x)=1`?), `Parity` (¿es par o impar el número de `x` con `f(x)=1`?), `Minimum` y la *búsqueda única* (hay exactamente un `z` con `f(z)=1`; encuéntralo) [@watrous-2025, L5.1, PDF p. 136]. Muchos son **problemas con promesa (promise problems)**: se garantiza algo sobre la entrada y, si no se cumple, el algoritmo puede hacer lo que quiera [@watrous-2025, L5.1, PDF p. 136].

Falta decidir cómo se consulta desde un circuito. La consulta clásica ("dame `f(x)`") no sirve tal cual, porque para algunas `f` la transformación `|x⟩ → |f(x)⟩` no sería unitaria [@watrous-2025, L5.1, PDF pp. 137-138]. La solución es la **puerta de consulta estándar** `U_f`, que deja `x` intacto y suma `f(x)` (con XOR) a un registro auxiliar:

```
U_f |x⟩|y⟩ = |x⟩|y ⊕ f(x)⟩
```

Es determinista, es su propia inversa y es una matriz de permutación, luego es unitaria [@watrous-2025, L5.1, PDF p. 138]. Con `y = 0` el registro auxiliar contiene `f(x)`, igual que la consulta clásica [@aaronson-2018, Lec17, pp. 1-2].

### Ejemplo
Con `n = 2` y una `f` que vale 1 solo en `x = 10`: `U_f|10⟩|0⟩ = |10⟩|1⟩`, y para los otros tres `x` el segundo qubit no cambia (se aplica la definición anterior). Lo nuevo frente a la consulta clásica es que `U_f` también puede recibir una superposición de entradas [@de-wolf-2026, §2.4, p. 29].

### Errores frecuentes
- *"Los `N` bits de la entrada y los `n` bits de dirección son lo mismo."* Hay `N` bits en `x` y `n = log₂ N` bits de dirección que los indexan; es un error de principiante confundirlos [@de-wolf-2026, §2.4, footnote 6, p. 29].

### Para seguir
La capa 2 explica el oráculo de fase y por qué la consulta lleva un registro auxiliar. Para ver el modelo en acción, [Deutsch-Jozsa](deutsch-jozsa.md) resuelve con una sola consulta un problema que clásicamente exige varias.

## Comprensión {#layer-2}

### Idea clave
Un oráculo XOR y un oráculo de fase, `|x⟩ → (−1)^{f(x)}|x⟩`, son equivalentes: cada uno simula al otro sin consultas extra [@aaronson-2018, Lec17, p. 2]. El de fase escribe `f(x)` en el signo de la amplitud, lo que facilita preparar patrones de interferencia [@watrous-2025, L8.2, PDF pp. 240-241].

### Explicación
Cuando `f` es booleana suele ser más cómodo el *oráculo de fase (phase oracle)*. No tiene análogo clásico, pero es muy útil para preparar interferencia [@aaronson-2018, Lec17, p. 2; @watrous-2025, L8.2, PDF pp. 240-241]. Se obtiene de `U_f` con una sola consulta y un qubit auxiliar en `|−⟩` (el truco de [retroceso de fase](phase-kickback.md)); ese qubit queda en `|−⟩` y puede reutilizarse [@watrous-2025, L8.2, PDF pp. 240-241; @de-wolf-2026, §2.4, pp. 29-30].

Esto explica también por qué la consulta estándar lleva un registro auxiliar. Una asignación reversible `|x⟩ → |f(x)⟩` exige que `f` sea inyectiva; e incluso para una `f` inyectiva y fácil de calcular, esa asignación podría no ser eficiente, porque ejecutarla al revés invertiría una función unidireccional. La forma `|x,a⟩ → |x,a⊕f(x)⟩` conserva `x` y no rompe nada [@aaronson-2018, Lec17, pp. 3-4].

Si `f` tiene un circuito booleano pequeño, `U_f` es implementable. La basura que deja el cálculo importa: si quedara entrelazada con el qubit útil, impediría los patrones de interferencia [@aaronson-2018, Lec17, p. 4]. Esto es lo que permite que el algoritmo de [Grover](grover-search.md) funcione con cualquier `f` que tenga un circuito booleano [@watrous-2025, L8.2, PDF p. 239].

El modelo, además, ignora el coste de construir las puertas de consulta: lo considera parte de preparar la entrada, no de resolver el problema. Es un instrumento teórico para mostrar ventajas potenciales, no una contabilidad completa de recursos [@watrous-2025, L5.1, PDF p. 139]. Por eso contar consultas equivale a dar coste unitario a las puertas de consulta y coste cero a las demás (por ejemplo, las Hadamard) [@watrous-2025, L6.2, PDF pp. 173-174].

Con esto se puede dar la definición formal. Un algoritmo de `T` consultas intercala unitarias fijas con el oráculo: `U_T O_x U_{T−1} … O_x U_0 |0…0⟩`. La *complejidad de consultas (query complexity)* de `f` es el mínimo `T` de un algoritmo que da `f(x)` con error `≤ 1/3` para todo `x`. Siempre bastan `N` consultas (consultar todos los bits) [@de-wolf-2026, §11.1, pp. 101-102]. Para error constante, repetir permite pasar de un error a otro sin cambiar el orden de magnitud [@childs-qa, §21.1, p. 97].

### Ejemplo
Para implementar `U_f` a partir de un circuito booleano pequeño de `f`:

1. Se calcula `f` de forma reversible.
2. Se copia la respuesta con `CNOT` (permitido: la respuesta es clásica).
3. Se ejecuta el circuito al revés para borrar la basura.

[@aaronson-2018, Lec17, p. 5; @childs-qa, §1.4, pp. 2-3]

### Errores frecuentes
- *"Una ventaja en consultas es una ventaja de tiempo."* Las separaciones exponenciales con consultas no dan por sí solas separaciones exponenciales en el modelo estándar de circuitos [@de-wolf-2026, §2.4, p. 29]. En el modelo estándar la entrada se da explícita y es "mucho más difícil" demostrar ventajas [@watrous-2025, L6 intro, PDF p. 161].
- *"Los problemas artificiales no sirven."* Sirven: el algoritmo de Shor se inspiró en el de Simon, y los casos extremos muestran el potencial y los límites de la computación cuántica [@watrous-2025, L5.1, PDF pp. 136-137].
- *"El oráculo de fase puede ser solo `|x⟩ → (−1)^{f(x)}|x⟩`, sin más."* Para distinguir `x` de su complemento hace falta incluir una componente sobre la que el oráculo actúe trivialmente (el `b=0` de `(−1)^{b·x_i}|i,b⟩`) [@childs-qa, §21.2, p. 98].

### Para seguir
La capa 3 muestra para qué sirve el modelo en la práctica teórica: demostrar cotas inferiores y saber cuándo fiarse de un resultado de consultas. Antes, [retroceso de fase](phase-kickback.md) detalla el truco del qubit `|−⟩`.

## Profesional {#layer-3}

### Idea clave
La ventaja principal del modelo de consultas es que permite *demostrar* límites, cosa casi imposible con la complejidad de circuitos, que solo admite cotas superiores y cotas inferiores condicionadas a hipótesis de dureza [@aaronson-2018, Lec17, p. 1; @childs-qa, §1.6, p. 3]. Hay que comprobar sus hipótesis antes de fiarse de un resultado.

### Explicación
Las dos herramientas estándar para esas cotas son estas:

- *Método polinómico (polynomial method).* La probabilidad de aceptación de un algoritmo de `t` consultas es un polinomio en los bits de entrada de grado como mucho `2t` (cada consulta sube el grado de la amplitud en 1), de modo que `Q_ε(f) ≥ grado-aproximado(f)/2` [@childs-qa, Lema 21.1, §21.3, pp. 98-99; @aaronson-2018, Lec24, p. 4].
- *Método del adversario (adversary method).* Con la versión simple (Ambainis) la cota es `Ω(√(m₀m₁/(ℓ₀ℓ₁)))`; la versión generalizada, un programa semidefinido, da la complejidad de consultas óptima para todas las funciones booleanas [@de-wolf-2026, §11.3, pp. 105-106; §12.1, pp. 111-114].

Los resultados que se obtienen son estos:

| Problema | Resultado | Fuente |
|---|---|---|
| `OR` de `n` bits | determinista `n`, aleatorio `Θ(n)`; cuántico `Θ(√n)` | [@childs-qa, §21.1, p. 97; §21.6, p. 101] |
| `Parity` de `n` bits | hacen falta `≥ n/2` consultas incluso con error acotado y cuántico; el truco de Deutsch por parejas lo alcanza | [@childs-qa, §21.5, pp. 99-100] |
| Contar exactamente los `x` marcados | `Ω(n)` consultas (determinaría la paridad) | [@childs-qa, §21.5, p. 100] |

Por tanto, en `Parity` no hay ventaja real, solo un factor 2 [@childs-qa, §21.5, pp. 99-100]. Y para toda función total la ventaja cuántica es como mucho de potencia 6 (para las simétricas, cuadrática); los problemas con promesa como Deutsch-Jozsa y Simon quedan fuera de esa cota [@de-wolf-2026, §11.2, p. 104].

El recuento de consultas es un buen indicador para la mayoría de los algoritmos estudiados (Deutsch-Jozsa, Simon, Grover, paseos cuánticos), porque su número total de puertas no es mucho mayor que el de consultas, y hasta el cálculo de periodos de Shor se analiza con pocas consultas a la función periódica [@de-wolf-2026, §11.1, p. 102]. Pero sigue siendo una hipótesis a vigilar, no una garantía.

### Ejemplo
Qué hay que comprobar antes de fiarse de un resultado de consultas:

1. *¿Existe acceso cuántico a `f`?* Aplicar `U_f` sobre superposiciones es una hipótesis real: en Shor casi no importa (una sola consulta cuyo resultado se descarta), pero en Grover sí [@aaronson-2018, Lec22, p. 1]. Para una base de datos física exigiría una memoria cuántica de acceso aleatorio (RAM cuántica), cuya construcción es un problema de hardware aparte [@aaronson-2018, Lec22, p. 2].
2. *¿Cuánto cuesta construir el oráculo?* Es parte del coste real aunque el modelo lo ignore [@watrous-2025, L5.1, PDF p. 139]; si `f` es un circuito booleano, hay que sumar la limpieza de ancillas.
3. *¿Contra qué clásico se compara?* Un algoritmo determinista y uno aleatorio pueden diferir mucho en consultas; la ventaja cuántica debe medirse frente al aleatorio [@shor-mit-2022, L16, p. 4]. Ver [Deutsch-Jozsa](deutsch-jozsa.md).
4. *¿Se pueden usar oráculos de entradas no binarias?* Sí: con alfabeto de tamaño `d`, el oráculo se convierte en `|i,b⟩ → |i, b+x_i mod d⟩` y una transformada de Fourier del segundo registro da la versión de fase [@childs-qa, §21.2, p. 98]. En Simon, una consulta con entradas de `n` bits se simula con `n` consultas binarias, así que el recuento cambia solo por un factor `n` [@de-wolf-2026, §3.1, p. 35].

### Para seguir
El modelo se usa en [Deutsch-Jozsa](deutsch-jozsa.md), [Bernstein-Vazirani y Simon](bernstein-vazirani-and-simon.md) y [Grover](grover-search.md); su alcance como argumento de ventaja se discute en [complejidad cuántica](quantum-complexity.md).
