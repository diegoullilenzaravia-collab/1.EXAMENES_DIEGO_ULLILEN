#REPORTE DE CALIFICACIONES
matematicas = 17
ciencia = 14
historia = 15
#PESOS CURSOS
peso_matematicas = 0.40
peso_ciencia = 0.30
peso_historia = 0.30
#CALCULA NOTA FINAL PONDERADA
nota_final = (
    matematicas * peso_matematicas
    + ciencia * peso_ciencia
    + historia * peso_historia
)
#EVALUACION
aprobado = nota_final >= 13.0
#MOSTRAR RESULTADOS
print(f"La nota final es: {nota_final:.1f}")
print(f"¿Aprobado?: {aprobado}")

#GENERAR CADENA RESUMEN
if aprobado:
    estado = "Aprobado"
else:
    estado = "Desaprobado"
resumen = (
    f"El estudiante obtuvo una nota final de "
    f"{nota_final:.1f} y su estado final es: {estado}"
)

print(resumen)
