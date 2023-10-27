#!/usr/bin/python3
"""Flask applications instances"""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif', '.jpeg']
app.config['UPLOAD_PATH'] = 'app/static/images'

# Flask-SQLAlchemy and Flask-Migrate initialization
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Flask-Login initialization
login = LoginManager(app)
login.login_view = 'signin'



from app import routes, models, errors
