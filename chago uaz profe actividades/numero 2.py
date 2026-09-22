print("Dame el costo del artículo deportivo: ")
costo = float(input())
print("Dame el pago del cliente: ")
pago = float(input())
if costo < pago:
    print("Con esa cantidad no se alcanza a pagar")
else:
    cambio = pago - costo
    print("El cambio es: " + cambio)
