
class Ciudad:

    # Constructor de la ciudad
    def __init__(self, nombreCiudad, nombrePais):
        self.nombreCiudad = nombreCiudad
        self.nombrePais = nombrePais
        self.actividades = []

    # Agrega una actividad a la lista
    def agregarActividad(self, actividad):
        self.actividades.append(actividad)

    # Calcula el costo de todas las actividades
    def totalActividades(self):
        total = 0

        for actividad in self.actividades:
            total = total + actividad.costoActividad

        return total
