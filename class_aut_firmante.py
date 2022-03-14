from class_persona import Persona


class Autoridad_firmante(Persona):
    def __init__(self, apellido, nombre, dni, cuit_cuil, direccion, telefono, mail):
        super().__init__(apellido, nombre, dni, cuit_cuil, direccion, telefono, mail)

    def __str__(self):
        return super().__str__()
