#split -> lista

#join -> String

#Sring
#Los espacios son caracteres
courses = 'Python, PHP, Ruby, Django, MongoDB, Ruby On Rails'

#En este caso el espacio en blanco es la forma de decirle al split que se base
#en eso para hacer el split.
list_courses = courses.split(' ')
#Esto generará un problema si se intenta poner en la lista algo que requiera un 
#espacio en su nombre, ya que lo dividirá y perderá el sentido, para arreglar esto
#le diremos que las condiciones del split ahora son que lleve una coma y un espacio
list_courses = courses.split(', ')
print(courses)
#a partir del string original hemos obtenido una lista
print(list_courses)


courses = ['Python', 'Ruby', 'Ruby on Rails', 'MongoDB']
#el argumento de join es lo que decidirá por que caracteres se dividirá la lista
#en este caso, por un espacio.
#Se puede utilizar cualquier string para hacer el join
messages_courses = ', '.join(courses)
print(messages_courses)
print(
    type(messages_courses)
)