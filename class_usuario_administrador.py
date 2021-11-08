# -*- coding: utf-8 -*-

from class_cliente_individuo import Cliente_individuo
from class_cliente_pyme import Cliente_pyme
from class_usuario import Usuario
from class_aut_firmante import Autoridad_firmante


class Usuario_administrador ():

    def __init__(self):
        self.username = 'administrador'
        self.clave = '4dm1n1str4d0r'

    def alta_usuario(self, dni, id_cliente, usuarios):
        es_cliente_individuo = False
        es_cliente_pyme = False

        if int(dni) in usuarios:
            return print("El usuario ya existe")
        else:
            clave = input("Ingrese una clave: ")
            tipo_cliente = input(
                "¿Es un cliente individuo, PyME o ambos? (i/p/a): ").lower()
            if tipo_cliente == "i":
                es_cliente_individuo = True
            elif tipo_cliente == "p":
                es_cliente_pyme = True
            elif tipo_cliente == "a":
                es_cliente_individuo = True
                es_cliente_pyme = True
            else:
                return print("Ingrese una opción válida")
            nuevo_usuario = Usuario(
                dni, clave, id_cliente, es_cliente_individuo, es_cliente_pyme)
            usuarios[dni] = nuevo_usuario
            return print(f'\nEl usuario ha sido generado exitosamente: ' + Usuario.__str__(nuevo_usuario))

    def alta_cliente_individuo(self, clientes_individuos):
        dni = int(input("Número de documento del cliente: "))

        for cliente in clientes_individuos:
            if clientes_individuos[cliente].dni == int(dni):
                return print("El cliente ya existe")

        apellido = input("Apellido del cliente: ")
        nombre = input("Nombre del cliente: ")
        cuit_cuil = input("CUIT/CUIL del cliente: ")
        direccion = input("Dirección del cliente: ")
        telefono = input("Teléfono del cliente: ")
        mail = input("Email del cliente: ")
        # formato del id de cliente: ITB029 - I: cliente individuo T: primer caracter nombre B: primer caracter apellido 029: últimos 3 dígitos del dni
        id_cliente = f'I{apellido[0].upper()}{nombre[0].upper()}{dni[-3:]}'
        cuentas = []  # lista de cuentas del cliente

        # creamos la instancia de Cliente_incividuo
        nuevo_cliente_individuo = Cliente_individuo(
            apellido, nombre, dni, cuit_cuil, direccion, telefono, mail, id_cliente, cuentas)
        clientes_individuos[id_cliente] = nuevo_cliente_individuo

        # creamos la instancia de Usuario
        self.alta_usuario(dni, id_cliente, usuarios)

        return print(f'\nEl cliente ha sido generado exitosamente: ' + nuevo_cliente_individuo.__str__)

    def alta_autoridad_firmante(self, id_cliente, usuarios):
        print(f'\nAlta de autoridad/firmante')
        dni = input("Número de documento: ")

        for cliente in clientes_individuos:
            if clientes_individuos[cliente].dni == int(dni):
                return print("Autoridad firmante existente")

        apellido = input("Apellido: ")
        nombre = input("Nombre: ")
        cuit_cuil = input("CUIT/CUIL: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        mail = input("Email: ")
        nueva_autoridad_firmante = Autoridad_firmante(
            apellido, nombre, dni, cuit_cuil, direccion, telefono, mail)

        # creamos la instancia de Usuario
        self.alta_usuario(dni, id_cliente, usuarios)

        return nueva_autoridad_firmante

    def alta_cliente_pyme(self, clientes_pyme):
        cuit_cuil = input("Número de CUIT/CUIL del cliente: ")

        for cliente in clientes_individuos:
            if clientes_individuos[cliente].dni == cuit_cuil:
                return print("El cliente ya existe")

        razon_social = input("Razón social del cliente: ")
        direccion = input("Dirección del cliente: ")
        telefono = input("Teléfono del cliente: ")
        mail = input("Email del cliente: ")

        # formato del id de cliente: PX1234 - P: cliente PyME X: primer caracter Razon Social 1234: últimos 4 dígitos del cuit
        id_cliente = f'P{razon_social[0].upper()}{cuit_cuil[-4:-2]}{cuit_cuil[-1]}'
        cuentas = []  # lista de cuentas del cliente

        autoridades_firmantes = []
        agregar_aut_firmante = True
        while agregar_aut_firmante:
            autoridad_firmante = self.alta_autoridad_firmante(
                id_cliente, usuarios)
            autoridades_firmantes.append(autoridad_firmante)
            agregar = input(
                "¿Desea agregar otra autoridad/firmante? (s/n)").lower()
            if agregar == "n":
                agregar_aut_firmante = False
            elif agregar == "s":
                agregar_aut_firmante = True
            else:
                print("Ingrese una opción válida")

        # creamos la instancia de Cliente_pyme
        nuevo_cliente_pyme = Cliente_pyme(razon_social, cuit_cuil, direccion, telefono, mail,
                                          autoridades_firmantes, id_cliente, cuentas)
        clientes_pyme[id_cliente] = nuevo_cliente_pyme
        return print(f'\nEl cliente ha sido generado exitosamente: ' + Cliente_pyme.__str__(nuevo_cliente_pyme))

    def modificar_cliente(self):
        pass

    def baja_cliente(self):
        pass

    def consultar_monto_saldo_retenido(self):
        pass

    def consultar_monto_descubierto(self):
        pass

    def modificar_costos(self):
        pass

    def calcular_porcentaje_benificios_transaccion(self):
        pass


# TEST
admin = Usuario_administrador()

usuarios = {
    1: Usuario(1, 12, 'IRO345', True, False),
    2: Usuario(2, 11, 'POB123', False, True)
}
clientes_individuos = {
    32521: Cliente_individuo("Boragini", "Trinidad", 32521456, 2035214528, "San Martin 100", 24941546289, 3, 32521, []),
    32123: Cliente_individuo("Gronda", "Lucio", 25487412, 25632145, "Saavedra 42", 4214587, 12, 32123, [])
}

clientes_pyme = {1: Cliente_pyme(
    "La Pirca", 125487458, "Belgrano 230", 2494561231, 'unmail', [3, 25], 1, [78, 79])}

# ALTA USUARIO
# admin.alta_usuario(3, usuarios)
# for usuario in usuarios:
#     print(usuarios[usuario])

# ALTA CLIENTE INDIVIDUO
# admin.alta_cliente_individuo(clientes_individuos)

# for cliente in clientes_individuos:
#     print(clientes_individuos[cliente].dni)
#     print(usuarios[usuario])

# ALTA CLIENTE PYME
admin.alta_cliente_pyme(clientes_pyme)
