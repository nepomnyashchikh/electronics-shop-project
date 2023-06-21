import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Нельзя складывать')
        return int(self.quantity) + int(other.quantity)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, add_name: str):
        if len(add_name) <= 10:
                self.__name = add_name

        else:
            raise Exception ("Длина наименования товара превышает 10 символов")

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        cls.all.clear()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        #dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'items.csv')
        with open(dir_path + '/items.csv', encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(num):
        """
        статический метод, возвращающий число из числа-строки
        """
        numb = float(num)
        return int(numb)
