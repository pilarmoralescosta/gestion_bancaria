# -*- coding: utf-8 -*-

from class_usuario import Usuario
from class_cliente_individuo import Cliente_individuo
from class_cliente_pyme import Cliente_pyme
from class_aut_firmante import Autoridad_firmante
from class_usuario_administrador import Usuario_administrador


clientes_individuos = {32521: Cliente_individuo(32521456, "Trinidad", "Boragini", 2035214528, "San Martin 100", 24941546289, 3, 32521, []),
                       32123: Cliente_individuo(32123, 25487412, "Lucio", "Gronda", 25632145, "Saavedra 42", 4214587, 12, [])}
clientes_pyme = {1: Cliente_pyme(
    "La Pirca", 125487458, "Belgrano 230", 2494561231, 'unmail', [3, 25], 1, [78, 79])}

usuarios = {
    1: Usuario(1, 12, 'IRO345', True, False),
    2: Usuario(2, 11, 'POB123', False, True)
}


class Banco():
    clientes_individuos = clientes_individuos
    clientes_pyme = clientes_pyme
    usuarios = usuarios

    def __init__(self):
        self.administrador = Usuario_administrador()
        self.usuario_logueado = None

    def alta_usuario(self, dni, id_cliente, usuarios):
        es_cliente_ind = False
        es_cliente_pyme = False

        if int(dni) in usuarios:
            return print("El usuario ya existe")
        else:
            clave = input("Ingrese una clave: ")
            tipo_cliente = input(
                "¿Es un cliente individuo, PyME o ambos? (i/p/a): ").lower()
            if tipo_cliente == "i":
                es_cliente_ind = True
            elif tipo_cliente == "p":
                es_cliente_pyme = True
            elif tipo_cliente == "a":
                es_cliente_ind = True
                es_cliente_pyme = True
            else:
                return print("Ingrese una opción válida")
            nuevo_usuario = Usuario(
                dni, clave, id_cliente, es_cliente_ind, es_cliente_pyme)
            usuarios[dni] = nuevo_usuario
            return print(f'\nEl usuario ha sido generado exitosamente: ' + Usuario.__str__(nuevo_usuario))

    def alta_cliente_ind(self, clientes_individuos):
        dni = int(input("Número de documento del cliente: "))

        for cliente in clientes_individuos:
            if clientes_individuos[cliente].dni == int(dni):
                return print("El cliente ya existe")

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
        clientes_individuos[id_cliente] = nuevo_cliente_ind

        # creamos la instancia de Usuario
        self.alta_usuario(dni, id_cliente, usuarios)

        return print(f'\nEl cliente ha sido generado exitosamente: ' + nuevo_cliente_ind.__str__)

    def alta_autoridad_firmante(self, id_cliente, usuarios):
        print(f'\nAlta de autoridad/firmante')
        dni = input("Número de documento: ")

        for cliente in clientes_individuos:
            if clientes_individuos[cliente].dni == int(dni):
                return print("Autoridad firmante existente")

        apellido = input("Apellido: ")
        nombre = input("Nombre: ")
        cuit_cuil = input("CUIT/CUIL: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        mail = input("Email: ")
        nueva_autoridad_firmante = Autoridad_firmante(
            apellido, nombre, dni, cuit_cuil, direccion, telefono, mail)

        # creamos la instancia de Usuario
        self.alta_usuario(dni, id_cliente, usuarios)

        return nueva_autoridad_firmante

    def alta_cliente_pyme(self, clientes_pyme):
        cuit_cuil = input("Número de CUIT/CUIL del cliente: ")

        for cliente in clientes_individuos:
            if clientes_individuos[cliente].dni == cuit_cuil:
                return print("El cliente ya existe")

        razon_social = input("Razón social del cliente: ")
        direccion = input("Dirección del cliente: ")
        telefono = input("Teléfono del cliente: ")
        mail = input("Email del cliente: ")

        # formato del id de cliente: PX1234 - P: cliente PyME X: primer caracter Razon Social 1234: últimos 4 dígitos del cuit
        id_cliente = f'P{razon_social[0].upper()}{cuit_cuil[-4:-2]}{cuit_cuil[-1]}'
        cuentas = []  # lista de cuentas del cliente

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
        clientes_pyme[id_cliente] = nuevo_cliente_pyme
        return print(f'\nEl cliente ha sido generado exitosamente: ' + Cliente_pyme.__str__(nuevo_cliente_pyme))

    def modificar_cliente_ind(cliente_ind_a_modificar):
        print('Modificación de datos del cliente: ')
        cliente_ind_a_modificar.apellido = input("Apellido del cliente: ")
        cliente_ind_a_modificar.nombre = input("Nombre del cliente: ")
        cliente_ind_a_modificar.dni = int(
            input("Número de documento del cliente: "))
        cliente_ind_a_modificar.cuit_cuil = input("CUIT/CUIL del cliente: ")
        cliente_ind_a_modificar.direccion = input("Dirección del cliente: ")
        cliente_ind_a_modificar.telefono = input("Teléfono del cliente: ")
        cliente_ind_a_modificar.mail = input("Email del cliente: ")

        return print(f'\nLos datos del cliente han sido modificados exitosamente: ' + cliente_ind_a_modificar.__str__)

    def menu_administrador(self):
        while True:
            opcion_seleccionada = int(input(
                "Ingrese la opción: \n1: Monto de saldo retenido \n2: Monto de saldo descubierto \n3: Costos de servicios para cada tipo de transacción \n4: Porcentajes de beneficios para cada tipo de transacción \n5: Registrar cliente \n6: Registro de cuentas de cliente \n7: Cerrar sesión"))
            try:

                if opcion_seleccionada == 1:
                    self.administrador.monto_saldo_retenido()
                elif opcion_seleccionada == 2:
                    self.administrador.monto_saldo_descubierto()
                elif opcion_seleccionada == 3:
                    self.administrador.costos_transaccion()
                elif opcion_seleccionada == 4:
                    self.administrador.beneficios_transaccion()
                elif opcion_seleccionada == 5:
                    self.administrador.registrar_cliente()
                elif opcion_seleccionada == 6:
                    self.administrador.registrar_cuenta()
                elif(int(opcion_seleccionada) == 7):
                    self.menu()
                else:
                    print("Opción incorrecta")
            except ValueError:
                print("La opción ingresada es inválida: escriba un numero entero")

    def logueo_administrador(self):

        nombre_usuario = input("Ingrese su nombre de usuario administrador")
        if nombre_usuario != self.administrador.username:
            return False

        clave = input("Ingrese su clave: ")
        if clave != self.administrador.clave:
            return False

        return True

    def logueo_usuario(self):

        numero_usuario = input("Ingrese su numero de usuario")

        if numero_usuario in self.usuarios:
            usuario = self.usuarios[numero_usuario]
            clave = input("Ingrese su clave: ")

            if clave == usuario.clave:
                self.usuario_logueado = self.clientes[usuario.id_cliente]
                return True
            else:
                return False
        else:

            return False

    def iniciar_sesion_administrador(self):

        if self.logueo_administrador():
            self.menu_administrador()
        else:
            opcion = input(
                "El logueo fue incorrecto, opcion 1 para seguir probando, 2 para salir")
            if opcion == "1":
                self.iniciar_sesion_administrador()
            else:
                exit()

    def menu_cuentas_usuario():
        pass

    def menu_usuario_cliente_individuo(self):

        opcion_seleccionada = int(input(
            "Ingrese la opción: \n1: Apertura de cuenta \n2: Cierre de cuenta \n3: Operar con cuentas\n4: Cerrar sesión"))
        if opcion_seleccionada == 1:
            self.cliente_logueado.apertura_cuenta()

        elif opcion_seleccionada == 2:
            self.cliente_logueado.cierre_cuenta()

        elif opcion_seleccionada == 3:
            self.menu_cuentas_usuario()

    def menu(self):
        ''' La funcion menu solicita al usuario que ingrese una de las opciones indicadas.
        Si la opción es correcta, se invoca a la función en cuestión, si la opción ingresada no es correcta se imprime un mensaje de error. Si elige la opción 2, se termina la ejecución del programa.'''

        while True:
            opcionNro = input(
                "Ingrese la opción: \n1: Iniciar sesión administrador \n2: Iniciar sesión usuario individuo \n3: Iniciar sesión usuario PyME \n4: Cerrar sesión")

            try:
                if(int(opcionNro) == 1):
                    self.iniciar_sesion_administrador()

                elif(int(opcionNro) == 2):
                    if self.logueo_usuario():
                        print("Inicio de sesion correcto")
                        self.menu_usuario_cliente_individuo()

                elif(int(opcionNro) == 3):

                    if self.logueo_usuario():
                        print("Inicio de sesion correcto")
                        self.menu_usuario_cliente_pyme()

                elif(int(opcionNro) == 4):
                    exit()
                else:
                    print("Opción incorrecta")
            except ValueError:
                print("La opción ingresada es inválida: escriba un numero entero")


# menu
banco = Banco()
banco.menu()
