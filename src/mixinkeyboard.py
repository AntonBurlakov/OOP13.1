class MixinKeyboard:
    def __init__(self):
        self.language = "EN"

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        return self

    def language(self):
        return self.language
