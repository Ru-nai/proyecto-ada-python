import readchar
from readchar import readkey, key
import os
import random
from typing import List, Tuple

'''jugador_nick = input('Ingresa tu nombre aquí: ') #Solicita el nombre del jugador

print(f'¡Bienvenido, {jugador_nick}!') #Imprime mensaje de bienvenida + el nickname..'''


'''Leer un caracter suelto del teclado, imprimirlo siempre que no sea la tecla arriba y detenerse al presionar dicha tecla arriba'''

'''continuar = True #variable para cambiar a Falso y detener el loop

while continuar == True: #loop infinito
    tecla = readchar.readkey()
    tecla != readchar.key.UP #si la tecla que se está presionando es diferente a la flecha arriba:
    print("Se presionó la tecla: ", tecla) #imprime la tecla que se esté presionando mientras esta sea diferente a la flecha arriba
    if tecla == readchar.key.UP: #si se mantiene presionada la flecha arriba:
        continuar == False #la variable ligada al ciclo cambia a falso
        print ("Se presionó la tecla: ↑")
        break #y se rompe el ciclo.'''

'''Ejercicio: iniciar con un número 0, leer la tecla n por el teclado, por cada presionada borrar consola e imprimir nuevo numero hasta 50'''

'''def clear_cons(tecla_n):
    if tecla_n == 'n':
        os.system('cls' if os.name == 'nt' else 'clear')
        print (iter)


for iter in range(0,51):
    clear_cons(tecla_n=readchar.readkey())
'''
''' PROYECTO INTEGRADOR PARTE 4: GENERAR LABERINTO Y RECORRIDO'''
#laberintos creados con dcode:
'''laberinto_1 = "..#####\n......#\n###.#.#\n#...#.#\n###.###\n#...#.#\n#.#.#.#\n#.#...#\n###.###\n#.....\n######"
laberinto_2 = "..###############\n..#.#.......#...#\n#.#.###.#.#.###.#\n#.......#.#.#.#.#\n#.#####.#.###.#.#\n#.....#.#.......\n################"
laberinto_3 = "..###########\n........#...#\n#######.#.###\n#...........\n############"

opciones_laberinto = [laberinto_1, laberinto_2, laberinto_3]#Almacena los laberintos en una lista
selecciona_laberinto_azar = random.choice(opciones_laberinto) #Se escoge un laberinto de 'opciones_laberinto' al azar con random, y se almacena dicho laberinto en 'selecciona_laberinto_azar'
'''
#------------------------------------------------------------------------------------------------------------
#FUNCIONES:
'''def obtener_tamano_laberinto(laberinto):
    filas = laberinto.strip().split('\n')
    num_filas = len(filas)
    num_columnas = max(len(fila) for fila in filas)
    return num_filas, num_columnas


def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')
'''

'''def mostrar_laberinto(mapa):
    limpiar_consola()
    for fila in mapa:
        print(''.join(fila))
'''

'''def main_loop(mapa: List[List[str]], posicion_inicial: Tuple[int, int], posicion_final: Tuple[int, int]):
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
'''
'''
def ejecutar():
    laberinto_seleccionado = selecciona_laberinto_azar #se le asigna el valor de la variable 'selecciona_laberinto_azar' a la variable 'laberinto_seleccionado'. De esta manera, se le pasará uno de los tres laberintos definidos al inicio del código
    tamano = obtener_tamano_laberinto(laberinto_seleccionado) #'tamano' almacena la tupla obtenida en la funcion 'obtener_tamano_laberinto' para luego 'tamano' para establecer la coordenada (end,end)
    posicion_inicial = (0, 0) #posicion de 'P' se inicia en (0,0), lo que es en la esquina superior izquierda
    posicion_final = (tamano[0] - 1, tamano[1] - 2) #se crea la variable 'posicion_final' y se calcula usando la tupla almacenada en 'tamano'. Intenté que (end,end) fuera visto en Y como una fila antes de la última fila, pero no funciona y no entiendo bien por qué esta es la convención para hacer laberintos
    mapa = [list(fila) for fila in laberinto_seleccionado.strip().split('\n')] #la variable mapa almacena 'laberinto_seleccionado' convertido en una lista de caracteres

    main_loop(mapa, posicion_inicial, posicion_final) #finalmente, se llama a la funcion "main_loop' y se le pasan como parámetros las variables que se definieron antes de llamar a dicha funcion dentro de 'ejecutar'

ejecutar() #llama a la funcion 'ejecutrar' para que ejecute todo lo que tiene adentro'''

