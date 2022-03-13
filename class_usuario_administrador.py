# -*- coding: utf-8 -*-

from class_cliente_pyme import Cliente_pyme
from class_usuario import Usuario

from class_cliente_individuo import Cliente_individuo


class Usuario_administrador():

    def __init__(self):
        self.username = 'administrador'
        self.clave = '4dm1n1str4d0r'

    def monto_saldo_retenido(self, costos):
        '''Este método del administrador define el monto de saldo retenido y lo retorna'''

        while True:
            print('Seleccione una opción:')
            try:
                opcion_seleccionada = int(input('\n1: Caja ahorro con retención saldo'
                                                '\n2: Cuenta corriente común'
                                                '\n3: Cuenta corriente con retención saldo'
                                                '\n4: Menu Administrador\n'))

                if opcion_seleccionada == 1 or opcion_seleccionada == 2 or opcion_seleccionada == 3:
                    print(f'El monto a retener actual es $',
                          costos[opcion_seleccionada]['Monto saldo retenido'])
                    monto_saldo_retenido = float(
                        input('Ingrese el monto a retener: '))
                    costos[opcion_seleccionada]['Monto saldo retenido'] = monto_saldo_retenido
                    return print('El monto a retener se ha modificado a $',
                                 monto_saldo_retenido)
                elif opcion_seleccionada == 4:
                    return
                else:
                    print('Opción inválida')
            except ValueError:
                print('\nIngrese un valor válido\n')

    def monto_saldo_descubierto(self, costos):
        '''Este método del administrador define el monto de saldo descubierto y lo retorna'''

        while True:
            print('Seleccione una opción:')
            try:
                opcion_seleccionada = int(input('\n1: Cuenta corriente común'
                                                '\n2: Cuenta corriente con retención saldo'
                                                '\n3: Menu Administrador\n'))

                if opcion_seleccionada == 1 or opcion_seleccionada == 2:
                    print(f'El monto de descubierto actual es $',
                          costos[opcion_seleccionada+1]['Monto saldo descubierto'])
                    monto_saldo_descubierto = float(
                        input('Ingrese el monto de descubierto: '))
                    costos[opcion_seleccionada +
                           1]['Monto saldo descubierto'] = monto_saldo_descubierto
                    return print('El monto de descubierto se ha modificado a $',
                                 monto_saldo_descubierto)
                elif opcion_seleccionada == 3:
                    return
                else:
                    print('\nOpción inválida\n')
            except ValueError:
                print('\nIngrese un valor válido\n')

    # Este método le permite al administrador consultar los costos
    # de las transacciones según el tipo de cuenta
    def costos_transaccion(self, costos):
        '''Este método del administrador, recibe una lista con los costos de las transacciones
        y muestra aquellas traansacciones que tengan costos, con su correspondientes costos'''

        print('Seleccione una opción:')
        try:
            opcion_seleccionada = int(input('\n1: Caja ahorro común'
                                            '\n2: Caja ahorro con retención saldo'
                                            '\n3: Cuenta corriente común'
                                            '\n4: Cuenta corriente con retención saldo'
                                            '\n5: Menu Administrador\n'))
            # si la opción es 1, 2, 3 o 4, se muestra el costo de las transacciones
            # de acuerdo al tipo de cuenta
            if opcion_seleccionada in range(1, 5):
                # .items() retorna una lista con tuplas de llave, valor
                transacciones = (costos[opcion_seleccionada-1].items())
                # solo se muestran los costos de las transacciones, no los beneficios
                for transaccion in transacciones:
                    if transaccion[0].split(' ')[0] in ['Mantenimiento',
                                                        'Depósitos', 'Pagos', 'Transferencias']:
                        print(f'{transaccion[0]}: ${transaccion[1]}')
                print('\n')
            elif opcion_seleccionada == 5:
                return
            else:
                print('\nOpción inválida\n')
        except ValueError:
            print('\nIngrese una opcion válida\n')

    def beneficios_transaccion(self, costos):
        '''Este método del administrador,  recibe una lista con los costos de las transacciones
        y muestra aquellas transacciones que tengan porcentaje de beneficios,
        con su correspondientes porcentajes'''

        print('Seleccione una opción:')
        try:
            opcion_seleccionada = int(input('\n1: Cuenta corriente común'
                                            '\n2: Cuenta corriente con retención saldo'
                                            '\n3: Menu Administrador\n'))
            # si la opción es 1 o 2, se muestra el porcentaje de beneficio
            # de acuerdo al tipo de cuenta
            if opcion_seleccionada in range(1, 3):
                # .items() retorna una lista con tuplas de llave, valor
                transacciones = (costos[opcion_seleccionada+1].items())
                # solo se muestran los costos de las transacciones, no los beneficios
                for transaccion in transacciones:
                    if transaccion[0].split(' ')[0] in ['Plazos', 'Bonos']:
                        print(f'{transaccion[0]}: {transaccion[1]}%')
                print('\n')
            elif opcion_seleccionada == 3:
                return
            else:
                print('\nOpción inválida\n')
        except ValueError:
            print('\nIngrese una opcion válida\n')

    def registrar_cliente(self, clientes_individuo, clientes_pyme):
        '''Este método del administrador, recibe la lista de clientes individuales y pymes
        y verifica si el cliente ya existe o no y retorna True o False en consecuencia'''

        existe_cliente = False

        print('Cliente a registrar en el sistema')
        while True:
            try:
                id_cliente = input('Ingrese el ID del cliente: ')
                if id_cliente in clientes_individuo.keys() or id_cliente in clientes_pyme.keys():
                    if id_cliente in clientes_individuo.keys():
                        clientes_individuo[id_cliente].registrado = True
                        existe_cliente = True
                    else:
                        clientes_pyme[id_cliente].registrado = True
                        existe_cliente = True
                else:
                    print('\nEl cliente no existe en el sistema\n')
            except ValueError:
                print('\nEl ID ingresado no es válido\n')

        return existe_cliente

    def registrar_cuenta(self):
        pass


# TEST
admin = Usuario_administrador()

# ALTA USUARIO
# admin.alta_usuario(3, usuarios)
# for usuario in usuarios:
#     print(usuarios[usuario])

# ALTA CLIENTE INDIVIDUO
# admin.alta_cliente_ind_a_modificar(clientes_individuos)

# for cliente in clientes_individuos:
#     print(clientes_individuos[cliente].dni)
#     print(usuarios[usuario])

# ALTA CLIENTE PYME
# admin.alta_cliente_pyme(clientes_pyme)

# MODIFICAR CLIENTE
# MODIFICAR CLIENTE INDIVIDUO
# admin.modificar_cliente(32123, clientes_individuos, clientes_pyme)
