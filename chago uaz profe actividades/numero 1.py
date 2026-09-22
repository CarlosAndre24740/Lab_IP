print("ingrese la altura")
h = float(input())
print("ingrese ancho")
w = float(input())
x = h / w
raiz = x ** 2 + float(1) / 16
s = 2 * w * raiz + 1 / 16 * x * log(x + raiz) + log(4)
print("La longitud de arco de la parábola es: " + Round(s, 4))
