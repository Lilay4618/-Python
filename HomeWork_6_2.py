# 2 – Дана последовательность чисел. Получить список уникальных элементов заданной последовательности, 
#список повторяемых и убрать дубликаты из заданной последовательности.
#Пример:
#[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

from random import randint, random

rand_list = []
n = int(input('Введите размер списка: '))
for i in range(n):
    rand_list.append(randint(1,10))
print(f'Основной список: {rand_list}')

unique = [i for i in rand_list if rand_list.count(i) == 1]
print(f'Список уникальных элементов: {unique}')

count_list = []
for i in rand_list:
    count = 0
    for x in rand_list:
        if x == i:
            count += 1
    count_list.append(count)

not_unique = set()
index = 0
while index < len(rand_list):
    if count_list[index] != 1:
        not_unique.add(rand_list[index])
    index += 1

print(f'Список повторяющихся элементов: {not_unique}')

kill_dupl = list(set(rand_list))
print(f'Список без дубликатов: {kill_dupl}')

