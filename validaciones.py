import re


def validar_dni(dni):
    '''Valida que el dni ingresado tenga entre 7 y 8 digitos del 0 al 9
    Retorna None si no es valido'''
    return re.fullmatch(r'^\d{7,8}$', dni)


def validar_cuit_cuil(cuit_cuil):
    '''Valida que el cuit/cuil ingresado tenga 11 digitos y empieze con 20, 23, 24, 27, 30, 33 o 34
    Retorna None si no es valido'''
    return re.fullmatch(r'^(20|23|24|27|30|33|34)\d{9}$', cuit_cuil)


def validar_input_no_vacio(texto, tipo):
    '''Función que recibe un valor, valida que no sea vacio y lo retorna'''
    while texto == '':
        print(f'El campo "{tipo}" es obligatorio')
        texto = input(f'{tipo}: ')
    return texto


def validar_texto(texto, tipo):
    '''Valida que el texto ingresado tenga una o mas palabras, separadas por un espacio.
    Las palabras contienen solo letras, inclusive tildes y deben ser mayores a 2 letras.
    Retorna None si no es valido'''
    texto_valido = re.fullmatch(r'^[A-Za-záéíóúñ]{2,}([\s][A-Za-záéíóúñ]{2,})+$', texto)
    if texto_valido == None:
        print(f'El campo "{tipo}" no puede contener números o caracteres especiales')
    return texto_valido
