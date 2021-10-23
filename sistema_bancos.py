# -*- coding: utf-8 -*-
from estructura_costos import estructura_costos


class Banco():

    def __init__(self):

        self.tarifas = estructura_costos
        self.clientes = ''
        self.usuarios = ''

    def logueo(self):

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
                "Ingrese la opción: \n1: Iniciar sesión \n2: Cerrar sesión")

            try:
                if(int(opcionNro) == 1):
                    self.logueo()
                elif(int(opcionNro) == 2):
                    exit()
                else:
                    print("Opción incorrecta")
            except ValueError:
                print("La opción ingresada es inválida: escriba un numero entero")


# menu
banco = Banco()
banco.menu()
