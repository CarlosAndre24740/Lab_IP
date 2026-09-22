print("dame un numero")
n = int(input())
suma = 0
texto = ""
for i in range(1, n + 1, 1):
    suma = suma + i
    if texto != "":
        texto = texto + "+"
        texto = texto + i
print("La suma de todos sus divisores menores o iguales a él es:")
print(texto + "=" + suma)
