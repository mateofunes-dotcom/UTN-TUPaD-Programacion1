from articulo import Articulo
from repartodiario import RepartoDiario
from remitoventa import RemitoVenta
from remitoventadetalle import RemitoVentaDetalle


class CrearRepartoDiario:
    """
    Clase principal que contiene el método main.
    Encargada de crear los artículos, los clientes, los remitos de venta
    y el reparto diario, e interactuar con el usuario por consola.
    """

    def __init__(self):
        # Lista que contendrá los objetos Articulo disponibles para la venta
        self.articulosDisponibles = []
        # Diccionario donde la clave es el CUIT y el valor es la razón social del cliente
        self.clientesReparto = {}

    def buscarCliente(self):
        """
        Solicita el CUIT del cliente y busca su nombre en el diccionario clientesReparto.
        Si el CUIT no existe, pide el nombre del cliente, lo agrega al diccionario
        y lo retorna.
        """
        cuit = input("Ingrese el CUIT: ")
        if cuit in self.clientesReparto:
            # El CUIT ya existe, retornamos el nombre guardado
            return self.clientesReparto[cuit]
        else:
            # El CUIT no existe, pedimos el nombre y lo guardamos en el diccionario
            razon = input("Ingrese nombre del cliente: ")
            self.clientesReparto[cuit] = razon
            return self.clientesReparto[cuit]

    def main(self):
        """
        Flujo principal del programa:
        1. Carga los artículos disponibles y los clientes iniciales.
        2. Solicita la fecha del reparto y crea el RepartoDiario.
        3. Ciclo para cargar remitos de venta con sus detalles.
        4. Muestra el resumen final del reparto.
        """

        # --- Carga de artículos disponibles ---
        self.articulosDisponibles.append(Articulo(codigo="10", denominacion="Filtro de Aceite", precio=10000))
        self.articulosDisponibles.append(Articulo(codigo="20", denominacion="Filtro de Aire", precio=8000))
        self.articulosDisponibles.append(Articulo(codigo="30", denominacion="Filtro de Combustible", precio=7500))
        self.articulosDisponibles.append(Articulo(codigo="40", denominacion="Aceite de Motor sw/10", precio=25000))
        self.articulosDisponibles.append(Articulo(codigo="50", denominacion="Correa de Distribucion", precio=20000))

        # --- Carga de clientes iniciales (CUIT -> Razon Social) ---
        self.clientesReparto = {
            "20284569875": "Juan Alonso",
            "20157896542": "Emiliano Salas",
            "50258963654": "Pacallcar Autos",
            "27654987456": "Julieta Videla",
            "50335588945": "Todo Auto SRL"
        }

        # --- Paso 1: solicitar fecha y crear el RepartoDiario ---
        fecha = input("Ingrese la fecha del reparto: ")
        reparto = RepartoDiario(fecha)

        # --- Paso 2 y 3: ciclo de carga de remitos de venta ---
        while True:
            # Buscamos o registramos al cliente del remito
            nombreCliente = self.buscarCliente()
            numeroRemito = int(input("Ingrese el número de remito: "))

            # Creamos el remito de venta vacío
            remito = RemitoVenta(nombreCliente, numeroRemito)

            # Ciclo para cargar al menos un detalle al remito
            while True:
                # Pedimos el código del artículo y validamos que exista en la lista
                while True:
                    codigo = input("Ingrese el código del artículo: ")
                    objetoEncontrado = None
                    for articulo in self.articulosDisponibles:
                        if codigo == articulo.codigo:
                            objetoEncontrado = articulo
                            break
                    if objetoEncontrado is not None:
                        break
                    print("el código es incorrecto, ingrese nuevamente")

                # Pedimos la cantidad y validamos que sea mayor a cero
                while True:
                    unidades = int(input("Ingrese la cantidad que desea comprar: "))
                    if unidades > 0:
                        break
                    print("La cantidad debe ser mayor a cero. Ingrese nuevamente.")

                # Creamos el detalle y lo agregamos al remito
                detalleNuevo = RemitoVentaDetalle(unidades, objetoEncontrado)
                remito.agregarDetalle(detalleNuevo)

                # Preguntamos si desea agregar otro artículo a este remito
                respuesta = input("¿Desea agregar otro artículo al remito? (sí/no): ")
                if respuesta.lower() == "no":
                    break
                
            # Agregamos el remito cargado al reparto diario
            reparto.agregarRemito(remito)

            # Preguntamos si desea cargar otro remito al reparto
            respuesta = input("¿Desea agregar otro remito al reparto? (sí/no): ")
            if respuesta.lower() == "no":
                break

        # --- Paso 4: mostrar el resumen final del reparto ---
        print()
        reparto.mostrarReparto()


# Punto de entrada del programa: creamos la instancia y ejecutamos main
if __name__ == "__main__":
    programa = CrearRepartoDiario()
    programa.main()
