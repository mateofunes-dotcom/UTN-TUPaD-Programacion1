# validaciones.py

def validar_solo_letras(cadena):
    return cadena.replace(" ", "").isalpha() #Devuelve un True o False si todos los caracteres de unan cadena son letras del alfabeto


def validar_legajo(legajo):
    return legajo.isdigit() and len(legajo) == 5 #Si es Verdadero en donde el legajo es un número y cumple con 5 dígitos


def validar_nota(nota_str):
    if not nota_str.replace(".", "", 1).isdigit():
        return False
    nota = float(nota_str)
    return 1 <= nota <= 10


def validar_existe_alumno(legajo, diccionario):
    return legajo in diccionario