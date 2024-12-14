class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.floors != other.floors
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, int):
            self.floors += value
            return self
        return NotImplemented

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

# Пример выполнения кода
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)  # Вывод информации о первом доме
print(h2)  # Вывод информации о втором доме

print(h1 == h2)  # Сравнение по количеству этажей (__eq__)

h1 = h1 + 10  # Увеличение этажей первого дома на 10 (__add__)
print(h1)  # Вывод информации о первом доме после увеличения
print(h1 == h2)  # Сравнение по количеству этажей (__eq__)

h1 += 10  # Увеличение этажей первого дома на 10 с помощью __iadd__
print(h1)  # Вывод информации о первом доме после увеличения

h2 = 10 + h2  # Увеличение этажей второго дома на 10 с помощью __radd__
print(h2)  # Вывод информации о втором доме после увеличения

print(h1 > h2)  # Сравнение по количеству этажей (__gt__)
print(h1 >= h2)  # Сравнение по количеству этажей (__ge__)
print(h1 < h2)  # Сравнение по количеству этажей (__lt__)
print(h1 <= h2)  # Сравнение по количеству этажей (__le__)
print(h1 != h2)  # Сравнение по количеству этажей (__ne__)