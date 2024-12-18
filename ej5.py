import sys
import requests

# Verificar que se ha proporcionado un argumento (dominio o IP)
if len(sys.argv) != 2:
    print("Uso: python script.py <dominio o IP>")
    sys.exit()

# Obtener el dominio o IP del argumento
dominio = sys.argv[1]

# Realizar un número de peticiones
for _ in range(1000):  # Ajusta el número de peticiones según lo necesites
    try:
        response = requests.get(dominio)
        print(f"Petición realizada a {dominio}, código de estado: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la petición: {e}")
