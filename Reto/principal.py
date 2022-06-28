
from raton import *
computadora1=computadora("Electrónico","DESKTOP-PC1","Lenovo","Blanco")
print("Tipo de DNI",computadora1.DNI)
print("Nombre de la computadora:",computadora1.Nombre)
print("Marca de la computadora:",computadora1.Marca)
print("Color de la computadora:",computadora1.Color)
computadora1.encender()
computadora1.apagar()

monitor1=monitor("LED","SF350")
print("El tipo del monitor es:",monitor1.Tipo)
print("El modelo del monitor es:",monitor1.Modelo)


raton1=raton("USB","inalambrico",)
print("El tipo de entrada del raton es:",raton1.Tipo_entrada)
print("La conexion del raton es:",raton1.conexion)
raton1.conectar()
raton1.desconectar()

mi_blog=open("Archivo.txt","w")
try:
    mi_blog.write(f"Esta es a una computadora {computadora1.Nombre}\n")
    mi_blog.write(f"Esto es un monitor tipo {monitor1.Tipo}\n")
    mi_blog.write(f"Esto es un raton con tipo de conexion{raton1.conexion}")
finally:
    mi_blog.close()



