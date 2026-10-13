from componentecpu import ComponenteCPU
from computadora import Computadora

class CostoComputadora:

    @staticmethod
    def main():

        while True:

            print("\n-----------------------")
            print("      COTIZADOR DE PC    ")
            print("\n-----------------------")

            marca_pc = input("Ingrese la marca de la Computadora: ")
            modelo_pc = input("Ingrese el modelo de la Computadora: ")

            #Se instancia la PC
            nueva_pc = Computadora(marca_pc, modelo_pc)
    
            while True: #se carga los componentes
                
                print("\n --- Carga de Componentes de PC ---")
                nombre_componente = input("Componentes a seleccionar: (ej. Memoria RAM, Disco HDD/SSD). ")
                marca_componente = input("Ingrese la marca del componente: ")
                
                numero_componentes = (input("¿cuantos componentes tiene la computadora?: "))
                if not numero_componentes.isdigit():
                    print("ERROR! La cantidad debe ser en números.")
                    continue
                cantidad = int(numero_componentes)

                precio_str = input("Precio por unidad: ")
                if not precio_str.replace(".", "", 1).isdigit():
                    print("ERROR! La cantidad debe tener un valor númerico.")
                    continue
                precio = float(precio_str)

                #Se instancia los componentes listados arriba
                nuevo_componente = ComponenteCPU(nombre_componente, marca_componente, cantidad, precio)
                nueva_pc.componentes.append(nuevo_componente)

                salir_componentes = (
                    input("¿Deseas salir de la pestaña de CARGA DE COMPONENTES? (S/N): ").strip().upper()
                )

                if salir_componentes == "SI" or salir_componentes == "S":
                    break
                
            if len(nueva_pc.componentes) == 0:
                print(
                    "ERROR! La computadora debe tener al menos un componente cargado"
                )
                continue

        #Información

            print(f"\nComputadora")
            print(f"Marca: {nueva_pc.marca}")
            print(f"Modelo: {nueva_pc.modelo}")
            print("COMPONENTES")
            print(
                f"{'Componente':<20} | {'Marca':<12} | {'Cantidad':<8} | {'Precio X Unidad':<15} | {'Subtotal'}"
            )
            print("-" * 75)

            costo_total = 0
            for c in nueva_pc.componentes:
                subtotal = c.precio * c.cantidad
                costo_total += subtotal
                print(
                    f"{c.componente:<20} | {c.marca:<12} | {c.cantidad:<8} | {c.precio:<15} | {subtotal}"
                )

            print("-" * 75)
            print(f"{' ' * 52} Costo Total | {costo_total}")

            if costo_total < 50000:
                porcentaje = costo_total * 0.40
                precio_sugerido = costo_total + porcentaje
                print(
                f"El precio sugerido de venta es {costo_total} + {porcentaje} (40%) = {precio_sugerido}"
                )
            else:
                porcentaje = costo_total * 0.30
                precio_sugerido = costo_total + porcentaje
                print(
                f"El precio sugerido de venta es {costo_total} + {porcentaje} (30%) = {precio_sugerido}"
                )

            repetir = (
                input("\n¿Desea cotizar una nueva computadora? (S/N): ").strip().upper()
            )
            if repetir != "SI":
                print(
                "Finalizando la ejecución del programa."
            )
            break

if __name__ == "__main__":
    CostoComputadora.main()