'''
Para esta sección del proyecto integrador necesitaremos aprender a manipular la terminal:

Iniciar con un número en 0, leer la tecla `n` del teclado en un bucle, por cada presionada, borrar la terminal
e imprimir el nuevo número hasta el número 50.

La operación de borrar la terminal e imprimir el nuevo número debe estar en su propia función.

Para borrar la terminal antes de imprimir nuevo contenido usar la instrucción:
os.system('cls' if os.name=='nt' else 'clear'), para esto se debe importar la librería os

'''
import readchar
from readchar import readkey, key
import os


def clear_cons(tecla_n):
    if tecla_n == 'n':
        os.system('cls' if os.name == 'nt' else 'clear')
        print (iter)


for iter in range(0,51):
    clear_cons(tecla_n=readchar.readkey())