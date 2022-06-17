

lista_alumnos_isic=[
        ["Miguel Ángel","Olivera Ortega","Miguel@gmail.com"],#lista0
        ["Marina","Toribio Salgado","Marina@gmail.com"],#lista1
        ["Victor","Mateos Francisco","Victor@gmail.com"],#lista2
        ["Gabriel","Garcia Dolores","Gabriel@gmail.com"],#lista3
]
"""print(lista_alumnos_isic)#imprime toda la lista

#mostrar una lista determinada
print(lista_alumnos_isic[1])

#mostrar un registro
print(lista_alumnos_isic[3][2])

#mostrar nombres ordenados
for nombres in lista_alumnos_isic:
    print(nombres)
#solo nombres
for nombres in lista_alumnos_isic:
    print(nombres[0])
#solo nombre y un apellido
for nombres in lista_alumnos_isic:
    print(nombres[0])
    print(nombres[1])"""

for alumnos in lista_alumnos_isic:
    for elemento in alumnos:
        if alumnos.index(elemento)==0:
            print(f"Nombre:{elemento}")
        elif alumnos.index(elemento)==1:
            print(f"apellidos{elemento}")
        elif alumnos.index(elemento)==2:
            print(f"correo{elemento}")
