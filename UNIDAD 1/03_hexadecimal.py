numero=30
if numero==0:
    print("0")
hexadecimal=""
while numero>0:
    residuo=numero%16
    if residuo==10:
            hexadecimal="A"+hexadecimal
    elif residuo==11:
            hexadecimal="B"+hexadecimal
    elif residuo==12:
            hexadecimal="C"+hexadecimal
    elif residuo==13:
            hexadecimal="D"+hexadecimal
    elif residuo==14:
            hexadecimal="E"+hexadecimal
    elif residuo==15:
            hexadecimal="F"+hexadecimal
    else:hexadecimal= str(residuo)+hexadecimal
    numero=numero//16
print(hexadecimal)
