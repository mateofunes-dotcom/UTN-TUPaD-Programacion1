from flask import Flask, request, jsonify
from crud import (
    obtener_autores_db, insertar_autor_db,
    obtener_libros_db, obtener_libro_por_id_db,
    insertar_libro_db, actualizar_libro_db, eliminar_libro_db
)
from inicializar_bd import crear_base_datos

# Asegurar que la base de datos esté creada al arrancar
crear_base_datos()

app = Flask(__name__)

# --- ENDPOINTS DE AUTORES ---

@app.route('/api/autores', methods=['GET'])
def listar_autores():
    autores = obtener_autores_db()
    return jsonify(autores), 200

@app.route('/api/autores', methods=['POST'])
def crear_autor():
    data = request.get_json()
    if not data or 'nombre' not in data or 'nacionalidad' not in data:
        return jsonify({"error": "Bad Request: Faltan campos obligatorios (nombre, nacionalidad)"}), 400
    
    nuevo_id = insertar_autor_db(data['nombre'], data['nacionalidad'])
    nuevo_autor = {"id": nuevo_id, "nombre": data['nombre'], "nacionalidad": data['nacionalidad']}
    return jsonify(nuevo_autor), 201


# --- ENDPOINTS DE LIBROS ---

@app.route('/api/libros', methods=['GET'])
def listar_libros_api():
    libros = obtener_libros_db()
    return jsonify(libros), 200

@app.route('/api/libros/<int:id_libro>', methods=['GET'])
def obtener_libro(id_libro):
    libro = obtener_libro_por_id_db(id_libro)
    if not libro:
        return jsonify({"error": f"Not Found: El libro con ID {id_libro} no existe."}), 404
    return jsonify(libro), 200

@app.route('/api/libros', methods=['POST'])
def crear_libro():
    data = request.get_json()
    if not data or 'titulo' not in data or 'anio' not in data or 'autor_id' not in data:
        return jsonify({"error": "Bad Request: Faltan campos obligatorios (titulo, anio, autor_id)"}), 400
    
    nuevo_id = insertar_libro_db(data['titulo'], data['anio'], data['autor_id'])
    libro_creado = obtener_libro_por_id_db(nuevo_id)
    return jsonify(libro_creado), 201

@app.route('/api/libros/<int:id_libro>', methods=['PUT'])
def actualizar_libro(id_libro):
    data = request.get_json()
    if not data or 'titulo' not in data or 'anio' not in data or 'autor_id' not in data:
        return jsonify({"error": "Bad Request: Faltan campos obligatorios para actualizar (titulo, anio, autor_id)"}), 400
    
    exito = actualizar_libro_db(id_libro, data['titulo'], data['anio'], data['autor_id'])
    if not exito:
        return jsonify({"error": f"Not Found: No se pudo actualizar, el libro con ID {id_libro} no existe."}), 404
    
    libro_actualizado = obtener_libro_por_id_db(id_libro)
    return jsonify(libro_actualizado), 200

@app.route('/api/libros/<int:id_libro>', methods=['DELETE'])
def eliminar_libro(id_libro):
    exito = eliminar_libro_db(id_libro)
    if not exito:
        return jsonify({"error": f"Not Found: No se pudo eliminar, el libro con ID {id_libro} no existe."}), 404
    
    return jsonify({"mensaje": f"Libro con ID {id_libro} eliminado correctamente."}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)