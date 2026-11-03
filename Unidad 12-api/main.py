from clase_bd import Autor, Libro
from inicializar_bd import crear_base_datos
from crud import(
    registrar_autor,
    registrar_libro,
    listar_libros,
    actualizar_titulo_libro,
    eliminar_libro
)

def ejecutar_prueba_integral():
    print("=== INICIANDO PRUEBA INTEGRAL ===\n")

    print("--- Probando Ejercicio 1 (Clases y Objetos) ---")
    autor_demo = Autor(1, "Gabriel García Márquez", "Colombiana")
    libro_demo = Libro(101, "Cien años de soledad", 1967, autor_demo)
    print(autor_demo)
    print(libro_demo)
    print()

    print("1. Inicializando base de datos...")
    crear_base_datos()
    print()

    # Paso 2: Registrar al menos 2 autores y 3 libros (crud.py)
    print("2. Registrando autores y libros...")
    id_autor1 = registrar_autor("Gabriel García Márquez", "Colombiana")
    id_autor2 = registrar_autor("Jorge Luis Borges", "Argentina")

    registrar_libro("Cien años de soledad", 1967, id_autor1)
    registrar_libro("El coronel no tiene quien le escriba", 1961, id_autor1)
    registrar_libro("Ficciones", 1944, id_autor2)
    print("   Autores y libros registrados correctamente.\n")

    # Paso 3: Listar todos los libros registrados en consola
    print("3. Listado inicial de libros:")
    listar_libros()

    # Paso 4: Actualizar el título de uno de los libros y verificar el cambio
    print("4. Actualizando título del libro con ID 1...")
    actualizar_titulo_libro(1, "Cien años de soledad (Edición Conmemorativa)")
    print("\n   Verificación tras la actualización:")
    listar_libros()

    # Paso 5: Eliminar un libro y mostrar el listado resultante
    print("5. Eliminando el libro con ID 2...")
    eliminar_libro(2)
    print("\n   Listado final resultante:")
    listar_libros()

if __name__ == "__main__":
    ejecutar_prueba_integral()