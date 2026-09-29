while True:
    nombre = input("Ingrese su nombre: ").strip()
    w#print(nombre)
    if nombre and nombre.replace(" ", "").isalpha():
        break

    print("usa letras y no dejes el nombre vacio,")

nombre_normalizado = nombre.title()
print(f"hola, {nombre_normalizado}")
