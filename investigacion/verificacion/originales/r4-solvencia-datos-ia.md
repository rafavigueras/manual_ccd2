---
type: source
created: 2026-11-23
status: active
freshness: snapshot
tags: [ccd2, research, r4]
---

# R4 · Solvencia, datos, IA y modelos

**Fecha de consulta:** 2026-11-23
**Agente:** Sonnet 5.5, brief `investigacion/briefs/r4-solvencia-datos-ia.md`
**Resumen en cinco líneas:**
1. El art. 18 de la CCD2 exige una evaluación "en profundidad", sobre ingresos y gastos, sin categorías especiales ni redes sociales, y da al consumidor un derecho de intervención humana con tres contenidos (explicación, punto de vista, revisión). El art. 19 regula las bases de datos y prohíbe tratar categorías especiales y datos de redes sociales.
2. El scoring de personas físicas es de alto riesgo (anexo III, punto 5, letra b, AI Act). Las obligaciones de alto riesgo se retrasaron al **2-dic-2027** por el *Digital Omnibus on AI* (Reglamento (UE) 2026/1744, firmado el 8-jul-2026), aprobado y ya en vigor. El calendario "2-ago-2026" que circula en blogs está superado.
3. Tras SCHUFA (C-634/21) el *score* puede ser en sí mismo una decisión automatizada del art. 22 RGPD si el banco se apoya "de manera determinante" en él. Eso encaja con el art. 18, apartado 8, CCD2 como medida de garantía. Tras Dun & Bradstreet (C-203/22) la explicación debe permitir entender qué datos y cómo se usaron; un algoritmo no basta.
4. En España ni la ley de crédito al consumo ni la ley de IA están aprobadas, y el 6-oct-2026 se disolvieron las Cortes (elecciones el 29-nov-2026): ambas iniciativas están en riesgo de decaer. La autoridad de vigilancia prevista para el scoring bancario es el **Banco de España**, no la AESIA.
5. No hay guía del Banco de España específica sobre IA o scoring de admisión. El marco supervisor operativo es EBA/GL/2020/06, adoptada por el Banco de España en julio de 2020, más la carta de mapeo de la EBA (nov-2025): "no hay contradicciones significativas" entre AI Act y normativa bancaria.

**Calidad de las fuentes.** La CCD2, el AI Act, el RGPD, la PSD2, la LOPDGDD, la Ley 15/2022, la Ley 16/2011, EBA/GL/2020/06 y la sentencia SCHUFA están leídos en texto íntegro. El Omnibus de IA está leído en el texto final del Consejo (PE-CONS 30/1/26 REV 1); el número 2026/1744 y la fecha de publicación (24-jul-2026) vienen de fuentes secundarias. La sentencia C-203/22 solo está leída en comunicado de prensa del TJUE y en una nota de la AEPD, no en el texto de la sentencia. El texto del anteproyecto español de crédito al consumo **no se pudo descargar** (error de certificado en la web del Ministerio de Economía); sus artículos 25-30 se citan a través del informe de la CNMC. Los apartados 5, 6 (parcialmente) y 7 tienen mayoría de afirmaciones `[Likely]`; se avisa en cada uno.

---

## 1. CCD2: evaluación de la solvencia y bases de datos (arts. 18 y 19)

Fuente: Directiva (UE) 2023/2225, texto español en DOUE L de 30.10.2023, copia en `fuentes/R4-DOUE-Directiva-2023-2225-es.pdf`. Todo el apartado salvo lo marcado: `[Certain]`.

### 1.1 Artículo 18, apartado por apartado

| Apdo. | Qué dice (resumen propio) |
|---|---|
| 18.1 | Antes de celebrar el contrato, el prestamista hace una "evaluación en profundidad" de la solvencia, **en interés del consumidor**, para prevenir el préstamo irresponsable y el endeudamiento excesivo. |
| 18.2 | Los intermediarios trasladan fielmente al prestamista la información obtenida del consumidor, conforme al RGPD. |
| 18.3, párr. 1 | La evaluación se basa en información pertinente y exacta sobre **ingresos y gastos** y otras circunstancias financieras y económicas, "necesarias y proporcionadas" a naturaleza, duración, valor y riesgos del crédito. Puede incluir prueba de ingresos u otras fuentes de reembolso, activos y pasivos financieros y otros compromisos. **No incluirá categorías especiales (art. 9.1 RGPD).** Fuentes internas o externas, incluido el consumidor; consulta a base de datos del art. 19 "en caso necesario". **Las redes sociales no se consideran fuente externa.** |
| 18.3, párr. 2 | La información se verifica adecuadamente, en caso necesario con documentación verificable de forma independiente. |
| 18.4 | El prestamista establece, documenta y mantiene los procedimientos de evaluación, y documenta y conserva la información del apdo. 3. |
| 18.5 | Solicitud conjunta: evaluación sobre la capacidad de reembolso conjunta. |
| 18.6 | No se pone el crédito a disposición hasta que la evaluación indique que es probable que se cumplan las obligaciones del contrato. |
| 18.7 | No se anula ni se modifica el contrato en detrimento del consumidor por una evaluación mal hecha, salvo que el consumidor haya ocultado o falsificado conscientemente la información. |
| 18.8 | Si la evaluación implica **procesamiento automatizado de datos personales**, el consumidor tiene derecho a solicitar y obtener **intervención humana**, que consiste en: (a) explicación clara y comprensible de la evaluación, incluida la lógica y los riesgos del tratamiento automatizado, su significado y sus efectos en la decisión; (b) expresar su punto de vista; (c) solicitar una revisión de la evaluación y de la decisión de concesión. Hay que informar al consumidor de este derecho. |
| 18.9 | Si se deniega, el prestamista informa **sin demora** y, en su caso, remite a asesoramiento en deudas. "En su caso" debe informar de que la evaluación se basa en tratamiento automatizado, del derecho a evaluación humana y del procedimiento para oponerse. |
| 18.10 | Si se acuerda aumentar el importe total del crédito tras la celebración, reevaluar con información actualizada antes de un aumento "significativo". |
| 18.11 | Los Estados pueden exigir la consulta de la base de datos pertinente. La evaluación **no se basará exclusivamente en el historial crediticio**. |

Observaciones sobre lo que el texto no dice (todas `[Certain]` como lectura del articulado):
- El art. 18 **no fija umbrales por importe** ni distingue regímenes según cuantía. La proporcionalidad entra solo por la fórmula del apdo. 3 ("necesarias y proporcionadas en relación con la naturaleza, la duración, el valor y los riesgos") y por el considerando 54 ("proporcionada"). El ámbito excluye créditos de más de 100 000 EUR salvo reformas de vivienda no hipotecarias (art. 2.2.c y 2.3).
- No define "procesamiento automatizado". No cita el art. 22 RGPD. El art. 3, punto 14, define "elaboración de perfiles" por remisión al art. 4.4 RGPD.
- El art. 18.9 usa "en su caso" para la información sobre automatización; el art. 18.8 impone informar del derecho. Qué es "sin demora" no se concreta.
- El art. 18.11, segunda frase, prohíbe basar la evaluación **exclusivamente** en historial crediticio. No impide que el historial sea un *driver* principal.

### 1.2 Artículo 19, apartado por apartado

- 19.1 y 19.3: acceso transfronterizo no discriminatorio a las bases de datos públicas y privadas.
- 19.2: solo prestamistas **supervisados** y que cumplan plenamente el RGPD acceden a las bases.
- 19.4: las bases de crédito al consumo contendrán al menos moras, tipo de crédito e identidad del prestamista.
- 19.5: prestamistas e intermediarios **no procesarán** categorías especiales ni datos personales obtenidos de redes sociales que puedan contener las bases.
- 19.6: si la denegación se basa en consulta a una base, informar **sin demora indebida y gratuitamente** del resultado, los detalles de la consulta y las categorías de datos tenidas en cuenta.
- 19.7: los proveedores de bases garantizan datos actualizados y exactos; los Estados velan por que se informe al consumidor, a más tardar 30 días después del registro de una mora, y de sus derechos RGPD.
- 19.8: procedimientos de reclamación para impugnar el contenido de las bases.

### 1.3 Otros artículos que tocan la admisión

