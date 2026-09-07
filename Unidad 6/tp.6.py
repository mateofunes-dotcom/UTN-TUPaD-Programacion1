#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

print("Ejercicio N°1")
def imprimir_hola_mundo():
     print("Hola mundo")
imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
#volver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

print("Ejercicio N°2")
def  saludar_usuario(nombre):
     print("hola",nombre)
    
nombre=input("ingrese su nombre: ")
saludar_usuario(nombre)

#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
#dir los datos al usuario y llamar a esta función con los valores in
#gresados.

print("Ejercicio N°3")
def informacion_personal(nombre, apellido,
edad, residencia):
   print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
    
nombre=input("ingrese su nombre: ")
apellido=input("ingrese su apellido: ")
edad=int(input("ingrese su edad: "))
residencia=input("ingrese su residencia: ")
informacion_personal(nombre,apellido,edad,residencia)

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
#dio como parámetro y devuelva el área del círculo. calcular_peri
#metro_circulo(radio) que reciba el radio como parámetro y devuel
#va el perímetro del círculo. Solicitar el radio al usuario y llamar am
#bas funciones para mostrar los resultados.

print("Ejercicio N°4")
def calcular_area_circulo(radio):
    area= 3.14 * (radio ** 2)
    return area
def calcular_perimetro_circulo(radio):
    perimetro=  2 * 3.14 * radio
    return perimetro
radio= float(input("ingrese el radio: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print("El area del circulo es:", area)
print("El perímetro del circulo es:", perimetro)

#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mos
#trar el resultado usando esta función.

print("Ejercicio N°5")
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

segundos = int(input("Ingrese una cantidad de segundos: "))
horas=segundos_a_horas(segundos)
print("La cantidad de horas son",horas)

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la fun
#ción.

print("Ejercicio N°6")
def tabla_multiplicar(numero):
    print(numero, "x 1 =", numero * 1)
    print(numero, "x 2 =", numero * 2)
    print(numero, "x 3 =", numero * 3)
    print(numero, "x 4 =", numero * 4)
    print(numero, "x 5 =", numero * 5)
    print(numero, "x 6 =", numero * 6)
    print(numero, "x 7 =", numero* 7)
    print(numero, "x 8 =", numero * 8)
    print(numero, "x 9 =", numero * 9)
    print(numero, "x 10 =", numero * 10)

numero=int(input("ingrese un numero del 1 al 10: "))
tabla_multiplicar(numero)


#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resulta
#do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
#sultados de forma clara.


print("Ejercicio N°7")
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b

    return suma, resta, multiplicacion, division

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(a, b)

print("La suma es:", resultados[0])
print("La resta es:", resultados[1])
print("La multiplicación es:", resultados[2])
print("La división es:", resultados[3])

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
#ción para mostrar el resultado con dos decimales.

print("Ejercicio N°8")
def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
resultado = calcular_imc(peso, altura)
print(f"Su IMC es de:, {resultado:.2f}")


#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

print("Ejercicio N°9")
def celsius_a_fahrenheit(celsius):
   tempfahrenheit = 9/5 * celsius + 32
   return tempfahrenheit

celsius = float(input("Ingresela temperatura en grados celsius: "))
tempfahrenheit=celsius_a_fahrenheit(celsius)
print("La su temperatura en fahrenheit es:",tempfahrenheit)

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función

print("Ejercicio N°10")
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

a = float(input("ingrese el primer número: "))
b = float(input("ingrese el segundo número: "))
c = float(input("ingrese el tercer número: "))
resultado = calcular_promedio(a, b, c)
print("El promedio es:", resultado)
