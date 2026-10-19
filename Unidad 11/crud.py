import sqlite3
import os

#Obtiene la ruta de la carpeta donde está el archivo de Python
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#Une esa ruta con el nombre de la base de datos
DB_PATH = os.path.join(BASE_DIR, "biblioteca.db")

#Luego uso DB_PATH en lugar de escribir "biblioteca.db" directamente ->
conexion = sqlite3.connect(DB_PATH)

def registrar_autor(nombre: str, nacionalidad: str) -> int:

    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO autores (nombre, nacionalidad)
        VALUES (?, ?)
    """, (nombre,nacionalidad))
    conexion.commit()
    autor_id = cursor.lastrowid
    conexion.close()
    return autor_id

def registrar_libro(titulo: str, anio: int, autor_id: int):
    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO libros (titulo, anio, autor_id)
        VALUES (?, ?, ?)
    """, (titulo,anio,autor_id))
    conexion.commit()
    conexion.close()

def listar_libros():
    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT libros.titulo, libros.anio, autores.nombre
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
    """)
    resultados = cursor.fetchall()
    conexion.close()

    print("\n LIBROS LISTADOS ")
    for titulo, anio, autor in resultados:
        print(f"TITULO: '{titulo}' | Año: {anio} | Autor: {autor}")
    print("-" * 20)

def actualizar_titulo_libro(id_libro: int, nuevo_titulo: str):
    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE libros
        SET titulo = ?
        WHERE id = ?
    """, (nuevo_titulo, id_libro))
    conexion.commit()
    conexion.close()
    print(f"LIBRO ACTUALIZADO {id_libro} actualizado con éxito!")

def eliminar_libro(id_libro: int):
    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()
    cursor.execute("""
        DELETE FROM libros
        WHERE id = ?
    """, (id_libro,))
    conexion.commit()
    conexion.close()
    print(f"EL LIBRO con ID {id_libro} fue retirado de la base de datos.")