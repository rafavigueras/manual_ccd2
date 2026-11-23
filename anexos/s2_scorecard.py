"""S2 · Scorecard sintética de admisión de consumo y su adaptación a la CCD2.

Anexo de código del Manual de crédito al consumo (Parte IV). Genera una cartera sintética
de solicitudes de la entidad de referencia del manual (tarjeta revolving, préstamo personal
digital y BNPL en el punto de venta), entrena una scorecard logística de referencia y mide:

  (a) el efecto en Gini y en tasa de aprobación a igual morosidad de retirar tres variables
      que con la CCD2 pasan a estar prohibidas o en duda (señal de redes sociales,
      nacionalidad y gama del dispositivo);
  (b) el efecto de añadir una regla de capacidad de pago (secuencial e integrada, estricta y
      proporcional), y qué perfiles se caen;
  (c) la mejora de añadir variables derivadas de movimientos de cuenta (open banking);
  (d) el sesgo de medir un modelo nuevo solo con los aprobados por el modelo viejo;
  (e) los motivos de denegación de un solicitante concreto y un contrafactual;
  (f) el orden de magnitud del esfuerzo del programa de modelos, con supuestos explícitos
      (estimación del autor, no una medición de mercado).

Todo es sintético: ninguna cifra describe a una entidad real ni al mercado español. Lo que
importa son los órdenes de magnitud y el método, no los decimales.

Uso:  .venv/bin/python -I anexos/s2_scorecard.py      (desde la raíz del proyecto)
"""
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

SEMILLA = 20261120          # fecha de aplicación de la CCD2
N = 300_000                 # solicitudes
APROBACION_REFERENCIA = 0.70  # punto de operación del modelo actual
PROB_CONSENTIMIENTO_OB = 0.50  # parte de solicitantes que comparte sus cuentas

PRODUCTOS = ["revolving", "prestamo", "bnpl"]

# Supuestos de esfuerzo del programa de modelos (persona-mes): banco grande con IRB y varias
# scorecards propias; entidad pequeña sin modelos internos y con scorecard de proveedor.
ESFUERZO = [
    ("Diagnóstico e inventario de modelos, reglas y variables", 6.0, 1.5),
    ("Reentrenamiento y validación de scorecards", 30.0, 5.0),
    ("Regla de capacidad de pago y estimación de gastos", 8.0, 2.0),
    ("Integración y variables de open banking", 12.0, 3.0),
    ("Motivos de denegación, explicaciones y revisión humana", 10.0, 3.0),
    ("Pruebas de sesgo y gobierno del dato", 6.0, 1.5),
    ("Impacto en IRB, IFRS 9, pricing y stress test", 12.0, 1.0),
    ("Documentación (art. 18.4 CCD2 y AI Act)", 8.0, 2.0),
]
COSTE_PM = {"grande": 13000, "pequena": 11000}  # coste medio interno y externo, EUR


# ---------------------------------------------------------------------------
# 1. Generación de la cartera sintética
# ---------------------------------------------------------------------------

