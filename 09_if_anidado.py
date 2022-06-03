nombre_alumno = input("Anota un nombre de alumno: ")
#matricula_alumno = input("Anota la matricula: ")

alumno1 = "victor"
alumno2 = "bruno"
alumno3 = "diana"
alumno4 = "cira"
matricula_alumno1 = "s2112201"
matricula_alumno2 = "s2112202"
matricula_alumno3 = "s2112203"
matricula_alumno4 = "s2112204"

if nombre_alumno == alumno1 or nombre_alumno == alumno2 or nombre_alumno == alumno3 or nombre_alumno == alumno4:
    print("Bienvenido al curso de Python")
    matricula_alumno = input("Anota la matricula: ")
    if matricula_alumno == matricula_alumno1 or matricula_alumno == matricula_alumno2 or matricula_alumno == matricula_alumno3 or matricula_alumno == matricula_alumno4:
        print(f"Matricula asignada a {nombre_alumno}")
    else:
        print("Matricula no asignada")
else:
    print("alumno no registrado")

"""nombre_alumno = input("Anota un nombre de alumno: ")

alumno1 = "victor"
alumno2 = "bruno"
alumno3 = "diana"
alumno4 = "cira"
matricula_alumno1 = "s2112201"
matricula_alumno2 = "s2112202"
matricula_alumno3 = "s2112203"
matricula_alumno4 = "s2112204"
if nombre_alumno == alumno1 or nombre_alumno == alumno2 or nombre_alumno == alumno3 or nombre_alumno == alumno4:
    matricula_alumno = input("Anota la matricula: ")
    print("Bienvenido al curso de Python")

    if matricula_alumno == matricula_alumno1 or matricula_alumno == matricula_alumno2 or matricula_alumno == matricula_alumno3 or matricula_alumno == matricula_alumno4:
        print(f"Matricula asignada a {nombre_alumno}")
    else:
        print("Matricula no asignada")
else:
    print("alumno no registrado")"""

