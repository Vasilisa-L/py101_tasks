"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""

if __name__ == '__main__':
    user_password = input('Enter pass > ')
    flag_length = len(user_password) >= 8
    flag_letters = False
    flag_numbers = False
    for i in user_password:
        if i.isdigit(): 
            flag_numbers = True
        if i.isalpha(): 
            flag_letters = True 
    if flag_length and flag_letters and flag_numbers:
        print('Сложный')
    else:
        print('Простой:')
        if not flag_length:
            print('\tПароль должен быть минимум 8 символов')
        if not flag_numbers:
            print('\tПароль должен содержать минимум 1 цифру')
        if not flag_letters:
            print('\tПароль должен содержать минимум 1 букву')
