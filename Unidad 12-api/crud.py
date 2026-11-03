import sqlite3
import os

# Obtiene la ruta de la carpeta donde está el archivo de Python
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "biblioteca.db")

# --- MÉTODOS REPOSITORIO (Para la API y test_api.py) ---

def obtener_autores_db():
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, nacionalidad FROM autores")
    filas = cursor.fetchall()
    conexion.close()
    return [{"id": f[0], "nombre": f[1], "nacionalidad": f[2]} for f in filas]

def insertar_autor_db(nombre: str, nacionalidad: str) -> int:
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)", (nombre, nacionalidad))
    conexion.commit()
    autor_id = cursor.lastrowid
    conexion.close()
    return autor_id

def obtener_libros_db():
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT libros.id, libros.titulo, libros.anio, autores.id, autores.nombre, autores.nacionalidad
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
    """)
    filas = cursor.fetchall()
    conexion.close()
    
    libros = []
    for f in filas:
        libros.append({
            "id": f[0],
            "titulo": f[1],
            "anio": f[2],
            "autor": {
                "id": f[3],
                "nombre": f[4],
                "nacionalidad": f[5]
            }
        })
    return libros

def obtener_libro_por_id_db(id_libro: int):
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT libros.id, libros.titulo, libros.anio, autores.id, autores.nombre, autores.nacionalidad
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
        WHERE libros.id = ?
    """, (id_libro,))
    f = cursor.fetchone()
    conexion.close()
    
    if not f:
        return None
    
    return {
        "id": f[0],
        "titulo": f[1],
        "anio": f[2],
        "autor": {
            "id": f[3],
            "nombre": f[4],
            "nacionalidad": f[5]
        }
    }

def insertar_libro_db(titulo: str, anio: int, autor_id: int) -> int:
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?)", (titulo, anio, autor_id))
    conexion.commit()
    libro_id = cursor.lastrowid
    conexion.close()
    return libro_id

def actualizar_libro_db(id_libro: int, titulo: str, anio: int, autor_id: int):
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE libros
        SET titulo = ?, anio = ?, autor_id = ?
        WHERE id = ?
    """, (titulo, anio, autor_id, id_libro))
    filas_afectadas = cursor.rowcount
    conexion.commit()
    conexion.close()
    return filas_afectadas > 0

def eliminar_libro_db(id_libro: int):
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
    filas_afectadas = cursor.rowcount
    conexion.commit()
    conexion.close()
    return filas_afectadas > 0


# --- MÉTODOS AUXILIARES / LEGACY (Para compatibilidad con main.py si lo usas) ---

def registrar_autor(nombre: str, nacionalidad: str) -> int:
    return insertar_autor_db(nombre, nacionalidad)

def registrar_libro(titulo: str, anio: int, autor_id: int):
    return insertar_libro_db(titulo, anio, autor_id)

def listar_libros():
    libros = obtener_libros_db()
    print("\n--- LIBROS LISTADOS ---")
    for l in libros:
        print(f"ID: {l['id']} | TITULO: '{l['titulo']}' | Año: {l['anio']} | Autor: {l['autor']['nombre']}")
    print("-" * 20)

def actualizar_titulo_libro(id_libro: int, nuevo_titulo: str):
    libro = obtener_libro_por_id_db(id_libro)
    if libro:
        actualizar_libro_db(id_libro, nuevo_titulo, libro["anio"], libro["autor"]["id"])
        print(f"LIBRO ACTUALIZADO {id_libro} con éxito!")

def eliminar_libro(id_libro: int):
    if eliminar_libro_db(id_libro):
        print(f"EL LIBRO con ID {id_libro} fue retirado de la base de datos.")