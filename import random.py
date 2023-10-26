import random

def opciones_laberinto():
    laberinto_1 = 1
    laberinto_2 = 2
    laberinto_3 = 3

    opciones_laberinto = [laberinto_1, laberinto_2, laberinto_3]
    selecciona_laberinto_azar = random.choice(opciones_laberinto)
    return selecciona_laberinto_azar

labetinto_seleccionado = opciones_laberinto()
print(labetinto_seleccionado)