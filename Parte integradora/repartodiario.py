from remitoventa import RemitoVenta


class RepartoDiario:
    """
    Clase que representa un reparto diario de ventas.
    Contiene una lista de remitos de venta y la fecha del reparto.
    Atributos:
        fecha (str): fecha del reparto.
        remitosVenta (lista): lista de objetos RemitoVenta asociados al reparto.
        totalReparto (float): campo calculado = suma del totalVenta de todos los remitos.
    """

    def __init__(self, fecha: str):
        # Fecha del reparto (ejemplo: "16/11/2026")
        self.fecha = fecha
        # Lista vacía donde se irán agregando los remitos de venta
        self.remitosVenta = []
        # Inicializamos el total del reparto en 0. Se recalculará al agregar cada remito.
        self.totalReparto = 0

    def agregarRemito(self, remito):
        """
        Agrega un remito de venta a la lista del reparto
        y recalcula el totalReparto sumando los totalVenta de todos los remitos.
        """
        # Agregamos el remito a la lista
        self.remitosVenta.append(remito)

        # Recalculamos el total del reparto sumando el totalVenta de cada remito
        total = 0
        for remito in self.remitosVenta:
            total += remito.totalVenta

        # Asignamos el total calculado (fuera del bucle, una sola vez)
        self.totalReparto = total

    def mostrarReparto(self):
        """
        Muestra por pantalla el resumen completo del reparto diario:
        fecha, cada remito con sus detalles y el monto total del reparto.
        """
        print("Reparto Diario")
        print("Fecha:", self.fecha)
        print("--------------Remitos del Reparto----------------")

        # Recorremos cada remito del reparto para mostrar sus datos
        for remito in self.remitosVenta:
            print("Nombre Cliente:", remito.nombreCliente)
            print("Numero Remito:", remito.numeroRemito)
            print("Cantidad  Items  Denominación Articulo   Precio Unitario")

            # Mostramos cada detalle del remito actual
            for detalle in remito.detallesRemito:
                print(detalle.cantidad, "      ",
                      detalle.articulo.denominacion, "      ",
                      detalle.articulo.precio)

            print("Total Remito Venta:", remito.totalVenta)

        print("---------------------------------")
        print("Monto Total Reparto:", self.totalReparto)
