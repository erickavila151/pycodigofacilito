#for-each & while

"""
while<condition>:
    ...
"""

"""counter = 0

while counter < 10:
    print('Valor', counter)
    #Ambas maneras son validas aunque el uso del += es más recomendada
    #counter = counter + 1
    counter += 1"""

counter = 0
number = int(
    input('Ingresa un número: ')
)

while number > 0:
    number = number // 10
    counter += 1
    print('Tu número tiene:', counter, 'dígitos' )