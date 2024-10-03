''' 
from abc import ABC, abstractmethod

class Automovil:
    # Atributo de clase ruedas, por defecto inicializado en 4
    ruedas = 4

    # Constructor con los parámetros color, marca, aceleracion y velocidad
    def __init__(self, color, marca, aceleracion, velocidad):
        self.color = color
        self.marca = marca
        self.aceleracion = aceleracion
        self.velocidad = velocidad

    # Método para mostrar los detalles del automóvil
    def mostrar_detalles(self):
        print(f"Color: {self.color}, Marca: {self.marca}, Aceleración: {self.aceleracion}, Velocidad: {self.velocidad}, Ruedas: {self.ruedas}")

    def mostrar_ruedas_acelaracion(self):
        print(f"Aceleración: {self.aceleracion}, Ruedas: {self.ruedas}")

    # Método para modificar la aceleración
    def modificar_aceleracion(self, nueva_aceleracion):
        self.aceleracion = nueva_aceleracion
        print(f"Aceleración modificada a: {self.aceleracion}")

    # Método para acelerar, que incrementa la velocidad usando la aceleración
    def acelerar(self):
        self.velocidad += self.aceleracion
        print(f"Velocidad aumentada a: {self.velocidad}")

    # Método para frenar, que disminuye la velocidad usando la aceleración
    def frenar(self):
        self.velocidad -= self.aceleracion
        if self.velocidad < 0:
            self.velocidad = 0  # La velocidad no puede ser negativa
        print(f"Velocidad reducida a: {self.velocidad}")

    @abstractmethod
    def conducir(self):
        pass  # Método abstracto para que las clases derivadas lo implementen
'''

class Vehiculo:
    def __init__(self, año, modelo):
        self._año = año
        self.__modelo = modelo

    def get_año(self):
        return self._año

    def set_año(self, año):
        self._año = año

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo
