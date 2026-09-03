for numero in range(1, 101):
 if numero <=1:
        print(numero, "no es primo")
 else:
    for i in range(2, numero):
        if (numero % i) == 0:
            print(numero, "no es primo")
            break
    else:
        print(numero, "es primo")



   