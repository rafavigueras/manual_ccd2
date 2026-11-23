# Instrucciones comunes a los agentes de research (R1-R6)

Este fichero lo leen todos los agentes Sonnet de F1 antes de su brief propio.

## Contexto

Estás haciendo el research de un manual de estudio sobre la **Directiva (UE) 2023/2225 de contratos de
crédito al consumo (CCD2) y su aplicación en España**. El manual es para profesionales de banca y de
entidades de *lending*. La carpeta del proyecto es
`/Users/rafa/Documents/Proyectos/Manuales/manual_ccd2/`. El plan está en `PROCESO.md` y el índice
provisional en `00-indice-manual-ccd2.md`: léelos por encima para saber para qué sirve tu nota.

La CCD2 se aplica desde el 20-nov-2026. A fecha del plan (2026-11-23) España no la ha transpuesto:
hay un anteproyecto de ley y un borrador de real decreto aprobados en primera vuelta el 7-ene-2026.
**Compruébalo**, no lo des por bueno.

## Reglas

1. **Fuente primaria primero.** EUR-Lex (en español), BOE, Congreso, Senado, Consejo de Ministros
   (La Moncloa), Ministerio de Consumo, Ministerio de Economía, Banco de España, EBA, CNMC, TJUE
   (curia.europa.eu), CENDOJ (Supremo). Despachos, consultoras y prensa solo como segunda capa y
   marcadas como tal.
2. **Nivel de confianza delante de cada afirmación:**
   - `[Certain]`: lo has leído en la fuente primaria, con URL.
   - `[Likely]`: inferencia fuerte, o fuente secundaria fiable que no has podido contrastar.
   - `[Guessing]`: hueco rellenado con criterio. Úsalo poco y dilo.
   Si la mayor parte de un apartado es `[Likely]` o `[Guessing]`, avísalo al principio del apartado.
3. **Cita exacta.** Número de artículo, apartado y letra; número y fecha de sentencias; código de
   directrices (EBA/GL/AAAA/NN). Si no lo has leído, no lo cites como si lo hubieras leído.
4. **Fecha.** Cada dato que pueda cambiar lleva "(a fecha de YYYY-MM-DD)". La fecha de consulta va
   en la cabecera.
5. **Si falta un dato, di "falta contexto"** y dónde lo has buscado. No lo inventes.
6. **Contradicciones:** si dos fuentes no coinciden, pon las dos, di cuál gana y por qué. Regla:
   la fuente oficial del emisor gana a la prensa si tiene menos de un año; si es más antigua, o no
   hay fuente oficial, gana la más reciente.
7. **No copies texto legal largo.** Resume con tus palabras y cita el artículo. Citas literales de
   menos de 30 palabras solo cuando la redacción exacta importa.
8. **PDFs:** si descargas alguno, guárdalo en `investigacion/fuentes/` con un nombre descriptivo.
9. **No escribas fuera de tu fichero de salida** (y de `fuentes/`).

## Formato de la nota

```markdown
---
type: source
created: YYYY-MM-DD
status: active
freshness: snapshot
tags: [ccd2, research, rN]
---

# RN · Título

**Fecha de consulta:** YYYY-MM-DD
**Agente:** Sonnet 5.5, brief `investigacion/briefs/rN-....md`
**Resumen en cinco líneas:** lo que más importa para el manual.

## 1. … (los apartados que pide tu brief)

## Hallazgos que cambian el índice
Lista corta: qué capítulo del índice v0.1 hay que añadir, quitar o mover, y por qué.

## Huecos
Lo que no has podido verificar, dónde lo buscaste y qué fuente lo cerraría.

## Fuentes
Lista numerada: título, emisor, fecha, URL, si es primaria o secundaria.
```

## Al terminar

Devuelve en tu respuesta final, en no más de 15 líneas: ruta del fichero, número de afirmaciones
por nivel de confianza, los tres hallazgos más importantes y los huecos que bloquean.
