
import funcion_practica

funcion_practica.menu()
funcion_practica.validando_opciones()

while True:
    condicion= input("¿desea hacer otro registro? (S=si N=no):")
    funcion_practica.menu()
    funcion_practica.validando_opciones()
    if condicion == "n" or condicion == "N":
        break
print("fin de la calculadora")
