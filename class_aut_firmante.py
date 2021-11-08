from class_caja_ahorro import Caja_ahorro
from class_cta_cte import Cuenta_corriente
from class_persona import Persona
import random
import datetime


class Autoridad_firmante(Persona):
    def __init__(self, apellido, nombre, dni, cuit_cuil, direccion, telefono, mail):
        super().__init__(apellido, nombre, dni, cuit_cuil, direccion, telefono, mail)

    def cierre_cuenta(self, cuenta_a_borrar, cliente):
        
        cerrar_cuenta = input("Esta seguro que quiere cerrrar la cuenta?")
        if cerrar_cuenta == "si":
            clientes_pyme[cliente.id_cliente].cuentas.remove(cuenta_a_borrar)
        

    def apertura_cuenta(self, cliente_pyme):

        cuenta_a_abrir = int(input("Escriba 1 si quiere abrir una Caja de Ahorro, 2 si quiere abrir una Cuenta Corriente y 3 para salir"))
        sucursal = input("Elija la sucursal")
        nro_cuenta = random.int(12)
        cbu = random.int(15)
        fecha_apertura = datetime.date()
        saldo = 0
        saldo_retenido = False
        es_bonificada = True
        
        if cuenta_a_abrir == 1:
            tipo = "Caja de Ahorro"
            clientes_pyme[cliente_pyme.id_cliente].cuentas.append(Caja_ahorro(sucursal, nro_cuenta, cbu, fecha_apertura, saldo, tipo, saldo_retenido, es_bonificada))
        elif cuenta_a_abrir == 2:
            tipo = "Cuenta Corriente"
            clientes_pyme[cliente_pyme.id_cliente].cuentas.append(Cuenta_corriente(sucursal, nro_cuenta, cbu, fecha_apertura, saldo, tipo, saldo_retenido, es_bonificada))

        else:
            exit()
        


    def __str__(self):
        return super().__str__()



jaimito.apertura_cuenta(amanecer)