'''
---------------------------------------------------------------------------------
* Instalar la librería: https://pypi.org/project/readchar/
* Investigrar cómo leer un caracter del teclado
* Escribir un programa que corra un bucle infinito leyendo e imprimiento las teclas,
 y sólo terminará cuando se presione la tecla ↑ indicada como UP
---------------------------------------------------------------------------------
'''
'''Leer un caracter suelto del teclado, imprimirlo siempre que no sea la tecla arriba y detenerse al presionar dicha tecla arriba'''
import readchar
from readchar import readkey, key


tecla = readchar.readkey()
if tecla == readchar.key.UP:
    print("Se presiono ↑")
else:
    print("Se presiono otra tecla")
