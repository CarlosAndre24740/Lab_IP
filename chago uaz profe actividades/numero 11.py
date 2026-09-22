print("Dame un número para verificar si es perfecto")

numero = int(input())

while numero != 0:

    if numero < 0:
        print("El", numero, "no es positivo")

    else:
        suma = 0
        i = 1

        while i < numero:
            if numero % i == 0:
                suma = suma + i
            i = i + 1

        if suma == numero:
            print("El", numero, "es perfecto")
        else:
            print("El", numero, "no es perfecto")

    numero = int(input())

print("Fin del algoritmo")