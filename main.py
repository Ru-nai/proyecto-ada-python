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

continuar = True #variable para cambiar a Falso y detener el loop

while continuar == True: #loop infinito
    tecla = readchar.readkey()
    tecla != readchar.key.UP #si la tecla que se está presionando es diferente a la flecha arriba:
    print("Se presionó la tecla: ", tecla) #imprime la tecla que se esté presionando mientras esta sea diferente a la flecha arriba
    if tecla == readchar.key.UP: #si se mantiene presionada la flecha arriba:
        continuar == False #la variable ligada al ciclo cambia a falso
        print ("Se presionó la tecla: ↑")
        break #y se rompe el ciclo