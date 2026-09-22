print("Monto total de la compra $: ")
monto = float(input())
if monto < 500:
    descuento = 0.05
    total = monto - monto * descuento
else:
    if monto < 1000:
        descuento = 0.05
    else:
        if monto < 7000:
            descuento = 0.1
        else:
            if monto < 15000:
                descuento = 0.15
            else:
                descuento = 0.25
print("El total a pagar incluyendo el descuento es $: " + Round(total, 2))
