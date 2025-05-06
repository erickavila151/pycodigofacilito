"""
lambda <parámetros>: <body> #Siempre retornan un valor. 

"""

add = lambda number1, number2=0: number1 + number2 #no es necesario usar return, ya que siempre
#va a retornar el resultado del cuerpo de la función

print(add(10))
print(add(20, 10))