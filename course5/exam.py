#primer ejercicio
"""my_dictionary = {
    'name' : '',
    'age' : '',
    'course' : ''
}
print(my_dictionary)"""

#Segundo ejercicio
"""my_dictionary = {'name':  'Cody', 'age': 12, 'course': 'python'}

lista = list(my_dictionary.keys())
lista2 = '-'.join(lista)
print(lista2)"""

#tercer ejercicio

"""my_dictionary = {'name':  'Cody', 'age': 12, 'course': ['Python', 'HTML', 'CSS']}
print(my_dictionary)"""

#Cuarto ejercicio

my_dictionary = {'name':  'Cody'
                 , 'age': 12, 
                 'course': ['python', 'ruby', 'javascript']}

del my_dictionary['course']

my_dictionary.update(
    {
        'age' : 20,
        'active' : True,
        'courses' : ['python', 'ruby', 'javascript']
    }
)

print(my_dictionary)