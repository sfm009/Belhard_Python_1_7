"""
Создайте класс RandSequence с методами, формирующими вложенную последовательность.

Определить атрибуты:

- n - длина последовательности
- sequence - последовательность

Определить методы:

- инициализатор __init__, который принимает длину последовательности n и генерирует
    случайную последовательность длиной n в атрибут sequence
- метод generate, который принимает длину последовательности n (если n не передано,
    то сгенерировать длиной self.n) и генерирует последовательность в атрибут sequence.
    Для получения некоторого рандомного числа - воспользоваться функцией
    random.randint(-n, n)
- метод print_seq, который выводит последовательность на экран
"""
from random import random


class RandSequence:

    def __init__(self, n, sequence):
        self.n = n
        self.sequence = sequence

    def generate(self, n):
        self.n = n
        self.sequence = random.randit(-self.n, self.n)

    def print_seq(self):
        print(self.sequence)

new_obj = RandSequence()
