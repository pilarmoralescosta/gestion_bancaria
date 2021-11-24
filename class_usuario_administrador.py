# -*- coding: utf-8 -*-

from class_cliente_pyme import Cliente_pyme
from class_usuario import Usuario

from class_cliente_individuo import Cliente_individuo


class Usuario_administrador():

    def __init__(self):
        self.username = 'administrador'
        self.clave = '4dm1n1str4d0r'

    def monto_saldo_retenido(self):
        pass

    def monto_saldo_descubierto(self):
        pass

    def costos_transaccion(self):
        pass

    def beneficios_transaccion(self):
        pass

    def registrar_cliente(self):
        pass

    def registrar_cuenta(self):
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
