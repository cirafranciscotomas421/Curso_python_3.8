def menu():
    print("para calcular eliga opciones")
    print("1.suma")
    print("2.resta")
    print("3.mult")
    print("4.division")
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def mult(a,b):
    return a*b
def division(a,b):
    return a/b


def validando_opciones():
    opcion=int(input("anota una opcion (1.suma,2.resta,3.mult,4=division"))
    numero1=int(input("anota un numero: "))
    numero2=int(input("anota otro numero: "))

    if opcion==1:
        print(suma(numero1,numero2))
    elif opcion==2:
        print(resta(numero1,numero2))
    elif opcion==3:
        print(mult(numero1,numero2))
    elif opcion==4:
        print(division(numero1,numero2))

        