def generar_cartera(n=N, semilla=SEMILLA):
    """Devuelve un DataFrame con una fila por solicitud y su resultado a 12 meses."""
    rng = np.random.default_rng(semilla)
    d = pd.DataFrame(index=range(n))

    d["producto"] = rng.choice(PRODUCTOS, size=n, p=[0.35, 0.40, 0.25])
    d["extranjero"] = (rng.random(n) < 0.14).astype(int)

    # Edad: los extranjeros de la muestra son algo más jóvenes.
    edad = rng.normal(43, 12, n) - 6 * d["extranjero"]
    d["edad"] = np.clip(edad, 18, 79).round()

    d["miembros_hogar"] = rng.choice([1, 2, 3, 4, 5], size=n, p=[0.25, 0.30, 0.22, 0.17, 0.06])

    # Situación laboral.
    u = rng.random(n)
    p_temporal = 0.16 + 0.12 * d["extranjero"] + 0.10 * (d["edad"] < 30)
    contrato = np.where(u < p_temporal, "temporal",
               np.where(u < p_temporal + 0.12, "autonomo", "indefinido"))
    contrato = np.where(d["edad"] >= 66, "pensionista", contrato)
    d["contrato"] = contrato
    d["antig_empleo_m"] = np.round(
        rng.exponential(24 + 2.2 * np.clip(d["edad"] - 18, 0, None), n)
        * np.where(d["contrato"] == "temporal", 0.3, 1.0))

    # Rasgo latente de comportamiento de pago: no observable directamente.
    z = rng.normal(0, 1, n)
    d["_z"] = z

    # Ingresos netos mensuales reales.
    log_ing = (np.log(1650) + 0.18 * np.tanh((d["edad"] - 25) / 15)
               - 0.20 * (d["contrato"] == "temporal") - 0.12 * d["extranjero"]
               + 0.10 * z + rng.normal(0, 0.38, n))
    d["ingresos_reales"] = np.exp(log_ing).round()
    # Ingresos declarados: se sobredeclaran más cuanto peor es el rasgo latente.
    sobre = np.clip(rng.normal(0.06 - 0.05 * z, 0.10, n), -0.05, None)
    d["ingresos_declarados"] = (d["ingresos_reales"] * (1 + sobre)).round()

    # Zona postal: índice de riesgo de 1 (bajo) a 10 (alto). Correlaciona con renta y origen.
    zona_lat = (-0.8 * (log_ing - log_ing.mean()) / log_ing.std() + 1.0 * d["extranjero"]
                + rng.normal(0, 1, n))
    d["zona"] = pd.qcut(zona_lat, 10, labels=False) + 1

    # Datos de bureau y CIR.
    d["meses_historial"] = np.round(np.clip(
        rng.gamma(2.0, 40, n) * np.clip((d["edad"] - 18) / 25, 0.15, 1.6)
        * np.where(d["extranjero"] == 1, 0.40, 1.0), 0, 480))
    d["incidencias"] = (rng.random(n) < 1 / (1 + np.exp(2.7 + 0.9 * z))).astype(int)
    d["consultas_6m"] = rng.poisson(np.exp(0.2 - 0.35 * z + 0.25 * (d["producto"] == "bnpl")))
    d["utilizacion"] = np.clip(1 / (1 + np.exp(0.6 + 0.8 * z + rng.normal(0, 0.8, n))), 0, 1)
    # Un 30 % no tiene otras deudas; el resto paga cuotas que suben cuanto peor es el rasgo latente.
    ratio_cuotas = np.where(rng.random(n) < 0.30, 0.0,
                            np.clip(rng.beta(1.6, 9, n) * (1.25 - 0.25 * z), 0, 0.8))
    d["cuotas_existentes"] = (ratio_cuotas * d["ingresos_reales"]).round()

    # Importe solicitado y cuota mensual según producto.
    ing = d["ingresos_reales"].to_numpy()
    imp = np.zeros(n)
    cuota = np.zeros(n)
    rev = d["producto"].eq("revolving").to_numpy()
    pre = d["producto"].eq("prestamo").to_numpy()
    bnp = d["producto"].eq("bnpl").to_numpy()
    imp[rev] = rng.choice([1000, 1500, 2000, 3000, 4000, 6000], rev.sum(),
                          p=[0.15, 0.20, 0.25, 0.20, 0.12, 0.08])
    # Criterio del art. 18.2.e) de la Orden EHA/2899/2011: cuota que amortice el 25 % anual
    # del límite en doce plazos mensuales iguales (sin intereses, simplificación).
    cuota[rev] = imp[rev] * 0.25 / 12
    imp[pre] = np.clip(rng.lognormal(np.log(9000), 0.6, pre.sum()) * (ing[pre] / 1650) ** 0.4,
                       3000, 30000).round(-2)
    plazo = rng.choice([36, 48, 60, 72, 84, 96], pre.sum())
    i_m = 0.099 / 12          # tipo nominal del préstamo de la entidad de referencia (cap. 5)
    cuota[pre] = imp[pre] * i_m / (1 - (1 + i_m) ** -plazo)
    imp[bnp] = np.clip(rng.lognormal(np.log(420), 0.7, bnp.sum()), 60, 1500).round()
    cuota[bnp] = imp[bnp] / rng.choice([3, 6, 12], bnp.sum(), p=[0.45, 0.35, 0.20])
    d["importe"] = imp
    d["cuota_nueva"] = cuota.round(2)

    # Variables que la CCD2 pone en duda o prohíbe.
    # Señal de un proveedor de "huella digital" construida en parte con redes sociales.
    d["senal_redes"] = 0.55 * z - 0.25 * (d["edad"] - 43) / 12 + rng.normal(0, 0.85, n)
    # Gama alta del dispositivo desde el que se solicita (proxy de renta y edad).
    p_gama = 1 / (1 + np.exp(-(0.9 * (log_ing - np.log(1650)) / 0.4 - 0.02 * (d["edad"] - 43)
                               + 0.25 * z - 0.2)))
    d["gama_alta"] = (rng.random(n) < p_gama).astype(int)

    # Movimientos de cuenta (open banking), disponibles si el cliente consiente.
    dsti_real = (d["cuotas_existentes"] + d["cuota_nueva"]) / d["ingresos_reales"]
    d["ob_ingresos"] = (d["ingresos_reales"] * rng.normal(1.0, 0.04, n)).round()
    d["ob_dias_descubierto"] = rng.poisson(np.exp(0.4 - 0.85 * z + 1.5 * np.clip(dsti_real, 0, 1)))
    d["ob_devoluciones"] = rng.poisson(np.exp(-1.4 - 0.8 * z))
    gasto_esencial = np.clip(rng.normal(0.55, 0.12, n) + 0.04 * (d["miembros_hogar"] - 2)
                             - 0.05 * z, 0.2, 1.1)
    d["ob_ratio_gasto"] = gasto_esencial.round(3)
    p_cons = PROB_CONSENTIMIENTO_OB + 0.10 * (d["edad"] < 40) - 0.10 * (d["edad"] >= 60)
    d["consiente_ob"] = (rng.random(n) < p_cons).astype(int)

    # Resultado: impago de 90 días o más en los 12 meses siguientes.
    renta_residual = d["ingresos_reales"] * (1 - gasto_esencial) - d["cuotas_existentes"] - d["cuota_nueva"]
    base = {"revolving": -3.05, "prestamo": -3.45, "bnpl": -3.15}
    logit = (d["producto"].map(base)
             - 1.05 * z
             + 0.95 * d["incidencias"]
             + 0.10 * d["consultas_6m"]
             + 0.55 * (d["contrato"] == "temporal") + 0.30 * (d["contrato"] == "autonomo")
             - 0.12 * np.log1p(d["antig_empleo_m"])
             + 0.60 * d["utilizacion"]
             + 0.025 * (d["zona"] - 5.5)
             - 0.004 * d["meses_historial"].clip(0, 120)
             + 3.0 * np.clip(dsti_real - 0.35, 0, None)
             + 0.9 * (renta_residual < 0))
    d["impago"] = (rng.random(n) < 1 / (1 + np.exp(-logit))).astype(int)
    d["dsti_real"] = dsti_real
    d["renta_residual_real"] = renta_residual
    d["muestra"] = np.where(rng.random(n) < 0.5, "desarrollo", "prueba")
    return d


