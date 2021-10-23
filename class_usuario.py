from abc import ABC


class Usuario(ABC):

    def __init__(self, id, username, clave, nro_cliente):
        self.id = id
        # segun el pdf tiene que ser el nro de dni el nombre de usuario
        self.username = username
        self.clave = clave
        self.nro_cliente = nro_cliente

    def __str__(self):

        return("Tu nombre de usuario es {}".format(self.username))
