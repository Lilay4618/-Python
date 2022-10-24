from itertools import zip_longest


def read_pol(file): 
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol

def convert_pol(pol): 
    pol = pol.replace(' = 0', '')
    pol = pol.split(' + ')
    pol = [i[0] for i in pol]
    for i in range (len(pol)):
        if pol [i] == 'x':
            pol[i] = '1'
    pol = pol[::-1]
    return pol

def add_list(a, b):
   c = [x+y for x, y in zip_longest(a, b, fillvalue=0)]
   return c

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

def write_file(info):
    with open('FileWithSumPoly', 'w') as data:
        data.write(info)

file_1 = 'FileWithCoef_1'
file_2 = 'FileWithCoef_2'

pol_1 = read_pol(file_1)
pol_2 = read_pol(file_2)

print(f'Многочлен №1: {pol_1}')
print(f'Многочлен №2: {pol_2}')

coef_pol_1 = list(map(int, convert_pol(pol_1)))
coef_pol_2 = list(map(int, convert_pol(pol_2)))

coef_pol = add_list(coef_pol_1, coef_pol_2)
result = create_str(coef_pol)
print(f'Сумма заданных многочленов: {result}')

write_file(result)
