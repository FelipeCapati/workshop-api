
from flask import jsonify, request
from functools import wraps
from src.infra.utility.environment import EnvironmentValiables

def check_auth(username, password):
    return username == EnvironmentValiables.get_basic_auth_user() and password == EnvironmentValiables.get_basic_auth_password()

def authenticate():
    response = {
        'status': False,
        'message': 'Unauthorized'
    }
    return jsonify(response), 401

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated