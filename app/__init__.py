# app/__init__.py

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
moment = Moment(app)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'signin'
login_manager.init_app(app)

# Load the views
from app import views

# Load the config file
app.config.from_object('config')