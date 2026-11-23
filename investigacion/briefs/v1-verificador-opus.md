# Brief V1 · Verificación del research (F1-bis)

**Agente:** Opus 5.5 (`model: "opus"`). Se lanza **cuando las seis notas R1-R6 existen**.
**Salida:** `investigacion/verificacion/informe-v1.md`.

## Contexto

Seis agentes Sonnet han escrito el research de un manual sobre la Directiva (UE) 2023/2225 (CCD2) y
su aplicación en España. Tu trabajo es verificarlo antes de que se cierre el índice del libro. Eres
crítico, no complaciente: un error aquí se hereda en todo el manual.

Lee primero `PROCESO.md` y `investigacion/briefs/_comun.md` (las reglas que tenían que seguir) y el
brief de cada nota en `investigacion/briefs/`. Carpeta:
`/Users/rafa/Documents/Proyectos/Manuales/manual_ccd2/`.

## Qué tienes que hacer

1. **Todas las afirmaciones `[Certain]`** de las seis notas: comprueba contra la fuente primaria
   citada que dice lo que la nota dice. Prioriza: números de artículo, fechas, números de sentencia,
   estado de la transposición, cifras.
2. **Una muestra de las `[Likely]`** (al menos un tercio, empezando por las que más pesan en el
   índice): ¿se puede subir a `[Certain]` con fuente primaria? ¿Hay que bajarla?
3. **Contradicciones entre notas** (por ejemplo, R1 y R6 numerando distinto un artículo, o R2 y R3
   con fechas distintas de la Ley 10/2025).
4. **Cumplimiento de los briefs:** qué pidió cada brief y no se hizo.
5. **Lo que falta y es crítico** para el índice, con dónde buscarlo.
6. Atención especial a **R2** (estado de la transposición, que caduca) y **R4** (la usará un
   especialista para la Parte IV; un error normativo ahí invalida el capítulo).

## Formato del informe

```markdown
# Informe de verificación V1 · Research CCD2

**Fecha:** YYYY-MM-DD · **Agente:** Opus 5.5

## Veredicto global
Un párrafo por nota: fiable / fiable con correcciones / rehacer.

## Correcciones
Tabla: nota · apartado · afirmación original · veredicto (confirmada / corregida / no verificable /
falsa) · corrección propuesta · fuente primaria (URL).

## Contradicciones entre notas

## Briefs incumplidos

## Huecos críticos para el índice

## Hallazgos que cambian el índice v0.1
```

**No edites las notas.** Las correcciones las aplica la sesión principal a partir de tu tabla.

## Al terminar

Devuelve en no más de 20 líneas: veredicto por nota, número de correcciones por tipo y los cinco
cambios más importantes para el índice.
