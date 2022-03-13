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
        while True:
            try:
                monto_a_depositar = float(
                    input("Ingrese el monto del depósito: "))
                self.saldo = self.saldo + monto_a_depositar
                print(
                    f'Se ha realizado el depósito, su nuevo saldo es: {self.saldo}')
            except ValueError:
                print("Debe ingresar un valor númerico")

    def realizar_transferencia(self):
        while True:
            try:
                input("Ingrese la cuenta a la que desea transferir: ")
                monto_a_transferir = float(
                    input("Ingrese el monto a transferir: "))
                if monto_a_transferir > self.saldo:
                    print("No hay saldo suficiente")
                else:
                    self.saldo = self.saldo - monto_a_transferir
                    print(
                        f'Transferencia realizada con éxito, su nuevo saldo es: {self.saldo}')
            except ValueError:
                print("Debe ingresar un valor numérico")

    def recibir_transferencia(self):
        while True:
            try:
                monto_transferencia = float(
                    input("Ingrese el monto de la transferencia a acreditar: "))
                self.saldo = self.saldo + monto_transferencia
                print(
                    f'Transferencia recibida con éxito, su nuevo saldo es: {self.saldo}')
            except ValueError:
                print("Debe ingresar un valor numérico")

    def pagar_en_linea(self):
        while True:
            try:
                monto_a_debitar = float(
                    input("Ingrese el monto a transferir: "))
                if monto_a_debitar > self.saldo:
                    print("No hay saldo suficiente")
                else:
                    self.saldo = self.saldo - monto_a_debitar
                    print(
                        f'Transferencia realizada con exito, su nuevo saldo es: {self.saldo}')
            except ValueError:
                print("Debe ingresar un valor numérico")

    def mostrar_saldo(self):
        print("El saldo de la cuenta es: ", self.saldo)
