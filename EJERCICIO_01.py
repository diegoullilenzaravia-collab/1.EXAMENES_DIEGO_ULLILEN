#ASIGNAR DATOS USUARIO
nombre = "Diego"
salario = 2500.50
edad = "32"
compania = "Hospital Belen de Trujillo"

#IDENTIFICAR TIPOS DE VARIABLE
print("Nombre:", nombre, "- Tipo:", type(nombre))
print("Salario:", salario, "- Tipo:", type(salario))
print("Edad:", edad, "- Tipo:", type(edad))
print("Compania:", compania, "- Tipo:", type(compania))

#Convertir la edad de string a entero
edad= int(edad)

#PORCENTAJE DE BONO
if edad > 30:
    porcentaje = 0.10
    print("Usted tiene un bono de 10% en el mes de diciembre")
else:
    porcentaje = 0.05
    print("Usted tiene un bono del 5% en el mes de diciembre")
#CALCULAR BONO FINAL
porcentaje_bono = salario ** 2 + ( salario * porcentaje)

#MOSTRAR RESULTADO
print("Nombre del usuario:", nombre)
print("Edad convertida a entero:", edad)
print("porcentaje_bono:", porcentaje_bono)