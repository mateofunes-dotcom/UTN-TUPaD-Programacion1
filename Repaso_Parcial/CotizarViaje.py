
from Actividad import Actividad
from Ciudad import Ciudad
from DiaViaje import DiaViaje
from PaqueteViaje import PaqueteViaje


class CotizarViaje:

    # Método principal del programa
    def main(self):

        # Lista donde vamos a guardar los precios del archivo
        costoActividades = []

        # Abrimos el archivo para leer los precios
        archivo = open("viajes.txt", "r")

        # Leemos cada línea del archivo
        for linea in archivo:

            # Separamos los datos utilizando ;
            datos = linea.strip().split(";")

            # Guardamos los datos en la lista
            costoActividades.append(datos)

        # Cerramos el archivo
        archivo.close()

        # Solicitamos el nombre del paquete
        nombre = input("Ingrese el nombre del viaje: ")

        # Creamos el paquete
        paquete = PaqueteViaje(nombre)

        # Validamos la cantidad de días
        cantidadDias = int(input("Ingrese la cantidad de días (7 a 30): "))

        while cantidadDias < 7 or cantidadDias > 30:
            print("La cantidad de días debe estar entre 7 y 30")
            cantidadDias = int(input("Ingrese nuevamente la cantidad de días: "))

        # Variable para controlar el costo acumulado
        totalAcumulado = 0

        # Recorremos todos los días del viaje
        for i in range(1, cantidadDias + 1):

            # Creamos un día
            dia = DiaViaje(i)

            print("\nDÍA:", i)

            # Preguntamos cuántas ciudades tendrá este día
            cantidadCiudades = int(input("Ingrese la cantidad de ciudades: "))

            # Recorremos las ciudades
            for j in range(cantidadCiudades):

                # Solicitamos los datos de la ciudad
                nombreCiudad = input("Ingrese el nombre de la ciudad: ")
                nombrePais = input("Ingrese el país: ")

                # Creamos la ciudad
                ciudad = Ciudad(nombreCiudad, nombrePais)

                # Pedimos la cantidad de actividades
                cantidadActividades = int(input("Cantidad de actividades (3 a 7): "))

                # Validamos la cantidad mínima y máxima
                while cantidadActividades < 3 or cantidadActividades > 7:
                    print("Debe ingresar entre 3 y 7 actividades")
                    cantidadActividades = int(input("Cantidad de actividades: "))

                # Lista para controlar actividades repetidas
                actividadesAgregadas = []

                # Variable para controlar los hoteles
                hotelAgregado = False

                # Recorremos las actividades
                for k in range(cantidadActividades):

                    print("\nACTIVIDADES DISPONIBLES")

                    # Mostramos las actividades del archivo
                    for dato in costoActividades:
                        print(dato[0], "-", dato[1])

                    # Solicitamos el código de actividad
                    codigo = input("Ingrese el código de actividad: ")

                    # Buscamos la actividad seleccionada
                    actividadEncontrada = None

                    for dato in costoActividades:
                        if dato[0] == codigo:
                            actividadEncontrada = dato

                    # Validamos que el código exista
                    while actividadEncontrada == None:
                        print("Código incorrecto")
                        codigo = input("Ingrese nuevamente el código: ")

                        for dato in costoActividades:
                            if dato[0] == codigo:
                                actividadEncontrada = dato

                    # Validamos que no se repita
                    while codigo in actividadesAgregadas:
                        print("Esta actividad ya fue agregada")
                        codigo = input("Ingrese otro código: ")

                        actividadEncontrada = None

                        for dato in costoActividades:
                            if dato[0] == codigo:
                                actividadEncontrada = dato

                        while actividadEncontrada == None:
                            print("Código incorrecto")
                            codigo = input("Ingrese nuevamente el código: ")

                            for dato in costoActividades:
                                if dato[0] == codigo:
                                    actividadEncontrada = dato

                    # Validamos que los hoteles no se repitan entre sí
                    while codigo in ["500", "600", "700"] and hotelAgregado:
                        print("Ya agregó un hotel. No puede agregar otro.")
                        codigo = input("Ingrese otro código: ")

                        actividadEncontrada = None

                        for dato in costoActividades:
                            if dato[0] == codigo:
                                actividadEncontrada = dato

                        while actividadEncontrada == None or codigo in actividadesAgregadas:
                            print("Código incorrecto o actividad repetida")
                            codigo = input("Ingrese otro código: ")

                            actividadEncontrada = None

                            for dato in costoActividades:
                                if dato[0] == codigo:
                                    actividadEncontrada = dato

                    # Guardamos el código para evitar repeticiones
                    actividadesAgregadas.append(codigo)

                    # Si es un hotel, indicamos que ya hay uno
                    if codigo in ["500", "600", "700"]:
                        hotelAgregado = True

                    # Preguntamos el tipo de actividad
                    tipo = input("Ingrese S para estándar o E para exclusive: ").upper()

                    while tipo != "S" and tipo != "E":
                        print("Tipo incorrecto")
                        tipo = input("Ingrese S o E: ").upper()

                    # Seleccionamos el costo según el tipo
                    if tipo == "S":
                        costo = int(actividadEncontrada[2])
                    else:
                        costo = int(actividadEncontrada[3])

                    # Creamos el objeto actividad
                    actividad = Actividad(actividadEncontrada[1], tipo, costo)

                    # Agregamos la actividad a la ciudad
                    ciudad.agregarActividad(actividad)

                    # Sumamos el costo acumulado
                    totalAcumulado = totalAcumulado + costo

                    # Controlamos que no supere los 10 millones
                    if totalAcumulado > 10000000:
                        print("El viaje supera los 10 millones de pesos")
                        return

                # Agregamos la ciudad al día
                dia.agregarCiudad(ciudad)

            # Agregamos el día al paquete
            paquete.agregarDia(dia)

        # Calculamos el costo total del viaje
        total = paquete.calcularTotalCostoViaje()

        # Mostramos el resultado
        print("\n----------- PAQUETE -----------")
        print("Nombre:", paquete.nombre)
        print("Total días:", paquete.cantidadDias(), "días")

        # Recorremos los días
        for dia in paquete.dias:

            print("\n----------- DÍA", dia.numeroDia, "-----------")

            # Recorremos las ciudades
            for ciudad in dia.ciudades:

                print("\nCiudad:", ciudad.nombreCiudad)
                print("País:", ciudad.nombrePais)

                print("----------- ACTIVIDADES -----------")

                # Mostramos cada actividad
                for actividad in ciudad.actividades:
                    print(actividad.tipoActividad, "Tipo:", actividad.tipo,
                          "$", actividad.costoActividad)

                # Mostramos el costo de las actividades de la ciudad
                print("COSTO TOTAL ACTIVIDADES: $", ciudad.totalActividades())

        # Mostramos el costo total del viaje
        print("\nCOSTO TOTAL VIAJE: $", total)

        # Calculamos el promedio por día
        promedio = total / paquete.cantidadDias()

        print("COSTO PROMEDIO POR DIA: $", promedio)


# Creamos el objeto y ejecutamos el programa
programa = CotizarViaje()
programa.main()
