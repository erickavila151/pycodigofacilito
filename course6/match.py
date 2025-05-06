score = 5

match score:
    case 10:
        print('Muchas felicidades, tu calificación es 10.')
    case 9 | 8:
        print('Felicidades, calificación aprobatoria')
    case 6 | 7:
        print('Aprobaste la materia')
#default
    case _:
        print('Calificación no aprobatoria')