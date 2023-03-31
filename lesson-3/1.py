"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).
Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!
Process finished with exit code 0
Пример:
Введите первое число: 10
Введите второе число: 10
1.0
Process finished with exit code 0
"""


def my_func(*args):
    try:
        return args[0] / args[1]
    except ZeroDivisionError:
        return 'Вы что? Пытаетесь делить на 0!'


try:
    first_number = int(input("Введите первое число: "))
    second_number = int(input("Введите второе число: "))
    print(my_func(first_number, second_number))
except ValueError:
    print('ValueError')
