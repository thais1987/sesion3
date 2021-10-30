	
from Animales.Animal import Animal
 
class Carnivoro(Animal):
        nroDientes: int
        nroGarras: int
        animalGranja: bool
        cantestomagos: int
 
        def __init__(self,nombre, nroPatas, ruido, edad, kgcomida, nroDientes, nroGarras, animalGranja, cantestomagos):
              super(Carnivoro, self).__init__(nombre, nroPatas, ruido, edad, kgcomida)
              self.nroDientes = nroDientes
              self.nroGarras = nroGarras
              self.animalGranja = animalGranja
              self.cantestomagos = cantestomagos


        def cuantosDientes(self,dientes):
          self.nroDientes += dientes
          print(f'El Carnivoro tiene: {self.nroDientes} dientes')

        def cuantasGarras(self,garras):
          self.nroGarras += garras
          print(f'El Carnivoro tiene: {self.nroGarras} garras')
        
        def comer(self, cantcomida):
          self.kgcomida += cantcomida
          print(f'El carnivoro ha comido {self.kgcomida} kg de carne esta semana')