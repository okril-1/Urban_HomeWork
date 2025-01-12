class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            return file.read().strip()

    def add(self, *products):
        with open(self.__file_name, 'a') as file:
            for product in products:
                if self.__check_product(product):
                    file.write(f'{product}\n')
                else:
                    print(f'Продукт {product.name} уже был в магазине, его общий вес теперь равен {product.weight + self.__get_product_weight(product)}')

    def __check_product(self, product):
        with open(self.__file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith(product.name) and line.endswith(product.category):
                    return False
            return True

    def __get_product_weight(self, product):
        with open(self.__file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith(product.name) and line.endswith(product.category):
                    return float(line.split(', ')[1])
        return 0

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())