from csv import DictReader

from set import DATA_ITEMS
from src.exp import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    items_path = DATA_ITEMS

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
        self.quantity = int(quantity)
        Item.all.append(self)

    def __repr__(self):
        return f'{self.__class__.__name__}(\'{self.__name}\', {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        raise TypeError("Unsupported operand types for +: '{}' and '{}'".format(
            self.__class__.__name__, other.__class__.__name__))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        try:
            with open(cls.items_path, 'r', encoding='windows-1251') as csv:
                data = DictReader(csv)
                for row in data:
                    cls(row['name'],
                        cls.string_to_number(row['price']),
                        cls.string_to_number(row['quantity']))

        except FileNotFoundError:
            raise FileNotFoundError("_Отсутствует файл item.csv_")
        except KeyError:
            raise InstantiateCSVError('Файл item.csv поврежден_')


    @staticmethod
    def string_to_number(decimal_string):
        return int(float(decimal_string))

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

