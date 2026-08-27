#Ejercicio 1: Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 
print("Ejercicio N°1")
for i in range(0,101):
    print(i)        

    
#Ejercicio 2: Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene. 

print("Ejercicio N°2")
num= int(input("Ingrese un numero entero: "))
if num == 0:
    cantidad_digitos = 1
else:
    cantidad_digitos = 0

    while num > 0:
        num = num // 10
        cantidad_digitos += 1
print("La cantidad de dígitos es:", cantidad_digitos)

#Ejercicio 3: Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores. 

print("Ejercicio N°3")
num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
suma = 0
for i in range(num1 + 1, num2):
    suma += i
print("La suma es:",suma)

#Ejercicio 4: Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0. 

print("Ejercicio N°4")
num = int(input("Ingrese un numero entero: "))
suma_total = 0
while num != 0:
    suma_total += num
    num = int(input("Ingrese un numero entero o ingrese 0 si desea terminar: "))
#Aca quiero especificar lo del 0 para que el usuario lo termine, ya que no se si sabe como terminarlo.
print("La suma total es:",suma_total)

#Ejercicio 5: Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

print("Ejercicio N°5")
import random
numero_secreto = random.randint(0, 9)
num = int(input("Adivine el numero del 0 al 9: "))
intentos = 1
while num != numero_secreto:
    num = int(input("Incorrecto. Intente nuevamente: "))
    intentos += 1
print("Corecto el numero era:",numero_secreto)
#Pongo el numero que era por si el usuario no se acuerda.(Capaz se ve medio feo pero bueno)
print("Cantidad de intentos:",intentos)

#Ejercicio 6: Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente. 

print("Ejercicio N°6")
i= 0
for i in range(100, -1, -1):
    if i % 2 == 0:
     print(i)

#Ejercicio 7: Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario. 

print("Ejercicio N°7")
num = int(input("ingrese un numero entero positivo: "))
suma = 0
for i in range(num + 1):
    suma += i
print("La suma es:", suma)

#Ejercicio 8: Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

print("Ejercicio N°8")
num_pares = 0
num_impares = 0
num_positivos = 0
num_negativos = 0

for i in range(5):#Aca lo puede modificar y probarlo.
    num = int(input("ingrese un numero: "))
    if num % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1
    if num > 0:
        num_positivos += 1
    elif num < 0:
        num_negativos += 1
print("La cantidad de numeros pares son:", num_pares)
print("La cantidad de numeros impares son:", num_impares)
print("La cantidad de numeros positivos son:", num_positivos)
print("La cantidad de numeros negativos son:", num_negativos)

#Ejercicio 9: Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor). 

print("Ejercicio N°9")
cantidad =100
#pongo cantidad para que la puedas modificar desde aca.
suma = 0
for i in range(cantidad):
    num = int(input("ingrese un numero: "))
    suma += num
media = suma // cantidad
#tambien pongo el "//" para que sea solo de enteros.
print("La media es:", media)

#Ejercicio 10: Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 

print("Ejercicio N°10")
num = int(input("ingrese un numero: "))
invertido = 0
while num > 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num = num // 10
print("numero invertido:", invertido)
