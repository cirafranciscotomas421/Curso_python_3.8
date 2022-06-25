from Alumno import*

#creando objetos
persona1=persona("Nicolaz", "Guzman", 30)
print("Me llamo", persona1.nombre)
print("Mis apellidos", persona1.apellido)
print("y tengo", persona1.edad ,"años")
persona1.comer()
persona1.caminando()

persona2=persona("Bruno","DFGH",20)#objecto
print(persona2.nombre)
#llamando alumno
alumno1=Alumno("Miguel","s2112201")
print(alumno1.promedio())
print(alumno1.comer())

mi_blog=open("archivo.txt","w")#txt=texto w=escribir r=leer
try:
    mi_blog.write(f"esta es una persona {alumno1.nombre}\n")
    mi_blog.write(f"Otra persona {persona2.nombre}")
finally:
    mi_blog.close()

