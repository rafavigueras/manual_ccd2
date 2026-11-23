---
type: decision-log
created: 2026-11-23
status: active
tags: [ccd2, parte-iv, especialista]
---

# Decisiones de la Parte IV · Adaptar los modelos de admisión

**Autor:** agente especialista en modelos (Opus 5.5), brief `especialista/brief-especialista-modelos.md`.
**Fecha:** 2026-11-23.
**Insumos:** `PROCESO.md`, índice v0.2, R1, R2 y R4 con sus "Correcciones de V1", `investigacion/verificacion/informe-v1.md` y, como fuente primaria directa, el texto de enero del anteproyecto (`fuentes/mineco_anteproyecto_ley_credito_consumo_2026-01-08.pdf`, arts. 31 a 33). Para alinear el hilo conductor se ha leído (sin tocarlo) el cap. 5 de `manual/parte-01.html` y el 9.6 de `manual/parte-02.html`.

## 1. Qué se entrega

| Fichero | Contenido |
|---|---|
| `manual/parte-04.html` | Caps. 20 a 26, unas 18.500 palabras. `revision.py`: OK |
| `anexos/s2_scorecard.py` | Cartera sintética (300.000 solicitudes, semilla 20261120), apartados a) a f). Ejecutado |
| `anexos/s3_sesgo.py` | Disparidad por nacionalidad sobre S2, apartados 0 a 5. Ejecutado. Importa S2 (añade su carpeta a `sys.path`, necesario con `-I`) |

Palabras por capítulo: 20 · 2.437; 21 · 3.096; 22 · 2.457; 23 · 2.763; 24 · 2.478; 25 · 2.222; 26 · 2.656. Los caps. 20, 22, 24 y 25 quedan algo por debajo de las 2.500 orientativas del brief: se ha preferido no rellenar.

Bloques: 7 CASO (uno por capítulo), 5 NÚMEROS (21.2, 22.4, 23.2, 24.2, 25.3.1), 2 PALANCA (21.2 y 22.4, con impacto en aprobación y morosidad), 6 NORMA, 4 DEFENSA, 6 TRAMPA, 4 QUÉ VIENE, 3 CÓDIGO, 2 MARGEN, 1 POR QUÉ, y el recuadro "Qué deberías saber hacer ahora".

## 2. Decisiones de estructura (desviaciones del índice v0.2)

1. **Se mantiene la estructura 20-26 y la numeración del índice.** Los anclajes `cap20` a `cap26` y `sN-M` coinciden con `index.html`.
2. **Dos apartados de cuarto nivel nuevos en el 25.3:** 25.3.1 (*reject inference* y evaluar con datos del modelo viejo, que pedía el brief en el punto 6) y 25.3.2 (seguimiento tras el despliegue). El índice solo tenía "25.3 Gobierno y validación".
3. **Un NÚMEROS más de los exigidos, en 23.2:** los motivos de denegación de un solicitante y su contrafactual, calculados en S2 (e). Da contenido real al 9.6 de la Parte II, que remite a la Parte IV.
4. **En 20.3 se añade un párrafo con las dos versiones (banco grande con IRB y entidad pequeña con proveedor)**, que pedía el brief; la versión por tamaño reaparece en 25.1, 26.1 y 26.4.
5. **No se ha hecho la tabla de equivalencias art. 18 CCD2 / art. 22 RGPD / AI Act / GL 2020/06 como anexo** (hallazgo 5 de R4). La tabla de 23.1 cubre lo esencial. Propuesta: que la sesión principal la monte en los anexos de referencia (R2) a partir del anexo de la carta de la EBA de 21-nov-2025.

## 3. Decisiones de fondo (para que Rafa las vea)

1. **Arquitectura recomendada para la capacidad de pago:** la carga de la operación (DSTI con la cuota nueva) dentro del modelo, para ordenar, y una regla de capacidad como suelo que impide conceder con resultado negativo (art. 18(6)). S2 lo respalda: a igual aprobación, el integrado tiene menos morosidad que la regla secuencial (3,27 % frente a 3,50 %).
2. **Tratar una *scorecard* logística como "sistema de IA" a efectos de gobierno**, aunque la pregunta esté abierta. Razón: el coste marginal es bajo para una entidad financiera (art. 17.4 AI Act) y el de equivocarse, alto (art. 99.4).
3. **Separar el corte comercial del suelo de solvencia** (25.3.1): es lo que permite seguir haciendo experimentación controlada por debajo del corte sin incumplir el art. 18(6).
4. **Retirar la zona postal** como ejemplo de proxy sin justificación, y **mantener el historial crediticio** aunque reconstruya mejor la nacionalidad: el criterio es el test de justificación objetiva (Ley 15/2022, art. 4.2; art. 6 CCD2), no el poder de reconstrucción.
5. **Rechazo explícito de cortes distintos por grupo** para corregir disparidad (24.3, TRAMPA).
6. **Priorización en tres niveles** (exigible ya, prudente ya, puede esperar) coherente con la de 4.3.1 de la Parte I. Se añaden al "exigible ya" la Directriz EBA/GL/2020/06 (adoptada por el BdE) y la Ley 15/2022, que la Parte I no lista.
7. **Presupuesto (26.4):** las cifras de persona-mes y coste son **estimaciones del autor**, no mediciones. Para respetar la regla de que ninguna cifra se publique sin ejecutarse, los supuestos están en S2 (f) y el script hace la suma (92 y 19 persona-mes; 1,20 y 0,21 M EUR). Si Rafa prefiere no publicar cifras de coste, basta con quitar la fila de coste de la tabla de 26.4.

## 4. La cartera sintética: supuestos y límites

