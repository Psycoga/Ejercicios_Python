import sys
import subprocess

# Verificar que se han proporcionado los tres argumentos
if len(sys.argv) != 3:
    print("Uso: python script.py <IP del servidor> <número de pings>")
    sys.exit()

# Obtener los argumentos
ip = sys.argv[1]
num_pings = int(sys.argv[2])

# Lanzar el comando ping utilizando subprocess
subprocess.run(["ping", "-i", "0.1", "-c", str(num_pings), ip])
