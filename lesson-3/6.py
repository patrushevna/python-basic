"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def my_func(my_list):
    result = []
    for el in my_list:
        result.append(el.title())
    print(' '.join(result))


# my_line = input('Введите строку из слов разделенную пробелами: ').split()
my_line = ('hello world and you').split()
my_func(my_line)
