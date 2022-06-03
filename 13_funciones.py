"""def mi_funcion(numero1, numero2):
    resultado = numero1 + numero2
    print(resultado)
mi_funcion(3, 5)
mi_funcion(30, 40)
print(30 * mi_funcion(10, 10))"""


def mi_funcion(numero1, numero2):
    resultado=numero1+numero2
    return resultado
numero1 =int(input("introduce un numero (1):"))
numero2 =int(input("introduce un numero (2):"))
resultado =mi_funcion(numero1, numero2)
print(resultado)



