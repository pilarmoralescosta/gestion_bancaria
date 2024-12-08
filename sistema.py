# -*- coding: utf-8 -*-

from xmlrpc.client import FastUnmarshaller
from class_usuario import Usuario
from class_cliente_individuo import Cliente_individuo
from class_cliente_pyme import Cliente_pyme
from class_aut_firmante import Autoridad_firmante
from class_usuario_administrador import Usuario_administrador
import utilidades as utils

# ----------------DATOS DE TEST ----------------

# ----------------DATOS DE CLIENTES INDIVIDUOS ----------------
#apellido, nombre, dni, cuit_cuil, direccion, telefono, email, id_cliente, cuentas, registrado
# La key es el id_cliente
clientes_individuos = {
    "TB029": Cliente_individuo("Boragini", "Trinidad", 26489029, 272648902984528, "San Martin 100", 24941546289, "trini@bora.com", "TB029", [], False),
    "LG412": Cliente_individuo("Gronda", "Lucio", 25487412, 20256321451, "Saavedra 42", 114214587, "lucio@gronda.com", "LG412", [], False),
    "JC929": Cliente_individuo("Chimondeguy", "Javier", 36645929, 2032541562, "Uruguay 1200", 3625142513, "jchimon@abc.gob.ar", "JC929", [], False)
}

# ----------------DATOS DE AUTORIDADES FIRMANTES ----------------
#apellido, nombre, dni, cuit_cuil, direccion, telefono, mail
aut_1 = Autoridad_firmante("Perez", "Juan", 25444666, 20254446661, "Rosales 48", 11111, "juan@mail.com")
aut_2 = Autoridad_firmante("Gomez", "Mariana", 40888999, 27408889995, "Paz 1234", 333, "mariana@mail.com")


# ----------------DATOS DE CLIENTES PYME ----------------
# razon_social, cuit_cuil, direccion, telefono, mail, autoridades_firmantes, id_cliente, cuentas, registrado
# La key es el id_cliente
clientes_pyme = {
    "LP458": Cliente_pyme("La Pirca", 30125487458, "Belgrano 230", 2494561231, 'unmail', [aut_1, aut_2], "LP458", [78, 79], False),
    "JC929": Cliente_pyme("La Rural", 33235142325, "San Martin 90", 2414512023, "ah@asd.com", [], "JC929", [], False)
}

# ----------------DATOS DE USUARIOS ----------------
# usuario, clave, id_cliente, es_cliente_individuo, es_cliente_pyme, cuentas
# La key es el usuario
usuarios = {
    26489029: Usuario(26489029, 'usuario1', 'TB029', True, False),
    25487412: Usuario(25487412, 'usuario2', 'LG412', True, False),
    30125487458: Usuario(30125487458, 'usuario3', "LP458", False, True),
    33235142325: Usuario(33235142325, 'usuario4', 'LR232', False, True),
    36645929: Usuario(36645929, 'usuario5', 'JC929', True, True)
}

# ----------------COTIZACION MONEDA EXTRANJERA ----------------
cotizacion_moneda_extranjera = 120

# ----------------ESTRUCTURA DE COSTOS ----------------

# ----------------ESTRUCTURA DE COSTOS CAJA DE AHORRO ----------------
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
# ----------------ESTRUCTURA DE COSTOS CUENTA CORRIENTE ----------------
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

estructura_costos = [caja_ahorro_comun, caja_ahorro_retencion_saldo, cuenta_corriente_comun, cuenta_corriente_retencion_saldo]


# ----------------MENSAJES ----------------

mensajes = {
    'ingresar_opcion_valida' : 'Ingrese una opción válida',
    'ingresar_cuit_cuil_cliente':'Número de CUIT/CUIL del cliente (sin guiones, sólo números): ',
    'ingresar_cuit_cuil_autoridad':'Número de CUIT/CUIL de autoridad/firmante (sin guiones, sólo números): ',
    'value_error' : 'La opción ingresada es inválida: escriba un numero entero.\n',
    'opcion_incorrecta': '\nOpción incorrecta, vuelva a intentarlo.\n'
}

