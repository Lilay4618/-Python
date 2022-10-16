#Реализуйте алгоритм перемешивания списка.

import random
def mix_list(original_list):
    copy_list = original_list[:]
    list_length = len(copy_list)
    for i in range(list_length):
        index = random.randint(0, list_length - 1)
        temp = copy_list[i]
        copy_list[i] = copy_list[index]
        copy_list[index] = temp
    return copy_list

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mixed_list = mix_list(test_list)
print("Исходный список: ")
print(test_list)
print("Перемешанный список: ")
print(mixed_list)