- **Art. 6 (no discriminación):** las condiciones para obtener crédito no discriminarán por nacionalidad, lugar de residencia ni "cualquier motivo" del art. 21 de la Carta, salvo diferencias "debidamente justificadas por criterios objetivos". `[Certain]`
- **Art. 13 y considerando 46:** si la oferta es personalizada con tratamiento automatizado, hay que informar al consumidor. El considerando 46 añade que el prestamista informa de las fuentes de datos (art. 14.2.f RGPD). `[Certain]` (texto leído).
- **Art. 32, apdos. 2 y 3:** la remuneración del personal no puede impedir actuar en interés del consumidor, y para los responsables de la evaluación de solvencia la remuneración **no dependerá del número o proporción de solicitudes aceptadas** (art. 32.3.b). `[Certain]`
- **Art. 35.1:** no se exige nueva evaluación del art. 18 al reestructurar o refinanciar con modificación de condiciones si el importe total adeudado no aumenta significativamente (considerando 80, igual). `[Certain]`
- **Art. 2.2.l y art. 47:** la CCD2 no se aplica a contratos vigentes a 20-nov-2026 (siguen bajo la Directiva 2008/48/CE), salvo los arts. 23, 24, 25.1 (segunda frase), 25.2, 28 y 39 para los de duración indefinida. El art. 18 **no** está en esa lista. `[Certain]` Que, por tanto, el art. 18.10 no obliga a reevaluar aumentos de límite en contratos de duración indefinida anteriores al 20-nov-2026 es mi inferencia: `[Likely]`.
- **Art. 2.4:** descubierto tácito: se aplica el art. 18 salvo que el Estado decida otra cosa. `[Certain]`
- **Art. 48:** transposición hasta el 20-nov-2025; aplicación desde el 20-nov-2026. `[Certain]`

### 1.4 Considerandos que lo desarrollan

Todos `[Certain]`, texto leído:
- **(53)** el prestamista tiene la responsabilidad de controlar individualmente la solvencia, y puede usar información del consumidor durante toda la relación. Se cita sin perjuicio de la Directiva 2013/36/UE.
- **(54)** evaluación proporcionada, en interés del consumidor; el calendario de reembolso debe adaptarse a la capacidad; la evaluación positiva no limita la libertad contractual del prestamista; los Estados pueden dar orientaciones adicionales, por ejemplo límites préstamo/valor o préstamo/ingresos.
- **(55)** la información incluirá "como mínimo" ingresos y gastos, con gastos corrientes del hogar y compromisos financieros; ejemplos de "datos sanitarios, incluidos los datos sobre cáncer" y de información de redes sociales como excluidos; **remite a las Directrices EBA de 29-may-2020** (EBA/GL/2020/06) para saber qué categorías de datos pueden usarse.
- **(56)** razón de la intervención humana: el AI Act (en la propuesta de 2021) clasifica como alto riesgo estos sistemas. La explicación debe cubrir "las principales variables, la lógica y los riesgos". La revisión "no debe conducir necesariamente a la concesión".
- **(57)** bases de datos: información mínima, prohibición de categorías especiales y redes sociales, aviso de mora en 30 días "por ejemplo enviándoles una advertencia por correo electrónico".
- **(30)** la CCD2 es sin perjuicio del RGPD (minimización, exactitud, limitación de finalidad). **(31)** no discriminación.

### 1.5 Estado de la transposición española del art. 18 y 19 (a fecha de 2026-11-23)

Fuente principal: informe de la CNMC IPN/CNMC/037/26, de 14-sep-2026 (`fuentes/R4-CNMC-IPN-037-26-informe-APL-credito-consumo-2026-09-14.pdf`).
- `[Likely]` El anteproyecto de ley (APL) contiene un capítulo "Información y Análisis de Solvencia" en los arts. 25-30; el art. 28 es la evaluación de solvencia "basada en ingresos y gastos reales", sin base exclusiva en historial crediticio, con consulta a sistemas de información crediticia "en caso necesario"; el art. 29 da derecho a explicación de la lógica en decisiones automatizadas; el art. 30 establece acceso igualitario a la CIR del Banco de España y a ficheros privados (CNMC, págs. 3-4, 10 y 18-19 del informe). No he leído el texto del APL (gap).
- `[Likely]` Los arts. 19 y 20 del APL exigen a los prestamistas de alto coste consultar sistemas de información crediticia antes de conceder (CNMC, sección 3.2.4).
- `[Likely]` El Consejo de Ministros aprobó el APL el 7-ene-2026 (primera vuelta) según La Moncloa y prensa; la nota de Consumo de 24-abr-2026 lo describe como "aprobado recientemente"; el informe de la CNMC de 14-sep-2026 sigue llamándolo anteproyecto. **No hay segunda vuelta confirmada.** R2 debe cerrar esto.
- `[Likely]` El Real Decreto 806/2026, de 5 de octubre (BOE de 6-oct-2026), disolvió las Cortes y convocó elecciones generales para el 29-nov-2026; las nuevas Cámaras se constituyen el 23-dic-2026. Lo he visto en varias fuentes secundarias (INAP, Iustel, LegalToday), no en el BOE. Consecuencia: **la CCD2 se aplica el 20-nov-2026 sin ley española de transposición**. Esto afecta a R2 y al hilo conductor del manual.
- `[Certain]` Derecho vigente hoy (Ley 16/2011): art. 14 (evaluación de solvencia con "información suficiente obtenida por los medios adecuados", consulta de ficheros, y para entidades de crédito además las normas de gestión de riesgos), art. 14.2 (reevaluar antes de aumento significativo) y art. 15 (informar inmediata y gratuitamente del resultado de la consulta si se deniega). Leído en BOE. La Directiva 2008/48/CE queda derogada con efecto desde el 20-nov-2026 (art. 47 CCD2, `[Certain]`). Que la Ley 16/2011 siga vigente en España al no haber ley nueva: `[Likely]` (no he buscado en el BOE una derogación o ley nueva; no hay ninguna que conozca).

---

## 2. EBA/GL/2020/06 sobre concesión y seguimiento de préstamos

Fuente: informe final EBA/GL/2020/06, 29-may-2020 (`fuentes/R4-EBA-GL-2020-06-informe-final-en.pdf`), tabla de cumplimiento actualizada a 21-feb-2022, recuadro 7.3 de la Memoria de Supervisión 2020 del Banco de España.

### 2.1 Contenido relevante (todo `[Certain]`, leído)

- **Ámbito (párrs. 5-9):** entidades según el art. 4.1.3 CRR; la sección 5 (originación) se aplica además a "acreedores" definidos en la CCD (2008/48/CE) y la MCD, salvo el párr. 93. Las secciones 5 y 6 se aplican a préstamos a consumidores y empresas, no a morosos ni refinanciados. Aplicación desde el **30-jun-2021** para préstamos originados desde esa fecha (párrs. 18-22).
- **Información de consumidores (párr. 85):** como mínimo finalidad, empleo, fuente de capacidad de reembolso, composición del hogar y personas a cargo, compromisos financieros y gastos, gastos regulares, garantías y otros mitigantes. El anexo 2 lista datos posibles y admite, "cuando se usen modelos automatizados", otras fuentes de naturaleza económica o financiera "en cumplimiento de la legislación aplicable", en particular la CCD, la MCD y el RGPD.
- **Verificación y documentación (párrs. 87-94):** uso de datos existentes de clientes según RGPD (87), consulta a terceros y bases cumpliendo RGPD (88), comprobaciones razonables si hay dudas de fiabilidad (89), **visión única del cliente** (90), conservar la documentación al menos durante la vida del contrato (94).
- **Consumidores, generalidades (párrs. 95-101):** analizar la capacidad y perspectiva de pago, evitar "undue hardship" y sobreendeudamiento, tener en cuenta compromisos existentes y comportamiento de pago, solicitud conjunta sobre capacidad conjunta (99). El párr. 101 permite "métodos y enfoques adecuados, que pueden incluir modelos", elegidos según nivel de riesgo, tamaño y tipo de préstamo.
- **Préstamo no garantizado a consumidores (párrs. 114-117):** especifica el art. 8 de la Directiva 2008/48/CE; verificar ingresos si son irregulares (115); no basar la capacidad en un aumento significativo esperado de ingresos salvo prueba (116); **análisis de sensibilidad** a eventos negativos (117).
- **Tecnología e innovación (párr. 53):** capturar los riesgos en el marco de gestión, comprensión de la dirección, entender los modelos (trazabilidad, auditabilidad, robustez), "si se requieren explicaciones, considerar un modelo interpretable" (53.d), calidad de datos, **detectar y prevenir sesgos** (53.e), monitorización continua (53.f).
- **Modelos automatizados de evaluación y decisión (párrs. 54-55):** entender metodología, datos, supuestos, limitaciones y salidas; políticas contra el sesgo y de calidad de datos; trazabilidad y auditabilidad; revisión periódica de la calidad de salida incluido *backtesting*; **controles, *overrides* y procedimientos de escalado** dentro del marco de decisión, con juicio experto y límites cuantitativos (54.d); documentación del modelo, incluido el seguimiento de las decisiones automatizadas sobre la calidad de la cartera (55).
- **Infraestructura de datos (párrs. 60-62):** granularidad por préstamo, criterios aplicados en origen, seguimiento de excepciones y *overrides* de rating o scoring (61).
- Las directrices **derogan EBA/GL/2015/11** sobre evaluación de solvencia de consumidores (recuadro 7.3, BdE). `[Certain]`

