from abc import ABC


class Cliente(ABC):
    def __init__(self, id_cliente, cuentas):
        self.id_cliente = id_cliente
        self.cuentas = cuentas
