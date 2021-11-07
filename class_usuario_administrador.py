# -*- coding: utf-8 -*-

from class_cliente_individuo import Cliente_individuo
from class_usuario import Usuario


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
        dni = input("Número de documento del cliente: ")

        for cliente in clientes_individuos:
            if clientes_individuos[cliente].dni == int(dni):
                return print("El cliente ya existe")

        apellido = input("Apellido del cliente: ")
        nombre = input("Nombre del cliente: ")
        cuit_cuil = input("CUIT/CUIL del cliente: ")
        direccion = input("Dirección del cliente: ")
        telefono = input("Teléfono del cliente: ")
        mail = input("Email del cliente: ")
        # formato del id de cliente: ITB029 -  T: primer caracter nombre B: primer caracter apellido 029: últimos 3 dígitos del dni
        id_cliente = f'I{apellido[0].upper()}{nombre[0].upper()}{dni[-3:]}'
        cuentas = []  # lista de cuentas del cliente

        # creamos la instancia de Cliente_incividuo
        nuevo_cliente_individuo = Cliente_individuo(
            apellido, nombre, dni, cuit_cuil, direccion, telefono, mail, id_cliente, cuentas)
        clientes_individuos[dni] = nuevo_cliente_individuo

        # creamos la instancia de Usuario
        self.alta_usuario(dni, id_cliente, usuarios)

        return print(f'\nEl cliente ha sido generado exitosamente: ' + Cliente_individuo.__str__(nuevo_cliente_individuo))

    def alta_cliente_pyme(self, clientes_pyme):
        pass

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
usuarios = {
    1: Usuario(1, 12, 'IRO345', True, False),
    2: Usuario(2, 11, 'POB123', False, True)
}
admin = Usuario_administrador()
# admin.alta_usuario(3, usuarios)
# for usuario in usuarios:
#     print(usuarios[usuario])
clientes_individuos = {
    32521: Cliente_individuo("Boragini", "Trinidad", 32521456, 2035214528, "San Martin 100", 24941546289, 3, 32521, []),
    32123: Cliente_individuo("Gronda", "Lucio", 25487412, 25632145, "Saavedra 42", 4214587, 12, 32123, [])
}
# print(clientes_individuos[32521])
admin.alta_cliente_individuo(clientes_individuos)

# for cliente in clientes_individuos:
#     print(clientes_individuos[cliente].dni)
#     print(usuarios[usuario])
