# Manual de Crédito al Consumo: la CCD2 en España
## Índice detallado, versión de trabajo v0.1 (2026-11-23, provisional hasta cerrar F1)

**Objetivo:** llevar a un profesional de banca que conoce el crédito al consumo como negocio, pero no su normativa de conducta, hasta el nivel de experto: alguien capaz de diagnosticar, implantar y defender la adaptación de una entidad española a la CCD2.
**Lo que se asume:** qué es un préstamo personal, una tarjeta y una financiación en el punto de venta; nociones de riesgo de crédito (PD, *scoring*) para la Parte IV. **Nada más:** ni la Ley 16/2011, ni la mecánica de las directivas, ni la jurisprudencia de usura.
**Perímetro (propuesto, §2.2 de `PROCESO.md`):** Directiva (UE) 2023/2225 y su transposición; usura y *revolving*; solvencia con IA (AI Act, RGPD); atención a la clientela (Ley 10/2025) y recobro donde toca al consumo.
**Fuera de perímetro:** crédito hipotecario (Ley 5/2019) salvo como comparación; servicios de pago; prudencial (capital) salvo el enlace con los modelos IRB en el cap. 25.
**Fecha de referencia:** CCD2 aplicable desde el 20-nov-2026. Estado de la ley española: lo que diga R2 a fecha de F1.
**Principio editorial:** el de los manuales anteriores: qué problema resuelve cada regla, a qué obliga, dónde deja margen y qué se hace con ese margen frente al supervisor, el juez y el cliente.

> **Aviso:** los números de artículo de este índice son de memoria y se verifican en F1 (R1). No se
> copian al texto del libro sin verificar.

---

## Convenciones del manual

### Bloques marcados

| Marca | Contenido |
|---|---|
| **[NORMA]** | Artículo de la directiva, su equivalente español (Ley 16/2011, anteproyecto o "sin equivalente") y qué exige en una frase |
| **[POR QUÉ]** | Qué falló con la CCD1 o qué se quiso conseguir |
| **[MARGEN]** | Discrecionalidad, opción nacional, silencio normativo |
| **[PALANCA]** | Impacto en aprobación, volumen, margen, coste o litigiosidad, con orden de magnitud |
| **[TRAMPA]** | Error frecuente en la implantación |
| **[NÚMEROS]** | Ejemplo trabajado de principio a fin |
| **[CÓDIGO]** | Remisión al anexo ejecutable |
| **[DEFENSA]** | Cómo se argumenta ante el Banco de España, un juez, la AEPD o auditoría |
| **[QUÉ VIENE]** | Cambio en curso, sin fechas firmes |
| **[CASO]** | Situación con supervisor, juzgado o cliente: qué llega, qué hay detrás, la respuesta que funciona y la que empeora las cosas |

### Tres niveles

| Nivel | Quién es al terminar | Partes |
|---|---|---|
| **N1 · Fundamentos** | Entiende qué regula la CCD2, por qué y cómo llega a España | 0 y I |
| **N2 · Practicante** | Puede trabajar en un programa de implantación sin que le expliquen la norma | II, III y IV (caps. 20-24) |
| **N3 · Experto** | Diagnostica, prioriza y defiende la adaptación de una entidad | IV (caps. 25-26), V y VI |

Cada parte termina con **"Qué deberías saber hacer ahora"** y una autoevaluación corta (anexo R5).

### Hilo conductor

Una entidad de referencia sintética con tres productos: una tarjeta *revolving*, un préstamo personal
contratado en móvil y un BNPL en el punto de venta a través de comercios asociados. Nace en el cap. 5
y reaparece en los caps. 9, 10, 18, la Parte IV, el cap. 28 y los anexos S1-S3.

---

# PARTE 0 · Cómo usar este manual

### 0.1 Para quién es
- 0.1.1 Lo que se asume y lo que no
- 0.1.2 Lo que este manual no es: ni un dictamen ni un resumen de despacho
- 0.1.3 La meta: de "sé qué es la TAE" a "sé defender por qué mi proceso de admisión cumple"

### 0.2 Rutas
- 0.2.1 La ruta completa
- 0.2.2 Por rol: cumplimiento, riesgos (Head of Risk: Parte IV directa), negocio y producto, tecnología
- 0.2.3 Incorporación urgente a un programa CCD2 en marcha
- 0.2.4 Modo referencia: buscar desde el artículo (anexo R2)

### 0.3 Cómo trabajar con las fuentes
- 0.3.1 Los textos de cabecera: directiva y su corrección de errores, Ley 16/2011, anteproyecto
- 0.3.2 Directiva, anteproyecto, proyecto, ley: no trabajar con la versión equivocada
- 0.3.3 **[QUÉ VIENE]** Qué partes caducan cuando se apruebe la ley española

