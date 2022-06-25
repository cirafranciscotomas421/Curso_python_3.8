class persona:

        def __init__(self,nombre, apellido,edad):#__init__().es el método constructor que se usa cada vez que inicia un objeto
            self.nombre=nombre#se usa self para la instancia de la clase
            self.apellido=apellido
            self.edad=edad
        def comer(self):
            print(self.nombre, "esta comiendo")#se usa self que sirve para la instancia de la clase
        def caminando(self):
            print(self.nombre, "esta caminando")

