# -*- coding: utf-8 -*-
"""
Genera la portada del manual en escala de grises, a la resolucion de un Kindle Paperwhite
(758x1024). Pensada para tinta electronica: alto contraste, pocos tonos limpios, tipografia
grande.

El motivo grafico son las cuatro TAE de los productos del hilo conductor (anexo S1) frente al
TEDR de tarjetas: el mismo credito leido como un unico numero.

Uso (desde la raiz del proyecto):  .venv/bin/python -I manual/generar_portada.py
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 758, 1024
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "anexos"))
import s1_tae
FUENTES = [Path("/System/Library/Fonts/Supplemental"), Path("/Library/Fonts"), Path(r"C:\Windows\Fonts")]

img = Image.new("L", (W, H), color=18)
draw = ImageDraw.Draw(img)


def fuente(nombres, tam):
    for carpeta in FUENTES:
        for n in nombres:
            if (carpeta / n).exists():
                return ImageFont.truetype(str(carpeta / n), tam)
    return ImageFont.load_default()


SANS = ["Arial.ttf", "arial.ttf"]
SANS_B = ["Arial Bold.ttf", "arialbd.ttf"]
SERIF = ["Georgia.ttf", "georgia.ttf"]


def centrado(y, texto, font, gris, esp=0):
    if esp:
        ancho = sum(draw.textlength(c, font=font) + esp for c in texto) - esp
        x = (W - ancho) / 2
        for c in texto:
            draw.text((x, y), c, font=font, fill=gris)
            x += draw.textlength(c, font=font) + esp
    else:
        ancho = draw.textlength(texto, font=font)
        draw.text(((W - ancho) / 2, y), texto, font=font, fill=gris)
    caja = font.getbbox(texto)
    return y + (caja[3] - caja[1]) + 12


y = 90
y = centrado(y, "MANUAL DE ESTUDIO Y REFERENCIA", fuente(SANS, 15), 200, esp=4)
y += 34
for linea in ("Crédito al consumo", "la CCD2 en España"):
    y = centrado(y, linea, fuente(SERIF, 62), 245)
y += 14
for linea in ("Directiva (UE) 2023/2225 y su aplicación", "en una entidad española"):
    y = centrado(y, linea, fuente(SANS, 22), 185)

# ---------- Motivo: TAE de los cuatro productos del hilo conductor (anexo S1) ----------
casos = [("Tarjeta", s1_tae.tarjeta_revolving), ("Préstamo", s1_tae.prestamo_personal),
         ("BNPL largo", s1_tae.bnpl_largo), ("BNPL corto", s1_tae.bnpl_cero)]
valores = []
for nombre, f in casos:
    disp, pagos, _, _ = f()
    valores.append((nombre, s1_tae.tae(disp, pagos)))

x0, x1, ytop, ybot = 130, 628, 560, 800
tmax = 26.0
draw.line([(x0, ybot), (x1, ybot)], fill=90, width=2)
ancho_barra = 70
sep = ((x1 - x0) - ancho_barra * len(valores)) / (len(valores) - 1)
etq = fuente(SANS_B, 20)
peq = fuente(SANS, 16)
for i, (nombre, v) in enumerate(valores):
    bx = x0 + i * (ancho_barra + sep)
    altura = max(3, (v / tmax) * (ybot - ytop))
    draw.rectangle([bx, ybot - altura, bx + ancho_barra, ybot], fill=235 if i == 0 else 150)
    t = f"{v:.2f} %".replace(".", ",")
    ancho = draw.textlength(t, font=etq)
    draw.text((bx + (ancho_barra - ancho) / 2, ybot - altura - 30), t, font=etq, fill=235)
    ancho = draw.textlength(nombre, font=peq)
    draw.text((bx + (ancho_barra - ancho) / 2, ybot + 10), nombre, font=peq, fill=185)
# referencia: TEDR de tarjetas, agosto de 2026
yref = ybot - (s1_tae.TEDR_TARJETAS / tmax) * (ybot - ytop)
for xx in range(x0, x1, 14):
    draw.line([(xx, yref), (xx + 7, yref)], fill=200, width=2)
lbl = "TEDR de tarjetas, agosto de 2026: 18,26 %"
draw.text((x1 - draw.textlength(lbl, font=peq), yref - 26), lbl, font=peq, fill=200)
centrado(ybot + 50, "TAE de los cuatro productos del hilo conductor", fuente(SANS, 18), 160)

centrado(940, "RAFAEL VIGUERAS", fuente(SANS, 18), 200, esp=5)

img.convert("RGB").save(AQUI / "portada.jpg", quality=92)
print("portada.jpg generada")
