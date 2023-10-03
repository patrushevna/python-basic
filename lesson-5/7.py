"""
7)	Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка:
[{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

import json

com_dict = {}
summa_profit = 0
i = 0

with open("test_6.txt", "r", encoding="utf-8") as my_file:
    for el in my_file:
        my_key = el.split()[0]
        profit = int(el.split()[2]) - int(el.split()[3])
        if profit >= 0:
            summa_profit += profit
            com_dict[my_key] = profit
            i += 1
        else:
            com_dict[my_key] = profit

aver_profit = summa_profit / i
aver_dict = {"average_profit": aver_profit}
my_dict = [com_dict, aver_dict]

with open("test.json", "w") as my_file:
    json.dump(my_dict, my_file)
