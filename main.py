import readchar
from readchar import readkey, key
import os

jugador_nick = input('Ingresa tu nombre aquí: ') #Solicita el nombre del jugador

print(f'¡Bienvenido, {jugador_nick}!') #Imprime mensaje de bienvenida + el nickname..

'''Leer un caracter suelto del teclado, imprimirlo siempre que no sea la tecla arriba y detenerse al presionar dicha tecla arriba'''

continuar = True #variable para cambiar a Falso y detener el loop

while continuar == True: #loop infinito
    tecla = readchar.readkey()
    tecla != readchar.key.UP #si la tecla que se está presionando es diferente a la flecha arriba:
    print("Se presionó la tecla: ", tecla) #imprime la tecla que se esté presionando mientras esta sea diferente a la flecha arriba
    if tecla == readchar.key.UP: #si se mantiene presionada la flecha arriba:
        continuar == False #la variable ligada al ciclo cambia a falso
        print ("Se presionó la tecla: ↑")
        break #y se rompe el ciclo.

'''Ejercicio: iniciar con un número 0, leer la tecla n por el teclado, por cada presionada borrar consola e imprimir nuevo numero hasta 50'''

def clear_cons(tecla_n):
    if tecla_n == 'n':
        os.system('cls' if os.name == 'nt' else 'clear')
        print (iter)


for iter in range(0,51):
    clear_cons(tecla_n=readchar.readkey())

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