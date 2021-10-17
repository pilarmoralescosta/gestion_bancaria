from abc import ABC


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

    def __str__(self):
        return f'\nNro. Cuenta: {nro_cuenta} \nSucursal: {sucursal} \nCBU: {cbu} \nFecha apertura: {fecha_apertura} \nSaldo: {saldo} \nTipo: {tipo} \nSaldo retenido: {saldo_retenido}'

    @abc.abstractmethod
    def realizar_deposito(self):
        pass

    @abc.abstractmethod
    def realizar_transferencia(self):
        pass

    @abc.abstractmethod
    def recibir_transferencia(self):
        pass

    @abc.abstractmethod
    def pagar_en_linea(self):
        pass