---

# PARTE I · Fundamentos [N1]

> Al terminar: sabes qué regula la CCD2, por qué existe, cómo encaja con el derecho español y qué
> pasa cuando una directiva se aplica sin ley nacional.

## Capítulo 1 · El crédito al consumo en España
### 1.1 Los productos
- 1.1.1 Préstamo personal, tarjeta de crédito y *revolving*, financiación al consumo en punto de venta
- 1.1.2 BNPL: qué es y por qué estaba fuera de la CCD1
- 1.1.3 Descubiertos, anticipos de nómina y microcréditos
### 1.2 Los actores
- 1.2.1 Bancos, establecimientos financieros de crédito, *fintech* y prestamistas no regulados
- 1.2.2 Comercios, intermediarios y plataformas
- 1.2.3 Supervisores: Banco de España, Consumo, comunidades autónomas, AEPD
### 1.3 Las cifras
- 1.3.1 Tamaño del mercado, crecimiento y morosidad (datos de R5, con fecha)
- 1.3.2 Dónde se concentran las reclamaciones

## Capítulo 2 · Por qué una segunda directiva
### 2.1 Lo que falló de la CCD1
- 2.1.1 Ámbito que se quedó corto: BNPL, créditos pequeños, sin intereses
- 2.1.2 Información que nadie lee
- 2.1.3 Solvencia mal definida y armonización a medias
### 2.2 Lo que cambió en el mercado
- 2.2.1 Digitalización y contratación en segundos
- 2.2.2 Datos alternativos y decisiones automatizadas
- 2.2.3 Sobreendeudamiento tras la pandemia
### 2.3 El proceso legislativo
- 2.3.1 Evaluación de la Comisión, propuesta de 2021 y texto final de 2023
- 2.3.2 Qué se quedó por el camino

## Capítulo 3 · El mapa normativo
### 3.1 Capa europea
- 3.1.1 CCD2 y su relación con la Directiva 2023/2673 de servicios financieros a distancia
- 3.1.2 RGPD, AI Act, PSD2 y FiDA
- 3.1.3 Directiva 2021/2167 de administradores y compradores de créditos
- 3.1.4 Directrices de la EBA sobre originación y seguimiento (EBA/GL/2020/06)
### 3.2 Capa española
- 3.2.1 Ley 16/2011 de contratos de crédito al consumo
- 3.2.2 Orden EHA/2899/2011 y Circular 5/2012 del Banco de España
- 3.2.3 Ley de Represión de la Usura de 1908
- 3.2.4 Ley 10/2025 de servicios de atención a la clientela
- 3.2.5 LOPDGDD y ficheros de solvencia
### 3.3 Quién supervisa qué
- 3.3.1 Entidades supervisadas por el Banco de España frente a prestamistas no bancarios
- 3.3.2 La autoridad de consumo y las comunidades autónomas

## Capítulo 4 · Cómo funciona una directiva que no se ha transpuesto
### 4.1 Directiva, transposición y armonización
- 4.1.1 Armonización máxima y sus excepciones en la CCD2
- 4.1.2 Opciones nacionales
### 4.2 Qué pasa cuando el Estado llega tarde
- 4.2.1 Efecto directo vertical, no horizontal
- 4.2.2 Interpretación conforme: lo que hará un juez español
- 4.2.3 Responsabilidad del Estado y procedimiento de infracción
### 4.3 Consecuencias para una entidad
- 4.3.1 Qué es exigible hoy, qué es prudente y qué puede esperar
- 4.3.2 **[CASO]** El juez que aplica la directiva en un pleito contra un banco

## Capítulo 5 · Un crédito de principio a fin
### 5.1 La entidad de referencia y sus tres productos
### 5.2 El ciclo de vida
- 5.2.1 Publicidad → información → solvencia → contrato → vida → dificultades de pago → recobro
- 5.2.2 Dónde muerde la CCD2 en cada paso
### 5.3 **[NÚMEROS]** Lo que cuesta cada producto al cliente (TAE con S1)

---

# PARTE II · La directiva [N2]

> Al terminar: conoces cada obligación de la CCD2, su equivalente en la Ley 16/2011 y lo que cambia.

## Capítulo 6 · Ámbito y definiciones
- 6.1 Qué entra: umbral de importe, BNPL, créditos sin intereses, alquiler con opción de compra
- 6.2 Qué sigue fuera y las opciones nacionales
- 6.3 Definiciones que cambian la implantación: prestamista, intermediario, proveedor de bienes
- 6.4 **[TRAMPA]** El comercio que no sabe que ahora es intermediario

