# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 17:31:06 2021

@author: alumno
"""

from abc import ABC


class Cliente(ABC):
    
    def __init__ (self, id_cliente, cuit_cuil, direccion, telefono, id_usuario):
        
        self.id_cliente = id_cliente
        self.cuit_cuil = cuit_cuil
        self.direccion = direccion
        self.telefono = telefono
        self.id_usuario = id_usuario
        