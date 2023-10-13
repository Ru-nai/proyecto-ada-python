'''import readchar
from readchar import readkey, key
import os

jugador_nick = input('Ingresa tu nombre aquí: ') #Solicita el nombre del jugador

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
    clear_cons(tecla_n=readchar.readkey())'''

''''

1. Implementar una función que reciba el mapa de un laberinto en forma de cadena, y lo convierta a matriz de caracteres.

    i. Para generar los laberintos, usar esta página: https://www.dcode.fr/maze-generator con las configuraciones
        a. USE THIS CHARACTER FOR WALLS: #
        b. USE THIS CHARACTER FOR PATHS: .
        c. SINGLE CHARARACTER (MORE RECTANGULAR)
    ii. Completar los dos caracteres de paredes faltantes al final.
    iii. Los puntos inicial y final deben ser dados al crear el juego, usar las coordenadas (0,0) para el inicio y (end, end) para el final 
        (Asegurarse que las coordenadas son caminos válidos)
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

'''
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row in matrix: #recorre las filas de la matriz. Le asigna un índice a cada fila. [1, 2, 3] son índice 0, [4, 5, 6] son índice 1, etc.
    for element in row: #ciclo anidado. Recorre las columnas de la matriz. Sitúa un segundo índice. Itera sobre >"row", que va conteniendo cada fila.  
        print(element, end = " ") # evita que el print haga un salto de línea después de cada elemento, es decir, evita que se impriman los elementos uno debajo del otro aunque se encuentren en la misma fila. Por sí solo, los imprime todos en una sola línea.
    print() #este print SÍ genera el salto de línea luego de que el for anidado termine de iterar sobre "row"
'''

#####################################################################

import random

#Define tres laberintos
laberinto_1 = "..#####\n......#\n###.#.#\n#...#.#\n###.###\n#...#.#\n#.#.#.#\n#.#...#\n###.###\n#.....\n######"
laberinto_2 = "..###############\n..#.#.......#...#\n#.#.###.#.#.###.#\n#.......#.#.#.#.#\n#.#####.#.###.#.#\n#.....#.#.......\n################"
laberinto_3 = "..###########\n........#...#\n#######.#.###\n#...........\n############"

opciones_laberinto = [laberinto_1, laberinto_2, laberinto_3]#Almacena los laberintos en una lista
selecciona_laberinto_azar = random.choice(opciones_laberinto)#Se escoge un laberinto de 'opciones_laberinto' al azar con random, y se almacena dicho laberinto en 'selecciona_laberinto_azar

#Implementar una función que reciba el mapa de un laberinto en forma de cadena, y lo convierta a matriz de caracteres

def mostrar_laberinto(mapa):
    # Convierte el laberinto en una matriz
    filas = mapa.strip().split('\n')  #procesa el "mapa" recibido y lo almacena en la lista 'filas.' "strip" está eliminando los espacios en blanco al inicio y al final de la cadena, y "split('\n')" divide la cadena del laberinto en una lista de cadenas, separando cada lista de str al llegar al salto de línea ('\n'). Todo el laberinto se muestra en una sola fila, separando cada lista (fila) por una coma
    matriz_laberinto = [] #crea una lista vacía que va a almacenar la matriz
    for fila in filas: #itera las filas (lista de listas)
        simbolo = list(fila) #el simbolo actual es igual al simbolo que esté almacenando el índice / iterador 'fila' proveniente de 'filas', y lo va convirtiendo en un índice / elemento de una lista
        matriz_laberinto.append(simbolo) #agrega el 'simbolo' actual a la lista 'matriz_laberinto'
    # Muestra la matriz del laberinto
    for fila in matriz_laberinto:
        print(''.join(fila)) #va uniendo las filas en str para más legibilidad

# Ejemplo de uso:
mostrar_laberinto(selecciona_laberinto_azar)