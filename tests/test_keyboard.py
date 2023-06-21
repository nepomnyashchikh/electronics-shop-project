import pytest

from src.mixin_lang import MixinLang
from src.item import Item
from src.keyboard import Keyboard


@pytest.fixture
def make_keyboard():
    return Keyboard('abrakadabra', 37000, 2)


def test_init(make_keyboard):
    keyboard = make_keyboard
    assert keyboard.name == "abrakadabra"
    assert keyboard.price == 37000
    assert keyboard.quantity == 2
    assert keyboard.language == 'EN'
    assert isinstance(keyboard, Item)
    assert isinstance(keyboard, MixinLang)


def test_mixin(make_keyboard):
    keyboard = make_keyboard
    assert keyboard.language == 'EN'
    keyboard.change_lang()
    assert keyboard.language == 'RU'
    keyboard.change_lang()
    assert keyboard.language == 'EN'
    keyboard.change_lang().change_lang()
    assert keyboard.language == 'EN'

    with pytest.raises(AttributeError):
        keyboard.language = 'UK'