# PROCESO: Manual de crédito al consumo (CCD2) en España

> **Léeme primero.** Este archivo existe para que cualquier sesión nueva, con o sin contexto previo,
> pueda retomar el trabajo con el mismo enfoque, la misma voz y las mismas convenciones. Si estás
> empezando una sesión, lee este archivo entero antes de escribir nada. Después lee
> `LANZAMIENTO.md`, que dice exactamente qué hacer a continuación.
>
> Es el tercer manual de la serie, después del *Manual de Capital y Provisiones* (`../manual_irb/`) y
> del *Manual de Stress Test* (`../manual_st/`). Hereda de ellos voz, formato y método. Donde este
> archivo no diga otra cosa, manda `../manual_st/PROCESO.md`, y si este tampoco lo dice,
> `../manual_irb/PROCESO.md`.

---

## 1. Qué estamos construyendo

Un **manual de estudio y referencia sobre la Directiva (UE) 2023/2225 de crédito al consumo (CCD2) y
su aplicación en España**, para profesionales de banca y de entidades de *lending*. El formato final es
AZW3 y EPUB, construidos desde HTML, como los dos manuales anteriores.

**No es** un resumen de despacho ni una transcripción de la directiva artículo por artículo. Es el
manual de **cómo implanta una entidad española una directiva que ya se aplica (20-nov-2026) pero que
España, a fecha de este plan, no ha transpuesto**: qué obliga a hacer, dónde deja margen, qué hace un
banco cuando no hay ley nacional, cómo cambian los productos y los modelos de admisión, y cómo se
defiende la entidad ante el Banco de España, ante un juez o ante un cliente.

### Encargo original (Rafa, 2026-11-23)

> Anteriormente me has ayudado a realizar libros para aprender de temas como los que hay en
> /Users/rafa/Documents/Proyectos/Manuales (es decir, el manual de provisiones y el de Stress test).
> Querría hacer algo similar pero con Consumer Credit Directive 2 (CCD2) en España.

Segundo mensaje, el mismo día:

> - El research lánzalo con agentes Sonnet 5.5 y luego verifica un agente Opus 5.5 el resultado.
> - Me gustaría una sección con los pasos que habría que dar para adaptar los modelos de admisión de
>   consumo a CCD2, esta sección me gustaría que la escribiera un agente especialista en modelos de
>   crédito, de manera que su contenido fuera interesante para un Head of Risk de cualquier banco o
>   entidad de lending de España.
> - Haz el plan completo y expórtalo a una nueva carpeta de proyecto (como los manuales)
>   completamente. Más adelante lanzaré este proyecto así que tiene que estar todo bien guardado.

Esos dos textos son el criterio de aceptación de todo lo que se escriba.

---

## 2. Decisiones

### 2.1 Cerradas (no reabrir sin que Rafa lo pida)

| Decisión | Valor |
|---|---|
| **Research (F1)** | Agentes **Sonnet 5.5** (`model: "sonnet"`) en paralelo, uno por nota, con los briefs de `investigacion/briefs/`. Después, **un agente Opus 5.5** (`model: "opus"`) verifica todas las notas contra fuente primaria y deja su informe en `investigacion/verificacion/`. Las correcciones se aplican a las notas antes de cerrar el índice |
| **Parte de modelos de admisión** | La escribe **un agente especialista en modelos de crédito** (Opus 5.5) con el brief de `especialista/brief-especialista-modelos.md`. Lector objetivo de esa parte: **el Head of Risk de cualquier banco o entidad de *lending* española**. La sesión principal la revisa (voz, remisiones, cifras ejecutadas) pero no le cambia el fondo sin avisar a Rafa |
| **Método** | El de los manuales anteriores: F0 arranque, F1 research, F2 índice a 3 niveles aprobado por Rafa, F3 base, F4 redacción por partes, F5 anexos ejecutados, F6 revisión, F7 publicación |
| **Formato** | Multi-archivo HTML (una parte por fichero) + CSS compartido → Calibre (AZW3 + EPUB) |
| **Anexos ejecutables** | Sí, en Python, **ejecutados antes de publicar**. Ningún número se publica sin haberse ejecutado |
| **Niveles de confianza** | `[Certain]` / `[Likely]` / `[Guessing]` obligatorios en `investigacion/`. En el texto del manual no van etiquetas: lo no verificado se escribe en cualitativo |
| **Idioma y voz** | Los del IRB (§6 de su `PROCESO.md`): español de España, un director de riesgos con quince años de proyecto explicándoselo a alguien capaz |
| **Repositorio** | Git local en esta carpeta, **sin remoto**. Publicar en GitHub (como `manual_st`) solo si Rafa lo pide de forma explícita |
| **Máquina** | Mac. Python con `python3 -m venv .venv` (no hay `uv`). Calibre en `/Applications/calibre.app/Contents/MacOS/` |

