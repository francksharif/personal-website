from flask import Flask 
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from flask_ckeditor import CKEditor

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
ckeditor = CKEditor()



def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    ckeditor.init_app(app)
    login_manager.login_view = 'auth.login'

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

    @login_manager.user_loader
    def load_user(user_id):
        return models.Admin.query.get(int(user_id))
    

    return app