from class_caja_ahorro import Caja_ahorro
from class_persona import Persona
from class_cliente import Cliente
from class_cta_cte import Cuenta_corriente
import random
import datetime


class Cliente_individuo(Persona, Cliente):
    def __init__(self, apellido, nombre, dni, cuit_cuil, direccion, telefono, email, id_cliente, cuentas, registrado):
        Persona.__init__(self, apellido, nombre, dni, cuit_cuil,
                         direccion, telefono, email)
        Cliente.__init__(self, id_cliente, cuentas, registrado)

    def abrir_cuenta_corriente(self):
        '''Este método de Cliente_individuo permite al usuario abrir una cuenta corriente'''
        abrir_cuenta = True

        while abrir_cuenta:

            sucursal = input("Ingrese el nombre de la sucursal: ")
            nro_cuenta = random.randint(0, 10000000)
            cbu = random.randint(0, 10000000)
            fecha_apertura = datetime.date
            saldo = 0
            saldo_retenido = False
            tipo = "Cuenta corriente"
            cuenta = Cuenta_corriente(
                sucursal, nro_cuenta, cbu, fecha_apertura, saldo, tipo, saldo_retenido)
            self.cuentas.append(cuenta)
            print("Cuenta creada con exito")
            print("Sus cuentas son", self.cuentas)

            return True

    def abrir_caja_ahorro(self):
        '''Este método de Cliente_individuo permite al usuario abrir una caja de ahorro'''
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
            cuenta = Caja_ahorro(sucursal, nro_cuenta, cbu, fecha_apertura,
                                 saldo, tipo, saldo_retenido, es_bonificada)
            self.cuentas.append(cuenta)
            print("Cuenta creada con exito")
            print("Sus cuentas son", self.cuentas)

            return True

    def mostrar_tipo_cliente(self, es_cliente_individuo, es_cliente_pyme):
        '''Este método de Cliente_individuo muestra el tipo de cliente, individuo o PyME'''
        if es_cliente_individuo == True and es_cliente_pyme == False:
            return 'Individuo'
        elif es_cliente_individuo == False and es_cliente_pyme == True:
            return 'PyME'
        else:
            return 'Individuo y PyME'

    def cerrar_cuenta(self):
        '''Este método de Cliente_individuo permite al usuario cerrar una cuenta'''
        if self.cuentas == []:
            print("Usted no tiene ninguna cuenta abierta")
            return True

        for num, cuenta in enumerate(self.cuentas):
            print("Si desea eliminar la siguente cuenta: ",
                  cuenta, "\n\n\nPresione: ", num)
        while True:
            try:
                cuenta_a_eliminar = int(input("Cuenta que desea eliminar: "))
                if cuenta_a_eliminar < 0 or cuenta_a_eliminar > len(self.cuentas):
                    print(
                        f'Opción inválida, debe ingresar un número de 0 a {len(self.cuentas)-1}')
                    self.cerrar_cuenta()
                else:
                    self.cuentas.pop(cuenta_a_eliminar)
                    print(
                        "Cuenta eliminada con exito. Sus cuentas ahora son: ", self.cuentas)
            except ValueError:
                print("Debe ingresar números enteros")

    def __str__(self):
        return Persona.__str__(self) + Cliente.__str__(self)
