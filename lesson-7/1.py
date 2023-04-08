"""
Задание 1.
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать
перегрузку метода __str()__ для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
Пример:
1 2 3
4 5 6
7 8 9
1 2 3
4 5 6
7 8 9
Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix:

    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) \
                            for i in self.my_matrix]))

    def __add__(self, other):
        summa_matrix = [[self.my_matrix[i][j] + other.my_matrix[i][j] \
                        for j in range(len(self.my_matrix[0]))] \
                            for i in range(len(self.my_matrix))]
        return str('\n'.join(['\t'.join([str(j) for j in i]) \
                            for i in summa_matrix]))


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(f'первая:\n{matrix1}')
print(f'вторая:\n{matrix2}')

print(f'Сумма матриц:\n{matrix1 + matrix2}')
