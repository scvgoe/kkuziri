from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

try:
    app.config.from_envvar('RUN_OPT')
except:
    app.config.from_object('config')

db = SQLAlchemy(app, session_options={'autocommit': True})

bcrypt = Bcrypt(app)

from views import *
