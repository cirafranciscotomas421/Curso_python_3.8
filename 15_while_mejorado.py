while True:
    nombre_alumno=input("anota el nombre del alumno :")
    apellidos_alumno=input("anota el apllido paterno :")
    edad_alumno=input("anota la edad :")
    print(f"alumno : {nombre_alumno}, {apellidos_alumno}, {edad_alumno} registrado corectamente")
    condicion=input("¿desea hacer otro registro? (S=si N=no):")
    if condicion=="n" or condicion=="N":
        break

print("Alumnos registrados correctamente")