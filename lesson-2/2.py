'''
Для списка реализовать обмен значений соседних элементов.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
При нечётном количестве элементов последний сохранить на своём месте.
Для заполнения списка элементов нужно использовать функцию input().
'''

my_list = input('Введите список ').split()

for el in range(0, len(my_list) - 1, 2):
    my_list[el], my_list[el+1] = my_list[el+1], my_list[el]

print(my_list)
