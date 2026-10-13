from barrio import Barrio
from habitacion import Habitacion
from vivienda import Vivienda


class PruebaBarrio:
    def main(self):
        barrio = Barrio("Los Alamos", "Constructora Sur")

        vivienda1 = Vivienda("San Martin", 100, "A", 1, 200.0)
        vivienda1.habitaciones.append(Habitacion("Living", 40.0))
        vivienda1.habitaciones.append(Habitacion("Cocina", 15.0))
        vivienda1.habitaciones.append(Habitacion("Dormitorio", 20.0))

        vivienda2 = Vivienda("San Martin", 120, "A", 2, 150.0)
        vivienda2.habitaciones.append(Habitacion("Living", 30.0))
        vivienda2.habitaciones.append(Habitacion("Dormitorio", 25.0))

        vivienda3 = Vivienda("Belgrano", 50, "B", 3, 300.0)
        vivienda3.habitaciones.append(Habitacion("Living", 50.0))
        vivienda3.habitaciones.append(Habitacion("Cocina", 20.0))
        vivienda3.habitaciones.append(Habitacion("Dormitorio", 30.0))
        vivienda3.habitaciones.append(Habitacion("Bano", 8.0))

        barrio.viviendas.append(vivienda1)
        barrio.viviendas.append(vivienda2)
        barrio.viviendas.append(vivienda3)

        print("Superficie total de terreno:", barrio.getSuperficieTotalTerreno())
        print("Superficie de terreno manzana A:", barrio.getSuperficieTotalTerrenoXManzana("A"))
        print("Superficie de terreno manzana B:", barrio.getSuperficieTotalTerrenoXManzana("B"))
        print("Metros cubiertos vivienda 1:", vivienda1.getMetrosCuadradosCubiertos())
        print("Metros cubiertos vivienda 2:", vivienda2.getMetrosCuadradosCubiertos())
        print("Metros cubiertos vivienda 3:", vivienda3.getMetrosCuadradosCubiertos())
        print("Superficie total cubierta:", barrio.getSuperficieTotalCubierta())


if __name__ == "__main__":
    PruebaBarrio().main()