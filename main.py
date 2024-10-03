'''
from automovil import Automovil
from automovilNormal import AutomovilNormal
from automovilVolador import AutomovilVolador
from abc import ABC, abstractmethod
from suma.mostrarsuma import mostrar_suma

# Crear una instancia del automóvil
mi_auto = Automovil("Rojo", "Toyota", 10, 120)

# Mostrar los detalles actuales
mi_auto.mostrar_ruedas_acelaracion()

# Modificar la aceleración
mi_auto.modificar_aceleracion(20)

# Mostrar los detalles nuevamente para ver la actualización
mi_auto.mostrar_ruedas_acelaracion()

# Acelerar el automóvil
mi_auto.acelerar()

# Mostrar los detalles después de acelerar
mi_auto.mostrar_detalles()

# Frenar el automóvil
mi_auto.frenar()

# Mostrar los detalles después de frenar
mi_auto.mostrar_detalles()

# Crear la segunda instancia del automóvil
auto2 = Automovil("Azul", "Ford", 15, 60)
auto2.mostrar_detalles()

# Frenar el segundo automóvil
auto2.frenar()
auto2.mostrar_detalles()

# Crear una instancia de AutomovilVolador
auto_volador = AutomovilVolador("Plateado", "Tesla", 20, 100)

# Mostrar las características iniciales del automóvil volador
print("Características del automóvil volador:")
auto_volador.mostrar_detalles()

# Acelerar el automóvil volador
print("\nAcelerando el automóvil volador...")
auto_volador.acelerar()
auto_volador.mostrar_detalles()

# Frenar el automóvil volador
print("\nFrenando el automóvil volador...")
auto_volador.frenar()
auto_volador.mostrar_detalles()

# Aterrizar el automóvil volador
print("\nAterrizando el automóvil volador...")
auto_volador.aterriza()
auto_volador.mostrar_detalles()

# Hacer que el automóvil vuelva a volar
print("\nHaciendo que el automóvil vuelva a volar...")
auto_volador.vuela()
auto_volador.mostrar_detalles()

 # Crear una instancia de AutomovilNormal
auto_normal = AutomovilNormal("Rojo", "Ferrari", 30, 150)

# Mostrar las características del automóvil normal
print("Características del automóvil normal:")
auto_normal.mostrar_detalles()

# Conducir el automóvil normal
print("\nConduciendo el automóvil normal:")
auto_normal.conducir()

# Conducir el automóvil volador
print("\nConduciendo el automóvil volador:")
auto_volador.conducir()

num1 = 5
num2 = 3
mostrar_suma(num1, num2)
'''

from clases.automovil_volador import AutomovilVolador

if __name__ == "__main__":
    auto_volador = AutomovilVolador(2024, "X-Wing", "Tesla", 300)
    print(f"Año: {auto_volador.get_año()}")
    print(f"Modelo: {auto_volador.get_modelo()}")
    print(f"Marca: {auto_volador.marca}")

    # Conducir y volar
    auto_volador.conducir()
    auto_volador.volar()

    # Intentar conducir mientras vuela
    auto_volador.conducir()

    # Aterrizar y conducir nuevamente
    auto_volador.aterrizar()
    auto_volador.conducir()