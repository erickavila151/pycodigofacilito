#clave (llave) : valor
#keys, values, items
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
#metodo Keys
print(list(user.keys()))
print(tuple(user.keys()))

#Metodo Values

print(user.values())
print(list(user.values()))

#Metodo Items

print(user.items())
print(list(user.items()))