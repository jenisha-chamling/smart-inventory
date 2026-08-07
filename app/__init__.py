from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect, generate_csrf

from .config import Config


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
csrf = CSRFProtect()


@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return db.session.get(User, int(user_id))


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)

    # Flask-Login Configuration
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please login to continue."
    login_manager.login_message_category = "warning"

    # Register Blueprints

    # Main Blueprint
    from .routes import main
    app.register_blueprint(main)

    # Authentication Blueprint
    from .auth import auth
    app.register_blueprint(auth)

    # Dashboard Blueprint
    from .dashboard import dashboard
    app.register_blueprint(dashboard)

    #Products Blueprint
    from .products import products
    app.register_blueprint(products)

    #Suppliers Blueprint
    from .suppliers import suppliers
    app.register_blueprint(suppliers)

    @app.context_processor
    def inject_csrf_token():
        return dict(csrf_token=generate_csrf)

    return app