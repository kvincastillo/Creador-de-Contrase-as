#importamos la libreria
import requests

#VAMOS HACER UN PETICION GET
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

#para ver el estado de la petición0
print("Codigo del estado: ", response.status_code)

#para imprimirlo en formatp texto
print("Contenido: ", response.text)

#Si es JSON 
print("JSON: ", response.json)