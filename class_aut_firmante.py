from class_persona import Persona


class Autoridad_firmante(Persona):
    def __init__(self, dni, cuit_cuil, nombre, apellido, direccion, telefono, email):
        super.__init__(self, dni, cuit_cuil, nombre,
                       apellido, direccion, telefono, email)

    def cierre_cuenta(self):
        pass

    def apertura_cuenta(self):
        pass

    def __str__(self):
        return super().__str__()
