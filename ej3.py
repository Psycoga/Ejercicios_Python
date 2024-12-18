import sys
import random

if len(sys.argv) != 4:
    print("Uso: python script.py <ancho> <alto> <tipo de línea>")
    sys.exit()

ancho = int(sys.argv[1])
alto = int(sys.argv[2])
tipo_linea = sys.argv[3]

if tipo_linea == "simple":
    esquina_izq_arriba = "┌"
    esquina_der_arriba = "┐"
    esquina_izq_abajo = "└"
    esquina_der_abajo = "┘"
    linea_horizontal = "─"
    linea_vertical = "│"
elif tipo_linea == "doble":
    esquina_izq_arriba = "╔"
    esquina_der_arriba = "╗"
    esquina_izq_abajo = "╚"
    esquina_der_abajo = "╝"
    linea_horizontal = "═"
    linea_vertical = "║"
else:
    esquina_izq_arriba = tipo_linea
    esquina_der_arriba = tipo_linea
    esquina_izq_abajo = tipo_linea
    esquina_der_abajo = tipo_linea
    linea_horizontal = tipo_linea
    linea_vertical = tipo_linea

print(esquina_izq_arriba + linea_horizontal * (ancho - 2) + esquina_der_arriba)

for _ in range(alto - 2):
    print(linea_vertical + ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for _ in range(ancho - 2)) + linea_vertical)

print(esquina_izq_abajo + linea_horizontal * (ancho - 2) + esquina_der_abajo)
