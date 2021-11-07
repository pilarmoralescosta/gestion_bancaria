# -*- coding: utf-8 -*-

from class_usuario import Usuario
from class_cliente_individuo import Cliente_individuo
from class_cliente_pyme import Cliente_pyme
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
        self.cliente_logueado = None

    def menu_administrador(self):
        pass

    def logueo_administrador(self):

        nombre_usuario = input("Ingrese su nombre de usuario administrador")
        if nombre_usuario != self.administrador.username:
            return False

        clave = input("Ingrese su clave: ")
        if clave != self.administrador.clave:
            return False
        else:
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

            return True

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

    def menu_usuario_cliente(self):

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
                "Ingrese la opción: \n1: Iniciar sesión administrador \n2: Iniciar sesión usuario \n3: Cerrar sesión")

            try:
                if(int(opcionNro) == 1):
                    self.iniciar_sesion_administrador()

                elif(int(opcionNro) == 2):
                    if self.logueo_usuario():
                        print("Inicio de sesion correcto")
                        self.menu_usuario_cliente()

                elif(int(opcionNro) == 3):
                    exit()
                else:
                    print("Opción incorrecta")
            except ValueError:
                print("La opción ingresada es inválida: escriba un numero entero")


# menu
banco = Banco()
banco.menu()
