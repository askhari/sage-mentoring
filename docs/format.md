# Formato de datos

Especificación de cómo se guardan los temas, sus recursos y el progreso de cada persona. Términos en [CONTEXT.md](../CONTEXT.md).

> Los valores de los ejemplos (páginas, textos, autores) son ilustrativos y no contenido verificado.

## Principios

1. **Idioma técnico vs. idioma de contenido.** Nombres de ficheros y carpetas, claves, identificadores y valores de configuración, **en inglés**. Todo lo que lee una persona (títulos, explicaciones, preguntas), **en el idioma del contenido** dentro de `i18n/<lang>/`. Excepción: los títulos de las fuentes se mantienen en su idioma original.
2. **Contenido separado de datos personales.** `topics/` se puede compartir; `learners/` nunca se incluye al compartir un tema.
3. **Parte común + parte por idioma.** La estructura del conocimiento (conceptos, fuentes, recursos, metadatos de preguntas) es común; solo se traduce el texto. Ambas partes se unen por identificadores.
4. **Identificadores estables.** En inglés, minúsculas y con guiones (`color-theory`, `hue`, `q-hue-001`). No cambian al traducir ni al reescribir el texto. El progreso se vincula a ellos.
5. **Cada tema es autocontenido.** Todo lo suyo vive dentro de su carpeta.
6. **Pensado para base de datos.** Cada fichero común equivale a una tabla y los identificadores, a sus relaciones.

## Estructura de primer nivel

```
sage_mentoring/
├── topics/<topic-id>/        # contenido compartible
├── learners/<learner-id>/    # datos personales
├── tools/                    # scripts (exportador a Anki, validadores, generadores de diagramas)
├── docs/                     # documentación
└── .claude/skills/           # procedimiento de generación de temas
```

## Un tema por dentro

```
topics/color-theory/
├── topic.yaml
├── concepts.yaml
├── sources.yaml
├── assets.yaml
├── assets/
│   ├── diagrams/
│   │   ├── src/                  # código que genera los diagramas
│   │   ├── color-wheel.es.svg    # con texto → una versión por idioma
│   │   └── spectrum.svg          # sin texto → versión única
│   └── images/                   # de terceros, solo con licencia compartible
├── questions/
│   └── <domain-id>.yaml          # metadatos de preguntas (común)
├── research/
│   ├── plan.md                   # plan de construcción y registro (decisiones, dudas, log)
│   └── notes/
│       └── <source-id>.md        # notas extraídas de cada fuente
└── i18n/
    └── es/
        ├── topic.yaml            # título, descripción, nombres de capas y de ámbitos
        ├── concepts.yaml         # títulos de los conceptos
        ├── overview.md           # capa 0
        ├── assets.yaml           # texto alternativo y pies de imagen
        ├── domains/
        │   └── <domain-id>/
        │       ├── index.md      # introducción al ámbito
        │       └── concepts/
        │           └── <concept-id>.md
        ├── questions/
        │   └── <domain-id>.yaml  # texto de las preguntas
        └── layers/               # GENERADO: índices por capa
            ├── layer-1.md
            ├── layer-2.md
            └── layer-3.md
```

### `topic.yaml` (común)

```yaml
id: color-theory
version: 1
languages: [es]
license: CC-BY-4.0          # licencia del contenido generado
domains:                    # ámbitos, en orden de estudio
  - perception
  - color-models
  - color-spaces
```

### `concepts.yaml` (común): mapa de conceptos

```yaml
- id: hue
  domain: perception
  first_layer: 1            # capa en la que aparece por primera vez
  prerequisites: [light-spectrum]
```

### `i18n/es/topic.yaml`: textos del tema

```yaml
title: "Teoría del color"
description: "…"
layers:                     # nombres de las capas
  0: "Orientación"
  1: "Fundamentos"
  2: "Comprensión"
  3: "Profesional"
domains:                    # título de cada ámbito de topic.yaml
  perception: "Percepción"
sections:                   # nombres de las subsecciones de la plantilla de capa (format: 2)
  key-idea: "Idea clave"
  explanation: "Explicación"
  example: "Ejemplo"
  pitfalls: "Errores frecuentes"
  disagreements: "Las fuentes discrepan"
  next: "Para seguir"
```

