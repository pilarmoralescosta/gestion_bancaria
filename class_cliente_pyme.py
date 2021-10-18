from class_cliente import Cliente


class Cliente_pyme(Cliente):
    def __init__(self, id_cliente, razon_social, cuit_cuil, direccion, telefono, usuario, autoridades_firmantes):
        super().__init__(id_cliente, cuit_cuil, direccion, telefono, usuario)
        self.razon_social = razon_social
        # autoridades_firmantes seria un arreglo del tipo Cliente_individuo
        self.autoridades_firmantes = autoridades_firmantes

    def mostrar_autoridades_firmantess(self, autoridades_firmantes):
        for i in range(len(self.autoridades_firmantes)):
            return f'Autoridad/firmante {i+1} {autoridades_firmantes[i].__str__()}'

    def __str__(self):
        return super().__str__() + f'\nRazón Social {self.razon_social} \n{self.mostrar_autoridades_firmantess(self.autoridades_firmantes)}'