### 2.2 Qué no hace la GL (lectura, `[Certain]` como ausencia en el texto)

No trata el art. 22 RGPD, el derecho a explicación ni la intervención humana del consumidor, y no menciona las redes sociales como fuente. Predata la CCD2 y el AI Act. El considerando 55 de la CCD2 la usa como referencia sobre datos admisibles.

### 2.3 Aplicación en España

- `[Likely]` El Banco de España consta como "intends to comply" con las directrices "en las fechas de aplicación (párrs. 18-22)" en la tabla de cumplimiento de la EBA (versión de 21-feb-2022). Leí la tabla en una copia de un tercero (Loyens & Loeff), no en la web de la EBA, y no sé si hay versión posterior.
- `[Certain]` Según el recuadro 7.3 de la Memoria de Supervisión 2020 del Banco de España, las directrices "se adoptaron en julio de 2020" y "se aplican íntegramente" a la actividad crediticia de entidades de crédito y establecimientos financieros de crédito; las secciones de originación, precios y garantías también se aplican a entidades de pago y de dinero electrónico que operen en más de una región, respecto de operaciones de la MCD y la CCD. Dice también que tienen "doble ámbito: prudencial y de conducta".
- `[Certain]` La página de guías supervisoras del Banco de España (consulta 2026-11-23) lista EBA/GL/2020/06 entre las guías "adoptadas como propias" en 2020.
- `[Certain]` La página de la EBA marca la GL como "In force" y no figura enmienda tras la CCD2 en lo que leí. El factsheet EBA de 21-nov-2025 dice que la EBA "no ha identificado ninguna necesidad inmediata" de nuevas guías o de revisar las existentes por el AI Act (véase 3.7). La posible revisión de la GL por la CCD2: falta contexto (no he encontrado anuncio).

---

## 3. AI Act (Reglamento (UE) 2024/1689)

Fuente: texto en español del DOUE (`fuentes/R4-DOUE-Reglamento-2024-1689-es.pdf`).

### 3.1 Clasificación

- `[Certain]` Anexo III, punto 5, letra b): "sistemas de IA destinados a ser utilizados para evaluar la solvencia de personas físicas o establecer su calificación crediticia, **salvo los sistemas de IA utilizados al objeto de detectar fraudes financieros**". El considerando 58 explica la razón (acceso a recursos financieros o servicios esenciales, riesgo de discriminación) y repite las exclusiones: detección de fraude y, a efectos prudenciales, cálculo de requisitos de capital de entidades de crédito y seguros.
- `[Certain]` Art. 6.3: un sistema del anexo III puede no ser de alto riesgo si no plantea riesgo importante, por ejemplo por realizar una tarea de procedimiento limitada o preparatoria, pero **"siempre" es de alto riesgo si elabora perfiles de personas físicas** (art. 6.3, último párrafo). Quien aplique la salvedad documenta su evaluación y se registra (art. 6.4, art. 49.2). Un scoring de crédito elabora perfiles (art. 3, punto 52, AI Act, que remite al RGPD), así que en la práctica **no puede acogerse a la salvedad del 6.3**. La última parte es lectura mía: `[Likely]`.
- `[Certain]` Borrador de directrices de la Comisión sobre clasificación de alto riesgo (art. 6.5 AI Act), publicado para consulta el 19-may-2026 (versión leída: copia en la web `table.media`; no he podido bajarla de la Comisión), sección 3.5.3: cubre "evaluar solvencia" y "establecer *credit score*" como usos distintos; basta uno; el *score* de un tercero (por ejemplo una agencia) es alto riesgo aunque el desplegador no sea quien decide (párrs. 295-300 y ejemplos). Un sistema de *pricing* puro no entra en 5(b), pero uno integrado con solvencia sí (párr. 300). Servicios esenciales incluyen préstamos, ampliación de línea o límite de tarjeta; **no** incluyen tarjetas *premium* ni "préstamos especiales, como de ocio o viajes" (párrs. 302-304), y el proveedor debe demostrar que su sistema solo se destina a servicios no esenciales. La excepción de fraude solo opera si el fraude es el uso previsto "principal" (párr. 307); AML/CFT no queda amparado por la excepción (párr. 309). Quedan fuera como no alto riesgo: segmentación de clientes y marketing personalizado si no entran en la solvencia, atención al cliente sobre la solicitud, gestión de reclamaciones posteriores, valoración de garantías y **monitorización de exposiciones para fines prudenciales una vez concedido el crédito**. **Es un borrador, no vinculante**; la versión definitiva debía haberse publicado antes del 2-feb-2026 (art. 6.5) y no he visto confirmación de que esté adoptada. `[Likely]` para su estado actual.
- `[Likely]` Que un *scorecard* logístico clásico sea un "sistema de IA" a efectos del Reglamento depende de la definición del art. 3.1 y de las directrices de la Comisión sobre esa definición (febrero 2025, que no he leído). No lo he podido cerrar. Es una pregunta abierta (apartado 8).

### 3.2 Obligaciones: proveedor y responsable del despliegue

Todo `[Certain]` salvo indicación; texto del Reglamento leído.

- **Proveedor** (quien desarrolla, o hace desarrollar, y comercializa o pone en servicio bajo su nombre): arts. 8-15 (requisitos: gestión de riesgos art. 9, datos y gobernanza de datos art. 10, documentación técnica art. 11, registro de eventos art. 12, transparencia art. 13, supervisión humana art. 14, exactitud, robustez y ciberseguridad art. 15), art. 16 (obligaciones), art. 17 (sistema de gestión de la calidad), evaluación de conformidad por **control interno (anexo VI), sin organismo notificado**, para anexo III puntos 2-8 (art. 43.2), registro (art. 49), vigilancia posterior (art. 72). Una entidad que desarrolla el modelo en casa es proveedor y responsable del despliegue a la vez (así lo explica el factsheet de la EBA).
- **Responsable del despliegue** (art. 26): medidas técnicas y organizativas para usar el sistema según instrucciones (26.1); **supervisión humana encomendada a personas con competencia, formación y autoridad** (26.2); datos de entrada pertinentes y representativos en la medida en que los controle (26.4); vigilar el funcionamiento y comunicar riesgos o incidentes graves (26.5); conservar los *logs* al menos seis meses (26.6); informar a las personas físicas de que se les aplica un sistema de alto riesgo cuando decide o ayuda a decidir sobre ellas (26.11); usar la información del proveedor (art. 13) para la EIPD del art. 35 RGPD (26.9).
- **Derechos de las personas (art. 86):** derecho a "explicaciones claras y significativas" sobre el papel del sistema y los elementos principales de la decisión, si es una decisión del responsable basada en un sistema del anexo III (salvo punto 2) con efectos jurídicos o análogos. No se aplica en la medida en que el derecho esté ya previsto en otro lugar del Derecho de la Unión (art. 86.3). El art. 18.8 CCD2 y el art. 22 RGPD son esos otros lugares. `[Likely]` para esta conclusión de solapamiento.
- **Sinergias para entidades financieras:** para entidades sujetas a gobernanza interna del derecho financiero: se entiende cumplida la obligación de sistema de calidad del proveedor, salvo art. 17.1, letras g), h) e i), si se respeta la gobernanza sectorial (art. 17.4); documentación técnica y *logs* se conservan dentro de la documentación sectorial (arts. 18.3, 19.2, 26.6); vigilancia del art. 26.5 se considera cumplida si se respetan las normas de gobernanza interna del derecho financiero; el art. 9 permite integrar el sistema de gestión de riesgos en los existentes. Art. 74.6: **la autoridad de vigilancia del mercado es la autoridad financiera competente**, en la medida en que la utilización esté directamente relacionada con el servicio financiero.
- **Evaluación de impacto en derechos fundamentales (art. 27):** obligatoria antes de desplegar, para los responsables del despliegue de sistemas del anexo III, punto 5, **letras b) y c)** (solvencia y seguros de vida y salud), sean públicos o privados (art. 27.1). Contenido: procesos, periodo y frecuencia, categorías de personas afectadas, riesgos de perjuicio, supervisión humana, medidas y mecanismos de reclamación. Se notifica el resultado a la autoridad de vigilancia del mercado con el cuestionario modelo (27.3 y 27.5). Puede complementar la EIPD (27.4; el Omnibus lo reformula para permitir remisiones cruzadas). `[Certain]`
- **Sanciones (art. 99.4):** incumplir las obligaciones de proveedores (art. 16) y de responsables del despliegue (art. 26): hasta 15 000 000 EUR o 3 % del volumen de negocios mundial. `[Certain]` Los Estados fijan el régimen (art. 99.1).
- **Datos de sesgo:** el art. 10.5 permite a proveedores tratar excepcionalmente categorías especiales para detectar y corregir sesgos, con condiciones estrictas. El Omnibus añade un nuevo **art. 4a** con régimen propio (condiciones de las letras a-f: no se puede lograr con otros datos, limitaciones de reutilización, no transmisión a terceros, borrado al corregir el sesgo, etc.). `[Certain]` (texto del Omnibus leído). Esto convive con el art. 18.3 CCD2 y 19.5, que prohíben **usar** categorías especiales para evaluar solvencia: el AI Act permite tratarlas para auditar sesgos, no para puntuar. La coordinación entre ambas es mía: `[Likely]`.

