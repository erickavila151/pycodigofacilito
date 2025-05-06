'''
def <nombre_de_la_funcion>(<parámetros, >):
    ...
'''
#valor de entrada que será asignado a number
#los parámetros no son más que variables asignadas para usar dentro de la
#función
            #Parámetro
def count_to(number):
    pass
def multiply(number1, number2):
    result = number1 * number2
    print( f'El resultado de la operación es: {result}')

def full_name(first_name, last_name, prefix):
    full_name = f'{prefix} {first_name} {last_name}'
    print(full_name)

#Un argumento es un valor que será almacenado en un parámetro
count_to(10) #Argumento
#Los argumentos por default se asignan por posición
multiply(3,4)
full_name(
    'Erick',
    'Avila',
    'Sr.'
)