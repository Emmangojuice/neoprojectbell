#Factory Function 
#to intitialize the app and load 
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Initialize plugins 
    db.init_app(app)

    # Register routes 
    from .rotues import app_routes
    app.register_blueprint(app_routes)
    
    return app 
