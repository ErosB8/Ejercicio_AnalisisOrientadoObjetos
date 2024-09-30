from automovil import Automovil
from abc import ABC, abstractmethod

class AutomovilNormal(Automovil):
    ruedas = 4  

    def __init__(self, color, marca, aceleracion, velocidad):
        super().__init__(color, marca, aceleracion, velocidad)  

    def mostrar_detalles(self):
        super().mostrar_detalles() 

    def conducir(self):
        print("Conduciendo por tierra 🚗.")