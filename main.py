'''

Proyecto integrador parte 4

1. Implementar una función que reciba el mapa de un laberinto en forma de cadena, y lo convierta a matriz de caracteres.
    i. Para generar los laberintos, usar esta página: https://www.dcode.fr/maze-generator con las configuraciones
        a. USE THIS CHARACTER FOR WALLS: #
        b. USE THIS CHARACTER FOR PATHS: .
        c. SINGLE CHARARACTER (MORE RECTANGULAR)
    ii. Completar los dos caracteres de paredes faltantes al final.
    iii. Los puntos inicial y final deben ser dados al crear el juego, usar las coordenadas (0,0) para el inicio y (end, end) para el final (Asegurarse que las coordenadas son caminos válidos)
    iv. Recuerdo: Para separar por filas usar split("\n") y para convertir una cadena a una lista de caracteres usar list(cadena).

2. Escribir una función que limpie la pantalla y muestre la matriz (recibe el mapa en forma de matriz)

3. Implementar el main loop en una función (recibe el mapa en forma de matriz)
    i. recibir: mapa List[List[str]], posicion inicial Tuple[int, int], posicion final Tuple[int, int].
    ii. definir dos variavles px y py que contienen las coordenadas del jugador, iniciar como los valores de la posición incial
    iii. procesar mientras (px, py) no coincida con la coordenada final.
        a. asignar el caracter P en el mapa a las coordenadas (px, py) en todo momento.
        b. leer del teclado las teclas de flechas, antes de actualizar la posición, verificar si esta posición tentativa:
            a) No se sale del mapa
            b) No es una pared
        c. Si la nueva posición es válida, actualizar (px, py), poner el caracter P en esta nueva coordenada y restaurar la anterior a .
        d. mostrar

'''

#Importa las librerías que se necesitarán. 'random' para que se seleccione un laberinto al azar de los puestos, 'os' para limpiar consola, 'readchar' para que el PC identifique las flechas, 'typing' para que el PC sepa cuáles serán los tipos datos a manejar
import random
import os
import readchar
from typing import List, Tuple

#laberintos creados con dcode:
laberinto_1 = "..#####\n......#\n###.#.#\n#...#.#\n###.###\n#...#.#\n#.#.#.#\n#.#...#\n###.###\n#.....\n######"
laberinto_2 = "..###############\n..#.#.......#...#\n#.#.###.#.#.###.#\n#.......#.#.#.#.#\n#.#####.#.###.#.#\n#.....#.#.......\n################"
laberinto_3 = "..###########\n........#...#\n#######.#.###\n#...........\n############"

opciones_laberinto = [laberinto_1, laberinto_2, laberinto_3]#Almacena los laberintos en una lista
selecciona_laberinto_azar = random.choice(opciones_laberinto) #Se escoge un laberinto de 'opciones_laberinto' al azar con random, y se almacena dicho laberinto en 'selecciona_laberinto_azar'

def obtener_tamano_laberinto(laberinto):
    #Función para obtener el tamaño del laberinto. Recibe como parámetro el laberinto y es para ayudar a hallar cuál sería la coordenada (end, end) si los laberintos son de distintos tamaños
    filas = laberinto.strip().split('\n') #Elimina espacios al inicio y al final del laberinto y separa el str en el salto de línea para crear distintas listas que funcionarán como filas, y  almacena dichas filas en la variable 'filas'
    num_filas = len(filas) #num_filas almacena / cuenta cuántas filas (listas dentro de la lista 'filas') hay en el laberinto.
    num_columnas = max(len(fila) for fila in filas) #calcula el número de columnas dentro de las filas del laberinto. Tiene un bucle 'for' que recorre cada fila de la lista 'filas'; 'len(fila)' calcula la longitud de cada fila en la que está iterando, es decir, la cantidad de carácteres dentro de cada fila. 'max()' encuentra el valor máximo de la longitud de las filas, y retorna el número máximo de columnas.
    return num_filas, num_columnas #retorna una tupla que contiene (num_filas, num_columnas)

def limpiar_consola():
    #Función para limpiar la pantalla/consola antes de imprimir / mostrar el laberinto usando la librería os.
    os.system('cls' if os.name == 'nt' else 'clear')