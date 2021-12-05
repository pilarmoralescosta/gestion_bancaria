from class_persona import Persona
from class_cliente import Cliente


class Cliente_individuo(Persona, Cliente):
    def __init__(self, apellido, nombre, dni, cuit_cuil, direccion, telefono, email, id_cliente, cuentas, registrado):
        Persona.__init__(self, apellido, nombre, dni, cuit_cuil,
                         direccion, telefono, email)
        Cliente.__init__(self, id_cliente, cuentas, registrado)

    def cierre_cuenta(self):
        pass

    def apertura_cuenta(self):
        pass

    def __str__(self):
        return Persona.__str__(self) + Cliente.__str__(self)