### `i18n/es/concepts.yaml`: títulos de los conceptos

Se escriben en la fase de mapa, antes que el contenido, para poder presentar y revisar el mapa en el idioma del contenido. Un título por concepto de `concepts.yaml`.

```yaml
- id: hue
  title: "Matiz (hue)"
```

Los títulos del frontmatter de los ficheros de concepto (`title`) y de los `index.md` de cada ámbito deben coincidir con estos; si se cambia un título, se cambia en los dos sitios.

### Fichero de concepto: `i18n/es/domains/<domain>/concepts/<concept>.md`

Una sección por capa, desde `first_layer` hasta 3. Cada sección lleva un ancla estable para los índices por capa.

```markdown
---
concept: hue
title: "Matiz (hue)"
---

## Fundamentos {#layer-1}
…

## Comprensión {#layer-2}
…

## Profesional {#layer-3}
…
```

- **Términos técnicos:** en español y con el original entre paréntesis la primera vez que aparecen.
- **Imágenes:** con ruta relativa a `assets/`.

#### Plantilla de capa (`format: 2`)

Todos los temas usan la misma plantilla didáctica dentro de cada capa. Lo fijo es la estructura; lo que va dentro depende del tema (en color, un ejemplo es una mezcla de paleta; en computación cuántica, un cálculo o un fragmento de código). Un fichero la adopta declarando `format: 2` en el frontmatter; los ficheros sin esa clave siguen el formato anterior y el validador solo avisa de que están por migrar.

```markdown
---
concept: complementary-colors
title: "Colores complementarios"
format: 2
---

## Fundamentos {#layer-1}

### Idea clave
Una o dos frases con lo esencial de la capa, con su cita al final [@fuente, p. 1].

### Explicación
La idea desarrollada paso a paso…

### Ejemplo
Un caso resuelto o una situación concreta…

### Errores frecuentes
- *"Creencia errónea."* Por qué no es así…

### Las fuentes discrepan
Qué dice cada fuente y qué se recomienda hacer…

### Para seguir
Qué leer después y por qué.

## Comprensión {#layer-2}
…
```

Subsecciones de cada capa, en este orden (los nombres salen de `sections` en `i18n/<lang>/topic.yaml`):

| Clave | Nombre (es) | ¿Obligatoria? | Para qué |
|---|---|---|---|
| `key-idea` | Idea clave | sí | Lo esencial en una o dos frases (≤ 60 palabras). Quien solo lea esto debe llevarse lo principal. |
| `explanation` | Explicación | sí | La idea desarrollada con un hilo: cada párrafo parte de lo anterior. |
| `example` | Ejemplo | sí | Capa 1: ejemplo cotidiano o de trabajo. Capa 2: caso que muestra el porqué. Capa 3: situación profesional y cómo decidir. |
| `pitfalls` | Errores frecuentes | no | Ideas erróneas habituales y por qué fallan. |
| `disagreements` | Las fuentes discrepan | no | Desacuerdos entre fuentes, cifras que no coinciden, debates abiertos. Así no se mezclan con la explicación. |
| `next` | Para seguir | sí | Una o dos frases: qué leer después (siguiente concepto o siguiente capa) y qué aporta. Hace de puente cuando la capa se lee de forma seguida. |

Dos piezas de la lectura **no se escriben a mano**; las añade `tools/build_reader.py` al generar la versión legible:

- **Antes conviene:** los prerrequisitos de `concepts.yaml`.
- **Compruébalo:** una o dos preguntas del banco para ese concepto y esa capa, con la respuesta plegada.

Reglas de redacción:

