
class DiaViaje:

    # Constructor del día
    def __init__(self, numeroDia):
        self.numeroDia = numeroDia
        self.ciudades = []

    # Agrega una ciudad al día
    def agregarCiudad(self, ciudad):
        self.ciudades.append(ciudad)

    # Calcula el costo de todas las ciudades del día
    def totalDia(self):
        total = 0

        for ciudad in self.ciudades:
            total = total + ciudad.totalActividades()

        return total
