"""
Задание 4.
Реализуйте базовый класс Car.
У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).
А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} начала движение'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        return f'{self.name} повернула {direction}'

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name}: {self.speed}км/ч')


class TownCar(Car):
    max_speed = 60

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name}: {self.speed}км/ч')

        if self.speed > self.max_speed:
            return f'Скорость {self.name} превышена'


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    max_speed = 40

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name}: {self.speed}км/ч')

        if self.speed > self.max_speed:
            return f'Скорость {self.name} превышена'


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейская машина'
        else:
            return f'{self.name} не полицейская машина'


car1 = SportCar(100, 'Red', 'Audi', False)
car2 = TownCar(30, 'White', 'MB', False)
car3 = WorkCar(70, 'Grey', 'Lada', False)
car4 = PoliceCar(110, 'Blue',  'Ford', True)
car5 = PoliceCar(200, 'Brown',  'Toyota', False)

print(car3.turn('налево'))
print(f'Когда {car2.turn("направо")}, потом {car1.stop()}')
print(f'{car3.name} цвета {car3.color}')
print(f'{car4.name} полицейская? {car4.is_police}')
print(car3.show_speed())
print(car5.police())
