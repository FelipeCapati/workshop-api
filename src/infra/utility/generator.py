from src.infra.utility.environment import EnvironmentValiables
from datetime import datetime
from random import uniform
import pandas as pd
import os

class Generator:
    def __init__(self):
        pass

    @staticmethod
    def radom_string_number() -> str:
        now = str(round(datetime.timestamp(datetime.now())))
        random_variable = str(int(uniform(0, 1000000)))

        return now + random_variable

    @staticmethod
    def temp_folder() -> bool:
        dir_name = EnvironmentValiables.get_upload_folder()
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)

        return True

    @staticmethod
    def df_from_dict(dictionary: dict, csv_filename: str) -> str:
        df = pd.DataFrame.from_dict(dictionary)
        random_string = Generator.radom_string_number()
        csv_path = './csv/' + csv_filename + random_string + '.csv'
        df.to_csv(csv_path, sep='&', index=False)

        return csv_path
