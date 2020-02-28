from src.infra.utility.generator import Generator as Gen
import src.infra.http.server as server
import config
import os

if __name__ == '__main__':
    config.base_path = os.path.dirname(__file__)
    Gen.temp_folder()
    server.run()
