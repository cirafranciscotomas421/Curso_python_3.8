nombre = input("ingrese su nombre: ")
calificacion = int(input("ingrese su calificacion: "))
cali= None

if 0 <= calificacion <= 69:
    cali="insuficiente (N/A)"

elif 70 <= calificacion <= 74:
    cali="suficiente"
elif 75 <= calificacion <= 84:
    cali="bueno"
elif 85 <= calificacion <= 94:
    cali="notable" 
elif 95 <= calificacion <= 100:
    cali="excelente"
else:
    print("tu calificacion no exciste")

print(f"tu calificacion es:{calificacion} ", cali)
