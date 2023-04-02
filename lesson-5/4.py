"""
3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

i = 0
summa = 0
counts = 0
my_dict = {}
result = []
with open("test_3.txt", "r", encoding="utf-8") as my_file:
    for el in my_file:
        (key, value) = el.split()
        my_dict[key] = float(value)

for key, value in my_dict.items():
    if value <= 20000:
        result.append(key)
    summa += value
    counts += 1

print(f'Имеют меньше 20к: {", ".join(result)}')
print(f'Средняя зп: {summa / counts}')
