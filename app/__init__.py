from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate
import os 

app = Flask(__name__)
app.config.from_object(Config)

# Set the upload folder here
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Now you can import views that may rely on app, db, or login_manager
from app import views