- **Se explica la idea, no al autor.** La cita va al final de la frase o del párrafo, nunca a mitad de la frase. Se nombra a un autor solo cuando su postura importa, por ejemplo en *Las fuentes discrepan*. Escribir "Los complementarios se neutralizan en gris [@munsell-1905, ¶61]", no "Munsell explica que…". El validador avisa de las citas a mitad de frase; al final de una celda de tabla son correctas.
- **Cada capa se puede leer seguida.** La capa N de un concepto solo da por sabido lo que hay en las capas ≤ N de sus prerrequisitos. Por tanto, fuera de *Para seguir* solo enlaza a conceptos cuyo `first_layer` sea ≤ N, y nunca a una sección `#layer-M` con M > N. El validador lo comprueba.
- **Sin repetir.** La capa N+1 parte de la N y no la resume de nuevo.

#### Índice del ámbito con `format: 2`

Además de la introducción, el orden de estudio y las lecturas complementarias, el `index.md` de un ámbito con `format: 2` lleva un texto de paso por cada capa en la que el ámbito tiene conceptos:

```markdown
## Fundamentos {#layer-1}
Qué se va a ver en esta capa del ámbito, en qué orden y en qué se apoya (un párrafo).
```

Al leer una capa de forma seguida, este texto abre el ámbito antes de sus conceptos.

### Lectura por capas: `tools/build_reader.py`

El contenido se **guarda por concepto**, porque preguntas, progreso y Anki apuntan a *concepto + capa*. Para **leerlo**, `tools/build_reader.py` monta un documento por capa, en HTML y en Markdown. Cada uno incluye, por ámbito y en orden de estudio: el texto de paso del ámbito, la sección de esa capa de cada concepto, *Antes conviene* y *Compruébalo*. Las citas pasan a notas al pie numeradas (al pasar el cursor por el número se ve la fuente) y al final va la bibliografía. El script no redacta nada: solo monta piezas ya escritas.

```bash
uv run tools/build_reader.py color-theory              # → exports/reader/color-theory/es/{index,layer-1,layer-2,layer-3}.{html,md}
uv run tools/build_reader.py color-theory --layer 1 --out lectura/
```

Necesita `pandoc` (≥ 3) instalado en el sistema. Los enlaces entre conceptos se reescriben para que apunten al documento de la capa que corresponda, y las imágenes se incrustan para que cada HTML sea autocontenido.

El `.md` es Markdown de GitHub (GFM) para leer en cualquier editor, en GitHub o en Obsidian: notas numeradas (`[^1]`), sección *Fuentes* al final y nada de sintaxis de Pandoc. Las imágenes van enlazadas con ruta relativa a `topics/`. Lo limpia el filtro `tools/reader/gfm.lua`.

Las citas se quedan como **claves** (`[@clave, localizador]`) en `topics/`: son el identificador estable que usan el validador, las preguntas y Anki, y la numeración depende del documento que se monte. Los números solo aparecen en las salidas. Para depurar el montaje, `--keep-source` guarda también el Markdown de Pandoc intermedio (`<nombre>.source.md`).

### Índices por capa: `i18n/<lang>/layers/layer-N.md`

Los **genera el procedimiento** cada vez que se crea o actualiza un tema; no se editan a mano. Listan, por ámbito, enlaces a la sección `#layer-N` de cada concepto que la tiene.

## Fuentes y citas

### `sources.yaml` (común)

```yaml
- id: fairchild-2013
  type: textbook            # textbook | course | standard | paper | docs | article
  reliability: A            # A | B | C
  title: "Color Appearance Models"
  authors: ["Mark D. Fairchild"]
  year: 2013
  language: en
  identifiers: { isbn: "978-1-119-96703-3" }   # isbn | doi | url
  access: paid              # open | paid
  accessed: 2026-11-01
  notes: "Solo índice y vista previa accesibles."   # opcional: acceso, cambios de URL, avisos
```

- **Fuentes de pago:** solo se usa lo que es accesible legítimamente (índice, vista previa o extractos, páginas del editor, reseñas). La nota de investigación indica qué se consultó, y cada afirmación se localiza en esa parte (p. ej. "índice, cap. 5" o "reseña de X").

