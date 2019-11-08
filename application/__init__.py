from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ('mysql+pymysql://' +
                                         getenv('MYSQL_USER') +
                                         ':' +
                                         getenv('MYSQL_PASSWORD') +
                                         '@' +
                                         getenv('MYSQL_URI') +
                                         '/' +
                                         getenv('MYSQL_DATABASE')
                                        )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '7218a9143c27c16610765205a1b21cb7'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from application import routes
