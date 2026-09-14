#1) Dado el diccionario precios_frutas 
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
#1450} 
#Añadir las siguientes frutas con sus respectivos precios: 
#● Naranja = 1200 
#● Manzana = 1500 
#● Pera = 2300 

print ("Ejercicio N°1")
#Diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450}
#Añadir frutas 
precios_frutas["Naranja"]= 1200
precios_frutas["Manzana"]= 1500
precios_frutas["Pera"]= 2300

print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
#● Banana = 1330 
#● Manzana = 1700 
#● Melón = 2800

print ("Ejercicio N°2")
# Actualizar precio 
precios_frutas["Banana"]= 1330
precios_frutas["Manzana"]= 1700
precios_frutas["Melón"]= 2800
#Precios actualizados
print(f"La lista actualizada es: {precios_frutas}")

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
#precios.

print ("Ejercicio N°3")
#Lista nueva
frutas = []
#agregar las frutas
for fruta in precios_frutas:
    frutas.append(fruta)

print(frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos. 
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
#• Luego, pedí un nombre y mostrale el número asociado, si existe. 

print ("Ejercicio N°4")
almacenar_numeros={}
#Agregar nombres y numeros
for i in range(5):
    nombre = input("Ingrese el nombre: ")
    numero = input("Ingrese el numero: ")
    almacenar_numeros[nombre]=numero
#Mostrar numero asociado
buscar_nombre=input("ingrese el nombre a buscar: ")
if buscar_nombre in almacenar_numeros:
    print(almacenar_numeros[buscar_nombre])
else:
    print("El contacto no existe")   


#5) Solicita al usuario una frase e imprime: 
#• Las palabras únicas (usando un set). 
#• Un diccionario con la cantidad de veces que aparece cada palabra. 

print ("Ejercicio N°5")
#Pedir frase
frase= input("Igrese una frase: ")
#Separar frase 
palabras = frase.split()
#Palabras unicas
set(palabras)
#Diccionario
repetidos = {}
#Agregar palabras repetidas
for palabra in palabras:
    if palabra in repetidos:
        repetidos[palabra] = repetidos[palabra] + 1
    else:
        repetidos[palabra] = 1

print(f"Cantidad de veces que aparece cada palabra son: {repetidos}")

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
#Luego, mostrá el promedio de cada alumno.

print("Ejercicio N°6")
#Diccionario
alumnos = {}
#pedir alumno y sus notas
for i in range(3):
    nombre_alumno = input("Ingrese el nombre del alumno: ")

    nota1 = int(input("Ingrese la primera nota: "))
    nota2 = int(input("Ingrese la segunda nota: "))
    nota3 = int(input("Ingrese la tercera nota: "))
    #convertir las nota en una tupla
    notas = (nota1, nota2, nota3)
    #guardamos el nombre y la notas
    alumnos[nombre_alumno] = notas

for clave, valor in alumnos.items():
    promedio = sum(valor) / 3
    print(f"El alumno {clave} tuvo un promedio de {promedio}")



#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
#y Parcial 2: 
#• Mostrá los que aprobaron ambos parciales. 
#• Mostrá los que aprobaron solo uno de los dos. 
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

print("Ejercicio N°7")

parcial1 = {1, 2, 3, 4, 5}
parcial2 = {3, 4, 5, 6, 7}

# Aprobaron ambos parciales
ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

# Aprobaron solo uno de los dos
solo_uno = (parcial1 - parcial2) | (parcial2 - parcial1)
print("Aprobaron solo uno:", solo_uno)

# Aprobaron al menos un parcial
al_menos_uno = parcial1 | parcial2 
print("Aprobaron al menos un parcial:", al_menos_uno)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#Permití al usuario: 
#• Consultar el stock de un producto ingresado. 
#• Agregar unidades al stock si el producto ya existe. 
#• Agregar un nuevo producto si no existe.

print("Ejercicio N°8")
#Diccionario
stock_productos = {}

while True:
  # nombre de producto
    producto = input("Ingrese el nombre del producto: ")
  #agregar stock
    if producto in stock_productos:
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        stock_productos[producto] = stock_productos[producto] + cantidad
    else:  #agregar nuevo producto
        cantidad = int(input("Ingrese la cantidad de unidades: "))
        stock_productos[producto] = cantidad
    #consultar producto
    consulta = input("Ingrese el producto a consultar: ")

    if consulta in stock_productos:
        print(f"El stock de {consulta} es: {stock_productos[consulta]}")
    else:
        print("El producto no existe")

    continuar = input("¿Desea continuar? (si/no): ")
   #salida del bucle
    if continuar == "no":
        break

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
#Permití consultar qué actividad hay en cierto día y hora. 

print("Ejercicio N°9")
agenda = {}
#Pedimos dia, hora, actividad
dia = input("Ingrese el día: ")
hora = input("Ingrese la hora: ")
actividad = input("Ingrese la actividad: ")
#Convertimos dia y hora en una sola tupla
dia_hora = (dia, hora)
#y agregamos la tupla mas la actividad en diccionario
agenda[dia_hora] = actividad
#cosultamos dia y hora
dia_consulta = input("Ingrese el día a consultar: ")
hora_consulta = input("Ingrese la hora a consultar: ")
#Convertimos en tupla
dia_hora_consulta = (dia_consulta, hora_consulta)
# comparamos si esta en el diccionario
if dia_hora_consulta in agenda:
    print(f"La actividad es: {agenda[dia_hora_consulta]}")
else:
    print("No hay ninguna actividad en ese día y hora.")



#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
#diccionario donde: 
#• Las capitales sean las claves. 
#• Los países sean los valores. 


print("Ejercicio N°10")
#Diccionario 
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia"
}
#Diccionario
invertido = {}
#invertimos las capitales por claves y los paises por valores 
for pais, capital in original.items():
    invertido[capital] = pais

print(invertido)