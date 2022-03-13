from abc import ABC
import random
from class_caja_ahorro import Caja_ahorro
from class_cta_cte import Cuenta_corriente
import datetime


class Cliente(ABC):
    def __init__(self, id_cliente, cuentas, registrado=False):
        self.id_cliente = id_cliente
        self.cuentas = cuentas  # arreglo con las cuentas de este cliente
        # para que el administrador lo valide a True en el método correspondiente
        self.registrado = registrado

    def abrir_cuenta_corriente(self):

        abrir_cuenta = True

        while abrir_cuenta:

            sucursal = input("Ingrese el nombre de la sucursal: ")
            nro_cuenta = random.randint(0, 10000000)
            cbu = random.randint(0, 10000000)
            fecha_apertura = datetime.date
            saldo = 0
            saldo_retenido = False
            tipo = "Cuenta corriente"
            cuenta = Cuenta_corriente(sucursal, nro_cuenta, cbu, fecha_apertura, saldo, tipo, saldo_retenido)
            self.cuentas.append(cuenta)
            print("Cuenta creada con exito")
            print("Sus cuentas son", self.cuentas)
            
            return True

    def abrir_caja_ahorro(self):

        abrir_cuenta = True

        while abrir_cuenta:

            sucursal = input("Ingrese el nombre de la sucursal: ")
            nro_cuenta = random.randint(0, 10000000)
            cbu = random.randint(0, 10000000)
            fecha_apertura = datetime.date
            saldo = 0
            saldo_retenido = False
            tipo = "Caja de ahorro"
            es_bonificada = True
            cuenta = Caja_ahorro(sucursal, nro_cuenta, cbu, fecha_apertura, saldo, tipo, saldo_retenido, es_bonificada)
            self.cuentas.append(cuenta)
            print("Cuenta creada con exito")
            print("Sus cuentas son", self.cuentas)
            
            return True
    
    def cerrar_cuenta(self):

        if self.cuentas == []:
            print("Usted no tiene ninguna cuenta abierta")
            return True

        for num, cuenta in enumerate(self.cuentas):
            print ("Si desea eliminar la siguente cuenta: ", cuenta, "\n\n\nPresione: ", num)
        cuenta_a_eliminar = int(input ("Cuenta que desea eliminar: "))
        self.cuentas.pop(cuenta_a_eliminar)
        print("Cuenta eliminada con exito. Sus cuentas ahora son: ", self.cuentas)

    def __str__(self):
        return f'\nID Cliente: {self.id_cliente} \nCuentas: {self.cuentas}'
