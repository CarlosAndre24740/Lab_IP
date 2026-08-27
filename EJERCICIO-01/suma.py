numero, binario=8, ""#asigna el valor del numero
if numero==0: print("0")#si el numero es 0 imprime 0
binario=""#crea una variable vacio para almacenar el resultado
while numero>0:#mientras el numero sea mayor a 0 
    binario= str(numero%2)+binario#
    numero=numero//2#numero se divide entre 2 y se asigna a numero 
print(binario)#imprime el resultado 