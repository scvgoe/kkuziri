from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager 

import markdown

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

# jinja2 function add
# markdown fucntion call in jinja2
app.jinja_env.globals.update(markdown=markdown.markdown)

from views import *
