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
                    print('Opción inválida')
            except ValueError:
                print('\nIngrese un valor válido\n')

    def costos_transaccion(self, costos):
        print('Seleccione una opción:')
        try:
            opcion_seleccionada = int(input('\n1: Caja ahorro común'
                                            '\n2: Caja ahorro con retención saldo'
                                            '\n3: Cuenta corriente común'
                                            '\n4: Cuenta corriente con retención saldo'
                                            '\n5: Menu Administrador\n'))
        except ValueError:
            print('\nIngrese una opcion valida\n')

    def beneficios_transaccion(self):
        pass

    def registrar_cliente(self):
        print('Cliente a registrar en el sistema: ')
        while True:
            tipo_cliente = input('\n1: Pyme\n2: Individuo\n')

            try:
                if tipo_cliente == '1':
                    pass
                elif tipo_cliente == '2':
                    pass
                else:
                    print('\nIngrese una opcion valida\n')
            except ValueError:
                print('\nIngrese una opcion valida\n')

    def registrar_cuenta(self):
        pass


# TEST
admin = Usuario_administrador()


usuarios = {
    1: Usuario(1, 12, 'IRO345', True, False),
    2: Usuario(2, 11, 'POB123', False, True)
}
clientes_individuos = {
    32521: Cliente_individuo("Boragini", "Trinidad", 32521456, 2035214528, "San Martin 100", 24941546289, 3, 32521, []),
    32123: Cliente_individuo("Gronda", "Lucio", 25487412, 25632145, "Saavedra 42", 4214587, 12, 32123, [])
}

clientes_pyme = {1: Cliente_pyme(
    "La Pirca", 125487458, "Belgrano 230", 2494561231, 'unmail', [3, 25], 1, [78, 79])}

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
