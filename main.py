jugador_nick = input('Ingresa tu nombre aquí: ') #Solicita el nombre del jugador

print(f'¡Bienvenido, {jugador_nick}!') #Imprime mensaje de bienvenida + el nickname

'''---------------------------------------------------------------------------------'''
'''Leer un caracter suelto del teclado, imprimirlo siempre que no sea la tecla arriba y detenerse al presionar dicha tecla arriba'''
import readchar
from readchar import readkey, key


'''from readchar import readkey, key
'''
key = readchar.readkey()
if key == 'a':
    print ('Presionó la tecla: ',key)