import os


class File:
    def __init__(self):
        pass

    @staticmethod
    def is_pdf(path: str) -> bool:
        path = path.lower()
        return path.endswith('.pdf')

    @staticmethod
    def is_image(path: str) -> bool:
        return File.is_valid_format(path=path, extensions_array=['.jpg', '.jpeg', '.png'])

    @staticmethod
    def is_valid_format(path: str, extensions_array: list) -> bool:
        valid = False
        path = path.lower()
        for extension in extensions_array:
            if path.endswith(extension):
                valid = True

        return valid

    @staticmethod
    def get_filename_from_path(path_file: str) -> str:
        head_path, tail_path = os.path.split(path_file)

        return tail_path
