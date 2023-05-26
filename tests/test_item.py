"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest

@pytest.fixture
def class_item():
   return Item('Ноутбук', 20000, 5)

def test_init(class_item):
   item = class_item
   assert item.name == 'Ноутбук'
   assert item.price == 20000
   assert item.quantity == 5

def test_calculate_total_price(class_item):
   item = class_item
   assert item.calculate_total_price() == 100000

def test_apply_discount(class_item):
   item = class_item
   item.apply_discount()
   assert item.price == 20000






