def deposit(balance, amount=0):
    return balance + amount

def withdraw(balance, amount=0):
    if amount > balance:
        return None
    
    return balance - amount

def default(*args, **kwargs):
    return ">>> Lo sentimos, opción no valida"

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


