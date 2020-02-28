from flask import send_from_directory
import config
import os

@config.app.route("/", methods=['GET'])
def index():
    return send_from_directory(os.path.abspath('./doc/'), "index.html")
