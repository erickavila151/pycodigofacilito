def factory_operation(option):

    def deposit(balance, amount = 0):
        return balance + amount

    def withdraw(balance, amount = 0):
        if amount > balance:
            return None
        return balance - amount
    
    default = lambda *args, **kwargs : '>>> Lo sentimos, opción no válida.'

    if option == 'deposit':
        return deposit
    elif option == 'withdraw':
        return withdraw
    else:
        return default
    
option = input('Ingresa una opción (deposit/withdraw)')
func = factory_operation(option)

print(func (10, 20))
print(type(func))

