"""
Задание 1.
Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:

    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

        self.day = Date.extraction(day_month_year)[0]
        self.month = Date.extraction(day_month_year)[1]
        self.year = Date.extraction(day_month_year)[2]

        Date.validation(self.day, self.month, self.year)

    @classmethod
    def extraction(cls, day_month_year):
        return [int(i) for i in day_month_year.split('_')]

    @staticmethod
    def validation(day, month, year):
        if day < 0 or day > 31:
            return 'Не верный формат дня'
        if month < 0 or month > 12:
            return 'Не верный формат месяца'
        if year < 1999 or year > 2023:
            return 'Не верный формат года'


Date('32_13_1995')