### 3.3 Calendario de aplicación (a fecha de 2026-11-23)

- `[Certain]` Texto original (art. 113): aplicación general **2-ago-2026**; art. 6.1 y obligaciones del anexo I, **2-ago-2027**.
- `[Certain]` **El Digital Omnibus on AI ha sido adoptado.** Texto final PE-CONS 30/1/26 REV 1, firmado en Estrasburgo el 8-jul-2026 (`fuentes/R4-Consejo-PE-30-2026-REV1-DigitalOmnibusIA-en.pdf`). Modifica el art. 113, párrafo tercero: el capítulo III, secciones 1, 2 y 3 (incluidos arts. 8-27) se aplica desde **2-dic-2027** a sistemas de alto riesgo del **art. 6.2 y anexo III** y desde **2-ago-2028** a los del art. 6.1 y anexo I. Entrada en vigor: tercer día tras su publicación en el DOUE. Los considerandos fundan el retraso en la falta de normas armonizadas y de autoridades nacionales.
- `[Likely]` Número y fecha: Reglamento (UE) 2026/1744 del Parlamento Europeo y del Consejo, de 8-jul-2026, publicado en el DOUE el 24-jul-2026, en vigor ~27-jul-2026 (Cuatrecasas, artificialintelligenceact.eu; no he abierto EUR-Lex, que bloquea descargas automáticas). El Parlamento adoptó su posición el 16-jun-2026 (P10_TA(2026)0198) y el Consejo cerró el 29-jun-2026 (fuentes secundarias).
- `[Certain]` Art. 111.2 reformulado: los sistemas de alto riesgo comercializados o puestos en servicio **antes de la fecha de aplicación del capítulo III** solo quedan sujetos si, desde esa fecha, sufren **modificaciones significativas de diseño**; los destinados a autoridades públicas deben cumplir antes del 2-ago-2030. Consecuencia para la banca privada (lectura mía, `[Likely]`): un modelo de scoring en producción antes del **2-dic-2027** que no sufra cambios significativos de diseño queda fuera de las obligaciones de alto riesgo, y qué sea un "cambio significativo de diseño" pasa a ser crítico para los reentrenamientos. El Reglamento define "modificación sustancial" (art. 3, punto 23), que no es literalmente la misma expresión que usa el art. 111.2; no he comprobado si la Comisión los equipara.
- `[Certain]` Otros calendarios del Omnibus (no afectan al scoring): marcas de agua del art. 50.2 hasta el 2-dic-2026 para sistemas ya comercializados; nuevas prohibiciones del art. 5.1 (ba, bb) y 1a, 1b desde el 2-dic-2026.

### 3.4 Autoridad de vigilancia en España

- `[Certain]` El art. 74.6 del Reglamento atribuye la vigilancia del mercado de sistemas de alto riesgo usados por entidades financieras reguladas a la autoridad nacional de supervisión financiera. El art. 74.7 permite designar otra autoridad "en las circunstancias apropiadas".
- `[Certain]` El **Proyecto de Ley Orgánica para el buen uso y la gobernanza de la IA** (121/000096), publicado en el BOCG, Congreso, serie A, núm. 97-1, de 12-jun-2026 (`fuentes/R4-BOCG-15-A-97-1-Proyecto-LO-gobernanza-IA.pdf`), designa en su **art. 5.5** al **Banco de España** como autoridad de vigilancia del mercado para los sistemas del anexo III.5.b) usados por entidades de las que sea supervisor competente (art. 7 de la Ley 13/1994), en la medida en que estén directamente relacionados con servicios financieros. El **art. 5.6** designa a la **CNMV** para esos mismos sistemas en el ámbito de operadores bajo la Ley 6/2023; el art. 5.7 a la DGSFP para seguros de vida y salud. La AESIA es autoridad de vigilancia de otros casos (por ejemplo, biometría, anexo III.6 y III.8.a) y punto de contacto único (arts. 5.2 y 6). Régimen sancionador en los arts. 13-41.
- `[Likely]` Entidades de crédito sujetas a supervisión de otra autoridad (por ejemplo, un prestamista no bancario sin supervisor financiero competente para ese servicio) caerían por defecto en la AESIA: no he encontrado el texto que lo diga y es una inferencia del art. 5.2 y del reparto.
- `[Likely]` Estado del proyecto: el Consejo de Ministros lo aprobó el 26-may-2026 (nota de prensa de La Moncloa, no leída; fecha vía búsqueda) y el BOCG lo publicó el 12-jun-2026 con apertura de plazo de enmiendas. Con la disolución de las Cortes (6-oct-2026) el proyecto **probablemente decae** al disolverse las Cámaras (regla general de los reglamentos parlamentarios, que no he comprobado): `[Guessing]`. R2 y el cap. 23 deben tratar el AI Act como directamente aplicable sin ley nacional de designación de autoridades.

### 3.5 Guía de la EBA sobre AI Act y banca

- `[Certain]` Carta del presidente de la EBA a DG FISMA y DG CNECT, **21-nov-2025** (EBA/2025/D/5384), y factsheet "AI Act: implications for the EU banking and payments sector", 21-nov-2025 (`fuentes/R4-EBA-carta-mapping-AI-Act-2025-11.pdf` y `...factsheet...pdf`). Conclusión: "no se han encontrado contradicciones significativas" entre el AI Act y la legislación bancaria y de pagos; son "complementarios"; la EBA no ve necesidad inmediata de nuevas guías; habrá actuaciones de coordinación supervisora en 2026-2027; es explícito que **no constituye guía ni expectativa supervisora**.
- `[Certain]` El anexo de la carta mapea requisitos del AI Act con CCD2, MCD, CRR/CRD, DORA y las GL de la EBA. Ejemplos: art. 86 AI Act ↔ art. 18.8 y 18.9 CCD2; supervisión humana (art. 14) ↔ art. 18.8 y 18.9 CCD2 y art. 174 CRR; sistema de gestión de la calidad (art. 17) ↔ arts. 18.3 y 18.4 CCD2 y párrs. 41, 54, 55, 60, 65 de la GL; FRIA (art. 27) ↔ art. 6 CCD2 (no discriminación); gestión de riesgos (art. 9) ↔ arts. 6 y 18.8-18.9 CCD2. Útil como tabla de equivalencias para la Parte IV.

---

## 4. RGPD art. 22, SCHUFA y Dun & Bradstreet

### 4.1 Art. 22 RGPD (texto leído en DOUE)

`[Certain]` Art. 22.1: derecho a no ser objeto de una decisión "basada únicamente" en tratamiento automatizado, incluida la elaboración de perfiles, con efectos jurídicos o significativamente similares. 22.2: excepciones: (a) necesaria para celebrar o ejecutar un contrato, (b) autorizada por Derecho de la Unión o de un Estado con medidas adecuadas, (c) consentimiento explícito. 22.3: en (a) y (c), como mínimo derecho a obtener **intervención humana**, expresar el punto de vista e **impugnar** la decisión. 22.4: no se basan en categorías especiales del art. 9.1, salvo art. 9.2.a) o g) con garantías.

