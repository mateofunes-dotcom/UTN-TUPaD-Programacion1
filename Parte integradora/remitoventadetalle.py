from articulo import Articulo


class RemitoVentaDetalle:
    """
    Clase que representa un detalle de un remito de venta.
    Un detalle indica cuántas unidades de un artículo se venden.
    Atributos:
        cantidad (int): cantidad de unidades del artículo.
        articulo (Articulo): objeto Articulo asociado a este detalle.
        subtotal (float): campo calculado = cantidad * precio del artículo.
    """

    def __init__(self, cantidad: int, articulo: Articulo):
        # Cantidad de unidades del artículo en este detalle
        self.cantidad = cantidad
        # Objeto Articulo al que pertenece este detalle
        self.articulo = articulo
        # Subtotal calculado: multiplicamos la cantidad por el precio del artículo
        self.subtotal = cantidad * articulo.precio