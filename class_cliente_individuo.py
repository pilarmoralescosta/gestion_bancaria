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
