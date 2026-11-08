participantes = []

# 2. Agregar los nombres de tres participantes
participantes.append("Diego")
participantes.append("Piero")
participantes.append("Julio")

# 3. Insertar un nuevo participante en la segunda posición
participantes.insert(1, "Carlos")

# 4. Actualizar el nombre del primer participante
participantes[0] = "Andrés"

# 5. Eliminar uno de los participantes
participantes.remove("Piero")

# 6. Mostrar la lista final y la cantidad de participantes
print("Lista final de participantes:", participantes)
print("Cantidad de participantes registrados:", len(participantes))
