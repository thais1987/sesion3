from Animales.Animal import Animal
 
class Herbivoro(Animal):
        animalGranja: bool
        cantestomagos: int
        nroDientes: int
        nroGarras: int
      
 
        def __init__(self,nombre, nroPatas, ruido, edad,kgcomida, animalGranja, cantestomagos, nroDientes, nroGarras):
                super(Herbivoro, self).__init__(nombre, nroPatas, ruido, edad,kgcomida)
                self.animalGranja = animalGranja
                self.cantestomagos = cantestomagos
                self.nroDientes = nroDientes
                self.nroGarras = nroGarras

        def vecesProcesaComida(self):
          print(f'El Herbivoro procesa la comida {self.cantestomagos} veces')

        
        def comer(self, cantcomida):
          self.kgcomida += cantcomida
          print(f'El Herbivoro ha comido {self.kgcomida} kg de hierba esta semana')