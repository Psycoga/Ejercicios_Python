import sys

# Verificar que se ha proporcionado un argumento
if len(sys.argv) < 2:
    print("Error: Debes proporcionar una cadena de texto como argumento.")
    print("Ejemplo: python ej2.py Hola Mundo")
    sys.exit()

# Obtener la cadena de texto desde los argumentos
texto = sys.argv[1]

# Diccionario de sustituciones
sustituciones = {
    'O': '0', 'I': '1', 'E': '3', 'A': '4', 'S': '5',
    'G': '6', 'T': '7', 'B': '8', 'g': '9', 'o': '0',
    'i': '1', 'e': '3', 's': '5', 't': '7', 'b': '8'
}

# Convertir el texto a 13375P34K usando el diccionario de sustituciones
texto_convertido = ''.join(sustituciones.get(caracter, caracter) for caracter in texto)

# Mostrar el resultado
print("Texto convertido a 13375P34K:", texto_convertido)
