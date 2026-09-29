
inicioCicloexterior = int(input("dame un ciclo exterior"))
fincicloexterior = int(input("dame un fin del ciclo exterior"))
inicioCiclointerior = int(input("dame un inicio del ciclo interior"))
finciclointerior = int(input("dame el fin del ciclo interior"))
i = inicioCicloexterior
while i <= fincicloexterior:
    print("T A B L A=  " + str(i))
    j = inicioCiclointerior
    while j <= finciclointerior:
        print(str(i) + "  x  " + str(j) + "  =  " + str(i * j))
        j = j + 1
    i = i + 1
