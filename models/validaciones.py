import re

def validar_cedula(cedula: str) -> bool:
    """Valida cédula nicaragüense (001-XXXXXX-XXXXX)"""
    return bool(re.match(r'^001-\d{6}-\d{4}[A-Z]$', cedula.upper()))

def validar_nombre(texto: str) -> bool:
    """Solo letras y espacios, 2-50 caracteres"""
    return texto.replace(" ", "").isalpha() and 2 <= len(texto) <= 50

def validar_edad(edad: str) -> bool:
    """Entre 15 y 50 años"""
    return edad.isdigit() and 15 <= int(edad) <= 50

def validar_telefono(telefono: str) -> bool:
    """8 dígitos exactos"""
    return telefono.isdigit() and len(telefono) == 8

def validar_peso(peso: str) -> bool:
    """Entre 30 y 200 kg"""
    try:
        return 30 <= float(peso) <= 200
    except ValueError:
        return False

def validar_altura(altura: str) -> bool:
    """Entre 100 y 250 cm"""
    try:
        return 100 <= float(altura) <= 250
    except ValueError:
        return False