### Citas en el texto (sintaxis Pandoc)

```markdown
El matiz es la dimensión que nombramos "rojo", "verde"… [@fairchild-2013, p. 87].
Afirmación aún no respaldada [unverified].
```

### Notas de investigación: `research/notes/<source-id>.md`

Una nota por fuente, con el mismo id que en `sources.yaml`. Recoge **resumidas** (nunca copiadas) las afirmaciones útiles para el tema, cada una con su localización. Es lo que se usa para redactar; las fuentes en bruto no se vuelven a leer.

```markdown
---
source: fairchild-2013
concepts: [hue, colorfulness]
---

- El matiz se define como … (p. 87) → hue
- Distinción entre colorfulness, chroma y saturation (pp. 88–90) → colorfulness
```

- Cada viñeta es una afirmación y termina en `→ <concept-id>` (o `→ id-a, id-b` si respalda varios conceptos), aunque las viñetas se agrupen bajo encabezados. Así se puede contar qué fuentes respaldan cada concepto; el validador avisa si una nota no tiene flechas o si un concepto de su frontmatter no tiene ninguna viñeta.
- Si de la fuente solo se ha podido leer el índice o el resumen, la nota empieza con una línea `Accessed: …` que lo dice.

Las notas están en el idioma en el que resulte más fiel resumir (normalmente el de la fuente).

### Reglas de citación

- Toda afirmación lleva cita o la marca `[unverified]`.
- Cada `@id` debe existir en `sources.yaml` (validable con un script en `tools/`).
- Nunca se reproduce texto protegido: se resume y se cita.

## Imágenes y diagramas

- **Diagramas propios** en `assets/diagrams/`, generados por código guardado en `assets/diagrams/src/`. Son reproducibles y se traducen regenerándolos.
- **Código compartido:** los cálculos de color que usan varios diagramas (funciones de igualación CIE, XYZ ↔ sRGB, colores espectrales, plantillas de fotopigmento…) viven en un módulo común, `assets/diagrams/src/colormath.py`, que cada generador importa. Solo usa la biblioteca estándar, y cada fórmula indica en su docstring de qué publicación sale.
- **Con texto dentro** → `<id>.<lang>.svg`. **Sin texto** → `<id>.svg`.
- **Imágenes de terceros** en `assets/images/`, solo con licencia CC o de dominio público, y con atribución.

### `assets.yaml` (común)

```yaml
- id: color-wheel
  file: diagrams/color-wheel.{lang}.svg
  origin: own               # own | third-party
  generator: diagrams/src/color_wheel.py
  license: CC-BY-4.0
  concepts: [hue, color-wheel]

- id: newton-prism
  file: images/newton-prism.jpg
  origin: third-party
  author: "…"
  source_url: "…"
  license: public-domain
  concepts: [light-spectrum]
```

### `i18n/es/assets.yaml`

```yaml
- id: color-wheel
  alt: "Rueda de color con doce matices…"
  caption: "Rueda de color RYB tradicional."
```

## Banco de preguntas

### Tipos

| `type` | Uso típico | Corrección | Anki |
|---|---|---|---|
| `single-choice` | capas 1–2 | automática | directa |
| `short-answer` | capa 1 | automática (respuestas aceptadas) | directa |
| `open` | capa 2 | Claude, con `rubric` | tarjeta con respuesta modelo |
| `case` | capa 3 | Claude, con `rubric` | tarjeta con respuesta modelo |

### `questions/<domain>.yaml` (común)

```yaml
- id: q-hue-001
  concept: hue
  layer: 1
  type: single-choice
  sources: [fairchild-2013]
  correct: b
```

### `i18n/es/questions/<domain>.yaml`

