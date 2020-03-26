# Import all Dependences
from flask import Flask
import config
from src.infra.utility.environment import EnvironmentValiables
import os


# Initialize Flask Global in config
APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC_PATH = os.path.join(APP_PATH, '../../doc/')

config.app = Flask(__name__, static_folder=PUBLIC_PATH, template_folder=PUBLIC_PATH)

# Import routes modules
import src.infra.http.routes.example
import src.infra.http.routes.doc

def run():
    # Start http server
    config.app.run(debug=EnvironmentValiables.get_system_debug(),
                   host='0.0.0.0',
                   port=EnvironmentValiables.get_system_port(),
                   threaded=True
    )
