print("dame un primer numero entero")
a = int(input())
print("dame un segundo numero entero")
b = int(input())
if a <= b:
    menor = a
    mayor = b
else:
    menor = b
    mayor = a
suma = 0
for i in range(menor, mayor + 1, 1):
    if i % 2 != 0:
        suma = suma + i
print("la suma de los menores impares entre los menores imapres que me diste son" + str(suma))
# Nombre = input()
