
from random import randint


k = int(input('Введите натуральную степень k: '))

def write_file_1(info):
    with open('FileWithCoef_1', 'w') as data:
        data.write(info)

def write_file_2(info):
    with open('FileWithCoef_2', 'w') as data:
        data.write(info)
 
def create_list(x):
    list = []
    for i in range(x + 1):
        list.append(randint(2, 9))    
    return list
    
def create_str(k):
    list = k[::-1]
    result = ''
    if len(list) < 1:
        result = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                result += f'{list[i]}x^{len(list) - i - 1}'
                if list [i + 1] != 0:
                    result += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                result += f'{list[i]}x'
                if list[i + 1] != 0:
                    result += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                result += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                result += ' = 0'
    return result
 
write_file_1(create_str(create_list(k)))
write_file_2(create_str(create_list(k)))




