'''
Реализовать структуру «Рейтинг»,
представляющую собой набор натуральных чисел,
который не возрастает.
У пользователя нужно запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться
после них.
'''

my_list = [7, 5, 3, 3, 2]
print(my_list)

element = int(input('Введите число '))
for i in range(len(my_list)):
    if my_list[i] == element:
        my_list.insert(i+1, element)
        break
    elif my_list[0] < element:
        my_list.insert(0, element)
        break
    elif my_list[-1] > element:
        my_list.append(element)
        break
    elif my_list[i] > element and my_list[i+1] < element:
        my_list.insert(i+1, element)
        break
print(my_list)
