from csv import DictReader

from set import DATA_ITEMS


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
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        with open(cls.items_path, 'r', encoding='windows-1251') as csv:
            data = DictReader(csv)
            for row in data:
                print(row['name'], row['price'], row['quantity'])

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
