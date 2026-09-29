USUARIO = "alumno"
CLAVE = "python123"

usuario_ingresado = input("usuario: ").strip().lower()
clave = input("contraseña: ")

if usuario_ingresado == USUARIO and clave == CLAVE:
    print("Bienvenido")
else:
    print("usuario o contraseña incorrectos")