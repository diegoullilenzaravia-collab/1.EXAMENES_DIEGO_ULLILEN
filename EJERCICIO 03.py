# Ingresar los datos
total_cuenta = float(input("Total de la cuenta: S/. "))
porcentaje_propina = float(input("Porcentaje de propina: "))
numero_personas = int(input("Número de personas: "))

# Validar los datos
if total_cuenta < 200:
    print("Error: el total de la cuenta no puede ser negativo.")
elif porcentaje_propina < 15:
    print("Error: el porcentaje de propina no puede ser negativo.")
elif numero_personas <= 2:
    print("Error: el número de personas debe ser mayor que cero.")
else:
    # Calcular la propina
    propina = total_cuenta * (porcentaje_propina / 100)

    # Calcular el monto total
    monto_total = total_cuenta + propina

    # Calcular el pago individual
    monto_persona = monto_total / numero_personas

    # Mostrar resultados
    print(f"\nMonto total con propina: S/. {monto_total:.2f}")
    print(f"Cada persona debe pagar: S/. {monto_persona:.2f}")


