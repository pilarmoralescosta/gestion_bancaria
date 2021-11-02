from class_usuario import Usuario

class Usuario_cliente(Usuario):

    def __init__(self, id, usuario, cliente):

        super().__init__(id, usuario)
        self.cliente = cliente



