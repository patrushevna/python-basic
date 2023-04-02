"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу,
открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

rus = ["Один ", "Два ", "Три ", "Четыре "]
i = 0
result = []
with open("test_2.txt", "r", encoding="utf-8") as my_file:
    for el in my_file:
        el = el.split(' ', 1)
        el[0] = rus[i]
        result.extend(el)
        i += 1
    # print(result)

with open("result.txt", "w", encoding="utf-8") as my_file:
    my_file.writelines(result)
