"""
Программа генерирует число от 0 до 1_000_000 и предлагает угадать его.

Программа должна приветствовать пользователя и считывать число с клавиатуры
Если число меньше загаданного, то программа выводит сообщение о том, что число
меньше
Если больше загаданного, то программа выводит сообщение о том, что больше

Программа должна выводить сообщения-предупреждения, если:
* пользователь ввёл не число
* число не входит в обозначенный в условии диапазон
Если пользователь ничего не ввёл/ввёл "exit", то происходит выход из программы.

Тебе может понадобится модуль random, цикл while и ветвления
"""
from random import randint
import sys

if __name__ == '__main__':
    print('Hey, darling!\nAre u ready for a little game?\nI\'m thinking of a number from one to 1000000\nCan u guess it?')
    grange = 100
    number_to_guess = randint(0, grange)
    user_number = 0
    while user_number != number_to_guess:
        user_number = input('Any guess? > ')
        if user_number == '' or user_number == 'exit':
            sys.exit()
        try:
            user_number = int(user_number)            
        except ValueError:
            print('Stop doing that! That\'s not a number! Try again!')
            continue
        if user_number < 0 or user_number > grange:
            print('Not in range! Try again!')
            continue
        elif int(user_number) > number_to_guess:
            print('Too much. My number is less.')
        elif int(user_number) < number_to_guess:
            print('You need something greater.')
    print('You got it! Goog job!')
            