# ---------------------------------------------------------------------------
# 2. Variables y modelos
# ---------------------------------------------------------------------------

def matriz(d, variables):
    """Construye la matriz de entrada con las transformaciones habituales de una scorecard."""
    x = pd.DataFrame(index=d.index)
    for v in variables:
        if v == "producto":
            x["prod_rev"] = (d["producto"] == "revolving").astype(int)
            x["prod_bnpl"] = (d["producto"] == "bnpl").astype(int)
        elif v == "contrato":
            for c in ["temporal", "autonomo", "pensionista"]:
                x["contrato_" + c] = (d["contrato"] == c).astype(int)
        elif v == "edad":
            x["edad_menor_25"] = (d["edad"] < 25).astype(int)
            x["edad_25_35"] = ((d["edad"] >= 25) & (d["edad"] < 35)).astype(int)
            x["edad_mayor_60"] = (d["edad"] >= 60).astype(int)
        elif v in ("ingresos_declarados", "ob_ingresos"):
            x["log_" + v] = np.log(d[v].clip(300))
        elif v == "dti_existente":
            x[v] = (d["cuotas_existentes"] / d["ingresos_declarados"]).clip(0, 1.5)
        elif v == "dsti_declarado":
            x[v] = ((d["cuotas_existentes"] + d["cuota_nueva"]) / d["ingresos_declarados"]).clip(0, 1.5)
        elif v == "dsti_ob":
            x[v] = ((d["cuotas_existentes"] + d["cuota_nueva"]) / d["ob_ingresos"]).clip(0, 1.5)
        elif v == "antig_empleo_m":
            x["log_antig_empleo"] = np.log1p(d[v])
        elif v == "meses_historial":
            x["historial_120"] = d[v].clip(0, 120)
        else:
            x[v] = d[v]
    return x