### 2.2 Valores por defecto, adoptados al lanzar el proyecto (2026-11-23)

Rafa no contestó a las cuatro preguntas, pero ordenó lanzar el proyecto ("empieza a desarrollar").
Se adoptan los valores por defecto de la columna Propuesta. Reabrir solo si Rafa lo pide.

| Decisión | Propuesta | Alternativa |
|---|---|---|
| **Lector** | Profesional de banca (riesgos, cumplimiento, negocio, producto) que conoce el crédito al consumo como negocio pero **no** la normativa de conducta. El manual lo lleva a experto. La Parte IV, además, está pensada para el Head of Risk | Lector de cumplimiento que ya conoce la Ley 16/2011 |
| **Perímetro** | **Amplio:** CCD2 más usura y *revolving*, solvencia con IA (AI Act, RGPD 22), Ley 10/2025 de atención a la clientela y recobro. En España son inseparables de CCD2 | Solo CCD2 y su transposición |
| **Publicación** | Repo privado local. Decidir en F7 si se sube a GitHub | Público desde el principio, como `manual_st` |
| **Entidades reales** | Con nombre real solo con datos públicos, fuente y fecha. La experiencia de encargos entra anonimizada, como patrón, en los bloques CASO | — |

---

## 3. Estructura de archivos

```
manual_ccd2/
├── PROCESO.md                       ← este archivo
├── LANZAMIENTO.md                   ← qué hacer, paso a paso, al lanzar el proyecto
├── README.md                        ← presentación corta
├── 00-indice-manual-ccd2.md         ← plan de trabajo: índice a 3 niveles (v0.1, provisional hasta F1)
├── investigacion/
│   ├── README.md                    ← qué nota es cuál y qué se espera de cada una
│   ├── briefs/                      ← prompts completos de los seis agentes Sonnet (R1-R6) y del verificador Opus (V1)
│   ├── fuentes/                     ← PDFs descargados (fuera de git)
│   ├── verificacion/                ← informe del agente Opus (F1-bis)
│   └── r1-…md … r6-…md              ← las notas, cuando existan
├── especialista/
│   └── brief-especialista-modelos.md  ← prompt del agente que escribe la Parte IV
├── herramientas/
│   └── revision.py                  ← copia de manual_st, por adaptar en F3
├── anexos/                          ← scripts Python de los anexos (F5)
└── manual/
    ├── estilo.css                   ← copia de manual_st, por cambiar de acento en F3
    ├── kindle-eink.css
    ├── construir_kindle.py          ← copia de manual_st
    └── generar_portada.py           ← copia de manual_st, por rehacer con motivo propio
```

**Regla heredada:** el `.md` del índice es el plan de trabajo (3 niveles); `manual/index.html` será el
índice del libro (2 niveles). Si cambia la estructura, se actualizan ambos.

---

## 4. Estado actual

| Fase | Entregable | Estado |
|---|---|---|
| F0 · Arranque | Carpeta, repo local, este archivo, `LANZAMIENTO.md`, índice v0.1, briefs de research, verificación y especialista, nota de seguimiento en el vault | ✅ 2026-11-23, salvo confirmar §2.2 con Rafa |
| F1 · Research | Seis notas R1-R6 (Sonnet) | ✅ 2026-11-23 |
| F1-bis · Verificación | `investigacion/verificacion/informe-v1.md` (Opus) y notas corregidas | ✅ 2026-11-23 (correcciones aplicadas; hallazgos en `investigacion/README.md`) |
| F2 · Índice a 3 niveles | `00-indice-manual-ccd2.md` v0.2, aprobado por Rafa | ✅ v0.2 aprobado por Rafa, 2026-11-23 |
| F3 · Base | `estilo.css` con acento propio, `index.html`, `parte-00.html`, `revision.py` adaptado | ✅ 2026-11-23 (portada y `construir_kindle` completos en F7) |
| F4 · Redacción | Partes I, II, III, V y VI (sesión principal) | ✅ Partes I, II, III, V y VI redactadas 2026-11-23 (pendiente: OK de Rafa antes de anexos, revisión y publicación) |
| F4-E · Parte IV | Modelos de admisión, por el agente especialista | ✅ 2026-11-23 (revisada por la sesión principal; decisiones de fondo para Rafa en `especialista/decisiones-parte-04.md`) |
| F5 · Anexos de código | S1-S3 ejecutados | ✅ 2026-11-23 (`anexos-codigo.html` con código y salidas) |
| F6 · Revisión | `revision.py` en OK, QUÉ VIENE inventariados, fugas revisadas | ✅ 2026-11-23 |
| F7 · Publicación | `manual-completo.html`, EPUB, AZW3, portada | ✅ generados 2026-11-23; sin publicar (GitHub solo si Rafa lo pide) |

