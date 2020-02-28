from werkzeug.local import LocalProxy


class Http:
    def __init__(self):
        pass

    @staticmethod
    def get_generic_request_form_data(request: LocalProxy, request_name: str, list_names: list, list_values: list) -> object:
        main_dict = dict(zip(list_names, list_values))
        response = None
        if request_name in request.form:
            key = request.form[request_name]
            if key in main_dict:
                response = main_dict[key]

        return response