COMUNES = ["producto", "edad", "contrato", "antig_empleo_m", "zona", "meses_historial",
           "incidencias", "consultas_6m", "utilizacion", "dti_existente"]
VARS_ACTUAL = COMUNES + ["ingresos_declarados", "senal_redes", "extranjero", "gama_alta"]
VARS_LIMPIO = COMUNES + ["ingresos_declarados"]
VARS_OB = [v for v in COMUNES if v != "dti_existente"] + [
    "ob_ingresos", "ob_dias_descubierto", "ob_devoluciones", "ob_ratio_gasto"]


def entrenar(d, variables, filtro=None):
    """Regresión logística sobre la muestra de desarrollo (o un subconjunto)."""
    des = d[d["muestra"] == "desarrollo"]
    if filtro is not None:
        des = des[filtro.loc[des.index]]
    modelo = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000, C=1.0))
    modelo.fit(matriz(des, variables), des["impago"])
    return modelo


def puntuar(modelo, d, variables):
    return modelo.predict_proba(matriz(d, variables))[:, 1]


def gini(y, pd_):
    return 2 * roc_auc_score(y, pd_) - 1


def corte_por_aprobacion(pd_, tasa):
    """Umbral de PD que aprueba la proporción `tasa` de solicitudes."""
    return np.quantile(pd_, tasa)


def aprobacion_a_igual_morosidad(y, pd_, mora_objetivo):
    """Máxima tasa de aprobación cuya morosidad de aprobados no supera la objetivo."""
    orden = np.argsort(pd_)
    y_ord = np.asarray(y)[orden]
    mora_acum = np.cumsum(y_ord) / np.arange(1, len(y_ord) + 1)
    validos = np.where(mora_acum <= mora_objetivo)[0]
    return (validos.max() + 1) / len(y_ord) if len(validos) else 0.0


def pct(x, dec=1):
    return f"{100 * x:.{dec}f} %".replace(".", ",")


def pp(x):
    """Diferencia en puntos porcentuales con signo y coma decimal."""
    return f"{100 * x:+.1f} p.".replace(".", ",", 1)


def num(x, dec=0):
    s = f"{x:,.{dec}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


# ---------------------------------------------------------------------------
# 3. Regla de capacidad de pago
# ---------------------------------------------------------------------------

def gastos_baremo(d):
    """Gasto mínimo de vida mensual por hogar: baremo sintético, no una cifra del INE."""
    return 450 + 150 * (d["miembros_hogar"] - 1)


def regla_capacidad(d, ingresos, dsti_max=0.40, proporcional=False):
    """True si la solicitud pasa la regla de capacidad de pago.

    Dos condiciones: cuotas totales sobre ingresos (DSTI) no superior a `dsti_max` y renta
    residual no negativa tras gastos de baremo, cuotas existentes y cuota nueva. En la versión
    proporcional, los BNPL de hasta 300 EUR y las tarjetas de hasta 1.500 EUR solo comprueban
    un DSTI de hasta el 50 %, sin baremo de gastos.
    """
    dsti = (d["cuotas_existentes"] + d["cuota_nueva"]) / ingresos
    residual = ingresos - gastos_baremo(d) - d["cuotas_existentes"] - d["cuota_nueva"]
    pasa = (dsti <= dsti_max) & (residual >= 0)
    if proporcional:
        pequeno = ((d["producto"] == "bnpl") & (d["importe"] <= 300)) | \
                  ((d["producto"] == "revolving") & (d["importe"] <= 1500))
        pasa = np.where(pequeno, dsti <= 0.50, pasa)
    return pd.Series(pasa, index=d.index).astype(bool)


# ---------------------------------------------------------------------------
# 4. Ejecución
# ---------------------------------------------------------------------------

def titulo(t):
    print("\n" + t)
    print("-" * len(t))


