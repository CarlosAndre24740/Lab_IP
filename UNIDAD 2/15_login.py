MAX = 3

for intento in range(1, MAX + 1):
    usuario = input("usuario: ")
    clave = input("contraseña: ")

    if usuario == "alumno" and clave == "python123":
        print("Bienvenido")
        break

    print("usuario o contraseña incorrectos")
else:
    print("Se han agotado los intentos")