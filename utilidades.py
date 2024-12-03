import validaciones as val


def validar_dni(dni):
    '''Función que recibe el dni del cliente, lo valida y retorna'''
    dni_valid = val.validar_dni(dni)
    while dni_valid == None:
        print("Ingrese un número de documento válido")
        dni = input("Número de documento del cliente: ")
        dni_valid = val.validar_dni(dni)
    return dni


def validar_cuit_cuil(cuit_cuil):
    '''Función que recibe el cuit/cuil del cliente, lo valida y lo retorna validado'''

    if '-' in cuit_cuil:
        cuit_cuil = cuit_cuil.replace('-', '')
    if '/' in cuit_cuil:
        cuit_cuil = cuit_cuil.replace('/', '')
    cuit_cuil_valid = val.validar_cuit_cuil(cuit_cuil)
    while cuit_cuil_valid == None:
        print("Ingrese un CUIT/CUIL válido")
        cuit_cuil = input(
            "Número de CUIT/CUIL del cliente (sin guiones, sólo números): ")
        cuit_cuil_valid = val.validar_cuit_cuil(cuit_cuil)
    return cuit_cuil


def validar_texto(tipo):
    '''Función que recibe el tipo de texto a validar, solicita que se ingrese un texto,
    valida que no esté vacio y que tenga un formato correcto y lo retorna validado'''
    texto_valido = None
    while texto_valido == None:
        texto = input(f'{tipo}: ')
        texto_valido = val.validar_texto(val.validar_input_no_vacio(texto, tipo), tipo)
    return texto_valido
