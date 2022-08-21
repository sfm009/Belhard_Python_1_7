"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5
"""


class Student:
    surname = 'фамилия'
    name = 'имя'
    group = 'номер группы'
    average_score = 'средний балл'

    def __init__(self, surname, name, group, average_score):
        self.surname = surname
        self.name = name
        self.group = group
        self.average_score = average_score

    def __eq__(self, other):
        return self.average_score == other

    def __ne__(self, other):
        return self.average_score != other

    def __lt__(self, other):
        return self.average_score < other

    def __gt__(self, other):
        return self.average_score > other

    def __le__(self, other):
        return self.average_score <= other

    def __ge__(self, other):
        return self.average_score >= other


student_list = [Student('James', 'Lebron', 23, 5.0),
                Student('Curry', 'Stephen', 30, 10.0),
                Student('Durant', 'Kevin', 7, 4.0),
                Student('Tatum', 'Jayson', 0, 8.0),
                Student('Embiid', 'Joel', 21, 9.0)]

print(student_list.sort(key=lambda x: x.average_score))
print(student_list.sort(key=lambda x: x.average_score, reverse=True))
