#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def random_list():
    rand_list = []
    n = int(input('Введите размер списка: '))
    for i in range(n):
        rand_list.append(random.randint(3,9))
    print(rand_list)
    return rand_list

def find_sum(x):
    result = 0
    for i in range(len(x)):
        if i % 2 != 0:
            result += x[i]
    print(result)

find_sum(random_list())
