---
type: source
created: 2026-11-23
status: active
freshness: snapshot
tags: [ccd2, research, r5]
---

# R5 · El mercado español y la transposición en otros países

**Fecha de consulta:** 2026-11-23
**Agente:** Sonnet 5.5, brief `investigacion/briefs/r5-mercado-y-comparados.md`
**Resumen en cinco líneas:**
1. Saldo vivo del crédito al consumo (bancos + EFC) en España: 113.345 M€ a dic-2025 y 117.810 M€ a jun-2026 (provisional); nueva producción 2025 de 46.639 M€ en préstamos, más 10.815 M€ de saldo en tarjetas. Los EFC pierden cuota: 18,9% a dic-2025.
2. Tipo medio de las nuevas operaciones de consumo (TEDR) 7,16% y tarjetas de crédito/*revolving* 18,26% en ago-2026 (provisional). El 7,60% que circula en prensa es de la zona del euro, no de España.
3. A fecha de consulta (el día 3 de aplicación) España no ha transpuesto: la Comisión le envió dictamen motivado el 1-oct-2026. Han transpuesto en plazo o casi: Italia, Alemania, Suecia, Austria, Croacia y Bélgica; Francia lo hizo por ordenanza pero sigue en la lista de dictámenes motivados.
4. No existe cifra oficial del tamaño del BNPL en España ni en la UE. Hay estimaciones de mercado (~4.000 M€ en España en 2025, sin método) y un dato regulatorio sólido de un solo país (AFM, Países Bajos: 5.100 M€ en 2024).
5. La evaluación de impacto de la Comisión (2021) cuantifica solo parcialmente: costes para la banca de ~1.460 M€ (284 M€ únicos y 1.179 M€ recurrentes, suma mía de su tabla 13) frente a ~1.990 M€ de beneficio al consumidor en 2021-2030. Los topes de tipos no se cuantificaron.

**Nota de fiabilidad global.** Las secciones 1 y 2 descansan sobre todo en fuentes primarias (Banco de España, ASNEF, CNMC). La sección 3 (BNPL) es en su mayoría `[Likely]` o `[Guessing]`, y lo digo allí. En la sección 4, lo de Italia, Alemania, Francia (habilitación) y Países Bajos está leído en la fuente oficial; Suecia, Austria, Bélgica, Croacia, Polonia y el resto vienen de un único medio secundario (Fintechweekly, 17-nov-2026) y no los he podido contrastar con EUR-Lex, que no se deja leer sin navegador.

---

## 1. Mercado español de crédito al consumo

### 1.1 Saldo vivo

- `[Certain]` Crédito al consumo de los hogares (entidades de crédito y EFC), saldo en M€: dic-2023 97.052; dic-2024 102.705; dic-2025 113.345; mar-2026 114.743; jun-2026 (provisional) 117.810. Del saldo de dic-2025, 76.948 M€ son "del cual bienes de consumo duradero". Fuente: Banco de España, *Boletín Estadístico* septiembre 2026, cuadro 4.13 (fichero en `fuentes/bde_boletin_estadistico_2026-09.pdf`).
- `[Certain]` De ahí, mi cálculo: +10,4% en 2025 (113.345/102.705) y +11,3% interanual a jun-2026 (117.810/105.880).
- `[Certain]` El *Informe de Estabilidad Financiera* de primavera 2026 dice que el crédito al consumo de las entidades de depósito creció un 12% en 2025, 4,7 pp más que en 2024. El consumo es el 14,5% del crédito a hogares a dic-2025 (la vivienda, el 79,7%). Fuente: BdE, IEF primavera 2026, cap. 3, pp. 61 y nota 17 (`fuentes/bde_ief_primavera2026_cap3.pdf`).
- `[Certain]` La CNMC, citando la MAIN del anteproyecto, da 116.026 M€ en feb-2026 con un +11% interanual, frente a un +4,6% de la financiación total a hogares. Fuente: CNMC, IPN/CNMC/037/26, 14-sep-2026, §1 (`fuentes/cnmc_6795242.pdf`).
- **Contradicción de cifras (regla 6).** El 12% del IEF y el 10,4% de mi cálculo difieren porque el IEF se refiere a entidades de depósito y el boletín suma también los EFC. Para el manual, uso el boletín (serie completa con EFC) y cito el IEF como contraste.
- `[Likely]` Una cifra de 121.600 M€ en jul-2026 (+12,6%) que da un medio secundario no coincide con el boletín (117.810 M€ a jun-2026). Descartada como no verificable.

### 1.2 Nueva producción

La definición importa. En la estadística del BdE (Circular 1/2010), las **tarjetas de crédito y *revolving*** y los **descubiertos** no se miden por lo concedido en el mes: se considera "operación nueva" su saldo vivo al final del mes. Los demás préstamos sí se miden por importe concedido.

- `[Certain]` Nuevas operaciones de crédito al consumo (préstamos y créditos, sin tarjetas), M€ por año: 2022 29.924; 2023 32.311; 2024 38.642; 2025 46.639. Mi cálculo: +20,7% en 2025. Por plazo inicial de fijación en 2025: hasta 1 año 5.439; de 1 a 5 años 18.399; más de 5 años 22.802. Fuente: BdE, *Boletín Estadístico* sept-2026, cuadro 19.12.
- `[Certain]` Saldo de tarjetas de crédito y *revolving* tratado como "nueva operación": 10.815 M€ a fin de 2025 (10.916 M€ a fin de 2024). Misma fuente.
- `[Certain]` Mensual 2026 (consumo sin tarjetas): ene 3.624; feb 4.114; mar 4.562; abr 3.790; may 4.093; jun 4.322; jul 4.276; ago (provisional) 3.322 M€. Misma fuente.
- `[Certain]` ASNEF mide otra cosa (sus asociados, sin financiación de automoción): inversión nueva de crédito al consumo 2025 de 27.681 M€ (+4,5%); total de la industria 29.227 M€ (+2,4%); 8,2 millones de contratos nuevos (-3,1%). Fuente: ASNEF, nota de prensa 29-jun-2026 (`fuentes/asnef_ndp_industria_financiacion_2025.pdf`).
- **Cómo cuadrar BdE y ASNEF** `[Guessing]`: el BdE cubre a todos los bancos y EFC, y ASNEF a sus asociados y sin automoción. No he encontrado una conciliación publicada. En el libro conviene citar las dos con su perímetro y no sumarlas ni compararlas.

### 1.3 Desglose por producto

- `[Certain]` ASNEF, dentro de su perímetro, 2025: inversión nueva en préstamos personales +5,5%; bienes de consumo +2,6%; *revolving* +5,2%; tarjetas no *revolving* +4,5%; operaciones inmobiliarias +13%; bienes de equipo -18,5%. El riesgo vivo del crédito al consumo baja un 11,9% hasta 19.979 M€, por el *revolving* (saldo -38,2%), mientras que préstamos personales (+2,2%) y bienes de consumo (+6,6%) suben. Los contratos nuevos de *revolving* caen un 14,1%. ASNEF lo interpreta como que los clientes usan más el crédito ya disponible. Misma nota de prensa.
- `[Likely]` La caída del saldo *revolving* en ASNEF es coherente con la presión de la jurisprudencia de usura sobre ese producto, pero ASNEF no da la causa; es inferencia mía.
- `[Certain]` Microcréditos y préstamos rápidos: según datos de AEMIP citados por la MAIN, en 2025 se formalizaron 3.840.864 contratos por 1.236 M€. Fuente: CNMC, IPN/CNMC/037/26, §3.1 (cita de segunda mano; no he leído la MAIN).
- Hueco: no he encontrado un desglose oficial de saldo por tarjetas/préstamo personal/automoción/punto de venta. Ver Huecos.

### 1.4 Tipos de interés de las nuevas operaciones

- `[Certain]` Tipo efectivo definido restrictivo (TEDR, no incluye comisiones ni seguros), nuevas operaciones, entidades de crédito y EFC, ago-2026 (provisional): crédito al consumo, tipo medio ponderado **7,16%** (hasta 1 año 5,01%; de 1 a 5 años 6,97%; más de 5 años 7,77%); **tarjetas de crédito y *revolving* 18,26%**. Serie de tarjetas: 2022 17,99%; 2023 18,22%; 2024 18,54%; dic-2025 18,32%; jun-2026 18,30%. Fuente: BdE, *Boletín Estadístico* sept-2026, cuadro 19.4.
- `[Certain]` TAE del crédito al consumo (excluye descubiertos y tarjetas de crédito con pago aplazado y *revolving*), ago-2026 (provisional) **8,01%**; dic-2025 7,41%; 2024 7,94%; 2023 8,83%. Misma fuente, cuadro 19.6.
- `[Certain]` **Cuidado con la zona del euro.** La nota del BdE/BCE de 2-sep-2026 dice que el tipo de los nuevos créditos al consumo "se situó en el 7,60%" en julio de 2026. Es un dato de la **zona del euro** (volumen 29,83 mM€), no de España. Fuente: `fuentes/bde_presbce2026-126.pdf`, cuadro 2. La prensa lo ha presentado como dato español.
- `[Certain]` El TEDR de las tarjetas (18,26%) no es comparable con un límite de TAE: el BdE avisa de que los TEDR no son "una referencia adecuada ni comparable del coste total" (nota a. del cuadro 19.4). El tope transitorio del anteproyecto es del 22% TAE, y la MAIN lo justifica con un límite jurisprudencial del 24,36% estimado para 2025 y con una media de Italia, Francia y Portugal de ~22,8% (CNMC, §3.2.3).
- `[Likely]` Tipo medio 2026 del crédito a corto plazo "10,06% TAE" y "11% TAE a menos de 12 meses" que dan medios secundarios: no he podido contrastarlos con el boletín (el cuadro 19.6 no desglosa por plazo). Descartados.

### 1.5 Morosidad

- `[Certain]` EFC, dic-2025: ratio de dudosos del crédito al consumo del 3,6% (+0,1 pp en el año), "tres décimas por debajo" del sector bancario en ese segmento. En vigilancia especial, el consumo de los EFC está en el 6,3% (+0,1 pp) y el bancario, en el 6,6%. Fuente: BdE, IEF primavera 2026, §3.2, p. 75.
- `[Likely]` De "tres décimas por debajo" sale un 3,9% para la banca en consumo (derivado, el IEF no da la cifra en ese párrafo).
- `[Certain]` En 2025, el saldo de dudosos de la cartera de consumo subió un 1% (4% en 2024), mientras bajó el de otras carteras de hogares (-16,7% en total hogares). Fuente: IEF primavera 2026, cap. 3.
- `[Certain]` ASNEF Equifax, informe de tendencias de crédito de junio 2026: el saldo impagado del fichero ASNEF baja un 14,5% desde enero de 2023, con un ligero repunte en personas físicas en el 2T-2026. Fuente: `fuentes/asnef_tendencias_credito_2026-06.pdf`, p. 6.
- No he encontrado una tasa de morosidad de consumo que combine bancos y EFC en el *Boletín*; una cifra de "5,4% de morosidad de los EFC" que apareció en un resumen de búsqueda no está en el informe de ASNEF que he leído. Descartada.

---

## 2. Actores

### 2.1 Bancos frente a EFC

- `[Certain]` Cuota de los EFC en el crédito al consumo concedido por EFC y bancos: **18,9% a dic-2025, 1,8 pp menos que en dic-2024** (es decir, ~20,7% a dic-2024, mi derivación). El crédito al consumo de los EFC creció un 0,1% en 2025, tras un 9,1% en 2024, y es el 47,5% de su crédito total. Fuente: BdE, IEF primavera 2026, §3.2, p. 75.
- `[Likely]` Un medio da 20,1% de cuota en 2024 y 19,2% en el 1T-2025, atribuido al BdE. Difiere del 20,7% derivado del IEF para dic-2024; puede deberse a una base distinta (nueva producción frente a saldo). Gana el IEF por ser fuente primaria más reciente.
- `[Certain]` El EFC pierde cuota pese a que el consumo crece un 11-12%. Lectura para el manual: el crecimiento del consumo en 2025 lo tiran los bancos.
- `[Likely]` Beneficio agregado de los EFC en 2025: 328 M€ (-16%); pico de >1.000 M€ en 2018 (The Objective, 27-abr-2026, citando al BdE). Esa misma pieza da 48.000 M€ de nueva producción (+20%) y >114.000 M€ de saldo y los atribuye a los EFC. **Esas dos cifras coinciden con el total bancos + EFC del *Boletín* (46.639 M€, +20,7%; 113.345 M€), no con los EFC.** `[Guessing]` Parece una atribución errónea del medio. No usar esas dos cifras como "EFC".
- `[Certain]` La MAIN calcula ~500 operadores que podrían conceder crédito al consumo: 414 ya registrados en el BdE (bancos, EFC, entidades de dinero electrónico y prestamistas inmobiliarios), más 10 EFC de actividad limitada y 17 prestamistas de alto coste previstos. Fuente: CNMC, IPN/CNMC/037/26, nota 1.

### 2.2 Principales entidades de consumo

- `[Certain]` El estudio sectorial de DBK, "Entidades de Financiación" (26ª edición, julio 2026), analiza a 29 entidades: ABANCA Servicios Financieros, Banco Cetelem, Bankinter Consumer Finance, BBVA Consumer Finance, BMW Bank, CA Auto Bank, CaixaBank Payments & Consumer, Cofidis, Confía, FCE Bank, Financiera El Corte Inglés, Findirect, GCC Consumo, Honda Bank, Ibercaja Servicios de Financiación, Iberia Cards, Kutxabank Kredit, Mercedes-Benz Financial Services, Mobilize Financial Services, Oney, Pepper Finance, Sabadell Consumer Finance, Santander Consumer Bank, Servicios Financieros Carrefour, Sofinco, Stellantis Financial Services, Toyota Kreditbank, Transolver Finance y Volkswagen Financial Services. Fuente: ficha-resumen DBK (`fuentes/dbk_entidades_financieras_2026-08.pdf`). Es secundaria (estudio comercial) y solo da la lista, no las cuotas.
- Falta contexto: cuotas por entidad. DBK las tiene en las tablas 8 y 9 del estudio completo (de pago). No las he podido ver.
- `[Likely]` Los EFC son, en su mayoría, filiales de bancos, de fabricantes de automóviles y de cadenas comerciales (The Objective, 27-abr-2026).

### 2.3 *Fintech* y BNPL activos en España

- `[Likely]` Klarna (2,3 millones de usuarios activos en España a ene-2026) y Oney (1,5 millones de clientes a jul-2026) figuran en material de Stripe. Es dato de la propia empresa recogido por un procesador de pagos, sin método publicado.
- `[Likely]` Aplazame, seQura, Scalapay, PayPal y Cofidis operan en España como financiación en comercio. **No he encontrado fuente fiable sobre su perfil regulatorio** (entidad de pago, EFC, o sin licencia), que es lo que importa para el artículo 37 de la CCD2. Un resumen de búsqueda atribuía Aplazame a WiZink; no coincide con lo que se conoce del sector y lo descarto como `[Guessing]` erróneo, a verificar en el registro del BdE.
- `[Certain]` La demanda de crédito de las entidades BNPL medida por consultas al fichero ASNEF "registra un ligero crecimiento" en el 2T-2026 frente al 1T. Fuente: ASNEF Equifax, informe de junio 2026, p. 5.
- `[Likely]` Un medio (Forbes España/Europa Press, 29-jul-2026) atribuye al informe ASNEF Equifax un +44,3% de demanda BNPL en el 1S-2026 frente al 1S-2025. En el PDF de junio 2026 no aparece esa cifra en texto (las series son gráficos); queda como secundaria.

### 2.4 Datos de ASNEF

Ver §1.2, §1.3 y §1.5. `[Certain]` ASNEF publica la inversión nueva y el riesgo vivo de sus asociados una vez al año (nota de 29-jun-2026 para el cierre de 2025) y un informe de tendencias de crédito trimestral con Equifax. No he encontrado una serie propia de morosidad de consumo en esos documentos.

---

## 3. BNPL

**Aviso: esta sección es mayoritariamente `[Likely]` o `[Guessing]`.** No hay cifra oficial.

### 3.1 Tamaño

- `[Likely]` España, 2025: ~4.000 M€ de operaciones BNPL, con el número de transacciones duplicándose en cada uno de los dos últimos años, ticket medio ~575 € y plazo medio de menos de 10 meses (Forbes España/Europa Press, 29-jul-2026). El texto atribuye la cifra a "datos de mercado", sin nombrar autor ni método. Un resumen de búsqueda la atribuía a Equifax; la fuente no lo dice.
- `[Likely]` Funcas estima que entre el 20% y el 35% de los comercios online españoles tendrían una solución BNPL visible o activable, y entre el 40% y el 60% en los grandes, "a falta de datos oficiales por parte del BIS" (Funcas OFT 17/2026, 28-abr-2026, `fuentes/funcas_nota_oft_17_2026.pdf`). Es estimación de Funcas, no medición.
- `[Certain]` Países Bajos, 2024, medido por el regulador (AFM, *BNPL Market Update 2025*, junio 2025): ~53 millones de transacciones por 5.100 M€ (+16% en valor), ticket medio 96,60 €, unos 5,5 millones de usuarios. Es el único dato de un supervisor con su método (`fuentes/afm_marketupdate_bnpl_2025_en.pdf`). Sirve de referencia de orden de magnitud, no de proxy de España.
- `[Likely]` UE: solo hay previsiones de consultoras (por ejemplo, 191.300 M$ de valor de pagos en Europa en 2025, de ResearchAndMarkets) que miden cosas distintas y difieren en dos órdenes de magnitud entre proveedores. **No cito ninguna en el texto del libro sin ver su método.** No he encontrado cifra de la Comisión, del BCE ni de la EBA para el conjunto de la UE.
- `[Certain]` El informe de tendencias de consumo de la EBA 2024-2025 recoge que varias autoridades nacionales han incluido el BNPL en su ley nacional y que preocupa su accesibilidad y el sobreendeudamiento (`fuentes/eba_consumer_trends_report_2024-2025.pdf`). No da un volumen.

### 3.2 Qué modelos quedan dentro de la CCD2

- `[Certain]` La directiva se aplica a los contratos de crédito (art. 2, ap. 1) y ya no tiene el umbral inferior de 200 €. Hay una exclusión de **pagos aplazados** (art. 2, ap. 2, letra h) cuando: el proveedor del bien o servicio da el plazo **sin que un tercero ofrezca crédito**; el precio se debe sin intereses ni otro coste salvo gastos limitados por demora; y el pago se hace íntegro en **50 días**. Si el proveedor no es micro, pequeña ni mediana empresa y vende a distancia (servicios de la sociedad de la información), la exclusión solo vale si no hay tercero que ofrezca ni adquiera el crédito, el pago es en **14 días** y no hay intereses ni otros costes (mismo apartado). Fuente: texto del DOUE, `fuentes/ccd2_es.txt`.
- `[Certain]` Lectura directa: **queda dentro de la CCD2** el BNPL en el que un tercero (plataforma de pagos, entidad financiera, el *fintech*) ofrece o adquiere el crédito, aunque sea sin intereses y a corto plazo; también el pago aplazado propio de un gran comercio online a más de 14 días o con intereses o costes. **Queda fuera** el aplazamiento propio del comercio, sin tercero, sin coste, en 50 días (14 si es un gran comerciante online). Esto es lectura mía del art. 2.2.h; las zonas grises (comercio que cede el crédito a un tercero tras la venta) son tema de R1.
- `[Certain]` Los créditos vigentes a 20-nov-2026 quedan fuera, salvo los arts. 23, 24, 25.1 (segunda frase), 25.2, 28 y 39 para los de duración indefinida (art. 2.2.l).
- `[Certain]` Art. 37: prestamistas y intermediarios no bancarios deben pasar por reconocimiento, registro y supervisión; quedan exentos los bancos, las entidades de pago (por los servicios del punto 4 del anexo I de la PSD2) y las de dinero electrónico (art. 37, ap. 2). Los Estados pueden eximir a micro y pymes que actúen a título subsidiario (ap. 3).
- Efecto en negocio `[Likely]`: el BNPL de un banco o una entidad de pago ya supervisada no necesita autorización nueva; el de un operador sin licencia sí. En España, el anteproyecto crea además dos figuras (EFC de actividad limitada y prestamistas de alto coste). Esto es de R2/R3.

---

## 4. Transposición en otros Estados miembros (a fecha de 2026-11-23)

### 4.1 Cuadro general

- `[Certain]` El plazo de transposición era el 20-nov-2025 y la aplicación es desde el 20-nov-2026. En enero de 2026 la Comisión envió cartas de emplazamiento a 23 Estados miembros. Fuente: Comisión Europea, paquete de infracciones INF/26/1760, copia en `fuentes/r2_comision_INF-26-1760_paquete-infracciones-octubre-2026.json` (guardada por R2).
- `[Certain]` En el paquete de octubre de 2026 la Comisión envió **dictámenes motivados a 16 Estados**: Bulgaria [INFR(2026)0017], Chequia [0031], Estonia [0045], Irlanda [0079], **España [0059]**, Francia [0069], Croacia [0073], Chipre [0023], Letonia [0096], Luxemburgo [0088], Malta [0100], Países Bajos [0108], Polonia [0114], Portugal [0122], Rumanía [0131] y Eslovenia [0141]. Disponen de dos meses (hasta primeros de diciembre de 2026) para responder; si no, la Comisión podría ir al TJUE y pedir sanciones. Misma fuente.
- `[Likely]` La fecha exacta del paquete es 1-oct-2026 (Fintechweekly y Brussels Signal coinciden; la copia de R2 no la he comprobado línea a línea).
- `[Likely]` Según Fintechweekly (17-nov-2026), EUR-Lex no lista medidas nacionales de comunicación para Bulgaria, Chipre, Luxemburgo, Países Bajos, Polonia, Portugal, Rumanía y España. Advierte de que la ausencia de notificación no prueba la ausencia de ley. No he podido leer el registro de EUR-Lex (necesita navegador).
- Lectura: de los 27, 23 recibieron carta en enero y 16 siguen con dictamen motivado. Por lo tanto 7 de los 23 comunicaron transposición completa entre enero y octubre (y 4 más la tenían antes), pero la Comisión no publica cuáles. `[Guessing]` Entre ellos, por lo que he podido leer: Italia, Alemania, Suecia, Austria y Bélgica.

### 4.2 Por país

**Italia.** `[Certain]` Decreto legislativo 31-dic-2025, n. 212, publicado en la *Gazzetta Ufficiale* n. 6 del 9-ene-2026; entra en vigor al día siguiente. Los prestamistas e intermediarios se adaptan **antes del 20-nov-2026 o, si es posterior, a los 90 días de la entrada en vigor de las normas de desarrollo del Banco de Italia**; los contratos anteriores siguen con la norma antigua (art. 6, ap. 2). Modifica el Texto Único Bancario. Fuente: GU, `fuentes/it_GU_2026-01-09_dlgs212-2025.pdf`. Lo llamativo: **la fecha de aplicación efectiva depende del desarrollo del supervisor**. `[Likely]` Italia no aparece en la lista de dictámenes motivados. Sobre límites de coste y BNPL: falta contexto, no he leído los artículos del TUB modificados.

**Alemania.** `[Certain]` Ley de 12-may-2026, BGBl. 2026 I Nr. 139, publicada el 18-may-2026, "para la transposición de la Directiva (UE) 2023/2225" (en el mismo texto se regula el fomento de la movilidad climáticamente neutra). Modifica el BGB (§§ 491 y ss., 505a a 505e) y la EGBGB. Aplica desde el 20-nov-2026; los contratos anteriores siguen con la ley antigua salvo los de duración indefinida y algunos artículos de información (arts. 247 §§ 15 y 17 EGBGB). Fuente: `fuentes/de_BGBl_2026_I_139_umsetzung_ccd.pdf`. En el texto, el aplazamiento sin tercero queda fuera con 50 días (14 días para el gran comercio a distancia) y hay una exclusión específica de tarjetas de débito con pago aplazado a ≤ 40 días y sin intereses (§ 491 reformado). `[Likely]` (fuente secundaria: IWW, Osborne Clarke) endurece el estándar de solvencia: de "sin dudas considerables" a "probable que cumpla" (§ 505a), y obliga a tener en cuenta el BNPL previo. No he encontrado límites de tipos en el texto del BGBl (búsqueda por palabra clave); `[Likely]` que Alemania no ha fijado tope numérico. `[Likely]` (Boersen-Zeitung vía búsqueda) los bancos critican que se estreche el margen en descubiertos tolerados.

**Francia.** `[Certain]` Ley 2025-391 de 30-abr-2025 (art. 2) habilitó al Gobierno a transponer por ordenanza en nueve meses; proyecto de ley de ratificación de la ordenanza 2025-880 de 3-sep-2025 registrado en el Senado el 2-dic-2025 (n.º 173). Fuente: `fuentes/fr_senat_pjl25-173_ratification_ord2025-880.pdf`. `[Likely]` Ordenanza correctora 2025-1154 de 2-dic-2025 y decreto 2026-105 (Dalloz, vie-publique, Fintechweekly). `[Certain]` **Francia figura en la lista de dictámenes motivados** de oct-2026: la Comisión no considera completa la comunicación. `[Likely]` Aplicación desde el 20-nov-2026. Sobre límites de coste y BNPL: falta contexto (Francia ya tiene tasa de usura por categorías, de tradición propia; no lo he verificado).

**Portugal.** `[Certain]` Dictamen motivado [INFR(2026)0122]. `[Likely]` No he encontrado proyecto ni propuesta de ley; la transposición implicaría revisar el Decreto-Lei 133/2009 y la normativa del Banco de Portugal (análisis de despacho). `[Likely]` Algunos comentaristas portugueses señalan que, sin transposición, el consumidor podría invocar la directiva ante el incumplimiento del Estado; la fecha del texto no es clara. Falta contexto: no he podido abrir la base del Parlamento.

**Países Bajos.** `[Certain]` Proyecto 36924 (implementación de la directiva; modifica la Wft, el Libro 7 del Código Civil y otras): presentado el 1-abr-2026; **aprobado en el Tweede Kamer el 6-oct-2026** (16 grupos a favor y 1 en contra, FVD); informe de la comisión de Finanzas del Eerste Kamer el 3-nov-2026; a la espera de la respuesta del Gobierno; sin debate en pleno ni publicación; **la entrada en vigor se fijará por real decreto**, posiblemente por partes. Fuente: Eerste Kamer, ficha del proyecto 36924. `[Likely]` La carta del ministro dice que el BNPL ya cae en el tope general de tipos del crédito al consumo neerlandés y que una prohibición nacional del BNPL en tienda física no es posible con el marco europeo (resumen de búsqueda, no leída en el original).

**Irlanda.** `[Certain]` Dictamen motivado [INFR(2026)0079]. `[Likely]` Consulta pública del Departamento de Finanzas sobre la CCD2 en sept-2024 y un informe de resultados en agosto de 2025; no he podido abrir la página (403). `[Likely]` El Banco Central define BNPL en sus Consumer Protection Regulations 2025, en vigor desde el 24-mar-2026, un instrumento aparte de la transposición. No he encontrado el texto de un proyecto de ley. Falta contexto.

**Otros, de una sola fuente secundaria (`[Likely]`, Fintechweekly 17-nov-2026):** Suecia, Ley de crédito al consumo SFS 2026:1011, adoptada el 27-may-2026; Austria, BGBl. I Nr. 36/2026, publicada el 10-jun-2026 (rige para contratos posteriores al 19-nov-2026); Croacia, NN 86/2026, 7-ago-2026 (el crédito diferido con tarjeta y el pago a plazos, desde el 1-ene-2028); Bélgica, ley publicada el 4-ago-2026. **Contradicción:** Croacia aparece en esa lista como transpuesta y también en la lista oficial de dictámenes motivados de oct-2026. Es coherente si la ley se publicó en agosto y la Comisión no la había valorado; gana la lista oficial para el estado frente a la Comisión, y la ley croata (agosto) como dato de que existe norma.

### 4.3 Decisiones llamativas (límites de coste, BNPL, solvencia)

- `[Certain]` El art. 31, ap. 1 de la CCD2 obliga a "introducir medidas" para evitar tipos, TAE o costes totales excesivos, "tales como límites máximos". No impone topes. Los Estados informan a la Comisión de esas medidas a más tardar el 20-nov-2026, y la Comisión las publicará antes del 20-nov-2027 (art. 31, ap. 3). **Esa publicación será el comparado oficial del cap. 15**, pero llega en 2027.
- Hasta entonces, lo que se sabe de topes nacionales a nivel de transposición es poco: Alemania, sin tope en el texto leído; Países Bajos, usa el tope existente; España, el anteproyecto trae un sistema de TAE máxima por tramos (publicada por el BdE) y un tope transitorio del 22% (CNMC, §3.2.3). `[Guessing]` Italia, Francia y Portugal usan sistemas de usura previos (la MAIN española los cita para su media de ~22,8%, CNMC §3.2.3).
- BNPL: Alemania y Países Bajos aplican la regla de 50/14 días; Croacia difiere el crédito con tarjeta a 2028 (`[Likely]`).
- Solvencia: Alemania endurece el estándar (`[Likely]`).

---

## 5. Posiciones de la industria

- **EBF.** `[Certain]` Documento "EBF's views on the evaluation of the Consumer Credit Directive", 28-abr-2020: considera que la directiva da un marco "sólido"; pide centrarse en aplicar las reglas existentes y evitar el *gold-plating* nacional, supervisar a todos los prestamistas ("same business, same rules, same supervision"), un texto neutral tecnológicamente, simplificar la información precontractual por exceso de carga y **no fijar requisitos rígidos y estandarizados de evaluación de solvencia**, porque podrían excluir a ciertos consumidores y llevarlos al *payday lending*. Fuente: copia local de la descarga de ebf.eu. Es previo a la propuesta de 2021. No he encontrado su posición posterior sobre topes, ni su reacción al acuerdo.
- **ESBG, EACB y WOCCU** (no son la EBF; no atribuir a la EBF). `[Certain]` Carta a los negociadores del trílogo, 29-nov-2022: piden igualdad de trato entre proveedores; en el BNPL, la exención de pagos aplazados del art. 2 les preocupaba por favorecer a las *big tech* (el Consejo proponía 90 días, el compromiso del 15-nov-2022 60 y el Parlamento 45) y piden ir al texto del Parlamento (45); rechazan que se exima de autorización a entidades de pago y de dinero electrónico (art. 37). Sobre solvencia, apoyan la posición del Consejo, quieren poder conceder crédito con evaluación negativa en casos justificados y se oponen a directrices de la EBA. **Sobre topes (art. 31), "contra la introducción obligatoria de topes en general"** y apoyan la posición del Consejo. Fuente: copia local de woccu.org.
- **Lo que quedó en el texto final** `[Certain]`: la exención de pagos aplazados quedó en **50 días** (14 para grandes comercios online sin tercero), y el art. 37 exime a bancos, entidades de pago y de dinero electrónico (apartado 2); el art. 31 obliga a medidas contra costes excesivos, "tales como límites máximos" y no impone topes numéricos. Es decir, el sector consiguió el 50 en vez de 45 y la exención del art. 37, y no consiguió que se eliminara la obligación del art. 31. Mi lectura, no declaración de las asociaciones. No he verificado el estado final de las directrices de la EBA en el art. 18.
- **Eurofinas.** `[Likely]` Richard Knubben (director general de Eurofinas y Leaseurope) acogió el acuerdo provisional como orientado a reforzar la protección "teniendo en cuenta las nuevas realidades digitales" (Vixio, 2022; resumen de búsqueda). No he encontrado su nota de prensa ni sus posiciones sobre topes y BNPL. Falta contexto.
- **BEUC.** `[Certain]` Nota de prensa "Consumers to get much-needed extra protections when taking out a loan" (fecha en la página: 2-dic-2022): celebra que entren el BNPL, el *leasing* y los préstamos de menos de 200 €, una evaluación de solvencia sólida con restricción del crédito si es negativa, el aplazamiento de pagos y el asesoramiento sobre deuda. Lamenta que los Estados miembros eliminaran los topes obligatorios de coste, lo que "carece de ambición". Fuente: beuc.eu. `[Certain]` Matiz mío: el texto final no impone topes, pero sí la obligación de medidas del art. 31.
- **AEB.** Falta contexto: no he encontrado alegaciones ni declaraciones públicas de la AEB sobre el anteproyecto. Busqué en el portal del Ministerio de Consumo, en la CNMC y en prensa; las alegaciones de la audiencia (cerrada el 30-ene-2026) están en el portal de audiencia pública del Ministerio de Economía, que no he podido consultar.
- **ASNEF.** `[Certain]` Artículo de su secretario general, Ignacio Pla Vidal, Noticias Jurídicas, 13-nov-2025: acepta topes si hay categorías de producto claras (y recuerda que el Supremo ya fijó criterios de usura para el *revolving*); pide no frenar el BNPL ni los créditos pequeños con cargas desproporcionadas y una evaluación de solvencia proporcional; "misma actividad, mismas reglas" con registro y supervisión de todos los prestamistas, incluidos los no supervisados por el BdE; impulsar los *bureaus* privados y regular los *credit scores*; simplificar la información precontractual; avisa del riesgo de fragmentación si cada Estado interpreta distinto la proporcionalidad. Es previo al anteproyecto. No he encontrado una reacción pública de ASNEF al tope del 22%.
- **AEFI (fintech).** `[Certain]` Comunicado del 26-ene-2026 (vía Bolsamanía): los topes "podrían resultar incompatibles con muchos modelos de negocios"; teme exclusión financiera en microcréditos; pide diálogo público-privado, registro en el BdE de entidades online no supervisadas y un boletín de tipos del crédito online.
- **ASUFIN y abogados de consumo.** `[Likely]` ASUFIN dijo (12-ene-2026, Law&Trends) que los topes son "muy generosos para la industria y onerosos para el consumidor" y que el legislador eligió la fórmula menos proporcional. Otras voces de abogados critican que el 22% sea provisional y que no regule el mecanismo de amortización del *revolving*.
- **CNMC.** `[Certain]` Informe IPN/CNMC/037/26 (14-sep-2026): advierte de que topes de TAE que "reducirán sustancialmente los ingresos de los prestamistas" pueden provocar racionamiento del crédito y retirada de operadores regulados, que el umbral no debería basarse solo en comparación internacional, y que la carga administrativa de 137 M€ de la MAIN puede ser una barrera de entrada. No es industria, pero es la crítica de más peso técnico.

---

## 6. Estimaciones de impacto

### 6.1 Evaluación de impacto de la Comisión (2021)

Documento: SWD(2021) 170 final, 30-jun-2021, *Impact Assessment Report* que acompaña a la propuesta COM(2021) 347 (copia local: `fuentes/ia_swd2021_170_impact_assessment_en.pdf`). Todo lo siguiente `[Certain]`, leído en el informe.

- **Opción preferida:** la 3a, una enmienda de la CCD con extensión a P2P, créditos < 200 €, créditos sin intereses, todos los descubiertos y todo el *leasing*, y sin extender a casas de empeño ni a créditos > 75.000 €; más prohibición de venta no solicitada, asesoramiento sobre deuda y la **obligación de que los Estados fijen topes de tipo o de TAE, sin reglas sobre cómo calcularlos** (medida 3b.4). Los topes **no se cuantificaron** "por falta de datos consistentes"; el informe dice que se han mostrado muy eficaces, "a menudo con la desaparición de productos de alto riesgo", y que los beneficios superan unos costes "muy limitados" (§8).
- **Costes para las empresas** (solo de la banca, "no los no bancarios", medidas parcialmente cuantificadas; tabla 13, con datos del estudio de apoyo de ICF): sumando las filas de costes directos para empresas, **284,3 M€ únicos y 1.179,1 M€ recurrentes**, total ~1.463 M€; el informe lo redondea a "alrededor de 1.460 M€", debido sobre todo a la ampliación del ámbito (§8.2). Las dos filas mayores son la 2.2 (83,1 M€ únicos y 667,8 M€ recurrentes) y la 2.3/2.7 (70,5 M€ y 318,6 M€). Parte se trasladaría al consumidor. El periodo exacto del coste recurrente no se aclara en la tabla (`[Guessing]` que sea 2021-2030, el horizonte del informe).
- **Beneficios para el consumidor:** unos 1.990 M€ en 2021-2030 por reducción de perjuicio, sobre todo por la extensión del ámbito, la prohibición de venta no solicitada y la información simplificada.
- **Administraciones:** ~3 M€ de costes parcialmente cuantificados y 22,57 M€ al año para servicios de asesoramiento en deuda (230 M€ hasta 2030), con un retorno de 1,4 a 5,3 € por cada euro.
- **Solvencia:** en una simulación, 1.049 M€ de beneficio al consumidor frente a 125 M€ de coste para prestamistas bancarios y no bancarios (relación > 8).
- **Ahorro por simplificación:** 14 M€ (publicidad en radio) y menor coste para "al menos 25 millones de préstamos personales" contratados online al año.
- **Escala del mercado:** crédito al consumo vivo en la UE 1,14 billones € en 2019, el 14,7% de la deuda de los hogares (7,78 billones €), según datos de la EBA (§ de contexto del informe).
- Aviso: el estudio es de 2021 y de la propuesta, no del texto final. El acuerdo final dejó los topes en el art. 31 (medidas "tales como límites máximos") y fijó el BNPL y la solvencia de forma distinta, de modo que los números no se pueden aplicar tal cual.

### 6.2 Estimación del Ministerio de Economía (MAIN del anteproyecto español)

- `[Certain]` La MAIN cuantifica las **nuevas cargas administrativas en 137 M€**, de los que 70 M€ por informar sobre asesoramiento, 25 M€ por remitir a clientes con dificultades a asesores de deuda y 20 M€ por la consulta obligatoria de bases de datos de los prestamistas de alto coste; y reconoce que los topes "reducirán sustancialmente los ingresos de los prestamistas". Fuente: CNMC, IPN/CNMC/037/26, §3.2.3 y §3.2.5 (cita de segunda mano; la MAIN no la he leído). Es estimación del Ministerio.

### 6.3 Estimaciones de consultoras y asociaciones sobre coste de implantación o caída de aprobación

- Falta contexto. No he encontrado ninguna estimación pública, con método, del coste de implantación de la CCD2 para una entidad ni de la caída del volumen de aprobación. Busqué en Banco de España, ASNEF, AEB, EBF/Eurofinas, CNMC y en las páginas de los despachos y consultoras que salieron (Oliver Wyman, PwC, KPMG, Cuatrecasas, CMS). El análisis de Oliver Wyman (feb-2025) sobre BNPL es cualitativo en los fragmentos que vi. `[Guessing]` Habrá que construir los órdenes de magnitud de la Parte V con casos propios, y marcarlos como estimaciones del autor.

---

## Contradicciones y cómo se han resuelto

| Tema | Fuente A | Fuente B | Gana |
|---|---|---|---|
| Tipo medio de consumo 7,60% | Medios: "España" | BdE/BCE 2-sep-2026: zona del euro | La nota oficial; España es 7,16% (TEDR, ago-2026, prov.) |
| Cuota EFC | Medio: 20,1% (2024) | IEF: 20,7% derivado (dic-2024) y 18,9% (dic-2025) | IEF (primaria y más reciente) |
| Nueva producción y saldo "de los EFC" | The Objective: 48.000 M€ y >114.000 M€ | Boletín BdE: 46.639 M€ y 113.345 M€ son el total bancos + EFC | Boletín; la pieza atribuye mal |
| Límite de TAE periodicidad | Nota de Consumo (24-abr-2026): publicación trimestral | CNMC (14-sep-2026), sobre el APL: semestral | Pendiente de R2 (versiones distintas del texto) |
| Interés mensual máximo en alto coste | Nota de Consumo: 4% y comisión del 5% con tope de 30 € | CNMC: 6% y comisiones de 10-15 € | Pendiente de R2; la nota de Consumo parece de una versión posterior (abril) y la CNMC de la que informó |
| Tope del 22%: ¿vigente o previsto? | Medios: "ya obliga a una de cada cuatro tarjetas" | CNMC: tope **transitorio previsto** en la DT 3ª del anteproyecto | CNMC (fuente primaria del texto), a confirmar por R2 |
| Fecha de la nota de Consumo | Nombre de fichero: 24-06-2026 | Cuerpo: "Madrid, 24 de abril de 2026" | Cuerpo del documento |
| Croacia | Fintechweekly: transpuesta (NN 86/2026) | Comisión: dictamen motivado oct-2026 | Ambas (ley de agosto; la Comisión no la valoró en octubre) |

---

## Hallazgos que cambian el índice

1. **Cap. 1 (cifras).** Usar la serie del *Boletín Estadístico* (cuadros 4.13, 19.4, 19.6, 19.12) y no cifras de prensa. Añadir un recuadro "Qué mide cada fuente" (BdE total, ASNEF sin automoción, IEF solo entidades de depósito): las tarjetas se miden por saldo y no por flujo, y esto rompe cualquier "nueva producción total" sumada.
2. **Cap. 2 (contexto).** Añadir la pérdida de cuota de los EFC (18,9%) y que el crecimiento de 2025 lo tiran los bancos. Cambia el relato "las financieras dominan el consumo".
3. **Cap. 15 (comparado).** El comparado detallado de límites de coste no se puede cerrar con fuentes públicas hoy: el art. 31.3 de la CCD2 hace que la Comisión publique las medidas nacionales antes del 20-nov-2027. Proponer un cap. 15 con **tres grupos** (transposición completa con norma publicada: IT, DE, SE, AT, HR, BE; por ordenanza y en ratificación: FR; en trámite o sin ley: NL, ES y el resto del grupo de 16) y marcar la tabla de topes como "a completar".
4. **Calendario.** Añadir un recuadro "20-nov-2026: aplicación sin ley española" con el dictamen motivado a España (INFR(2026)0059), el plazo de dos meses (hasta ~1-dic-2026) y el posible paso al TJUE. Esto afecta al cap. de "qué hago el lunes" y a la Parte VI.
5. **BNPL.** El manual no debe dar un tamaño de mercado como dato. Dar el dato del AFM neerlandés como referencia y las estimaciones españolas marcadas como no oficiales. El cap. de BNPL se apoya mejor en el art. 2.2.h y el art. 37 (qué queda dentro y quién necesita autorización).
6. **Parte V (impacto).** La única estimación cuantificada oficial de coste es de 2021 y sobre la propuesta (1.460 M€ para la banca en la UE) y la de la MAIN (137 M€ de cargas, solo administrativas). No hay *benchmark* de caída de aprobación. Los números de la Parte V serán ejercicios propios.
7. **Italia.** Su aplicación efectiva se vincula al desarrollo de Banca d'Italia (90 días tras sus normas): útil como ejemplo de cómo el supervisor puede mover la fecha, y relevante para el cap. de BdE.

## Huecos

- **Desglose por producto del saldo** (tarjetas, *revolving*, préstamo personal, automoción, punto de venta): no hay serie oficial pública que lo dé; el BdE solo separa "bienes de consumo duradero" y "resto". Lo buscaría en la *Memoria de la CIR* 2025 (`fuentes`: no leída) o en el informe de DBK de pago.
- **Cuotas por entidad de los EFC y banco-EFC en nueva producción:** solo la lista de DBK. Cerraría el estudio completo de DBK o la memoria de ASNEF.
- **Perfil regulatorio de Klarna, PayPal, Aplazame, seQura, Scalapay, Cofidis y Oney en España:** registro de entidades de pago y de EFC del Banco de España. Es lo que decide si el art. 37 les exige autorización nueva.
- **Tamaño del BNPL en la UE y en España con método:** ni la Comisión, ni el BCE ni la EBA lo publican. Cerraría un estudio del BCE o del BIS (Funcas cita un trabajo del BIS de 2023, que no he abierto).
- **Registro de EUR-Lex de medidas nacionales:** no se lee sin navegador (JavaScript). Cerraría abrirlo con Chrome y exportar la tabla por Estado. Con ello se confirmarían Suecia, Austria, Croacia, Bélgica y la lista de los 7 Estados que comunicaron entre enero y octubre.
- **Francia, Portugal, Irlanda:** contenido de la norma (topes, BNPL, solvencia), no leído. Cerraría Légifrance (ordenanzas 2025-880 y 2025-1154, decreto 2026-105), el Diário da República y el Oireachtas.
- **Italia:** contenido de los artículos del TUB sobre topes y BNPL (Normattiva).
- **Posiciones de AEB y de Eurofinas:** alegaciones a la audiencia pública del anteproyecto (cierre 30-ene-2026); notas de prensa de Eurofinas y EBF de 2022-2023.
- **MAIN del anteproyecto:** las cifras de la MAIN (116.026 M€, 500 operadores, 137 M€, 24,36%, 22,8%) las cito a través de la CNMC. Cerraría la MAIN en el portal del Ministerio de Economía.
- **Estimaciones privadas de impacto (coste de implantación, caída de aprobación):** no encontradas.
- **Estado español a fecha de hoy:** lo de R2. Aquí solo registro lo que vi: anteproyecto aprobado en primera vuelta el 7-ene-2026 (Brussels Signal y La Moncloa vía Fintechweekly); a fecha de oct-2026, sin segunda vuelta (Brussels Signal, secundaria); dictamen motivado de 1-oct-2026 (Comisión, primaria). Hay diferencias entre versiones del texto (ver tabla de contradicciones).

## Fuentes

Locales (en `investigacion/fuentes/`):

1. Banco de España, *Boletín Estadístico*, septiembre 2026. Primaria. `bde_boletin_estadistico_2026-09.pdf` (URL: https://www.bde.es/f/webbe/SES/Secciones/Publicaciones/InformesBoletinesRevistas/BoletinEstadistico/26/Fich/be_septiembre2026_es.pdf).
2. Banco de España, *Informe de Estabilidad Financiera*, primavera 2026, cap. 3. Primaria. `bde_ief_primavera2026_cap3.pdf` (https://www.bde.es/f/webbe/Secciones/Publicaciones/InformesBoletinesRevistas/InformesEstabilidadFinancera/26/IEF_2026_1_Cap3.pdf).
3. BCE/BdE, nota de prensa de 2-sep-2026 (tipos de interés de las entidades de crédito de la zona del euro, julio 2026). Primaria. `bde_presbce2026-126.pdf` (https://www.bde.es/f/webbe/GAP/Secciones/SalaPrensa/ComunicadosBCE/NotasInformativasBCE/26/presbce2026-126.pdf). También `bde_presbce2026-80.pdf` (abril 2026), no usada.
4. ASNEF, nota de prensa 29-jun-2026, "La industria de la financiación cierra 2025…". Primaria (asociación sectorial; datos de sus asociados). `asnef_ndp_industria_financiacion_2025.pdf` (https://asnef.com/media/5078/asnef_ndp_la-industria-de-la-financiación-2025.pdf).
5. ASNEF Equifax, *Informe de tendencias de crédito*, junio 2026. Primaria (asociación). `asnef_tendencias_credito_2026-06.pdf` (https://asnef.com/media/5107/informe-tendencias-de-crédito-junio_2026-1.pdf).
6. CNMC, Informe IPN/CNMC/037/26 sobre el anteproyecto de ley de contratos de crédito al consumo, 14-sep-2026. Primaria. `cnmc_6795242.pdf` (https://cnmc.es/sites/default/files/6795242.pdf; hay otra copia de R3 como `cnmc_ipn_037_26.pdf`).
7. Ministerio de Economía, Comercio y Empresa/Consumo, nota informativa "Las nuevas normas sobre créditos al consumo limitarán los intereses…", 24-abr-2026. Primaria. `consumo_NI_credito_consumo_2026-06-24.pdf` (https://portal-cec.consumo.gob.es/sites/default/files/documentos/NI_Credito_Consumo_24_06_2026.pdf).
8. Comisión Europea, SWD(2021) 170 final, *Impact Assessment Report*, 30-jun-2021. Primaria. `ia_swd2021_170_impact_assessment_en.pdf` (copia alojada en https://www.parlament.gv.at/dokument/XXVII/EU/67409/imfname_11079323.pdf).
9. Comisión Europea, paquete de infracciones INF/26/1760 (oct-2026). Primaria. `r2_comision_INF-26-1760_paquete-infracciones-octubre-2026.json` (guardada por R2; URL de origen https://ec.europa.eu/commission/presscorner/detail/es/inf_26_1760). La nota de enero de 2026 (INF/26/115) no la he podido abrir.
10. Directiva (UE) 2023/2225, texto en español. Primaria. `ccd2_es.txt`, `R4-DOUE-Directiva-2023-2225-es.pdf` (EUR-Lex, CELEX 32023L2225).
11. *Gazzetta Ufficiale* n. 6, 9-ene-2026, D.Lgs. 31-dic-2025, n. 212. Primaria. `it_GU_2026-01-09_dlgs212-2025.pdf` (https://www.gazzettaufficiale.it/eli/gu/2026/01/09/6/sg/pdf).
12. *Bundesgesetzblatt* 2026 I Nr. 139, 18-may-2026. Primaria (copia alojada por un tercero, inkasso.de). `de_BGBl_2026_I_139_umsetzung_ccd.pdf` (https://www.inkasso.de/fileadmin/user_upload/Branchennews/2026_05_18_bgbl_139_umsetzung_ccd.pdf).
13. Sénat (Francia), proyecto de ley n.º 173, 2-dic-2025, ratificación de la ordenanza 2025-880. Primaria. `fr_senat_pjl25-173_ratification_ord2025-880.pdf` (https://www.senat.fr/leg/pjl25-173.pdf).
14. AFM (Países Bajos), *Buy Now, Pay Later Market Update 2025*, junio 2025. Primaria (regulador). `afm_marketupdate_bnpl_2025_en.pdf` (https://www.afm.nl/~/profmedia/files/rapporten/2025/rapport-marketupdate-bnpl-2025-eng.pdf).
15. Funcas, Análisis OFT 17/2026, 28-abr-2026, "Compre ahora y pague después". Secundaria (centro de estudios). `funcas_nota_oft_17_2026.pdf`.
16. EBA, *Consumer Trends Report 2024-2025*. Primaria. `eba_consumer_trends_report_2024-2025.pdf`.
17. Informa D&B/DBK, *Entidades de Financiación*, 26ª ed., julio 2026 (ficha-resumen). Secundaria. `dbk_entidades_financieras_2026-08.pdf`.

Solo en web (no guardadas):

18. Eerste Kamer, ficha del proyecto 36924. Primaria. https://www.eerstekamer.nl/wetsvoorstel/36924_implementatiewet_herziene (consultada 2026-11-23).
19. EBF, "EBF's views on the evaluation of the Consumer Credit Directive", 28-abr-2020. Primaria (asociación). https://www.ebf.eu/wp-content/uploads/2020/04/EBFs-views-on-the-evaluation-of-the-Consumer-Credit-Directive.pdf
20. ESBG, EACB y WOCCU, carta a los negociadores del trílogo, 29-nov-2022. Primaria (asociaciones). https://woccu.org/documents/ESBG_EACB_WOCCU_letter_to_trilogue_CCD_review
21. BEUC, nota de prensa "Consumers to get much-needed extra protections when taking out a loan" (2-dic-2022 según la página). Primaria (asociación). https://www.beuc.eu/press-releases/consumers-get-much-needed-extra-protections-when-taking-out-loan
22. Ignacio Pla Vidal (ASNEF), "Hacia una transposición coherente de la directiva…", Noticias Jurídicas, 13-nov-2025. Primaria (posición de ASNEF). https://noticias.juridicas.com/conocimiento/tribunas/20685-hacia-una-transposicion-coherente-de-la-directiva-de-contratos-de-credito-al-consumo:-retos-y-oportunidades/
23. Fintechweekly, "CCD2, BNPL and the November 2026 transposition", 17-nov-2026. **Secundaria**, usada solo para Suecia, Austria, Croacia, Bélgica y la lista del registro de EUR-Lex. https://www.fintechweekly.com/magazine/articles/ccd2-bnpl-consumer-credit-directive-transposition-november-2026
24. Brussels Signal, oct-2026, sobre el dictamen motivado a España. **Secundaria** (prensa). https://brusselssignal.eu/2026/10/brussels-threatens-spain-with-court-action-over-consumer-credit-delay/
25. The Objective, 27-abr-2026, sobre el beneficio de las financieras. **Secundaria** (prensa). https://theobjective.com/economia/banca/2026-04-27/financieras-tres-anos-caida-beneficios-creditos/
26. Forbes España/Europa Press, 29-jul-2026, sobre el BNPL. **Secundaria** (prensa). https://forbes.es/?p=990243
27. Bolsamanía, comunicado de AEFI, 26-ene-2026. **Secundaria** (prensa que recoge el comunicado). https://www.bolsamania.com/noticias_amp/mercados/economiafinanzas--la-aefi-muestra-su-preocupacion-por-los-topes-propuestos-en-la-nueva-ley-de-creditos-al-consumo--21550259.html
28. Law&Trends, 12-ene-2026, sobre las reacciones al anteproyecto. **Secundaria**. https://www.lawandtrends.com/noticias/bancario/el-gobierno-plantea-una-regulacion-de-los-intereses-maximos-del-mercado-de-credito-al-consumo-que-no-convence-a-los-1.html
29. Vixio, reacción de asociaciones al acuerdo provisional (Knubben, Eurofinas), 2022. **Secundaria**; solo vi el resumen de búsqueda. https://www.vixio.com/insights/pc-update-trade-associations-express-cautious-optimism-about-new-eu-consumer

## Correcciones de V1 (2026-11-23)

Informe: `verificacion/informe-v1.md`. Original en `verificacion/originales/`.

- **Resumen 3:** ningún país transpuso en plazo (20-nov-2025). Italia, 31-dic-2025; Alemania, 12/18-may-2026; los demás entre mayo y agosto de 2026. Leer "han publicado ley de transposición", no "en plazo o casi".
- **Tabla de contradicciones (alto coste):** la nota de Consumo de abril reproduce el **texto de enero** (4 % mensual; 5 % con tope de 30 €; trimestral). La CNMC informó sobre el texto recibido el 4-ago-2026, posterior (6 %; 10-15 €; semestral). Gana la CNMC por más reciente.
- **§3.2 y fuentes:** `fuentes/ccd2_es.txt` no existe; es `fuentes/dir-2023-2225-texto-DOUE-original-es.txt`.
- **§4.1:** la fecha del dictamen (1-oct-2026) sube a [Certain].
- Confirmadas las cifras del *Boletín Estadístico*, del IEF y de ASNEF.
- El comparado por países depende de una sola fuente secundaria (Fintechweekly) para Suecia, Austria, Croacia y Bélgica.
- Briefs incumplidos: sin desglose por producto, sin perfil regulatorio de los operadores BNPL (decide el art. 37), Francia, Portugal e Irlanda sin contenido, sin AEB ni Eurofinas.
