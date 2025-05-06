#zip

#Colecciones
users = ["user1", "user2", "user3"] #Lista
courses = ("Python", "Django", "Rails") #Tupla
scores = [10, 8, 7]

response = list(zip(users, courses, scores))
print(response)