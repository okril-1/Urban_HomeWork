class Animal:
    def __init__(self, name):
        self.alive = True  # Живое
        self.fed = False   # Накормленное
        self.name = name   # Имя животного

class Plant:
    def __init__(self, name):
        self.edible = False  # Съедобность
        self.name = name     # Имя растения

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Переопределяем атрибут edible

# Создаем объекты классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Проверяем имена объектов
print(a1.name)  # Волк с Уолл-Стрит
print(p1.name)  # Цветик семицветик

# Проверяем состояние объектов
print(a1.alive)  # True
print(a2.fed)    # False

# Выполняем действия
a1.eat(p1)  # Хищник пытается съесть цветок
a2.eat(p2)  # Млекопитающее ест фрукт

# Проверяем состояние объектов после действий
print(a1.alive)  # False (погиб)
print(a2.fed)    # True (насытился)
