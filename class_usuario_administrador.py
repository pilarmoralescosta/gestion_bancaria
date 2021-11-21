# -*- coding: utf-8 -*-

from class_cliente_pyme import Cliente_pyme
from class_usuario import Usuario

from class_cliente_individuo import Cliente_individuo


class Usuario_administrador():

    def __init__(self):
        self.username = 'administrador'
        self.clave = '4dm1n1str4d0r'

    def modificar_autoridad_firmante(aut_firmante_a_modificar):
        pass

    # def modificar_cliente_pyme(cliente_py_a_modificar):
    #     print('Modificación de datos del cliente: ')
    #     cliente_py_a_modificar.razon_social = input(
    #         "Razón Social del cliente: ")
    #     cliente_py_a_modificar.cuit_cuil = input("CUIT/CUIL del cliente: ")
    #     cliente_py_a_modificar.direccion = input("Dirección del cliente: ")
    #     cliente_py_a_modificar.telefono = input("Teléfono del cliente: ")
    #     cliente_py_a_modificar.mail = input("Email del cliente: ")
    #     dni_aut = input('Ingrese el DNI de la autoridad/firmante: ')

    #     # for cliente in clientes_pyme:

    #     if dni_aut in clientes_pyme.autoridades_firmantes:
    #         cliente_py_a_modificar = Banco.clientes_pyme[id_cliente]
    #         return self.modificar_cliente_pyme(cliente_py_a_modificar)

    #     return print(f'\nLos datos del cliente han sido modificados exitosamente: ' + cliente_ind_a_modificar.__str__)

    def modificar_cliente(self, id_cliente, sistema):

        if id_cliente in sistema.clientes_individuos:
            cliente_ind_a_modificar = sistema.clientes_individuos[id_cliente]
            return self.modificar_cliente_ind(cliente_ind_a_modificar)
        elif id_cliente in clientes_pyme:
            cliente_py_a_modificar = sistema.clientes_pyme[id_cliente]
            return self.modificar_cliente_pyme(cliente_py_a_modificar)
        else:
            return print('No se encontraron coincidencias')

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
# admin.alta_cliente_ind_a_modificar(clientes_individuos)

# for cliente in clientes_individuos:
#     print(clientes_individuos[cliente].dni)
#     print(usuarios[usuario])

# ALTA CLIENTE PYME
# admin.alta_cliente_pyme(clientes_pyme)

# MODIFICAR CLIENTE
# MODIFICAR CLIENTE INDIVIDUO
# admin.modificar_cliente(32123, clientes_individuos, clientes_pyme)
