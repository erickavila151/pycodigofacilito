title = '   Curso Profesional de Python!   '
#Aqui ya hemos estandarizado title eliminando los caracteres en blanco
title = title.strip()
print(title.upper())
print(title.lower())

#Metodo strip podemos eliminar todos los caracteres en blanco al inicio y al
#final de la sentencia
'''print(title.strip())'''

#Metodo find va a retornar el indice en donde se encuentra un caracter y siempre
#sera del primero que encuentre
print(
    title.find('o')
)

#El metodo isnumeric nos devolvera verdadero o falso si el string es entero

print('6'.isnumeric())

#el Metodo capitalize va a poner en mayúscula el primer caracter

message = 'codigo facilito'

print(
    message.capitalize()
)

#obtener el mismo resultado usando f strings

print(f'{message[0].upper()}{message[1:]}')