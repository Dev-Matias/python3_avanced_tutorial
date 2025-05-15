import requests

url_api = "http://127.0.0.1:5000/libro"

try:
    respuesta = requests.get(url_api)
    respuesta.raise_for_status()  # Lanza una excepción para códigos de estado HTTP malos (4xx o 5xx)
    datos_libro = respuesta.json()
    print("Información del libro obtenida de la API:")
    print(f"Título: {datos_libro['titulo']}")
    print(f"Autor: {datos_libro['autor']}")
    print(f"Año: {datos_libro['año']}")
    print(f"Género: {datos_libro['genero']}")

except requests.exceptions.RequestException as e:
    print(f"Error al conectar con la API: {e}")
except ValueError:
    print("Error al decodificar la respuesta JSON.")