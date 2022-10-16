# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

decimal = int(input('Введите десятичное число: '))
binary = ''
def find_num(number_a, number_b):
    while number_a > 0:
        number_b = str(number_a % 2) + number_b
        number_a = number_a // 2
    return number_b

print(f'Десятичное число = {decimal}') 
print(f'Двоичное число = {find_num(decimal, binary)}')