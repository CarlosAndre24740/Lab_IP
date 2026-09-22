print("numero de terminos:")
n = float(input())
if n > 0:
    a = 2
    b = 1
    prod = 1
    i = 1
    while i <= n:
        prod = prod * a / b
        if i % 2 != 0:
            b = a + 1
        else:
            a = a + 2
            b = a - 1
        i = i == i + 1
    p1 = 2 * prod
    print("valor aproximado de pi" + str(p1))
else:
    print("el numero debe ser positivo")
