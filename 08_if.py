edad = int(input("Anota tu edad:"))
mensaje = None

if 0 <= edad <= 10:
    mensaje = "La infancia es increible..."

elif 10 <= edad <= 20:
    mensaje = "Muchos cambios, mucho estudio..."

elif 20 <= edad <= 30:
    mensaje = "Amor y mucho trabajo..."
else:
    mensaje = "Edad no encontrada, estas cañon"
print(f"tienes {edad} años de edad y ", mensaje)


