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

        abrir_cuenta = True

        while abrir_cuenta:

            sucursal = input("Ingrese el nombre de la sucursal")
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
        
        pass

    def mostrar_tipo_cliente(self, es_cliente_individuo, es_cliente_pyme):
        if es_cliente_individuo == True and es_cliente_pyme == False:
            return 'Individuo'
        elif es_cliente_individuo == False and es_cliente_pyme == True:
            return 'PyME'
        else:
            return 'Individuo y PyME'

    def cierre_cuenta(self):
        pass

    def apertura_cuenta(self):
        pass

    def __str__(self):
        return Persona.__str__(self) + Cliente.__str__(self)
