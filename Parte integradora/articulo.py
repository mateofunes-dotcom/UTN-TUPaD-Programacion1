class Articulo:
    """
    Clase que representa un artículo o producto.
    Atributos:
        codigo (str): código identificador del artículo.
        denominacion (str): nombre o descripción del artículo.
        precio (float): precio unitario del artículo.
    """

    def __init__(self, codigo: str, denominacion: str, precio: float):
        # Código del artículo (ejemplo: "10", "20", etc.)
        self.codigo = codigo
        # Nombre o descripción del artículo (ejemplo: "Filtro de Aceite")
        self.denominacion = denominacion
        # Precio unitario del artículo
        self.precio = precio
