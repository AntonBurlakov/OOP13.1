"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone


def test_item(item):
    assert item.price == 20000
    assert item.name == "Ноутбук"
    assert item.quantity == 5


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 100000


def test_apply_discount(item):
    item.apply_discount()
    assert item.price == 20000.0


def test_instantiate_from_csv(item):
    item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 9


def test_name(item):
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    assert item.name != 'СуперСмартфон'


def test_name_(item):
    item1 = item.all[0]
    assert item1.name == 'Ноутбук'


def test_string_to_number(item):
    assert item.string_to_number('5') == 5
    assert item.string_to_number('5.0') == 5

    assert item.string_to_number('5.5') == 5


def test_repr(item):
    assert repr(item) == "Item('Ноутбук', 20000, 5)"


def test_str(item):
    assert str(item) == 'Ноутбук'


def test_iphone_init():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2


def test_iphone_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_iphone_add():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
