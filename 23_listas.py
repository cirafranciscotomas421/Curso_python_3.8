lista_nombre=["Diana","Bruno","Victor","gabriel"]#solo cadenas
lista_numeros=[2,8,1,90]#solo numeros

lista1=list["hola",23,2.9]#en python se puede mezclar tipos de datos
print(lista_nombre)#imprimir lista
print(lista_numeros)#imprimir lista

#tamaño lista
print(len(lista_nombre))


#acceder a una pocision
print(lista_nombre[0])#indice
print(lista_nombre[1])
print(lista_nombre[2])

#imprimir rango determinado
print(lista_nombre[2][3])

#agregar un elemento
lista_nombre.insert(3,"cira")
print(lista_nombre)
#modificar un valor

#iterar
for elementos in lista_nombre:
    print(elementos)


#agregar
lista_nombre.append("miguel")
print(lista_nombre)

#quitar un elemnto se usa remove
lista_nombre.remove("bruno")
print(lista_nombre)

#eluminar el ultimo elemento
lista_nombre.pop()
print(lista_nombre)

#limpiar lista
#lista_nombre.clear()#limpialos los elementos de nuestra lista
#print(lista_nombre)

#eluminar lista
#del lista_nombre
#print(lista_nombre)

#ordenar
lista_numeros.sort()
print(lista_numeros)
