
from datetime import datetime

class Persona:

    def __init__(self, nombre, edad, saldo=0):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        self.nacionalidad = "Peruana"
        self.fecha_registro = datetime.now()

    # Consultar saldo
    def consultar_saldo(self):
        print(f"Saldo de {self.nombre}: S/. {self.saldo:.2f}")

    # Realizar transferencia
    def transferir(self, receptor, monto):

        try:
            monto = float(monto)

        except (ValueError, TypeError):
            print("Error: El monto debe ser numérico.")
            return

        # Validar monto positivo
        if monto <= 0:
            print("Error: El monto debe ser mayor que cero.")
            return

        # Validar saldo disponible
        if monto > self.saldo:
            print("Error: Saldo insuficiente para realizar la transferencia.")
            return

        # Ejecutar transferencia
        self.saldo -= monto
        receptor.saldo += monto

        print("\n¡Transferencia realizada exitosamente!")
        print("Persona que envía:", self.nombre)
        print("Persona que recibe:", receptor.nombre)
        print(f"Monto transferido: S/. {monto:.2f}")

    # Método cumpleaños
    def cumpleanios(self):
        self.edad += 1

    # Mostrar fecha de registro
    def mostrar_fecha_registro(self):
        fecha = self.fecha_registro.strftime("%d/%m/%Y %H:%M")
        print(f"Registro de {self.nombre}: {fecha}")


# CREAR DOS PERSONAS

persona1 = Persona("DIEGO ULLILEN", 28, 1500.00)
persona2 = Persona("PIERO VASQUEZ", 23, 800.00)


# MOSTRAR SALDOS INICIALES

print("===== SALDOS INICIALES =====")

persona1.consultar_saldo()
persona2.consultar_saldo()


# PRIMERA TRANSFERENCIA VÁLIDA

print("\n===== TRANSFERENCIA VÁLIDA =====")

persona1.transferir(persona2, 300.00)


# MOSTRAR SALDOS ACTUALIZADOS

print("\n===== SALDOS DESPUÉS DE LA TRANSFERENCIA =====")

persona1.consultar_saldo()
persona2.consultar_saldo()


# SEGUNDA TRANSFERENCIA RECHAZADA

print("\n===== TRANSFERENCIA RECHAZADA =====")

persona1.transferir(persona2, 2000.00)


# COMPROBAR QUE LOS SALDOS NO CAMBIARON

print("\n===== SALDOS FINALES =====")

persona1.consultar_saldo()
persona2.consultar_saldo()