---

## 5. Sistema de bloques

Los nueve de los manuales anteriores, con la misma clase CSS y el mismo marcado
(`<div class="bloque b-x"><span class="etiqueta">…</span>…</div>`): NORMA, POR QUÉ, MARGEN, PALANCA,
TRAMPA, NÚMEROS, CÓDIGO, DEFENSA, QUÉ VIENE. Ajustes propios:

- **NORMA** cita siempre la directiva **y** su equivalente español: el artículo de la Ley 16/2011
  vigente, el del anteproyecto o "sin equivalente". Es lo que más se va a consultar.
- **PALANCA** se lee como impacto en negocio: tasa de aprobación, volumen, margen, coste de
  cumplimiento o exposición a litigios, con orden de magnitud (puntos de aprobación, pb de margen).
- **DEFENSA**: cómo se argumenta ante el Banco de España, un juez, la AEPD o la auditoría interna.
- **Bloque nuevo, CASO** (`b-caso`, reutiliza el CSS del manual de *stress test*): una situación real
  con el supervisor, un juzgado o un cliente. Cuatro tiempos fijos: **qué llega** (requerimiento,
  reclamación, demanda, inspección), **qué hay detrás**, **la respuesta que funciona**, **la que
  empeora las cosas**. Al menos uno por capítulo en las Partes III a VI.

Marcado, anclas (`capN`, `sN-M`, `sN-M-K`), etiquetas vacías autocerradas, notas al pie, tablas en
`tabla-scroll` y esqueleto de parte: idénticos a `../manual_st/PROCESO.md` §5 y `../manual_irb/PROCESO.md`
§5 y §8. Las reglas del bloque QUÉ VIENE también: sin fechas de aplicación firmes ni números de norma
en negociación. En este manual pesan más que en ninguno: la ley española está en tramitación.

**Revisión:** `python3 herramientas/revision.py` desde la raíz, tras cada parte. Verificación visual
con capturas de Chrome sin ancla en la URL, en claro y en oscuro, en `.capturas/` (fuera de git).

---

## 6. Voz y precisión

Remisión íntegra a §6 del `PROCESO.md` del IRB. Añadidos propios de este manual:

- **Directiva frente a ley española.** Cada obligación se escribe diciendo de dónde nace (artículo de
  la directiva), si ya existe en derecho español (Ley 16/2011, Orden EHA/2899/2011, Circular 5/2012…)
  y qué dice el anteproyecto. Nunca "la ley obliga" sin decir cuál.
- **Fechas.** Todo lo que dependa de la tramitación lleva sello "(a fecha de YYYY-MM-DD)". La
  aplicación de CCD2 desde el 20-nov-2026 es firme; la ley española no lo es.
- **Numeración de artículos.** La numeración de la directiva se verifica en F1 contra EUR-Lex en
  español, con la corrección de errores publicada en el DOUE. El índice v0.1 cita artículos de
  memoria y puede tener errores: **no copiar números del índice al texto sin verificarlos**.
- **Jurisprudencia.** Sentencias del TJUE y del Supremo con número y fecha. Si no se ha leído la
  sentencia, se dice lo que "según la doctrina" establece y no se cita el fallo.
- **Sin consejo legal.** El manual explica la norma y su práctica; no sustituye a un dictamen.
  Se dice una vez en la Parte 0 y no se repite en cada capítulo.
- **Wording.** Sin raya (—) en el texto del libro, igual que en las propuestas de Rafa.

---

## 7. Índice

