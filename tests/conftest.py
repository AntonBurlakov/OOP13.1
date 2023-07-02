import pytest

from src.item import Item


@pytest.fixture
def item():
    return Item("Ноутбук", 20000, 5)


