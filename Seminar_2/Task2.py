# Напишите программу, которая принимает две строки вида
# “a/b” - дробь с числителем и знаменателем. Программа
# должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction as frac

FIRST_FRACTION = frac(input("Введите первую дробь: \n"))
SECOND_FRACTION = frac(input("Введите вторую дробь: \n"))

print ("Сумма дробей = ", FIRST_FRACTION + SECOND_FRACTION)
print ("Произведение дробей = ", FIRST_FRACTION * SECOND_FRACTION)
