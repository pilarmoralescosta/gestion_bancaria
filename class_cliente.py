from abc import ABC


class Cliente(ABC):
    def __init__(self, id_cliente, cuentas, registrado=False):
        self.id_cliente = id_cliente
        self.cuentas = cuentas  # arreglo con las cuentas de este cliente
        # para que el administrador lo valide a True en el método correspondiente
        self.registrado = registrado

    def __str__(self):
        return f'\nID Cliente: {self.id_cliente} \nCuentas: {self.cuentas}'
