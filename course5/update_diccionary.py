user = {
    #llave   Valor
    'name': 'User1',
    'age' : 10,
    'active' : True,
    'courses': [
        'Python', 'Django', 'Redis'
    ],
    'settings' : (123, True),
}
#modify
#user['name'] = 'Codigo'
#new
#user['last_name'] = 'facilito'

#metodo update

courses = user.get('courses', [])
courses.append('Ruby On Rails')
courses.append('Rust')


user.update(
    {
        #update si ya existe la llave
        'name' : 'Cody',
        #adding si no existe la llave
        'last_name' : 'Facilito',
        'courses' : courses
    }
)

#Metodo set default
#Intenta obtener el valor de la llave, si no existe, la creará
user.setdefault('id', 100)

del user['courses']

value = user.pop('settings')

#conocer la cantidad de pares de llaves y valores que hay en el diccionario
print(len(user))
print(user, value)