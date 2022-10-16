#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('Введите число: '))

def get_fib(x):
    arr = []
    a, b =  1, 1
    for i in range (x):
        arr.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (x+1):
        arr.insert(0, a)
        a, b = b, a - b
    return arr
   
arr_fibo = get_fib(num)
print(get_fib(num))