## Capítulo 7 · Publicidad y comercialización
- 7.1 Información básica en la publicidad y el aviso sobre el coste del crédito
- 7.2 Prácticas prohibidas: consentimiento por defecto, ventas vinculadas y combinadas
- 7.3 Ofertas no solicitadas y comercialización digital
- 7.4 **[CASO]** Una campaña en redes sociales que llega al supervisor

## Capítulo 8 · Información precontractual, explicaciones y asesoramiento
- 8.1 La información normalizada europea (SECCI) y el resumen en la primera página
- 8.2 Cuándo y cómo se entrega en un canal digital
- 8.3 Explicaciones adecuadas
- 8.4 Servicios de asesoramiento
- 8.5 Conocimientos y competencia del personal

## Capítulo 9 · Solvencia y bases de datos
- 9.1 La obligación de evaluar la solvencia: interés del consumidor, no del prestamista
- 9.2 Qué datos se pueden usar y cuáles no
- 9.3 Decisiones automatizadas: derecho a intervención humana y a una explicación
- 9.4 Qué pasa si la evaluación es negativa
- 9.5 Acceso a bases de datos y ficheros transfronterizos
- 9.6 **[NÚMEROS]** La solicitud del hilo conductor bajo las reglas nuevas (remite a la Parte IV)

## Capítulo 10 · Contrato, TAE y límites de coste
- 10.1 Información que debe contener el contrato
- 10.2 La TAE: cálculo y supuestos (S1)
- 10.3 Límites a tipos, TAE o coste total: la obligación de los Estados
- 10.4 **[PALANCA]** Qué productos dejan de ser rentables con un límite de coste

## Capítulo 11 · Derechos durante la vida del crédito
- 11.1 Desistimiento
- 11.2 Contratos vinculados
- 11.3 Reembolso anticipado y compensación
- 11.4 Cesión de derechos
- 11.5 Cambios en el tipo deudor

## Capítulo 12 · Descubiertos y rebasamientos

## Capítulo 13 · Dificultades de pago
- 13.1 Medidas de tolerancia antes de la ejecución
- 13.2 Servicios de asesoramiento de deudas
- 13.3 Límites a los recargos por impago
- 13.4 Remisión a la operativa del cap. 30

## Capítulo 14 · Prestamistas no bancarios, intermediarios y sanciones
- 14.1 Admisión, registro y supervisión de prestamistas e intermediarios
- 14.2 Sanciones efectivas y disuasorias
- 14.3 Resolución alternativa de litigios

---

# PARTE III · España [N2]

> Al terminar: sabes qué está en vigor hoy en España, qué cambiará con la ley y cómo operar mientras tanto.

## Capítulo 15 · Estado de la transposición (a fecha de F1)
- 15.1 Cronología: anteproyecto, informes, Consejo de Estado, Cortes
- 15.2 El procedimiento de infracción de la Comisión
- 15.3 **[QUÉ VIENE]** Escenarios de aprobación y qué cambia en cada uno

## Capítulo 16 · El anteproyecto frente a la directiva
- 16.1 Lo que transpone tal cual
- 16.2 Lo que endurece España (*gold-plating*)
- 16.3 Las opciones nacionales que elige
- 16.4 El borrador de real decreto

## Capítulo 17 · Vivir sin ley
- 17.1 Qué aplica ya: la Ley 16/2011 vigente leída a la luz de la directiva
- 17.2 Qué espera el Banco de España
- 17.3 **[DEFENSA]** Cómo documenta una entidad sus decisiones de implantación
- 17.4 **[CASO]** El cliente que reclama un derecho de la CCD2 que la ley española aún no recoge

## Capítulo 18 · Usura y *revolving*
- 18.1 La Ley Azcárate y su lectura moderna
- 18.2 Las sentencias del Supremo de 2015, 2020 y 2023
- 18.3 El índice de referencia y cómo se compara la TAE (S1)
- 18.4 Límites de coste de la CCD2 y usura: cómo encajan
- 18.5 **[PALANCA]** Exposición a litigios de una cartera *revolving*

## Capítulo 19 · Supervisión de conducta y litigiosidad
- 19.1 Banco de España: inspección de conducta, memoria de reclamaciones, criterios
- 19.2 La nueva autoridad de atención a la clientela (Ley 10/2025)
- 19.3 Litigación masiva: lo que enseñan las cláusulas suelo y los gastos hipotecarios

---

# PARTE IV · Adaptar los modelos de admisión [N2-N3]

> **La escribe el agente especialista en modelos de crédito** (`especialista/brief-especialista-modelos.md`).
> Lector objetivo: el Head of Risk de un banco o una entidad de *lending* española.
> Al terminar: sabes qué cambiar en tus modelos y procesos de admisión, en qué orden, con qué coste
> y cómo defenderlo ante el supervisor.
>
> La estructura de abajo es la propuesta; el especialista puede reordenarla y lo justifica en
> `especialista/decisiones-parte-04.md`.

