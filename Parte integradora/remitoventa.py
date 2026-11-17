class RemitoVenta:
    """
    Clase que representa un remito de venta.
    Un remito pertenece a un cliente y contiene una lista de detalles (RemitoVentaDetalle).
    Atributos:
        nombreCliente (str): nombre del cliente.
        numeroRemito (int): número identificador del remito.
        detallesRemito (lista): lista de objetos RemitoVentaDetalle.
        totalVenta (float): campo calculado = suma de los subtotales de los detalles.
    """

    def __init__(self, nombreCliente: str, numeroRemito: int):
        # Nombre del cliente que recibe el remito
        self.nombreCliente = nombreCliente
        # Número del remito
        self.numeroRemito = numeroRemito
        # Lista vacía donde se irán agregando los detalles del remito
        self.detallesRemito = []
        # Inicializamos el total en 0. Se calculará al agregar cada detalle.
        self.totalVenta = 0

    def agregarDetalle(self, detalle):
        """
        Agrega un detalle (RemitoVentaDetalle) a la lista de detalles del remito
        y recalcula el totalVenta sumando todos los subtotales.
        """
        # Agregamos el detalle a la lista
        self.detallesRemito.append(detalle)

        # Recalculamos el total sumando el subtotal de cada detalle
        total = 0
        for detalle in self.detallesRemito:
            total += detalle.subtotal

        # Asignamos el total calculado (fuera del bucle, una sola vez)
        self.totalVenta = total