```yaml
- id: q-hue-001
  prompt: "¿Qué describe el matiz (hue) de un color?"
  options:
    a: "Lo claro u oscuro que es"
    b: "Su posición en la gama rojo–amarillo–verde–azul"
    c: "Lo intenso o apagado que es"
  explanation: "…"

- id: q-hue-010
  prompt: "Explica por qué…"
  model_answer: "…"
  rubric:
    - "Menciona …"
    - "Relaciona … con …"

- id: q-hue-020           # short-answer
  prompt: "…"
  accepted: ["matiz", "tono"]
```

- El **identificador** es lo que enlaza la pregunta con el progreso: reescribir o traducir el texto no invalida el historial.
- Cada pregunta indica su concepto, su capa y sus fuentes.

## Progreso

```
learners/askhari/
├── profile.yaml
└── progress/
    └── color-theory/
        ├── attempts.jsonl      # registro: solo se añaden líneas
        └── summary.json        # derivado: se recalcula desde el registro
```

### `profile.yaml`

```yaml
id: askhari
language: es
```

### `attempts.jsonl`: una línea por respuesta

```json
{"at":"2026-11-03T19:40:00","question":"q-hue-001","concept":"hue","layer":1,"mode":"chat","lang":"es","result":"correct","score":1.0,"session":"2026-11-03-a"}
```

- `result`: `correct` | `partial` | `incorrect`. `score`: de 0 a 1 (nota parcial en `open`/`case`, con un campo `feedback` opcional).
- `mode`: `chat` en v1; `anki` cuando se importen resultados (hoja de ruta).
- **Nunca se edita ni se borra una línea.** Si cambia el cálculo del dominio, se recalcula `summary.json`.

### `summary.json`

Estado por concepto y por capa (`mastered` | `learning` | `weak` | `new`), con el último repaso y la tasa de acierto. Lo usa Claude para elegir qué preguntar.

### Repaso en v1

En cada examen se priorizan las preguntas falladas y los conceptos que llevan más tiempo sin repasar. El algoritmo FSRS completo queda para la aplicación; en Anki ya viene incorporado.

## Exportación a Anki

`tools/export_anki.py` une la parte común y la de idioma de las preguntas y genera un mazo `.apkg` por tema e idioma, importable en Anki de escritorio, AnkiWeb y AnkiMobile.

```bash
uv run tools/export_anki.py color-theory                 # → exports/anki/color-theory.es.apkg
uv run tools/export_anki.py color-theory --lang es --types single-choice,short-answer --out mazo.apkg
```

- **Solo lee `topics/`:** el mazo no lleva progreso ni nada de `learners/`. `exports/` no se versiona (se regenera).
- **Barajas:** `<título del tema>::<n> <ámbito>`, una subbaraja por ámbito en orden de estudio.
- **Etiquetas jerárquicas** con ids: `sage::<topic>::domain::<id>`, `::layer::<n>`, `::concept::<id>`, `::type::<tipo>`, `::source::<id>`. La capa se filtra por etiqueta.
- **Tarjetas** (un único tipo de nota): `single-choice` muestra las opciones en su orden y, detrás, la correcta y la explicación; `short-answer`, la respuesta principal y las demás aceptadas; `open` y `case`, la respuesta modelo y la rúbrica como lista para autoevaluarse. Al pie, el nombre del concepto, el ámbito, la capa, el id de la pregunta y las fuentes (autores, año, título y URL, o ISBN/DOI).
- **IDs estables:** el GUID de cada nota sale de `(topic, lang, id de pregunta)` y los ids del tipo de nota y de las barajas, de un hash del tema, idioma y ámbito. Reimportar un mazo regenerado actualiza las notas en vez de duplicarlas. No se deben renombrar los ids de pregunta ni cambiar los campos del tipo de nota.
- **Enlace con el progreso:** el primer campo de la nota es `QuestionId`; servirá para importar los resultados de Anki a `attempts.jsonl` con `mode: anki` (hoja de ruta).
- Los textos de las tarjetas (p. ej. «Comprueba que tu respuesta:») están en `LABELS` dentro del script; un idioma nuevo necesita su entrada.
