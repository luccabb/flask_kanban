from flask import Flask
from .models import db
from .routes import routes
from .auth import login_manager, auth
import os
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

app = Flask(__name__)

app.register_blueprint(routes)
app.register_blueprint(auth)

# updating 
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

login_manager.init_app(app)
db.init_app(app)
csrf.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()

app.run()