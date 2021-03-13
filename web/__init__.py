from flask import Flask
from .models import db, mail
from .routes import routes
from .auth import login_manager, auth
import os
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from .config import config

csrf = CSRFProtect()

app = Flask(__name__)

app.register_blueprint(routes)
app.register_blueprint(auth)

# updating configs based on FLASK_ENV specified
app.config.from_object(config[os.environ.get('FLASK_ENV')])

login_manager.init_app(app)
db.init_app(app)
csrf.init_app(app)
mail.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    # db.create_all()
    pass

if __name__ == '__main__':
    app.run()