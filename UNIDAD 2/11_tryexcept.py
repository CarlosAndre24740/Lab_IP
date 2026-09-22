while True:
    try:
        edad = int(input("edad: "))
        if 0 <= edad <= 120:
            break
        else:
            print("Por favor, la edad debe de estar entre  (0-120).")
    except ValueError:
        print("Por favor, ingrese un numero entero.")

print(f"Edad registrada: {edad}")   
