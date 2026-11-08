
from datetime import datetime


class Persona:

    # Constructor de la clase
    def __init__(self, nombre="", edad=0, saldo=0.0,
                 nacionalidad="Peruana"):

        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        self.nacionalidad = nacionalidad

        # Registrar fecha y hora de creación
        self.fecha_registro = datetime.now()

    # Método para registrar nombre y edad
    def registrar_persona(self):

        self.nombre = input("Ingrese el nombre: ").upper()

        while True:
            try:
                edad = int(input("Ingrese la edad: "))

                if edad < 0:
                    print("Error: La edad no puede ser negativa.")
                else:
                    self.edad = edad
                    break

            except ValueError:
                print("Error: Ingrese una edad válida en números enteros.")

    # Método cumpleaños
    def cumpleaños(self):
        self.edad += 1

    # Método para mostrar los datos
    def mostrar_datos(self):

        print("\n------- DATOS DE LA PERSONA -------")
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Saldo: S/.", self.saldo)
        print("Nacionalidad:", self.nacionalidad)


# Función para mostrar fecha y hora de registro
def mostrar_fecha_registro(persona):

    fecha = persona.fecha_registro.strftime("%d/%m/%Y %H:%M")

    print("Fecha y hora de registro:", fecha)


# ---------------------------------------
# CREACIÓN DE LOS OBJETOS
# ---------------------------------------

persona1 = Persona("DIEGO", 28, 1500.50)
persona2 = Persona("PIERO", 23, 2300.75)


# ---------------------------------------
# MOSTRAR DATOS INICIALES
# ---------------------------------------

print("\n========== PERSONA 1 ==========")
persona1.mostrar_datos()
mostrar_fecha_registro(persona1)

print("\n========== PERSONA 2 ==========")
persona2.mostrar_datos()
mostrar_fecha_registro(persona2)


# ---------------------------------------
# APLICAR MÉTODO CUMPLEAÑOS
# ---------------------------------------

persona1.cumpleaños()
persona2.cumpleaños()


# ---------------------------------------
# MOSTRAR EDADES ACTUALIZADAS
# ---------------------------------------

print("\n========== EDADES ACTUALIZADAS ==========")

print(persona1.nombre, "cumplió años. Nueva edad:", persona1.edad)

print(persona2.nombre, "cumplió años. Nueva edad:", persona2.edad)
