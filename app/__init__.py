from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .config import Config
import os 

rootdir = os.getcwd() 
print(rootdir)
for subdir, dirs, files in os.walk(rootdir + '/Users/brandon/info3180-lab4'): 
    for file in files: 
        print(os.path.join(subdir, file))
# import flask migrate here

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
# Instantiate Flask-Migrate library here

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import views

from flask_migrate import Migrate
migrate = Migrate(app,db)