import readchar
from readchar import readkey, key
import os
import random
from typing import List, Tuple

jugador_nick = input('Ingresa tu nombre aquí: ')

print(f'¡Bienvenido, {jugador_nick}!')


'''Leer un caracter suelto del teclado, imprimirlo siempre que no sea la tecla arriba y detenerse al presionar dicha tecla arriba'''

continuar = True

while continuar == True:
    tecla = readchar.readkey()
    tecla != readchar.key.UP
    print("Se presionó la tecla: ", tecla)
    if tecla == readchar.key.UP:
        continuar == False
        print ("Se presionó la tecla: ↑")
        break

'''Ejercicio: iniciar con un número 0, leer la tecla n por el teclado, por cada presionada borrar consola e imprimir nuevo numero hasta 50'''

def clear_cons(tecla_n):
    if tecla_n == 'n':
        os.system('cls' if os.name == 'nt' else 'clear')
        print (iter)


for iter in range(0,51):
    clear_cons(tecla_n=readchar.readkey())

''' PROYECTO INTEGRADOR PARTE 4: GENERAR LABERINTO Y RECORRIDO'''
#laberintos creados con dcode:
laberinto_1 = "..#####\n......#\n###.#.#\n#...#.#\n###.###\n#...#.#\n#.#.#.#\n#.#...#\n###.###\n#.....\n######"
laberinto_2 = "..###############\n..#.#.......#...#\n#.#.###.#.#.###.#\n#.......#.#.#.#.#\n#.#####.#.###.#.#\n#.....#.#.......\n################"
laberinto_3 = "..###########\n........#...#\n#######.#.###\n#...........\n############"

opciones_laberinto = [laberinto_1, laberinto_2, laberinto_3]
selecciona_laberinto_azar = random.choice(opciones_laberinto)

#------------------------------------------------------------------------------------------------------------
#FUNCIONES:
def obtener_tamano_laberinto(laberinto):
    filas = laberinto.strip().split('\n')
    num_filas = len(filas)
    num_columnas = max(len(fila) for fila in filas)
    return num_filas, num_columnas


def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_laberinto(mapa):
    limpiar_consola()
    for fila in mapa:
        print(''.join(fila))


def main_loop(mapa: List[List[str]], posicion_inicial: Tuple[int, int], posicion_final: Tuple[int, int]):
    px, py = posicion_inicial
    while (px, py) != posicion_final:
        mapa[px][py] = 'P'
        mostrar_laberinto(mapa)
        current_px, current_py = px, py

        tecla_presionada = readchar.readkey()

        if tecla_presionada == readchar.key.UP:
            current_px -= 1 #Si la flecha presionada fue la tecla arriba, reduce current_px en 1
        elif tecla_presionada == readchar.key.DOWN:
            current_px += 1 #Si la flecha presionada fue la tecla abajo, incrementa current_px en 1
        elif tecla_presionada == readchar.key.LEFT:
            current_py -= 1 #Si la flecha presionada fue la tecla izquierda, reduce current_py en 1
        elif tecla_presionada == readchar.key.RIGHT:
            current_py += 1 #Si la flecha presionada fue la tecla derecha, incrementa current_py en 1

        if 0 <= current_px < len(mapa) and 0 <= current_py < len(mapa[0]) and mapa[current_px][current_py] != '#':
            #este if verifica si 'current_px' y 'current_py' está dentro del tamaño del laberinto, comprobando si current_px y current_py se encuentran entre 0 y el número de columnas que haya en el laberinto. Tambien evalúa que la posicion no sea '#'
            #por alguna razon, este if no esta funcionando bien, deja que 'P' se salga de la matriz y da un error por consola
            mapa[px][py] = '.'
            px, py = current_px, current_py


def ejecutar():
    laberinto_seleccionado = selecciona_laberinto_azar
    tamano = obtener_tamano_laberinto(laberinto_seleccionado)
    posicion_inicial = (0, 0)
    posicion_final = (tamano[0] - 1, tamano[1] - 2)
    mapa = [list(fila) for fila in laberinto_seleccionado.strip().split('\n')]

    main_loop(mapa, posicion_inicial, posicion_final)

ejecutar()

'''PROYECTO INTEGRADOR PARTE 5: ENCAPSULAMIENTO DE UNA CLASE Y MANEJO DE ARCHIVOS'''


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

            self.mapa[px][py] = 'P'
            self.__mostrar_laberinto()

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

        mapa = []
        for line in lines[1:]:
            mapa.append(list(line.strip()))

        coordenadas = [int(coordenates) for coordenates in lines[0].split()]
        posicion_inicial = tuple(coordenadas[:2])

        num_filas = len(mapa)
        num_columnas = len(mapa[0])
        posicion_final = (num_filas - 1, num_columnas - 2)

        return mapa, posicion_inicial, posicion_final

def main():
    path_a_mapas = r'D:\proyecto_integrador_ADA_2\mapas_proyecto_integrador'
    juego = JuegoArchivo(path_a_mapas)

if __name__ == '__main__':
    main()