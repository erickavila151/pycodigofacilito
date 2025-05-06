# * (Posición) - Agrupados en una tupla
# ** (Nombres) - Diccionario

'''def show_info(*args, **kwargs):
    print('>>> info')
    for value in args:
        print(value)
    print('\n')
    print(">>> Details")
    for key, value in kwargs.items():
        print(key, value)

#asignando valores por posición
show_info(
    'Erick', 'Avila', 12, 'erickavila414@gmail.com',
#Asignando valores por nombre usando un diccionario
    courses = ['Python', 'Django', 'Flask'],
    score = 10,
    active = True

)'''


def show_info(username, lastname, *args, active=True, is_super_admin=False, **kwargs):
    print('Username', username)
    print('Lastname', lastname)


    print('>>> Extra info: ')
    for value in args:
        print(value)
    print('Active', active)
    print('Super admin', is_super_admin)
    
    print(kwargs)

show_info(
    'Cody', 'Facilito',
    'erickavila414@gmail.com', 'password123', #args
    courses =['Python', 'Flask'], is_deleted = False #kwargs
)