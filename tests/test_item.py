"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


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
    assert repr(item) == "Item(Ноутбук, 20000, 5)"


def test_str(item):
    assert str(item) == 'Ноутбук'
