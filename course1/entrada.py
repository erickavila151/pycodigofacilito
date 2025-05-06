"""
nombre_completo = input("Ingresa tu nombre completo: ") #str
print(nombre_completo)
edad = input("Ingresa tu edad: ")
edad = int(edad)
altura = input("Ingresa tu altura: ")
altura = float(altura)
autorizacion = input("¿autorizas el programa?: (si/no): ")
autorizacion = autorizacion == "si"
print(edad,altura,autorizacion)
print(type(edad))
print(type(altura))
"""
#Optimización de código
nombre_completo = input("Ingresa tu nombre completo: ")
edad = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu altura: "))
autorizacion = input("¿autorizas el programa?: (si/no): ") == "si"
print(nombre_completo,edad,altura,autorizacion)