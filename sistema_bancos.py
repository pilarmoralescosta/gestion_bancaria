from estructura_costos import estructura_costos

class Banco():

    def __init__():

        self.tarifas = estructura_costos
        self.clientes =
        self.usuarios = 


    def logueo(self):

        numero_usuario = input ("Ingrese su numero de usuario")
        
        if numero_usuario in self.usuarios:
            usuario = self.usuarios[numero_usuario]
            clave = input("Ingrese su clave: ")

            if clave == usuario.clave:
                return self.clientes[usuario.nro_cliente]
            else:
                return input("Clave incorrecta vuelva a escribirla")
        else:
            
            return input("Usuario inexistente vuelva a escribirlo")
