"""S3 · Pruebas de sesgo y disparidad sobre la scorecard de S2.

Anexo de código del Manual de crédito al consumo (caps. 24 y 32). Usa la misma cartera
sintética y los mismos modelos de `s2_scorecard.py` y mide, para un atributo protegido
sintético (nacionalidad extranjera, que el art. 6 CCD2 nombra expresamente):

  1. cuánto del atributo se puede reconstruir desde las variables del modelo (prueba de proxy);
  2. disparidad de resultados con el corte al 70 % de aprobación: tasa de aprobación por grupo
     y su cociente, igualdad de oportunidades (aprobación entre quienes no impagan) y
     morosidad de los aprobados por grupo;
  3. calibración por grupo: PD media estimada frente a impago observado, global y por tramo;
  4. qué cuesta en Gini y qué gana en disparidad retirar la variable proxy (zona postal).

Todo es sintético. La nacionalidad no tiene efecto causal directo en el impago en el modelo
generador: su relación con el impago pasa por la situación laboral, el historial y la renta.

Uso:  .venv/bin/python -I anexos/s3_sesgo.py      (desde la raíz del proyecto)
"""
import sys
from pathlib import Path

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# Con -I Python no añade la carpeta del script a la ruta: se añade a mano para importar S2.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import s2_scorecard as s2  # noqa: E402

APROBACION = s2.APROBACION_REFERENCIA


def auc_atributo(d, variables):
    """AUC de predecir la nacionalidad con las variables dadas (0,5 = no la revelan)."""
    des = d[d["muestra"] == "desarrollo"]
    pru = d[d["muestra"] == "prueba"]
    m = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))
    m.fit(s2.matriz(des, variables), des["extranjero"])
    return roc_auc_score(pru["extranjero"], m.predict_proba(s2.matriz(pru, variables))[:, 1])


def metricas_grupo(p, pd_, corte):
    y = p["impago"].to_numpy()
    g = p["extranjero"].to_numpy()
    ap = pd_ <= corte
    r = {}
    for k, nombre in [(0, "nacionales"), (1, "extranjeros")]:
        m = g == k
        buenos = m & (y == 0)
        r[nombre] = {
            "aprobacion": ap[m].mean(),
            "aprob_buenos": ap[buenos].mean(),
            "mora_aprobados": y[m & ap].mean(),
            "pd_media": pd_[m].mean(),
            "impago_obs": y[m].mean(),
        }
    return r


def calibracion_por_tramo(p, pd_, n_tramos=10):
    """Diferencia máxima entre impago observado y PD media por grupo dentro de cada tramo."""
    y = p["impago"].to_numpy()
    g = p["extranjero"].to_numpy()
    tramos = np.quantile(pd_, np.linspace(0, 1, n_tramos + 1))
    idx = np.clip(np.searchsorted(tramos, pd_, side="right") - 1, 0, n_tramos - 1)
    filas = []
    for t in range(n_tramos):
        fila = [t + 1]
        for k in (0, 1):
            m = (idx == t) & (g == k)
            fila += [pd_[m].mean(), y[m].mean(), m.sum()]
        filas.append(fila)
    return filas


