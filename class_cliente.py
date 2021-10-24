# -*- coding: utf-8 -*-

from abc import ABC
from abc import abstractmethod
from class_usuario import Usuario


class Cliente(ABC):

    def __init__(self, nro_cliente, cuit_cuil, direccion, telefono, usuario):

        self.nro_cliente = nro_cliente
        self.cuit_cuil = cuit_cuil
        self.direccion = direccion
        self.telefono = telefono
        self.usuario = usuario  # objeto del tipo Usuario

    @abstractmethod
    def __str__(self):
        return f'\nID cliente: {self.id_cliente} \nCUIT/CUITL: {self.cuit_cuil} \nDirección: {self.direccion} \nTelefono: {self.telefono} \n{self.usuario}'
