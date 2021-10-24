# -*- coding: utf-8 -*-
from estructura_costos import estructura_costos
from todos_usuarios import usuarios
from todos_clientes import clientes
from class_usuario_administrador import Usuario_administrador


class Banco():

    def __init__(self):

        self.tarifas = estructura_costos
        self.clientes = clientes
        self.usuarios = usuarios

    def menu_administrador(self):
        pass

    def menu_usuario(self, nro_cliente):
        pass

    def logueo_administrador(self):

        nombre_usuario = input("Ingrese su nombre de usuario administrador")
        if nombre_usuario != Usuario_administrador.username:
            while nombre_usuario != Usuario_administrador.username:
                nombre_usuario = input(
                    "Usuario administrador inexistente vuelva a escribirlo")

        clave = input("Ingrese su clave: ")
        if clave != Usuario_administrador.clave:
            while clave != Usuario_administrador.clave:
                clave = input("Clave incorrecta vuelva a escribirla")
                if clave == Usuario_administrador.clave:
                    print("Bienvenido administrador")
                    return True
        else:
            print("Bienvenido administrador")
            return True

        return False

    def logueo_usuario(self):

        numero_usuario = input("Ingrese su numero de usuario")

        if numero_usuario in self.usuarios:
            usuario = self.usuarios[numero_usuario]
            clave = input("Ingrese su clave: ")

            if clave == usuario.clave:
                return self.clientes[usuario.nro_cliente]
            else:
                return input("Clave incorrecta vuelva a escribirla")
        else:

            return input("Usuario inexistente vuelva a escribirlo")

    def menu(self):
        ''' La funcion menu solicita al usuario que ingrese una de las opciones indicadas.
        Si la opción es correcta, se invoca a la función en cuestión, si la opción ingresada no es correcta se imprime un mensaje de error. Si elige la opción 2, se termina la ejecución del programa.'''

        while True:
            opcionNro = input(
                "Ingrese la opción: \n1: Iniciar sesión administrador \n2: Iniciar sesión usuario \n3: Cerrar sesión")

            try:
                if(int(opcionNro) == 1):
                    logueado = False
                    while logueado == False:
                        logueado = self.logueo_administrador()
                        # print(logueado)
                    self.menu_administrador()
                elif(int(opcionNro) == 2):
                    logueado = False
                    # while logueado == False:
                    #     nro_cliente = self.logueo_usuario()
                    #     if nro_cliente != -1:
                    #         logueado = True
                    #     print(logueado)
                    # # se le pasa por parámetro el nro del cliente que inició sesión
                    # self.menu_usuario(self, nro_cliente)
                elif(int(opcionNro) == 3):
                    exit()
                else:
                    print("Opción incorrecta")
            except ValueError:
                print("La opción ingresada es inválida: escriba un numero entero")


# menu
banco = Banco()
banco.menu()
