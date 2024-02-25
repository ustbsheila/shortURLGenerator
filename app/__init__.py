from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from .config import Config

# Create a SQLAlchemy database instance
db = SQLAlchemy()
csrf = CSRFProtect()


def create_app():
    # Create and configure the Flask app
    app = Flask(__name__)

    # Load configuration from a separate Config class
    app.config.from_object(Config)

    # Initialize the database with the Flask app
    from .models import urlmapping
    db.init_app(app)
    # Create tables in the database
    with app.app_context():
        db.create_all()

    # # Set the secret key for CSRF protection
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['WTF_CSRF_METHODS'] = []  # This is the magic

    # Import and register blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app