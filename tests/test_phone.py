from src.item import Item
from src.phone import Phone
import pytest


@pytest.fixture
def class_phone():
    return Phone("iPhone 14", 120000, 5, 2)

def test_init(class_phone):
    phone = class_phone
    assert phone.name == 'iPhone 14'
    assert phone.price == 120000
    assert phone.quantity == 5

def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    assert phone1.number_of_sim == 2

def test__str__():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    # Проверяем методы
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

def test___repr__():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"