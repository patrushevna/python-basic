"""
6)	Необходимо создать (не программно) текстовый файл,
где каждая строка описывает у
чебный предмет и наличие лекционных, практических и
лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь,
содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
                    Информатика:   100(л)   50(пр)   20(лаб).
                    Физика:   30(л)   —   10(лаб)
                    Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

import re

my_dict = {}

with open("test_5.txt", "r", encoding="utf-8") as my_file:
    for el in my_file:
        my_value = sum([int(i) for i in re.findall(r'-?\d+\.?\d*', el)])
        my_key = el.split()[0]
        my_dict[my_key] = my_value

print(f"Результат: {my_dict}")
