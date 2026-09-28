class Archivo:
    def __init__(self, nombre: str, tamano_bytes: int):
        self.nombre = nombre
        self.tamano_bytes = tamano_bytes

class Directorio:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.archivos = []        # Lista de objetos Archivo
        self.subdirectorios = []  # Lista de objetos Directorio