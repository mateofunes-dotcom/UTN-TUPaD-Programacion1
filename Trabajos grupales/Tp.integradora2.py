# Diccionario Alumnos
alumnos = {
    60902: "Rodolfo Fernandez",
    61654: "Luis Gomez",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales"
}
#Lista Materia 2 dimensiones
materias = [
    ["Ciencias", 0, 0, 0],
    ["Historia", 0, 0, 0],
    ["Geografia", 0, 0, 0],
    ["Matematicas", 0, 0, 0],
    ["Fisica", 0, 0, 0]
]
#Lista Notas Finales
notasFinales = [
    ["Rodolfo Fernandez", 0],
    ["Luis Gomez", 0],
    ["Andrea Pereira", 0],
    ["Juan Cruz Gonzales", 0]
]
# =======================
# Validaciones Actividad B
# =======================

def validar_nota(mensaje):
    nota = input(mensaje)
    while not nota.isdigit() or int(nota) < 0 or int(nota) > 10:
        print("Error: la nota debe ser un número entre 0 y 10.")
        nota = input(mensaje)
    return int(nota)

def cargar_notas_alumno(nombre):
    for materia in materias:
        print(f"\nIngrese las notas para la materia {materia[0]}")
        nota1 = validar_nota("Nota 1: ")
        nota2 = validar_nota("Nota 2: ")

        nota_final = (nota1 + nota2) / 2

        materia[1] = nota1
        materia[2] = nota2
        materia[3] = nota_final

        print(f"Nota Final: {nota_final}")

def mostrar_materias():
    print("\n===== LISTA DE MATERIAS =====")
    print(f"{'Materia':<15}{'Nota 1':<10}{'Nota 2':<10}{'Nota Final':<10}")
    print("-" * 45)
    for materia in materias:
        print(f"{materia[0]:<15}{materia[1]:<10}{materia[2]:<10}{materia[3]:<10}")

def materia_mas_alta(nombre_alumno):
    mejor = materias[0]
    for materia in materias:
        if materia[3] > mejor[3]:
            mejor = materia
    print(f"\nLa materia con la calificación más alta de {nombre_alumno} " f"es {mejor[0]} con {mejor[3]}")

def calcular_promedio_general():
    contador = 0
    for legajo, nombre in alumnos.items():
        suma = 0
        for materia in materias:
            suma += materia[3]
        promedio = suma / len(materias)
        
        notasFinales[contador][0] = nombre
        notasFinales[contador][1] = promedio
        
        contador += 1
    return notasFinales

def mostrar_mejor_promedio():
    mejor = notasFinales[0]
    for alumno in notasFinales:
        if alumno[1] > mejor[1]:
            mejor = alumno
    print(f"\n===== MEJOR PROMEDIO =====")
    print(f"El alumno con el mejor promedio es {mejor[0]} con {mejor[1]:.2f}")


##############Ejercicio############
"""Un instituto necesita un programa para gestionar las notas de sus estudiantes. El
programa debe permitir almacenar las calificaciones de cada estudiante en
distintas asignaturas, realizar cálculos estadísticos y validar los datos ingresados.
Para resolver el programa deberá respetar los siguientes lineamientos

1- Cree un Diccionario de alumnos que contiene como clave el Legajo del
alumno y como valor su apellido y nombre.

60902 Rodolfo Fernandez
61654 Luis Gomez
61852 Andrea Pereira
61754 Juan Cruz Gonzales

2- Cree una lista de materias de 2 dimensiones de con la siguiente estructura:
Ciencias
Historia
Geografia
Matematicas
Fisica

Las columnas se corresponden con Materia, Nota 1, Nota 2, Nota Final (que será el
promedio de (Nota 1 + Nota 2) / 2).

3- Cree una lista notasFinales con la siguiente estructura:
Rodolfo Fernandez
Luis Gomez
Andrea Pereira
Juan Cruz Gonzales

Las columnas se corresponden con el nombre del alumno, y la segunda columna
con el promedio general del alumno que será calculado.
Codifique en el archivo los métodos necesarios para ejecutar las siguientes
acciones:
Iterar el diccionario de alumnos.
* Para cada alumno se deberá recorrer la lista de materias y solicitar el ingreso
de 2 notas que serán asignadas en la segunda y tercer columna de cada
materia, la tercera columna será el promedio de las 2 notas anteriores. Valide
que las notas ingresadas se encuentren en el rango de 0 a 10.
Ejemplo:
Alumno Rodolfo Fernandez
Ingrese las notas para la materia Ciencias
Nota 1
7
Nota 2
8
Nota Final 7.5
…..este proceso se repetirá para cada materia………
* Mostrar por pantalla la lista materias completa cargada
* Determinar la materia con la calificación más alta para el alumno y mostrarla
por pantalla
* Al finalizar la carga de todas las notas se deberá calcular el promedio general
del alumno, el cual será el promedio de las notas finales calculadas
anteriormente (tercera columna). El nombre y apellido del alumno y el
promedio general del alumno deberán ser asignados en la lista de notasFinales
* Repetir el proceso para el siguiente alumno
* Terminado el proceso para todos los alumnos determinar cuál de todos los
alumnos analizados posee el mejor promedio y mostrarlo por pantalla."""

def main():
    for legajo, nombre in alumnos.items():
        print(f"\n{'='*50}")
        print(f"Alumno: {nombre}")
        print(f"{'='*50}")

        # Cargar notas de todas las materias
        cargar_notas_alumno(nombre)

        # Mostrar materias del alumno
        mostrar_materias()

        # Materia con calificación más alta
        materia_mas_alta(nombre)

        # Calcular y guardar promedio
        calcular_promedio_general()

        # Mostrar promedio del alumno actual
        for alumno in notasFinales:
            if alumno[0] == nombre:
                print(f"\nPromedio general de {nombre}: {alumno[1]:.2f}")
                break

    # Mostrar todos los promedios finales
    print("\n===== PROMEDIOS FINALES =====")
    for alumno in notasFinales:
        print(f"{alumno[0]}: {alumno[1]:.2f}")

    # Mostrar el mejor promedio
    mostrar_mejor_promedio()

main()