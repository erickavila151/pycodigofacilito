# * (Posición) - Agrupados en una tupla
# ** (Nombres)

def show_info(username, email, *scores):
    print(username)
    print(email)
    
    average = sum(scores) / len(scores)
    print(average)



show_info(
    'Erick',
    'erickavila414@gmail.com',
    10, 10, 8, 9, 6, 9 #Tupla
)