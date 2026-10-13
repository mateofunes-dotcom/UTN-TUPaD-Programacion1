from componentecpu import ComponenteCPU

class Computadora:

    def __init__(self,marca :str, modelo :str):
        self.marca = marca
        self.modelo = modelo
        self.componentes = []