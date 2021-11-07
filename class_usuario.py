class Usuario():

    def __init__(self, usuario, clave, id_cliente, es_cliente_individuo, es_cliente_pyme, cuentas=[]):
        self.usuario = usuario  # usuario es el dni
        self.clave = clave
        self.id_cliente = id_cliente
        self.es_cliente_individuo = es_cliente_individuo
        self.es_cliente_pyme = es_cliente_pyme
        self.cuentas = cuentas

    def mostrar_tipo_cliente(self, es_cliente_individuo, es_cliente_pyme):
        if es_cliente_individuo == True and es_cliente_pyme == False:
            return 'Individuo'
        elif es_cliente_individuo == False and es_cliente_pyme == True:
            return 'PyME'
        else:
            return 'Individuo y PyME'

    def __str__(self):

        return f'\n Usuario: {self.usuario} \nClave: {self.clave} \nID Cliente: {self.id_cliente} \nTipo Cliente: {self.mostrar_tipo_cliente(self.es_cliente_individuo, self.es_cliente_pyme)}'
