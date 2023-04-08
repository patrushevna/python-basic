"""
5)	Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

my_list = input('Введите список: ')
summa = 0

with open("test_4.txt", "w", encoding="utf-8") as my_file:
    my_file.write(str(my_list))

with open("test_4.txt", "r", encoding="utf-8") as my_file_2:
    my_list_2 = my_file_2.read()
    for el in my_list_2.split():
        summa += int(el)
    print(f"Сумма числе в файле = {summa}")
