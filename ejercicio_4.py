def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def factorial(num):
    resultado = 1
    for i in range(1, num + 1):
        resultado = resultado * i
    return resultado

def contar_vocales(texto):
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letra in texto.lower():
        if letra in vocales:
            vocales[letra] += 1
    return vocales

def main():
    print("Seleccione una opcion:")
    print("1. Determinar si un numero es primo")
    print("2. Calcular factorial")
    print("3. Contar vocales en un texto")

    opcion = input("\nOpcion: ")

    if opcion == "1":
        num = int(input("Ingrese un numero: "))
        if es_primo(num):
            print(f"{num} es primo")
        else:
            print(f"{num} no es primo")

    elif opcion == "2":
        num = int(input("Ingrese un numero: "))
        resultado = factorial(num)
        print(f"El factorial de {num} es: {resultado}")

    elif opcion == "3":
        texto = input("Ingrese un texto: ")
        resultado = contar_vocales(texto)
        for vocal, cantidad in resultado.items():
            print(f"  {vocal}: {cantidad}")

    else:
        print("Opcion no valida")

if __name__ == "__main__":
    main()