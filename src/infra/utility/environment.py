class EnvironmentValiables:
    def __init__(self):
        pass

    @staticmethod
    def get_system_port() -> int:
        return 9000

    @staticmethod
    def get_system_debug() -> bool:
        return False

    @staticmethod
    def get_basic_auth_user() -> str:
        return "admin"

    @staticmethod
    def get_basic_auth_password() -> str:
        return "kpmg2019"

    @staticmethod
    def get_upload_folder() -> str:
        return "./temp"
