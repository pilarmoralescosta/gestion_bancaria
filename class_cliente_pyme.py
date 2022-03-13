from class_cliente import Cliente


class Cliente_pyme(Cliente):
    def __init__(self, razon_social, cuit_cuil, direccion, telefono, mail, autoridades_firmantes, id_cliente, cuentas, registrado):
        super().__init__(id_cliente, cuentas, registrado)
        self.razon_social = razon_social
        self.cuit_cuil = cuit_cuil
        self.direccion = direccion
        self.telefono = telefono
        self.mail = mail
        # autoridades_firmantes es un arreglo del tipo Persona
        self.autoridades_firmantes = autoridades_firmantes

    def mostrar_autoridades_firmantes(self, autoridades_firmantes):
        for i in range(len(self.autoridades_firmantes)):
            return f'Autoridad/firmante {i+1} {autoridades_firmantes[i].__str__()}'

    def __str__(self):
        return f'\nRazón Social {self.razon_social} \nCUIT/CUIL: {self.cuit_cuil} \nDirección: {self.direccion} \nTeléfono: {self.telefono} \nMail: {self.mail} \n{self.mostrar_autoridades_firmantes(self.autoridades_firmantes)}' + super().__str__()
