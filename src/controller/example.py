from src.domain.business_logic_example import BusinessLogicExample
from werkzeug.local import LocalProxy


def __to_validation(request: LocalProxy):
    if not ('bool' in request.json):
        raise ValueError('Specify key bool in Body')

    if not ('number' in request.json):
        raise ValueError('Specify key number in Body')

def __get_number_by_request(request: LocalProxy):
    if 'number' in request.json:
        number = int(request.json['number'])
    else:
        number = 500

    return number

def __get_bool_data_by_request(request: LocalProxy):
    if 'bool' in request.json:
        data = request.json['bool'].lower()
        if data in ['true', 't', 'yes', 'y', '1']:
            bool = True
        else:
            bool = False
    else:
        bool = False

    return bool

def run(request):
    # TO Validations
    __to_validation(request)

    # Set variable to input functions
    number = __get_number_by_request(request)
    bool = __get_bool_data_by_request(request)

    # Execute function to process a business logic
    result = BusinessLogicExample.process(number=number, bool=bool)

    response = {
        'status': True,
        'data': result,
    }

    return response
