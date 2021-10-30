	
import requests
 
def randomUser():
 
  # URL -> api-endpoint
  URL = 'https://randomuser.me/api/'
 
  respuesta = requests.get(url = URL)
  	
# Extraemos los datos en formato JSON
  datos = respuesta.json()
 
# Obtenemos valor en la clave 'value' del JSON que nos interesa
  nombre: str = datos['results']['name']['first']
  apellido: str = datos['results']['name']['last']
  email: str = datos['results'] ['email']
  print(nombre + apellido)
  print (email)
