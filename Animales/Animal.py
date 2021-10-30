class Animal():
    nombre:str
    nroPatas:str
    ruido:str
    edad:int
    kgcomida:float
   
    def __init__(self, nombre, nroPatas, ruido, edad,kgcomida):
      self.nombre = nombre
      self.nroPatas = nroPatas
      self.ruido = ruido
      self.edad = edad
      self.kgcomida = kgcomida
      
    def hacerRuido(self):
      print(f'El animal hace {self.ruido}')
    
    def comer(self, cantcomida):
      self.kgcomida += cantcomida
      print(f'El animal ha comido {self.kgcomida} kg de comida esta semana')