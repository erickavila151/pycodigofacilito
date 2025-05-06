title = 'Curso profesional de Python!'
#para python es importante las mayusculas y minusculas, es sensible a ellas
#para solucionar este problema necesitamos estandarizar nuestros strings
#el metodo lower generará un nuevo string todo en minusculas
print(
  'curso' in title.lower()
)
#Hace que el string sea todo en mayusculas
print(
    title.upper()
)
#Count retorna la cantidad de veces que el argumento en parentesis está en el string
print(
    title.count('a')
)
#Nos permite saber con que caracteres EMPIEZA el string o substring
print(
    title.startswith('C')
)
#Nos pemire saber con que caracteres TERMIN un string o substring
print (
    title.endswith('Python!')
)