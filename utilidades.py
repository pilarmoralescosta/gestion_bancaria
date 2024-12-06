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
    return texto


def validar_direccion():
    '''Función que pide al usuario que ingrese una direccion, la valida y la retorna validada'''
    direccion_valida = None
    mensaje = "Direccion del cliente"
    while direccion_valida == None:
        direccion = input(f'{mensaje}: ')
        direccion_valida = val.validar_direccion(val.validar_input_no_vacio(direccion, mensaje))
    return direccion


def validar_telefono():
    '''Función que pide al usuario que ingrese un telefono, lo valida y lo retorna validado'''
    telefono_valido = None
    mensaje = "Teléfono del cliente"
    while telefono_valido == None:
        telefono = input(f'{mensaje} (sin incluir el 0 del código de área ni 15 si es celular): ')
        telefono_valido = val.validar_telefono(val.validar_input_no_vacio(telefono, mensaje))
    return telefono


def validar_email():
    '''Función que pide al usuario que ingrese un email, lo valida y lo retorna validado'''
    email_valido = None
    mensaje = "Email del cliente"
    while email_valido == None:
        email = input(f'{mensaje}: ')
        email_valido = val.validar_email(val.validar_input_no_vacio(email, mensaje))
    return email


def validar_clave():
    '''Función que pide al usuario que ingrese una clave, la valida y la retorna validada'''
    clave_valida = None
    mensaje = "Ingrese una clave"
    while clave_valida == None:
        clave = input(f'{mensaje} (mínimo 8 caracteres): ')
        clave_valida = val.validar_clave(val.validar_input_no_vacio(clave, mensaje))
    return clave
