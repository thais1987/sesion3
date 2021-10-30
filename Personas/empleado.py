from Personas.persona import Persona
class Empleado(Persona):
    puesto: str
    preciohora: float
    horasTrabajadas: int
    sueldo: float
    
    def __init__(self, nombre, apellido, edad,puesto, precioHora,horasTrabajadas, sueldo):
      super(Empleado, self).__init__(nombre, apellido, edad)
      self.puesto = puesto
      self.precioHora = precioHora
      self.horasTrabajadas = horasTrabajadas
      self.sueldo = sueldo

    def trabajar (self,horas):
      self.horasTrabajadas += horas
      print(self.horasTrabajadas)
    
    def cobrar (self):
      self.sueldo = self.precioHora * self.horasTrabajadas
      print(f'Ha cobrado: {self.sueldo}')

      
        


    