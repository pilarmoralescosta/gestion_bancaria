from class_cliente import Cliente
from class_usuario import Usuario


class Cliente_individuo(Cliente, Usuario):
    def __init__(self, id_cliente, dni, nombre, apellido, cuit_cuil, direccion, telefono, usuario):
        super().__init__(id_cliente, cuit_cuil, direccion, telefono, usuario)
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido


    def cierre_cuenta(self):
        pass

    def apertura_cuenta(self):
        pass

    def __str__(self):
        return super().__str__() + f'\nDni: {self.dni} \nApellido y nombre {self.apellido}, {self.nombre}'
