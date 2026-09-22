print("dame un numero")
n = int(input())
if n > 0:
    f = 0
    x = 0
    print("segun la funcion la serie es: " + str(f))
    while x < n:
        x = x + 1
        f = 2 * f + x ** 2
        print("segun la funcion la serie es:" + str(f))
