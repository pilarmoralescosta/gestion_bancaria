# -*- coding: utf-8 -*-

from xmlrpc.client import FastUnmarshaller
from class_usuario import Usuario
from class_cliente_individuo import Cliente_individuo
from class_cliente_pyme import Cliente_pyme
from class_aut_firmante import Autoridad_firmante
from class_usuario_administrador import Usuario_administrador
import validaciones as val

import re

# ----------------DATOS DE TEST ----------------
clientes_individuos = {
    "POB123": Cliente_individuo("Boragini", "Trinidad", 32521456, 2035214528, "San Martin 100", 24941546289,
                                "trini@bora.com", "POB123", [], False),
    "ILG412": Cliente_individuo("Gronda", "Lucio", 25487412, 20256321451, "Saavedra 42",
                                114214587, "lucio@gronda.com", "ILG412", [], False),
    "IRO345": Cliente_individuo("Chimondeguy", "Javier", 36645929, 2032541562, "Uruguay 1200", 3625142513, "jchimon@abc.gob.ar", "IRO345", [6, 7], False)

}

aut_1 = Autoridad_firmante("Perez", "Juan", 25444666,
                           20254446661, "Rosales 48", 11111, "juan@mail.com")
aut_2 = Autoridad_firmante(
    "Gomez", "Mariana", 40888999, 27408889995, "Paz 1234", 333, "mariana@mail.com")

clientes_pyme = {
    "PY30": Cliente_pyme("La Pirca", 125487458, "Belgrano 230", 2494561231, 'unmail', [aut_1, aut_2], "PY30", [78, 79], False),
    "PY120": Cliente_pyme("La Rural", 20514232, "San Martin 90", 2414512023, "ah@asd.com", [], "PY120", [], False)
}

usuarios = {
    # 1 es el usuario, que es el dni del cliente (coinciden la clave del usuario con el atributo usuario del cliente)
    1: Usuario(1, 12, 'IRO345', True, False),
    2: Usuario(2, 11, 'POB123', True, False),
    3: Usuario(3, 10, "PY120", False, True)
}

# ----------------ESTRUCTURA DE COSTOS ----------------

caja_ahorro_comun = {
    'Mantenimiento mensual': 200,
    'Transferencias realizadas': 5,
    'Depósitos realizados': 5,
    'Pagos en línea': 3
}
caja_ahorro_retencion_saldo = {
    'Mantenimiento mensual': 0,
    'Transferencias realizadas': 0,
    'Depósitos realizados': 0,
    'Pagos en línea': 0,
    'Monto saldo retenido': 0,
}

cuenta_corriente_comun = {
    'Mantenimiento cuenta en pesos': 500,
    'Mantenimiento cuenta moneda extranjera': 800,
    'Transferencias realizadas': 5,
    'Depósitos realizados': 5,
    'Pagos en línea': 3,
    'Plazos fijos porcentaje pago anual': 36,
    'Bonos': 5,
    'Pago de sueldos cuentas del banco': 0,
    'Pago de sueldos cuentas otros bancos': 4,
    'Monto saldo descubierto': 0,
}

cuenta_corriente_retencion_saldo = {
    'Mantenimiento cuenta en pesos': 500,
    'Mantenimiento cuenta moneda extranjera': 800,
    'Transferencias realizadas': 0,
    'Depósitos realizados': 0,
    'Pagos en línea': 0,
    'Plazos fijos porcentaje pago anual': 36,
    'Bonos': 5,
    'Pago de sueldos cuentas del banco': 0,
    'Pago de sueldos cuentas otros bancos': 4,
    'Monto saldo retenido': 0,
    'Monto saldo descubierto': 0,
}

estructura_costos = [caja_ahorro_comun, caja_ahorro_retencion_saldo,
                     cuenta_corriente_comun, cuenta_corriente_retencion_saldo]

# -----------------------------------------------------


