courses = (
#    0           1         2           3            4
    "Python", "Django", "Ruby", "Ruby on Rails", "MySQL"
)

"""var1 = courses[0]
var2 = courses[1]
var3 = courses[2]
var4 = courses[3]
var5 = courses[4]"""
#Siempre que estemos trabajando con valores divididos por una coma es una tupla
"""var1,var2,var3,var4,var5 = courses[0], courses[1], courses[2], courses[3], courses[4]"""
#esto es lo mismo que arriba, separado por comas = Tupla
"""var1,var2,var3,var4,var5 = "Python", "Django", "Ruby", "Ruby on Rails", "MySQL"""
#optimización del mismo concepto, se asignan sus valores en orden de izquierda a derecha
var1,var2,var3,var4,var5 = courses

print(
    var1,var2,var3,var4,var5
)