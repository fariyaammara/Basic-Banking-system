from flask import Flask
from flask_pymongo import PyMongo
from config import config
from flask_cors import CORS

db = PyMongo()

def create_app(config_name):
    # print('config_name',config_name)
    app = Flask(__name__)
    cors = CORS(app, resources={r"*": {"origins": "*"}})

    app.config.from_object(config[config_name])
    app.app_context().push()

    db.init_app(app)
    
    #db.create_all()

    from .v1 import v1_blueprint
    app.register_blueprint(v1_blueprint, url_prefix='/api/v1')

    # Swagger ui config
    app.config.SWAGGER_UI_OPERATION_ID = True
    app.config.SWAGGER_UI_REQUEST_DURATION = True
    app.config.SWAGGER_UI_DOC_EXPANSION = 'list'

    return app

