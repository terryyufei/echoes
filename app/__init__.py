#!/usr/bin/python3
"""Flask applications instances"""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

# Flask-SQLAlchemy and Flask-Migrate initialization
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Flask-Login initialization
login = LoginManager(app)
login.login_view = 'signin'

from app import routes, models
