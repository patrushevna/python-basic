"""
Задание 2.
Создайте собственный!!! класс-исключение,
обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля
в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class OwnError(Exception):

    def __init__(self, txt):
        self.txt = txt


numerator = int(input('Введите числитель: '))
denominator = int(input('Введите знаменатель: '))

try:
    if denominator == 0:
        raise OwnError('Делить на ноль нельзя')
except OwnError as err:
    print(err)
else:
    print(f'Равно: {(numerator / denominator):.2f}')
