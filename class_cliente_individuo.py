from class_persona import Persona
from class_cliente import Cliente


class Cliente_individuo(Persona, Cliente):
    def __init__(self, dni, apellido, nombre, direccion, telefono, email, id_cliente, cuentas):
        Persona.__init__(self, dni, apellido, nombre,
                         direccion, telefono, email)
        Cliente.__init__(self, id_cliente, cuentas)

    def cierre_cuenta(self):
        pass

    def apertura_cuenta(self):
        pass

    def __str__(self):
        return super().__str__() + f'\nDni: {self.dni} \nApellido y nombre {self.apellido}, {self.nombre}'