class Juego:
    def __init__(self, 
                 mapa: List[List[str]], 
                 posicion_inicial: Tuple[int, int], 
                 posicion_final: Tuple[int, int]):
        
        self.mapa = mapa
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final
    
    def __opciones_laberinto(self):
        self.laberinto_1 = "..#####\n......#\n###.#.#\n#...#.#\n###.###\n#...#.#\n#.#.#.#\n#.#...#\n###.###\n#.....\n######"
        self.laberinto_2 = "..###############\n..#.#.......#...#\n#.#.###.#.#.###.#\n#.......#.#.#.#.#\n#.#####.#.###.#.#\n#.....#.#.......\n################"
        self.laberinto_3 = "..###########\n........#...#\n#######.#.###\n#...........\n############"

        opciones_laberinto = [self.laberinto_1, self.laberinto_2, self.laberinto_3]
        selecciona_laberinto_azar = random.choice(opciones_laberinto)
        return selecciona_laberinto_azar

    def __obtener_tamano_de_laberinto(self, laberinto):
        filas = laberinto.strip().split('\n')
        num_filas = len(filas)
        num_columnas = max(len(fila) for fila in filas)
        return num_filas, num_columnas
    
    def __limpiar_consola(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def __mostrar_laberinto(self, mapa):
        self.__limpiar_consola()
        for fila in mapa:
            print(''.join(fila))

    def __main_loop(self, 
                    mapa: List[List[str]], 
                    posicion_inicial: Tuple[int, int], 
                    posicion_final: Tuple[int, int]):
        
        self.px, self.py = posicion_inicial

        while (self.px, self.py) != posicion_final:

            mapa[self.px][self.py] = 'P'
            self.__mostrar_laberinto(mapa)
            current_px, current_py = self.px, self.py

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
                mapa[self.px][self.py] = '.'
                self.px, self.py = current_px, current_py
    
    def ejecutar(self):
        self.laberinto_seleccionado = self.__opciones_laberinto()
        self.tamano = self.__obtener_tamano_de_laberinto(self.laberinto_seleccionado) 
        self.posicion_inicial = (0, 0) 
        self.posicion_final = (self.tamano[0] - 1, self.tamano[1] - 1) 
        self.mapa = [list(fila) for fila in self.laberinto_seleccionado.strip().split('\n')] 

        self.__main_loop(self.mapa, self.posicion_inicial, self.posicion_final) 


class JuegoArchivo (Juego):
    def __init__(self, path_a_mapas):
        self.path_a_mapas = path_a_mapas
        super().__init__(self.__obtener_mapa())

    def __obtener_mapa(self):
        archivos_de_mapas = os.listdir(self.path_a_mapas)
        nombre_archivo = random.choice(archivos_de_mapas)
        path_completo = os.path.join(self.path_a_mapas, nombre_archivo)
        
        with open(path_completo, 'r') as archivo_mapa:
            mapa = archivo_mapa.read()
        
        return self.__procesar_mapa(mapa)
    
    def __procesar_mapa(self, mapa):
        # Procesar el mapa para obtener las coordenadas de inicio y fin.
        lineas = mapa.strip().split('\n')
        tamano = lineas[0].split(',')
        mapa = '\n'.join(lineas[1:])  # Eliminar la primera línea que contiene dimensiones y coordenadas
        return mapa, (int(tamano[0]), int(tamano[1])), (int(tamano[2]), int(tamano[3]))


'''-------------------------------------------------------------------------------------'''

def main():
    path_a_mapas = "tu_ruta_a_los_mapas"  # Reemplaza con la ruta a tu carpeta de mapas
    juego = JuegoArchivo(r'C:\Users\Papas con queso\Downloads\mapas_proyecto_integrador')

    juego.ejecutar()


if __name__ == '__main__':
    main()