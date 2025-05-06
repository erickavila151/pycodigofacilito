'''
def <nombre_de_la_funcion>(<parámetros, >):
    ...
'''

def division(number1, number2):
    if number1 == 0 or number2 == 0:
        return None
    return number1 / number2

print(
    division(10, 5)
)

def multiply(number1, number2):
    result = number1 * number2
    return result

def full_name(first_name, last_name, prefix):
    full_name = f'{prefix} {first_name} {last_name}'
    return full_name

result = multiply(10, 5)
print( result)

user_full_name = full_name('Erick', 'Avila', 'Ing.')
print(
    f"Hola, el nombre del usuario es {user_full_name}"
)

print(
    full_name(
        first_name='Erick',
        last_name='Javier',
        prefix="test"
    )
)