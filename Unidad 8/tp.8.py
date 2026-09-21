#1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
#productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad 

with open ("productos.txt", "w") as archivo:
    archivo.write("Mause,12000,6\n")
    archivo.write("Auriculares,35000,10\n")
    archivo.write("Teclado,55000,8\n")

#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
#formato: #Producto: Lapicera | Precio: $120.5 | Cantidad: 30 

print("Ejercicio N°2")
with open ("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
        print("Producto:", partes[0], "| Precio: $", partes[1], "| Cantidad:", partes[2])

print("========================================")
#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, 
#cantidad) y lo agregue al archivo sin borrar el contenido existente. 

print("Ejercicio N°3")
with open ("productos.txt", "r") as archivo:
      for linea in archivo:
            linea = linea.strip()
            partes = linea.split(",")
            print("Producto:", partes[0], "| Precio: $", partes[1], "| Cantidad:", partes[2])

nombre = input("Igrese un producto: ")
precio = input("Ingrese el precio del producto: ") 
cantidad = input("ingrese la cantidad disponible del producto: ")
producto_final = nombre + "," + precio + "," + cantidad

with open ("productos.txt", "a") as archivo:
     archivo.write(producto_final + "\n" )

print("========================================")
#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
#una lista llamada productos, donde cada elemento sea un diccionario con claves: 
#nombre, precio, cantidad.

print("Ejercicio N°4")
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        partes = linea.strip().split(",")
        producto = {
            "nombre": partes[0],
            "precio": partes[1],
            "cantidad": partes[2]
        }
        productos.append(producto)
        print(producto)

print("========================================")
#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
#no existe, mostrar un mensaje de error. 

print("Ejercicio N°5")

buscar_producto = input("Ingrese nombre del producto que desea buscar: ")

for producto in productos:
    if buscar_producto == producto["nombre"]:
        print("Producto:", producto["nombre"], "| Precio: $", producto["precio"], "| Cantidad:", producto["cantidad"])
        break
else:
     print("Este producto no existe")
     
print("========================================")


#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado 
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los 
#productos actualizados desde la lista. 

print("Ejercicio N°6")
with open("productos.txt", "w") as archivo:
    for producto in productos:
        archivo.write(
            producto["nombre"] + "," +
            producto["precio"] + "," +
            producto["cantidad"] + "\n"
        )