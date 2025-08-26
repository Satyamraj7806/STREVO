# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
from .extensions import db



login_manager = LoginManager() # Create an instance of LoginManager

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = '7030462c9768585fff83df5478c5306fbac974b804b1bc5d'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///strevo.db'
    
    db.init_app(app)
    
    
    # Initialize the login manager
    login_manager.init_app(app)
    # Set the name of the login view function
    login_manager.login_view = 'main.register_page'
    
    # This is required by Flask-Login to load a user from the session
    @login_manager.user_loader
    def load_user(user_id):
        # We need to import the User model here to avoid circular imports
        from .models import User
        return User.query.get(int(user_id))
    
    # Import your blueprints and models AFTER app and db are initialized
    from .models import User, Item
    from .routes import main # Assuming your blueprint is named 'main'

    app.register_blueprint(main)

    return app