## Capítulo 20 · Qué cambia para un modelo de admisión
- 20.1 El art. 18 traducido a requisitos de modelo
- 20.2 De "¿me devolverá?" a "¿puede permitírselo?": riesgo de crédito y capacidad de pago
- 20.3 Diagnóstico rápido: las diez preguntas que un Head of Risk hace a su equipo

## Capítulo 21 · Datos
- 21.1 Inventario de variables y clasificación: permitidas, prohibidas, dudosas
- 21.2 Retirar variables sin destruir el poder predictivo (S2)
- 21.3 Fuentes nuevas: *open banking*, ficheros positivos, datos del comercio
- 21.4 Calidad y trazabilidad del dato

## Capítulo 22 · Capacidad de pago frente a probabilidad de *default*
- 22.1 Ingresos, gastos y renta disponible: cómo se estiman
- 22.2 Reglas de *affordability* y su interacción con la *scorecard*
- 22.3 Proporcionalidad: el BNPL de 50 € frente al préstamo de 30.000 €
- 22.4 **[NÚMEROS]** Aprobación y morosidad con y sin regla de capacidad de pago (S2)

## Capítulo 23 · Explicabilidad, intervención humana y decisiones automatizadas
- 23.1 Lo que exigen la CCD2, el RGPD y el AI Act a la vez
- 23.2 Motivos de denegación explicables
- 23.3 Diseñar la revisión humana para que no sea un sello
- 23.4 **[CASO]** El cliente denegado que pide una explicación

## Capítulo 24 · Sesgo y discriminación
- 24.1 Qué se considera discriminación y qué no
- 24.2 Métricas y pruebas (S3)
- 24.3 Variables proxy

## Capítulo 25 · Impacto en el resto del ecosistema de modelos
- 25.1 Modelos IRB: cuando el *score* de admisión es un *driver* de PD (política de cambios de modelo)
- 25.2 IFRS 9, *pricing* y *stress test*
- 25.3 Gobierno y validación: lo que preguntará validación interna

## Capítulo 26 · Hoja de ruta para un Head of Risk
- 26.1 Diagnóstico en 30 días
- 26.2 Priorización: lo exigible ya, lo prudente y lo que puede esperar a la ley
- 26.3 Plan a 90, 180 y 365 días
- 26.4 Presupuesto, equipo y proveedores
- 26.5 Indicadores de seguimiento
- 26.6 **[DEFENSA]** Lo que pedirá el supervisor y cómo se le enseña

---

# PARTE V · Implantación en la entidad [N3]

> Al terminar: sabes montar y dirigir un programa CCD2 de principio a fin.

## Capítulo 27 · El programa CCD2
- 27.1 Análisis de *gaps* (anexo R3)
- 27.2 Gobierno: quién es dueño de qué
- 27.3 Calendario y dependencias de tecnología
## Capítulo 28 · Producto a producto
- 28.1 Tarjeta *revolving*
- 28.2 Préstamo personal digital
- 28.3 BNPL y financiación con comercios
- 28.4 Descubiertos y anticipos
## Capítulo 29 · El recorrido digital
- 29.1 Información, explicaciones y firma en el móvil
- 29.2 Pruebas de usabilidad como evidencia de cumplimiento
## Capítulo 30 · Recobro y dificultades de pago
- 30.1 Medidas de tolerancia en la práctica
- 30.2 Derivación a asesoramiento de deudas
- 30.3 Recobro automatizado y canal humano
## Capítulo 31 · El impacto en negocio
- 31.1 Aprobación, volumen y margen
- 31.2 Coste de cumplimiento
- 31.3 **[PALANCA]** Escenarios para la entidad de referencia

---

# PARTE VI · Retos [N3]

## Capítulo 32 · IA en solvencia: AI Act y CCD2 a la vez
## Capítulo 33 · *Open finance* y FiDA
## Capítulo 34 · Litigiosidad masiva: el próximo frente
## Capítulo 35 · Qué viene

---

# ANEXOS

### Anexos de código
- **S1** `s1_tae.py`: TAE de los tres productos del hilo conductor y comparación con usura
- **S2** `s2_scorecard.py`: *scorecard* sintética, retirada de variables, regla de capacidad de pago, *open banking*
- **S3** `s3_sesgo.py`: pruebas de sesgo sobre S2

### Anexos de referencia
- **R1** Glosario
- **R2** Tabla de correspondencia: CCD1, CCD2, Ley 16/2011 y anteproyecto, artículo por artículo
- **R3** *Checklist* de análisis de *gaps* por área
- **R4** Fuentes y cómo seguir lo que viene
- **R5** Autoevaluación por parte
- **R6** Casos integrados
