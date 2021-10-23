from class_usuario import Usuario


# creo que no debería ser hijo de usuario ya que tiene atributos propios y no depende de usuario
class Usuario_administrador (Usuario):

    username = 'administrador'
    clave = '4dm1n1str4d0r'

    def __init__(self, id, username, clave):
        super().__init__(id, username, clave)

    def alta_usuario(self):
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
