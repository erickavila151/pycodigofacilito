#Primer ejercicio
"""my_tuple = (1, 2, 3)
print(my_tuple[2])"""

#segundo ejercicio

"""my_tuple = ('Hola','Como', 'Estas', 'Hoy', 'Viernes')

var1 = my_tuple[0]
var2 = my_tuple[3]
var3 = my_tuple[4]

print(var1, var2, var3)"""

"""#tercer ejercicio

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = list(zip(lista [1::2]))
print(pares)"""
# Definimos la lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Generamos una tupla con los números pares
pares = tuple(num for num in lista if num % 2 == 0)

# Imprimimos la tupla
print("Números pares en la tupla:", pares)