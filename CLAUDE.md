# Sage Mentoring

Herramienta personal de aprendizaje para cualquier tema: investiga fuentes fiables, sintetiza el conocimiento en capas (de lo básico a lo profesional) y valida lo aprendido con preguntas y repaso espaciado. Términos definidos en [CONTEXT.md](CONTEXT.md).

## Problema
Una persona curiosa que quiere aprender a fondo temas muy distintos pierde mucho tiempo encontrando fuentes fiables, cribándolas, unificándolas en un recorrido ordenado y creando pruebas para comprobar lo que retiene. Con Claude ese trabajo de recopilar, curar, estructurar y evaluar puede automatizarse en gran parte.

- **Usuario ahora:** el autor (uso personal).
- **Visión:** herramienta abierta que cualquiera pueda usar y en la que se pueda colaborar.

## MVP (v1)
Tema piloto: **teoría del color**, desde cero hasta nivel profesional.
1. **Tema completo** generado con un procedimiento fijo (skill de Claude Code): mapa de conceptos con prerrequisitos, fuentes clasificadas por fiabilidad, capas 0–3, imágenes y diagramas.
2. **Banco de preguntas** en fichero, vinculadas a concepto, capa y fuente. Es la fuente única para las dos vías siguientes.
3. **Exámenes en el chat** con Claude; los resultados se guardan en ficheros de progreso.
4. **Exportación a Anki** del banco de preguntas para repaso espaciado (AnkiWeb gratis / AnkiMobile en iPhone).

## Hoja de ruta
- Aplicación propia: primero local, después usable desde móvil y web (hoy no hay infraestructura más allá del dispositivo).
- Más temas.
- Motor repetible y automatizado de generación de temas.
- Integración con Obsidian.
- Fuentes robustas ante cambios (edición, copias archivadas, caché local de fuentes abiertas).
- Importar resultados de Anki al progreso.
- Versión en inglés y traducciones a otros idiomas.
- Abrir la herramienta a otras personas y permitir colaborar.

## Restricciones y reglas fijas
- **Toda afirmación con fuente.** Lo que no se respalda se marca "sin verificar" o no se incluye.
- **No reproducir texto protegido:** se resume y se cita.
- **Imágenes:** preferentemente creadas por nosotros; las de terceros solo con licencia compartible (CC / dominio público) y con atribución.
- **Cada pregunta indica su concepto y su fuente.**
- **Contenido del tema separado de los datos personales** (progreso y resultados), para poder compartir temas sin compartir historial.
- **Idioma técnico en inglés:** nombres de ficheros y carpetas, claves, identificadores, configuración y código.
- **Idioma del contenido v1:** español (en `i18n/es/`); términos técnicos en español y en el idioma original; fuentes citadas en su idioma original. La estructura permite variantes de idioma por tema.
- **Sin fecha límite**, a ritmo propio. **Presupuesto:** suscripción Claude Pro; vigilar el consumo de contexto y tokens.
- **No hay infraestructura de despliegue** por ahora; todo en local.

## Formato de datos
Decidido y especificado en [docs/format.md](docs/format.md): `topics/` (contenido compartible, parte común + `i18n/<lang>/`) separado de `learners/` (progreso personal), un fichero por concepto con secciones por capa, índices por capa generados, citas Pandoc, diagramas propios generados por código y registro de intentos en el que solo se añaden líneas.

## Plan de trabajo
1. ~~Alcance del producto~~ y ~~formato de datos~~ (hechos).
2. ~~Skills y herramientas~~ (hechas; `topic-builder` y los tres subagentes probados con el piloto en las fases 1 y 2; `topic-examiner` aún sin probar): `topic-builder` y `topic-examiner` en `.claude/skills/`; subagentes `source-researcher`, `concept-writer` y `question-writer` (Sonnet) en `.claude/agents/`; scripts en `tools/` (`validate_topic.py`, `build_layer_index.py`, `progress.py`; tests: `uv run tools/tests/test_validate_topic.py`). Los scripts se ejecutan con `uv run`; las tareas mecánicas, con scripts y no con modelos.
3. Piloto: teoría del color, en curso: mapa aprobado (enfoque pintura y arte, 7 ámbitos) y ámbito `light-and-vision` hecho. Estado y siguiente paso en `topics/color-theory/research/plan.md`.
4. Exportador a Anki (`tools/`).
5. Aplicación: volver al pipeline Navigate (`architect` → …).
