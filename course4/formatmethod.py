name = 'Erick'
last_name = 'Avila'

#4 Format
string_base = 'El nombre completo es: {} {}. Su edad es: {}'
full_name = string_base.format(name, last_name, 30)

#4 Format - Utilizando inputs
"""name = input('ingresa tu nombre: ')
last_name = input('ingresa tu apellido: ')
age = input('Ingresa tu edad: ')

string_base = 'El nombre completo es: {} {}. Su edad es: {}.'
full_name = string_base.format(name, last_name, age)"""

#4 Format - con los placeholders teniendo un nombre para la variable correspondiente
string_base = 'El nombre completo es: {name} {last_name}. Y su edad es: {age}. Active: {active}'
full_name = string_base.format(
    name=name,
    last_name=last_name,
    age=30,
    active = True

)


print(full_name)
