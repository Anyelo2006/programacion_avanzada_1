nombre = input("Nombre del estudiante: ")
edad = int(input("Edad: "))
estado = input("Estado (activo/inactivo): ")

materias = {}
n = int(input("Cuantas materias tiene? "))

if n < 3:
    print("Error: debe tener al menos 3 materias.")
else:
    for i in range(n):
        materia = input(f"Nombre de la materia {i+1}: ")
        nota = float(input(f"Nota de {materia}: "))
        while nota < 0.0 or nota > 5.0:
            print("Error: la nota debe estar entre 0.0 y 5.0")
            nota = float(input(f"Nota de {materia}: "))
        materias[materia] = nota

    suma = 0
    for nota in materias.values():
        suma += nota
    promedio = suma / len(materias)

    mejor = ""
    peor = ""
    nota_max = -1
    nota_min = 6

    for materia, nota in materias.items():
        if nota > nota_max:
            nota_max = nota
            mejor = materia
        if nota < nota_min:
            nota_min = nota
            peor = materia

    print("\n--- RESULTADOS ---")
    print(f"Estudiante: {nombre}")
    print(f"Edad: {edad}")
    print(f"Estado: {estado}")
    print(f"Promedio general: {promedio:.2f}")
    print(f"Mejor nota: {mejor} ({nota_max})")
    print(f"Peor nota: {peor} ({nota_min})")

    if promedio >= 3.0:
        print("El estudiante APRUEBA")
    else:
        print("El estudiante NO APRUEBA")