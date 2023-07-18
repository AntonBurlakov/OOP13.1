class MixinKeyboard:
    def __init__(self):
        self.__language = "EN"

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        return self

    @property
    def language(self):
        return self.__language
