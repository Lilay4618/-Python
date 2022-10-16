#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]

import random

def random_list():
    rand_list = []
    n = int(input('Введите размер списка: '))
    for i in range(n):
        rand_list.append(random.randint(3,9))
    print(rand_list)
    return rand_list

def mult_list(arr):
    new_list = []
    for i in range(len(arr)//2 + 1 if len(arr) % 2 !=0 else len(arr)//2):
        new_list.append(arr[i] * arr[i*(-1) - 1])
    print(new_list)
    
mult_list(random_list())