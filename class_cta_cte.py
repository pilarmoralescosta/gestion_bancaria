from class_servicio_financiero import Servicio_financiero


class Cuenta_corriente(Servicio_financiero):

    def __init__(self, sucursal, nro_cuenta, cbu, fecha_apertura, saldo, tipo, saldo_retenido, moneda=False, descubierto=False):
        super().__init__(sucursal, nro_cuenta,
                         cbu, fecha_apertura, saldo, tipo, saldo_retenido)
        self.moneda = moneda
        self.descubierto = descubierto

    def __str__(self):
        return f'Cuenta Corriente: \n' + super().__str__() + f'\nMoneda: {self.moneda}'

    def realizar_plazo_fijo(self):
        plazo = (input("Elija el plazo: 30, 60, 90"))
        monto = float(input("Elija el monto con el que quiera hacer el plazo fijo: "))


        if monto <= self.saldo:
            self.saldo = self.saldo - monto
            print("Plazo Fijo Realizado con Exito. En {} dias lo vera reflejado en su cuenta").format(plazo)

        else:
            print("El saldo es insuficiente, su saldo actual es {}").format(self.saldo)



    def comprar_moneda_extranjera(self, cotizacion):
        
        monto_a_comprar = int(input("Ingrese la cantidad de dolares a comprar"))
        if monto_a_comprar*cotizacion <= self.saldo:
            self.saldo = self.saldo - monto_a_comprar*cotizacion
            print ("Compra realizada con exito, se debitaron de su cuenta: {} pesos").format(str(monto_a_comprar*cotizacion))
        else:
            print("El saldo es insuficiente, su saldo actual es {}").format(self.saldo)