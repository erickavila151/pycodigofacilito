name = 'Erick'
last_name = 'Avila'


#1
full_name = name + ' ' + last_name + ' ' + str(30)
print(full_name)

#2
full_name = ' '.join([name, last_name, str(30)])
print(full_name)

#3 esta estructura no es muy utilizada, mayoritariamente se usan en los registros de logs
full_name  = 'El nombre completo es %s %s' %(name, last_name)

print(full_name)