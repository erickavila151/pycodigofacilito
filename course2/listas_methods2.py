courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"]

 #copy_list = courses[:] #Shallow copy

#copy
copy_list = courses.copy()

#reverse con slicing - La lista no se modifica, se crea una nueva

#reverse_list = courses[::-1]

#reverse con metodo - La lista original se modifica
reverse_list = courses.reverse()

#sort

courses.sort(reverse=True)
print(courses)