
#instanciando el codigo se usa from
from persona import *#se importa la clase persona en otro script
class Alumno(persona):
    def __init__(self,nombre,matricula):


        self.nombre=nombre
        self.matricula=matricula
    def comer(self):
        super().comer()
    def caminando(self):
        super().caminando()
    def promedio(self):
        return f"soy {self.nombre} y no. Tengo promedio aun"
