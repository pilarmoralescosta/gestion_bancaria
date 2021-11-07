class Usuario():

    def __init__(self, usuario, clave, es_cliente_individuo, es_cliente_pyme, cuentas):
        self.usuario = usuario  # usuario es el dni
        self.clave = clave
        self.es_cliente_individuo = es_cliente_individuo
        self.es_cliente_pyme = es_cliente_pyme
        self.cuentas = []

    def __str__(self):

        return("Tu nombre de usuario es {}".format(self.usuario))
