"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

while True:
    my_line = input("Вводите тест, пустая строка выход: ")
    if not my_line:
        print(my_line)
        break
    with open('test_1.txt', 'a') as file_obj:
        file_obj.writelines(my_line + '\n')
    my_line = []
