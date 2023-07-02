"""Здесь надо написать тесты с использованием pytest для модуля item."""


def test_item(item):
    assert item.price == 20000
    assert item.name == "Ноутбук"
    assert item.quantity == 5


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 100000


def test_apply_discount(item):
    item.apply_discount()
    assert item.price == 20000.0
