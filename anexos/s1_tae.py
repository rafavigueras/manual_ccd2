"""S1. TAE de los tres productos de la entidad de referencia.

La TAE es el tipo anual X que iguala el valor actual de las disposiciones con el de los
pagos del consumidor (ecuacion del anexo III de la Directiva (UE) 2023/2225):
    sum_k A_k / (1+X)^t_k  =  sum_l D_l / (1+X)^s_l
con t en anos y meses de igual duracion (1/12 de ano).

Los tres productos son sinteticos. Los supuestos de cada uno (importe, plazo, cuotas) son
de este script y sirven para ilustrar el calculo; no son los supuestos obligatorios del
anexo III para cada tipo de credito.

Referencias de comparacion (ilustrativas, ver cap. 18 del manual):
  - TEDR de tarjetas de credito y revolving, ago-2026 (provisional): 18,26 % (Banco de Espana).
  - Margen de 6 puntos sobre el tipo medio de la categoria que usa el Supremo
    (STS 258/2023, segun nota del CGPJ).
  - Tope transitorio del anteproyecto, texto de enero de 2026: 22 (DT 2.a); aun no es derecho.

Uso:  .venv/bin/python -I anexos/s1_tae.py
"""
from scipy.optimize import brentq

TEDR_TARJETAS = 18.26
MARGEN_SUPREMO = 6.0
TOPE_ANTEPROYECTO_ENERO = 22.0


def tae(disposiciones, pagos):
    """disposiciones y pagos: listas de (mes, importe). Devuelve la TAE en %."""
    def f(x):
        va_a = sum(a / (1 + x) ** (m / 12) for m, a in disposiciones)
        va_d = sum(d / (1 + x) ** (m / 12) for m, d in pagos)
        return va_a - va_d
    return brentq(f, -0.5, 10.0, xtol=1e-12) * 100


def cuota_francesa(capital, tin_anual, n):
    i = tin_anual / 12
    return capital * i / (1 - (1 + i) ** -n) if i else capital / n


def tarjeta_revolving():
    """Limite 3.000 EUR dispuesto el primer dia; TIN 21,5 %; sin cuota anual.
    Reembolso con el criterio de la Orden EHA/2899/2011 art. 18.2.e: 25 % del limite al ano
    en doce cuotas mensuales iguales de principal, mas intereses sobre el saldo."""
    limite, tin = 3000.0, 0.215
    amort = limite * 0.25 / 12
    saldo, pagos = limite, []
    for m in range(1, 49):
        interes = saldo * tin / 12
        pagos.append((m, amort + interes))
        saldo -= amort
    return [(0, limite)], pagos, limite, tin


def prestamo_personal():
    """Prestamo digital de 6.000 EUR a 36 meses, TIN 9,9 %, comision de apertura 1,5 %
    cobrada al desembolsar (el consumidor recibe 5.910 y devuelve las cuotas del principal)."""
    capital, tin, n, com = 6000.0, 0.099, 36, 0.015
    cuota = cuota_francesa(capital, tin, n)
    pagos = [(m, cuota) for m in range(1, n + 1)]
    return [(0, capital * (1 - com))], pagos, capital, tin


def bnpl_cero():
    """BNPL de 120 EUR en 3 pagos de 40 EUR (en el acto, a 1 y a 2 meses), sin coste para el
    consumidor: lo paga el comercio."""
    return [(0, 120.0)], [(0, 40.0), (1, 40.0), (2, 40.0)], 120.0, 0.0


def bnpl_largo():
    """BNPL de 600 EUR a 12 meses con comision del 3 % para el consumidor, sin TIN."""
    capital, n, com = 600.0, 12, 0.03
    cuota = capital * (1 + com) / n
    return [(0, capital)], [(m, cuota) for m in range(1, n + 1)], capital, 0.0


def main():
    casos = [
        ("Tarjeta revolving (3.000 EUR, TIN 21,5 %)", tarjeta_revolving()),
        ("Préstamo personal digital (6.000 EUR, 36 m, TIN 9,9 %, apertura 1,5 %)", prestamo_personal()),
        ("BNPL corto (120 EUR en 3 pagos, sin coste)", bnpl_cero()),
        ("BNPL largo (600 EUR a 12 m, comisión 3 %)", bnpl_largo()),
    ]
    ref_sup = TEDR_TARJETAS + MARGEN_SUPREMO
    print(f"Referencias: TEDR tarjetas {TEDR_TARJETAS:.2f} %; "
          f"TEDR + {MARGEN_SUPREMO:.0f} puntos = {ref_sup:.2f} %; "
          f"tope transitorio anteproyecto (enero) {TOPE_ANTEPROYECTO_ENERO:.0f}\n")
    for nombre, (disp, pagos, capital, tin) in casos:
        x = tae(disp, pagos)
        total = sum(p for _, p in pagos)
        tin_equiv = ((1 + tin / 12) ** 12 - 1) * 100 if tin else 0.0
        print(f"{nombre}")
        print(f"  Importe recibido {sum(a for _, a in disp):10.2f} | pagos totales {total:10.2f} | "
              f"coste total {total - sum(a for _, a in disp):9.2f}")
        print(f"  TIN {tin*100:5.2f} % (equivalente anual {tin_equiv:5.2f} %) | TAE {x:6.2f} %")
        if x > 0:
            print(f"  frente a TEDR + 6: {x - ref_sup:+6.2f} puntos | frente a 22: {x - TOPE_ANTEPROYECTO_ENERO:+6.2f} puntos")
        print()


if __name__ == "__main__":
    main()
