#Напишите программу, которая принимает на вход координаты точки (X и Y), 
#причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#Пример:
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

x = int(input('Введите значение Х(не равное 0): '))
y = int(input('Введите значение Y(не равное 0): '))

def coordinate(coord1, coord2):
    if(x != 0 and y != 0):
        if(x > 0 and y > 0):
            return '1'
        elif(x < 0 and y > 0):
            return '2'
        elif(x < 0 and y < 0):
            return '3'
        elif(x > 0 and y < 0):
            return '4'
    else:
        return 'Нарушено условие X ≠ 0 и Y ≠ 0'        
    
print(coordinate(x, y))