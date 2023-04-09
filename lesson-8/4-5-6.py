"""
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над четвертым заданием.
Разработать методы, отвечающие за приём оргтехники на
склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над пятым заданием. Р
еализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class MyWarehouseEquipment:
    tech = []
    issued = {}

    @classmethod
    def reception(cls, my_list):
        cls.tech.append(my_list.my_dict)

    @classmethod
    def issuance_to_division(cls, my_list, division):
        cls.issued = {'Тип устройства': my_list.my_dict['Тип устройства'],
                      'Модель устройства':
                      my_list.my_dict['Модель устройства'],
                      'Подразделение': division}
        print(cls.issued)


class MyOfficeEquipment:

    def __init__(self, my_type, my_model, my_quantity):
        self.my_type = my_type
        self.my_model = my_model

        try:
            if isinstance(my_quantity, int):
                self.my_quantity = my_quantity
                self.my_dict = {'Тип устройства': self.my_type,
                                'Модель устройства': self.my_model,
                                'Количество': self.my_quantity}
            else:
                raise OwnError('Количество - это число')
        except OwnError as err:
            print(err)

    def __str__(self):
        return f'{self.my_dict}'


class Printer(MyOfficeEquipment):

    def __init__(self, my_type, my_model, my_quantity, color):
        super().__init__(my_type, my_model, my_quantity)
        self.color = color  # Цветной или нет


class Scanner(MyOfficeEquipment):

    def __init__(self, my_type, my_model, my_quantity, type_scanner):
        super().__init__(my_type, my_model, my_quantity)
        self.type_scanner = type_scanner  # Струйный или лазерный


class Copier(MyOfficeEquipment):

    def __init__(self, my_type, my_model, my_quantity, copier):
        super().__init__(my_type, my_model, my_quantity)
        self.copier = copier  # двухсторонний или нет


item_1 = Printer('Принтер', 'MyQ', 100, 'цветной')
item_2 = Scanner('Сканер', 'HP', 200, 'лазерный')
item_3 = Copier('Ксерокс', 'Xerox', 300, 'двухсторонний')

MyWarehouseEquipment.reception(item_1)
MyWarehouseEquipment.reception(item_2)
MyWarehouseEquipment.reception(item_3)
MyWarehouseEquipment.issuance_to_division(item_1, 'Бухгалтерия')
