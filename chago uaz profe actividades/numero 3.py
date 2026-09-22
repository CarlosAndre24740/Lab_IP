print("Ingresa largo del terreno: ")
largo = float(input())
print("Ingresa ancho del terreno: ")
ancho = float(input())
print("Ingresa precio por metro cuadrado de terreno $: ")
precioM2 = float(input())
area = largo * ancho
if are > 1000:
    decuento = 0.25
else:
    if area > 500:
        descuento = 0.17
    else:
        descuento = 0
precio = area * precioM2 * 1 - descuento
print("Precio del terreno es: $ " + Round(precio, 2))
