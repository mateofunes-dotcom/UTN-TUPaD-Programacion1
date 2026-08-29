#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función 
#range. 

print("Ejercicio N°1")
multiplos_de_4 = []
for i in range(1,101):
    if i % 4 == 0:
        multiplos_de_4.append(i)
print (multiplos_de_4) 

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el 
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el 
#indexing con números negativos! 

print("Ejercicio N°2")
elementos = ["mateo",2,4,"manzana",45]
print(elementos[-2])

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por 
#pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por 
#ejemplo: 
#lista_vacia = [] 

print("Ejercicio N°3")
palabras = []
for i in range(3):
    le = input("escribi una palabra: ")
    palabras.append(le)
print(palabras)

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
#respectivamente.  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra 
#en los videos o bien investigar cómo funciona el indexing con números negativos! 
#animales = ["perro", "gato", "conejo", "pez"] 
print("Ejercicio N°4")
animales = ["perro", "gato", "conejo", "pez"] 
animales[1]=  "loro"
animales[-1]= "oso"
print(animales)

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

print("Ejercicio N°5")
numeros =[8,15,3,22,7]
numeros.remove(max(numeros))
print("con en .remove sacamos un numeros especifico y con la funcion (max(numeros) estamos revisando el numero mas alto de la " \
"lista en este caso seria el 22 para eliminarlo con el remove, la lista quedarias asi")
print(numeros)

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
#pantalla los dos primeros. 

print("Ejercicio N°6")
numeros=[]
for i in range(10,35,5):
    numeros.append(i)
print(numeros[0:2])

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores 
#cualesquiera. 

print("Ejercicio N°7")
autos = ["sedan", "polo", "suran", "gol"] 
autos[1]= "bora"
autos[2] = "neon"
print(autos)

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append 
#directamente. Imprimir la lista resultante por pantalla. 

print("Ejercicio N°8")
dobles=[]
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por 
#diferentes clientes: 
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], 
#["agua"]] 
#a) Agregar "jugo" a la lista del tercer cliente usando append. 
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
#c) Eliminar "pan" de la lista del primer cliente.  
#d) Imprimir la lista resultante por pantalla 

print("Ejercicio N°9")

compras = [["pan", "leche"],["arroz", "fideos", "salsa"], ["agua"]] 
compras[2].append("jugo")
compras[1][1]= "tallarines"
compras[0].remove("pan")
print(compras)

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
#● Posición lista_anidada[0]: 15 
#● Posición lista_anidada[1]: True 
#● Posición lista_anidada[2][0]: 25.5 
#● Posición lista_anidada[2][1]: 57.9 
#● Posición lista_anidada[2][2]: 30.6 
#● Posición lista_anidada[3]: False 
#Imprimir la lista resultante por pantalla.

print("Ejercicio N°10")

lista_anidada=[]
lista_anidada.append(15)
lista_anidada.append(True)
lista_anidada.append([25.5,57.9,30.6])
lista_anidada.append(False)
print(lista_anidada)
