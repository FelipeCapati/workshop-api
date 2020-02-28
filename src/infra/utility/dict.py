class Dict:
    def __init__(self):
        pass

    @staticmethod
    def generate_dict(list_keys: list, list_values: list) -> dict:
        main_dict = dict(zip(list_keys, list_values))
        return main_dict

    @staticmethod
    def load_from_dict(source_dict: dict, key: object) -> object:
        return source_dict[key]
