def foo():
    #Automáticamente se crea una tupla
    return 'Cody', True, 12
result = foo()

username, active, age = foo()
print(username,active,age)