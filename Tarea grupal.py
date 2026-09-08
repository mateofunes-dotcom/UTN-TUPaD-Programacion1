 #Ejercicio 1:
#Suma de Elementos 
#Escribe un programa que permita al usuario 
#ingresar una lista de números y calcule la suma de todos los elementos en la lista.

print("Ejercicio N°1")
numeros=[]
for i in range(7):
    nuum=int(input("ingrese un numero:"))
    numeros.append(nuum)
#print(numeros)
suma= sum(numeros)
print(f"la suma de los numeros son",suma)

#Ejercicio 2: Encontrar el Mayor y el Menor 
#Escribe un programa que pida al usuario una lista de números y encuentre el mayor y el menor de ellos. 
print("Ejercicio N°2")
menor_menor=[]
for i in range(5):
    nym=int(input("ingrese un numero:"))
    menor_menor.append(nym)
print(f"El numero mas alto es:",max(menor_menor))
print(f"El numero mas bajo es:",min(menor_menor))
#Ejercicio 3: Invertir una Lista 
#Escribe un programa que permita al usuario ingresar una lista y la invierta. 

print("Ejercicio N°3")
invertir=[]
for i in range(10):
    Numeros=int(input("Ingrese un numero: "))
    invertir.append(Numeros)
invertir.reverse() 
print(invertir)

#Ejercicio 4: Contar Elementos Pares e Impares 
#Escribe un programa que pida al usuario una lista de números 
# y cuente cuántos de ellos son pares y cuántos son impares. 

print("Ejercicio N°4")
numeros = []
pares = 0
impares = 0
for i in range(10):
    numero = int(input("Ingrese un numero: "))
    numeros.append(numero)
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print("Cantidad de numeros pares:", pares)
print("Cantidad de numeros impares:", impares)

#Ejercicio 5: Multiplicar Elementos por un Valor 
#Escribe un programa que multiplique cada elemento de una lista de números por un valor 
#ingresado por el usuario. 

print("Ejercicio N°5")
numeros = []
for i in range(5):
    numero = int(input("Ingrese un numero: "))
    numeros.append(numero)
multiplicador = int(input("Ingrese un valor para multiplicar: "))
for i in range(len(numeros)):
    numeros[i] = numeros[i] * multiplicador
print("La lista multiplicada es:", numeros)

#Ejercicio 6: Eliminar Duplicados 
# Escribe un programa que permita al usuario ingresar una lista de números 
# y elimine los elementos duplicados. Pista:  Utiliza la función set(). 

print("Ejercicio N°6")
duplicados=[]
for i in range(10):
    dupli=int(input("ingrese un numero: "))
    duplicados.append(dupli)
duple=set(duplicados)
print(f"Lista sin duplicados:",duple)

#Ejercicio 7: Promedio de una Lista 
# Escribe un programa que permita al usuario ingresar una lista de números y 
# calcule el promedio de los elementos. 

print("Ejercicio N°7")
numeros = []
for i in range(10):
    numero = int(input("Ingrese un numero: "))
    numeros.append(numero)
promedio=sum(numeros)/len(numeros)
print(f"El promedio es:",promedio)

#Ejercicio 8: Encontrar Elementos Repetidos 
# Escribe un programa que identifique y muestre los elementos que se repiten en una lista. 
# Pista:  Utiliza un diccionario o un conjunto (set) para hacer el seguimiento de los elementos. 

print("Ejercicio N°8")
repetidos = [2,2,1,6,7,8,6,9,0,7]
elementos_repetidos=set()
for i in repetidos:
    cantidad = repetidos.count(i)
    if cantidad > 1:
        elementos_repetidos.add(i)
print("Los elemetos que se repiten son:",elementos_repetidos)

#Ejercicio 9: Lista de Números Primos 
# Escribe un programa que permita al usuario ingresar una lista de números y 
# filtre los números primos. Pista:  Usa una función para verificar si un número es primo

print("Ejercicio N°9")
numeros_primos = []
for i in range(10):
    numero = int(input("Ingrese un numero: "))
    es_primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            es_primo = False
    if es_primo:
        numeros_primos.append(numero)
print("los numeros primos son:",numeros_primos)

#Ejercicio 10: Eliminar un Elemento por su Índice 
# Escribe un programa que permita al usuario ingresar una lista de números 
# y eliminar un elemento en un índice especificado. 

print("Ejercicio N°10")
num = []
for i in range(10):
    numero = int(input("Ingrese un numero: "))
    num.append(numero)
print("Su lista es:",num)
eliminar=int(input("ingrese el indice del numero que desee eliminar del 0 al 9:"))
del num[eliminar]
print("Su lista actualizada es:",num)

