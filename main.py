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

#------------------------------------------------------------------------------------------------------------
#FUNCIONES:
def obtener_tamano_laberinto(laberinto):
    #Función para obtener el tamaño del laberinto. Recibe como parámetro el laberinto y es para ayudar a hallar cuál sería la coordenada (end, end) si los laberintos son de distintos tamaños
    filas = laberinto.strip().split('\n') #Elimina espacios al inicio y al final del laberinto y separa el str en el salto de línea para crear distintas listas que funcionarán como filas, y  almacena dichas filas en la variable 'filas'
    num_filas = len(filas) #num_filas almacena / cuenta cuántas filas (listas dentro de la lista 'filas') hay en el laberinto.
    num_columnas = max(len(fila) for fila in filas) #calcula el número de columnas dentro de las filas del laberinto. Tiene un bucle 'for' que recorre cada fila de la lista 'filas'; 'len(fila)' calcula la longitud de cada fila en la que está iterando, es decir, la cantidad de carácteres dentro de cada fila. 'max()' encuentra el valor máximo de la longitud de las filas, y retorna el número máximo de columnas.
    return num_filas, num_columnas #retorna una tupla que contiene (num_filas, num_columnas)


def limpiar_consola():
    #Función para limpiar la pantalla/consola antes de imprimir / mostrar el laberinto usando la librería os.
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_laberinto(mapa):
    #Función para mostrar el laberinto en la consola luego de limpiarla. Recibe como parámetro 'mapa' que es una matriz que representa el laberinto
    limpiar_consola() #llama a la función 'limpiar_consola' antes de imprimir
    for fila in mapa: #bucle for que recorre cada fila (lista de listas) de la matriz 'mapa'
        print(''.join(fila)) #cada fila de la matriz 'mapa' se convierte a una cadena, para que se impriman como str en lugar de listas y se vea más claro, y las va imprimiendo


def main_loop(mapa: List[List[str]], posicion_inicial: Tuple[int, int], posicion_final: Tuple[int, int]):
    #define la funcion del main_loop, toma tres argumentos: 'mapa', el cual es una matriz que representa el laberinto; 'posicion_inicial' la cual es una tupla que contiene las posiciones inicial del jugador en el eje x y el eje y. Por último, 'posicion_final' contiene la posicion final de 'P'
    px, py = posicion_inicial #Se asigna a las variable 'px' y 'py' las coordenadas de 'posicion_inicial'. Se usarán para rastrear la posicion actual de 'P'

    while (px, py) != posicion_final: #inicia un bucle 'while' que se ejecute siempre y cuando px y py sean diferentes a la posicion_final
        mapa[px][py] = 'P' #asigna el caracter 'P' a las 'coordenadas' actuales de px y py dentro del mapa
        mostrar_laberinto(mapa) #llama a la función 'mostrar_laberinto'. Lo que muestra es el laberinto con la posicion actual de 'P'
        current_px, current_py = px, py #la posicion actual de 'P' en X y Y se basa en la posicion px, py señalada anteriormente, para determinar donde se encuentra 'P'

        tecla_presionada = readchar.readkey()#asigna la tecla presionada por el usuario a la variable 'tecla_presionada' usando readchar.readkey

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
            mapa[px][py] = '.'  # si después de que el 'if' evalúe, la posición del 'P' cumple las condiciones, reemplaza 'P' por '.'
            px, py = current_px, current_py  # mueve a 'P' a la nueva posicion válida luego de reemplazar su posicion anterior por '.'


def ejecutar(): #configura / ejecuta las funciones anteriores para que sí se imprima algo
    laberinto_seleccionado = selecciona_laberinto_azar #se le asigna el valor de la variable 'selecciona_laberinto_azar' a la variable 'laberinto_seleccionado'. De esta manera, se le pasará uno de los tres laberintos definidos al inicio del código
    tamano = obtener_tamano_laberinto(laberinto_seleccionado) #'tamano' almacena la tupla obtenida en la funcion 'obtener_tamano_laberinto' para luego 'tamano' para establecer la coordenada (end,end)
    posicion_inicial = (0, 0) #posicion de 'P' se inicia en (0,0), lo que es en la esquina superior izquierda
    posicion_final = (tamano[0] - 1, tamano[1] - 2) #se crea la variable 'posicion_final' y se calcula usando la tupla almacenada en 'tamano'. Intenté que (end,end) fuera visto en Y como una fila antes de la última fila, pero no funciona y no entiendo bien por qué esta es la convención para hacer laberintos
    mapa = [list(fila) for fila in laberinto_seleccionado.strip().split('\n')] #la variable mapa almacena 'laberinto_seleccionado' convertido en una lista de caracteres

    main_loop(mapa, posicion_inicial, posicion_final) #finalmente, se llama a la funcion "main_loop' y se le pasan como parámetros las variables que se definieron antes de llamar a dicha funcion dentro de 'ejecutar'

ejecutar() #llama a la funcion 'ejecutrar' para que ejecute todo lo que tiene adentro