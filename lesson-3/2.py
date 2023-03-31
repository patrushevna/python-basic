"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def my_func(**kwargs):
    print(f'{user["firstname"]} {user["lastname"]} {user["year"]} '
          f'года рождения, проживает в городе {user["city"]}, '
          f'email: {user["email"]}, телефон: {user["telephone"]}')


user = {
    "firstname": "Patrushev",
    "lastname": "Nikita",
    "year": "1995",
    "city": "SPB",
    "email": "npatrushev@example.com",
    "telephone": "88005555555"
}

my_func(**user)
