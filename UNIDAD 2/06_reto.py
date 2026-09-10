total= float(input("ingresa total de la cuenta"))
propina= float(input("ingresa el porcentaje de propina"))
personas= int(input("el total de personas que van a pagar"))

total_propina=total*(propina/100)
total_cuenta=total+total_propina
monto_por_persona=total_cuenta/personas

print(f"total de la cuenta: ${total: .2f}")
print(f"propina: ${total_propina: .2f}")
print(f"monto por persona: ${monto_por_persona: .2f}")


