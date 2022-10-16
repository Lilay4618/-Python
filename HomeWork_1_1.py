#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет

DayWeekNumber = int(input('Введите номер дня недели: '))
def WhichDay(NumberDay):
    if(0 < NumberDay < 8):
        if(0 < NumberDay < 6):
            return 'Нет'
        else:
            return 'Да'
    else:
        return 'Ошибка. Неверные исходные данные'

print(WhichDay(DayWeekNumber))