### 4.2 TJUE, C-634/21, SCHUFA Holding (Scoring), 7-dic-2023 (Sala Primera)

`[Certain]` (texto íntegro en inglés leído; copia en `fuentes/R4-TJUE-C-634-21-SCHUFA-sentencia-en.pdf`; comunicado de prensa 186/23 en `fuentes`).
- Fallo: el art. 22.1 RGPD debe interpretarse en el sentido de que **el establecimiento automatizado, por una agencia de información crediticia, de un valor de probabilidad sobre la capacidad futura de pago constituye "decisión individual automatizada"** cuando un tercero al que se transmite ese valor "se basa de manera determinante" en él ("draws strongly on") para establecer, ejecutar o poner fin a una relación contractual.
- Razonamiento: tres condiciones acumulativas (decisión; basada únicamente en tratamiento automatizado incluido perfilado; efectos jurídicos o análogos), apdos. 42-43. "Decisión" es un concepto amplio que incluye el resultado del cálculo de solvencia (apdos. 44-46). La actividad de SCHUFA es "perfilado" (art. 4.4) (apdo. 47). Si un valor insuficiente lleva "casi siempre" a la denegación del banco, el valor afecta como mínimo significativamente al interesado (apdos. 48-50). El art. 22.1 establece una **prohibición de principio** que no hay que invocar individualmente (apdo. 52).
- Excepciones nacionales (art. 22.2.b): la ley que autorice debe incluir garantías adecuadas, entre ellas procedimientos estadísticos adecuados, minimización de errores y prevención de efectos discriminatorios, y como mínimo intervención humana, punto de vista e impugnación (apdos. 65-66). Esa ley debe respetar además los arts. 5 y 6 RGPD; los Estados no pueden fijar de antemano el resultado de la ponderación del art. 6.1.f (apdos. 67-70).
- Alcance para un banco: el fallo se refiere al proveedor del *score* (una agencia) cuando un tercero decide. La sentencia no analiza el *score* interno del propio banco; que se aplique el mismo criterio cuando el banco puntúa y decide es mi lectura: `[Likely]`.
- Conexión con la CCD2 (lectura mía, `[Likely]`): el art. 18.8 CCD2 se aplica a **cualquier** evaluación con procesamiento automatizado, sin condicionar a que la decisión sea "exclusivamente" automatizada; el art. 22 RGPD solo si la decisión es "únicamente" automatizada. Un proceso con revisión humana real de todos los rechazos puede quedar fuera del art. 22 pero seguirá dentro del art. 18.8.

### 4.3 TJUE, C-203/22, Dun & Bradstreet Austria, 27-feb-2025 (Sala Primera)

- `[Certain]` Comunicado de prensa 22/25 del TJUE (no oficial, `fuentes/R4-TJUE-C-203-22-DunBradstreet-comunicado-es.pdf`): el responsable debe describir "el procedimiento y los principios concretamente aplicados" para que el interesado comprenda **qué datos personales se han usado y cómo**; puede ser adecuado informar de en qué medida una variación de los datos habría llevado a un resultado diferente (explicación contrafáctica); **la mera comunicación de un algoritmo no es una explicación suficiente**; si el responsable alega secretos comerciales o datos de terceros, debe entregar la información supuestamente protegida a la **autoridad de control o al órgano judicial**, que pondera; y el RGPD **se opone** a una norma nacional que excluya en principio el acceso cuando comprometa un secreto comercial.
- `[Certain]` Una nota de la AEPD de 7-oct-2026 (sobre sistemas algorítmicos en el trabajo) resume la sentencia en el mismo sentido: la información significativa debe explicar de forma concisa, transparente e inteligible el procedimiento y los principios efectivamente aplicados, no exige el código fuente, pero no admite explicaciones genéricas o puramente técnicas.
- `[Likely]` Base jurídica de la sentencia: art. 15.1.h RGPD ("información significativa sobre la lógica aplicada"). Los números de apartado y el fallo literal no los he leído (EUR-Lex bloqueó la descarga; ECLI:EU:C:2025:117 según búsquedas). Falta contexto: texto íntegro.

### 4.4 Autoridades de protección de datos

- `[Certain]` AEPD, entrada de blog de 4-mar-2024 "Evaluación de la intervención humana en las decisiones automatizadas": parte de WP251; la intervención solo cuenta si es significativa (revisor con competencia y autoridad real para cambiar el resultado, formación específica, independencia frente a la presión y al sesgo de automatización, medios y tiempo). El grado de participación humana se registra en la EIPD. Menciona SCHUFA.
- `[Certain]` La nota de la AEPD de 7-oct-2026 sostiene que "la presencia formal de una persona no excluye el art. 22" y que hay que vigilar variables sustitutivas ("proxies") de categorías especiales. Está escrita para el ámbito laboral (RD 723/2026) y el criterio es general.
- `[Likely]` CEPD: las Directrices WP251 rev.01 (adoptadas por el WP29 el 6-feb-2018 y asumidas por el CEPD) son la referencia sobre el art. 22. No las he releído. Falta contexto sobre una guía AEPD o CEPD específica de *scoring* crediticio: no la he encontrado (buscado en aepd.es y en la web del CEPD).
- `[Certain]` LOPDGDD, art. 20 (leído en BOE): presunción de licitud de los **sistemas de información crediticia** comunes si los datos son de deudas ciertas, vencidas y exigibles no reclamadas, hay información previa en el contrato o requerimiento, notificación al afectado en 30 días con bloqueo de datos durante ese plazo, conservación mientras persista el impago con máximo de **cinco años** desde el vencimiento, consulta solo si hay relación contractual o solicitud de financiación, e información al afectado si se deniega por la consulta (art. 20.1.a-f); el acreedor y el sistema son corresponsables (20.2); la presunción **no ampara** que el sistema añada otras informaciones "a fin de llevar a cabo un perfilado, en particular mediante la aplicación de técnicas de calificación crediticia" (20.3). Esto limita el *scoring* con datos de bureau más allá del dato de morosidad. Es un hallazgo que el especialista debe tener.

---

## 5. Datos nuevos: PSD2 / acceso a cuentas y FiDA

*Apartado con mayoría de `[Likely]`.*

### 5.1 PSD2

- `[Certain]` Directiva (UE) 2015/2366, art. 67 (leído en DOUE, `fuentes/R4-DOUE-Directiva-2015-2366-PSD2-es.pdf`): el proveedor de servicios de información sobre cuentas (AISP) presta servicios "exclusivamente sobre la base del consentimiento explícito" del usuario (67.2.a), accede solo a las cuentas designadas y sus operaciones (67.2.d), no pide datos de pago sensibles (67.2.e) y **no usa, almacena ni accede a datos para fines distintos del servicio expresamente solicitado por el usuario** (67.2.f). El banco gestor de cuenta trata las peticiones sin discriminación (67.3.b); no se exige contrato entre AISP y banco (67.4). Art. 94.2: los proveedores solo obtienen y tratan los datos necesarios para sus servicios con consentimiento expreso del usuario.
- `[Likely]` Lo que permite: que el solicitante, con consentimiento explícito, comparta su historial de cuenta (ingresos, gastos, recurrentes) con el prestamista **a través de un AISP** (o directamente si el prestamista es AISP autorizado), y que esa información alimente la evaluación de solvencia a petición del propio solicitante. Encaja con el art. 18.3 CCD2: ingresos y gastos reales. 
- `[Likely]` Lo que no permite: reutilizar esos datos para otro fin (por ejemplo modelos de marketing, o un modelo entrenado con datos de terceros sin base propia): 67.2.f. Los datos de cuenta pueden contener categorías especiales inferibles (salud, sindicato, partido político, religión: pagos a ciertas entidades) y datos de terceros (el beneficiario de una transferencia). Esto choca con el art. 18.3 y art. 19.5 CCD2: el prestamista no debe usarlas para evaluar solvencia, por lo que el *feature engineering* sobre transacciones debe filtrarlas. Este razonamiento es mío: `[Guessing]` como aplicación concreta (la norma lo exige; el cómo, no).
- `[Likely]` Directrices 06/2020 del CEPD sobre la interacción entre PSD2 y RGPD, versión final de **15-dic-2020** (fecha `[Certain]` por la web del CEPD; contenido no releído): distinguen el "consentimiento explícito" contractual de PSD2 del consentimiento RGPD y tratan los datos de la "parte silenciosa" y categorías especiales.
- `[Likely]` PSD3 y Reglamento de servicios de pago (PSR): acuerdo político provisional el **27-nov-2025**; textos de compromiso en abril de 2026 y publicación en el DOUE esperada a finales del cuarto trimestre de 2026 (fuentes: DLA Piper, Taylor Wessing, PwC; no he confirmado publicación a fecha de consulta). El acuerdo busca reducir barreras al acceso de AISP y listar obstáculos prohibidos.

