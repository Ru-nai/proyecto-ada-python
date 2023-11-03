import readchar
from readchar import readkey, key
import os
import random
from typing import List, Tuple

'''

Proyecto integrador parte 6

1. Reescribir la función que convierte el laberinto de cadena a matriz,
para que en vez de usar un bucle, haga uso de la función map

2. Reescribir la función que lee el mapa usando la función 'readlines()'
para leerlo todo en una sola operación. 
Cargar las coordenadas y usar 'reduce()' para concatenar las filas leídas en una sola cadena, 
en otras palabras, sustituir el bucle de lectura del mapa en forma de candena para usar la función reduce.

'''

class Juego:
    def __init__(self, mapa: List[List[str]], posicion_inicial: Tuple[int, int], posicion_final: Tuple[int, int]):
        self.mapa = mapa
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final

    def __limpiar_consola(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def __mostrar_laberinto(self):
        self.__limpiar_consola()
        for fila in self.mapa:
            print(''.join(fila))

    def __main_loop(self):
        px, py = self.posicion_inicial

        while (px, py) != self.posicion_final:

            current_px, current_py = px, py

            tecla_presionada = readchar.readkey()

            if tecla_presionada == readchar.key.UP:
                current_px -= 1
            elif tecla_presionada == readchar.key.DOWN:
                current_px += 1
            elif tecla_presionada == readchar.key.LEFT:
                current_py -= 1
            elif tecla_presionada == readchar.key.RIGHT:
                current_py += 1

            if 0 <= current_px < len(self.mapa) and 0 <= current_py < len(self.mapa[0]) and self.mapa[current_px][current_py] != '#':
                self.mapa[px][py] = '.'
                px, py = current_px, current_py

            self.mapa[px][py] = 'P'  # Muestra 'P' en la última posición visitada
            self.__mostrar_laberinto()  # Muestra el laberinto después de actualizar

            if (px, py) == self.posicion_final:
                break

    def ejecutar(self):
        self.__main_loop()


class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        super().__init__([], (0, 0), (0, 0))
        self.path_a_mapas = path_a_mapas
        self.mapa, self.posicion_inicial, self.posicion_final = self.__leer_mapa()
        self.ejecutar()

    def __leer_mapa(self):
        archivos = os.listdir(self.path_a_mapas)
        nombre_archivo = random.choice(archivos)
        path_completo = os.path.join(self.path_a_mapas, nombre_archivo)

        with open(path_completo, 'r') as archivo:
            lines = archivo.readlines()

        #Reescribir la función que convierte el laberinto de cadena a matriz, para que en vez de usar un bucle, haga uso de la función map
        #'map interior' está usando strip para quitar espacios blancos al inicio y al final de la cadena que es el laberinto desde la segunda fila ya que los mapas dados tienen unos números en la primera fila
        #'map exterior' está tomando el mapa ya sin espacios al inicio y al final, e itera sobre cada fila en el mapa, y con 'list (interior)' está haciendo una lista de listas con el contenido de cada fila del mapa
        #'list exterior' está transformando todo lo obtenido de los dos maps y el list interior, en una lista de listas
        mapa = list(map(list, map(str.strip, lines[1:])))
        
        coordenadas = [int(coor) for coor in lines[0].split()]
        posicion_inicial = tuple(coordenadas[:2])

        # Establecer la posición final en la última fila, penúltima columna
        num_filas = len(mapa)
        num_columnas = len(mapa[0])
        posicion_final = (num_filas - 1, num_columnas - 2)

        return mapa, posicion_inicial, posicion_final

def main():
    path_a_mapas = r'd:\proyecto_integrador_ADA_2\mapas_proyecto_integrador'
    juego_archivo = JuegoArchivo(path_a_mapas)

if __name__ == '__main__':
    main()