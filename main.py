'''
from Personas.empleado import Empleado

miEmpleado: Empleado = Empleado('Thais', 'Casares', 34,'QA',20.0,0,0.0)

miEmpleado.trabajar(10)
miEmpleado.cobrar()
'''
from Animales.Animal import Animal
from Animales.Carnivoro import Carnivoro
from Animales.Herbivoro import Herbivoro


Animal = Animal('Leon',4,'arr',5,0)
tigre = Carnivoro('Tigre', 4, 'grarrr', 6, 7, 80, 43,0,1)
vaca = Herbivoro('Vaca', 4, 'muuuu', 8, 50, 1, 6, 20, 0)

Animal.hacerRuido()
Animal.comer(10)

tigre.comer(4)

vaca.comer(4)
vaca.vecesProcesaComida()