# Ejercicio 11: Contar Ocurrencias de un Elemento 
# Escribe un programa que permita al usuario ingresar una lista y un número,
#  y cuente cuántas veces aparece ese número en la lista. 

print("Ejercicio N°11")
numeros = []
for i in range(10):
    numero = int(input("Ingrese un numero: "))
    numeros.append(numero)
buscar = int(input("Ingrese el numero que desea buscar: "))
cantidad = numeros.count(buscar)
print("El numero", buscar, "aparece", cantidad, "veces")


# Ejercicio 12: Sumar Listas Elemento por Elemento
# Escribe un programa que sume dos listas de números elemento por elemento.
# Las listas deben tener la misma longitud. 

print("Ejercicio N°12")
lista1 = []
lista2 = []
for i in range(5):
    numero = int(input("Ingrese un numero para la lista 1: "))
    lista1.append(numero)
for i in range(5):
    numero = int(input("Ingrese un numero para la lista 2: "))
    lista2.append(numero)
resultado = []
for i in range(len(lista1)):
    resultado.append(lista1[i] + lista2[i])
print("La lista 1 es:", lista1)
print("La lista 2 es:", lista2)
print("El resultado de la suma es:", resultado)

# Ejercicio 13: Explique y ejemplifique la librería NumPy para trabajar con matrices y arrays 

# NumPy es una librería de Python que sirve principalmente para trabajar con números, arrays y matrices.
# para usarla podemos escrirlo asi:
# "import numpy as np"  el "as np" es para escribirle un nombre mas corto es como si fuera un alias.
"""print("Ejercicio N°13")
import numpy as np                #Este seria un ejemplo de como lo podemos usar en una matriz 
matriz = np.array([       
    [1, 2],
    [3, 4]
])
print(matriz)"""

"""import numpy as np         # Este seria un ejemplo con array
numeros = np.array([1, 2, 3, 4, 5])
print(numeros)
Resultado:
[1 2 3 4 5]"""


#Ejercicio 1: Crear una Matriz de Números Crea una función que reciba dos parámetros: el número de filas y columnas.
# La función debe generar una matriz de ese tamaño, donde los valores son números enteros consecutivos empezando desde 1. 

print("Ejercicio N°1")
def crear_matriz(filas, columnas):
    matriz = []
    numero = 1
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(numero)
            numero += 1
        matriz.append(fila)
    return matriz

filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))
matriz = crear_matriz(filas, columnas)
print(matriz)

#Ejercicio 2: Suma de Todos los Elementos 
# Escribe un programa que calcule la suma de todos los elementos en una lista bidimensional.
#  Pista: Aplique la función sum 

print("Ejercicio N°2")
matriz = [
    [1, 2, 9],
    [8, 5, 3]
]
suma = 0
for fila in matriz:
    suma += sum(fila)
print("La suma de todos los elementos es:", suma)

#Ejercicio 3: Suma de Cada Fila Modifica el programa anterior para que imprima la suma de cada fila de la lista bidimensional. 

print("Ejercicio N°3")
matriz = [
    [1, 2, 9],
    [8, 5, 3],
]
for i, fila in enumerate(matriz):
    print(f"Suma de la fila {i + 1}: {sum(fila)}")

#Ejercicio 4: Matriz Transpuesta Escribe un programa que calcule la transpuesta de una matriz. 
# La transpuesta de una matriz intercambia sus filas por columnas. 

print("Ejercicio N°4")
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]
transpuesta = []
for j in range(len(matriz[0])):
    fila = []
    for i in range(len(matriz)):
        fila.append(matriz[i][j])
    transpuesta.append(fila)
print("Matriz original:", matriz)
print("Matriz transpuesta:", transpuesta)

#Ejercicio 5: Encontrar el Elemento Mayor Escribe un programa que encuentre el valor más grande en una lista bidimensional. 

print("Ejercicio N°5")
matriz = [
    [4, 8, 2],
    [10, 37, 6],
    [7, 58, 96]
]
valor = matriz[0][0]
for fila in matriz:
    for numero in fila:
        if numero > valor:
            valor = numero
print("El valor mas grande es:", valor)

#Ejercicio 6: Multiplicar una Matriz por un Escalar 
# Escribe un programa que multiplique cada elemento de una lista bidimensional por un valor escalar dado por el usuario. 

print("Ejercicio N°6")
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]
escalar = int(input("Ingrese el valor escalar: "))
resultado = []
for fila in matriz:
    nueva_fila = []
    for numero in fila:
        nueva_fila.append(numero * escalar)
    resultado.append(nueva_fila)
print("Matriz original:", matriz)
print("Matriz multiplicada:", resultado)

#Ejercicio 7: Diagonal de una Matriz Cuadrada 
#Escribe un programa que extraiga los elementos de la diagonal principal de una matriz cuadrada. 