### 5.2 FiDA

- `[Certain]` Propuesta de Reglamento de acceso a datos financieros: COM(2023) 360, procedimiento 2023/0205(COD), 28-jun-2023.
- `[Likely]` Estado (2026-11-23): bloqueada desde las negociaciones de 2025 (sin trílogos desde jun-2025 según fuentes secundarias). **El programa de trabajo de la Comisión para 2027, publicado el 4-nov-2026, lista FiDA entre las propuestas que retirará** (fuentes secundarias: The European Post, openbankingtracker, MLex; una afirma que es el punto 5 de 18 del anexo de retiradas; no lo he comprobado en el documento oficial). La retirada formal requiere un proceso. En febrero de 2025 un borrador filtrado ya la incluía y la versión publicada la mantuvo. Para el manual: no contar con FiDA; las referencias a "datos nuevos" para solvencia se limitan a PSD2/PSR y a acuerdos voluntarios.

---

## 6. Expectativas supervisoras sobre modelos de admisión (España y UE)

*Apartado con mayoría de `[Likely]` y varios "falta contexto".*

- `[Certain]` **Banco de España, Memoria de Supervisión 2025** (`fuentes/R4-BdE-Memoria-Supervision-2025.pdf`; fecha de publicación 28-abr-2026 según búsqueda): entre las prioridades de riesgo de crédito para entidades significativas (2025-2027), "crédito al consumo y pymes: inspecciones *in situ*", con la conclusión destacable "**Consumo: modelos internos y aplicación de NIIF 9 con deficiencias**" y "se iniciaron los trabajos para la identificación de buenas prácticas en la concesión de crédito" (esquema 3.1). También refiere trabajo en "la aplicación del reglamento de la Inteligencia Artificial al sistema financiero", y un uso racional de la IA como objetivo supervisor. No hay una guía específica de scoring ni una circular sobre IA: la afirmación de blogs (Creditolab, otros) de una circular del Banco de España en junio de 2026 que exige revisión humana y ausencia de sesgos **no se confirma en ninguna fuente oficial y la trato como no fiable**. Lo mismo con una supuesta sanción de la AEPD de 890 000 EUR por scoring con IA: no verificada.
- `[Certain]` **Guías supervisoras propias del Banco de España** (consulta de la página oficial el 2026-11-23): 2023 "Gobernanza y transparencia del crédito *revolving*"; 2021 criterios de organización de servicios de atención al cliente; 2019 modelos de valoración automatizada de inmuebles. No hay guía sobre IA, scoring o préstamo responsable. EBA/GL/2020/06 aparece como adoptada. Relevante para R3 (la guía de 2023 sobre revolving).
- `[Certain]` **BdE, Circular 1/2026, de 21-oct-2026, sobre la CIR** (BOE de 30-oct-2026, `fuentes/R4-BOE-A-2026-22720-Circular-BdE-1-2026-CIR.pdf`): refunde la Circular 1/2013 y, por la Orden ECM/531/2026, de 27-may-2026, que restablece las previsiones de la Orden ETD/699/2020 del crédito revolvente, fija que el umbral de exención de declaración individualizada baje de 3 000 a **1 000 EUR a partir del 2-ene-2027** (régimen transitorio a 3 000 EUR hasta el 1-ene-2027). La CIR facilita mensualmente a cada entidad los riesgos acumulados de titulares **iguales o superiores a 1 000 EUR**. Entra en vigor a los 20 días de su publicación (cálculo mío: en torno al 19-20-nov-2026, `[Likely]`). Efecto: los micro-préstamos de importe pequeño empiezan a verse en la CIR desde 2027. Es el dato más concreto sobre "datos nuevos" para la solvencia en España.
- `[Likely]` **EBA, informe de seguimiento sobre *machine learning* en modelos IRB**, publicado el 4-ago-2023 (nota de prensa leída; el informe, no): recoge el *feedback* al documento de debate de nov-2021, reitera sus recomendaciones sobre uso prudente del ML en el marco IRB y trata la interacción con el RGPD y el AI Act, pidiendo aclaraciones para reducir incertidumbre jurídica. El código EBA/REP/2023/28 viene de una fuente secundaria.
- `[Likely]` **EBA, informe sobre *big data* y analítica avanzada**, enero de 2020 (EBA/REP/2020/01): no leído en esta ronda; falta contexto. Aparece citado por la bibliografía habitual; verificar.
- `[Certain]` **EBA, carta y factsheet sobre el AI Act**, 21-nov-2025: véase 3.5.
- `[Likely]` BCE: no he encontrado en esta ronda un documento del BCE sobre scoring de admisión de consumo. La Guía del BCE sobre modelos internos y el informe del BCE sobre el *Omnibus* de IA (dictamen de 15-abr-2026 citado por el Parlamento) existen pero no los he leído. Falta contexto.

---

## 7. Interacción con modelos IRB

*Apartado con mayoría de `[Likely]`.*

- `[Certain]` El Reglamento Delegado (UE) 529/2014 regula la materialidad de extensiones y cambios del enfoque IRB. Distingue cambios **materiales** (requieren aprobación), de notificación previa (dos meses antes) y de notificación posterior, con criterios cualitativos en el anexo y umbrales cuantitativos basados en la reducción de APR (informe final EBA/RTS/2026/05, resumen ejecutivo).
- `[Certain]` **Sucesor:** el 30-mar-2026 la EBA publicó el informe final EBA/RTS/2026/05 con proyecto de RTS que **modifica** el Reglamento 529/2014 (mandato del art. 143.5 CRR, tras CRR3, Reglamento (UE) 2024/1623) (`fuentes/R4-EBA-RTS-2026-05-cambios-materiales-modelos-IRB.pdf`). Objetivos: adaptar al CRR3 (se eliminan referencias a renta variable IRB y AMA) y **reducir el número de cambios materiales** reforzando los umbrales cuantitativos; los criterios cualitativos solo hacen material un cambio si rompe el umbral cuantitativo, salvo cambios "tan fundamentales" como un rediseño completo. Se complementará con una revisión del Reglamento Delegado (UE) 2022/439.
- `[Likely]` Estado: el proyecto de RTS se presentó a la Comisión para su adopción y publicación; no he confirmado adopción ni publicación en el DOUE a 2026-11-23. Sigue vigente el 529/2014 hasta entonces. 
- Falta contexto: no he extraído del anexo del RTS qué cambio de un *score* de admisión que es *driver* de PD cuenta como material, de notificación previa o posterior. El informe trata "nueva originación de exposiciones de un tipo ya calificado" como categoría de cambio; el especialista debe leer el anexo.
- `[Certain]` La carta de la EBA mapea para IRB el art. 174 CRR (uso de modelos, juicio humano y *override*), art. 144.1.f, art. 185 y el RD 2022/439 con el art. 14 AI Act.
- `[Likely]` Vínculo (lectura mía): un cambio de modelo de admisión debe pasar por (i) el marco IRB, si el *score* alimenta la PD IRB, (ii) la evaluación de cambio significativo del AI Act y (iii) el art. 18.4 CCD2 (documentar y mantener los procedimientos).

---

## 8. Discriminación

