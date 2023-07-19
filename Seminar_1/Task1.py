#Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
#стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
#двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
#с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
#равнобедренным или равносторонним.

FIRST_SIDE = int(input("Введите длину первого отрезка в см: \n"))
SECOND_SIDE = int(input("Введите длину второго отрезка в см: \n"))
THIRD_SIDE = int(input("Введите длину третьего отрезка в см: \n"))

sum1 = SECOND_SIDE + THIRD_SIDE
sum2 = FIRST_SIDE + THIRD_SIDE
sum3 = FIRST_SIDE + SECOND_SIDE

if FIRST_SIDE < sum1 and SECOND_SIDE < sum2 and THIRD_SIDE < sum3:
    if FIRST_SIDE == SECOND_SIDE == THIRD_SIDE:
        print ("Треугольник равносторонний")
    elif FIRST_SIDE == SECOND_SIDE and FIRST_SIDE != THIRD_SIDE or FIRST_SIDE != SECOND_SIDE and FIRST_SIDE == THIRD_SIDE or SECOND_SIDE == THIRD_SIDE:
        print ("Треугольник равнобедренный")
    else:
        print ("Это обычный треугольник.")    
else:
    print("Треугольник с такими сторонами не существует.")
