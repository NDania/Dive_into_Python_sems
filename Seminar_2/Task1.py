# Напишите программу, которая получает целое число
# и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

NUM = int(input("Введите целое число: \n"))

DIVIDER = 16
result = ""

print (hex(NUM))   #проверка

while NUM > 0:
    result += str(NUM % DIVIDER)
    NUM //= DIVIDER

result = result[::-1]
print (result)