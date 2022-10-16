#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#[1.1, 1.2, 3.1, 5, 10.01] => 0.20

import random

def random_list():
    rand_list = []
    n = int(input('Введите размер списка: '))
    for i in range(n):
        rand_list.append(round(random.uniform(1, 10), 2))
    print(rand_list)
    return rand_list

def diff(arr):
    min = 1
    max = 0 
    for i in range(len(arr)):
        if arr[i] - int(arr[i]) < min:
            min = round(arr[i] - int(arr[i]), 2)
        if arr[i] - int(arr[i]) > max:
            max = round(arr[i] - int(arr[i]), 2)
    print(f'min: {min}')
    print(f'max: {max}')
    print(max - min)

diff(random_list())