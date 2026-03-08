def pedir_datos():
    while True:
        nombre = input("Ingrese su nombre: ")
        if len(nombre) >= 3:
            break
        print("Error: el nombre debe tener minimo 3 caracteres.")

    while True:
        edad = int(input("Ingrese su edad: "))
        if 0 <= edad <= 120:
            break
        print("Error: la edad debe estar entre 0 y 120.")

    while True:
        correo = input("Ingrese su correo: ")
        if "@" in correo and (".com" in correo or ".edu.co" in correo):
            break
        print("Error: el correo debe contener @ y terminar en .com o .edu.co")

    return nombre, edad, correo

def main():
    lista = []

    nombre, edad, correo = pedir_datos()
    persona = {"nombre": nombre, "edad": edad, "correo": correo}
    lista.append(persona)

    print("DATOS ALMACENADOS")
    for p in lista:
        print(f"Nombre: {p['nombre']}, Edad: {p['edad']}, Correo: {p['correo']}")
if __name__ == "__main__":
    main()