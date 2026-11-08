# 1. Funcion para solicitar dos valores numericos
def solicitar_numeros():
    while True:
        try:
            numero1 = float(input("Ingrese el primer numero: "))
            numero2 = float(input("Ingrese el segundo numero: "))

        except ValueError:
            print("Error: Debe ingresar valores numericos.")
            continue

        else:
            return numero1, numero2

        finally:
            print("Proceso de ingreso de numeros finalizado.")


# 2. Funcion para realizar una division
def dividir(a, b):
    try:
        resultado = a / b

    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
        return None

    else:
        return resultado

    finally:
        print("Operacion de division ejecutada.")


# 3. Funcion para realizar una suma
def sumar(a, b):
    return a + b


# 4. Funcion para registrar elementos en una lista
def registrar_elementos():
    elementos = []

    while True:
        try:
            cantidad = int(input("Cuantos usuarios desea registrar? "))

            if cantidad <= 0:
                print("Ingrese una cantidad mayor que cero.")
                continue

            break

        except ValueError:
            print("Error: Ingrese un numero entero.")

    for i in range(cantidad):
        nombre = input(f"Ingrese el nombre del usuario {i + 1}: ")
        elementos.append(nombre)

    return elementos


# 5. Funcion para consultar un elemento por indice
def consultar_elemento(lista):
    while True:
        try:
            indice = int(input("Ingrese el indice que desea consultar: "))
            print("Usuario encontrado:", lista[indice])
            break

        except ValueError:
            print("Error: Ingrese un indice numerico.")

        except IndexError:
            print("Error: El indice no existe. Intente nuevamente.")


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

print("========== EXAMEN DE PYTHON ==========")

# Datos numericos de ejemplo
print("\nREGISTRO DE NUMEROS")
numero1 = 20
numero2 = 5

print("Primer numero:", numero1)
print("Segundo numero:", numero2)

# Division
resultado_division = dividir(numero1, numero2)
print("Resultado de la division:", resultado_division)

# Suma
resultado_suma = sumar(numero1, numero2)
print("Resultado de la suma:", resultado_suma)

# Registro de usuarios
print("\nREGISTRO DE USUARIOS")

usuarios = ["Diego", "Pedro", "Juan"]

for usuario in usuarios:
    print("Usuario registrado:", usuario)

# Consulta por indice
print("\nCONSULTA DE USUARIO")

indice = 1

try:
    print("Usuario en el indice", indice, ":", usuarios[indice])

except IndexError:
    print("Error: El indice no existe.")

# Resumen final
print("\n========== RESULTADOS FINALES ==========")
print("Division:", resultado_division)
print("Suma:", resultado_suma)
print("Cantidad de usuarios:", len(usuarios))
print("Lista de usuarios:", usuarios)
print("========================================")