- `[Certain]` Ley 15/2022, integral para la igualdad de trato y la no discriminación (BOE-A-2022-11589, leída): art. 2.1 lista causas, incluidas edad, discapacidad, sexo, origen racial o étnico, enfermedad o condición de salud, predisposición genética, orientación e identidad sexual, **situación socioeconómica** y "cualquier otra condición o circunstancia personal o social"; art. 3.1.k y 3.1.o: ámbito de acceso a bienes y servicios y "inteligencia artificial y gestión masiva de datos"; art. 6.1.b: discriminación indirecta (criterio aparentemente neutro con desventaja particular); art. 17.1: quienes ofrecen bienes y servicios, "tales como servicios financieros", no pueden discriminar en el acceso; art. 17.2: no puede denegarse el acceso a seguros o servicios financieros afines ni establecerse diferencias de trato por esas causas, salvo las proporcionadas a la finalidad y a las condiciones objetivas, en los términos de la normativa de seguros; art. 4.2: no hay discriminación si la diferencia se justifica objetivamente por finalidad legítima y medio adecuado, necesario y proporcionado; art. 30: **inversión de la carga de la prueba** cuando se aportan indicios fundados; art. 48: multas de 300 a 500 000 EUR.
- `[Certain]` **Art. 23 de la Ley 15/2022** ("Inteligencia Artificial y mecanismos de toma de decisión automatizados"): es de contenido programático. Las administraciones públicas "favorecerán" mecanismos de minimización de sesgos, transparencia y rendición de cuentas (23.1), priorizarán la transparencia y la interpretabilidad (23.2), "las administraciones públicas y las empresas **promoverán** el uso de una IA ética, confiable y respetuosa" (23.3) y se promoverá un sello de calidad de algoritmos (23.4). **No impone obligaciones concretas a entidades privadas.** La prohibición real para el scoring viene de los arts. 4, 6 y 17.
- `[Likely]` Variables prohibidas o de riesgo (síntesis, conforme a CCD2, RGPD y Ley 15/2022): (i) **prohibidas para evaluar solvencia**: categorías especiales (origen racial o étnico, opiniones políticas, convicciones religiosas, afiliación sindical, datos genéticos, biométricos, de salud, vida u orientación sexual) (art. 18.3 y 19.5 CCD2 y art. 9 RGPD) y datos de redes sociales (id.); (ii) **no se pueden usar como criterio de diferenciación sin justificación objetiva** las causas del art. 2.1 de la Ley 15/2022 y del art. 21 de la Carta (art. 6 CCD2), incluidos nacionalidad y lugar de residencia; (iii) **efectos indirectos**: variables neutras con efecto desproporcionado (código postal, tipo de contrato, edad) se sujetan a justificación objetiva, adecuación, necesidad y proporcionalidad; (iv) la AEPD pide revisar *proxies*. La lista de variables concretas es del especialista; la norma no las enumera. El criterio de "justificación objetiva" en la CCD2 (art. 6, párr. 2) y en la Ley 15/2022 (art. 4.2) es el mismo test en sustancia, pero por textos distintos: `[Likely]`.
- `[Certain]` Las excepciones por edad en seguros o servicios financieros (art. 17.2 Ley 15/2022) remiten a la normativa de seguros; no hay equivalente expreso para crédito. Falta contexto sobre jurisprudencia española aplicando la Ley 15/2022 a scoring.

---

## Preguntas abiertas para el especialista en modelos

La norma no las resuelve. Las dejo sin responder.
1. ¿Un *scorecard* de regresión logística entra en la definición de "sistema de IA" del art. 3.1 AI Act? ¿Qué cambia entre un *scorecard* clásico y un modelo de *gradient boosting*? (Directrices de la Comisión sobre la definición de IA, feb-2025: no leídas.)
2. ¿Qué es "modificación significativa de diseño" (art. 111.2 y art. 3.23 AI Act) para un reentrenamiento periódico o una recalibración? Define si el modelo en producción antes del 2-dic-2027 queda fuera.
3. ¿Qué nivel de explicación cumple a la vez art. 18.8.a CCD2, art. 86 AI Act y C-203/22: razones principales, explicación contrafáctica, importancia de variables? ¿Cómo se defiende un modelo no lineal?
4. ¿Cuándo la revisión humana es "significativa" (AEPD, 4-mar-2024) en un flujo con *scoring* automático y *cut-off*: tasa de *override*, formación, tiempos, sesgo de automatización? ¿Cómo se mide y evidencia?
5. ¿Qué variables y *proxies* dejan de ser admisibles por el art. 18.3 y 19.5 CCD2, por la Ley 15/2022 y por el art. 9 RGPD? ¿Cómo se prueba la ausencia de efecto discriminatorio indirecto, y cómo se concilia con el uso de categorías especiales solo para auditar sesgo (art. 10.5 y art. 4a AI Act)?
6. *Reject inference* y representatividad de los datos (art. 10 AI Act, párr. 54 GL) cuando se amplía el ámbito de la CCD2 (BNPL, microcréditos).
7. Si el *score* de admisión es *driver* de la PD IRB, ¿qué cambios son "materiales" según el RTS modificado y cómo se coordina con el ciclo de validación del art. 174 CRR?
8. Datos de cuenta (AISP): ¿cómo se filtran transacciones con categorías especiales o de terceros antes de entrenar o puntuar?
9. Regla "no exclusivamente historial crediticio" (art. 18.11 CCD2): ¿qué peso máximo de variables de *bureau* es defendible?
10. Calibración de la capacidad de pago frente a un modelo de PD: ¿debe haber un *cap* de cuota/ingresos independiente del *score*? La CCD2 (considerando 54) deja a los Estados fijar ratios préstamo/ingresos.
11. Remuneración (art. 32.3.b CCD2): ¿cómo se compagina con objetivos de aprobación o *conversion* en el proceso digital?

---

## Hallazgos que cambian el índice

1. **Parte IV y cap. 23 (AI Act):** el calendario base es **2-dic-2027** (Reglamento 2026/1744), no agosto de 2026. Añadir un cuadro del régimen transitorio del art. 111.2 (modelos anteriores y "modificación significativa"). Añadir la figura del Banco de España como autoridad de vigilancia (propuesta, pendiente) y su dependencia de la ley nacional, que corre riesgo de decaer.
2. **Nuevo apartado sobre datos de crédito y CIR:** la Circular 1/2026 del Banco de España (umbral CIR a 1 000 EUR desde 2-ene-2027) y el art. 20 LOPDGDD (límite de cinco años, prohibición de ampararse en la presunción para perfilado). Mover a un capítulo propio de "bases de datos" en la Parte IV o en el cap. 9.
3. **Cap. 3 (mapa normativo):** FiDA se retira (programa de trabajo 2027 de la Comisión, por confirmar); PSD3/PSR pendiente de publicación. Quitar FiDA como pieza del marco y sustituir por PSD2/PSR.
4. **Cap. 3 y cap. 5 (hilo conductor):** las Cortes están disueltas (RD 806/2026) y la ley española no estará antes de 2027; el manual debe describir la aplicación de la CCD2 sin ley de transposición en vigor. R2 debe confirmar y definir el tratamiento.
5. **Tabla de equivalencias** art. 18 CCD2 / art. 22 RGPD / arts. 14, 26, 27, 86 AI Act / GL/2020/06 (anexo de la carta de la EBA como base): añadir como anexo de la Parte IV.

## Huecos

- **Texto del anteproyecto de ley (arts. 25-30) y del real decreto:** no leído. Intenté el PDF del Ministerio de Economía (portal.mineco.gob.es, `ECO_TES_20260108_AP_APL_Credito_Consumo.pdf`) y falló por error de certificado TLS; no lo he eludido. Cerraría el hueco: descargar el PDF desde otra red o la ficha de audiencia pública.
- **Sentencia C-203/22:** texto íntegro y numeración de apartados (EUR-Lex y curia.europa.eu bloquean la descarga automática). Solo comunicado y nota de la AEPD.
- **Texto oficial de EUR-Lex del Reglamento 2026/1744:** número y fecha de publicación solo por fuentes secundarias.
- **Directrices de la Comisión sobre clasificación de alto riesgo:** versión final (borrador del 19-may-2026 leído en copia de un tercero). Directrices sobre la definición de sistema de IA: no leídas.
- **Directrices WP251 rev.01 y Directrices 06/2020 del CEPD:** contenido no releído.
- **Informes de la EBA sobre *big data* (2020) y ML en IRB (2023):** no leídos en el original. Tabla de cumplimiento de la EBA: versión de 2022 en copia de tercero.
- **Adopción del RTS EBA/RTS/2026/05 por la Comisión:** sin confirmar.
- **RD 806/2026 y efectos sobre proyectos de ley en tramitación:** leído por prensa jurídica, no en el BOE.
- **Guía o expectativa del BCE sobre scoring de admisión de consumo:** no encontrada.
- **Estado de la CCD2 en la Ley 16/2011 y de la corrección de errores de 2026 de la CCD2:** la búsqueda indicó que una corrección publicada en 2026 afecta al art. 2.7 y al art. 16.2, no al art. 18; no la he leído (es de R1).
- **Cuantía de sanciones nacionales del AI Act:** el proyecto de ley (arts. 13-41) no se leyó en detalle.
- **Jurisprudencia española** (Supremo, AEPD) sobre scoring con IA, y resoluciones de la AEPD sobre scoring: no localizadas.

