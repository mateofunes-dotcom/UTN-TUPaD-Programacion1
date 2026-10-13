from ingrediente import Ingrediente
from plato import Plato

class MenuRestaurant:

    @staticmethod
    def main():
        platos_menu = []

        print("\n------ MENÚ del RESTAURANT ------")

        while True:
            print("\n--- Nuevo Plato ---")
            nombre_plato = input("Ingresa el nombre del plato o bebida: ")

            # Validación de precio en decimal
            precio_str = input("Ingrese el precio del producto: ")
            if not precio_str.replace(".", "", 1).isdigit():
                print("ERROR! Debe ser valor númerico.")
                continue
            precio = float(precio_str)

            #Es bebida?
            esBebida = (input("¿Es una bebida? (S/N): ").strip().upper())
            es_bebida = (
                esBebida == "SI" or esBebida == "S"
            )

            #Craemos instancia del plato
            nuevo_plato = Plato(nombre_plato, precio, es_bebida)

            if not es_bebida:
                while True:
                    print("\n--- Carga los ingredientes del plato ---")
                    nombre_ingrediente = input("Nombre del Ingrediente: ")

                    #validacion de cantidad decimal
                    cantidad_str = input("Cantidad: ")
                    if not cantidad_str.replace(".", "", 1).isdigit():
                        print("ERROR! Debe ser en números.")
                        continue
                    cantidadIngrediente = float(cantidad_str)

                    unidadMedida = input(
                        "Unidad de medida (EJ: gramos, militros, unidades)"
                    )

                    #Creamos el ingrediente y lo agregamos al plato
                    nuevo_ingrediente = Ingrediente(
                        nombre_ingrediente, cantidadIngrediente, unidadMedida
                    )

                    nuevo_plato.ingredientes.append(nuevo_ingrediente)

                    salirIngredientes = (
                        input("¿Deseas salir de la pestaña INGREDIENTES? (S/N): ")
                        .strip()
                        .upper()
                    )
                    if (
                        salirIngredientes == "SI" or salirIngredientes == "S"
                    ):
                        break

                    # Validación: si no es bebida, debe tener al menos 1 ingrediente
                    if len(nuevo_plato.ingredientes) == 0:
                        print(
                        "ERROR! El plato debe tener al menos un ingrediente. Intente cargarlo nuevamente."
                    )
                    continue

                #Agregamos el plato completo a la lista
                platos_menu.append(nuevo_plato)
                
                salirMenu = (
                    input("¿Deseas salir de la CARGA DE PLATOS? (S/N): ")
                    .strip()
                    .upper()
                )

                if salirMenu == "SI" or salirMenu == "S":
                    break

        print("#################")
        print("\n----- MENÚ ----")
        print("#################")

        for plato in platos_menu:
            print(f"\n{plato.nombreCompleto}")
            print(f"Precio: $ {plato.precio}")

            if not plato.esBebida and len(plato.ingredientes) > 0:
                print("Ingredientes:")
                print(f"{nombre_plato:<20} | {cantidadIngrediente:<10} | {unidadMedida}")
                print("-" * 50)
                for ingrediente in plato.ingredientes:
                    print(
                        f"{ingrediente.nombre:<20} | {ingrediente.cantidad<10} | {ingrediente.unidad_medida}"
                    )

if __name__ == "__main__":
    MenuRestaurant.main()