def main():
    d = generar_cartera()
    p = d[d["muestra"] == "prueba"].copy()
    y = p["impago"].to_numpy()

    titulo("0. Cartera sintética")
    print(f"Solicitudes: {num(len(d))} (desarrollo {num((d['muestra'] == 'desarrollo').sum())}, "
          f"prueba {num(len(p))})")
    for prod in PRODUCTOS:
        s = d[d["producto"] == prod]
        print(f"  {prod:10} {pct(len(s) / len(d))} de las solicitudes · importe medio "
              f"{num(s['importe'].mean())} EUR · cuota media {num(s['cuota_nueva'].mean())} EUR · "
              f"impago a 12 meses (todas las solicitudes) {pct(s['impago'].mean())}")
    print(f"  Total: impago medio de las solicitudes {pct(d['impago'].mean())}; "
          f"extranjeros {pct(d['extranjero'].mean())}; consienten open banking "
          f"{pct(d['consiente_ob'].mean())}")

    # (a) Modelo actual y retirada de variables -----------------------------------
    m_act = entrenar(d, VARS_ACTUAL)
    pd_act = puntuar(m_act, p, VARS_ACTUAL)
    g_act = gini(y, pd_act)
    corte = corte_por_aprobacion(pd_act, APROBACION_REFERENCIA)
    aprob = pd_act <= corte
    mora_obj = y[aprob].mean()

    titulo("a) Retirada de variables prohibidas o en duda")
    print(f"Modelo actual (14 variables): Gini {pct(g_act)}; aprobando el "
          f"{pct(APROBACION_REFERENCIA, 0)}, morosidad de aprobados {pct(mora_obj, 2)}")
    print("Esa morosidad es la referencia: cada modelo se compara por la aprobación que alcanza sin superarla.")

    filas = [("Actual", VARS_ACTUAL)]
    for v, nombre in [("senal_redes", "sin señal de redes sociales"),
                      ("extranjero", "sin nacionalidad"),
                      ("gama_alta", "sin gama del dispositivo")]:
        filas.append((nombre, [x for x in VARS_ACTUAL if x != v]))
    filas.append(("Limpio (sin las tres)", VARS_LIMPIO))
    filas.append(("Limpio y sin edad (sensibilidad)", [x for x in VARS_LIMPIO if x != "edad"]))
    resultados_a = {}
    for nombre, vars_ in filas:
        m = m_act if nombre == "Actual" else entrenar(d, vars_)
        pd_ = puntuar(m, p, vars_)
        g = gini(y, pd_)
        ap = aprobacion_a_igual_morosidad(y, pd_, mora_obj)
        resultados_a[nombre] = (g, ap, m, pd_)
        print(f"  {nombre:33} Gini {pct(g)} ({pp(g - g_act)})  aprobación a igual "
              f"morosidad {pct(ap)} ({pp(ap - APROBACION_REFERENCIA)})")

    g_lim, ap_lim, m_lim, pd_lim = resultados_a["Limpio (sin las tres)"]
    # Retirada sin reentrenar: se pone la variable a su media (lo que hace quien "apaga" la variable).
    p_neutra = p.copy()
    des = d[d["muestra"] == "desarrollo"]
    for v in ["senal_redes", "extranjero", "gama_alta"]:
        p_neutra[v] = des[v].mean()
    pd_neutra = puntuar(m_act, p_neutra, VARS_ACTUAL)
    g_neutra = gini(y, pd_neutra)
    print(f"  {'Apagadas sin reentrenar':33} Gini {pct(g_neutra)} ({pp(g_neutra - g_act)})  "
          f"aprobación a igual morosidad {pct(aprobacion_a_igual_morosidad(y, pd_neutra, mora_obj))}; "
          f"con el corte actual, morosidad {pct(y[pd_neutra <= corte].mean(), 2)}")
    # Si se mantiene el corte de PD del modelo actual con el modelo limpio:
    aprob_lim_mismo_corte = pd_lim <= corte
    print(f"  Limpio con el mismo corte de PD que el actual: aprobación "
          f"{pct(aprob_lim_mismo_corte.mean())}, morosidad {pct(y[aprob_lim_mismo_corte].mean(), 2)}")
    coincide = (aprob == (pd_lim <= corte_por_aprobacion(pd_lim, APROBACION_REFERENCIA))).mean()
    print(f"  Al 70 % de aprobación, el modelo actual y el limpio coinciden en el {pct(coincide)} "
          f"de las decisiones (el resto son cambios de sentido)")

    # (b) Regla de capacidad de pago ----------------------------------------------
    titulo("b) Regla de capacidad de pago (DSTI <= 40 % y renta residual >= 0, sobre el modelo limpio)")
    corte_lim = corte_por_aprobacion(pd_lim, APROBACION_REFERENCIA)
    ap_score = pd_lim <= corte_lim
    regla_decl = regla_capacidad(p, p["ingresos_declarados"]).to_numpy()
    regla_prop = regla_capacidad(p, p["ingresos_declarados"], proporcional=True).to_numpy()
    regla_ob = regla_capacidad(p, p["ob_ingresos"]).to_numpy()
    print(f"Solo scorecard limpia: aprobación {pct(ap_score.mean())}, morosidad {pct(y[ap_score].mean(), 2)}")
    for nombre, regla in [("Secuencial, ingresos declarados", regla_decl),
                          ("Secuencial, proporcional por importe", regla_prop),
                          ("Secuencial, ingresos verificados (cuentas)", regla_ob)]:
        ap = ap_score & regla
        caen = ap_score & ~regla
        print(f"  {nombre:42} aprobación {pct(ap.mean())} ({pp(ap.mean() - ap_score.mean())}), "
              f"morosidad {pct(y[ap].mean(), 2)}; caen {pct(caen.mean())} de las solicitudes con "
              f"morosidad {pct(y[caen].mean(), 1)}")
    caen = ap_score & ~regla_decl
    quedan = ap_score & regla_decl
    print("  Quién se cae con la regla estricta (frente a quien sigue aprobado):")
    perfil = pd.DataFrame({
        "caen": [p.loc[caen, "ingresos_declarados"].median(), p.loc[caen, "edad"].mean(),
                 (p.loc[caen, "contrato"] == "temporal").mean(), p.loc[caen, "miembros_hogar"].mean(),
                 (p.loc[caen, "cuotas_existentes"] / p.loc[caen, "ingresos_declarados"]).median()],
        "siguen": [p.loc[quedan, "ingresos_declarados"].median(), p.loc[quedan, "edad"].mean(),
                   (p.loc[quedan, "contrato"] == "temporal").mean(), p.loc[quedan, "miembros_hogar"].mean(),
                   (p.loc[quedan, "cuotas_existentes"] / p.loc[quedan, "ingresos_declarados"]).median()]},
        index=["ingreso declarado mediano", "edad media", "temporales", "miembros del hogar",
               "DTI existente mediano"])
    for idx, r in perfil.iterrows():
        if idx in ("temporales",):
            print(f"    {idx:28} {pct(r['caen'])} frente a {pct(r['siguen'])}")
        elif idx == "DTI existente mediano":
            print(f"    {idx:28} {pct(r['caen'])} frente a {pct(r['siguen'])}")
        else:
            print(f"    {idx:28} {num(r['caen'], 1)} frente a {num(r['siguen'], 1)}")
    print("  Caída de aprobación por producto (estricta / proporcional):")
    for prod in PRODUCTOS:
        mk = (p["producto"] == prod).to_numpy()
        base_ap = ap_score[mk].mean()
        print(f"    {prod:10} {pct(base_ap)} -> {pct((ap_score & regla_decl)[mk].mean())} / "
              f"{pct((ap_score & regla_prop)[mk].mean())}")
    # Pasan con ingresos declarados y no con los verificados.
    solo_decl = ap_score & regla_decl & ~regla_ob
    print(f"  Aprobados por score que pasan con ingreso declarado y no con el verificado: "
          f"{pct(solo_decl.sum() / max((ap_score & regla_decl).sum(), 1))} de los que pasan; "
          f"su morosidad {pct(y[solo_decl].mean(), 1)}")

    # Integrada: DSTI de la nueva operación como variable del modelo.
    vars_int = VARS_LIMPIO + ["dsti_declarado"]
    m_int = entrenar(d, vars_int)
    pd_int = puntuar(m_int, p, vars_int)
    g_int = gini(y, pd_int)
    ap_int = aprobacion_a_igual_morosidad(y, pd_int, mora_obj)
    print(f"  Integrada (DSTI dentro del modelo): Gini {pct(g_int)} ({pp(g_int - g_lim)} "
          f"sobre el limpio), aprobación a igual morosidad {pct(ap_int)}")
    # Morosidad de la combinación secuencial al mismo volumen que la integrada a igual mora.
    ap_seq = ap_score & regla_decl
    print(f"  Secuencial: aprobación {pct(ap_seq.mean())} con morosidad {pct(y[ap_seq].mean(), 2)}; "
          f"la integrada, a esa misma aprobación, tiene morosidad "
          f"{pct(y[pd_int <= corte_por_aprobacion(pd_int, ap_seq.mean())].mean(), 2)}")
    # Integrada + regla como suelo (lo que se recomienda en el texto).
    ap_int_corte = pd_int <= corte_por_aprobacion(pd_int, APROBACION_REFERENCIA)
    ap_int_regla = ap_int_corte & regla_prop
    print(f"  Integrada al 70 % + regla proporcional como suelo: aprobación {pct(ap_int_regla.mean())}, "
          f"morosidad {pct(y[ap_int_regla].mean(), 2)}")

    # (c) Open banking ------------------------------------------------------------
    titulo("c) Variables de movimientos de cuenta (open banking)")
    vars_ob = VARS_OB + ["dsti_ob"]
    m_ob = entrenar(d, vars_ob)
    pd_ob = puntuar(m_ob, p, vars_ob)
    g_ob = gini(y, pd_ob)
    ap_ob = aprobacion_a_igual_morosidad(y, pd_ob, mora_obj)
    print(f"  Cobertura total (todos comparten): Gini {pct(g_ob)} ({pp(g_ob - g_int)} sobre la "
          f"integrada; {pp(g_ob - g_act)} sobre el actual), aprobación a igual morosidad {pct(ap_ob)}")
    cons = (p["consiente_ob"] == 1).to_numpy()
    pd_mix = np.where(cons, pd_ob, pd_int)
    g_mix = gini(y, pd_mix)
    ap_mix = aprobacion_a_igual_morosidad(y, pd_mix, mora_obj)
    print(f"  Cobertura parcial ({pct(cons.mean(), 0)} comparten; el resto con la integrada): Gini "
          f"{pct(g_mix)}, aprobación a igual morosidad {pct(ap_mix)}")
    print(f"  Dentro de quienes comparten: Gini integrada {pct(gini(y[cons], pd_int[cons]))} frente a "
          f"open banking {pct(gini(y[cons], pd_ob[cons]))}")

    # (d) Evaluar con datos generados por el modelo viejo ---------------------------
    titulo("d) Medir el modelo nuevo solo con los aprobados del modelo viejo")
    des = d[d["muestra"] == "desarrollo"]
    pd_des_act = puntuar(m_act, des, VARS_ACTUAL)
    aprob_hist = pd.Series(pd_des_act <= np.quantile(pd_des_act, APROBACION_REFERENCIA), index=des.index)
    filtro = pd.Series(False, index=d.index)
    filtro.loc[aprob_hist.index] = aprob_hist
    m_kgb = entrenar(d, vars_int, filtro=filtro)
    pd_kgb = puntuar(m_kgb, p, vars_int)
    ap_p_act = pd_act <= corte
    print(f"  Modelo integrado entrenado con toda la población: Gini en toda la población {pct(g_int)}, "
          f"medido solo en aprobados por el actual {pct(gini(y[ap_p_act], pd_int[ap_p_act]))}")
    print(f"  Mismo modelo entrenado solo con aprobados: Gini en toda la población {pct(gini(y, pd_kgb))}, "
          f"en aprobados {pct(gini(y[ap_p_act], pd_kgb[ap_p_act]))}")
    rech = ~ap_p_act
    print(f"  Morosidad real de los rechazados por el actual: {pct(y[rech].mean(), 1)}; PD media que les "
          f"asigna el modelo entrenado solo con aprobados: {pct(pd_kgb[rech].mean(), 1)}; el de toda la "
          f"población: {pct(pd_int[rech].mean(), 1)}")

    # (e) Motivos de denegación y contrafactual -----------------------------------
    titulo("e) Motivos de denegación de un solicitante (scorecard integrada, puntos PDO 20)")
    corte_int = corte_por_aprobacion(pd_int, APROBACION_REFERENCIA)
    x = matriz(p, vars_int)
    esc = m_int.named_steps["standardscaler"]
    lr = m_int.named_steps["logisticregression"]
    xs = (x - esc.mean_) / esc.scale_
    factor = 20 / np.log(2)
    puntos = -xs * lr.coef_[0] * factor        # puntos frente al solicitante medio (positivo = mejor)
    # Ejemplo elegido a propósito: el primer préstamo personal denegado cerca del corte, sin
    # incidencias, cuyo motivo principal es la carga de cuotas (el caso que ilustra el cap. 22).
    cand = p[(pd_int > corte_int) & (pd_int < corte_int * 1.35) & (p["producto"] == "prestamo")
             & (p["incidencias"] == 0)]
    i = next(j for j in cand.index if puntos.loc[j].idxmin() == "dsti_declarado")
    fila = p.loc[i]
    print(f"  Solicitante {i}: préstamo de {num(fila['importe'])} EUR, cuota {num(fila['cuota_nueva'])} EUR, "
          f"ingreso declarado {num(fila['ingresos_declarados'])} EUR, edad {int(fila['edad'])}, "
          f"contrato {fila['contrato']}, antigüedad {int(fila['antig_empleo_m'])} meses")
    pd_i = pd_int[p.index.get_loc(i)]
    print(f"  PD estimada {pct(pd_i, 2)} frente a un corte de {pct(corte_int, 2)}")
    pts = puntos.loc[i].sort_values()
    print("  Tres variables que más restan frente al solicitante medio:")
    for var, v in pts.head(3).items():
        print(f"    {var:22} {v:+.0f} puntos")
    print(f"  Regla de capacidad (proporcional) con el importe solicitado: "
          f"{'pasa' if regla_prop[p.index.get_loc(i)] else 'no pasa'}")
    # Contrafactual: mayor importe, en pasos del 5 %, con el que se aprobaría (mismo plazo):
    # tiene que quedar por debajo del corte de PD y pasar la regla de capacidad de pago.
    for factor_imp in np.arange(0.95, 0.20, -0.05):
        q = p.loc[[i]].copy()
        q["importe"] = fila["importe"] * factor_imp
        q["cuota_nueva"] = fila["cuota_nueva"] * factor_imp
        if (puntuar(m_int, q, vars_int)[0] <= corte_int
                and regla_capacidad(q, q["ingresos_declarados"], proporcional=True).iloc[0]):
            print(f"  Contrafactual: con un importe de {num(q['importe'].iloc[0], 0)} EUR "
                  f"({pct(factor_imp, 0)} del solicitado) la solicitud se aprobaría")
            break
    else:
        print("  Contrafactual: reducir el importe no basta para aprobar")

    # (f) Esfuerzo del programa ------------------------------------------------------
    titulo("f) Esfuerzo del programa de modelos (supuestos del autor, persona-mes)")
    print(f"  {'Frente de trabajo':56} {'grande':>7} {'pequeña':>8}")
    tot_g = tot_p = 0.0
    for frente, g_pm, p_pm in ESFUERZO:
        tot_g += g_pm
        tot_p += p_pm
        print(f"  {frente:56} {num(g_pm, 1):>7} {num(p_pm, 1):>8}")
    print(f"  {'Total persona-mes':56} {num(tot_g, 1):>7} {num(tot_p, 1):>8}")
    print(f"  Coste a {num(COSTE_PM['grande'])} / {num(COSTE_PM['pequena'])} EUR por persona-mes: "
          f"{num(tot_g * COSTE_PM['grande'] / 1e6, 2)} M EUR / {num(tot_p * COSTE_PM['pequena'] / 1e6, 2)} M EUR "
          f"(sin licencias ni motor de decisión)")

    titulo("Resumen")
    print(f"  Gini: actual {pct(g_act)} · limpio {pct(g_lim)} · integrado {pct(g_int)} · "
          f"open banking total {pct(g_ob)} · parcial {pct(g_mix)}")
    print(f"  Aprobación a la morosidad de referencia ({pct(mora_obj, 2)}): actual {pct(APROBACION_REFERENCIA, 0)} · "
          f"limpio {pct(ap_lim)} · integrado {pct(ap_int)} · open banking total {pct(ap_ob)} · parcial {pct(ap_mix)}")


if __name__ == "__main__":
    main()
