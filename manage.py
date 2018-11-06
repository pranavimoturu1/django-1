
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://flask:flask123@localhost/flask"

app._static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ContactUs/static")

db = SQLAlchemy(app)

from ContactUs.models import *

from ContactUs.views import api
app.register_blueprint(api)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()