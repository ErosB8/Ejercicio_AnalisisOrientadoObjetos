''' 
from clases.vehiculo import Automovil
from abc import ABC, abstractmethod

# Clase AutomovilVolador que hereda de Automovil
class AutomovilVolador(Automovil):
    ruedas = 6  # Sobrescribe el atributo ruedas con 6 para el automóvil volador

    def __init__(self, color, marca, aceleracion, velocidad, esta_volando=True):
        super().__init__(color, marca, aceleracion, velocidad)  
        self.esta_volando = esta_volando  

    def mostrar_detalles(self):
        super().mostrar_detalles()  # Llama al método de la clase padre para mostrar los detalles
        estado_vuelo = "volando" if self.esta_volando else "en tierra"
        print(f"Estado: {estado_vuelo}")

    # Método para hacer que el automóvil vuele
    def vuela(self):
        if not self.esta_volando:
            self.esta_volando = True
            print("El automóvil ahora está volando.")
        else:
            print("El automóvil ya está volando.")

    # Método para aterrizar el automóvil
    def aterriza(self):
        if self.esta_volando:
            self.esta_volando = False
            print("El automóvil ha aterrizado.")
        else:
            print("El automóvil ya está en tierra.")

    def conducir(self):
        print("Conduciendo en el aire 🚀.")
'''

from clases.automovil import Automovil

class AutomovilVolador(Automovil):
    ruedas = 6

    def __init__(self, año, modelo, marca, velocidad=0, esta_volando=False):
        super().__init__(año, modelo, marca, velocidad)
        self.esta_volando = esta_volando

    def volar(self):
        if not self.esta_volando:
            self.esta_volando = True
            print(f"El {self.marca} está volando.")
        else:
            print(f"El {self.marca} ya está en el aire.")

    def aterrizar(self):
        if self.esta_volando:
            self.esta_volando = False
            print(f"El {self.marca} ha aterrizado.")
        else:
            print(f"El {self.marca} ya está en tierra.")

    def conducir(self):
        if self.esta_volando:
            print(f"El {self.marca} está volando y no puede conducir en tierra.")
        else:
            super().conducir()
