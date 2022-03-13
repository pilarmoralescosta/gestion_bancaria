# -*- coding: utf-8 -*-

from class_usuario import Usuario
from class_cliente_individuo import Cliente_individuo
from class_cliente_pyme import Cliente_pyme
from class_aut_firmante import Autoridad_firmante
from class_usuario_administrador import Usuario_administrador



clientes_individuos = {
    "POB123" : Cliente_individuo("Boragini","Trinidad", 32521456, 2035214528, "San Martin 100", 24941546289, 
    "trini@bora.com", "POB123", [], False),
    "ILG412" : Cliente_individuo("Gronda", "Lucio",25487412, 20256321451, "Saavedra 42",
    114214587, "lucio@gronda.com", "ILG412", [], False),
    "IRO345": Cliente_individuo("Chimondeguy", "Javier", 36645929, 2032541562, "Uruguay 1200", 3625142513, "jchimon@abc.gob.ar", "IRO345", [], False)

} 


clientes_pyme = {"PY30": Cliente_pyme(
    "La Pirca", 125487458, "Belgrano 230", 2494561231, 'unmail', [3, 25], "PY30", [78, 79], False),
    "PY120" : Cliente_pyme("La Rural", 20514232, "San Martin 90", 2414512023, "ah@asd.com", [1,2], "PY120", [], False )
    }

usuarios = {
    1: Usuario(1, 12, 'IRO345', True, False),
    2: Usuario(2, 11, 'POB123', True, False),
    3: Usuario(3, 10, "PY120", False, True)
}

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
    'Plazos fijos porcentaje pago anual': 0.36,
    'Bonos': '',
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
    'Plazos fijos porcentaje pago anual': 0.36,
    'Bonos': '',
    'Pago de sueldos cuentas del banco': 0,
    'Pago de sueldos cuentas otros bancos': 4,
    'Monto saldo retenido': 0,
    'Monto saldo descubierto': 0,
}


estructura_costos = [caja_ahorro_comun, caja_ahorro_retencion_saldo,
                     cuenta_corriente_comun, cuenta_corriente_retencion_saldo]