El índice de trabajo a 3 niveles está en `00-indice-manual-ccd2.md` (v0.2, pendiente de aprobación). Se cierra en
F2 con lo que salga del research verificado. Resumen a 2 niveles:

- **Parte 0 · Cómo usar este manual**
- **Parte I · Fundamentos** (N1) — 1 El crédito al consumo en España · 2 Por qué una segunda directiva ·
  3 El mapa normativo · 4 Cómo funciona una directiva que no se ha transpuesto · 5 Un crédito de
  principio a fin
- **Parte II · La directiva** (N2) — 6 Ámbito · 7 Publicidad y comercialización · 8 Información
  precontractual y explicaciones · 9 Solvencia y bases de datos · 10 Contrato, TAE y límites de coste ·
  11 Derechos durante la vida del crédito (con contratos vigentes y descubiertos; el 12 queda fusionado y se renumera en F3) · 13 Dificultades de pago · 14 Prestamistas
  no bancarios, intermediarios y sanciones
- **Parte III · España** (N2) — 15 Estado de la transposición (dos versiones del texto, Cortes disueltas) · 16 El anteproyecto frente a la
  directiva (con reserva de actividad) · 17 Vivir sin ley · 18 Usura y *revolving* · 19 Supervisión de conducta y litigiosidad
- **Parte IV · Adaptar los modelos de admisión** (N2-N3, agente especialista) — 20 a 26
- **Parte V · Implantación en la entidad** (N3) — 27 El programa · 28 Producto a producto · 29 El
  recorrido digital · 30 Recobro · 31 El impacto en negocio
- **Parte VI · Retos** (N3) — 32 IA en solvencia · 33 *Open banking* (FiDA fuera) · 34 Litigiosidad masiva · 35 Qué viene
- **Anexos de código** — S1 TAE · S2 *scorecard* sintética · S3 prueba de sesgo
- **Anexos de referencia** — R1 glosario · R2 tabla de correspondencia · R3 *checklist* de *gaps* ·
  R4 fuentes · R5 autoevaluación · R6 casos

**Hilo conductor:** una entidad de referencia sintética con tres productos (tarjeta *revolving*,
préstamo personal digital y BNPL en el punto de venta con comercios asociados). Nace en el cap. 5 y
reaparece en las Partes II, IV y V y en los anexos S1-S3.

---

## 8. F1 · Plan de research

Seis agentes Sonnet 5.5 en paralelo, uno por nota. Cada brief completo, listo para pegar como `prompt`
del Agent tool, está en `investigacion/briefs/`. Cada nota se guarda en `investigacion/` con fecha de
consulta, URL de cada fuente y nivel de confianza por afirmación.

| # | Nota | Contenido |
|---|---|---|
| R1 | `r1-directiva.md` | Texto completo de la Directiva 2023/2225 en español, artículo por artículo, con la corrección de errores; comparación con la 2008/48; considerandos clave; fechas (art. 48) |
| R2 | `r2-transposicion-espana.md` | Estado de la transposición en España a fecha de consulta; texto del anteproyecto y del borrador de RD; informe de la CNMC; procedimiento de infracción; qué añade España sobre la directiva |
| R3 | `r3-marco-espanol.md` | Ley 16/2011, Orden EHA/2899/2011, Circular 5/2012, usura y jurisprudencia del Supremo sobre *revolving*, Ley 10/2025, ficheros de solvencia (LOPDGDD art. 20), CIRBE, memoria de reclamaciones del BdE |
| R4 | `r4-solvencia-datos-ia.md` | Arts. 18 y 19 de CCD2; EBA/GL/2020/06 (originación); AI Act anexo III y calendario de alto riesgo; RGPD art. 22 y sentencia SCHUFA (C-634/21); PSD2 y FiDA; expectativas del BdE sobre modelos. **Insumo principal de la Parte IV** |
| R5 | `r5-mercado-y-comparados.md` | Datos del mercado español (volúmenes, *revolving*, BNPL, morosidad, EFC, *fintech*); transposición en otros países de la UE; posiciones de la industria (ASNEF, AEB, EBF) |
| R6 | `r6-posventa-y-recobro.md` | Arts. 35 y 36 y resto de la posventa; cesión de créditos; Directiva 2021/2167 de administradores de créditos y su transposición; prácticas de recobro en España. Reutiliza `knowledge/concepts/collections-2026/03-regulacion.md` del vault como punto de partida |

