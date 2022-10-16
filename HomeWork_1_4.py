#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

numberQuarter = int(input('Введите номер четверти оси координат: '))

def range(randomQuarter):
    if(randomQuarter == 2):
        return 'X(0; -∞), Y(0; ∞)'
    elif(randomQuarter == 1):
        return 'X(0; ∞), Y(0; ∞)'
    elif(randomQuarter == 3):
        return 'X(0; -∞), Y(0; -∞)'
    elif(randomQuarter == 4):
        return 'X(0; ∞), Y(0; -∞)'
    
print(range(numberQuarter))