#Primer ejercicio
"""numbers = [2, 3, 5]
suma = numbers[0] + numbers[2]
print(suma)"""

#segundo ejercicio
"""numbers = [4, 5, 3, 9]
suma_total = sum(numbers)
print(suma_total)"""

"""#tercer ejercicio
strings_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
new_list = strings_list[:3] + strings_list[-3:]
print(new_list)"""

#cuarto ejercicio
"""strings_list = ["a", "b", "C", "d", "e", "f", "g", "h", "i", "j"]
print("'CodigoFacilito'" in strings_list)"""

#quinto ejercicio
matrix = [
    [2, 5, 7],
    [4, 9, 1],
    [6, 8, 3]
]
# Verificamos si el primer elemento de cada fila es par
resultado = all(fila[0] % 2 == 0 for fila in matrix)
# Imprimimos el resultado
print("¿El primer elemento de cada fila es par?:", resultado)