Después, **V1: un agente Opus 5.5** (`investigacion/briefs/v1-verificador-opus.md`) lee las seis notas,
comprueba contra fuente primaria todas las afirmaciones `[Certain]` y una muestra de las `[Likely]`,
busca contradicciones entre notas y deja `investigacion/verificacion/informe-v1.md` con el veredicto
por afirmación. La sesión principal aplica las correcciones a las notas (conservando la versión
original en `investigacion/verificacion/originales/`) y escribe en `investigacion/README.md` los
hallazgos que cambian el índice. Con eso se pasa a F2.

---

## 9. La Parte IV y el agente especialista

- **Cuándo:** después de F2 (índice aprobado) y antes de redactar la Parte V, que se apoya en ella.
- **Quién:** un agente Opus 5.5 con el papel de especialista en modelos de riesgo de crédito al
  consumo. Brief completo en `especialista/brief-especialista-modelos.md`.
- **Insumos:** este archivo, el índice aprobado, las notas R1, R2 y R4 verificadas, y `manual/estilo.css`
  y `manual/parte-00.html` para el marcado.
- **Salida:** `manual/parte-04.html` completa, el script `anexos/s2_scorecard.py` (y `s3_sesgo.py`)
  ejecutados con sus cifras, y una nota `especialista/decisiones-parte-04.md` con lo que decidió y lo
  que dejó abierto.
- **Revisión:** la sesión principal pasa `revision.py`, comprueba voz y remisiones, y ejecuta los
  scripts. Si discrepa en el fondo, lo anota en `especialista/decisiones-parte-04.md` y lo consulta
  con Rafa en vez de reescribirlo.

---

## 10. Flujo por parte, anexos y publicación

Mismo método que §8-§10 del `PROCESO.md` del IRB y §9-10 del de *stress test*. Los scripts viven en
`anexos/` y se ejecutan con `.venv/bin/python -I anexos/<script>.py` (numpy, pandas, scipy,
scikit-learn). Si se toca un script, hay que revisar el texto que cita sus cifras.

| Anexo | Contenido | Lo usa |
|---|---|---|
| S1 `s1_tae.py` | Cálculo de la TAE según el anexo de la directiva, con los tres productos del hilo conductor, y comparación con los umbrales de usura | Caps. 10 y 18 |
| S2 `s2_scorecard.py` | *Scorecard* sintética de admisión: efecto en aprobación y morosidad de quitar variables no permitidas, añadir una regla de capacidad de pago y usar datos de *open banking* | Parte IV |
| S3 `s3_sesgo.py` | Prueba de sesgo y de disparidad de resultados sobre la *scorecard* de S2 | Caps. 24 y 32 |

## 11. Registro de reparto de contenido

> Cuando un capítulo no desarrolla algo porque le toca a otro, se anota aquí y se deja remisión
> explícita en el texto.

| Tema | Se menciona en | Se desarrolla en | Nota |
|---|---|---|---|
| Art. 18 como norma | Cap. 9 | Cap. 9 (norma) y **Parte IV** (modelos) | El cap. 9 no entra en técnica de modelos |
| Decisiones automatizadas y RGPD 22 | Cap. 9 | **Cap. 23** | |
| AI Act | Cap. 3 | **Caps. 23 y 32** | |
| Arts. 35-36 | Cap. 13 (norma) | **Cap. 30** (operativa de recobro) | |
| Usura | Caps. 3 y 10 | **Cap. 18** | |

## 12. Notas de sesión

- **2026-11-23** — F0. Rafa pide el plan completo y que quede guardado para lanzarlo más adelante.
  Creados carpeta, repo git local (sin remoto), `.gitignore`, este archivo, `LANZAMIENTO.md`,
  `README.md`, índice v0.1, seis briefs de research (Sonnet), el brief del verificador (Opus) y el del
  especialista en modelos (Opus). Copiados de `manual_st` `estilo.css`, `kindle-eink.css`,
  `construir_kindle.py`, `generar_portada.py` y `herramientas/revision.py`, **sin adaptar todavía**.
  Nota de seguimiento en el vault: `work/projects/2026-manual-ccd2.md`. Pendiente: confirmar §2.2 con
  Rafa y lanzar F1.