class Banco():
    # Clase Banco, clase principal del sistema
    clientes_individuos = clientes_individuos
    clientes_pyme = clientes_pyme
    usuarios = usuarios
    costos = estructura_costos

    def __init__(self):
        self.administrador = Usuario_administrador()
        self.usuario_logueado = None

    def existe_usuario(self, dni):
        '''Este método del Banco verifica si el usuario ingresado existe en el sistema
        recibe el usuario y retorna True o False dependiendo si existe o no en Usuarios'''

        existe_usuario = False

        try:
            if int(dni) in self.usuarios.keys():
                print("El usuario ya existe")
                existe_usuario = True
        except ValueError:
            print(
                "El usuario es el número de documento del cliente, debe ingresar números")

        return existe_usuario

    def alta_usuario(self, dni, id_cliente, tipo_cliente):
        '''Método para dar de alta un usuario del sistema. Recive como parametro el dni del usuario y
        el id del cliente, actualiza el diccionario de usuarios y retorna un mensaje de confirmación'''

        es_cliente_ind = False
        es_cliente_pyme = False

        # verificamos si el usuario ya existe
        existe_usuario = self.existe_usuario(dni)

        # si no existe, creamos la instancia de Usuario
        if existe_usuario == False:
            clave = input("Ingrese una clave: ")
            if tipo_cliente == "i":
                es_cliente_ind = True
            elif tipo_cliente == "p":
                es_cliente_pyme = True
            else:
                return print("Ingrese una opción válida")

            nuevo_usuario = Usuario(
                dni, clave, id_cliente, es_cliente_ind, es_cliente_pyme)

            # actualizamos el diccionario de usuarios
            self.usuarios[dni] = nuevo_usuario

            return print(f'\nEl usuario ha sido generado exitosamente: {Usuario.__str__(nuevo_usuario)}')

    def ingresar_dni(self):
        dni = input("Número de documento del cliente: ")
        dni_valid = val.validar_dni(dni)
        while dni_valid == None:
            print("Ingrese un número de documento válido")
            dni = input("Número de documento del cliente: ")
            dni_valid = val.validar_dni(dni)
        return dni

    def ingresar_cuit_cuil(self):
        cuit_cuil = input(
            "Número de CUIT/CUIL del cliente (sin guiones, sólo números): ")
        if '-' in cuit_cuil:
            cuit_cuil = cuit_cuil.replace('-', '')
        if '/' in cuit_cuil:
            cuit_cuil = cuit_cuil.replace('/', '')
        cuit_cuil_valid = val.validar_cuit_cuil(cuit_cuil)
        while cuit_cuil_valid == None:
            print("Ingrese un CUIT/CUIL válido")
            cuit_cuil = input(
                "Número de CUIT/CUIL del cliente (sin guiones, sólo números): ")
            cuit_cuil_valid = val.validar_cuit_cuil(cuit_cuil)
        return cuit_cuil

    def alta_cliente_ind(self):
        '''Método para dar de alta un cliente individuo, actualiza el el diccionario de clientes individuos
        con el nuevo cliente y retorna un mensaje de éxito junto con el cliente creado'''

        dni = self.ingresar_dni()

        # verificamos que el cliente no exista
        for cliente in self.clientes_individuos:
            if self.clientes_individuos[cliente].dni == int(dni):
                return print("El cliente ya existe")

        # solicitamos al usuario los datos del cliente
        apellido = input("Apellido del cliente: ")
        nombre = input("Nombre del cliente: ")
        cuit_cuil = self.ingresar_cuit_cuil()
        direccion = input("Dirección del cliente: ")
        telefono = input("Teléfono del cliente: ")
        mail = input("Email del cliente: ")
        # formato del id de cliente: ITB029 - I: cliente individuo T: primer caracter nombre B: primer caracter apellido 029: últimos 3 dígitos del dni
        id_cliente = f'I{apellido[0].upper()}{nombre[0].upper()}{dni[-3:]}'
        cuentas = []  # lista de cuentas del cliente
        registrado = False

        # creamos la instancia de Cliente_individuo
        nuevo_cliente_ind = Cliente_individuo(
            apellido, nombre, dni, cuit_cuil, direccion, telefono, mail, id_cliente, cuentas, registrado)

        # actualiza el diccionario de clientes individuos
        self.clientes_individuos[id_cliente] = nuevo_cliente_ind

        # creamos la instancia de Usuario
        self.alta_usuario(dni, id_cliente, "i")

        return print(f'\nEl cliente ha sido generado exitosamente: {nuevo_cliente_ind.__str__()}')

    def alta_autoridad_firmante(self, id_cliente):
        '''Método para dar de alta una autoridad/firmante de una PyME, recibe el id de la PyME y el arreglo de usuarios
        del sistema, lo actualiza con el usuario creado y retorna la instancia de la autoridad/firmante creada'''

        print(f'\nAlta de autoridad/firmante')
        dni = self.ingresar_dni()

        # verificamos que la autoridad/firmante no exista
        for cliente_pyme in self.clientes_pyme.values():
            for autoridad in cliente_pyme.autoridades_firmantes:
                if autoridad.dni == dni:
                    return print("Autoridad firmante existente")

        # solicitamos al usuario los datos de la autoridad/firmante
        apellido = input("Apellido: ")
        nombre = input("Nombre: ")
        cuit_cuil = self.ingresar_cuit_cuil()
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        mail = input("Email: ")

        # creamos la instancia de Autoridad_firmante
        nueva_autoridad_firmante = Autoridad_firmante(
            apellido, nombre, dni, cuit_cuil, direccion, telefono, mail)

        # creamos la instancia de Usuario
        self.alta_usuario(dni, id_cliente, "p")

        return nueva_autoridad_firmante

    def alta_cliente_pyme(self):
        '''Método para crear un cliente PyME, actualiza el diccionario de clientes PyME
        con el nuevo cliente y retorna un mensaje de éxito junto con el cliente creado'''

        cuit_cuil = self.ingresar_cuit_cuil()

        # verificamos que el cliente no exista
        for cliente in self.clientes_pyme:
            if self.clientes_pyme[cliente].cuit_cuil == cuit_cuil:
                return print("El cliente ya existe")

        # solicitamos al usuario los datos del cliente
        razon_social = input("Razón social del cliente: ")
        direccion = input("Dirección del cliente: ")
        telefono = input("Teléfono del cliente: ")
        mail = input("Email del cliente: ")

        # formato del id de cliente: PX1234 - P: cliente PyME X: primer caracter Razon Social 1234: últimos 4 dígitos del cuit
        id_cliente = f'P{razon_social[0].upper()}{cuit_cuil[-4:-2]}{cuit_cuil[-1]}'
        cuentas = []  # lista de cuentas del cliente

        # creamos la instancia de autoridad/es-firmante/s
        autoridades_firmantes = []
        agregar_aut_firmante = True
        while agregar_aut_firmante:
            autoridad_firmante = self.alta_autoridad_firmante(id_cliente)
            autoridades_firmantes.append(autoridad_firmante)
            agregar = input(
                "¿Desea agregar otra autoridad/firmante? (s/n)").lower()
            if agregar == "n":
                agregar_aut_firmante = False
            elif agregar == "s":
                agregar_aut_firmante = True
            else:
                print("Ingrese una opción válida")
        registrado = False
        # creamos la instancia de Cliente_pyme
        nuevo_cliente_pyme = Cliente_pyme(
            razon_social, cuit_cuil, direccion, telefono, mail, autoridades_firmantes, id_cliente, cuentas, registrado)

        # actualizamos el diccionario de clientes PyME
        self.clientes_pyme[id_cliente] = nuevo_cliente_pyme

        return print(f'\nEl cliente ha sido generado exitosamente: {Cliente_pyme.__str__(nuevo_cliente_pyme)}')

    def alta_cliente(self):
        '''Este método del Banco verifica el tipo de cliente a dar de alta y
        llama al método correspondiente para dar de alta el cliente individuo o pyme'''
        try:
            tipo_cliente = input(
                'Ingrese el tipo de cliente que desea dar de alta: Individuo o PyMe (i/p): ').lower()
            if tipo_cliente == "i":
                self.alta_cliente_ind()
            elif tipo_cliente == "p":
                self.alta_cliente_pyme()
            else:
                print('Opción inválida, debe ingresar "i" o "p"')
        except ValueError:
            print("Ingrese una opción válida")

    def baja_cliente(self, tipo_cliente):
        '''Este método elimina u cliente de la lista de clientes clientes_individuos
        o pyme, dependiendo del tipo de cliente pasado por parámetro'''

        id_cliente = input(
            "Ingrese el ID del cliente que desea dar de baja: ").upper()

        if tipo_cliente == "i":
            if id_cliente in self.clientes_individuos.keys():
                print(
                    f'\nEl cliente {id_cliente} ha sido dado de baja exitosamente')
            else:
                print(f'\nEl cliente no existe')
        else:
            if id_cliente in self.clientes_pyme.keys():
                del self.clientes_pyme[id]
                print(
                    f'\nEl cliente {id_cliente} ha sido dado de baja exitosamente')
            else:
                print(f'\nEl cliente no existe')

    def menu_cuentas_usuario(self):
        '''Este metodo del Banco muestra las transacciones disponibles para las
        cuentas del usuario y permite realizar una de ellas. Si el usuario no tiene
        ninguna cuenta, se le informa y se muestra el menú correspondiente'''
        while True:
            try:
                if self.usuario_logueado.cuentas == []:
                    print("Usted no tiene ninguna cuenta, debe crear una primero")
                    self.menu_usuario_cliente()
                for num, cuenta in enumerate(self.usuario_logueado.cuentas):
                    print("Presione:", num, "\nPara operar la cuenta: ", cuenta)
                try:
                    cuenta_seleccionada = int(
                        input('Seleccione la opción que corresponde a la cuenta con la que desea operar: '))
                    if cuenta_seleccionada < 0 or cuenta_seleccionada > len(self.usuario_logueado.cuentas):
                        print(
                            f'Opción inválida, debe ingresar un número de 0 a {len(self.usuario_logueado.cuentas)-1}')
                        self.menu_cuentas_usuario()
                    else:
                        cuenta = self.usuario_logueado.cuentas[cuenta_seleccionada]
                except ValueError:
                    print("Debe ingresar números enteros")
                    self.menu_cuentas_usuario()

                opcion_seleccionada = int(input(
                    '\n¿Que desea hacer con la cuenta?'
                    '\n1: Consulta de Saldo\n2: Transferir a otra cuenta'
                    '\n3: Depositar \n4: Realizar plazo fijo \n5: Comprar moneda extranjera'
                    '\n6:Cerrar cuenta \n7: Salir\n'))

                if opcion_seleccionada == 1:
                    cuenta.mostrar_saldo()
                    self.menu_cuentas_usuario()
                elif opcion_seleccionada == 2:
                    cuenta.realizar_transferencia()
                    self.menu_cuentas_usuario()
                elif opcion_seleccionada == 3:
                    cuenta.realizar_deposito()
                    self.menu_cuentas_usuario()
                elif opcion_seleccionada == 4:
                    cuenta.realizar_plazo_fijo()
                    self.menu_cuentas_usuario()
                elif opcion_seleccionada == 5:
                    cuenta.comprar_moneda_extranjera()
                    self.menu_cuentas_usuario()
                elif opcion_seleccionada == 6:
                    cuenta.cerrar_cuenta()
                    self.menu_cuentas_usuario()
                elif opcion_seleccionada == 7:
                    self.usuario_logueado = None
                    self.menu()
            except ValueError:
                print("La opción ingresada es inválida: escriba un numero entero")

    def logueo_usuario(self):
        '''Este método se encarga de loguear al usuario.
        Retorna True si el usuario y la contraseña ingresados son correctos,
        False si no lo son.'''

        numero_usuario = int(input("Ingrese su numero de usuario: "))

        # verificamos que el usuario ingresado exista
        if numero_usuario in self.usuarios:
            usuario = self.usuarios[numero_usuario]

            clave = int(input("Ingrese su clave: "))
            # veridficamos que la contraseña ingresada sea la correcta
            if clave == usuario.clave:
                if usuario.es_cliente_individuo:
                    self.usuario_logueado = self.clientes_individuos[usuario.id_cliente]
                    return True
                if usuario.es_cliente_pyme:
                    self.usuario_logueado = self.clientes_pyme[usuario.id_cliente]
                    return True

            else:
                return False
        else:
            return False

    def logueo_administrador(self):
        '''Este método se encarga de loguear al administrador, recibe el usuario administrador.
        Retorna True si el usuario y la contraseña ingresados son correctos, False si no lo son.'''

        # verificamos que el usuario ingresado sea el administrador
        nombre_usuario = input('Ingrese su nombre de usuario administrador: ')
        if nombre_usuario != self.administrador.username:
            return False

        # verificamos que la contraseña ingresada sea la correcta
        clave = input('Ingrese su clave: ')
        if clave != self.administrador.clave:
            return False

        return True

    def iniciar_sesion_administrador(self):
        '''Este método se encarga de iniciar sesión al administrador, realiza el logueo del administrador
        y si las credenciales son correctas, se invoca al método menu_administrador, si no, se informa
        al usuario y se vuelve a llamar al método'''

        if self.logueo_administrador():
            self.menu_administrador()
        else:
            opcion = input(
                "El logueo fue incorrecto, opcion 1 para seguir probando, 2 para volver al menú principal")
            if opcion == "1":
                self.iniciar_sesion_administrador()
            else:
                self.menu()

    def menu_usuario_cliente(self):
        '''Este método se encarga de mostrar el menú de opciones del usuario, Si la opción es correcta,
        se invoca al método en cuestión, si la opción ingresada no es correcta se imprime un mensaje de error.'''

        while True:
            try:
                opcion_seleccionada = int(input(
                    'Ingrese la opción: \n1: Apertura de cuenta corriente'
                    '\n2: Apertura de Caja de Ahorro \n3: Cierre de cuenta \n4: Operar con cuentas'
                    '\n5: Cerrar sesión\n'))

                if opcion_seleccionada == 1:
                    self.usuario_logueado.abrir_cuenta_corriente()
                elif opcion_seleccionada == 2:
                    self.usuario_logueado.abrir_caja_ahorro()
                elif opcion_seleccionada == 3:
                    self.usuario_logueado.cerrar_cuenta()
                elif opcion_seleccionada == 4:
                    self.menu_cuentas_usuario()
                elif opcion_seleccionada == 5:
                    self.usuario_logueado = None
                    self.menu()
                else:
                    print("Opción incorrecta")
            except ValueError:
                print("La opción ingresada es inválida: escriba un numero entero")

    def menu_administrador(self):
        '''Método para mostrar el menú de opciones del administrador, recibe el usuario administrador.
        Si la opción seleccionada es correcta, se invoca a la función en cuestión, si la opción ingresada no es correcta
        se imprime un mensaje de error. Si elige la opción 2, se termina la ejecución del programa.'''
        print("\nMENÚ ADMINISTRADOR:")
        while True:
            try:
                opcion_seleccionada = int(input(
                    '\nIngrese la opción:'
                    '\n1: Alta de cliente individuo \n2: Alta de cliente PyME'
                    '\n3: Monto de saldo retenido \n4: Monto de saldo descubierto'
                    '\n5: Costos de servicios para cada tipo de transacción'
                    '\n6: Porcentajes de beneficios para cada tipo de transacción'
                    '\n7: Registrar cliente \n8: Registro de cuentas de cliente'
                    '\n9: Baja de cliente individuo \n10: Baja de cliente PyME'
                    '\n11: Cerrar sesión\n'))

                if opcion_seleccionada == 1:
                    self.alta_cliente_ind()
                elif opcion_seleccionada == 2:
                    self.alta_cliente_pyme()
                elif opcion_seleccionada == 3:
                    self.administrador.monto_saldo_descubierto(self.costos)
                elif opcion_seleccionada == 4:
                    self.administrador.monto_saldo_descubierto(self.costos)
                elif opcion_seleccionada == 5:
                    self.administrador.costos_transaccion(self.costos)
                elif opcion_seleccionada == 6:
                    self.administrador.beneficios_transaccion(self.costos)
                elif opcion_seleccionada == 7:
                    existe_cliente = self.administrador.registrar_cliente(
                        self.clientes_individuos, self.clientes_pyme)
                    if existe_cliente == False:
                        self.alta_cliente()
                elif opcion_seleccionada == 8:
                    self.administrador.registrar_cuenta()
                elif opcion_seleccionada == 9:
                    self.baja_cliente("i")
                elif opcion_seleccionada == 10:
                    self.baja_cliente("p")
                elif(int(opcion_seleccionada) == 11):
                    self.menu()
                else:
                    print('\nOpción incorrecta\n')
            except ValueError:
                print('\nLa opción ingresada es inválida: escriba un numero entero\n')

    def menu(self):
        ''' La funcion menu solicita al usuario que ingrese una de las opciones indicadas.
        Si la opción es correcta, se invoca a la función en cuestión, si la opción ingresada no es correcta
        se imprime un mensaje de error. Si elige la opción 2, se termina la ejecución del programa.'''

        while True:
            opcion_seleccionada = input(
                'Ingrese la opción:'
                '\n1: Iniciar sesión administrador'
                '\n2: Iniciar sesión usuario'
                '\n3: Salir\n')

            try:
                if(int(opcion_seleccionada) == 1):
                    self.iniciar_sesion_administrador()
                elif(int(opcion_seleccionada) == 2):
                    if self.logueo_usuario():
                        print("Inicio de sesion correcto")
                        self.menu_usuario_cliente()
                elif(int(opcion_seleccionada) == 3):
                    exit()
                else:
                    print('\nOpción incorrecta\n')
            except ValueError:
                print('\nLa opción ingresada es inválida: escriba un numero entero\n')


# ----------------MENU PRINCIPAL ----------------
banco = Banco()
banco.menu()