## Fuentes

1. Directiva (UE) 2023/2225 relativa a los contratos de crédito al consumo, DOUE L de 30.10.2023, texto ES. Primaria. https://www.boe.es/doue/2023/2225/L00001-00067.pdf (ELI http://data.europa.eu/eli/dir/2023/2225/oj)
2. Reglamento (UE) 2024/1689 (AI Act), DOUE L de 12.7.2024, texto ES. Primaria. https://www.boe.es/doue/2024/1689/L00001-00144.pdf
3. PE-CONS 30/1/26 REV 1, Reglamento (UE) 2026/… (*Digital Omnibus on AI*), Estrasburgo, 8-jul-2026. Primaria. https://data.consilium.europa.eu/doc/document/PE-30-2026-REV-1/en/pdf
4. Cuatrecasas, "Digital Omnibus on AI has been published". Secundaria. https://www.cuatrecasas.com/en/spain/intellectual-property/art/digital-omnibus-ai-has-been-published
5. Gibson Dunn, "EU AI Act Omnibus Agreement". Secundaria. https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/
6. Parlamento Europeo, texto adoptado P10_TA(2026)0198, 16-jun-2026. Primaria (PDF ilegible en la lectura). https://data.europarl.europa.eu/distribution/doc/TA-10-2026-0198_en.pdf
7. Comisión Europea, borrador de directrices sobre clasificación de alto riesgo (art. 6 AI Act), consulta, 19-may-2026 (copia de un tercero). Primaria (copia no oficial). https://table.media/assets/documents/draft_guidelines_on_the_classification_of_high_risk_ai_annex_iii_7mxr3yiz2gw3uppjpwvvndd8ioi_128561.pdf
8. Proyecto de Ley Orgánica para el buen uso y la gobernanza de la IA, BOCG Congreso, A, núm. 97-1, 12-jun-2026. Primaria. https://www.congreso.es/public_oficiales/L15/CONG/BOCG/A/BOCG-15-A-97-1.PDF
9. Reglamento (UE) 2016/679 (RGPD), DOUE L 119, 4.5.2016, texto ES. Primaria. https://www.boe.es/doue/2016/119/L00001-00088.pdf
10. TJUE, sentencia de 7-dic-2023, C-634/21, SCHUFA Holding (Scoring), texto en inglés (copia en collab.dpa.gr de la versión CURIA) y comunicado de prensa 186/23. Primaria. https://curia.europa.eu/jcms/upload/docs/application/pdf/2023-12/cp230186es.pdf
11. TJUE, sentencia de 27-feb-2025, C-203/22, Dun & Bradstreet Austria, comunicado de prensa 22/25. Primaria (comunicado no oficial). https://curia.europa.eu/jcms/upload/docs/application/pdf/2025-02/cp250022es.pdf
12. AEPD, "Evaluación de la intervención humana en las decisiones automatizadas", 4-mar-2024. Primaria. https://www.aepd.es/prensa-y-comunicacion/blog/evaluacion-de-la-intervencion-humana-en-las-decisiones-automatizadas
13. AEPD, nota "Sistemas algorítmicos en el ámbito laboral", 7-oct-2026. Primaria. https://www.aepd.es/guias/Nota-RD-723-2026-AI-00009-2026.pdf
14. Ley Orgánica 3/2018 (LOPDGDD), art. 20. Primaria. https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673
15. Ley 15/2022, integral para la igualdad de trato y la no discriminación. Primaria. https://www.boe.es/buscar/act.php?id=BOE-A-2022-11589
16. Ley 16/2011 de contratos de crédito al consumo, arts. 14-15. Primaria. https://www.boe.es/buscar/act.php?id=BOE-A-2011-10970
17. EBA, Final Report, Guidelines on loan origination and monitoring (EBA/GL/2020/06), 29-may-2020. Primaria. https://www.eba.europa.eu/sites/default/files/document_library/Publications/Guidelines/2020/Guidelines%20on%20loan%20origination%20and%20monitoring/884283/EBA%20GL%202020%2006%20Final%20Report%20on%20GL%20on%20loan%20origination%20and%20monitoring.pdf
18. EBA, tabla de cumplimiento EBA/GL/2020/06 (21-feb-2022), copia de un tercero. Primaria (copia). https://www.loyensloeff.com/nl/eba-gl-2020-06---ct-gls-on-loan-origination-and-monitoring.pdf
19. Banco de España, Memoria de Supervisión 2020, recuadro 7.3. Primaria. https://www.bde.es/f/webbde/Secciones/Publicaciones/PublicacionesAnuales/MemoriaSupervisionBancaria/20/Supervision_Report_Box7.3.pdf
20. Banco de España, guías supervisoras. Primaria. https://www.bde.es/wbe/en/punto-informacion/contenidos/normativa-guias-recomendaciones/guias-supervisoras-banco-espana/
21. Banco de España, Memoria de Supervisión 2025 (abr-2026). Primaria. https://www.bde.es/f/webbe/Secciones/Publicaciones/PublicacionesAnuales/MemoriaSupervisionBancaria/25/MemoriaSupervision2025.pdf
22. Banco de España, Circular 1/2026, de 21-oct-2026, sobre la CIR, BOE núm. 270, 30-oct-2026. Primaria. https://boe.es/boe/dias/2026/10/30/pdfs/BOE-A-2026-22720.pdf
23. EBA, carta del presidente sobre el mapeo del AI Act (EBA/2025/D/5384, 21-nov-2025) y factsheet "AI Act: implications for the EU banking and payments sector". Primaria. https://www.eba.europa.eu/sites/default/files/2025-11/2019d1b5-59f8-4149-ad3b-23cfcd4388a1/EBA%20Chair%20letter%20to%20Mr%20Berrigan%20and%20Mr%20Viola%20on%20outcome%20of%20EBA%E2%80%99s%20AI%20Act%20mapping%20exercise.pdf
24. EBA, nota de prensa, informe de seguimiento sobre ML en modelos IRB, 4-ago-2023. Primaria. https://eba.europa.eu/publications-and-media/press-releases/eba-publishes-follow-report-use-machine-learning-internal
25. EBA, EBA/RTS/2026/05, informe final, 30-mar-2026, proyecto de RTS que modifica el Reglamento Delegado (UE) 529/2014. Primaria. https://www.eba.europa.eu/sites/default/files/2026-03/7bbbbcd4-caa4-489d-b2b4-a837d04e709e/Final%20report%20RTS%20on%20material%20model%20changes.pdf
26. Directiva (UE) 2015/2366 (PSD2), DOUE L 337, 23.12.2015, texto ES. Primaria. https://www.boe.es/doue/2015/337/L00035-00127.pdf
27. CEPD, Directrices 06/2020 sobre la interacción entre PSD2 y RGPD (15-dic-2020), ficha. Primaria (solo metadatos leídos). https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-062020-interplay-second-payment-services_en
28. CNMC, informe IPN/CNMC/037/26 sobre el anteproyecto de ley de contratos de crédito al consumo, 14-sep-2026. Primaria (autoridad). https://cnmc.es/sites/default/files/6795242.pdf
29. Ministerio de Consumo, nota informativa sobre las nuevas normas de crédito al consumo, 24-abr-2026. Primaria. https://portal-cec.consumo.gob.es/sites/default/files/documentos/NI_Credito_Consumo_24_06_2026.pdf
30. Cuatrecasas, "Anteproyecto de Ley de Contratos de Crédito al Consumo y reglamento" (Legal Flash, ene-2026). Secundaria. https://www.cuatrecasas.com/resources/creditos-consumo-text-6968f4269fda5805689910.pdf
31. Prensa jurídica sobre el Real Decreto 806/2026 de disolución de las Cortes (INAP, Iustel, LegalToday, elderecho.com), oct-2026. Secundaria. https://www.legaltoday.com/actualidad-juridica/noticias-de-derecho/el-boe-publica-el-real-decreto-de-disolucion-de-las-cortes-y-la-convocatoria-electoral-para-el-29-de-noviembre-2026-10-06/
32. The European Post, "Financial Data Access Regulation exit reshapes open finance", 6-nov-2026; MLex; openbankingtracker. Secundaria. https://theeuropeanpost.eu/research-analysis/financial-data-access-regulation-exit-reshapes-open-finance
33. DLA Piper, Taylor Wessing, PwC, MoFo: PSD3/PSR 2025-2026. Secundaria. https://www.dlapiper.com/en/insights/publications/2026/03/psd3-and-psr
