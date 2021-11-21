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
        monto_a_depositar = float(input("Ingrese el monto del deposito: "))
        self.saldo = self.saldo + monto_a_depositar
        print("Se ha realizado el deposito, su nuevo saldo es: {}".format(self.saldo))

    def realizar_transferencia(self):
        cuenta_a_transferir = input(
            "Ingrese la cuenta a la que desea transferir: ")
        monto_a_transferir = float(input("Ingrese el monto a transferir: "))
        self.saldo = self.saldo - monto_a_transferir
        print("Transferencia realizada con exito, su nuevo saldo es: {}".format(self.saldo))

    def recibir_transferencia(self):
        monto_transferencia = float(
            input("Ingrese el monto de la transferencia a acreditar: "))
        self.saldo = self.saldo + monto_transferencia
        print("Transferencia recibida con exito, su nuevo saldo es: {}".format(self.saldo))

    def pagar_en_linea(self):
        monto_a_debitar = float(input("Ingrese el monto a transferir: "))
        self.saldo = self.saldo - monto_a_debitar
        print("Transferencia realizada con exito, su nuevo saldo es: {}".format(self.saldo))


# servicio = Servicio_financiero(1, 12, 123, 124, 12, "A", 1231)
# servicio.realizar_deposito()
