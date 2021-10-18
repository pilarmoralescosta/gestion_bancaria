from class_cta_cte import Cuenta_corriente


class Cuenta_corriente_pyme(Cuenta_corriente):

    def __init__(self, id_servicio, sucursal, nro_cuenta, cbu, fecha_apertura, saldo, tipo, saldo_retenido, moneda, descubierto):
        super().__init__(id_servicio, sucursal, nro_cuenta, cbu,
                         fecha_apertura, saldo, tipo, saldo_retenido, moneda)
        self.descubierto = descubierto

    def __str__(self):
        return super().__str__() + f'\nDescubierto: {self.descubierto}'

    def realizar_plazo_fijo(self):
        super().realizar_plazo_fijo()

    def comprar_moneda_extranjerada(self):
        super().comparar_moneda_extranjera()

    def invertir_bonos(self):
        pass

    def pagar_sueldos(self):
        pass
