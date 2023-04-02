"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

i = 0

with open("test_1.txt", "r", encoding="utf-8") as my_file:
    my_lines = my_file.readlines()
    print(f'Количество строк в файле: {len(my_lines)}')

with open("test_1.txt", "r", encoding="utf-8") as my_file_2:
    my_lines_2 = my_file_2.readlines()
    for el in my_lines_2:
        i += 1
        print(f'Количество символов в строке {i}: {len(el.split())}')
