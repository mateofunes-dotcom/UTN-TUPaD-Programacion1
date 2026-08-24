#Ejercicio 1: crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  
print("Ejercicio N°1")
print("Hola mundo")
#Ejercicio 2: Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
#realizar la impresión por pantalla. 
print("Ejercicio N°2")
nombre = input("ingrese un nombre")
print(f"hola",nombre)
#Ejercicio 3: Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
#la impresión por pantalla.
print("Ejercicio N°3")
nombre = input("ingrese su nombre ")
apellido = input("ingrese su apellido ")
edad = input("ingrese su edad ")
residencia = input("ingrese su residencia ")
print(f"Soy",nombre, apellido, "tengo",edad, "y vivo en",residencia)
#Ejercicio 4:  Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
#su perímetro. 
print("Ejercicio N°4")
pi= 3.14
radio= float(input ("ingrese el radio del circulo "))
area = 3.14 * (radio ** 2)
perimetro = 2 * 3.14 * radio
print("El area del circulo es",area)
print("El perimetro del circulo es",perimetro)
#Ejercicio 5:  Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
#cuántas horas equivale. 
print("Ejercicio N°5")
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print("La cantidad de horas es:", horas)
#Ejercicio 6:  Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
#multiplicar de dicho número.  
print("Ejercicio N°6")
num = int(input("ingrese un numero "))
print(num, "x 1 =", num * 1)
print(num, "x 2 =", num * 2)
print(num, "x 3 =", num * 3)
print(num, "x 4 =", num * 4)
print(num, "x 5 =", num * 5)
print(num, "x 6 =", num * 6)
print(num, "x 7 =", num* 7)
print(num, "x 8 =", num * 8)
print(num, "x 9 =", num * 9)
print(num, "x 10 =", num * 10)
#Ejercicio 7:  Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 
print("Ejercicio N°7")
num1 = int(input("ingrese un numero "))
num2 = int(input("ingrese un numero "))
print(f"Su suma es", num1 + num2 )
print(f"Su resta es", num1 - num2 )
print(f"Su multiplicación es", num1 * num2 )
print(f"Su división es", num1 // num2 )
#Ejercicio 8:  Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
print("Ejercicio N°8")
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
imc = peso / (altura ** 2)
print("Su imc es de ", imc)
#Ejercicio 9:  Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 
print("Ejercicio N°9")
temp = float(input("Ingresela temperatura en grados celsius "))
tempfahrenheit = float (9/5 * temp + 32)
print(f"su temperatura equivale a",tempfahrenheit,"grados Fahrenheit")
#Ejercicio 10:  Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
#dichos números.
print("Ejercicio N°10")
num1 = int(input("ingrese un numero "))
num2 = int(input("ingrese un numero "))
num3 = int(input("ingrese un numero "))
promedio = (num1 + num2 + num3) // 3
print (f"su promedio es",promedio)