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
        print(f'El campo "{tipo}" es obligatorio, no puede estar vacío\n')
        texto = input(f'{tipo}: ')
    return texto


def validar_texto(texto, tipo):
    '''Valida que el texto ingresado tenga una o mas palabras, separadas por un espacio.
    Las palabras contienen solo letras, inclusive tildes y deben ser mayores a 2 letras.
    Retorna None si no es valido'''
    texto_valido = re.fullmatch(r'^[A-Za-záéíóúñ]{2,}([\s][A-Za-záéíóúñ]{2,})*$', texto)
    if texto_valido == None:
        print(f'El campo "{tipo}" no puede contener números o caracteres especiales\n')
    return texto_valido


def validar_direccion(direccion):
    '''Valida que el texto ingresado tenga una o mas palabras separadas por un espacio
    y una secuencia de numeros.
    Las palabras contienen solo letras, inclusive tildes y deben ser mayores a 2 letras.
    Retorna None si no es valido'''
    direccion_valida = re.fullmatch(r'^[A-Za-záéíóúñ]{2,}([\s][A-Za-záéíóúñ]{2,})*\s\d+$', direccion)
    if direccion_valida == None:
        print('La direccion ingresada no es válida\n')
    return direccion_valida


def validar_telefono(telefono):
    '''Valida que el telefono ingresado tenga 10 digitos
    y que el primer dígito no sea 0.
    Retorna None si no es valido'''
    telefono_valido = re.fullmatch(r'[1-9]\d{9}', telefono)
    if telefono_valido == None:
        print('El telefono ingresado no es valido. El primer dígito no debe ser 0 y deben ser 10 dígitos en total, incluido el 0\n')
    return telefono_valido


def validar_email(email):
    '''Valida que el email ingresado tenga un formato valido
    Retorna None si no es valido'''
    email_valido = re.fullmatch(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)
    if email_valido == None:
        print('El email ingresado no es válido\n')
    return email_valido