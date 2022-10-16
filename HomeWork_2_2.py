#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math

input = int(input('Введите число N: '))
def result(number):
    sum = 1
    while(number != 1):
        sum = sum * number
        number = number - 1
    return(sum)
    
result(input)
lst = [ math.factorial(i) for i in range(1, input + 1)]
print(f'Пусть N = {input}, тогда {lst}')

