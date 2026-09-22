while True:
    try:
        x = int(input("Ingrese un número: "))
        print(f"El número ingresado es: {x}")
        break
    except ValueError:
        print("Error: Por favor ingrese un número válido.")
    