def main():
    d = s2.generar_cartera()
    p = d[d["muestra"] == "prueba"].copy()
    y = p["impago"].to_numpy()

    s2.titulo("0. El atributo protegido en la cartera sintética")
    for k, nombre in [(0, "nacionales"), (1, "extranjeros")]:
        m = p["extranjero"] == k
        print(f"  {nombre:12} {s2.pct(m.mean())} de las solicitudes · impago observado "
              f"{s2.pct(p.loc[m, 'impago'].mean())} · temporales {s2.pct((p.loc[m, 'contrato'] == 'temporal').mean())} "
              f"· historial mediano {int(p.loc[m, 'meses_historial'].median())} meses · zona media "
              f"{s2.num(p.loc[m, 'zona'].mean(), 1)}")

    s2.titulo("1. Prueba de proxy: ¿cuánto revelan las variables la nacionalidad? (AUC)")
    vars_int = s2.VARS_LIMPIO + ["dsti_declarado"]
    vars_sin_zona = [v for v in vars_int if v != "zona"]
    for nombre, vars_ in [("solo zona postal", ["zona"]),
                          ("solo meses de historial", ["meses_historial"]),
                          ("solo tipo de contrato", ["contrato"]),
                          ("todas las del modelo integrado", vars_int),
                          ("todas menos la zona", vars_sin_zona)]:
        print(f"  {nombre:34} AUC {s2.num(auc_atributo(d, vars_), 3)}")

    s2.titulo("2. Disparidad de resultados con el corte al 70 % de aprobación")
    modelos = [("Actual (con nacionalidad)", s2.VARS_ACTUAL),
               ("Integrado (sin nacionalidad)", vars_int),
               ("Integrado sin zona postal", vars_sin_zona)]
    resumen = []
    for nombre, vars_ in modelos:
        m = s2.entrenar(d, vars_)
        pd_ = s2.puntuar(m, p, vars_)
        corte = s2.corte_por_aprobacion(pd_, APROBACION)
        r = metricas_grupo(p, pd_, corte)
        nac, ext = r["nacionales"], r["extranjeros"]
        air = ext["aprobacion"] / nac["aprobacion"]
        eo = ext["aprob_buenos"] - nac["aprob_buenos"]
        g = s2.gini(y, pd_)
        resumen.append((nombre, g, air, eo, pd_, vars_))
        print(f"\n  {nombre}  (Gini {s2.pct(g)})")
        print(f"    aprobación          nacionales {s2.pct(nac['aprobacion'])} · extranjeros "
              f"{s2.pct(ext['aprobacion'])} · cociente {s2.num(air, 2)}")
        print(f"    aprobación de quienes no impagan (igualdad de oportunidades): "
              f"{s2.pct(nac['aprob_buenos'])} frente a {s2.pct(ext['aprob_buenos'])} ({s2.pp(eo)})")
        print(f"    morosidad de los aprobados: {s2.pct(nac['mora_aprobados'], 2)} frente a "
              f"{s2.pct(ext['mora_aprobados'], 2)}")
        print(f"    calibración global: PD media {s2.pct(nac['pd_media'], 2)} / impago {s2.pct(nac['impago_obs'], 2)} "
              f"(nacionales); {s2.pct(ext['pd_media'], 2)} / {s2.pct(ext['impago_obs'], 2)} (extranjeros)")

    s2.titulo("3. Calibración por tramo de PD (modelo integrado): PD media / impago observado")
    pd_int = resumen[1][4]
    print("  tramo   nacionales (n)              extranjeros (n)")
    peor = 0.0
    for t, pd0, y0, n0, pd1, y1, n1 in calibracion_por_tramo(p, pd_int):
        print(f"  {t:>5}   {s2.pct(pd0, 1):>7} / {s2.pct(y0, 1):>7} ({n0:>5})   "
              f"{s2.pct(pd1, 1):>7} / {s2.pct(y1, 1):>7} ({n1:>4})")
        if n1 >= 200:
            peor = max(peor, abs((y1 - pd1) - (y0 - pd0)))
    print(f"  Mayor diferencia entre grupos del error de calibración (tramos con 200 o más "
          f"extranjeros): {s2.num(100 * peor, 1)} p.")

    s2.titulo("4. Qué cuesta retirar la zona postal")
    _, g_int, air_int, eo_int, pd_i, _ = resumen[1]
    _, g_sz, air_sz, eo_sz, pd_sz, _ = resumen[2]
    mora_obj = y[pd_i <= s2.corte_por_aprobacion(pd_i, APROBACION)].mean()
    ap_sz = s2.aprobacion_a_igual_morosidad(y, pd_sz, mora_obj)
    print(f"  Gini {s2.pct(g_int)} -> {s2.pct(g_sz)} ({s2.pp(g_sz - g_int)}); cociente de aprobación "
          f"{s2.num(air_int, 2)} -> {s2.num(air_sz, 2)}; brecha de igualdad de oportunidades "
          f"{s2.pp(eo_int)} -> {s2.pp(eo_sz)}")
    print(f"  Aprobación a la morosidad del integrado ({s2.pct(mora_obj, 2)}): "
          f"{s2.pct(APROBACION, 0)} -> {s2.pct(ap_sz)}")

    s2.titulo("5. Cuánta disparidad explica el riesgo")
    ext = p["extranjero"].to_numpy() == 1
    print(f"  Impago observado: nacionales {s2.pct(y[~ext].mean())}, extranjeros {s2.pct(y[ext].mean())} "
          f"(cociente {s2.num(y[ext].mean() / y[~ext].mean(), 2)})")
    # Disparidad con un modelo "oráculo" que conociera la probabilidad real de impago.
    # Referencia: un modelo que añade a las variables legítimas el rasgo latente y la carga real,
    # que ninguna entidad observa. La disparidad que deja es la que explica el riesgo.
    vars_or = vars_sin_zona + ["_z", "dsti_real"]
    m_or = s2.entrenar(d, vars_or)
    pd_or = s2.puntuar(m_or, p, vars_or)
    r_or = metricas_grupo(p, pd_or, s2.corte_por_aprobacion(pd_or, APROBACION))
    nac, ext_ = r_or["nacionales"], r_or["extranjeros"]
    print(f"  Con un modelo que viera también el rasgo latente y la carga real (no observable): "
          f"Gini {s2.pct(s2.gini(y, pd_or))}, cociente de aprobación "
          f"{s2.num(ext_['aprobacion'] / nac['aprobacion'], 2)}, brecha de igualdad de oportunidades "
          f"{s2.pp(ext_['aprob_buenos'] - nac['aprob_buenos'])}")


if __name__ == "__main__":
    main()