- **2026-11-23** (2) — F1 y F1-bis. Seis agentes Sonnet escribieron R1-R6 (1.707 líneas); ninguna hubo que
  relanzar. El verificador Opus (V1) falló una vez por límite de gasto y se reanudó. Veredicto: las seis
  fiables con correcciones (4 afirmaciones falsas, 17 corregidas, 27 confirmadas, 6 no verificables).
  Correcciones aplicadas al final de cada nota, originales en `investigacion/verificacion/originales/`.
  Hallazgo mayor: Cortes disueltas el 6-oct-2026, elecciones el 29-nov, proyectos caducados; no hay
  transposición antes de 2027. Cambios propuestos al índice en `investigacion/README.md`. **Parado antes
  de F2:** falta el OK de Rafa; luego, índice v0.2.
- **2026-11-23** (3) — F2. Con el OK de Rafa a los cambios, índice subido a v0.2: números de artículo
  verificados, cap. 12 fusionado en 11.7, 11.6 (contratos vigentes), 11.8, 13.5 (dos fechas de la
  tolerancia), 15.0 y reescrito el 15, 16.5 (reserva de actividad), 17.5, 19.2 a QUÉ VIENE, 21.5, 23.1
  con calendario del AI Act, 27.4, 30.4 y 30.5, cap. 33 sin FiDA. Pendiente: aprobación final de Rafa.
- **2026-11-23** (4) — F3. Rafa aprueba el índice v0.2. Acento burdeos `#7b2d4a` (oscuro `#e19ab4`),
  distinto del verde del IRB y del azul de `manual_st`. `index.html` a 2 niveles, `parte-00.html`
  escrita (norma 1, trampa 1, qué viene 1). `revision.py`: etiqueta del bloque CASO es "Caso" y avisa de
  las partes que faltan. `construir_kindle.py`: una sola `parte-03.html` y títulos nuevos. Pendiente de
  F7: portada (`generar_portada.py` sigue con el motivo de stress test). Verificación visual en claro y
  oscuro con copias de CSS incrustado en `.capturas/`. `revision.py`: OK. Parado antes de F4.
- **2026-11-23** (5) — F4. `.venv` creado (numpy, pandas, scipy, scikit-learn). Lanzado el especialista Opus
  para la Parte IV. Mientras, `anexos/s1_tae.py` ejecutado (TAE: tarjeta 23,75 %, préstamo 11,51 %, BNPL
  corto 0 %, BNPL largo 5,63 %) y redactadas la Parte I (caps. 1-5, ~5.700 palabras) y la Parte II (caps.
  6-14, ~6.600 palabras, cap. 12 fusionado en 11.7). Referencias a la Ley 16/2011 contrastadas con el
  consolidado del BOE (corregidas: publicidad art. 9, TAE art. 32; la ley no tiene techo de exclusión,
  solo aplicación parcial sobre 75.000 EUR). `revision.py` OK. Pendiente: volver el especialista, revisar
  S2 y S3, y pedir OK a Rafa antes de III, V y VI.
- **2026-11-23** (6) — F4-E. Vuelve el especialista: `manual/parte-04.html` (caps. 20-26, ~18.500
  palabras, 7 CASO), `anexos/s2_scorecard.py`, `anexos/s3_sesgo.py` y `especialista/decisiones-parte-04.md`.
  Revisión: `revision.py` OK, sin rayas ni asteriscos; S2 y S3 reejecutados (deterministas) y todas las
  cifras con decimales del texto coinciden con la salida (las dos únicas fuera, 0,5 y 0,8 puntos, son
  diferencias de la propia salida). Visual en claro y oscuro OK. Pendiente de Rafa (ver decisiones §3 y
  §5): costes de 26.4 son estimaciones del autor; tres afirmaciones de conocimiento propio por verificar;
  C-203/22 sin leer. Parado antes de las Partes III, V y VI.
