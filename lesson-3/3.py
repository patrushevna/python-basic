"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(*args):
    my_set = [args[0], args[1], args[2]]
    my_set.sort(reverse=True)
    print(f'Сумма наибольших чисел через sort: {my_set[0]+my_set[1]}')


def my_func2(*args):
    if args[0] >= args[2] and args[1] >= args[2]:
        print(args[0] + args[1])
    elif args[0] > args[1] and args[0] <= args[2]:
        print(args[0] + args[2])
    else:
        print(args[1] + args[2])


my_func(3, 2, 3)
my_func2(3, 2, 3)
