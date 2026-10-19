class Autor():

    def __init__(self, id_autor: int, nombre: str, nacionalidad: str):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"Autor: {self.nombre} ({self.nacionalidad})"

class Libro():

    def __init__(self, id_libro: int, titulo: str, anio_publicacion: int, autor: Autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.autor = autor

    def __str__(self):
        return f"Libro: '{self.titulo}' ({self.anio_publicacion}) - {self.autor}"