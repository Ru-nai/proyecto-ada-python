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

import readchar
from readchar import readkey, key
import os
import random
from typing import List, Tuple


class Juego: #Crea una clase llamada 'Juego' que contendrá las funciones creadas en la rama: proyecto_integrador_pt_4, como si estas fueran métodos privados
    def __init__(self, mapa: List[List[str]], posicion_inicial: Tuple[int, int], posicion_final: Tuple[int, int]): #el método constructor recibe el mapa (que es una lista de listas de caracteres), la posicion_inicial (que será una tupla de dos enteros (0,0)), y la posicion_final, (que será una tupla de dos enteros equivalentes al la última fila y penúltima columna del mapa)
        self.mapa = mapa #almacena el mapa que se pasó como parámetro en el método constructor, en la variable 'mapa' del objeto (self)
        self.posicion_inicial = posicion_inicial #almacena la posicion_inicial pasada como parámetro en una variable
        self.posicion_final = posicion_final #almacena la posicion_final pasada como parámetro en una variable

    def __limpiar_consola(self): #método para limpiar la consola 
        os.system('cls' if os.name == 'nt' else 'clear')

    def __mostrar_laberinto(self): #método para mostrar el laberinto por consola
        self.__limpiar_consola() #llama al método para limpiar la consola antes de comenzar la impresión
        for fila in self.mapa: #itera sobre mapa e imprime cada carácter
            print(''.join(fila))

    def __main_loop(self): #define el método 'main_loop'
        px, py = self.posicion_inicial #obtiene y almacena la posición inicial del jugador basándose en la información recibida como parámetro en posicion_inicial

        while (px, py) != self.posicion_final: #mientras la posicion de 'P' sea diferente a la posicion_final:

            current_px, current_py = px, py #asigna la posición de px, py a las variables temporales current_px, current_py para calcular la posición posible de 'P'

            tecla_presionada = readchar.readkey() #lee / almacena la tecla que se presione

            if tecla_presionada == readchar.key.UP:
                current_px -= 1 #si la tecla presionada es 'UP', decrementa en 1 la posición de px, moviendo a 'P' hacia arriba 
            elif tecla_presionada == readchar.key.DOWN:
                current_px += 1 #si la tecla presionada es 'DOWN' incrementa en 1 la posición de px, mueve a 'P' hacia abajo
            elif tecla_presionada == readchar.key.LEFT:
                current_py -= 1 #si la tecla presionada es 'LEFT' decrementa en 1 la posición de py, mueve a 'P' hacia la izquierda
            elif tecla_presionada == readchar.key.RIGHT:
                current_py += 1 #si la tecla presionada es 'RIGHT' incrementa en 1 la posición de py, mueve a 'P' hacia la derecha

            if 0 <= current_px < len(self.mapa) and 0 <= current_py < len(self.mapa[0]) and self.mapa[current_px][current_py] != '#':
                #si la posicion actual de px y py es menor o igual a las dimensiones del mapa, y el espacio a donde se quiere mover es diferente a #:
                self.mapa[px][py] = '.' #reemplaza la posición px, py (anterior posición de 'P') por el punto (.), para que 'P' no vaya dejando un rastro
                px, py = current_px, current_py #y asigna la nueva posición de 'P' en px y py a current_px y current_py

            self.mapa[px][py] = 'P'  #cambia el (.) que estaba en px, py, por la letra 'P' (personaje)
            self.__mostrar_laberinto() #llama al método '__mostrar_laberinto()' para imprimir el laberinto actualizado con la posición actual de 'P'

            if (px, py) == self.posicion_final: #si la posición de px, py es igual a la posición final (última fila, penúltima columna), se rompe el bucle y termina la ejecución
                break

    def ejecutar(self): #inicia la ejecución del juego llamando a __main_loop
        self.__main_loop()


class JuegoArchivo(Juego): #crea una clase hija llamada 'JuegoArchivo', que hereda de la clase 'Juego' para poder cargar mapas desde archivos .txt
    def __init__(self, path_a_mapas): #recibe el directorio (path) a donde están los mapas almacenados
        super().__init__([], (0, 0), (0, 0)) #invoca el método __init__ de la clase padre 'Juego' y sus atributos, y le pasa una lista vacía como mapa, una tupla (0,0) como posicion inicial y una tupla (0,0) como posicion final
        self.path_a_mapas = path_a_mapas #almacena el directorio que se pasó como argumento en la variable propia del objeto "path_a_mapas"
        self.mapa, self.posicion_inicial, self.posicion_final = self.__leer_mapa() #asigna los valores del método __leer_mapa (que leerá un archivo al azar que contiene el mapa) a self.mapa, self.posicion_inicial y self.posicion_final
        self.ejecutar() #llama al método "ejecutar" que a su vez llama al método __main_loop

    def __leer_mapa(self): #lee / carga un mapa desde un archivo .txt
        archivos = os.listdir(self.path_a_mapas) #hace una lista de los nombres de los archivos en el directorio que se señale como path_a_mapas
        nombre_archivo = random.choice(archivos) #escoge al azar uno de los archivos .txt
        path_completo = os.path.join(self.path_a_mapas, nombre_archivo) #crea la ruta del archivo que seleccione random.choice

        with open(path_completo, 'r') as archivo: #abre el archivo en modo lectura. Usa el comando 'with' para que se cierre bien luego de usarlo
            lines = archivo.readlines() #lee todas las líneas del archivo seleccionado y las almacena en la variable 'lines'

        mapa = [] #crea una lista vacía llamada 'mapa'
        for line in lines[1:]: #por cada línea en la variable 'lines', comenzando por la segunda fila:
            mapa.append(list(line.strip())) #va agregando a la lista vacía 'mapa' cada línea que se lee como una lista de carácteres, eliminando los espacios en blanco al inicio y al final 

        coordenadas = [int(coordenates) for coordenates in lines[0].split()] #divide la primera línea del archivo en valores enteros, y va almacenando los resultados en una lista llamada "coordenadas".
        posicion_inicial = tuple(coordenadas[:2]) #toma los primeros dos índices de la lista 'coordenadas' y los usa como posicion_inicial

        num_filas = len(mapa) #calcula el número de filas en la matriz
        num_columnas = len(mapa[0]) #calcula el número de columnas teniendo en cuenta el tamaño de la primera fila (primera lista de listas)
        posicion_final = (num_filas - 1, num_columnas - 2) #establece como posicion_final el numero de filas - 1 (la última fila) y el numero de columnas - 2 (la penúltima columna)

        return mapa, posicion_inicial, posicion_final #retorna el mapa, la posicion inicial y la posicion final

def main():
    path_a_mapas = r'D:\proyecto_integrador_ADA_2\mapas_proyecto_integrador' #asigna un string con el directorio donde están ubicados los mapas a la variable "path_a_mapas"
    juego = JuegoArchivo(path_a_mapas) #crea un objeto de la clase hija 'JuegoArchivo,' y se le pasa la variable "path_a_mapas" como argumento de la clase para que sepa dónde encontrar los archivos

if __name__ == '__main__':
    main()