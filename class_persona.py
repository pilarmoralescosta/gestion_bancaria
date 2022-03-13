# -*- coding: utf-8 -*-

from abc import ABC
from abc import abstractmethod
from class_usuario import Usuario


class Persona(ABC):

    def __init__(self, apellido, nombre, dni, cuit_cuil, direccion, telefono, mail):

        self.apellido = apellido
        self.nombre = nombre
        self.dni = dni
        self.cuit_cuil = cuit_cuil
        self.direccion = direccion
        self.telefono = telefono
        self.mail = mail

    def __str__(self):
        return f'\nApellido y nombre: {self.apellido}, {self.nombre} \nDNI: {self.dni} \nCUIT/CUITL: {self.cuit_cuil} \nDirección: {self.direccion} \nTelefono: {self.telefono} \nMail: {self.mail}'
