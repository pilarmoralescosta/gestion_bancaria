from class_servicio_financiero import Servicio_financiero


class Caja_ahorro(Servicio_financiero):
    def __init__(self, sucursal, nro_cuenta, cbu, fecha_apertura, saldo, tipo, saldo_retenido, es_bonificada):
        super().__init__(sucursal, nro_cuenta, cbu,
                         fecha_apertura, saldo, tipo, saldo_retenido)
        self.es_bonificada = es_bonificada

    def __str__(self):
        return f'Caja de ahorro: \n' + super().__str__()

    def realizar_deposito(self):
        super().realizar_deposito()

    def realizar_transferencia(self):
        super().realizar_transferencia()

    def recibir_transferencia(self):
        super().recibir_transferencia()

    def pagar_en_linea(self):
        super().pagar_en_linea()
