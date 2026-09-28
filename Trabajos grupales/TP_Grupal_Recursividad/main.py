from clases import Archivo, Directorio
from funciones_main import construir_arbol, calcular_tamano_total, buscar_por_extension, limpiar_archivos_vacios

if __name__ == "__main__":
    # Crear estructura
    root = construir_arbol()
    
    # Prueba 1: Tamaño total
    tam_total = calcular_tamano_total(root)
    print(f"1. Tamaño total: {tam_total} bytes")
    print(f"   Esperado: 7800 bytes " if tam_total == 7800 else f"    Incorrecto")
    
    # Prueba 2: Buscar .pdf
    archivos_pdf = buscar_por_extension(root, ".pdf")
    print(f"\n2. Archivos .pdf: {archivos_pdf}")
    esperado_pdf = ["root/documento.pdf", "root/proyectos/avance.pdf"]
    print(f"   Esperado: {esperado_pdf} " if archivos_pdf == esperado_pdf else f"    Incorrecto")
    
    # Prueba 3: Limpiar vacíos
    eliminados = limpiar_archivos_vacios(root)
    print(f"\n3. Archivos eliminados: {eliminados}")
    print(f"   Esperado: 2 " if eliminados == 2 else f"    Incorrecto")