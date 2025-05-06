message = 'Hola mundo!'

print(message)
print(
    type(message)
)
print(
    len(message)
)
print('?' in message)
print(message.index ('!'))


print(message[10])
#Los strings son inmutables, no podemos modificarlos, pero si podemos utilizarlos para generar nuevos
message2 = 'h' + message[1:]
print(message2)




