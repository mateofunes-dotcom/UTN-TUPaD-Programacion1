import os
from validaciones import (
    validar_solo_letras,
    validar_legajo,
    validar_nota,
    validar_existe_alumno
)

"""Trabajo Práctico: Lectura y Escritura de Archivos en Python"""

#Desarrollar un programa en Python que gestione un registro de alumnos y sus notas

ARCHIVO_ALUMNOS = "alumnos.txt"
ARCHIVO_APROBADOS = "aprobados.txt"

def crear_archivo_si_no_existe():
    archivo = open(ARCHIVO_ALUMNOS, "a")  # "a" crea el archivo si no existe
    archivo.close()

def leer_alumnos():
    """
    Lee alumnos.txt y devuelve:
      - lista_alumnos: lista de diccionarios
      - diccionario_legajos: {legajo: diccionario_alumno}
    """
    lista_alumnos = []
    diccionario_legajos = {}

    archivo = open(ARCHIVO_ALUMNOS, "r")
    lineas = archivo.readlines()
    archivo.close()

    for linea in lineas:
        linea = linea.strip()
        if linea == "":
            continue
        partes = linea.split(";")
        if len(partes) != 4:
            continue

        nombre = partes[0]
        apellido = partes[1]
        legajo = partes[2]
        nota = float(partes[3])

        alumno = {
            "nombre": nombre,
            "apellido": apellido,
            "legajo": legajo,
            "nota": nota
        }
        lista_alumnos.append(alumno)
        diccionario_legajos[legajo] = alumno

    return lista_alumnos, diccionario_legajos

def mostrar_alumnos(lista_alumnos):
    """Muestra por pantalla todos los alumnos con su nota."""
    if len(lista_alumnos) == 0:
        print("No hay alumnos registrados.")
        return

    print("\n--- Lista de Alumnos ---")
    for a in lista_alumnos:
        print(a["nombre"], a["apellido"], "- Legajo:", a["legajo"], "- Nota:", a["nota"])

def agregar_alumno(lista_alumnos, diccionario_legajos):
    """Pide datos, valida y agrega el alumno al archivo y al diccionario."""
    print("\n--- Agregar Nuevo Alumno ---")

    # Nombre
    nombre = input("Nombre: ").strip()
    while not validar_solo_letras(nombre):
        print("Error: el nombre solo debe contener letras.")
        nombre = input("Nombre: ").strip()

    # Apellido
    apellido = input("Apellido: ").strip()
    while not validar_solo_letras(apellido):
        print("Error: el apellido solo debe contener letras.")
        apellido = input("Apellido: ").strip()

    # Legajo
    legajo = input("Legajo (5 dígitos): ").strip()
    while not validar_legajo(legajo):
        print("Error: el legajo debe tener exactamente 5 dígitos.")
        legajo = input("Legajo (5 dígitos): ").strip()

    # Validar que no exista
    if validar_existe_alumno(legajo, diccionario_legajos):
        print("El legajo", legajo, "ya existe en el archivo alumnos.txt, no se permite su escritura")
        return

    # Nota
    nota_str = input("Nota promedio (1-10): ").strip()
    while not validar_nota(nota_str):
        print("Error: la nota debe ser un número entre 1 y 10.")
        nota_str = input("Nota promedio (1-10): ").strip()
    nota = float(nota_str)

    # Crear diccionario del alumno
    nuevo_alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "legajo": legajo,
        "nota": nota
    }

    # Escribir en el archivo (modo append)
    archivo = open(ARCHIVO_ALUMNOS, "a")
    archivo.write(nombre + ";" + apellido + ";" + legajo + ";" + str(nota) + "\n")
    archivo.close()

    # Actualizar lista y diccionario en memoria
    lista_alumnos.append(nuevo_alumno)
    diccionario_legajos[legajo] = nuevo_alumno

    print("Alumno agregado correctamente.")

def guardar_aprobados(lista_alumnos):
    """Genera aprobados.txt con alumnos con nota >= 6 y lo muestra."""
    aprobados = []
    for a in lista_alumnos:
        if a["nota"] >= 6:
            aprobados.append(a)

    archivo = open(ARCHIVO_APROBADOS, "w")
    for a in aprobados:
        archivo.write(a["nombre"] + ";" + a["apellido"] + ";" + a["legajo"] + ";" + str(a["nota"]) + "\n")
    archivo.close()

    print("\n--- Contenido de aprobados.txt ---")
    if len(aprobados) == 0:
        print("No hay alumnos aprobados.")
    else:
        for a in aprobados:
            print(a["nombre"], a["apellido"], "- Legajo:", a["legajo"], "- Nota:", a["nota"])




def menu():
    """Menú principal."""
    crear_archivo_si_no_existe()
    lista_alumnos, diccionario_legajos = leer_alumnos()

    opcion = ""
    while opcion != "4":
        print("\n===== MENÚ =====")
        print("1. Ver alumnos")
        print("2. Agregar alumno")
        print("3. Generar y mostrar archivo de aprobados")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_alumnos(lista_alumnos)
        elif opcion == "2":
            agregar_alumno(lista_alumnos, diccionario_legajos)
        elif opcion == "3":
            guardar_aprobados(lista_alumnos)
        elif opcion == "4":
            print("Saliendo del programa...")
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()