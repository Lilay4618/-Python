#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input('Введите натуральное число: '))

def prime_factors(x):
   i = 2
   prime_factors = []
   while i * i <= x:
       while x % i == 0:
           prime_factors.append(i)
           x /= i
       i += 1
   if x > 1:
       prime_factors.append(x)
   return prime_factors

print(prime_factors(N))