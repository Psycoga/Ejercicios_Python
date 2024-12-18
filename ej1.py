import sys

# Obtener la cadena de ARN desde los argumentos
arn_cadena = sys.argv[1].upper()

# Validar que la cadena solo contiene A, U, G y C
for caracter in arn_cadena:
    if caracter not in "AUGC":
        print("Error: La cadena solo puede contener A, U, G y C.")
        sys.exit()

# Convertir ARN a ADN reemplazando U por T
adn_cadena = arn_cadena.replace("U", "T")

# Mostrar la cadena de ADN resultante
print("Cadena de ADN:", adn_cadena)
