# LANZAMIENTO: qué hacer, paso a paso

> Para la sesión que lance el proyecto. Lee antes `PROCESO.md` entero. Cada paso termina
> actualizando la tabla de §4 y las notas de sesión de §12 de `PROCESO.md`.

## Paso 1 · Confirmar decisiones con Rafa (F0)

Pregúntale, de una vez, las cuatro de `PROCESO.md` §2.2 (lector, perímetro, publicación, entidades
reales), con la propuesta como opción recomendada. Escribe las respuestas en §2.1 y borra la fila de
§2.2. Si cambia el perímetro, ajusta los briefs afectados antes del paso 2.

## Paso 2 · Lanzar el research (F1)

Seis agentes **en paralelo**, en el mismo mensaje, con el Agent tool:

| Agente | `model` | `description` | `prompt` |
|---|---|---|---|
| R1 | `sonnet` | Research CCD2 directiva | contenido de `investigacion/briefs/r1-directiva.md` |
| R2 | `sonnet` | Research CCD2 transposición | `investigacion/briefs/r2-transposicion-espana.md` |
| R3 | `sonnet` | Research CCD2 derecho español | `investigacion/briefs/r3-marco-espanol.md` |
| R4 | `sonnet` | Research CCD2 solvencia e IA | `investigacion/briefs/r4-solvencia-datos-ia.md` |
| R5 | `sonnet` | Research CCD2 mercado | `investigacion/briefs/r5-mercado-y-comparados.md` |
| R6 | `sonnet` | Research CCD2 posventa | `investigacion/briefs/r6-posventa-y-recobro.md` |

Cómo componer cada `prompt`: una primera línea "Carpeta del proyecto:
/Users/rafa/Documents/Proyectos/Manuales/manual_ccd2/. Lee primero investigacion/briefs/_comun.md y
después sigue este brief:" y a continuación el texto completo del brief. Tipo de agente:
`general-purpose` (necesita WebSearch, WebFetch, Write).

Cuando terminen, comprueba que existen los seis ficheros y que siguen el formato de `_comun.md`. Si
alguno falta o está claramente incompleto, relánzalo con el mismo brief y una línea sobre lo que
faltó.

## Paso 3 · Verificar (F1-bis)

Un agente **Opus** (`model: "opus"`, `general-purpose`) con el contenido de
`investigacion/briefs/v1-verificador-opus.md`, precedido de la misma línea de carpeta.

Con su informe:
1. Copia las seis notas originales a `investigacion/verificacion/originales/`.
2. Aplica las correcciones de la tabla del informe a las notas (añade al final de cada nota un
   apartado "Correcciones de V1 (fecha)").
3. Rellena "Hallazgos que cambian el plan" en `investigacion/README.md`.
4. Resume a Rafa: veredicto por nota, correcciones importantes, cambios que propones al índice.

## Paso 4 · Índice (F2)

Sube `00-indice-manual-ccd2.md` a v0.2 con lo verificado: corrige los números de artículo (el v0.1
los tiene de memoria), mueve o añade capítulos según los hallazgos. Enséñaselo a Rafa y espera su
aprobación. Actualiza el resumen de §7 de `PROCESO.md`.

## Paso 5 · Base (F3)

Como en `manual_st`: `estilo.css` con un acento de color propio (ni el del IRB ni el azul del de
*stress test*), `index.html`, `parte-00.html`, `herramientas/revision.py` adaptado a las partes de este
manual (revisar las listas de ficheros que espera). Verificación visual en claro y oscuro.

## Paso 6 · Parte IV con el especialista (F4-E)

Un agente **Opus** (`model: "opus"`, `general-purpose`) con el contenido de
`especialista/brief-especialista-modelos.md`, precedido de la línea de carpeta. Puede ir en paralelo
a la redacción de las Partes I y II por la sesión principal (no comparten ficheros). Antes, crea el
`.venv` (`python3 -m venv .venv` y `.venv/bin/pip install numpy pandas scipy scikit-learn`).

Al volver: `revision.py`, ejecuta S2 y S3 y comprueba que las cifras del texto coinciden, revisa voz
y remisiones. Discrepancias de fondo → a `especialista/decisiones-parte-04.md` y a Rafa.

## Paso 7 · Resto de la redacción, anexos, revisión y publicación (F4-F7)

Igual que en `manual_st` (ver su `PROCESO.md` §4 y §9-10): una parte por paso, `revision.py` tras
cada una, S1 ejecutado antes de citar TAE, inventario de QUÉ VIENE, revisión de fugas, `manual-completo.html`,
EPUB y AZW3 con Calibre, portada nueva. Publicar en GitHub **solo** si Rafa lo pide.

## Recordatorios

- Commits en este repo al cerrar cada fase. Sin remoto salvo petición expresa.
- Al cerrar cada fase, actualiza también la nota del vault
  `/Users/rafa/Documents/Second_brain/work/projects/2026-manual-ccd2.md` (estado con fecha).
- Nada de este proyecto se sube ni se pega en servicios externos sin que Rafa lo pida.
