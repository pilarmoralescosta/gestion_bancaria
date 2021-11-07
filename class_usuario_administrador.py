# -*- coding: utf-8 -*-

from class_usuario import Usuario


class Usuario_administrador ():

    def __init__(self):
        self.username = 'administrador'
        self.clave = '4dm1n1str4d0r'

    def alta_usuario(self, usuarios):
        es_cliente_individuo = False
        es_cliente_pyme = False

        usuario = input("Ingrese el número de documento del cliente: ")

        if int(usuario) in usuarios:
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
                usuario, clave, es_cliente_individuo, es_cliente_pyme)
            usuarios[usuario] = nuevo_usuario
            return print(f'El usuario ha sido generado exitosamente: ' + Usuario.__str__(nuevo_usuario))

    def alta_usuario_pyme(self):
        pass

    def alta_cliente(self):
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
usuarios = {1: Usuario(1, 12, True, False), 2: Usuario(2, 11, False, True)}
admin = Usuario_administrador()
admin.alta_usuario_cliente(usuarios)
for usuario in usuarios:
    print(usuarios[usuario])
