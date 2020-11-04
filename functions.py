"""Задания по ветвлениям, итерациям и вводу данных."""

# напиши функцию, которая принимает на вход любое
# количество чисел и сообщает, есть ли среди них чётное
def find_even(num_string):
    num_list = num_string.split(' ')
    flag = False
    for number in num_list:
        try:
            number = int(number)
            if number % 2 == 0:
                flag = True
        except ValueError:
            print('Passing "' + number + '". This is not a number.')
    print('Even is found') if flag else print('No even numbers')

# используй тернарный оператор, чтобы вызвать функцию
# если возраст больше 21 года, в противном случае верни
# сообщение "Мы не продаём алкоголь несовершеннолетним."
def sell_alcohol():
    print('Price 17$')

age = 17
sell_alcohol() if age >= 21 else print("Мы не продаём алкоголь несовершеннолетним.")


# напиши функцию, которая проверит, является ли строка ключевым словом в Питоне
# тебе понадобится модуль keyword, импортируй его и изучи с помощью dir()

from keyword import iskeyword

def is_keyword(string):
    print(string + ' is a python keyword') if iskeyword(string) else print (string + ' is not a keyword')


# напиши функцию, которая возвращает тип данных на русском языке:
# число, строка, булевый, None, список, кортеж, множество, словарь
# пример: get_type("что-то") возвращает "Это строка."
# пример2: get_type(42) возвращает "Это словарь."

def get_type(sth):
    if sth == None:
        return "None"
    var_type = type(sth)
    if var_type == int:
        return "Это число"
    elif var_type == str:
        return "Это строка"
    elif var_type == bool:
        return "Это булевый тип"
    elif var_type == list:
        return "Это список"
    elif var_type == tuple:
        return "Это кортеж"
    elif var_type == set:
        return "Это множество"
    elif var_type == dict:
        return "Это словарь"
    else:
        return "Что это?"
