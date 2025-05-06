def outer_function():
    message = 'Hola nos encontramos en una función anidada'
    
    def inner_function():
        info = 'Info value'
        print(message)
        print(info)

    
    inner_function()

outer_function()