class Banco():
    # Clase Banco, clase principal del sistema
    clientes_individuos = clientes_individuos
    clientes_pyme = clientes_pyme
    usuarios = usuarios
    costos = estructura_costos

    def __init__(self):
        self.administrador = Usuario_administrador()
        self.usuario_logueado = None

    def alta_usuario(self, dni, id_cliente):
        '''Método para dar de alta un usuario del sistema. Recive como parametro el dni del usuario y
        el id del cliente, actualiza el diccionario de usuarios y retorna un mensaje de confirmación'''

        es_cliente_ind = False
        es_cliente_pyme = False

        # verificamos que el cliente exista
        if int(dni) in self.usuarios:
            return print("El usuario ya existe")
        # si no existe, verificamos si es cliente individuo o cliente pyme
        else:
            clave = input("Ingrese una clave: ")
            tipo_cliente = input(
                "¿Es un cliente individuo o PyME? (i/p): ").lower()
            if tipo_cliente == "i":
                es_cliente_ind = True
            elif tipo_cliente == "p":
                es_cliente_pyme = True
            else:
                return print("Ingrese una opción válida")

            # creamos la instancia de Usuario
            nuevo_usuario = Usuario(
                dni, clave, id_cliente, es_cliente_ind, es_cliente_pyme)

            # actualizamos el diccionario de usuarios
            self.usuarios[dni] = nuevo_usuario

            return print(f'\nEl usuario ha sido generado exitosamente: ' + Usuario.__str__(nuevo_usuario))

    def alta_cliente_ind(self):
        '''Método para dar de alta un cliente individuo, actualiza el el diccionario de clientes individuos
        con el nuevo cliente y retorna un mensaje de éxito junto con el cliente creado'''

        dni = int(input("Número de documento del cliente: "))

        # verificamos que el cliente no exista
        for cliente in self.clientes_individuos:
            if self.clientes_individuos[cliente].dni == int(dni):
                return print("El cliente ya existe")

        # solicitamos al usuario los datos del cliente
        apellido = input("Apellido del cliente: ")
        nombre = input("Nombre del cliente: ")
        cuit_cuil = input("CUIT/CUIL del cliente: ")
        direccion = input("Dirección del cliente: ")
        telefono = input("Teléfono del cliente: ")
        mail = input("Email del cliente: ")
        # formato del id de cliente: ITB029 - I: cliente individuo T: primer caracter nombre B: primer caracter apellido 029: últimos 3 dígitos del dni
        id_cliente = f'I{apellido[0].upper()}{nombre[0].upper()}{dni[-3:]}'
        cuentas = []  # lista de cuentas del cliente

        # creamos la instancia de Cliente_individuo
        nuevo_cliente_ind = Cliente_individuo(
            apellido, nombre, dni, cuit_cuil, direccion, telefono, mail, id_cliente, cuentas)

        # actualiza el diccionario de clientes individuos
        self.clientes_individuos[id_cliente] = nuevo_cliente_ind

        # creamos la instancia de Usuario
        self.alta_usuario(dni, id_cliente, usuarios)

        return print(f'\nEl cliente ha sido generado exitosamente: ' + nuevo_cliente_ind.__str__)

    def alta_autoridad_firmante(self, id_cliente):
        '''Método para dar de alta una autoridad/firmante de una PyME, recibe el id de la PyME y el arreglo de usuarios
        del sistema, lo actualiza con el usuario creado y retorna la instancia de la autoridad/firmante creada'''

        print(f'\nAlta de autoridad/firmante')
        dni = input("Número de documento: ")

        # verificamos que la autoridad/firmante no exista
        for autoridad in self.clientes_pyme:
            if self.clientes_pyme[autoridad].dni == int(dni):
                return print("Autoridad firmante existente")

        # solicitamos al usuario los datos de la autoridad/firmante
        apellido = input("Apellido: ")
        nombre = input("Nombre: ")
        cuit_cuil = input("CUIT/CUIL: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        mail = input("Email: ")

        # creamos la instancia de Autoridad_firmante
        nueva_autoridad_firmante = Autoridad_firmante(
            apellido, nombre, dni, cuit_cuil, direccion, telefono, mail)

        # creamos la instancia de Usuario
        self.alta_usuario(dni, id_cliente)

        return nueva_autoridad_firmante

    def alta_cliente_pyme(self):
        '''Método para crear un cliente PyME, actualiza el diccionario de clientes PyME
        con el nuevo cliente y retorna un mensaje de éxito junto con el cliente creado'''

        cuit_cuil = input(
            "Número de CUIT/CUIL del cliente (sin guiones, sólo números): ")

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
            autoridad_firmante = self.alta_autoridad_firmante(
                id_cliente, usuarios)
            autoridades_firmantes.append(autoridad_firmante)
            agregar = input(
                "¿Desea agregar otra autoridad/firmante? (s/n)").lower()
            if agregar == "n":
                agregar_aut_firmante = False
            elif agregar == "s":
                agregar_aut_firmante = True
            else:
                print("Ingrese una opción válida")

        # creamos la instancia de Cliente_pyme
        nuevo_cliente_pyme = Cliente_pyme(
            razon_social, cuit_cuil, direccion, telefono, mail, autoridades_firmantes, id_cliente, cuentas)

        # actualizamos el diccionario de clientes PyME
        self.clientes_pyme[id_cliente] = nuevo_cliente_pyme

        return print(f'\nEl cliente ha sido generado exitosamente: ' + Cliente_pyme.__str__(nuevo_cliente_pyme))

    def menu_cuentas_usuario(self):
        
        while True:
            try:
                for num, cuenta in enumerate(self.usuario_logueado.cuentas):
                    print(num, cuenta)
                cuenta_seleccionada = int(input('Seleccione el numero de la cuenta que desea operar: )'))
                cuenta = self.usuario_logueado.cuentas[cuenta_seleccionada]
                opcion_seleccionada = int(input('Que desea hacer con la cuenta?"\n1: Consulta de Saldo\n2: Transferir a otra cuenta'
                '\n3: Depositar''\n4: Realizar plazo fijo''\n5: Comprar moneda extranjera'
                '\n6:Cerrar cuenta \n7: Salir\n'))

                if opcion_seleccionada == 1:
                    cuenta.mostrar_saldo()
                elif opcion_seleccionada == 2:
                    cuenta.realizar_transferencia()
                elif opcion_seleccionada == 3:
                    cuenta.realizar_deposito()
                elif opcion_seleccionada == 4:
                    cuenta.realizar_plazo_fijo()
                elif opcion_seleccionada == 5:
                    cuenta.comprar_moneda_extranjera()
                elif opcion_seleccionada == 6:
                    cuenta.cerrar_cuenta()
                elif opcion_seleccionada == 7:
                    self.usuario_logueado = None
                    self.menu()
            except ValueError:
                print("La opción ingresada es inválida: escriba un numero entero")

    def logueo_usuario(self):
        '''Este método se encarga de loguear al usuario, recibe el usuario.
        Retorna True si el usuario y la contraseña ingresados son correctos, False si no lo son.'''

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
                "El logueo fue incorrecto, opcion 1 para seguir probando, 2 para salir")
            if opcion == "1":
                self.iniciar_sesion_administrador()
            else:
                exit()

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
                    self.usuario_logueado.cierre_cuenta()
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

        while True:
            try:
                opcion_seleccionada = int(input(
                    'Ingrese la opción:'
                    '\n1: Monto de saldo retenido \n2: Monto de saldo descubierto'
                    '\n3: Costos de servicios para cada tipo de transacción'
                    '\n4: Porcentajes de beneficios para cada tipo de transacción'
                    '\n5: Registrar cliente \n6: Registro de cuentas de cliente'
                    '\n7: Cerrar sesión\n'))

                if opcion_seleccionada == 1:
                    self.administrador.monto_saldo_retenido(
                        self.costos)
                elif opcion_seleccionada == 2:
                    self.administrador.monto_saldo_descubierto(self.costos)
                elif opcion_seleccionada == 3:
                    self.administrador.costos_transaccion(self.costos)
                elif opcion_seleccionada == 4:
                    self.administrador.beneficios_transaccion(self.costos)
                elif opcion_seleccionada == 5:
                    self.administrador.registrar_cliente(
                        self.clientes_individuos, self.clientes_pyme)
                elif opcion_seleccionada == 6:
                    self.administrador.registrar_cuenta()
                elif(int(opcion_seleccionada) == 7):
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


# menu
banco = Banco()
banco.menu()
