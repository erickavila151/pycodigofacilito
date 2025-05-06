# clave (llave) : valor  
#N cantidad de claves y valores, donde a 
#cada clave le corresponde un valor y vicervesa
#las claves (llaves) son inmutables y 99% son siempre Strings aunque
#pueden ser listas, tuplas, enteros y booleanos
user = {
    #Clave   Valor
    'name': 'User1',
    'age' : 10,
    'active' : True,
    'courses': [
        'Python', 'Django', 'Redis'
    ],
    'settings' : (123, True)
}
print(user)