- **Productos alineados con la entidad de referencia del cap. 5:** la cartera de solicitudes reparte importes alrededor de los productos tipo (tarjeta de 1.000 a 6.000 EUR con cuota de evaluación al 25 % anual del límite, Orden EHA/2899/2011 art. 18.2.e; préstamo de 3.000 a 30.000 EUR a 36-96 meses al 9,9 % nominal, el tipo del cap. 5; BNPL de 60 a 1.500 EUR a 3, 6 o 12 plazos sin intereses). **Diferencia con el cap. 5:** el BNPL de S2 no modela la variante a doce meses con comisión del 3 %; y el préstamo tipo del cap. 5 (6.000 EUR a 36 meses) no es el solicitante de ejemplo de 23.2 (28.200 EUR), elegido porque su motivo principal es la carga de cuotas.
- **Mecanismo generador:** un rasgo latente de comportamiento de pago, no observable, más carga real (DSTI) y renta residual. La nacionalidad no tiene efecto causal directo; la zona postal tiene un efecto propio pequeño. Las variables "prohibidas" (señal de redes sociales, gama del dispositivo) están construidas para tener algo de poder predictivo, como en la práctica.
- **Robustez:** con las semillas 1 y 2 (prueba manual, no incluida en el script) las conclusiones no cambian: retirar las tres variables cuesta 1,2-1,3 p. de Gini y 1,7-2,1 p. de aprobación; la regla, unos 6 p. de aprobación; *open banking* con cobertura total, +4,2-4,4 p. de Gini sobre el integrado; quitar la nacionalidad deja el cociente de aprobación igual o peor; quitar la zona lo sube unas tres centésimas por una o dos décimas de Gini; la referencia no observable deja un cociente de 0,88-0,90. Las cifras del libro son las de la semilla fija.
- **Límites que conviene decir si alguien pregunta:** todos los solicitantes tienen resultado observado (no hay truncamiento salvo en el experimento d); la tasa de impago "a la puerta" (9,7 %) es alta frente al 3,6 % de dudosos de los EFC (IEF) porque mide solicitudes, no cartera; el baremo de gastos (450 EUR más 150 por miembro adicional) es sintético, no del INE; el consentimiento a *open banking* (53 %) es un supuesto.
- **Si se toca un script, hay que revisar el texto:** todas las cifras de la Parte IV se han auditado contra la salida ejecutada (comparación automática de todos los números con decimales del texto contra la salida de S2 y S3; solo quedan fuera parámetros e importes ilustrativos: 1.500, 18.000, 30.000 y 500.000).

## 5. Huecos normativos (lo que queda abierto)

1. **C-203/22 (Dun & Bradstreet):** V1 pedía leer el texto íntegro antes de F4-E. **No se ha leído.** En el texto se cita siempre "según el comunicado del TJUE". Cerrar con curia.europa.eu (ECLI:EU:C:2025:117).
2. **¿Es una *scorecard* logística un "sistema de IA" (art. 3.1 AI Act)?** Sin leer las directrices de la Comisión sobre la definición (feb-2025). El texto lo trata como pregunta abierta y recomienda gobernarla como si lo fuera.
3. **"Cambios significativos de diseño" (art. 111.2 en la redacción del *Omnibus*):** sin criterio publicado. El texto pide a la entidad un criterio propio por escrito.
4. **Anexo del RTS EBA/RTS/2026/05 (cambios materiales IRB):** no extraído; su adopción por la Comisión no consta. El 25.1 se escribe en cualitativo y el RTS va en un QUÉ VIENE.
5. **Número oficial del *Omnibus* (2026/1744):** sigue sin fuente primaria. El texto no da el número: "Reglamento *Digital Omnibus* sobre IA, firmado el 8 de julio de 2026".
6. **Texto de septiembre del anteproyecto:** no leído; los arts. 28-30 (y el 29 para la intervención humana) se citan "según la CNMC". Las consecuencias civiles (pérdida o reducción de intereses) van en QUÉ VIENE sin cifras.
7. **Afirmaciones de conocimiento propio, no recogidas en R1, R2 ni R4,** que conviene verificar en la revisión: (a) que la Ley 16/2011 no prevé una consecuencia civil específica por evaluar mal la solvencia (CASO de 22.4); (b) que la nacionalidad no es categoría especial del art. 9 RGPD (24.1); (c) la regla estadounidense de los cuatro quintos, citada como convención de aquel país (24.2).
8. **Afirmaciones de R3 usadas sin estar en los insumos del brief:** art. 18.2.e de la Orden EHA/2899/2011 (25 % anual como criterio de evaluación), en la redacción corregida por V1; coincide con la Parte I.
9. **Sin guía del Banco de España sobre *scoring* o IA:** se dice así en 26.6, junto con la advertencia de que la "circular de 2026" que circula en blogs no consta en fuente oficial.

## 6. Pendiente para la sesión principal

- Comprobar visualmente `parte-04.html` (claro y oscuro); solo se ha pasado `revision.py`.
- Los enlaces a `parte-03.html` y `parte-05.html` (navegación) quedan como pendientes hasta que existan. Las remisiones a otros capítulos van en texto ("cap. 17"), sin enlace.
- `anexos-codigo.html`: presentar S2 y S3 con su salida. Coordinar con S1 si se quiere que el préstamo tipo use también la comisión de apertura del 1,5 % del cap. 5 (S2 no la modela).
- Si en la revisión se discrepa del fondo (arquitectura integrada más suelo, tratamiento de la *scorecard* como sistema de IA, retirada de la zona, cifras de presupuesto), anotarlo aquí y consultarlo con Rafa, como dice `PROCESO.md` §9.
