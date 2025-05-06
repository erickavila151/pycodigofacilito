lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java", "Rust"]
print(len(lista_cursos))
lista_curso2 = ["C", "C++", "Docker"]

lista_cursos.append("MongoDB")
lista_cursos.append("C#")
lista_cursos.append("JavaScript")


lista_cursos.insert(1, "Rails")
lista_cursos.insert(0, "PyGame")

lista_cursos.extend(lista_curso2)

print(lista_cursos)

lista_cursos.remove("MongoDB")
del lista_cursos[-1]

lista_cursos.clear()

print (len(lista_cursos))