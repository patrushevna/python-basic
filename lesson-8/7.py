"""
Задание 7.*
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта,
создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumbers:

    def __init__(self, my_number_1, my_number_2):
        self.my_number_1 = my_number_1
        self.my_number_2 = my_number_2

    def __add__(self, other):
        return ComplexNumbers(self.my_number_1 + other.my_number_1,
                              self.my_number_2 + other.my_number_2)

    def __mul__(self, other):
        self.mult_1 = self.my_number_1 * other.my_number_1
        self.mult_2 = self.my_number_2 * other.my_number_2
        self.mult_3 = self.my_number_2 * other.my_number_1
        self.mult_4 = self.my_number_1 * other.my_number_2

        return ComplexNumbers(self.mult_1 - self.mult_2,
                              self.mult_3 + self.mult_4)

    def __str__(self):
        return f"{self.my_number_1:.2f} + {self.my_number_2:.2f}i"


a = ComplexNumbers(-1.24, 0.5)
b = ComplexNumbers(2.1, -0.1)

print(a + b)
print(a * b)
