lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java"]
#lista_cursos[4] = "Rust"
#[start:end]
#[start:] -> obtenemos los ultimos elementos de la lista
#[:end] -> obtenemos los primeros elementos de la lista
#[start:end:skip] -> Cantidad de saltos
#también se puede hacer de forma negativa -1

#saber la cantidad de elementos que almacena mi lista

numbers = [1, 2, 3, 4, 5]
sub_lista = lista_cursos[1:]
sub_lista2 = lista_cursos [:4]
sub_lista3 = lista_cursos [0:5:2]
last_index = lista_cursos[-1]
print(last_index)
print(sub_lista3)


