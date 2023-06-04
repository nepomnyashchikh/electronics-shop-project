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

def test_name():
   # Создаем класс для проверки новых методов
   item = Item('Телефон', 10000, 5)

   # Exception: Длина наименования товара превышает 10 символов.

   assert item.name == 'Телефон'

   # проверяем сеттер товар, у которого наименование менее 10 символов
   item.name = 'Смартфон'
   assert item.name == 'Смартфон'
   with pytest.raises(Exception):
     item.name = 'СуперСмартфон'

def test_instantiate_from_csv():
   # Запускаем метод вызывающий класс из файла
   Item.instantiate_from_csv()
   # Проверяем корректность работы метода, подсчетом записей
   assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

   item6 = Item.all[0]
   assert item6.name == 'Шпинат'

def test_string_to_number():
   # проверка стаческого метода, который возвращает число из числа-строки
   assert Item.string_to_number('5') == 5
   assert Item.string_to_number('5.0') == 5
   assert Item.string_to_number('5.5') == 5






