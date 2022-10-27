#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_text = input('Введите текст для исправления: \n')

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)
print(f'Оригинальный текст: {my_text}')
my_text = del_some_words(my_text)
print(f'Исправленный текст: {my_text}')