courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"]
#Sublista - Recordar que el ultimo elemento no se imprime, es el limite.
#Slicing: [start:end:skips]
new_list = courses[0:2]
courses_copy = courses[:]

print(courses_copy) #Shallow Copy - copia de la original