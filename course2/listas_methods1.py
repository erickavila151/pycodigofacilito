courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"] 
#sublista que se añadirá a la original usando extend
new_courses =["React", "Next"]
courses.append("Ruby On Rails")
courses.append("PHP")
courses.append("Laravel")

courses.insert(2, "HTML")
courses.insert(3, "JavaScript")
#extend añadiendo los elementos al final
courses.extend(new_courses)

#Eliminar de un listado
courses.remove("Python")

#Eliminar siempre el ultimo elemento de la lista
courses.pop()

#Eliminar un indice en especifico
courses.pop()

#Eliminar TODOS los elementos de la lista

courses.clear()

#al insertar todos los elementos pasan a recorrerse a la derecha
print(courses)
print(len(courses))

#conocer si un elemento se encuentra o no dentro de la lista

"""print(
    "Python" in courses
    )
print(courses.index("Next"))"""