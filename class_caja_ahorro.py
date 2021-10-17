from class_servicio_financiero import Servicio_financiero


class Caja_ahorro(Servicio_financiero):
    def __init__(self):
        super().__init__()

    def realizar_deposito(self):
        super().realizar_deposito()

    def realizar_transferencia(self):
        super().realizar_transferencia()

    def recibir_transferencia(self):
        super().recibir_transferencia()

    def pagar_en_linea(self):
        super().pagar_en_linea()
