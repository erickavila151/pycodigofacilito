numbers = [1, 2, 3, 4, 5]
message = 'Hola mundo'
diccionary = {
    'name': 'User',
    'age': 17,
    'password': 'password123'
}

#la variable va a almacenar todos los elementos de una colección
#por cada iteración cambiarâ de valor
'''
for <variable> in <collection>:

'''

for n in numbers:
    print('Hola, el valor de la variable es', n)

for caracter in message:
    print(caracter)

#Desempaquetado de tuplas dentro del for
for hola, adios in diccionary.items():
    print('La llave es', hola, 'el valor es', adios )
    