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

