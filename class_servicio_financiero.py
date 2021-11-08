from abc import ABC


class Servicio_financiero(ABC):
    def __init__(self, sucursal, nro_cuenta, cbu, fecha_apertura, saldo, tipo, saldo_retenido):
        self.sucursal = sucursal
        self.nro_cuenta = nro_cuenta
        self.cbu = cbu
        self.fecha_apertura = fecha_apertura
        self.saldo = saldo
        self.tipo = tipo  # comun o retencion de saldo
        self.saldo_retenido = saldo_retenido

    def __str__(self):
        return f'\nNro. Cuenta: {self.nro_cuenta} \nSucursal: {self.sucursal} \nCBU: {self.cbu} \nFecha apertura: {self.fecha_apertura} \nSaldo: {self.saldo} \nTipo: {self.tipo} \nSaldo retenido: {self.saldo_retenido}'

    def realizar_deposito(self):
        pass

    def realizar_transferencia(self):
        pass

    def recibir_transferencia(self):
        pass

    def pagar_en_linea(self):
        pass


servicio = Servicio_financiero(1, 12, 123, 124, 12, "A", 1231)

print(servicio)
