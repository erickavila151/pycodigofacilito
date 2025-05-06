# * (Posición) - Agrupados en una tupla
# ** (Nombres) - Diccionario

def show_info(**user):
    for key, value in user.items():
        print(key, '-', value)

show_info(
    username = 'Erick',
    email = 'erickavila414@gmail.com',
    password = '1234',
    active = True,
    courses = ['Python', 'Django', 'Flask'],
    last_login = '2024',
    is_super_user = True

)
