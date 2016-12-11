from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager 
from config import *

app = Flask(__name__)

try:
    app.config.from_envvar('RUN_OPT')
except:
    app.config.from_object('config')

# db = SQLAlchemy(app, session_options={'autocommit': True})
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from utils import Auth
auth = Auth()

import markdown

# jinja2 function add
app.jinja_env.globals.update(markdown=lambda text: markdown.markdown(text, extensions=['markdown.extensions.nl2br']))
app.jinja_env.globals.update(Auth=auth)

from views import *
