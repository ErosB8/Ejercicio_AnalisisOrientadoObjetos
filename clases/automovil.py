''' 
from clases.vehiculo import Automovil
from abc import ABC, abstractmethod

class AutomovilNormal(Automovil):
    ruedas = 4  

    def __init__(self, color, marca, aceleracion, velocidad):
        super().__init__(color, marca, aceleracion, velocidad)  

    def mostrar_detalles(self):
        super().mostrar_detalles() 

    def conducir(self):
        print("Conduciendo por tierra 🚗.")
'''

from clases.vehiculo import Vehiculo

class Automovil(Vehiculo):
    ruedas = 4

    def __init__(self, año, modelo, marca, velocidad=0):
        super().__init__(año, modelo)
        self.marca = marca
        self.velocidad = velocidad

    def conducir(self):
        print(f"Conduciendo por tierra a {self.velocidad} km/h")
