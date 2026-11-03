import requests

BASE_URL = "http://127.0.0.1:5000/api"

def probar_api():
    print("--- 1. Probando GET /api/libros ---")
    response = requests.get(f"{BASE_URL}/libros")
    print(f"Status: {response.status_code}")
    print(response.json())
    print()

    print("--- 2. Creando Autor y Libro (POST) ---")
    res_autor = requests.post(f"{BASE_URL}/autores", json={
        "nombre": "Julio Cortázar",
        "nacionalidad": "Argentina"
    })
    autor_id = res_autor.json().get("id")
    print(f"Autor creado con ID: {autor_id}")

    res_libro = requests.post(f"{BASE_URL}/libros", json={
        "titulo": "Rayuela",
        "anio": 1963,
        "autor_id": autor_id
    })
    print(f"Status Libro POST: {res_libro.status_code}")
    libro_creado = res_libro.json()
    libro_id = libro_creado.get("id")
    print(libro_creado)
    print()

    print("--- 3. Actualizando el libro creado (PUT) ---")
    res_put = requests.put(f"{BASE_URL}/libros/{libro_id}", json={
        "titulo": "Rayuela (Edición Aniversario)",
        "anio": 1963,
        "autor_id": autor_id
    })
    print(f"Status PUT: {res_put.status_code}")
    print(res_put.json())
    print()

    print("--- 4. Eliminando el libro creado (DELETE) ---")
    res_del = requests.delete(f"{BASE_URL}/libros/{libro_id}")
    print(f"Status DELETE: {res_del.status_code}")
    print(res_del.json())

if __name__ == "__main__":
    probar_api()