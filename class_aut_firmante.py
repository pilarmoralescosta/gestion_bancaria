from class_persona import Persona


class Autoridad_firmante(Persona):
    def __init__(self, dni, cuit_cuil, nombre, apellido, telefono, email):
        super.__init__(self, dni, cuit_cuil, nombre, apellido, telefono, email)

    def cierre_cuenta(self):
        pass

    def apertura_cuenta(self):
        pass

    def __str__(self):
        return super().__str__() + f'\nDni: {self.dni} \nApellido y nombre {self.apellido}, {self.nombre}'
