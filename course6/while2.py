#generador de números enteros aleatorios
from random import randint

number = None
#randit hace referencia a random interger
random_number = randint(0,10)

lifes = 0

while number != random_number and lifes < 3:
   
    number = int( #Int transforma el String a entero
        input('Ingresa un número: ') #String que será convertido en entero
    )
    if random_number > number:
        print('El ńumero aleatorio es mayor')
    elif random_number < number:
        print('El ńumero aleatorio es menor') 
    else:
        print('Correcto!') 

    lifes += 1
else:
    if number == random_number:
        print(f'Felicidades, encontraste el ńumero aleatorio {random_number}')
    else:
        print('Lo sentimos, no encontraste el número')
    