- **2026-11-23** (7) — F4 cierre. Redactadas la Parte III (caps. 15-19, ~5.600 palabras), la V (caps.
  27-31, ~4.400) y la VI (caps. 32-35, ~3.100); al menos un CASO por capítulo en III a VI; QUÉ VIENE sin
  fechas firmes; remisiones a la Parte IV en texto. Cifras de la V sacadas de S1 y S2. `revision.py` OK
  tras cada parte. **No se usó el navegador** para cerrar huecos: lo que sigue sin verificar queda en
  cualitativo en el texto y aquí: (1) texto íntegro de las SSTS (628/2015, 149/2020, 258/2023, 154/2025,
  482/2026 y la de préstamo personal de 2026), que van "según notas del CGPJ y comentarios"; (2) texto de
  septiembre del anteproyecto y borrador de RD, citados según CNMC y CES; (3) perfil regulatorio de
  cada operador BNPL (cap. 6.4); (4) BOE del RD 806/2026; (5) art. 21.5 Ley 50/1997 y art. 21.2 LO 3/1980
  (de memoria, marcados "sin verificar"); (6) origen legal de los 50 € de la AEPD; (7) C-203/22, directrices
  de la Comisión sobre sistema de IA y RTS EBA/RTS/2026/05. Pendiente de Rafa: anexos de referencia
  (R1-R6, incluida la tabla de equivalencias CCD2/RGPD/AI Act/GL 2020/06), anexos-codigo.html, revisión
  final de QUÉ VIENE y de fugas, renumeración del cap. 12 y publicación (F5-F7).
- **2026-11-23** (8) — F5-F7. `anexos-codigo.html` (S1, S2 y S3 con código y salida de la última
  ejecución) y `anexos-referencia.html` (R1 glosario, R2 tabla de correspondencia de 50 artículos con
  CCD1, Ley 16/2011 y anteproyecto con versión, R3 checklist, R4 fuentes, R5 autoevaluación, R6 tres
  casos integrados; sin raya en las celdas). Inventario de QUÉ VIENE: 19 bloques, ninguno con fecha de
  aplicación pendiente ni número de norma en negociación (se quitó el número 2026/1744 del bloque de la
  Parte I; las fechas que quedan son de normas ya adoptadas o plazos de la directiva). Revisión de fugas:
  `manual-completo.html` sin rutas locales ni nombres internos; se corrigió una mención al "research del
  manual"; las únicas entidades con nombre son Wizink y Cofidis (sanciones publicadas en el BOE, con
  fecha) y ASNEF, FAES y OCU como posiciones públicas. Portada nueva con las cuatro TAE de S1 frente al
  TEDR; EPUB y AZW3 con Calibre ("Manual de Credito al Consumo (CCD2)"), `revision.py` OK. **Sin
  publicar nada**: pendiente de Rafa decidir si se sube a GitHub (repo privado o público) y si se
  quita la fila de costes de 26.4; sin revisar en un Kindle real. Huecos sin verificar: ver nota (7).

- **2026-11-23** — Publicado a petición de Rafa en repo **privado**: https://github.com/rafavigueras/manual_ccd2 (remoto `origin`). Sin GitHub Pages.

- **2026-11-25** — **Actualización por el Real Decreto-ley 44/2026** (BOE 25-nov-2026, BOE-A-2026-24702), a
  petición de Rafa. Nueva nota `investigacion/r7-rdl-44-2026.md` (lectura directa del BOE; copia en
  `fuentes/R7-…txt`). Cambia la premisa del manual: ya no es "directiva sin ley" sino "norma española
  por tramos (2, 3 y 6 meses) pendiente de convalidación y de reglamento". Cambios: Parte III caps.
  15-17 reescritos (15 · El RDL 44/2026; 16 · El RDL frente a la directiva, con 16.6 consecuencias
  civiles; 17 · La transición, con 17.6 contratos vivos), 18.4 rehecho (topes y usura por tramo; la
  tarjeta de S1 cumple la regla de stock, TIN 21,5 %, pero no el tope de producción, TAE 23,75 %),
  19.2 y autoevaluación; Parte 0 (lead, 0.3.2, 0.3.3, trampa, conversación); Parte I (4.3.1 y
  referencias); Parte II (todos los NORMA con artículo del RDL); Parte IV solo referencias normativas
  (anotado en `especialista/decisiones-parte-04.md` §7); Parte V (calendario, revolving, 30.4, nueva
  30.6 venta de carteras y vulnerables, escenarios de 31.3); Parte VI; anexos R1, R2 (columna RDL en
  la tabla de correspondencia, mapeo propio), R3, R4, R5, R6; S1 reejecutado (constante
  `TOPE_TRANSITORIO_RDL`; cifras sin cambios). Índice v0.3 en `00-indice-manual-ccd2.md` e `index.html`.
  `revision.py` OK; EPUB y AZW3 regenerados; captura de la Parte III en `.capturas/p3-rdl.png`.
  **Sin commit ni push.** Huecos: convalidación, reglamento (segmentos, márgenes, umbral de alto
  coste, FICAC), qué partes de la CCD2 quedan sin transponer, fecha exacta de entrada en vigor.
