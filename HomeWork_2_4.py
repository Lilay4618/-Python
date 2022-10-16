# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

def create_list_main():
    n = int(input('Введите значение N: '))
    lst = list(range(-n, n + 1))
    return lst

def open_file(x):
    text_in_file = open(x, 'r')
    list_from_file = []
    for line in text_in_file:
        list_from_file.append(int(line))
    text_in_file.close
    return list_from_file

def multiplication(x , y):
    result = 1
    for i in range(len(y)):
        num = y[i]
        if(num < len(x)):
            result = result * x[num]
    return result

list_main = create_list_main()
list_double = open_file('for_2_4.txt')
print(f'Основной список: {list_main}')
print(f'Позиции элементов для перемножения в основном списке(при их наличии): {list_double}')
print(f'Произведение элементов основного списка на позициях из предоставленного файла = {multiplication(list_main, list_double)}')