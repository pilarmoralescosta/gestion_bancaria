from abc import ABC
from abc import abstractmethod


class Servicio_financiero(ABC):
    def __init__(self, id_servicio, sucursal, nro_cuenta, cbu, fecha_apertura, saldo, tipo, saldo_retenido):
        self.id_servicio = id_servicio
        self.sucursal = sucursal
        self.nro_cuenta = nro_cuenta
        self.cbu = cbu
        self.fecha_apertura = fecha_apertura
        self.saldo = saldo
        self.tipo = tipo
        self.saldo_retenido = saldo_retenido

    @abstractmethod
    def __str__(self):
        return f'\nNro. Cuenta: {self.nro_cuenta} \nSucursal: {self.sucursal} \nCBU: {self.cbu} \nFecha apertura: {self.fecha_apertura} \nSaldo: {self.saldo} \nTipo: {self.tipo} \nSaldo retenido: {self.saldo_retenido}'

    @abstractmethod
    def realizar_deposito(self):
        pass

    @abstractmethod
    def realizar_transferencia(self):
        pass

    @abstractmethod
    def recibir_transferencia(self):
        pass

    @abstractmethod
    def pagar_en_linea(self):
        pass


servicio = Servicio_financiero(1, 12, 123, 124, 12, 50, "A", 1231)

print(servicio)
