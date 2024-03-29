from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///librarydata.db'
app.config['SECRET_KEY'] = 'thissecret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB max-limit.

db = SQLAlchemy(app)
db.init_app(app)


login=LoginManager()
login.init_app(app)
login.login_view = 'login'

bootstrap = Bootstrap(app)

from library import routes

