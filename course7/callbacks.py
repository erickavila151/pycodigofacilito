def deposit(balance, amount=0):
    return balance + amount

def withdraw(balance, amount=0):
    if amount > balance:
        return None
    
    return balance - amount

def default(*args, **kwargs):
    return ">>> Lo sentimos, opción no valida"
                    #PARAMETROS
def handle_operation(callback, *args, **kwargs): 
                    #PASANDO DE FORMA INTEGRA 
   result = callback(*args, **kwargs)
   print("El resultado es", result)

#Evitar poner parentesis, ya que estaríamos llamando a la función
#Almacenamiento de funciones en variables
func1 = deposit 
func2 = withdraw

options = {
    "a": deposit,
    "b": withdraw
}

option = input("Ingresa una opción (a/b): ")
balance = int(input("Ingresa tu balance: "))
amount = int(input("Ingresa tu cantidad: "))

function = options.get(option, default)
total = function(balance, amount)
print(total)


handle_operation(
    callback=function,
   balance = balance,
   amount = amount
)