# -----------------------------------------------------

# Clase Banco, clase principal del sistema


class Banco():
    clientes_individuos = clientes_individuos
    clientes_pyme = clientes_pyme
    usuarios = usuarios
    costos = estructura_costos
    mensajes = mensajes

    # Metodo para imprimir el diccionario de clientes individuos (solo para desarrollo)
    def listar_clientes_individuos(self):
        for cliente in self.clientes_individuos:
            print(self.clientes_individuos[cliente])
            print("\n")

    # Metodo para imprimir el diccionario de clientes pyme (solo para desarrollo)
    def listar_clientes_pyme(self):
        for cliente in self.clientes_pyme:
            print(self.clientes_pyme[cliente])
            print("\n")
    
    # Metodo para imprimir el diccionario de usuarios (solo para desarrollo)
    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(self.usuarios[usuario])
            print("\n")

    # Metodo para imprimir los diccionarios (solo para desarrollo)
    def listar_datos(self):
        self.listar_clientes_individuos()
        self.listar_clientes_pyme()
        self.listar_usuarios()

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
            clave = utils.validar_clave()
            if tipo_cliente == "i":
                es_cliente_ind = True
            elif tipo_cliente == "p":
                es_cliente_pyme = True
            else:
                return print(self.mensajes['ingresar_opcion_valida'])

            nuevo_usuario = Usuario(
                dni, clave, id_cliente, es_cliente_ind, es_cliente_pyme)

            # actualizamos el diccionario de usuarios
            self.usuarios[dni] = nuevo_usuario

            return print(f'\nEl usuario ha sido generado exitosamente: {Usuario.__str__(nuevo_usuario)}')

    def alta_cliente_ind(self):
        '''Método para dar de alta un cliente individuo, actualiza el el diccionario de clientes individuos
        con el nuevo cliente y retorna un mensaje de éxito junto con el cliente creado'''

        dni = utils.validar_dni(input("Número de documento del cliente: "))

        # verificamos que el cliente no exista
        for cliente in self.clientes_individuos:
            if self.clientes_individuos[cliente].dni == int(dni):
                return print("El cliente ya existe")

        # solicitamos al usuario los datos del cliente
        apellido = utils.validar_texto("Apellido del cliente")
        nombre = utils.validar_texto("Nombre del cliente: ")
        cuit_cuil = utils.validar_cuit_cuil(input(self.mensajes['ingresar_cuit_cuil_cliente']))
        direccion = utils.validar_direccion()
        telefono = utils.validar_telefono()
        mail = utils.validar_email()
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
        dni = utils.validar_dni(input("Número de documento del cliente: "))

        # verificamos que la autoridad/firmante no exista
        for cliente_pyme in self.clientes_pyme.values():
            for autoridad in cliente_pyme.autoridades_firmantes:
                if autoridad.dni == int(dni): #no se validaba nunca porque faltaba el int
                    print("Autoridad firmante existente") # modificacion se retorna None si ya existe el dni
                    return None

        # solicitamos al usuario los datos de la autoridad/firmante
        apellido = utils.validar_texto("Apellido del cliente")
        nombre = utils.validar_texto("Nombre del cliente: ")
        cuit_cuil = utils.validar_cuit_cuil(input(self.mensajes['ingresar_cuit_cuil_autoridad']))
        direccion = utils.validar_direccion()
        telefono = utils.validar_telefono()
        mail = utils.validar_email()

        # creamos la instancia de Autoridad_firmante
        nueva_autoridad_firmante = Autoridad_firmante(
            apellido, nombre, dni, cuit_cuil, direccion, telefono, mail)

        # creamos la instancia de Usuario
        self.alta_usuario(dni, id_cliente, "p")

        return nueva_autoridad_firmante

    def alta_cliente_pyme(self):
        '''Método para crear un cliente PyME, actualiza el diccionario de clientes PyME
        con el nuevo cliente y retorna un mensaje de éxito junto con el cliente creado'''

        cuit_cuil = utils.validar_cuit_cuil(input(self.mensajes['ingresar_cuit_cuil_cliente']))

        # verificamos que el cliente no exista
        for cliente in self.clientes_pyme:
            if self.clientes_pyme[cliente].cuit_cuil == int(cuit_cuil):#no coincidia nunca, faltaba convertir a int
                return print(f'El cliente ya existe:\n{self.clientes_pyme[cliente].__str__()}')

        # solicitamos al usuario los datos del cliente
        razon_social = utils.validar_texto("Razón social del cliente: ")
        direccion = utils.validar_direccion()
        telefono = utils.validar_telefono()
        mail = utils.validar_email()

        # formato del id de cliente: PX1234 - P: cliente PyME X: primer caracter Razon Social 1234: últimos 4 dígitos del cuit
        id_cliente = f'P{razon_social[0].upper()}{cuit_cuil[-4:-2]}{cuit_cuil[-1]}'
        cuentas = []  # lista de cuentas del cliente

        # creamos la instancia de autoridad/es-firmante/s
        autoridades_firmantes = []
        agregar_aut_firmante = True
        while agregar_aut_firmante:
            autoridad_firmante = self.alta_autoridad_firmante(id_cliente)
            if autoridad_firmante is not None: # se agrega esta condicion por si ya existe la autoridad, asi no se agrega
                autoridades_firmantes.append(autoridad_firmante)
            agregar = input(
                "¿Desea agregar otra autoridad/firmante? (s/n)").lower()
            if agregar == "n" or agregar == "no":
                agregar_aut_firmante = False
            elif agregar == "s" or agregar == "si":
                agregar_aut_firmante = True
            else:
                print(self.mensajes['ingresar_opcion_valida'])
                agregar_aut_firmante = False
        registrado = False
        # creamos la instancia de Cliente_pyme
        nuevo_cliente_pyme = Cliente_pyme(
            razon_social, cuit_cuil, direccion, telefono, mail, autoridades_firmantes, id_cliente, cuentas, registrado)

        # actualizamos el diccionario de clientes PyME
        self.clientes_pyme[id_cliente] = nuevo_cliente_pyme

        return print(f'\nEl cliente ha sido generado exitosamente: {Cliente_pyme.__str__(nuevo_cliente_pyme)}\n')

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
            print(self.mensajes['ingresar_opcion_valida'])

    def baja_cliente(self, tipo_cliente):
        '''Este método elimina un cliente de la lista de clientes clientes_individuos
        o pyme, dependiendo del tipo de cliente pasado por parámetro'''

        id_cliente = input(
            "Ingrese el ID del cliente que desea dar de baja: ").upper()
        
        if tipo_cliente == "i":
            if id_cliente in self.clientes_individuos.keys():
                cliente = self.clientes_individuos[id_cliente] #todo recuperar cliente
                del self.clientes_individuos[id_cliente] #TODO SE AGREGO PORQUE NO SE ELIMINABA DEL DICCIONARIO
                del self.usuarios[cliente.dni] #TODO SE AGREGO PORQUE NO SE ELIMINABA DEL DICCIONARIO
                print(
                    f'\nEl cliente Individuo {id_cliente} ha sido dado de baja exitosamente')
            else:
                print(f'\nEl cliente no existe')
        else:
            if id_cliente in self.clientes_pyme.keys():
                cliente_pyme = self.clientes_pyme[id_cliente] #todo recuperar cliente
                del self.clientes_pyme[id_cliente]
                del self.usuarios[cliente_pyme.cuit_cuil] #TODO SE AGREGO PORQUE NO SE ELIMINABA DEL DICCIONARIO
                print(
                    f'\nEl cliente PyME {id_cliente} ha sido dado de baja exitosamente')
            else:
                print(f'\nEl cliente no existe')

    def menu_cuentas_usuario(self):
        '''Este método del Banco muestra las transacciones disponibles para las
        cuentas del usuario y permite realizar una de ellas. Si el usuario no tiene
        ninguna cuenta, se le informa y se muestra el menú correspondiente'''
        while True:
            try:
                if self.usuario_logueado.cuentas == []:
                    print("Usted no tiene ninguna cuenta, debe crear una primero")
                    self.menu_usuario_cliente()
                for num, cuenta in enumerate(self.usuario_logueado.cuentas):
                    print(f'\nPresione {num} para operar la cuenta {cuenta}')
                try:
                    cuenta_seleccionada = int(
                        input('\nSeleccione la opción que corresponde a la cuenta con la que desea operar: '))
                    if cuenta_seleccionada < 0 or cuenta_seleccionada > len(self.usuario_logueado.cuentas):
                        print(
                            f'Opción inválida, debe ingresar un número de 0 a {len(self.usuario_logueado.cuentas)-1}')
                        self.menu_cuentas_usuario()
                    else:
                        cuenta = self.usuario_logueado.cuentas[cuenta_seleccionada]
                except ValueError:
                    print(self.mensajes['value_error'])
                    self.menu_cuentas_usuario()

                opcion_seleccionada = int(input(
                    '\n¿Que desea hacer con la cuenta?'
                    '\n1: Consulta de Saldo\n2: Transferir a otra cuenta'
                    '\n3: Depositar \n4: Realizar plazo fijo \n5: Comprar moneda extranjera'
                    '\n6: Salir\n'))

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
                    cuenta.comprar_moneda_extranjera(
                        cotizacion_moneda_extranjera)
                    self.menu_cuentas_usuario()
                elif opcion_seleccionada == 6:
                    self.usuario_logueado = None
                    self.menu()
            except ValueError:
                print(self.mensajes['value_error'])

    def logueo_usuario(self):
        '''Este método se encarga de loguear al usuario.
        Retorna True si el usuario y la contraseña ingresados son correctos,
        False si no lo son.'''

        numero_usuario = int(input("Ingrese su numero de usuario: "))

        # verificamos que el usuario ingresado exista
        if numero_usuario in self.usuarios:
            usuario = self.usuarios[numero_usuario]

            clave = input("Ingrese su clave: ") #TODO SE MODIFICO PORQUE LA CLAVE NO ES UN INT
            # veridficamos que la contraseña ingresada sea la correcta
            if usuario.es_cliente_individuo and usuario.es_cliente_pyme:
                ingreso = input(
                    "Desea ingresar como pyme o como individuo (p/i)")
                if ingreso == "p":
                    self.usuario_logueado = self.clientes_pyme[usuario.id_cliente]
                    return True
                elif ingreso == "i":
                    self.usuario_logueado = self.clientes_individuos[usuario.id_cliente]
                    return True
            if clave == usuario.clave:
                if usuario.es_cliente_individuo:
                    self.usuario_logueado = self.clientes_individuos[usuario.id_cliente]
                    return True
                if usuario.es_cliente_pyme:
                    self.usuario_logueado = self.clientes_pyme[usuario.id_cliente]
                    return True

            else:
                print("Clave incorrecta.\n")
                self.logueo_usuario() #TODO SE MODIFICO PARA QUE NO SALGA DEL MENU LOGUEO USUARIO
                return False
        else:
            print("El usuario no existe.\n")
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
            try:
                opcion = input(
                    "El logueo fue incorrecto, opción 1 para seguir probando, 2 para volver al menú principal\n")
                if opcion == "1":
                    self.iniciar_sesion_administrador()
                elif opcion == "2":
                    self.menu()
                else:
                    print(self.mensajes['opcion_incorrecta'])
                    self.menu()
            except ValueError:
                print(self.mensajes['value_error'])

    def menu_usuario_cliente(self):
        '''Este método se encarga de mostrar el menú de opciones del usuario, Si la opción es correcta,
        se invoca al método en cuestión, si la opción ingresada no es correcta se imprime un mensaje de error.'''

        while True:
            try:
                opcion_seleccionada = int(input(
                    '\nIngrese la opción: \n1: Apertura de cuenta corriente'
                    '\n2: Apertura de Caja de Ahorro \n3: Cierre de cuenta \n4: Operar con cuentas'
                    '\n5: Ver Cuentas \n6: Cerrar sesión\n'))

                if opcion_seleccionada == 1:
                    self.usuario_logueado.abrir_cuenta_corriente()
                elif opcion_seleccionada == 2:
                    self.usuario_logueado.abrir_caja_ahorro()
                elif opcion_seleccionada == 3:
                    self.usuario_logueado.cerrar_cuenta()
                elif opcion_seleccionada == 4:
                    self.menu_cuentas_usuario()
                elif opcion_seleccionada == 5:
                    self.usuario_logueado.mostrar_cuentas(
                        self.usuario_logueado.cuentas)
                elif opcion_seleccionada == 6:
                    self.usuario_logueado = None
                    self.menu()
                else:
                    print(self.mensajes['opcion_incorrecta'])
            except ValueError:
                print(self.mensajes['value_error'])

    def menu_administrador(self):
        '''Método para mostrar el menú de opciones del administrador, recibe el usuario administrador.
        Si la opción seleccionada es correcta, se invoca a la función en cuestión, si la opción ingresada no es correcta
        se imprime un mensaje de error.'''
        print("\nMENÚ ADMINISTRADOR:")
        while True:
            try:
                opcion_seleccionada = int(input(
                    '\nIngrese la opción:\n'
                    '\n1: Alta de cliente individuo \n2: Alta de cliente PyME'
                    '\n3: Monto de saldo retenido \n4: Monto de saldo descubierto'
                    '\n5: Costos de servicios para cada tipo de transacción'
                    '\n6: Porcentajes de beneficios para cada tipo de transacción'
                    '\n7: Registrar cliente'
                    '\n8: Baja de cliente individuo \n9: Baja de cliente PyME'
                    '\n10: Cerrar sesión\n\n'))

                if opcion_seleccionada == 1:
                    self.alta_cliente_ind()
                elif opcion_seleccionada == 2:
                    self.alta_cliente_pyme()
                elif opcion_seleccionada == 3:
                    self.administrador.monto_saldo_descubierto_retenido(self.costos, 'retenido')#se modifica a saldo retenido_descubierto ya que se  unifican los metodos por tener la misma funcion
                elif opcion_seleccionada == 4:
                    self.administrador.monto_saldo_descubierto_retenido(self.costos, 'descubierto')
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
                    self.baja_cliente("i")
                elif opcion_seleccionada == 9:
                    self.baja_cliente("p")
                elif(int(opcion_seleccionada) == 10):
                    self.menu()
                else:
                    print(self.mensajes['opcion_incorrecta'])
            except ValueError:
                print(self.mensajes['value_error'])

    def menu(self):
        ''' La funcion menu solicita al usuario que ingrese una de las opciones indicadas.
        Si la opción es correcta, se invoca a la función en cuestión, si la opción ingresada no es correcta
        se imprime un mensaje de error. Si elige la opción 2, se termina la ejecución del programa.'''

        while True:
            opcion_seleccionada = input(
                'Ingrese la opción:'
                '\n1: Iniciar sesión administrador'
                '\n2: Iniciar sesión usuario'
                '\n3: Salir\n\n')

            try:
                if(int(opcion_seleccionada) == 1):
                    self.iniciar_sesion_administrador()
                elif(int(opcion_seleccionada) == 2):
                    if self.logueo_usuario():
                        print(f'\nInicio de sesion correcto.\nBienvenido, {self.usuario_logueado.nombre}\n')
                        self.menu_usuario_cliente()
                elif(int(opcion_seleccionada) == 3):
                    exit()
                else:
                    print(self.mensajes['opcion_incorrecta'])
            except ValueError:
                print(self.mensajes['value_error'])


# ----------------MENU PRINCIPAL ----------------
banco = Banco()
#banco.listar_datos() # Solo para desarrollo
banco.menu()
