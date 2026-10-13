import tpPoo_instancias

#1. Codifique la clase Celda con los atributos.

mi_matriz = Matriz()

print("Ingrese los datos de la celda (escriba 'FIN' en el valor para terminar).")

while True:

    valor_input = input("Ingrese el valor (o FIN para salir): ")

    #Condición de salida.
    if valor_input.upper() == "FIN":
        break

    #Validación de fila para enteros.
    fila_str = input("Ingrese la fila (entero): ")
    if not fila_str.isdigit():
        print("Error: Debes darme un número entero en fila.")
        continue
    fila_input = int(fila_str)

    #Validación de columna para enteros.
    columna_str = input("Ingrese la columna (entero): ")
    if not columna_str.isdigit():
        print("Error: Debes darme un número entero en columna.")
        continue
    columna_input = int(columna_str)

    #Valida que la celda creada ya no exista anteriormente
    celda_existente = mi_matriz.buscar_celda(fila_input, columna_input)
    if celda_existente is not None:
        print(f"La fila {fila_input} y columna {columna_input} ya fueron cargadas en el sistema.")
        continue

    #Crea una instancia de la clase Celda y asigna los valores
    nueva_celda = Celda(fila_input, columna_input, valor_input)

    #Agregamos la instancia a la lista celdasMatriz
    mi_matriz.celdasMatriz.append(nueva_celda)
    print("Celda agregada exitosamente.")

print("\n--- Valores cargados en la lista celdasMatriz ---")
if not mi_matriz.celdasMatriz:
    print("No hay celdas cargadas.")
else:
    for celda in mi_matriz.celdasMatriz:
        print(
            f"Fila: {celda.fila} | Columna: {celda.columna} | Valor: {celda.valor}"
        )

# --- Ejemplo de consulta con el método ---
print("\n--- Consultar una celda ---")
f_busq = int(input("Ingrese fila a consultar: "))
c_busq = int(input("Ingrese columna a consultar: "))
print(mi_matriz.obtener_valor(f_busq, c_busq))

#2. Codifique las siguientes clases Python en archivos separados.


class CargaNotas:

    @staticmethod
    def main():
        #Variable que contiene la lista alumno
        alumnos = []

        while True:
            print("\n---- Ingrese datos del Alumno ----")
            nombreCompleto = input("Ingrese el nombre completo del alumno.")

            #Validamos legajo
            legajo_int = input("Ingrese el legajo (entero): ")
            if not legajo_int.isdigit():
                print("ERROR! Debe ser numérico.")
                continue
            legajo = int(legajo_int)

            #Se instancia la clase Alumno
            nuevo_alumno = Alumno(nombreCompleto, legajo)

            while True:
                print ("\n---- Carga de Notas ----")
                catedra = input("Ingrese el nombre de la cátedra: ")

                #Validación de nota
                nota_decimal = input("Ingrese la nota del exámen: ")
                validaNota = nota_decimal.replace(".", "", 1).isdigit()
                if not validaNota:
                    print("ERROR! Ingresá un valor decimal válido.")
                    continue
                nota_examen = float(nota_decimal)

                nueva_nota = Nota(catedra, nota_examen)
                nuevo_alumno.notas.append(nueva_nota)


                #Preguntar si desea salir
                salir_notas = input("¿Deseas salir de la pestaña ---Cargar Notas--- (S/N): ").upper()
                if salir_notas == "S":
                    break

            #Validacion para que el alumno tenga al menos una nota
            if len(nuevo_alumno.notas) == 0:
                print("ERROR! El alumno debe tener al menos una nota cargada.")
                continue

            #Cargar alumno a la lista alumnos
            alumnos.append(nuevo_alumno)

            salir_alumno = input("¿Deseas salir de la pestaña ---Carga Alumnos--- (S/N): ").upper()
            if salir_alumno == "S":
                break

        for alumno in alumnos:
            print(f"\n Datos Alumno: {alumno.nombreCompleto}")
            print(f"Legajo: {alumno.legajo}")
            print("Notas:")
            for notas in alumno.notas:
                print(f"Catedra: {notas.catedra} | Notaa: {notas.nota_examen}")

            promedio = alumno.calcular_promedio()
            print(f"El promedio del alumno es {promedio:.2f}")

if __name__ == "__main__":
    CargaNotas.main()

