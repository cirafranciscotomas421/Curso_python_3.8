class computadora:
    def __init__(self,DNI,Nombre,Marca,Color):
        self.DNI=DNI
        self.Nombre=Nombre
        self.Marca=Marca
        self.Color=Color

    def encender(self):
       print("Tu computadora",self.Nombre,"Esta encendido")
    def apagar(self):
        print("Tu computadora",self.Nombre,"Esta apagada")


