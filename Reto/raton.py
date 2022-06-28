
from monitor import *
class raton(monitor):
    def __init__(self,Tipo_entrada,conexion):
        self.Tipo_entrada=Tipo_entrada
        self.conexion=conexion

    def conectar(self):
        print(self.Tipo_entrada,"Esta conectado")
    def desconectar(self):
        print(self.Tipo_entrada,"Esta desconectado")


