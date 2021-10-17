from class_servicio_financiero import Servicio_financiero


class Cuenta_corriente(Servicio_financiero):

    def __init__(self, id_servicio, sucursal, nro_cuenta, cbu, fecha_apertura, saldo, tipo, saldo_retenido, moneda):
        super().__init__(id_servicio, sucursal, nro_cuenta,
                         cbu, fecha_apertura, saldo, tipo, saldo_retenido)
        self.moneda = moneda

    def __str__(self):
        return f'Cuenta Corriente: \n' + super().__str__() + f'\nMoneda: {moneda}'

    def realizar_deposito(self):
        super().realizar_deposito()

    def realizar_transferencia(self):
        super().realizar_transferencia()

    def recibir_transferencia(self):
        super().recibir_transferencia()

    def pagar_en_linea(self):
        super().pagar_en_linea()

    def realizar_plazo_fijo(self):
        pass

    def comprar_moneda_extranjera(self):
        pass
