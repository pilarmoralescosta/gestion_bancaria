from abc import ABC


class Usuario(ABC):

    def __init__(self, nro_usuario, clave):
        # segun el pdf tiene que ser el nro de dni el nombre de usuario
        self.nro_usuario = nro_usuario
        self.clave = clave

    def __str__(self):

        return("Tu nombre de usuario es {}".format(self.username))

