from clases import Archivo, Directorio 

# ---------------------------
# Función 1: Calcular Tamaño Total
# ---------------------------
def calcular_tamano_total(directorio: Directorio) -> int:
    # Sumar archivos del directorio actual
    total = sum(archivo.tamano_bytes for archivo in directorio.archivos)
    # Sumar recursivamente cada subdirectorio
    for subdir in directorio.subdirectorios:
        total += calcular_tamano_total(subdir)
    return total

# ---------------------------
# Función 2: Buscar por Extensión
# ---------------------------
def buscar_por_extension(directorio: Directorio, extension: str, ruta_actual: str = "") -> list:
    resultados = []
    # Construir la ruta de este directorio
    ruta = f"{ruta_actual}{directorio.nombre}/"
    
    # Revisar archivos locales
    for archivo in directorio.archivos:
        if archivo.nombre.endswith(extension):
            resultados.append(f"{ruta}{archivo.nombre}")
    
    # Llamada recursiva a subdirectorios
    for subdir in directorio.subdirectorios:
        resultados.extend(buscar_por_extension(subdir, extension, ruta))
    
    return resultados

# ---------------------------
# Función 3: Limpiar Archivos Vacíos
# ---------------------------
def limpiar_archivos_vacios(directorio: Directorio) -> int:
    contador = 0
    
    # Eliminar archivos vacíos del directorio actual
    archivos_conservar = []
    for archivo in directorio.archivos:
        if archivo.tamano_bytes == 0:
            contador += 1
        else:
            archivos_conservar.append(archivo)
    directorio.archivos = archivos_conservar
    
    # Limpiar recursivamente subdirectorios
    for subdir in directorio.subdirectorios:
        contador += limpiar_archivos_vacios(subdir)
    
    return contador

def construir_arbol():
    # Raíz
    root = Directorio("root")
    
    # Archivos en raíz
    root.archivos.append(Archivo("documento.pdf", 1500))
    root.archivos.append(Archivo("config.txt", 0))  # Vacío
    
    # Subdirectorio imagenes
    imagenes = Directorio("imagenes")
    imagenes.archivos.append(Archivo("foto1.png", 2000))
    root.subdirectorios.append(imagenes)
    
    # Subdirectorio proyectos
    proyectos = Directorio("proyectos")
    proyectos.archivos.append(Archivo("foto2.png", 3500))
    proyectos.archivos.append(Archivo("avance.pdf", 800))
    
    # Subdirectorio temp dentro de proyectos
    temp = Directorio("temp")
    temp.archivos.append(Archivo("log.txt", 0))  # Vacío
    proyectos.subdirectorios.append(temp)
    
    root.subdirectorios.append(proyectos)
    
    return root