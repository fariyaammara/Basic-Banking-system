import os,uuid
from app import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
#from flask import jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from flask_apscheduler import APScheduler

#import os
import urllib.request
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
import calendar
import time
from datetime import datetime

app = create_app('default')
CORS(app)
scheduler = APScheduler()
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)



@manager.command
def run():
    app.run(use_reloader=True,debug=True)
if __name__ == '__main__':
	app.jinja_env.auto_reload = True
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.config['PROPAGATE_EXCEPTIONS'] = True
	app.run(host='localhost',port='5003')
	#app.run(host='172.16.234.1',port='5000',ssl_context='adhoc')