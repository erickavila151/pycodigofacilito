numbers = (
    1, 4, 5, 3, 3, 7, 2, 10
)
#len = cantidad de elementos que posee una colección
print(
    len(numbers)
)
#sorted organiza de forma ordenada de manera ascendente - menos a más
print(
    sorted(numbers)
)
#sorted con el párametro reverse = True organizará de manera descendente
print(
    sorted(numbers, reverse=True)
)
#count nos retorna cuantas veces se encuentra un elemento en la colección
print(
    numbers.count(3)
)
#In nos devolverá un valor booleano al comprobar si el elemento se encuentra en la
#colección
print(
    3 in numbers #True / False
    #True -> 1
)
#index nos permite saber en que indice esta ubicado el valor que le ponemos dentro
#en este caso el numero 4 se encuentra en el indice número 1
print(
    numbers.index(4)
)