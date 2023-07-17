from src.keyboard import Keyboard
from src.mixinkeyboard import MixinKeyboard


def test_keyboard():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"


def test_mixin():
    mix = MixinKeyboard()
    assert str(mix.language) == "EN"
