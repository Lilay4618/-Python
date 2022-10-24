#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

def random_list():
    rand_list = []
    n = int(input('Введите размер списка: '))
    for i in range(n):
        rand_list.append(random.randint(1, 10))
    return rand_list

lst = random_list()
unique_lst = list(set(lst))

print(f'Основной список: {lst}')
print(f'Список из неповторяющихся элементов: {unique_lst}')

