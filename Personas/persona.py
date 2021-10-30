	
class Persona():
    nombre:str
    apellido:str
    edad:int
   
    def __init__(self, nombre, apellido, edad):
      self.nombre = nombre
      self.apellido = apellido
      self.edad = edad
      
    def saludar(self):
      print(f'Hola me llamo {self.nombre} {self.apellido}, tengo {self.edad} años')
  