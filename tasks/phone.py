"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""

class Phone:
    brand = 'brand'
    model = 'model'
    issue_year = 'issue_year'

    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.mode = model
        self.issue_year = issue_year

    def __str__(self):
        print(self.brand)
        print(self.model)
        print(self.issue_year)

    @staticmethod
    def receive_call(name):
        print(f'Звонит {name}')

    def get_info(self):
        return (self.brand, self.mode, self.issue_year)
