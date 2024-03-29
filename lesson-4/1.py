"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""


from sys import argv

name, hours, rph, bonus = argv

try:
    print(f'Зарплата {name} равна {int(hours) * int(rph) + bonus}')
except ValueError:
    print('ValueError')
