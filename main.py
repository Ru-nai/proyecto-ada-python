jugador_nick = input('Ingresa tu nombre aquí: ') #Solicita el nombre del jugador

print(f'¡Bienvenido, {jugador_nick}!') #Imprime mensaje de bienvenida + el nickname

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
    
'''from readchar import readkey, key
'''
'''key = readchar.readkey()
if key == 'a':
    print ('Presionó la tecla: ',key)

continuar = True #variable para cambiar a Falso y detener el loop
while continuar: #loop infinito
    keyboard.read_key() != keyboard.KEY_UP #si la tecla que se está presionando es diferente a la flecha arriba:
    print(keyboard.read_key()) #imprime la tecla que se esté presionando mientras esta sea diferente a la flecha arriba
    if keyboard.is_pressed(keyboard.KEY_UP): #si se mantiene presionada la flecha arriba:
        continuar == False #la variable ligada al ciclo cambia a falso
        print ("Fin")
        break #y se rompe el ciclo'''