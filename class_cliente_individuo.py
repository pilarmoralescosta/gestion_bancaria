from class_persona import Persona
from class_cliente import Cliente


class Cliente_individuo(Persona, Cliente):
    def __init__(self, apellido, nombre, dni, direccion, telefono, email, id_cliente, cuentas):
        Persona.__init__(self, apellido, nombre, dni,
                         direccion, telefono, email)
        Cliente.__init__(self, id_cliente, cuentas)

    def cierre_cuenta(self):
        pass

    def apertura_cuenta(self):
        pass

    def __str__(self):
        return Persona().__str__() + Cliente().__str__()
