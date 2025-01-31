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
import random


class RandSequence:
    n: int
    sequence = []

    def __init__(self, n):
        self.n = n
        self.sequence = [random.uniform(-self.n, self.n) for i in range(self.n)]

    def generate(self, n=None):
        if not n:
            n = self.n
        self.sequence = [random.uniform(-n, n) for i in range(n)]

    @classmethod
    def print_seq(cls, sequence):
        print(sequence)


new_obj = RandSequence(5)
print(new_obj)
