import requests

# Hacer la petición GET al endpoint
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

# Comprobar si la respuesta fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener la lista de usuarios en formato JSON
    users = response.json()

    # Mostrar los nombres de los usuarios en pantalla
    for user in users:
        print(user["name"])

    # Guardar los nombres en un archivo
    with open("nombres_usuarios.txt", "w") as file:
        for user in users:
            file.write(user["name"] + "\n")
else:
    print(f"Error al realizar la petición: {response.status_code}")
