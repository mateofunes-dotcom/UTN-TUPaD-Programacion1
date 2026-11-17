
class PaqueteViaje:

    # Constructor del paquete
    def __init__(self, nombre):
        self.nombre = nombre
        self.totalCostoViaje = 0
        self.dias = []

    # Agrega un día al paquete
    def agregarDia(self, dia):
        self.dias.append(dia)

    # Calcula el costo total del viaje
    def calcularTotalCostoViaje(self):
        total = 0

        for dia in self.dias:
            total = total + dia.totalDia()

        self.totalCostoViaje = total

        return total

    # Calcula la cantidad de días
    def cantidadDias(self):
        return len(self.dias)
