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
