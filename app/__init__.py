from flask import Flask 
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint) 

    from .project import project as project_blueprint
    app.register_blueprint(project_blueprint)

    with app.app_context():
        from . import models
    

    return app