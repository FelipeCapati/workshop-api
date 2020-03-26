from flask import jsonify, request
import src.controller.example as example
import src.infra.http.auth as auth
import config

"""
@api {post} /api/v1/example Verify data input
@apiGroup Example
@apiName Verify data

@apiHeader {String} Authorization Basic auth with user and password.

@apiParam {String} bool Boolean data [True or False]
@apiParam {String} number Integer number data [-inf, +inf]

@apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        "data": "The number is less than 10 and bool is True",
        "status": true
    }
"""
@config.app.route('/api/v1/example', methods=['POST'])
@auth.requires_auth
def request_ocr_v1():
    try:
        response = example.run(request)

        return jsonify(response), 200
    except Exception as err:
        print(err)
        response = {
            'status': False,
            'error': str(err)
        }

        return jsonify(response), 500
