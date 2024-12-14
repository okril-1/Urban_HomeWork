class House:
    def __init__(self, name, number_of_floors):
        self.name = name  # Название дома
        self.number_of_floors = number_of_floors  # Количество этажей

    def __len__(self):
        # Возвращаем количество этажей
        return self.number_of_floors

    def __str__(self):
        # Возвращаем строку с информацией о доме
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

# Пример выполняемого кода
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)  # Вывод: Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Вывод: Название: ЖК Акация, кол-во этажей: 20

# __len__
print(len(h1))  # Вывод: 10
print(len(h2))  # Вывод: 20