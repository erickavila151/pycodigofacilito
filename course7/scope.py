#Scope
#Global - Local

username = 'Cody' #Global

def show_info():
    username = 'Erick' #Local
    last_name = 'Avila'
    print(id(username))
    print(id(last_name))

show_info()

print(id(username))