print("Ejercicio N°7")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
diagonal = []
for i in range(len(matriz)):
    diagonal.append(matriz[i][i])
print("La diagonal principal es:", diagonal)

#Ejercicio 8: Matriz Identidad Crea un programa que genere una matriz identidad de tamaño n. 
# Una matriz identidad es una matriz cuadrada donde los elementos de la diagonal principal son 1 y el resto son 0.
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1 

print("Ejercicio N°8")
n = int(input("Ingrese el tamaño de la matriz: "))
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)
for fila in matriz:
    print(fila)

#Ejercicio 9: Matriz Identidad Inversa 
# Crea un programa que genere una matriz identidad inversa de tamaño n.
#  Una matriz identidad inversa es una matriz cuadrada donde los elementos de la diagonal inversa principal son 1 y el resto son 0.
# 0 0 0 1
# 0 0 1 0 
# 0 1 0 0 
# 1 0 0 0 

print("Ejercicio N°9")
n = int(input("Ingrese el tamaño de la matriz: "))
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        if i + j == n - 1:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)
for fila in matriz:
    print(fila)

#Ejercicio 10: Verificar Matriz Simétrica Una matriz es simétrica si es igual a su transpuesta.
# Escribe un programa que verifique si una matriz es simétrica. 

print("Ejercicio N°10")
matriz = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]
es_simetrica = True
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j] != matriz[j][i]:
            es_simetrica = False
if es_simetrica:
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")

#Ejercicio 11: Rotar una Matriz 90 Grados 
# Escribe un programa que gire una lista bidimensional (matriz) 90 grados en el sentido de las agujas del reloj. 

print("Ejercicio N°11")
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]
rotada = []
for j in range(len(matriz[0])):
    fila = []
    for i in range(len(matriz) - 1, -1, -1):
        fila.append(matriz[i][j])
    rotada.append(fila)
print("Matriz original:")
for fila in matriz:
    print(fila)
print("Matriz a 90 grados:")
for fila in rotada:
    print(fila)


#Ejercicio 12: Analizador y Filtrado de Calificaciones 
#En una asignatura universitaria se ha registrado una cadena de texto con las notas finales obtenidas por las estudiantes en un examen, 
#separadas por comas (por ejemplo: "45, 88, -5, 92, 30, 110, 75, 60, 15").
# Debido a un error en el sistema de carga, se incluyeron algunas notas inválidas (menores a 0 o mayores a 100).
# Escribe un programa en Python que realice las siguientes tareas:
# 1. Convierta la cadena de notas en una lista utilizando el método .split().
# 2. Recorra la lista resultante mediante un bucle for.
# 3. Si encuentra una nota fuera del rango válido (0 <= nota <= 100), debe omitirla utilizando la palabra clave continue.
# 4. Clasifique las notas válidas en dos listas independientes utilizando .append():  o aprobados: notas iguales o superiores a 60.
#  o reprobados: notas inferiores a 60.
# 5. Muestre por consola: o La lista de aprobados y la de reprobados. 
# o El promedio total de las notas válidas. o Los últimos 2 aprobados registrados utilizando slicing. 

print("Ejercicio N°12")
notas_texto = "45, 88, -5, 92, 30, 110, 75, 60, 15"
notas = notas_texto.split(",")
aprobados = []
reprobados = []
suma = 0
cantidad = 0
for nota in notas:
    nota = int(nota)
    if nota < 0 or nota > 100:
        continue
    suma += nota
    cantidad += 1
    if nota >= 60:
        aprobados.append(nota)
    else:
        reprobados.append(nota)
promedio = suma / cantidad
print("Aprobados:", aprobados)
print("Reprobados:", reprobados)
print("Promedio de notas válidas:", promedio)
print("Últimos 2 aprobados:", aprobados[-2:])

#Ejercicio 13: Gestor Interactivo de Proyectos con while y Operador in 
# Un equipo de desarrollo universitario necesita un sistema en consola para administrar los nombres de las tareas o proyectos activos. 
# Escribe un programa interactivo en Python que mantenga una lista de tareas (tareas = [])
#  e incluya un menú ejecutado dentro de un bucle while con las siguientes opciones:  
# Agregar tarea: Pide el nombre de una tarea. Si la tarea ya existe en la lista (verificando con el operador in), 
# muestra un mensaje indicando que ya está registrada. Si no existe, agrégala con .append().  

tareas = []

while True:
    print("1. Agregar tarea")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        tarea = input("Ingrese una tarea: ")
        if tarea in tareas:
            print("La tarea ya está registrada.")
        else:
            tareas.append(tarea)
            print("Tarea agregada correctamente.")
    elif opcion == "2":
        break
print("Las tareas agregadas son:",tareas)
