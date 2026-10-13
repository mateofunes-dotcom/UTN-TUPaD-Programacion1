from vivienda import Vivienda


class Barrio:
    def __init__(self, nombre: str, empresaConstructora: str):
        self.nombre = nombre
        self.empresaConstructora = empresaConstructora
        self.viviendas: list[Vivienda] = []

    def getSuperficieTotalTerreno(self) -> float:
        total = 0.0
        for vivienda in self.viviendas:
            total += vivienda.superficieTerreno
        return total

    def getSuperficieTotalTerrenoXManzana(self, manzana: str) -> float:
        total = 0.0
        for vivienda in self.viviendas:
            if vivienda.manzana == manzana:
                total += vivienda.superficieTerreno
        return total

    def getSuperficieTotalCubierta(self) -> float:
        total = 0.0
        for vivienda in self.viviendas:
            total += vivienda.getMetrosCuadradosCubiertos()
        return total