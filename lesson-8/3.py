"""
Задание 3.
Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять
список только числами.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class OwnError(Exception):

    def __init__(self, txt):
        self.txt = txt


my_list = []

while True:
    my_value = input('Введите число: ')
    try:
        if my_value == 'quit':
            print(my_list)
            break
        elif my_value.isdigit() is not True:
            raise OwnError('Вы неправильно')
    except OwnError as err:
        print(err)
    else:
        my_list.append(my_value)
