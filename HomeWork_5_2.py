# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint
from secrets import choice

def player_vs_player():
    max_candies = 2021
    max_step = 28
    message = ['Ну же, ходи', 'Скорее бери конфету', 'Решайся', 'Не тормози, конфету возьми' ]
    count = 0
    print('\nМы начинаем игру!\n')
    player_1 = input('\nИгрок № 1, как тебя зовут?\n')
    player_2 = input('\nИгрок № 2, а тебя?\n')
    print('\nОпределим, кто первый...\n')
    x = randint(1, 2)
    if x == 1:
        win = player_1
        fall = player_2
    if x == 2:
        win = player_2
        fall = player_1
    print(f'\nХодит {win}!\n')
    print('\nСо стола берём не более 28 конфет! Начинай!\n')
    while max_candies > 0:
        while count == 0:
            step = int(input(f'\n{choice(message)}, {win}\n'))
            if step > max_step:
                print('\nХватит жадничать! Не больше 28 штук за раз!\n')
            elif step > max_candies:
                print(f'\nОсталось всего {max_candies} конфет! Ты не можешь взять больше!\n')
            else:
                max_candies = max_candies - step
                if max_candies > 0:
                    print(f'\nОсталось {max_candies} конфет. Играем дальше.\n')
                    count = 1
                else:
                    print(f'\nСтоп Игра! Победа за {win}\n')
        if count == 1:
            step = int(input(f'\n{choice(message)}, {fall}\n'))
            if step > max_step:
                print('\nХватит жадничать! Не больше 28 штук за раз!\n')
            elif step > max_candies:
                print(f'\nОсталось всего {max_candies} конфет! Ты не можешь взять больше!\n')
            else:
                max_candies = max_candies - step
                if max_candies > 0:
                    print(f'\nОсталось {max_candies} конфет. Играем дальше.\n')
                    count = 0
                else:
                    print(f'\nСтоп Игра! Победа за {fall}\n')

def player_vs_pc():
    max_candies = 2021
    max_step = 28
    message = ['Ну же, ходи', 'Скорее бери конфету', 'Решайся', 'Не тормози, конфету возьми' ]

    print('\nМы начинаем игру!\n')
    player_1 = input('\nИгрок № 1, как тебя зовут?\n')
    player_2 = input('\nА твоего вымышленного соперника?\n')
    print('\nОпределим, кто первый...\n')
    x = randint(1, 2)
    if x == 1:
        win = player_1
        fall = player_2
        count = 0
    if x == 2:
        win = player_2
        fall = player_1
        count = 1
    print(f'\nХодит {win}!\n')
    print('\nСо стола берём не более 28 конфет! Начинай!\n')
    while max_candies > 0:
        if count == 0:
            step = int(input(f'\n{choice(message)}, {player_1}\n'))
            if step > max_step:
                print('\nХватит жадничать! Не больше 28 штук за раз!\n')
            elif step > max_candies:
                print(f'\nОсталось всего {max_candies} конфет! Ты не можешь взять больше!\n')
            else:
                max_candies = max_candies - step
                if max_candies > 0:
                    print(f'\nОсталось {max_candies} конфет. Играем дальше.\n')
                    count = 1
                else:
                    print(f'\nСтоп Игра! Победа за {player_1}\n')
            print('-----------------------------------------------------------------')
        if count == 1:
            if max_candies >= 28:
                step = randint(1, 28)
                print(f'\n{player_2} берёт {step} конфет\n')
            else:
                step = max_candies
            max_candies = max_candies - step
            if max_candies > 0:
                print(f'\nОсталось {max_candies} конфет. Играем дальше.\n')
                count = 0
            else:
                print(f'\nСтоп Игра! Победа за {player_2}\n')
            print('-----------------------------------------------------------------')


player_vs_pc()



