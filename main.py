from automovil import Automovil

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