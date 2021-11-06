from class_usuario import Usuario
from funciones import generar_clave

# creo que no debería ser hijo de usuario ya que tiene atributos propios y no depende de usuario


class Usuario_administrador ():

    def __init__(self):
        self.username = 'administrador'
        self.clave = '4dm1n1str4d0r'

    def alta_usuario_cliente(self):
        nro_usuario = input("Ingrese el número de documento del cliente: ")
        if nro_usuario in usuarios:
            return print("El usuario ya existe")
        else:
            for cliente in clientes:
                if nro_usuario == cliente.dni or nro_usuario == cliente.cuit_cuil:
                    id_cliente = clientes.cliente.nro_cliente
                    break
            clave = generar_clave()
            for usuario in usuarios:
                if usuario[clave] == clave:
                    clave = generar_clave()
            usuarios.append(Usuario(nro_usuario, clave, id_cliente))
            return print("El usuario ha sido generado exitosamente")

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


# admin = Usuario_administrador()
# admin.alta_usuario()
