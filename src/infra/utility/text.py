import re


class Text:
    def __init__(self):
        pass

    @staticmethod
    def remove_black_list_char_by(string: str, by: str) -> str:
        black_list = [" ", "\n", "\f", "\xa0", "\x0c", "\x00", "\xad"]
        for char in black_list:
            string = string.replace(char, by)

        return string

    @staticmethod
    def remove_white_space(string: str) -> str:
        return re.sub("\s\s+", " ", string)

    @staticmethod
    def adjuste_punctuation(string: str) -> str:
        return string.replace(" ,", ",").replace(" .", ".").replace(" ;", ";")

    @staticmethod
    def non_valid_string(string: str) -> bool:
        self = Text()
        string = self.remove_black_list_char_by(string=string, by="")
        return string == '' or not string.isprintable() or string.find("#$%") != -1

    @staticmethod
    def fit_text(string: str) -> str:
        self = Text()
        string = self.remove_black_list_char_by(string=string, by=" ")
        string = self.remove_white_space(string=string)
        string = self.adjuste_punctuation(string=string)

        return string
