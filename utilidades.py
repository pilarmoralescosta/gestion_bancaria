import validaciones as val


def validar_dni(dni):
    '''Función que recibe el dni del cliente, lo valida y lo validado'''
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
