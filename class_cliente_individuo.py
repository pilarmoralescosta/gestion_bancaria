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
        if es_cliente_individuo == True and es_cliente_pyme == False:
            return 'Individuo'
        elif es_cliente_individuo == False and es_cliente_pyme == True:
            return 'PyME'
        else:
            return 'Individuo y PyME'

    

    def apertura_cuenta(self):
        pass

    def __str__(self):
        return Persona.__str__(self) + Cliente.__str__(self)
