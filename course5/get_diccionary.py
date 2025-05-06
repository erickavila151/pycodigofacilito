#clave (llave) : valor
#String, tuplas, int, float, booleans, functions

user = {
    #llave   Valor
    'name': 'User1',
    'age' : 10,
    'active' : True,
    'courses': [
        'Python', 'Django', 'Redis'
    ],
    'settings' : (123, True),
    3.14 : True
}

#1. confirmar si una llave existe o no
"""print('name' in user)
print(
    user['name']
)
user_name = user['name']
print(user_name)
print(user[3.14])
"""
#Metodo GET : Intentar acceder al valor usando una llave, si la llave existe dentro
#del diccionario obtendremos su valor
                    #llave          #Valor que se imprimirá si no se encuentra
user_name = user.get('password', 'Lo siento la contraseña no existe')
print(user_name)

#Los diccionarios en python son mutables y se pueden borrar o ańadir o editar
#de la siguiente manera.

user['last_name'] = 'facilito'

print(user)
